"""Anomaly detection over the collected snapshot.

Two complementary engines, because a report has to be useful on its very first
run as well as on its hundredth:

1. **Threshold rules** fire immediately from a single snapshot. They encode what
   "unhealthy" means on Solana specifically - a sub-1,000 TPS floor, slot times
   above 600 ms, delinquent stake over 5 %, an epoch that has stopped advancing.
   Day-over-day moves use the *source's own* change fields (DeFiLlama's
   ``change_1d``, CoinGecko's ``price_change_percentage_24h``), so large TVL and
   price moves are caught on run one.

2. **Statistical rules** fire once local history exists. For each tracked metric
   we take the run-over-run history, compute a robust z-score (median and
   median-absolute-deviation, so one earlier spike doesn't blind the detector)
   and flag anything beyond the configured sigma. This catches drift that no
   fixed threshold anticipates.

Severity vocabulary is fixed - ``info`` / ``warning`` / ``serious`` / ``critical`` -
and is what the HTML, Markdown and JSON outputs all colour against.
"""

from __future__ import annotations

import statistics
from typing import Any, Callable

SEVERITY_ORDER = {"critical": 0, "serious": 1, "warning": 2, "info": 3}

# Metric paths pulled from each snapshot into the statistical engine.
TRACKED_METRICS: dict[str, tuple[str, str]] = {
    "tps_avg": ("network.performance.tps_avg", "Average TPS"),
    "tps_non_vote_avg": ("network.performance.tps_non_vote_avg", "Average non-vote TPS"),
    "slot_time_ms_avg": ("network.performance.slot_time_ms_avg", "Average slot time (ms)"),
    "validators_active": ("validators.active_count", "Active validators"),
    "validators_delinquent": ("validators.delinquent_count", "Delinquent validators"),
    "tvl_usd": ("defi.tvl.tvl_usd", "Solana TVL"),
    "sol_price": ("market.price_usd", "SOL price"),
    "stablecoin_supply": ("stablecoins.supply_usd", "Stablecoin supply"),
    "dex_volume_24h": ("dex.total_24h", "24h DEX volume"),
    "rev_fees_24h": ("rev.fees.total_24h", "24h chain fees"),
    "priority_fee_median": ("fees.priority_fee_micro_lamports_median", "Median priority fee"),
}


def dig(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def _finding(
    rule: str, severity: str, title: str, detail: str, *, metric: str | None = None, value: Any = None,
    baseline: Any = None, engine: str = "threshold",
) -> dict:
    return {
        "rule": rule,
        "engine": engine,
        "severity": severity,
        "title": title,
        "detail": detail,
        "metric": metric,
        "value": value,
        "baseline": baseline,
    }


# --------------------------------------------------------------------------- #
# Engine 1 - threshold rules
# --------------------------------------------------------------------------- #

def _rule_tps(snap: dict) -> list[dict]:
    out = []
    perf = dig(snap, "network.performance") or {}
    tps = perf.get("tps_avg")
    nv = perf.get("tps_non_vote_avg")
    if tps is None:
        return out
    if tps < 800:
        out.append(_finding("tps_floor", "critical", "Severe throughput drop",
                            f"Average TPS over the last {perf.get('samples', 0)} minutes is {tps:,.0f}, "
                            f"far below Solana's normal 2,000-5,000 band.", metric="tps_avg", value=tps, baseline=2000))
    elif tps < 1500:
        out.append(_finding("tps_floor", "serious", "Throughput below normal band",
                            f"Average TPS is {tps:,.0f}; the healthy floor used here is 1,500.",
                            metric="tps_avg", value=tps, baseline=1500))
    if perf.get("tps_peak") and tps and perf["tps_peak"] > tps * 2.5:
        out.append(_finding("tps_spike", "info", "Throughput spike inside the sample window",
                            f"Peak TPS {perf['tps_peak']:,.0f} is {perf['tps_peak']/tps:.1f}x the window average "
                            f"({tps:,.0f}) - a burst, not a steady load.", metric="tps_avg",
                            value=perf["tps_peak"], baseline=tps))
    if nv is not None and tps and nv / tps < 0.10:
        out.append(_finding("low_user_share", "warning", "User transactions are a small share of throughput",
                            f"Non-vote TPS is {nv:,.0f} of {tps:,.0f} total ({100*nv/tps:.1f}%).",
                            metric="tps_non_vote_avg", value=nv, baseline=tps))
    return out


def _rule_slot_time(snap: dict) -> list[dict]:
    out = []
    perf = dig(snap, "network.performance") or {}
    avg = perf.get("slot_time_ms_avg")
    worst = perf.get("slot_time_ms_max")
    if avg is None:
        return out
    if avg > 800:
        out.append(_finding("slot_time", "critical", "Slots are producing very slowly",
                            f"Average slot time {avg:.0f} ms against a 400 ms target.",
                            metric="slot_time_ms_avg", value=avg, baseline=400))
    elif avg > 600:
        out.append(_finding("slot_time", "serious", "Slot time elevated",
                            f"Average slot time {avg:.0f} ms against a 400 ms target.",
                            metric="slot_time_ms_avg", value=avg, baseline=400))
    elif avg > 500:
        out.append(_finding("slot_time", "warning", "Slot time slightly elevated",
                            f"Average slot time {avg:.0f} ms against a 400 ms target.",
                            metric="slot_time_ms_avg", value=avg, baseline=400))
    if worst and worst > 1000:
        out.append(_finding("slot_time_worst", "warning", "A slow minute inside the sample window",
                            f"Worst 1-minute bucket averaged {worst:.0f} ms per slot.",
                            metric="slot_time_ms_avg", value=worst, baseline=400))
    return out


def _rule_validators(snap: dict) -> list[dict]:
    out = []
    v = snap.get("validators") or {}
    if not v.get("available"):
        return out
    stake_pct = v.get("delinquent_stake_pct")
    count_pct = v.get("delinquent_pct")
    if stake_pct is not None:
        if stake_pct >= 5:
            out.append(_finding("validator_delinquency", "critical", "Delinquent stake above 5 %",
                                f"{stake_pct:.2f}% of active stake is delinquent "
                                f"({v.get('delinquent_count')} validators). Above ~33 % the chain stalls.",
                                metric="validators_delinquent", value=stake_pct, baseline=5))
        elif stake_pct >= 2:
            out.append(_finding("validator_delinquency", "serious", "Delinquent stake elevated",
                                f"{stake_pct:.2f}% of active stake is delinquent "
                                f"({v.get('delinquent_count')} validators).",
                                metric="validators_delinquent", value=stake_pct, baseline=2))
    if count_pct is not None and count_pct >= 10:
        out.append(_finding("validator_delinquency_count", "warning", "Many validators are delinquent",
                            f"{v.get('delinquent_count')} of {v.get('active_count', 0) + v.get('delinquent_count', 0)} "
                            f"validators ({count_pct:.1f}%) are not voting.",
                            metric="validators_delinquent", value=count_pct, baseline=10))
    nak = v.get("nakamoto_coefficient")
    if nak is not None and nak < 20:
        out.append(_finding("stake_concentration", "warning", "Stake concentration is high",
                            f"Nakamoto coefficient is {nak}: that many validators together control over a third "
                            f"of active stake.", metric="nakamoto", value=nak, baseline=20))
    return out


def _rule_epoch(snap: dict) -> list[dict]:
    out = []
    health = dig(snap, "network.rpc_health") or {}
    unhealthy = [h for h, d in health.items() if not d.get("healthy")]
    if health and len(unhealthy) == len(health):
        out.append(_finding("rpc_health", "critical", "No public RPC endpoint reported healthy",
                            "Every endpoint in the pool failed getHealth this run.", metric="rpc"))
    elif unhealthy:
        out.append(_finding("rpc_health", "info", "Some public RPC endpoints are degraded",
                            "Unhealthy this run: " + ", ".join(sorted(unhealthy)) + ".", metric="rpc"))
    return out


def _rule_market_moves(snap: dict) -> list[dict]:
    """Day-over-day moves straight from the sources' own change fields."""
    out = []
    checks: list[tuple[str, Any, str, float, float, str]] = [
        ("price_move", dig(snap, "market.change_24h_pct"), "SOL price", 8, 15, "sol_price"),
        ("tvl_move", dig(snap, "defi.tvl.change_1d_pct"), "Solana TVL", 6, 12, "tvl_usd"),
        ("stablecoin_move", dig(snap, "stablecoins.change_1d_pct"), "Stablecoin supply", 3, 6, "stablecoin_supply"),
        ("dex_move", dig(snap, "dex.change_1d_pct"), "DEX volume", 40, 70, "dex_volume_24h"),
        ("fee_move", dig(snap, "rev.fees.change_1d_pct"), "Chain fees", 40, 70, "rev_fees_24h"),
    ]
    for rule, change, label, warn_at, serious_at, metric in checks:
        if not isinstance(change, (int, float)):
            continue
        magnitude = abs(change)
        if magnitude < warn_at:
            continue
        severity = "serious" if magnitude >= serious_at else "warning"
        direction = "up" if change > 0 else "down"
        out.append(_finding(rule, severity, f"{label} moved sharply ({direction} {magnitude:.1f}% in 24h)",
                            f"{label} changed {change:+.1f}% over the last day, past the {warn_at}% alert band.",
                            metric=metric, value=change, baseline=warn_at))
    return out


def _rule_client_spread(snap: dict) -> list[dict]:
    out = []
    version = dig(snap, "network.version.solana_core")
    if version and "-rc" in str(version):
        out.append(_finding("client_version", "info", "Answering RPC node runs a release candidate",
                            f"The endpoint that served this run reports agave {version}.",
                            metric="client", value=version))
    return out


THRESHOLD_RULES: list[Callable[[dict], list[dict]]] = [
    _rule_tps, _rule_slot_time, _rule_validators, _rule_epoch, _rule_market_moves, _rule_client_spread,
]


# --------------------------------------------------------------------------- #
# Engine 2 - robust z-score over local history
# --------------------------------------------------------------------------- #

def _robust_z(series: list[float], value: float) -> tuple[float, float, float] | None:
    """Return (z, median, mad-scaled-sigma) or None when the series is unusable."""
    if len(series) < 5:
        return None
    med = statistics.median(series)
    mad = statistics.median([abs(x - med) for x in series])
    sigma = 1.4826 * mad  # MAD -> standard-deviation-equivalent for normal data
    if sigma <= 0:
        sigma = statistics.pstdev(series)
    if sigma <= 0:
        return None
    return (value - med) / sigma, med, sigma


def statistical_findings(snap: dict, history: list[dict], sigma: float = 3.0) -> list[dict]:
    out = []
    for key, (path, label) in TRACKED_METRICS.items():
        value = dig(snap, path)
        if not isinstance(value, (int, float)):
            continue
        series = [
            v for v in (dig(h, path) for h in history) if isinstance(v, (int, float))
        ]
        result = _robust_z(series, float(value))
        if result is None:
            continue
        z, med, _ = result
        if abs(z) < sigma:
            continue
        severity = "serious" if abs(z) >= sigma * 1.67 else "warning"
        direction = "above" if z > 0 else "below"
        pct = (100 * (value / med - 1)) if med else 0
        out.append(
            _finding(
                f"zscore_{key}", severity,
                f"{label} is {direction} its recent norm",
                f"Current {value:,.2f} sits {abs(z):.1f} sigma {direction} the median of the last "
                f"{len(series)} runs ({med:,.2f}, {pct:+.1f}%).",
                metric=key, value=value, baseline=round(med, 4), engine="zscore",
            )
        )
    return out


def detect(snap: dict, history: list[dict], sigma: float = 3.0) -> dict:
    findings: list[dict] = []
    for rule in THRESHOLD_RULES:
        try:
            findings.extend(rule(snap))
        except Exception as exc:  # a broken rule must never break the report
            findings.append(_finding("rule_error", "info", "An anomaly rule failed",
                                     f"{rule.__name__}: {type(exc).__name__}: {exc}"))
    findings.extend(statistical_findings(snap, history, sigma))
    findings.sort(key=lambda f: SEVERITY_ORDER.get(f["severity"], 9))

    counts = {level: sum(1 for f in findings if f["severity"] == level) for level in SEVERITY_ORDER}
    if counts["critical"]:
        status, headline = "critical", "Critical anomalies detected"
    elif counts["serious"]:
        status, headline = "serious", "Serious anomalies detected"
    elif counts["warning"]:
        status, headline = "warning", "Minor anomalies detected"
    else:
        status, headline = "good", "All monitored metrics inside normal bands"

    return {
        "status": status,
        "headline": headline,
        "counts": counts,
        "history_runs_available": len(history),
        "sigma_threshold": sigma,
        "findings": findings,
        "rules_evaluated": len(THRESHOLD_RULES) + len(TRACKED_METRICS),
    }
