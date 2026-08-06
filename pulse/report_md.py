"""Render the human-readable Markdown report."""

from __future__ import annotations

from .anomalies import dig

SEV_ICON = {"critical": "[CRITICAL]", "serious": "[SERIOUS]", "warning": "[WARNING]", "info": "[INFO]"}
STATUS_LINE = {
    "good": "**Network status: HEALTHY** - all monitored metrics inside their normal bands.",
    "warning": "**Network status: WATCH** - minor anomalies detected.",
    "serious": "**Network status: DEGRADED** - serious anomalies detected.",
    "critical": "**Network status: CRITICAL** - critical anomalies detected.",
}


def money(v, prefix: str = "$") -> str:
    if not isinstance(v, (int, float)):
        return "n/a"
    a = abs(v)
    for cut, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= cut:
            return f"{prefix}{v / cut:,.2f}{suffix}"
    return f"{prefix}{v:,.2f}"


def num(v, digits: int = 0) -> str:
    if not isinstance(v, (int, float)):
        return "n/a"
    return f"{v:,.{digits}f}"


def pct(v, digits: int = 2, signed: bool = False) -> str:
    if not isinstance(v, (int, float)):
        return "n/a"
    return f"{v:+.{digits}f}%" if signed else f"{v:.{digits}f}%"


def render(snap: dict) -> str:
    L: list[str] = []
    add = L.append

    gen = snap.get("generated_at", "unknown")
    anom = snap.get("anomalies") or {}
    market = snap.get("market") or {}
    perf = dig(snap, "network.performance") or {}
    epoch = dig(snap, "network.epoch") or {}
    val = snap.get("validators") or {}
    tvl = dig(snap, "defi.tvl") or {}
    protos = dig(snap, "defi.protocols") or {}
    stables = snap.get("stablecoins") or {}
    dex = snap.get("dex") or {}
    rev = snap.get("rev") or {}
    fees = snap.get("fees") or {}
    derived = snap.get("derived") or {}
    supply = snap.get("supply") or {}
    activity = snap.get("activity") or {}

    add("# Solana Ecosystem Pulse")
    add("")
    add(f"**Generated:** {gen} · **Schema:** `{snap.get('schema_version')}` · "
        f"**Collection time:** {dig(snap, 'collection.duration_secs')}s · "
        f"**Sources OK:** {dig(snap, 'collection.sources.ok')}/{dig(snap, 'collection.sources.calls')}")
    add("")
    add("> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; "
        "every number below carries its source in [Data sources](#data-sources).")
    add("")
    add(STATUS_LINE.get(anom.get("status", "good"), ""))
    add("")

    # ---------------------------------------------------------------- summary
    add("## At a glance")
    add("")
    add("| Metric | Value | 24h |")
    add("|---|---:|---:|")
    add(f"| SOL price | {money(market.get('price_usd'))} | {pct(market.get('change_24h_pct'), 2, True)} |")
    add(f"| Market cap | {money(market.get('market_cap_usd'))} | rank #{market.get('market_cap_rank', 'n/a')} |")
    add(f"| Total value locked | {money(tvl.get('tvl_usd'))} | {pct(tvl.get('change_1d_pct'), 2, True)} |")
    add(f"| Stablecoin supply | {money(stables.get('supply_usd'))} | {pct(stables.get('change_1d_pct'), 2, True)} |")
    add(f"| DEX volume (24h) | {money(dex.get('total_24h'))} | {pct(dex.get('change_1d_pct'), 2, True)} |")
    add(f"| Chain fees / REV (24h) | {money(dig(snap, 'rev.fees.total_24h'))} | "
        f"{pct(dig(snap, 'rev.fees.change_1d_pct'), 2, True)} |")
    add(f"| Non-vote TPS (1h avg) | {num(perf.get('tps_non_vote_avg'), 0)} | "
        f"peak {num(perf.get('tps_peak'), 0)} total |")
    add(f"| Active validators | {num(val.get('active_count'))} | "
        f"{num(val.get('delinquent_count'))} delinquent |")
    add(f"| Epoch {epoch.get('epoch', 'n/a')} | {pct(epoch.get('progress_pct'))} complete | "
        f"{num(epoch.get('slots_remaining'))} slots left |")
    add("")

    # ------------------------------------------------------------- anomalies
    add("## Anomaly detection")
    add("")
    counts = anom.get("counts") or {}
    add(f"{anom.get('headline', '')}. {anom.get('rules_evaluated', 0)} rules evaluated across two engines "
        f"(threshold + robust z-score over {anom.get('history_runs_available', 0)} historical runs, "
        f"sigma = {anom.get('sigma_threshold')}).")
    add("")
    add(f"Critical {counts.get('critical', 0)} · Serious {counts.get('serious', 0)} · "
        f"Warning {counts.get('warning', 0)} · Info {counts.get('info', 0)}")
    add("")
    findings = anom.get("findings") or []
    if findings:
        add("| Severity | Finding | Detail | Engine |")
        add("|---|---|---|---|")
        for f in findings:
            add(f"| {SEV_ICON.get(f['severity'], f['severity'])} | {f['title']} | {f['detail']} | `{f['engine']}` |")
    else:
        add("No findings. Every threshold rule passed and no tracked metric exceeded its z-score band.")
    add("")

    # --------------------------------------------------------------- network
    add("## Network performance")
    add("")
    add(f"- **Non-vote (user) TPS:** {num(perf.get('tps_non_vote_avg'), 1)} average over the last "
        f"{perf.get('window_minutes', 0)} minutes; {num(perf.get('tps_non_vote_current'), 1)} in the latest sample.")
    add(f"- **Total TPS:** {num(perf.get('tps_avg'), 1)} average, {num(perf.get('tps_peak'), 1)} peak. "
        f"Consensus votes account for {pct(perf.get('vote_share_pct'), 1)} of all transactions.")
    add(f"- **Slot time:** {num(perf.get('slot_time_ms_avg'), 1)} ms average "
        f"(target 400 ms), worst 1-minute bucket {num(perf.get('slot_time_ms_max'), 1)} ms.")
    add(f"- **Block height:** {num(dig(snap, 'network.block_height'))} at absolute slot "
        f"{num(dig(snap, 'network.absolute_slot'))}.")
    add(f"- **Epoch {epoch.get('epoch', 'n/a')}:** slot {num(epoch.get('slot_index'))} of "
        f"{num(epoch.get('slots_in_epoch'))} ({pct(epoch.get('progress_pct'))} complete).")
    add(f"- **Client:** agave `{dig(snap, 'network.version.solana_core')}`, feature set "
        f"`{dig(snap, 'network.version.feature_set')}`. Inflation "
        f"{pct(dig(snap, 'network.inflation.total_pct'), 3)} annualised.")
    add("")

    health = dig(snap, "network.rpc_health") or {}
    if health:
        add("**Public RPC endpoint health this run**")
        add("")
        add("| Endpoint | Healthy | Latency |")
        add("|---|:--:|---:|")
        for host, info in health.items():
            add(f"| `{host}` | {'yes' if info.get('healthy') else 'no'} | {info.get('latency_ms')} ms |")
        add("")

    # ------------------------------------------------------------ validators
    add("## Validators & stake")
    add("")
    if val.get("available"):
        add(f"- **{num(val.get('active_count'))} active** validators, "
            f"**{num(val.get('delinquent_count'))} delinquent** "
            f"({pct(val.get('delinquent_pct'))} by count, {pct(val.get('delinquent_stake_pct'), 3)} by stake).")
        add(f"- **Total stake:** {num(val.get('total_stake_sol'))} SOL "
            f"({money(derived.get('staked_value_usd'))}); stake rate "
            f"{pct(derived.get('stake_rate_pct'))} of total supply.")
        add(f"- **Concentration:** Nakamoto coefficient **{val.get('nakamoto_coefficient')}**; "
            f"top 10 hold {pct(val.get('top10_stake_pct'))} and top 33 hold {pct(val.get('top33_stake_pct'))} "
            f"of active stake.")
        comm = val.get("commission") or {}
        add(f"- **Commission:** median {num(comm.get('median'), 1)}%, mean {num(comm.get('mean'), 2)}%; "
            f"{num(comm.get('at_zero'))} validators at 0% and {num(comm.get('at_100'))} at 100%.")
        add("")
        add("### Top validators by stake")
        add("")
        add("| # | Vote account | Stake (SOL) | Share | Commission |")
        add("|--:|---|--:|--:|--:|")
        for i, v in enumerate((val.get("top_validators") or [])[:10], start=1):
            add(f"| {i} | `{v['vote_pubkey']}` | {num(v['stake_sol'])} | {pct(v['stake_pct'], 3)} | "
                f"{v['commission']}% |")
    else:
        add("Validator data was unavailable from every public endpoint on this run.")
    add("")

    # ----------------------------------------------------------------- money
    add("## Economics")
    add("")
    add(f"- **SOL:** {money(market.get('price_usd'))} "
        f"({pct(market.get('change_24h_pct'), 2, True)} 24h, {pct(market.get('change_7d_pct'), 2, True)} 7d, "
        f"{pct(market.get('change_30d_pct'), 2, True)} 30d). "
        f"Market cap {money(market.get('market_cap_usd'))}, 24h volume {money(market.get('volume_24h_usd'))} "
        f"({pct(market.get('volume_to_mcap_pct'))} of cap). Price source: `{market.get('provider')}`.")
    add(f"- **TVL:** {money(tvl.get('tvl_usd'))} across {num(protos.get('protocols_tracked'))} protocols - "
        f"rank #{tvl.get('chain_rank_by_tvl', 'n/a')} of {num(tvl.get('chains_tracked'))} chains, "
        f"{pct(tvl.get('share_of_all_chain_tvl_pct'))} of all tracked chain TVL. "
        f"{pct(tvl.get('change_7d_pct'), 2, True)} over 7d, {pct(tvl.get('pct_from_ath'), 1, True)} from its ATH.")
    add(f"- **Stablecoins:** {money(stables.get('supply_usd'))} circulating on Solana "
        f"({pct(stables.get('change_7d_pct'), 2, True)} 7d) - "
        f"${num(derived.get('stablecoins_per_tvl_dollar'), 2)} of stablecoin per dollar locked in DeFi "
        f"(stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).")
    add(f"- **DEX volume:** {money(dex.get('total_24h'))} in 24h, {money(dex.get('total_7d'))} over 7d "
        f"across {num(dex.get('protocols_tracked'))} venues. Volume/TVL turnover "
        f"{num(derived.get('dex_volume_to_tvl_ratio'), 3)}x per day.")
    add(f"- **REV (chain fees):** {money(dig(snap, 'rev.fees.total_24h'))} in 24h, "
        f"{money(dig(snap, 'rev.fees.total_30d'))} over 30d. Retained chain revenue "
        f"{money(dig(snap, 'rev.revenue.total_24h'))} ({pct(rev.get('revenue_share_pct'), 1)} of fees). "
        f"Annualised fees are {pct(derived.get('annualised_fees_to_mcap_pct'))} of market cap.")
    add(f"- **Transaction fees:** base fee {num(fees.get('base_fee_lamports'))} lamports; median priority fee "
        f"{num(fees.get('priority_fee_micro_lamports_median'), 2)} micro-lamports/CU across "
        f"{num(fees.get('samples'))} recent slots ({pct(fees.get('slots_with_priority_fee_pct'), 1)} of slots "
        f"carried one). A modelled 200k-CU transaction costs "
        f"{num(fees.get('modelled_typical_fee_sol'), 9)} SOL "
        f"(~{money(derived.get('modelled_typical_fee_usd'))}).")
    if supply.get("available"):
        add(f"- **Supply:** {num(supply.get('circulating_sol'))} SOL circulating of "
            f"{num(supply.get('total_sol'))} total ({pct(supply.get('circulating_pct'))}).")
    add("")

    # ------------------------------------------------------------- ecosystem
    add("## Ecosystem")
    add("")
    if protos.get("available"):
        add("### Top protocols by TVL on Solana")
        add("")
        add("| # | Protocol | Category | TVL | 1d | 7d |")
        add("|--:|---|---|--:|--:|--:|")
        for i, p in enumerate((protos.get("top") or [])[:12], start=1):
            add(f"| {i} | {p['name']} | {p['category']} | {money(p['tvl_usd'])} | "
                f"{pct(p.get('change_1d_pct'), 1, True)} | {pct(p.get('change_7d_pct'), 1, True)} |")
        add("")
        add(f"The top five protocols hold {pct(protos.get('top5_share_pct'), 1)} of Solana's tracked TVL. "
            f"Summed across all {num(protos.get('protocols_tracked'))} protocols the total is "
            f"{money(protos.get('tvl_sum_usd'))}. {protos.get('tvl_sum_note', '')}")
        add("")
        add("**TVL by category:** " + " · ".join(
            f"{c['category']} {pct(c['share_pct'], 1)}" for c in (protos.get("categories") or [])[:6]
        ))
        add("")
        ta = protos.get("tokenized_assets") or {}
        add(f"### Tokenised assets")
        add("")
        add(f"{money(ta.get('tvl_usd'))} of tokenised real-world assets and equities are locked on Solana - "
            f"{pct(ta.get('share_of_solana_tvl_pct'), 3)} of chain TVL.")
        if ta.get("protocols"):
            add("")
            for p in ta["protocols"][:5]:
                add(f"- {p['name']} ({p['category']}): {money(p['tvl_usd'])}")
        add("")
        add(f"*{ta.get('note', '')}*")
        add("")

    if activity.get("available"):
        add("### Address activity (proxy)")
        add("")
        add(f"Across {activity.get('blocks_sampled')} sampled blocks, an average of "
            f"**{num(activity.get('unique_fee_payers_per_block_avg'), 1)} unique fee payers** signed per block "
            f"({num(activity.get('unique_fee_payers_union'))} distinct addresses in the union, "
            f"{pct(activity.get('overlap_pct'), 1)} overlap between blocks).")
        add("")
        add(f"*{activity.get('note', '')}*")
        add("")

    # ------------------------------------------------------------------ news
    add("## News, releases & upcoming upgrades")
    add("")
    feed = dig(snap, "news.solana_foundation") or {}
    if feed.get("items"):
        add("### Solana Foundation news")
        add("")
        for item in feed["items"][:5]:
            add(f"- [{item['title']}]({item['url']}) - {item.get('published', '')}")
        add("")
    releases = dig(snap, "news.releases") or {}
    if releases.get("releases"):
        add("### Validator client releases (Agave)")
        add("")
        add("| Tag | Published | Channel |")
        add("|---|---|---|")
        for r in releases["releases"][:5]:
            add(f"| [{r['tag']}]({r['url']}) | {r.get('published', '')[:10]} | "
                f"{'pre-release' if r['prerelease'] else 'stable'} |")
        add("")
    simds = dig(snap, "news.simds") or {}
    if simds.get("open_proposals"):
        add("### Open SIMD proposals (live from the SIMD repository)")
        add("")
        for s in simds["open_proposals"][:8]:
            tag = f"{s['simd']}: " if s.get("simd") else ""
            add(f"- [{tag}{s['title']}]({s['url']}) - updated {s.get('updated', '')[:10]}")
        add("")
    roadmap = dig(snap, "news.roadmap") or {}
    if roadmap.get("milestones"):
        add(f"### Tracked milestones (curated list, last reviewed {roadmap.get('last_reviewed', 'unknown')})")
        add("")
        add("| Milestone | Status | What it changes |")
        add("|---|---|---|")
        for m in roadmap["milestones"]:
            add(f"| **{m['name']}** | {m['status']} | {m['summary']} |")
        add("")

    # --------------------------------------------------------------- history
    add("## Trend")
    add("")
    deltas = snap.get("deltas") or {}
    if deltas.get("available") and deltas.get("windows"):
        for label, window in deltas["windows"].items():
            add(f"### Change over {label} (vs run at {window['reference_time']})")
            add("")
            add("| Metric | Then | Now | Change |")
            add("|---|--:|--:|--:|")
            for m in window["metrics"].values():
                add(f"| {m['label']} | {num(m['previous'], 2)} | {num(m['current'], 2)} | "
                    f"{pct(m['change_pct'], 2, True)} |")
            add("")
    else:
        add(deltas.get("note", "No local history yet."))
        add("")
        add("Source-provided change windows are still available above (24h / 7d / 30d on price, TVL, "
            "stablecoins, DEX volume and fees), so the report is never blind on a first run.")
        add("")

    # --------------------------------------------------------------- sources
    add("## Data sources")
    add("")
    add("| Source | What it provides | Key required |")
    add("|---|---|:--:|")
    add("| Solana JSON-RPC (public mainnet pool) | epoch, slot, block height, TPS, slot time, validators, "
        "stake, supply, priority fees, account probes, sampled blocks | no |")
    add("| DeFiLlama | chain TVL + history, per-protocol TVL, categories, tokenised assets | no |")
    add("| DeFiLlama stablecoins | stablecoin supply on Solana + history | no |")
    add("| DeFiLlama dexs / fees | DEX volume, chain fees, chain revenue | no |")
    add("| CoinGecko free API | SOL price, market cap, volume, ATH, 90d chart | no |")
    add("| coins.llama.fi | price fallback when CoinGecko rate-limits | no |")
    add("| solana.com news RSS | ecosystem and community news | no |")
    add("| GitHub API (anza-xyz/agave) | validator client releases | no |")
    add("| GitHub API (solana-improvement-documents) | open SIMD proposals | no |")
    add("")
    sources = dig(snap, "collection.sources") or {}
    add(f"This run made {sources.get('calls', 0)} HTTP calls ({sources.get('ok', 0)} succeeded, "
        f"{sources.get('failed', 0)} failed) in {round((sources.get('total_ms') or 0) / 1000, 1)}s of wall time.")
    failed = [e for e in (sources.get("detail") or []) if not e["ok"]]
    if failed:
        add("")
        add("<details><summary>Failed calls this run (the report degrades, it does not break)</summary>")
        add("")
        for e in failed[:20]:
            add(f"- `{e['name']}` - {e['error']} ({e['attempts']} attempts)")
        add("")
        add("</details>")
    add("")
    add("---")
    add("")
    add("Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - "
        "Python standard library only, zero API keys, zero installed packages.")
    add("")
    return "\n".join(L)
