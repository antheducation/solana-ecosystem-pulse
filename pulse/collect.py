"""Orchestration: run every collector, assemble the versioned snapshot."""

from __future__ import annotations

import platform
import time
from pathlib import Path

from . import anomalies, history
from .net import SourceLog
from .sources import coingecko, defillama, news, rpc

SCHEMA_VERSION = "1.0.0"


def _iso(ts: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))


def build_snapshot(root: Path, *, verbose: bool = True) -> dict:
    started = time.time()
    log = SourceLog()

    def step(label: str, fn, default=None):
        if verbose:
            print(f"  -> {label} ...", flush=True)
        t0 = time.time()
        try:
            value = fn()
        except Exception as exc:  # noqa: BLE001 - a failing source degrades, never crashes
            if verbose:
                print(f"     !! {label} failed: {type(exc).__name__}: {exc}", flush=True)
            return default if default is not None else {"available": False, "error": f"{type(exc).__name__}: {exc}"}
        if verbose:
            print(f"     ok ({time.time() - t0:.1f}s)", flush=True)
        return value

    pool = rpc.RpcPool(log)
    step("RPC health probe", pool.probe_health, {})

    network = step("network / epoch / version", lambda: rpc.collect_network(pool), {})
    network["performance"] = step("performance samples (TPS, slot time)", lambda: rpc.collect_performance(pool), {})
    validators = step("validators (getVoteAccounts)", lambda: rpc.collect_validators(pool), {"available": False})
    supply = step("SOL supply (getSupply)", lambda: rpc.collect_supply(pool), {"available": False})
    fees = step("fee market (getRecentPrioritizationFees)", lambda: rpc.collect_fee_market(pool), {})
    accounts = step("account probes (getBalance / getSignaturesForAddress)", lambda: rpc.collect_accounts(pool), {})
    activity = step("active-address proxy (sampled getBlock)", lambda: rpc.collect_active_addresses(pool),
                    {"available": False})

    tvl = step("DeFiLlama chain TVL", lambda: defillama.collect_tvl(log), {"available": False})
    protocols = step("DeFiLlama protocols on Solana", lambda: defillama.collect_protocols(log), {"available": False})
    stablecoins = step("DeFiLlama stablecoins", lambda: defillama.collect_stablecoins(log), {"available": False})
    dex = step("DeFiLlama DEX volume", lambda: defillama.collect_dex(log), {"available": False})
    rev = step("DeFiLlama fees / revenue (REV)", lambda: defillama.collect_rev(log), {"available": False})
    market = step("CoinGecko SOL market data", lambda: coingecko.collect_market(log), {"available": False})

    feed = step("solana.com news RSS", lambda: news.collect_news(log), {"available": False})
    releases = step("Agave releases", lambda: news.collect_releases(log), {"available": False})
    simds = step("open SIMD proposals", lambda: news.collect_simds(log), {"available": False})
    roadmap = news.load_roadmap(root / "data" / "roadmap.json")

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": _iso(started),
        "generated_at_unix": int(started),
        "generator": {
            "name": "solana-ecosystem-pulse",
            "python": platform.python_version(),
            "third_party_packages": [],
            "api_keys_required": 0,
        },
        "network": network,
        "validators": validators,
        "supply": supply,
        "fees": fees,
        "accounts": accounts,
        "activity": activity,
        "market": market,
        "defi": {"tvl": tvl, "protocols": protocols},
        "stablecoins": stablecoins,
        "dex": dex,
        "rev": rev,
        "news": {"solana_foundation": feed, "releases": releases, "simds": simds, "roadmap": roadmap},
    }

    # Derived cross-source figures - the multi-source correlation the brief asks for.
    snapshot["derived"] = _derive(snapshot)

    hist_dir = root / "data" / "history"
    past = history.load(hist_dir)
    snapshot["anomalies"] = anomalies.detect(snapshot, past)
    snapshot["deltas"] = history.deltas(snapshot, past)

    snapshot["collection"] = {
        "duration_secs": round(time.time() - started, 1),
        "sources": log.summary(),
    }
    return snapshot


def _derive(snap: dict) -> dict:
    """Numbers that only exist because two independent sources are in the same run."""
    out: dict = {}
    price = (snap.get("market") or {}).get("price_usd")
    supply = snap.get("supply") or {}
    validators = snap.get("validators") or {}
    tvl = ((snap.get("defi") or {}).get("tvl") or {}).get("tvl_usd")
    fees = snap.get("fees") or {}
    perf = (snap.get("network") or {}).get("performance") or {}
    rev24 = ((snap.get("rev") or {}).get("fees") or {}).get("total_24h")

    if price and validators.get("total_stake_sol"):
        out["staked_value_usd"] = round(price * validators["total_stake_sol"])
    if supply.get("available") and validators.get("total_stake_sol") and supply.get("total_sol"):
        out["stake_rate_pct"] = round(100 * validators["total_stake_sol"] / supply["total_sol"], 2)
    if price and fees.get("modelled_typical_fee_sol"):
        out["modelled_typical_fee_usd"] = round(price * fees["modelled_typical_fee_sol"], 6)
    if tvl and (snap.get("market") or {}).get("market_cap_usd"):
        out["tvl_to_mcap_pct"] = round(100 * tvl / snap["market"]["market_cap_usd"], 2)
    if tvl and (snap.get("stablecoins") or {}).get("supply_usd"):
        # Stablecoins are not a subset of DeFi TVL, so this ratio routinely exceeds 100%.
        # Read it as "dollars of stablecoin on the chain per dollar locked in DeFi".
        out["stablecoins_per_tvl_dollar"] = round(snap["stablecoins"]["supply_usd"] / tvl, 2)
    dex24 = (snap.get("dex") or {}).get("total_24h")
    if dex24 and tvl:
        out["dex_volume_to_tvl_ratio"] = round(dex24 / tvl, 3)
    if rev24 and perf.get("tps_non_vote_avg"):
        daily_user_txs = perf["tps_non_vote_avg"] * 86400
        out["fee_per_user_transaction_usd"] = round(rev24 / daily_user_txs, 8)
        out["estimated_daily_user_transactions"] = round(daily_user_txs)
    if rev24 and (snap.get("market") or {}).get("market_cap_usd"):
        out["annualised_fees_to_mcap_pct"] = round(100 * rev24 * 365 / snap["market"]["market_cap_usd"], 2)
    out["_note"] = "Derived figures combine two or more independent sources collected in the same run."
    return out
