"""SOL market data from CoinGecko's free (keyless) API, with a fallback.

CoinGecko's free tier is generous but aggressively rate-limits shared egress
IPs - exactly the situation a GitHub Actions runner is in. So:

  1. try CoinGecko for the rich payload (price, mcap, volume, ATH, changes),
  2. try CoinGecko again for the 90-day price chart,
  3. if either 429s or fails, fall back to DeFiLlama's keyless price feed
     (``coins.llama.fi``) so the report still has a SOL price.

The output records which path produced the numbers, so the dashboard can say so.
"""

from __future__ import annotations

import time
from typing import Any

from ..net import SourceLog, fetch

CG = "https://api.coingecko.com/api/v3"
LLAMA_COINS = "https://coins.llama.fi"


def _n(v: Any, digits: int = 2) -> float | None:
    return round(float(v), digits) if isinstance(v, (int, float)) else None


def collect_market(log: SourceLog, chart_days: int = 90) -> dict:
    out: dict[str, Any] = {"available": False, "provider": None}

    res = log.record(
        "coingecko:coins/solana",
        fetch(
            f"{CG}/coins/solana?localization=false&tickers=false"
            "&market_data=true&community_data=false&developer_data=false&sparkline=false",
            ttl=300,
            retries=2,
        ),
    )
    if res.ok and isinstance(res.data, dict):
        md = res.data.get("market_data") or {}
        out.update(
            {
                "available": True,
                "provider": "coingecko",
                "price_usd": _n((md.get("current_price") or {}).get("usd"), 4),
                "market_cap_usd": _n((md.get("market_cap") or {}).get("usd"), 0),
                "fully_diluted_usd": _n((md.get("fully_diluted_valuation") or {}).get("usd"), 0),
                "volume_24h_usd": _n((md.get("total_volume") or {}).get("usd"), 0),
                "change_24h_pct": _n(md.get("price_change_percentage_24h")),
                "change_7d_pct": _n(md.get("price_change_percentage_7d")),
                "change_30d_pct": _n(md.get("price_change_percentage_30d")),
                "change_1y_pct": _n(md.get("price_change_percentage_1y")),
                "ath_usd": _n((md.get("ath") or {}).get("usd"), 2),
                "ath_change_pct": _n((md.get("ath_change_percentage") or {}).get("usd")),
                "ath_date": (md.get("ath_date") or {}).get("usd"),
                "atl_usd": _n((md.get("atl") or {}).get("usd"), 4),
                "circulating_supply": _n(md.get("circulating_supply"), 0),
                "total_supply": _n(md.get("total_supply"), 0),
                "market_cap_rank": res.data.get("market_cap_rank"),
                "volume_to_mcap_pct": None,
            }
        )
        if out["market_cap_usd"]:
            out["volume_to_mcap_pct"] = round(100 * (out["volume_24h_usd"] or 0) / out["market_cap_usd"], 2)

    if not out["available"]:
        fb = log.record(
            "llama:prices/solana", fetch(f"{LLAMA_COINS}/prices/current/coingecko:solana", ttl=300)
        )
        coin = ((fb.data or {}).get("coins") or {}).get("coingecko:solana") if fb.ok else None
        if coin:
            out.update(
                {
                    "available": True,
                    "provider": "defillama-fallback",
                    "price_usd": _n(coin.get("price"), 4),
                    "note": "CoinGecko was rate-limited or unreachable; price from DeFiLlama's keyless feed.",
                }
            )

    # Price history. CoinGecko first; DeFiLlama batch-historical as the fallback.
    chart = log.record(
        "coingecko:market_chart",
        fetch(f"{CG}/coins/solana/market_chart?vs_currency=usd&days={chart_days}&interval=daily", ttl=900, retries=2),
    )
    if chart.ok and isinstance(chart.data, dict) and chart.data.get("prices"):
        out["price_history"] = [
            {"t": int(t / 1000), "v": round(float(v), 4)} for t, v in chart.data["prices"]
        ]
        out["volume_history"] = [
            {"t": int(t / 1000), "v": round(float(v))} for t, v in (chart.data.get("total_volumes") or [])
        ]
    else:
        out["price_history"] = _llama_price_history(log, chart_days)
        out["volume_history"] = []

    if out.get("price_history") and out.get("price_usd") is None:
        out["price_usd"] = out["price_history"][-1]["v"]
        out["available"] = True

    if out.get("price_history") and out.get("change_24h_pct") is None and len(out["price_history"]) > 1:
        first, last = out["price_history"][-2]["v"], out["price_history"][-1]["v"]
        out["change_24h_pct"] = round(100 * (last / first - 1), 2) if first else None

    return out


def _llama_price_history(log: SourceLog, days: int) -> list[dict]:
    """Daily SOL closes from DeFiLlama's keyless historical price endpoint."""
    now = int(time.time())
    stamps = [now - d * 86400 for d in range(days, -1, -7)]  # weekly resolution keeps it to one call
    body = ",".join(str(s) for s in stamps[:40])
    res = log.record(
        "llama:price_history",
        fetch(f"{LLAMA_COINS}/batchHistorical?coins=%7B%22coingecko%3Asolana%22%3A%5B{body}%5D%7D", ttl=1800),
    )
    coin = ((res.data or {}).get("coins") or {}).get("coingecko:solana") if res.ok else None
    prices = (coin or {}).get("prices") or []
    return sorted(
        ({"t": int(p["timestamp"]), "v": round(float(p["price"]), 4)} for p in prices if p.get("price")),
        key=lambda p: p["t"],
    )
