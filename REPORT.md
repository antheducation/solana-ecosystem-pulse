# Solana Ecosystem Pulse

**Generated:** 2026-11-22T13:41:14Z · **Schema:** `1.0.0` · **Collection time:** 15.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.12 | -0.33% |
| Market cap | $41.49B | rank #7 |
| Total value locked | $4.65B | +1.61% |
| Stablecoin supply | $13.37B | +0.82% |
| DEX volume (24h) | $1.35B | -28.59% |
| Chain fees / REV (24h) | $7.57M | -8.71% |
| Non-vote TPS (1h avg) | 1,279 | peak 1,752 total |
| Active validators | 661 | 24 delinquent |
| Epoch 1093 | 89.16% complete | 46,847 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 134 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,279; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,366,255,308.00 sits 3.1 sigma below the median of the last 134 runs (15,973,982,918.00, -16.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,279.2 average over the last 60 minutes; 1,553.9 in the latest sample.
- **Total TPS:** 1,279.2 average, 1,752.2 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 450,575,036 at absolute slot 472,561,153.
- **Epoch 1093:** slot 385,153 of 432,000 (89.16% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.546% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 70 ms |
| `solana-rpc.publicnode.com` | yes | 70 ms |
| `api.mainnet.solana.com` | yes | 153 ms |

## Validators & stake

- **661 active** validators, **24 delinquent** (3.50% by count, 0.017% by stake).
- **Total stake:** 428,316,392 SOL ($30.03B); stake rate 67.14% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.86% and top 33 hold 46.49% of active stake.
- **Commission:** median 5.0%, mean 12.90%; 219 validators at 0% and 62 at 100%.

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

- **SOL:** $70.12 (-0.33% 24h, -3.67% 7d, -32.81% 30d). Market cap $41.49B, 24h volume $2.18B (5.26% of cap). Price source: `coingecko`.
- **TVL:** $4.65B across 343 protocols - rank #3 of 426 chains, 6.71% of all tracked chain TVL. +0.18% over 7d, -60.9% from its ATH.
- **Stablecoins:** $13.37B circulating on Solana (-6.05% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.35B in 24h, $11.29B over 7d across 144 venues. Volume/TVL turnover 0.289x per day.
- **REV (chain fees):** $7.57M in 24h, $290.60M over 30d. Retained chain revenue $2.58M (34.1% of fees). Annualised fees are 6.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,961,460 SOL circulating of 637,981,291 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +2.5% | -1.4% |
| 2 | Kamino Lend | Lending | $1.14B | +1.9% | +1.6% |
| 3 | Jupiter Lend | Lending | $959.55M | +1.9% | +5.5% |
| 4 | Raydium AMM | Dexs | $784.75M | +2.5% | -5.5% |
| 5 | Binance Staked SOL | Liquid Staking | $727.20M | +2.7% | -1.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $706.54M | +1.1% | +0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $573.96M | +3.0% | +2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $363.71M | +2.6% | -0.4% |
| 9 | Sentora Curator | Risk Curators | $356.52M | +0.0% | -0.6% |
| 10 | OnRe | RWA | $287.49M | -0.1% | -5.5% |
| 11 | Forward Industries SOL | Liquid Staking | $278.25M | +2.9% | +0.1% |
| 12 | CCIP | Bridge | $267.42M | -0.3% | -4.0% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.81B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.4% · Dexs 14.5% · Derivatives 5.4% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$776.68M of tokenised real-world assets and equities are locked on Solana - 6.575% of chain TVL.

- OnRe (RWA): $287.49M
- Huma (RWA): $225.25M
- Solstice (Basis Trading): $201.03M
- JupUSD (Basis Trading): $39.43M
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

### Change over 24h (vs run at 2026-11-21T13:47:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,480.30 | 1,279.20 | -13.59% |
| Average non-vote TPS | 1,480.30 | 1,279.20 | -13.59% |
| Average slot time (ms) | 214.80 | 215.20 | +0.19% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 23.00 | 24.00 | +4.35% |
| Solana TVL | 4,553,427,239.00 | 4,650,170,865.00 | +2.12% |
| SOL price | 70.37 | 70.12 | -0.36% |
| Stablecoin supply | 13,258,597,026.00 | 13,366,255,308.00 | +0.81% |
| 24h DEX volume | 1,884,688,033.35 | 1,345,931,988.87 | -28.59% |
| 24h chain fees | 8,289,486.06 | 7,568,696.38 | -8.70% |

### Change over 7d (vs run at 2026-11-15T13:02:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,228.19 | 1,279.20 | +4.15% |
| Average non-vote TPS | 1,228.19 | 1,279.20 | +4.15% |
| Average slot time (ms) | 214.30 | 215.20 | +0.42% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 38.00 | 24.00 | -36.84% |
| Solana TVL | 4,718,587,563.00 | 4,650,170,865.00 | -1.45% |
| SOL price | 72.84 | 70.12 | -3.73% |
| Stablecoin supply | 14,225,356,442.00 | 13,366,255,308.00 | -6.04% |
| 24h DEX volume | 1,692,508,944.70 | 1,345,931,988.87 | -20.48% |
| 24h chain fees | 7,874,648.14 | 7,568,696.38 | -3.89% |

### Change over 30d (vs run at 2026-10-23T20:43:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,163.30 | 1,279.20 | -40.87% |
| Average non-vote TPS | 2,163.30 | 1,279.20 | -40.87% |
| Average slot time (ms) | 212.20 | 215.20 | +1.41% |
| Active validators | 664.00 | 661.00 | -0.45% |
| Delinquent validators | 14.00 | 24.00 | +71.43% |
| Solana TVL | 5,856,286,188.00 | 4,650,170,865.00 | -20.60% |
| SOL price | 103.58 | 70.12 | -32.30% |
| Stablecoin supply | 15,965,866,149.00 | 13,366,255,308.00 | -16.28% |
| 24h DEX volume | 2,039,384,832.23 | 1,345,931,988.87 | -34.00% |
| 24h chain fees | 11,472,475.22 | 7,568,696.38 | -34.03% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 15.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
