# Solana Ecosystem Pulse

**Generated:** 2026-11-21T22:30:14Z · **Schema:** `1.0.0` · **Collection time:** 23.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.20 | +1.64% |
| Market cap | $41.55B | rank #7 |
| Total value locked | $4.63B | -2.21% |
| Stablecoin supply | $13.26B | -1.45% |
| DEX volume (24h) | $1.88B | -1.02% |
| Chain fees / REV (24h) | $8.30M | -10.84% |
| Non-vote TPS (1h avg) | 1,844 | peak 2,521 total |
| Active validators | 661 | 24 delinquent |
| Epoch 1093 | 30.31% complete | 301,040 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 134 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,256,078,315.00 sits 3.2 sigma below the median of the last 134 runs (15,973,982,918.00, -17.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,844.5 average over the last 60 minutes; 1,774.9 in the latest sample.
- **Total TPS:** 1,844.5 average, 2,520.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.4 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 450,320,891 at absolute slot 472,306,960.
- **Epoch 1093:** slot 130,960 of 432,000 (30.31% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.546% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 179 ms |
| `solana-rpc.publicnode.com` | yes | 118 ms |
| `api.mainnet.solana.com` | yes | 155 ms |

## Validators & stake

- **661 active** validators, **24 delinquent** (3.50% by count, 0.017% by stake).
- **Total stake:** 428,316,392 SOL ($30.07B); stake rate 67.14% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.86% and top 33 hold 46.49% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 220 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,043,671 | 3.980% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,329,817 | 3.813% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,620 | 2.898% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,241,724 | 2.392% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,826,793 | 2.295% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,616,961 | 2.246% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,166 | 2.157% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,985,737 | 1.865% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,985,063 | 1.631% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,774,154 | 1.582% | 5% |

## Economics

- **SOL:** $70.20 (+1.64% 24h, +0.52% 7d, -32.23% 30d). Market cap $41.55B, 24h volume $3.75B (9.03% of cap). Price source: `coingecko`.
- **TVL:** $4.63B across 343 protocols - rank #3 of 426 chains, 6.82% of all tracked chain TVL. -5.07% over 7d, -61.0% from its ATH.
- **Stablecoins:** $13.26B circulating on Solana (-6.82% 7d) - $2.86 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.88B in 24h, $11.64B over 7d across 144 venues. Volume/TVL turnover 0.407x per day.
- **REV (chain fees):** $8.30M in 24h, $295.34M over 30d. Retained chain revenue $2.83M (34.1% of fees). Annualised fees are 7.29% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,961,653 SOL circulating of 637,981,484 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +4.3% | -12.1% |
| 2 | Kamino Lend | Lending | $1.14B | +1.9% | -2.5% |
| 3 | Jupiter Lend | Lending | $956.45M | +0.4% | +1.4% |
| 4 | Raydium AMM | Dexs | $780.72M | +1.9% | -11.2% |
| 5 | Binance Staked SOL | Liquid Staking | $725.77M | +4.0% | -14.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $709.16M | +4.8% | -10.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $569.27M | +0.9% | -5.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $362.37M | +3.6% | -8.8% |
| 9 | Sentora Curator | Risk Curators | $356.22M | +0.2% | -0.3% |
| 10 | OnRe | RWA | $287.42M | -0.7% | -7.0% |
| 11 | Forward Industries SOL | Liquid Staking | $277.32M | +2.1% | -12.2% |
| 12 | CCIP | Bridge | $267.76M | -0.5% | -6.8% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.78B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.4% · Dexs 14.5% · Derivatives 5.3% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$777.03M of tokenised real-world assets and equities are locked on Solana - 6.596% of chain TVL.

- OnRe (RWA): $287.42M
- Huma (RWA): $225.75M
- Solstice (Basis Trading): $200.97M
- JupUSD (Basis Trading): $39.42M
- Solomon USDv (Basis Trading): $8.72M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19

### Tracked milestones (curated list, last reviewed 2026-08-06)

| Milestone | Status | What it changes |
|---|---|---|
| **Alpenglow** | Approved (SIMD-0326), rollout in progress | Replaces TowerBFT and Proof-of-History-based consensus with Votor + Rotor, targeting sub-second (~150 ms) finality and moving voting off-chain to cut validator vote costs. |
| **Firedancer** | Frankendancer in production; full client rolling out | Jump Crypto's independent validator client written in C. Client diversity is the point: a bug in one implementation should not stop the chain. |
| **SIMD-0096 / priority fee routing** | Live | 100% of priority fees go to the block producer rather than half being burned, changing validator economics and the shape of the fee market. |
| **SIMD-0228 (market-based emissions)** | Proposed, did not reach supermajority | Would tie SOL issuance to the staking participation rate rather than a fixed disinflation curve. Watch the SIMD queue in this report for successor proposals. |
| **Increased block limits** | Shipping incrementally | Successive raises to the per-block compute unit ceiling, lifting throughput headroom ahead of Alpenglow's consensus changes. |
| **Token Extensions (Token-2022)** | Live and expanding | Confidential transfers, transfer hooks and permanent delegates - the feature set institutional and tokenised-asset issuers ask for. |

## Trend

### Change over 24h (vs run at 2026-11-20T23:26:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,463.53 | 1,844.50 | +26.03% |
| Average non-vote TPS | 1,463.53 | 1,844.50 | +26.03% |
| Average slot time (ms) | 215.10 | 215.40 | +0.14% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 23.00 | 24.00 | +4.35% |
| Solana TVL | 4,588,288,121.00 | 4,634,019,893.00 | +1.00% |
| SOL price | 69.14 | 70.20 | +1.53% |
| Stablecoin supply | 13,451,822,446.00 | 13,256,078,315.00 | -1.46% |
| 24h DEX volume | 1,904,105,685.06 | 1,884,688,072.35 | -1.02% |
| 24h chain fees | 9,305,684.57 | 8,298,729.06 | -10.82% |

### Change over 7d (vs run at 2026-11-14T21:44:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,639.46 | 1,844.50 | -30.12% |
| Average non-vote TPS | 2,639.46 | 1,844.50 | -30.12% |
| Average slot time (ms) | 215.80 | 215.40 | -0.19% |
| Active validators | 663.00 | 661.00 | -0.30% |
| Delinquent validators | 36.00 | 24.00 | -33.33% |
| Solana TVL | 4,728,855,740.00 | 4,634,019,893.00 | -2.01% |
| SOL price | 70.58 | 70.20 | -0.54% |
| Stablecoin supply | 14,226,361,055.00 | 13,256,078,315.00 | -6.82% |
| 24h DEX volume | 1,560,618,093.20 | 1,884,688,072.35 | +20.77% |
| 24h chain fees | 9,227,351.07 | 8,298,729.06 | -10.06% |

### Change over 30d (vs run at 2026-10-22T20:55:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,984.31 | 1,844.50 | -38.19% |
| Average non-vote TPS | 2,984.31 | 1,844.50 | -38.19% |
| Average slot time (ms) | 196.40 | 215.40 | +9.67% |
| Active validators | 655.00 | 661.00 | +0.92% |
| Delinquent validators | 21.00 | 24.00 | +14.29% |
| Solana TVL | 5,883,924,131.00 | 4,634,019,893.00 | -21.24% |
| SOL price | 103.14 | 70.20 | -31.94% |
| Stablecoin supply | 16,152,572,344.00 | 13,256,078,315.00 | -17.93% |
| 24h DEX volume | 2,270,402,206.37 | 1,884,688,072.35 | -16.99% |
| 24h chain fees | 11,957,946.66 | 8,298,729.06 | -30.60% |

## Data sources

| Source | What it provides | Key required |
|---|---|:--:|
| Solana JSON-RPC (public mainnet pool) | epoch, slot, block height, TPS, slot time, validators, stake, supply, priority fees, account probes, sampled blocks | no |
| DeFiLlama | chain TVL + history, per-protocol TVL, categories, tokenised assets | no |
| DeFiLlama stablecoins | stablecoin supply on Solana + history | no |
| DeFiLlama dexs / fees | DEX volume, chain fees, chain revenue | no |
| CoinGecko free API | SOL price, market cap, volume, ATH, 90d chart | no |
| coins.llama.fi | price fallback when CoinGecko rate-limits | no |
| solana.com news RSS | ecosystem and community news | no |
| GitHub API (anza-xyz/agave) | validator client releases | no |
| GitHub API (solana-improvement-documents) | open SIMD proposals | no |

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
