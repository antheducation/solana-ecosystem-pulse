#!/usr/bin/env python3
"""Solana Ecosystem Pulse - collect, analyse, render.

One command, no arguments needed, no packages to install, no keys to set:

    python run.py

Writes:
    data/latest.json          the full machine-readable snapshot (versioned schema)
    data/history/<stamp>.json a slim per-run snapshot for trend + anomaly baselines
    REPORT.md                 the human-readable narrative report
    docs/index.html           the self-contained interactive dashboard
    docs/data/latest.json     the same JSON, served next to the dashboard

Useful flags:
    --no-history      don't write a history snapshot (dry runs)
    --quiet           only print the summary
    --out DIR         write everything under DIR instead of the repo root
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pulse import collect, dashboard, history, report_md  # noqa: E402

BANNER = r"""
 solana-ecosystem-pulse   |  stdlib only  |  zero API keys
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the Solana ecosystem report and dashboard.")
    parser.add_argument("--out", default=None, help="output root (defaults to the repository root)")
    parser.add_argument("--no-history", action="store_true", help="skip writing a history snapshot")
    parser.add_argument("--quiet", action="store_true", help="less chatter")
    parser.add_argument("--sigma", type=float, default=3.0, help="z-score threshold for statistical anomalies")
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parent
    out_root = Path(args.out).resolve() if args.out else repo_root
    verbose = not args.quiet

    if verbose:
        print(BANNER)
        print(f"Collecting at {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")

    started = time.time()
    snapshot = collect.build_snapshot(repo_root, verbose=verbose)

    hist_dir = out_root / "data" / "history"
    if not args.no_history:
        saved = history.save(snapshot, hist_dir)
        removed = history.prune(hist_dir)
        if verbose:
            print(f"  history: wrote {saved.name}, pruned {removed} old snapshot(s), "
                  f"{len(list(hist_dir.glob('*.json')))} kept")

    data_dir = out_root / "data"
    docs_dir = out_root / "docs"
    (data_dir).mkdir(parents=True, exist_ok=True)
    (docs_dir / "data").mkdir(parents=True, exist_ok=True)

    latest = data_dir / "latest.json"
    latest.write_text(json.dumps(snapshot, indent=2, sort_keys=False), encoding="utf-8")

    report = out_root / "REPORT.md"
    report.write_text(report_md.render(snapshot), encoding="utf-8")

    page = docs_dir / "index.html"
    page.write_text(dashboard.render(snapshot), encoding="utf-8")
    shutil.copyfile(latest, docs_dir / "data" / "latest.json")
    (docs_dir / ".nojekyll").write_text("", encoding="utf-8")

    anom = snapshot.get("anomalies") or {}
    sources = (snapshot.get("collection") or {}).get("sources") or {}
    print("")
    print("-" * 66)
    print(f"  status        : {anom.get('status', '?').upper()} - {anom.get('headline', '')}")
    print(f"  findings      : {len(anom.get('findings') or [])} "
          f"({(anom.get('counts') or {}).get('critical', 0)} critical, "
          f"{(anom.get('counts') or {}).get('serious', 0)} serious)")
    print(f"  source calls  : {sources.get('ok', 0)}/{sources.get('calls', 0)} OK")
    print(f"  wall time     : {round(time.time() - started, 1)}s")
    print(f"  data/latest   : {latest.relative_to(out_root)} ({latest.stat().st_size // 1024} KB)")
    print(f"  report        : {report.relative_to(out_root)} ({report.stat().st_size // 1024} KB)")
    print(f"  dashboard     : {page.relative_to(out_root)} ({page.stat().st_size // 1024} KB)")
    print("-" * 66)

    # A run that reached zero sources is a real failure; a partial run is not.
    if sources.get("ok", 0) == 0:
        print("ERROR: no data source responded. Check network access.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
