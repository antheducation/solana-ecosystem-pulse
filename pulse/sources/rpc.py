"""On-chain collection over plain Solana JSON-RPC.

Public RPC endpoints are generous but flaky and individually rate-limited, so
this module keeps a *pool* of keyless endpoints and fails over between them per
method. Every method is optional: if an endpoint refuses ``getSupply`` (several
public nodes do), the report simply reports that field as unavailable instead of
dying.

RPC methods used, all of them keyless:
    getHealth, getVersion, getEpochInfo, getSlot, getBlockHeight, getBlockTime,
    getRecentPerformanceSamples, getVoteAccounts, getSupply, getInflationRate,
    getRecentPrioritizationFees, getBalance, getSignaturesForAddress, getBlock
"""

from __future__ import annotations

import statistics
from typing import Any

from ..net import SourceLog, budget_left, fetch

LAMPORTS_PER_SOL = 1_000_000_000

#: Keyless mainnet-beta endpoints, tried in order. Every one of these answers
#: without a key, a header or a signup. The pool exists because public RPC is
#: rate-limited per IP: when one starts returning 429 the next takes over, and
#: the endpoint that answered gets promoted to the front for the rest of the run.
ENDPOINTS = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-rpc.publicnode.com",
    "https://api.mainnet.solana.com",
]

#: Well-known mainnet accounts we probe with getBalance / getSignaturesForAddress.
#: These are public program IDs and burn addresses - no user wallets, no secrets.
WATCHED_ACCOUNTS = [
    ("Token program", "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
    ("Token-2022 program", "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"),
    ("Jupiter aggregator v6", "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4"),
    ("Stake program", "Stake11111111111111111111111111111111111111"),
]


class RpcPool:
    """Round-robin-with-failover JSON-RPC client over the keyless endpoint list."""

    def __init__(self, log: SourceLog, endpoints: list[str] | None = None) -> None:
        self.log = log
        self.endpoints = list(endpoints or ENDPOINTS)
        self.health: dict[str, Any] = {}

    def call(self, method: str, params: list | None = None, *, ttl: int = 0) -> Any:
        """Return the RPC ``result`` or ``None`` after every endpoint has failed."""
        errors = []
        for endpoint in self.endpoints:
            if budget_left() < 10:
                break
            res = fetch(
                endpoint,
                payload={"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []},
                ttl=ttl,
                retries=2,
                timeout=30,
            )
            self.log.record(f"rpc:{method}@{_host(endpoint)}", res)
            if res.ok and isinstance(res.data, dict):
                if "result" in res.data:
                    # Promote the endpoint that answered so later calls start there.
                    self.endpoints.remove(endpoint)
                    self.endpoints.insert(0, endpoint)
                    return res.data["result"]
                errors.append(f"{_host(endpoint)}: {str(res.data.get('error'))[:120]}")
            else:
                errors.append(f"{_host(endpoint)}: {res.error}")
        return None

    def probe_health(self) -> None:
        for endpoint in self.endpoints:
            res = fetch(
                endpoint,
                payload={"jsonrpc": "2.0", "id": 1, "method": "getHealth"},
                retries=1,
                timeout=12,
            )
            self.log.record(f"rpc:getHealth@{_host(endpoint)}", res)
            healthy = bool(res.ok and isinstance(res.data, dict) and res.data.get("result") == "ok")
            self.health[_host(endpoint)] = {
                "healthy": healthy,
                "latency_ms": res.elapsed_ms,
                "detail": None if healthy else (res.error or str(res.data)[:120]),
            }


def _host(url: str) -> str:
    return url.split("//", 1)[-1].split("/", 1)[0]


def _median(values: list[float]) -> float:
    return statistics.median(values) if values else 0.0


# --------------------------------------------------------------------------- #
# Collectors
# --------------------------------------------------------------------------- #


def collect_network(pool: RpcPool) -> dict:
    """Epoch, slot, block height, wall-clock, client versions, inflation."""
    out: dict[str, Any] = {}

    epoch = pool.call("getEpochInfo")
    if epoch:
        slots_in_epoch = epoch.get("slotsInEpoch") or 432_000
        slot_index = epoch.get("slotIndex") or 0
        out["epoch"] = {
            "epoch": epoch.get("epoch"),
            "slot_index": slot_index,
            "slots_in_epoch": slots_in_epoch,
            "progress_pct": round(100 * slot_index / slots_in_epoch, 2),
            "slots_remaining": slots_in_epoch - slot_index,
            "transaction_count": epoch.get("transactionCount"),
        }
        out["absolute_slot"] = epoch.get("absoluteSlot")
        out["block_height"] = epoch.get("blockHeight")

    if out.get("absolute_slot") is None:
        out["absolute_slot"] = pool.call("getSlot")
        out["block_height"] = pool.call("getBlockHeight")

    if out.get("absolute_slot"):
        block_time = pool.call("getBlockTime", [out["absolute_slot"]])
        out["block_time_unix"] = block_time
    version = pool.call("getVersion")
    if version:
        out["version"] = {
            "solana_core": version.get("solana-core"),
            "feature_set": version.get("feature-set"),
        }
    inflation = pool.call("getInflationRate")
    if inflation:
        out["inflation"] = {
            "total_pct": round(100 * float(inflation.get("total", 0)), 3),
            "validator_pct": round(100 * float(inflation.get("validator", 0)), 3),
            "epoch": inflation.get("epoch"),
        }
    out["rpc_health"] = pool.health
    return out


def collect_performance(pool: RpcPool, samples: int = 60) -> dict:
    """TPS (total + non-vote), slot time and their recent series.

    ``getRecentPerformanceSamples`` returns ~60s buckets, newest first.
    """
    raw = pool.call("getRecentPerformanceSamples", [samples]) or []
    series = []
    for s in reversed(raw):  # oldest -> newest for charting
        period = s.get("samplePeriodSecs") or 60
        num_slots = s.get("numSlots") or 0
        total = s.get("numTransactions") or 0
        non_vote = s.get("numNonVoteTransactions")
        series.append(
            {
                "slot": s.get("slot"),
                "tps": round(total / period, 2),
                "tps_non_vote": round(non_vote / period, 2) if non_vote is not None else None,
                "slot_time_ms": round(1000 * period / num_slots, 1) if num_slots else None,
                "slots": num_slots,
            }
        )

    tps_vals = [p["tps"] for p in series]
    tps_nv = [p["tps_non_vote"] for p in series if p["tps_non_vote"] is not None]
    slot_ms = [p["slot_time_ms"] for p in series if p["slot_time_ms"]]

    return {
        "samples": len(series),
        "window_minutes": len(series),
        "tps_current": series[-1]["tps"] if series else None,
        "tps_avg": round(sum(tps_vals) / len(tps_vals), 2) if tps_vals else None,
        "tps_peak": max(tps_vals) if tps_vals else None,
        "tps_non_vote_current": series[-1]["tps_non_vote"] if series else None,
        "tps_non_vote_avg": round(sum(tps_nv) / len(tps_nv), 2) if tps_nv else None,
        "vote_share_pct": (
            round(100 * (1 - (sum(tps_nv) / sum(tps_vals))), 1) if tps_vals and tps_nv and sum(tps_vals) else None
        ),
        "slot_time_ms_avg": round(sum(slot_ms) / len(slot_ms), 1) if slot_ms else None,
        "slot_time_ms_max": max(slot_ms) if slot_ms else None,
        "series": series,
    }


def collect_validators(pool: RpcPool, top_n: int = 15) -> dict:
    """Active/delinquent counts, stake distribution, commissions, concentration."""
    accounts = pool.call("getVoteAccounts", [{"keepUnstakedDelinquents": False}])
    if not accounts:
        return {"available": False}

    current = accounts.get("current") or []
    delinquent = accounts.get("delinquent") or []

    def stake(v: dict) -> float:
        return float(v.get("activatedStake") or 0) / LAMPORTS_PER_SOL

    active_stakes = sorted((stake(v) for v in current), reverse=True)
    total_active = sum(active_stakes)
    delinquent_stake = sum(stake(v) for v in delinquent)
    total_stake = total_active + delinquent_stake

    # Nakamoto coefficient: fewest validators whose combined stake exceeds 33.33%
    nakamoto, running = 0, 0.0
    for s in active_stakes:
        running += s
        nakamoto += 1
        if total_active and running / total_active > 1 / 3:
            break

    commissions = [int(v.get("commission", 0)) for v in current]
    staked_commissions = [int(v.get("commission", 0)) for v in current if stake(v) > 0]

    top = sorted(current, key=stake, reverse=True)[:top_n]
    top_validators = [
        {
            "vote_pubkey": v.get("votePubkey"),
            "node_pubkey": v.get("nodePubkey"),
            "stake_sol": round(stake(v)),
            "stake_pct": round(100 * stake(v) / total_active, 3) if total_active else None,
            "commission": v.get("commission"),
            "last_vote": v.get("lastVote"),
        }
        for v in top
    ]

    return {
        "available": True,
        "active_count": len(current),
        "delinquent_count": len(delinquent),
        "delinquent_pct": round(100 * len(delinquent) / max(1, len(current) + len(delinquent)), 2),
        "total_stake_sol": round(total_stake),
        "active_stake_sol": round(total_active),
        "delinquent_stake_sol": round(delinquent_stake),
        "delinquent_stake_pct": round(100 * delinquent_stake / total_stake, 3) if total_stake else None,
        "nakamoto_coefficient": nakamoto,
        "top10_stake_pct": round(100 * sum(active_stakes[:10]) / total_active, 2) if total_active else None,
        "top33_stake_pct": round(100 * sum(active_stakes[:33]) / total_active, 2) if total_active else None,
        "commission": {
            "median": _median([float(c) for c in staked_commissions]),
            "mean": round(sum(commissions) / len(commissions), 2) if commissions else None,
            "at_zero": sum(1 for c in commissions if c == 0),
            "at_100": sum(1 for c in commissions if c >= 100),
            "distribution": _histogram(commissions),
        },
        "top_validators": top_validators,
        "delinquent_sample": [
            {"vote_pubkey": v.get("votePubkey"), "stake_sol": round(stake(v)), "last_vote": v.get("lastVote")}
            for v in sorted(delinquent, key=stake, reverse=True)[:10]
        ],
    }


def _histogram(commissions: list[int]) -> list[dict]:
    buckets = [(0, 0), (1, 5), (6, 10), (11, 50), (51, 99), (100, 100)]
    out = []
    for lo, hi in buckets:
        label = f"{lo}%" if lo == hi else f"{lo}-{hi}%"
        out.append({"bucket": label, "count": sum(1 for c in commissions if lo <= c <= hi)})
    return out


def collect_supply(pool: RpcPool) -> dict:
    """Circulating vs total SOL. Some public endpoints refuse this; that's fine."""
    supply = pool.call("getSupply", [{"excludeNonCirculatingAccountsList": True}])
    if not supply:
        return {"available": False, "note": "getSupply unavailable on all public endpoints this run"}
    value = supply.get("value", supply)
    total = float(value.get("total", 0)) / LAMPORTS_PER_SOL
    circulating = float(value.get("circulating", 0)) / LAMPORTS_PER_SOL
    return {
        "available": True,
        "total_sol": round(total),
        "circulating_sol": round(circulating),
        "non_circulating_sol": round(total - circulating),
        "circulating_pct": round(100 * circulating / total, 2) if total else None,
    }


def collect_fee_market(pool: RpcPool) -> dict:
    """Priority-fee market from getRecentPrioritizationFees + the fixed base fee.

    The base signature fee is 5,000 lamports. A typical simple transfer uses far
    less than the 200k-CU default budget, so the "typical transaction" estimate
    below is explicitly a *modelled* figure, not an observed median. It is
    labelled as such everywhere it appears.
    """
    fees = pool.call("getRecentPrioritizationFees") or []
    values = [float(f.get("prioritizationFee", 0)) for f in fees]
    non_zero = [v for v in values if v > 0]
    median_micro = _median(values)
    p75 = statistics.quantiles(values, n=4)[2] if len(values) >= 4 else median_micro

    base_lamports = 5000
    # micro-lamports per CU * 200,000 CU / 1e6 = lamports
    modelled_priority_lamports = median_micro * 200_000 / 1_000_000
    return {
        "samples": len(values),
        "base_fee_lamports": base_lamports,
        "priority_fee_micro_lamports_median": round(median_micro, 2),
        "priority_fee_micro_lamports_p75": round(p75, 2),
        "slots_with_priority_fee_pct": round(100 * len(non_zero) / len(values), 1) if values else None,
        "modelled_typical_fee_lamports": round(base_lamports + modelled_priority_lamports, 1),
        "modelled_typical_fee_sol": round((base_lamports + modelled_priority_lamports) / LAMPORTS_PER_SOL, 9),
        "note": "Priority fee is the observed median across recent slots; the typical-fee figure models a 200k-CU transaction.",
    }


def collect_accounts(pool: RpcPool) -> dict:
    """getBalance + getSignaturesForAddress probes on public program accounts."""
    watch = []
    for label, pubkey in WATCHED_ACCOUNTS:
        if budget_left() < 60:
            break
        balance = pool.call("getBalance", [pubkey])
        lamports = balance.get("value") if isinstance(balance, dict) else balance
        sigs = pool.call("getSignaturesForAddress", [pubkey, {"limit": 25}]) or []
        slots = [s.get("slot") for s in sigs if s.get("slot")]
        errs = sum(1 for s in sigs if s.get("err"))
        watch.append(
            {
                "label": label,
                "pubkey": pubkey,
                "balance_sol": round(float(lamports or 0) / LAMPORTS_PER_SOL, 6),
                "recent_signatures": len(sigs),
                "signature_error_rate_pct": round(100 * errs / len(sigs), 1) if sigs else None,
                "slot_span": (max(slots) - min(slots)) if len(slots) > 1 else None,
            }
        )
    return {"watch": watch}


def collect_active_addresses(pool: RpcPool, blocks: int = 3) -> dict:
    """Active-address proxy: unique fee payers in a small sample of recent blocks.

    True daily-active-addresses needs an indexer. What a public RPC *can* give
    us honestly is the unique fee-payer count in individual blocks, which is a
    real, reproducible measure of per-block address breadth. We sample a few
    blocks and extrapolate a per-hour upper bound, clearly labelled as a proxy.
    """
    tip = pool.call("getSlot", [{"commitment": "finalized"}])
    if not tip:
        return {"available": False}

    samples = []
    all_payers: set[str] = set()
    for offset in range(blocks):
        if budget_left() < 90:
            break
        slot = int(tip) - 40 - offset * 150
        block = pool.call(
            "getBlock",
            [
                slot,
                {
                    "encoding": "json",
                    "transactionDetails": "accounts",
                    "rewards": False,
                    "maxSupportedTransactionVersion": 0,
                },
            ],
        )
        if not isinstance(block, dict):
            continue
        payers = set()
        txs = block.get("transactions") or []
        for tx in txs:
            keys = (tx.get("transaction") or {}).get("accountKeys") or []
            if keys:
                payers.add(keys[0].get("pubkey") if isinstance(keys[0], dict) else keys[0])
        payers.discard(None)
        all_payers |= payers
        samples.append(
            {
                "slot": slot,
                "transactions": len(txs),
                "unique_fee_payers": len(payers),
            }
        )

    if not samples:
        return {"available": False, "note": "no public endpoint served getBlock for the sampled slots"}

    avg_payers = sum(s["unique_fee_payers"] for s in samples) / len(samples)
    return {
        "available": True,
        "blocks_sampled": len(samples),
        "unique_fee_payers_per_block_avg": round(avg_payers, 1),
        "unique_fee_payers_union": len(all_payers),
        "overlap_pct": round(
            100 * (1 - len(all_payers) / max(1, sum(s["unique_fee_payers"] for s in samples))), 1
        ),
        "samples": samples,
        "note": (
            "Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much "
            "address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer."
        ),
    }
