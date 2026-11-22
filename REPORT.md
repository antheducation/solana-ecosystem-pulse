# Solana Ecosystem Pulse

**Generated:** 2026-11-22T03:45:15Z · **Schema:** `1.0.0` · **Collection time:** 22.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $69.24 | +4.69% |
| Market cap | $41.00B | rank #7 |
| Total value locked | $4.62B | +0.94% |
| Stablecoin supply | $13.36B | +0.81% |
| DEX volume (24h) | $1.56B | -17.20% |
| Chain fees / REV (24h) | $7.89M | -4.67% |
| Non-vote TPS (1h avg) | 1,378 | peak 1,990 total |
| Active validators | 661 | 24 delinquent |
| Epoch 1093 | 50.66% complete | 213,149 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 133 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,378; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,364,640,996.00 sits 3.2 sigma below the median of the last 133 runs (15,977,966,490.00, -16.4%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,378.2 average over the last 60 minutes; 945.2 in the latest sample.
- **Total TPS:** 1,378.2 average, 1,990.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.6 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 450,408,770 at absolute slot 472,394,851.
- **Epoch 1093:** slot 218,851 of 432,000 (50.66% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.546% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 205 ms |
| `solana-rpc.publicnode.com` | yes | 94 ms |
| `api.mainnet.solana.com` | yes | 119 ms |

## Validators & stake

- **661 active** validators, **24 delinquent** (3.50% by count, 0.017% by stake).
- **Total stake:** 428,316,392 SOL ($29.66B); stake rate 67.14% of total supply.
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

- **SOL:** $69.24 (+4.69% 24h, -2.92% 7d, -33.74% 30d). Market cap $41.00B, 24h volume $3.17B (7.74% of cap). Price source: `coingecko`.
- **TVL:** $4.62B across 343 protocols - rank #3 of 426 chains, 6.78% of all tracked chain TVL. -0.48% over 7d, -61.2% from its ATH.
- **Stablecoins:** $13.36B circulating on Solana (-6.06% 7d) - $2.89 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.56B in 24h, $10.54B over 7d across 144 venues. Volume/TVL turnover 0.338x per day.
- **REV (chain fees):** $7.89M in 24h, $289.61M over 30d. Retained chain revenue $2.63M (33.4% of fees). Annualised fees are 7.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,961,575 SOL circulating of 637,981,407 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +2.3% | -1.9% |
| 2 | Kamino Lend | Lending | $1.14B | +1.1% | +1.0% |
| 3 | Jupiter Lend | Lending | $952.25M | +0.8% | +4.7% |
| 4 | Raydium AMM | Dexs | $780.19M | +2.0% | -6.1% |
| 5 | Binance Staked SOL | Liquid Staking | $713.83M | +1.1% | -3.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $711.15M | +2.6% | +0.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $568.17M | +1.2% | +1.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $361.48M | +2.0% | -1.0% |
| 9 | Sentora Curator | Risk Curators | $356.30M | +0.1% | -0.6% |
| 10 | OnRe | RWA | $287.49M | -0.6% | -5.5% |
| 11 | Forward Industries SOL | Liquid Staking | $276.49M | +2.5% | -0.6% |
| 12 | CCIP | Bridge | $267.29M | -0.8% | -4.0% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.73B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.4% · Dexs 14.5% · Derivatives 5.3% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$776.60M of tokenised real-world assets and equities are locked on Solana - 6.619% of chain TVL.

- OnRe (RWA): $287.49M
- Huma (RWA): $225.24M
- Solstice (Basis Trading): $200.98M
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

### Change over 24h (vs run at 2026-11-21T04:30:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,430.89 | 1,378.16 | -43.31% |
| Average non-vote TPS | 2,430.89 | 1,378.16 | -43.31% |
| Average slot time (ms) | 215.50 | 215.60 | +0.05% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 23.00 | 24.00 | +4.35% |
| Solana TVL | 4,553,805,751.00 | 4,619,778,328.00 | +1.45% |
| SOL price | 65.28 | 69.24 | +6.07% |
| Stablecoin supply | 13,257,552,960.00 | 13,364,640,996.00 | +0.81% |
| 24h DEX volume | 1,836,080,739.35 | 1,560,546,106.87 | -15.01% |
| 24h chain fees | 8,962,669.20 | 7,893,685.33 | -11.93% |

### Change over 7d (vs run at 2026-11-15T03:28:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,657.93 | 1,378.16 | -16.87% |
| Average non-vote TPS | 1,657.93 | 1,378.16 | -16.87% |
| Average slot time (ms) | 215.40 | 215.60 | +0.09% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 37.00 | 24.00 | -35.14% |
| Solana TVL | 4,612,450,821.00 | 4,619,778,328.00 | +0.16% |
| SOL price | 71.61 | 69.24 | -3.31% |
| Stablecoin supply | 14,224,431,770.00 | 13,364,640,996.00 | -6.04% |
| 24h DEX volume | 1,614,007,307.70 | 1,560,546,106.87 | -3.31% |
| 24h chain fees | 8,186,168.20 | 7,893,685.33 | -3.57% |

### Change over 30d (vs run at 2026-10-22T20:55:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,984.31 | 1,378.16 | -53.82% |
| Average non-vote TPS | 2,984.31 | 1,378.16 | -53.82% |
| Average slot time (ms) | 196.40 | 215.60 | +9.78% |
| Active validators | 655.00 | 661.00 | +0.92% |
| Delinquent validators | 21.00 | 24.00 | +14.29% |
| Solana TVL | 5,883,924,131.00 | 4,619,778,328.00 | -21.48% |
| SOL price | 103.14 | 69.24 | -32.87% |
| Stablecoin supply | 16,152,572,344.00 | 13,364,640,996.00 | -17.26% |
| 24h DEX volume | 2,270,402,206.37 | 1,560,546,106.87 | -31.27% |
| 24h chain fees | 11,957,946.66 | 7,893,685.33 | -33.99% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
