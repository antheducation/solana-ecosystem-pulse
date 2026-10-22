# Solana Ecosystem Pulse

**Generated:** 2026-10-22T20:55:10Z · **Schema:** `1.0.0` · **Collection time:** 12.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.14 | -4.58% |
| Market cap | $60.80B | rank #7 |
| Total value locked | $5.88B | -1.82% |
| Stablecoin supply | $16.15B | +0.87% |
| DEX volume (24h) | $2.27B | -6.87% |
| Chain fees / REV (24h) | $11.96M | -10.49% |
| Non-vote TPS (1h avg) | 2,984 | peak 8,156 total |
| Active validators | 655 | 21 delinquent |
| Epoch 1065 | 22.81% complete | 333,472 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 117 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 4 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,984.31 sits 3.4 sigma below the median of the last 117 runs (4,659.15, -35.9%). | `zscore` |
| [WARNING] | Active validators is below its recent norm | Current 655.00 sits 4.3 sigma below the median of the last 117 runs (674.00, -2.8%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 21.00 sits 3.7 sigma above the median of the last 117 runs (10.00, +110.0%). | `zscore` |
| [INFO] | Throughput spike inside the sample window | Peak TPS 8,156 is 2.7x the window average (2,984) - a burst, not a steady load. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,984.3 average over the last 60 minutes; 2,279.6 in the latest sample.
- **Total TPS:** 2,984.3 average, 8,155.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 196.4 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 438,210,903 at absolute slot 460,178,528.
- **Epoch 1065:** slot 98,528 of 432,000 (22.81% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.590% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 249 ms |
| `solana-rpc.publicnode.com` | yes | 50 ms |
| `api.mainnet.solana.com` | yes | 140 ms |

## Validators & stake

- **655 active** validators, **21 delinquent** (3.11% by count, 0.332% by stake).
- **Total stake:** 438,318,925 SOL ($45.21B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 46.00% of active stake.
- **Commission:** median 5.0%, mean 12.94%; 220 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,133,144 | 3.922% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,621 | 3.655% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,556,096 | 2.874% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,936,237 | 2.503% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,726,420 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,476,174 | 2.169% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,244,629 | 2.116% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,797,559 | 1.785% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,036,293 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,002,101 | 1.603% | 0% |

## Economics

- **SOL:** $103.14 (-4.58% 24h, -2.62% 7d, -12.74% 30d). Market cap $60.80B, 24h volume $2.49B (4.09% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 330 protocols - rank #3 of 421 chains, 6.54% of all tracked chain TVL. -1.31% over 7d, -54.6% from its ATH.
- **Stablecoins:** $16.15B circulating on Solana (+0.60% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.27B in 24h, $14.45B over 7d across 138 venues. Volume/TVL turnover 0.386x per day.
- **REV (chain fees):** $11.96M in 24h, $437.76M over 30d. Retained chain revenue $4.55M (38.1% of fees). Annualised fees are 7.18% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,653,510 SOL circulating of 636,273,920 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | -3.5% | +3.0% |
| 2 | Kamino Lend | Lending | $1.31B | -2.3% | -0.3% |
| 3 | Raydium AMM | Dexs | $1.17B | -3.8% | +1.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | -4.0% | +2.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.08B | -4.1% | -1.4% |
| 6 | Jupiter Lend | Lending | $1.04B | -1.3% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $724.02M | -4.3% | -1.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $541.89M | -4.4% | -0.4% |
| 9 | Sentora Curator | Risk Curators | $418.45M | +0.3% | -8.6% |
| 10 | Marinade Native | Staking Pool | $371.85M | -4.7% | -2.6% |
| 11 | PumpSwap | Dexs | $344.49M | -4.6% | -0.7% |
| 12 | Orca DEX | Dexs | $306.53M | -0.3% | +2.8% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.74B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.7% · Dexs 15.2% · Derivatives 5.0% · Risk Curators 3.9% · RWA 3.8%

### Tokenised assets

$864.66M of tokenised real-world assets and equities are locked on Solana - 5.493% of chain TVL.

- OnRe (RWA): $295.03M
- Huma (RWA): $258.61M
- Solstice (Basis Trading): $201.75M
- JupUSD (Basis Trading): $42.96M
- Plume Vaults (RWA): $36.23M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-22
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-22
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-22
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21
- [SIMD-0529: [SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-21T20:57:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,089.84 | 2,984.31 | +42.80% |
| Average non-vote TPS | 2,089.84 | 2,984.31 | +42.80% |
| Average slot time (ms) | 213.00 | 196.40 | -7.79% |
| Active validators | 668.00 | 655.00 | -1.95% |
| Delinquent validators | 9.00 | 21.00 | +133.33% |
| Solana TVL | 6,055,835,656.00 | 5,883,924,131.00 | -2.84% |
| SOL price | 108.08 | 103.14 | -4.57% |
| Stablecoin supply | 16,012,993,627.00 | 16,152,572,344.00 | +0.87% |
| 24h DEX volume | 2,437,800,216.24 | 2,270,402,206.37 | -6.87% |
| 24h chain fees | 13,174,208.40 | 11,957,946.66 | -9.23% |

### Change over 7d (vs run at 2026-10-15T20:36:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,323.17 | 2,984.31 | -43.94% |
| Average non-vote TPS | 2,236.62 | 2,984.31 | +33.43% |
| Average slot time (ms) | 216.50 | 196.40 | -9.28% |
| Active validators | 672.00 | 655.00 | -2.53% |
| Delinquent validators | 9.00 | 21.00 | +133.33% |
| Solana TVL | 6,044,693,032.00 | 5,883,924,131.00 | -2.66% |
| SOL price | 105.91 | 103.14 | -2.62% |
| Stablecoin supply | 16,055,865,871.00 | 16,152,572,344.00 | +0.60% |
| 24h DEX volume | 2,118,350,659.32 | 2,270,402,206.37 | +7.18% |
| 24h chain fees | 10,654,111.63 | 11,957,946.66 | +12.24% |

### Change over 30d (vs run at 2026-09-22T20:34:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,893.52 | 2,984.31 | -39.02% |
| Average non-vote TPS | 2,379.33 | 2,984.31 | +25.43% |
| Average slot time (ms) | 268.00 | 196.40 | -26.72% |
| Active validators | 677.00 | 655.00 | -3.25% |
| Delinquent validators | 12.00 | 21.00 | +75.00% |
| Solana TVL | 6,505,534,933.00 | 5,883,924,131.00 | -9.56% |
| SOL price | 118.17 | 103.14 | -12.72% |
| Stablecoin supply | 17,173,484,924.00 | 16,152,572,344.00 | -5.94% |
| 24h DEX volume | 3,428,858,820.75 | 2,270,402,206.37 | -33.79% |
| 24h chain fees | 18,642,402.21 | 11,957,946.66 | -35.86% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
