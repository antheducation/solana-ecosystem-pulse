"""Ecosystem news, releases and protocol roadmap - all from keyless feeds.

Three streams, none of which needs a key or a signup:

  * ``solana.com/news/rss.xml``  - official Solana Foundation news.
  * GitHub releases for ``anza-xyz/agave`` - what validators are actually being
    asked to run, which is the real upgrade signal.
  * Open pull requests on ``solana-foundation/solana-improvement-documents`` -
    the SIMD pipeline, i.e. what is being *proposed* right now.

The unauthenticated GitHub API allows 60 requests/hour/IP; this module makes
two. A curated ``data/roadmap.json`` carries the named milestones (Alpenglow and
friends) that no machine-readable feed publishes, with an explicit review date so
staleness is visible rather than hidden.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree

from ..net import SourceLog, fetch

SOLANA_RSS = "https://solana.com/news/rss.xml"
GH = "https://api.github.com"


def _clean(text: str | None, limit: int = 320) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit] + ("..." if len(text) > limit else "")


def collect_news(log: SourceLog, limit: int = 6) -> dict:
    res = log.record("solana.com:news_rss", fetch(SOLANA_RSS, ttl=1800, parse_json=False))
    items = []
    if res.ok and isinstance(res.data, str):
        try:
            root = ElementTree.fromstring(res.data)
            for item in root.iter("item"):
                items.append(
                    {
                        "title": _clean(item.findtext("title"), 160),
                        "url": (item.findtext("link") or "").strip(),
                        "published": (item.findtext("pubDate") or "").strip(),
                        "summary": _clean(item.findtext("description")),
                    }
                )
                if len(items) >= limit:
                    break
        except ElementTree.ParseError as exc:
            return {"available": False, "error": f"RSS parse error: {exc}"}
    return {"available": bool(items), "source": SOLANA_RSS, "items": items}


def collect_releases(log: SourceLog, limit: int = 5) -> dict:
    res = log.record(
        "github:agave_releases", fetch(f"{GH}/repos/anza-xyz/agave/releases?per_page={limit}", ttl=1800)
    )
    if not res.ok or not isinstance(res.data, list):
        return {"available": False, "error": res.error}
    releases = [
        {
            "tag": r.get("tag_name"),
            "name": _clean(r.get("name"), 120),
            "published": r.get("published_at"),
            "prerelease": bool(r.get("prerelease")),
            "url": r.get("html_url"),
            "notes": _clean(r.get("body"), 400),
        }
        for r in res.data
    ]
    stable = next((r for r in releases if not r["prerelease"]), None)
    return {
        "available": True,
        "source": "https://github.com/anza-xyz/agave/releases",
        "latest_stable": stable,
        "releases": releases,
    }


def collect_simds(log: SourceLog, limit: int = 8) -> dict:
    res = log.record(
        "github:simd_prs",
        fetch(
            f"{GH}/repos/solana-foundation/solana-improvement-documents/pulls"
            f"?state=open&per_page={limit}&sort=updated&direction=desc",
            ttl=1800,
        ),
    )
    if not res.ok or not isinstance(res.data, list):
        return {"available": False, "error": res.error}
    simds = []
    for pr in res.data:
        title = _clean(pr.get("title"), 160)
        match = re.search(r"SIMD[- ]?(\d{3,4})", title, re.I)
        simds.append(
            {
                "number": pr.get("number"),
                "simd": f"SIMD-{match.group(1)}" if match else None,
                "title": title,
                "url": pr.get("html_url"),
                "updated": pr.get("updated_at"),
                "labels": [lbl.get("name") for lbl in (pr.get("labels") or [])],
            }
        )
    return {
        "available": True,
        "source": "https://github.com/solana-foundation/solana-improvement-documents/pulls",
        "open_proposals": simds,
    }


def load_roadmap(path: Path) -> dict:
    """Curated milestone list. Dated, so a stale entry is obvious in the report."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {"available": False, "error": str(exc), "milestones": []}
