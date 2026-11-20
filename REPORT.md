# Solana Ecosystem Pulse

**Generated:** 2026-11-20T23:26:37Z · **Schema:** `1.0.0` · **Collection time:** 20.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $69.14 | -5.33% |
| Market cap | $40.93B | rank #7 |
| Total value locked | $4.59B | -3.28% |
| Stablecoin supply | $13.45B | +3.04% |
| DEX volume (24h) | $1.90B | +4.89% |
| Chain fees / REV (24h) | $9.31M | -14.66% |
| Non-vote TPS (1h avg) | 1,464 | peak 2,121 total |
| Active validators | 662 | 23 delinquent |
| Epoch 1092 | 40.95% complete | 255,080 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 133 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,464; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.0% in 24h) | Stablecoin supply changed +3.0% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,451,822,446.00 sits 3.1 sigma below the median of the last 133 runs (15,977,966,490.00, -15.8%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,463.5 average over the last 60 minutes; 1,355.0 in the latest sample.
- **Total TPS:** 1,463.5 average, 2,120.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 449,934,900 at absolute slot 471,920,920.
- **Epoch 1092:** slot 176,920 of 432,000 (40.95% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.548% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 128 ms |
| `solana-rpc.publicnode.com` | yes | 196 ms |
| `api.mainnet.solana.com` | yes | 141 ms |

## Validators & stake

- **662 active** validators, **23 delinquent** (3.36% by count, 0.017% by stake).
- **Total stake:** 428,985,797 SOL ($29.66B); stake rate 67.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.82% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 12.87%; 220 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,041,638 | 3.973% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,354,101 | 3.813% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,891 | 2.896% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,309,121 | 2.404% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,779,397 | 2.280% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,564,403 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,683 | 2.152% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,986,182 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,985,765 | 1.629% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,773,182 | 1.579% | 5% |

## Economics

- **SOL:** $69.14 (-5.33% 24h, -11.00% 7d, -35.62% 30d). Market cap $40.93B, 24h volume $3.57B (8.72% of cap). Price source: `coingecko`.
- **TVL:** $4.59B across 342 protocols - rank #3 of 426 chains, 6.87% of all tracked chain TVL. -8.82% over 7d, -61.5% from its ATH.
- **Stablecoins:** $13.45B circulating on Solana (-6.43% 7d) - $2.93 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.90B in 24h, $11.31B over 7d across 144 venues. Volume/TVL turnover 0.415x per day.
- **REV (chain fees):** $9.31M in 24h, $300.21M over 30d. Retained chain revenue $2.99M (32.2% of fees). Annualised fees are 8.30% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,906,488 SOL circulating of 637,920,464 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.24B | -6.6% | -14.4% |
| 2 | Kamino Lend | Lending | $1.12B | -1.9% | -4.9% |
| 3 | Jupiter Lend | Lending | $952.87M | +0.3% | -0.9% |
| 4 | Raydium AMM | Dexs | $766.00M | -5.5% | -17.9% |
| 5 | Binance Staked SOL | Liquid Staking | $711.47M | -4.4% | -19.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $695.11M | -4.3% | -16.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $564.25M | -3.2% | -9.3% |
| 8 | Sentora Curator | Risk Curators | $355.43M | -0.5% | -2.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $349.76M | -5.0% | -16.2% |
| 10 | OnRe | RWA | $289.31M | -0.8% | -6.5% |
| 11 | Forward Industries SOL | Liquid Staking | $271.60M | -4.3% | +5.5% |
| 12 | CCIP | Bridge | $269.18M | -1.6% | +2.6% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 342 protocols the total is $11.59B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 39.8% · Lending 19.5% · Dexs 14.5% · Derivatives 5.4% · RWA 4.6% · Risk Curators 4.2%

### Tokenised assets

$785.07M of tokenised real-world assets and equities are locked on Solana - 6.774% of chain TVL.

- OnRe (RWA): $289.31M
- Huma (RWA): $231.30M
- Solstice (Basis Trading): $201.11M
- JupUSD (Basis Trading): $39.90M
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

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17

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

### Change over 24h (vs run at 2026-11-19T23:57:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,928.85 | 1,463.53 | -24.12% |
| Average non-vote TPS | 1,928.85 | 1,463.53 | -24.12% |
| Average slot time (ms) | 215.70 | 215.10 | -0.28% |
| Active validators | 659.00 | 662.00 | +0.46% |
| Delinquent validators | 26.00 | 23.00 | -11.54% |
| Solana TVL | 4,721,393,649.00 | 4,588,288,121.00 | -2.82% |
| SOL price | 73.08 | 69.14 | -5.39% |
| Stablecoin supply | 13,055,005,144.00 | 13,451,822,446.00 | +3.04% |
| 24h DEX volume | 1,815,395,819.31 | 1,904,105,685.06 | +4.89% |
| 24h chain fees | 10,954,885.63 | 9,305,684.57 | -15.05% |

### Change over 7d (vs run at 2026-11-13T22:57:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,140.34 | 1,463.53 | -31.62% |
| Average non-vote TPS | 2,140.34 | 1,463.53 | -31.62% |
| Average slot time (ms) | 215.20 | 215.10 | -0.05% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 38.00 | 23.00 | -39.47% |
| Solana TVL | 4,958,650,115.00 | 4,588,288,121.00 | -7.47% |
| SOL price | 78.20 | 69.14 | -11.59% |
| Stablecoin supply | 14,376,185,613.00 | 13,451,822,446.00 | -6.43% |
| 24h DEX volume | 1,503,485,412.77 | 1,904,105,685.06 | +26.65% |
| 24h chain fees | 8,074,998.20 | 9,305,684.57 | +15.24% |

### Change over 30d (vs run at 2026-10-21T20:57:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,089.84 | 1,463.53 | -29.97% |
| Average non-vote TPS | 2,089.84 | 1,463.53 | -29.97% |
| Average slot time (ms) | 213.00 | 215.10 | +0.99% |
| Active validators | 668.00 | 662.00 | -0.90% |
| Delinquent validators | 9.00 | 23.00 | +155.56% |
| Solana TVL | 6,055,835,656.00 | 4,588,288,121.00 | -24.23% |
| SOL price | 108.08 | 69.14 | -36.03% |
| Stablecoin supply | 16,012,993,627.00 | 13,451,822,446.00 | -15.99% |
| 24h DEX volume | 2,437,800,216.24 | 1,904,105,685.06 | -21.89% |
| 24h chain fees | 13,174,208.40 | 9,305,684.57 | -29.36% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
