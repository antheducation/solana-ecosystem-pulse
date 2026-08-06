"""HTTP plumbing: stdlib-only fetching with caching, retry/backoff and honesty.

Every network call in this project goes through here. Nothing else imports
urllib. That gives us one place to enforce:

  * a polite User-Agent and a hard timeout,
  * an on-disk response cache with a per-call TTL (so re-running the collector
    during development does not hammer a public endpoint),
  * exponential backoff with jitter, and respect for ``Retry-After`` on 429,
  * gzip transparency,
  * a structured result so a failing source degrades the report instead of
    crashing it.

No API keys. No third-party packages.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import random
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

USER_AGENT = "solana-ecosystem-pulse/1.0 (+https://github.com/antheducation/solana-ecosystem-pulse)"
DEFAULT_TIMEOUT = float(os.environ.get("PULSE_HTTP_TIMEOUT", "45"))
DEFAULT_TTL = int(os.environ.get("PULSE_CACHE_TTL", "0"))  # 0 = always refetch
CACHE_DIR = Path(os.environ.get("PULSE_CACHE_DIR", ".cache"))

# Wall-clock budget for the whole run. Public endpoints occasionally hang; the
# collector must still produce a report.
_started = time.monotonic()
RUN_BUDGET_SECS = float(os.environ.get("PULSE_RUN_BUDGET", "900"))


def budget_left() -> float:
    return RUN_BUDGET_SECS - (time.monotonic() - _started)


@dataclass
class FetchResult:
    """The outcome of one network call, successful or not."""

    ok: bool
    url: str
    data: Any = None
    error: str | None = None
    from_cache: bool = False
    elapsed_ms: int = 0
    status: int | None = None
    attempts: int = 1

    def unwrap(self, default: Any = None) -> Any:
        return self.data if self.ok else default


@dataclass
class SourceLog:
    """Collects one FetchResult per call so the report can show its own plumbing."""

    entries: list[dict] = field(default_factory=list)

    def record(self, name: str, res: FetchResult) -> FetchResult:
        self.entries.append(
            {
                "name": name,
                "url": _redact(res.url),
                "ok": res.ok,
                "status": res.status,
                "elapsed_ms": res.elapsed_ms,
                "attempts": res.attempts,
                "from_cache": res.from_cache,
                "error": res.error,
            }
        )
        return res

    def summary(self) -> dict:
        ok = sum(1 for e in self.entries if e["ok"])
        return {
            "calls": len(self.entries),
            "ok": ok,
            "failed": len(self.entries) - ok,
            "total_ms": sum(e["elapsed_ms"] for e in self.entries),
            "detail": self.entries,
        }


def _redact(url: str) -> str:
    """Belt-and-braces: this project uses no keys, but never echo a query secret."""
    for marker in ("api_key=", "apikey=", "token=", "key="):
        idx = url.lower().find(marker)
        if idx != -1:
            return url[: idx + len(marker)] + "REDACTED"
    return url


def _cache_path(key: str) -> Path:
    return CACHE_DIR / (hashlib.sha256(key.encode()).hexdigest()[:32] + ".json")


def _cache_read(key: str, ttl: int) -> Any | None:
    if ttl <= 0:
        return None
    path = _cache_path(key)
    try:
        if not path.exists() or time.time() - path.stat().st_mtime > ttl:
            return None
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _cache_write(key: str, value: Any) -> None:
    if DEFAULT_TTL <= 0 and not os.environ.get("PULSE_CACHE_ALWAYS"):
        return
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        _cache_path(key).write_text(json.dumps(value), encoding="utf-8")
    except (OSError, TypeError, ValueError):
        pass


def _read_body(resp) -> bytes:
    raw = resp.read()
    if resp.headers.get("Content-Encoding", "").lower() == "gzip":
        raw = gzip.decompress(raw)
    return raw


def fetch(
    url: str,
    *,
    payload: dict | None = None,
    ttl: int | None = None,
    retries: int = 3,
    timeout: float = DEFAULT_TIMEOUT,
    parse_json: bool = True,
    headers: dict[str, str] | None = None,
) -> FetchResult:
    """GET (or POST when ``payload`` is given) with cache, retry and backoff."""

    ttl = DEFAULT_TTL if ttl is None else ttl
    cache_key = url + ("|" + json.dumps(payload, sort_keys=True) if payload else "")

    cached = _cache_read(cache_key, ttl)
    if cached is not None:
        return FetchResult(ok=True, url=url, data=cached, from_cache=True, status=200)

    req_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/xml, */*",
        "Accept-Encoding": "gzip",
    }
    if payload is not None:
        req_headers["Content-Type"] = "application/json"
    if headers:
        req_headers.update(headers)

    body = json.dumps(payload).encode() if payload is not None else None
    last_error = "unknown error"
    last_status: int | None = None
    started = time.time()

    for attempt in range(1, retries + 1):
        if budget_left() < 5:
            last_error = "run budget exhausted before attempt"
            break
        try:
            req = urllib.request.Request(url, data=body, headers=req_headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = _read_body(resp)
                last_status = resp.status
                data = json.loads(raw.decode("utf-8")) if parse_json else raw.decode("utf-8", "replace")
                _cache_write(cache_key, data)
                return FetchResult(
                    ok=True,
                    url=url,
                    data=data,
                    status=resp.status,
                    elapsed_ms=int((time.time() - started) * 1000),
                    attempts=attempt,
                )
        except urllib.error.HTTPError as exc:
            last_status = exc.code
            last_error = f"HTTP {exc.code}"
            if exc.code in (400, 401, 403, 404):
                break  # not worth retrying
            wait = float(exc.headers.get("Retry-After") or 0) if exc.headers else 0.0
        except Exception as exc:  # noqa: BLE001 - any transport failure degrades the same way
            last_error = f"{type(exc).__name__}: {exc}"
            wait = 0.0

        if attempt < retries:
            sleep_for = max(wait, (2 ** (attempt - 1)) * 1.5) + random.uniform(0, 0.6)
            time.sleep(min(sleep_for, max(0.0, budget_left() - 2)))

    return FetchResult(
        ok=False,
        url=url,
        error=last_error,
        status=last_status,
        elapsed_ms=int((time.time() - started) * 1000),
        attempts=min(attempt, retries),
    )
