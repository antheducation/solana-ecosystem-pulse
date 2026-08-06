"""Off-chain economics from DeFiLlama's free, keyless API.

Endpoints used (all public, no key, no signup):

    https://api.llama.fi/v2/chains                                  chain TVL snapshot
    https://api.llama.fi/v2/historicalChainTvl/Solana               TVL history
    https://api.llama.fi/lite/protocols2                            per-protocol TVL + categories
    https://stablecoins.llama.fi/stablecoincharts/Solana            stablecoin supply history
    https://api.llama.fi/overview/dexs/solana                       DEX volume
    https://api.llama.fi/overview/fees/solana?dataType=dailyFees    chain fees
    https://api.llama.fi/overview/fees/solana?dataType=dailyRevenue chain revenue (REV input)
"""

from __future__ import annotations

from typing import Any

from ..net import SourceLog, fetch

BASE = "https://api.llama.fi"
STABLE = "https://stablecoins.llama.fi"

#: Categories DeFiLlama uses for tokenised real-world assets / equities.
RWA_CATEGORIES = {"RWA", "RWA Lending", "Tokenized Equities", "Treasury Bonds", "Basis Trading"}


def _pct_change(series: list[float], lookback: int) -> float | None:
    if len(series) <= lookback or not series[-1 - lookback]:
        return None
    return round(100 * (series[-1] / series[-1 - lookback] - 1), 2)


def collect_tvl(log: SourceLog, history_days: int = 400) -> dict:
    out: dict[str, Any] = {"available": False}

    chains = log.record("defillama:chains", fetch(f"{BASE}/v2/chains", ttl=900)).unwrap([])
    if isinstance(chains, list):
        ranked = sorted(
            (c for c in chains if isinstance(c.get("tvl"), (int, float))),
            key=lambda c: c["tvl"],
            reverse=True,
        )
        for idx, chain in enumerate(ranked, start=1):
            if chain.get("name") == "Solana":
                out["tvl_usd"] = round(chain["tvl"])
                out["chain_rank_by_tvl"] = idx
                out["chains_tracked"] = len(ranked)
                out["available"] = True
                total = sum(c["tvl"] for c in ranked)
                out["share_of_all_chain_tvl_pct"] = round(100 * chain["tvl"] / total, 2) if total else None
                break

    hist = log.record(
        "defillama:historicalChainTvl", fetch(f"{BASE}/v2/historicalChainTvl/Solana", ttl=900)
    ).unwrap([])
    if isinstance(hist, list) and hist:
        trimmed = hist[-history_days:]
        out["history"] = [{"t": int(p["date"]), "v": round(float(p["tvl"]))} for p in trimmed]
        values = [p["v"] for p in out["history"]]
        out.setdefault("tvl_usd", values[-1])
        out["available"] = True
        out["change_1d_pct"] = _pct_change(values, 1)
        out["change_7d_pct"] = _pct_change(values, 7)
        out["change_30d_pct"] = _pct_change(values, 30)
        out["ath_usd"] = max(values)
        out["pct_from_ath"] = round(100 * (values[-1] / max(values) - 1), 2) if max(values) else None
    return out


def collect_protocols(log: SourceLog, top_n: int = 12) -> dict:
    """Top Solana protocols by TVL, plus the category mix and the RWA subtotal."""
    raw = log.record("defillama:protocols", fetch(f"{BASE}/lite/protocols2", ttl=1800)).unwrap()
    protocols = (raw or {}).get("protocols") if isinstance(raw, dict) else None
    if not protocols:
        return {"available": False}

    solana = []
    for p in protocols:
        # chainTvls maps chain -> {tvl, tvlPrevDay, tvlPrevWeek, tvlPrevMonth}. Sibling keys
        # such as "Solana-borrowed" and "Solana-liquidstaking" are breakdowns of the same
        # value, so only the exact chain key is read.
        block = (p.get("chainTvls") or {}).get("Solana")
        if isinstance(block, dict):
            tvl, prev_day, prev_week = block.get("tvl"), block.get("tvlPrevDay"), block.get("tvlPrevWeek")
        elif isinstance(block, (int, float)):
            tvl, prev_day, prev_week = block, None, None
        elif "Solana" in (p.get("chains") or []) and len(p.get("chains") or []) == 1:
            tvl, prev_day, prev_week = p.get("tvl"), p.get("tvlPrevDay"), p.get("tvlPrevWeek")
        else:
            continue
        if not isinstance(tvl, (int, float)) or tvl <= 0:
            continue
        solana.append(
            {
                "name": p.get("name"),
                "category": p.get("category") or "Other",
                "tvl_usd": round(float(tvl)),
                # Chain-scoped deltas, not the protocol's all-chain delta.
                "change_1d_pct": _delta(tvl, prev_day),
                "change_7d_pct": _delta(tvl, prev_week),
            }
        )

    solana.sort(key=lambda x: x["tvl_usd"], reverse=True)
    total = sum(p["tvl_usd"] for p in solana)

    categories: dict[str, float] = {}
    for p in solana:
        categories[p["category"]] = categories.get(p["category"], 0) + p["tvl_usd"]
    top_categories = sorted(categories.items(), key=lambda kv: kv[1], reverse=True)

    rwa_total = sum(v for k, v in categories.items() if k in RWA_CATEGORIES)
    rwa_protocols = [p for p in solana if p["category"] in RWA_CATEGORIES][:8]

    return {
        "available": True,
        "protocols_tracked": len(solana),
        "tvl_sum_usd": total,
        "tvl_sum_note": (
            "The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips "
            "double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) "
            "from chain totals but reports it in each protocol's own figure. Both numbers are correct; "
            "they answer different questions."
        ),
        "top": solana[:top_n],
        "top5_share_pct": round(100 * sum(p["tvl_usd"] for p in solana[:5]) / total, 1) if total else None,
        "categories": [
            {"category": k, "tvl_usd": round(v), "share_pct": round(100 * v / total, 2) if total else None}
            for k, v in top_categories[:8]
        ],
        "tokenized_assets": {
            "tvl_usd": round(rwa_total),
            "share_of_solana_tvl_pct": round(100 * rwa_total / total, 3) if total else None,
            "protocols": rwa_protocols,
            "note": (
                "Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories "
                + ", ".join(sorted(RWA_CATEGORIES))
                + ". This is locked value, not traded volume - keyless per-venue equity volume is not published."
            ),
        },
    }


def _round(v: Any) -> float | None:
    return round(float(v), 2) if isinstance(v, (int, float)) else None


def _delta(current: Any, previous: Any) -> float | None:
    if not isinstance(current, (int, float)) or not isinstance(previous, (int, float)) or not previous:
        return None
    return round(100 * (current / previous - 1), 2)


def _overview(log: SourceLog, name: str, url: str, history_days: int) -> dict:
    data = log.record(name, fetch(url, ttl=900)).unwrap()
    if not isinstance(data, dict):
        return {"available": False}
    chart = data.get("totalDataChart") or []
    history = [{"t": int(t), "v": round(float(v))} for t, v in chart[-history_days:] if v is not None]
    values = [p["v"] for p in history]
    return {
        "available": True,
        "total_24h": _round(data.get("total24h")),
        "total_7d": _round(data.get("total7d")),
        "total_30d": _round(data.get("total30d")),
        "total_1y": _round(data.get("total1y")),
        "change_1d_pct": _round(data.get("change_1d")),
        "change_7d_pct": _round(data.get("change_7d")),
        "change_1m_pct": _round(data.get("change_1m")),
        "protocols_tracked": len(data.get("protocols") or []),
        "history": history,
        "avg_30d": round(sum(values[-30:]) / len(values[-30:])) if values else None,
    }


def collect_dex(log: SourceLog, history_days: int = 180) -> dict:
    return _overview(
        log,
        "defillama:dexs",
        f"{BASE}/overview/dexs/solana?excludeTotalDataChartBreakdown=true",
        history_days,
    )


def collect_rev(log: SourceLog, history_days: int = 180) -> dict:
    """Real Economic Value inputs: chain fees and chain revenue.

    DeFiLlama's Solana "fees" adapter aggregates fees paid across protocols on
    the chain; "revenue" is the share retained. We publish both, plus the ratio,
    and we say plainly what the number is - REV in the strictest sense (base
    fees + priority fees + Jito tips) needs a block-by-block accounting that no
    keyless endpoint exposes.
    """
    fees = _overview(
        log,
        "defillama:fees",
        f"{BASE}/overview/fees/solana?excludeTotalDataChartBreakdown=true&dataType=dailyFees",
        history_days,
    )
    revenue = _overview(
        log,
        "defillama:revenue",
        f"{BASE}/overview/fees/solana?excludeTotalDataChartBreakdown=true&dataType=dailyRevenue",
        history_days,
    )
    out = {"available": fees.get("available") or revenue.get("available"), "fees": fees, "revenue": revenue}
    if fees.get("total_24h") and revenue.get("total_24h"):
        out["revenue_share_pct"] = round(100 * revenue["total_24h"] / fees["total_24h"], 1)
    out["definition"] = (
        "REV proxy = DeFiLlama chain-level fees for Solana (24h). Chain revenue is the retained share. "
        "Strict REV (base + priority fees + MEV tips) requires block-level accounting unavailable keylessly."
    )
    return out


def collect_stablecoins(log: SourceLog, history_days: int = 400) -> dict:
    raw = log.record("defillama:stablecoins", fetch(f"{STABLE}/stablecoincharts/Solana", ttl=1800)).unwrap([])
    if not isinstance(raw, list) or not raw:
        return {"available": False}

    def usd(point: dict, key: str = "totalCirculatingUSD") -> float:
        block = point.get(key) or {}
        return float(sum(v for v in block.values() if isinstance(v, (int, float))))

    history = [{"t": int(p["date"]), "v": round(usd(p))} for p in raw[-history_days:]]
    values = [p["v"] for p in history]
    latest = raw[-1]
    pegs = latest.get("totalCirculatingUSD") or {}

    peg_label = {"peggedUSD": "USD-pegged", "peggedEUR": "EUR-pegged", "peggedVAR": "Variable peg"}
    breakdown = [
        {"peg": peg_label.get(k, k), "supply_usd": round(float(v))}
        for k, v in sorted(pegs.items(), key=lambda kv: kv[1], reverse=True)
        if isinstance(v, (int, float)) and v > 0
    ]

    return {
        "available": True,
        "supply_usd": values[-1] if values else None,
        "change_1d_pct": _pct_change(values, 1),
        "change_7d_pct": _pct_change(values, 7),
        "change_30d_pct": _pct_change(values, 30),
        "ath_usd": max(values) if values else None,
        "breakdown": breakdown,
        "history": history,
    }
