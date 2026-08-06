"""Per-run snapshot history: what makes deltas and z-scores possible.

Every run writes a *slim* snapshot (headline scalars only, no chart arrays) to
``data/history/``. Chart arrays already come from the upstream APIs with their
own history, so duplicating them per run would balloon the repo for nothing.

Retention keeps the archive useful and the repo small:
  * everything from the last 14 days,
  * then one snapshot per day for the last 180 days,
  * then one per week for ever.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from .anomalies import TRACKED_METRICS, dig

SLIM_EXTRA = {
    "epoch": "network.epoch.epoch",
    "epoch_progress_pct": "network.epoch.progress_pct",
    "block_height": "network.block_height",
    "absolute_slot": "network.absolute_slot",
    "nakamoto_coefficient": "validators.nakamoto_coefficient",
    "validators_total_stake_sol": "validators.total_stake_sol",
    "market_cap_usd": "market.market_cap_usd",
    "sol_volume_24h_usd": "market.volume_24h_usd",
    "rev_revenue_24h": "rev.revenue.total_24h",
    "tokenized_assets_usd": "defi.protocols.tokenized_assets.tvl_usd",
    "unique_fee_payers_per_block": "activity.unique_fee_payers_per_block_avg",
    "anomaly_status": "anomalies.status",
}


def slim(snapshot: dict) -> dict:
    out = {
        "generated_at": snapshot.get("generated_at"),
        "generated_at_unix": snapshot.get("generated_at_unix"),
        "schema_version": snapshot.get("schema_version"),
    }
    for key, path in {**{k: v[0] for k, v in TRACKED_METRICS.items()}, **SLIM_EXTRA}.items():
        out[key] = dig(snapshot, path)
    # Keep the nested shape the anomaly engine expects when reading history back.
    nested: dict = {"network": {"performance": {}, "epoch": {}}, "validators": {}, "defi": {"tvl": {}},
                    "market": {}, "stablecoins": {}, "dex": {}, "rev": {"fees": {}}, "fees": {}}
    for key, (path, _label) in TRACKED_METRICS.items():
        parts = path.split(".")
        cur = nested
        for part in parts[:-1]:
            cur = cur.setdefault(part, {})
        cur[parts[-1]] = out[key]
    out["_nested"] = nested
    return out


def _rehydrate(record: dict) -> dict:
    nested = record.get("_nested") or {}
    nested["generated_at"] = record.get("generated_at")
    nested["generated_at_unix"] = record.get("generated_at_unix")
    return nested


def save(snapshot: dict, history_dir: Path) -> Path:
    history_dir.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(snapshot.get("generated_at_unix") or time.time()))
    path = history_dir / f"{stamp}.json"
    path.write_text(json.dumps(slim(snapshot), indent=2, sort_keys=True), encoding="utf-8")
    return path


def load(history_dir: Path, limit: int = 400) -> list[dict]:
    """Newest-last list of rehydrated history records for the anomaly engine."""
    if not history_dir.exists():
        return []
    files = sorted(history_dir.glob("*.json"))[-limit:]
    out = []
    for f in files:
        try:
            out.append(_rehydrate(json.loads(f.read_text(encoding="utf-8"))))
        except (OSError, ValueError):
            continue
    return out


def load_raw(history_dir: Path, limit: int = 400) -> list[dict]:
    if not history_dir.exists():
        return []
    out = []
    for f in sorted(history_dir.glob("*.json"))[-limit:]:
        try:
            out.append(json.loads(f.read_text(encoding="utf-8")))
        except (OSError, ValueError):
            continue
    return out


def prune(history_dir: Path, now: float | None = None) -> int:
    """Apply the retention ladder. Returns the number of files removed."""
    if not history_dir.exists():
        return 0
    now = now or time.time()
    files = sorted(history_dir.glob("*.json"))
    keep: set[Path] = set()
    seen_day: set[str] = set()
    seen_week: set[str] = set()

    for path in reversed(files):  # newest first
        try:
            stamp = time.strptime(path.stem, "%Y%m%dT%H%M%SZ")
        except ValueError:
            keep.add(path)
            continue
        age_days = (now - time.mktime(stamp)) / 86400
        if age_days <= 14:
            keep.add(path)
        elif age_days <= 180:
            day = path.stem[:8]
            if day not in seen_day:
                seen_day.add(day)
                keep.add(path)
        else:
            week = time.strftime("%Y-%W", stamp)
            if week not in seen_week:
                seen_week.add(week)
                keep.add(path)

    removed = 0
    for path in files:
        if path not in keep:
            try:
                path.unlink()
                removed += 1
            except OSError:
                pass
    return removed


def deltas(snapshot: dict, records: list[dict]) -> dict:
    """Week-over-week (and run-over-run) deltas from the local archive."""
    if not records:
        return {"available": False, "note": "First run - no local history yet, so deltas start next run."}

    now = snapshot.get("generated_at_unix") or time.time()

    def nearest(target_age_secs: float) -> dict | None:
        target = now - target_age_secs
        candidates = [r for r in records if r.get("generated_at_unix")]
        if not candidates:
            return None
        best = min(candidates, key=lambda r: abs(r["generated_at_unix"] - target))
        # only useful if it is within 40% of the requested age
        if abs(best["generated_at_unix"] - target) > target_age_secs * 0.4 + 3600:
            return None
        return best

    out: dict = {"available": True, "runs_in_archive": len(records), "windows": {}}
    for label, secs in (("24h", 86400), ("7d", 7 * 86400), ("30d", 30 * 86400)):
        ref = nearest(secs)
        if not ref:
            continue
        window: dict = {"reference_time": ref.get("generated_at"), "metrics": {}}
        for key, (path, human) in TRACKED_METRICS.items():
            current = dig(snapshot, path)
            previous = dig(ref, path)
            if not isinstance(current, (int, float)) or not isinstance(previous, (int, float)) or not previous:
                continue
            window["metrics"][key] = {
                "label": human,
                "current": current,
                "previous": previous,
                "change_pct": round(100 * (current / previous - 1), 2),
            }
        if window["metrics"]:
            out["windows"][label] = window
    if not out["windows"]:
        out["note"] = "History exists but is younger than the shortest comparison window (24h)."
    return out
