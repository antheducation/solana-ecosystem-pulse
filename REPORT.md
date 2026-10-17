# Solana Ecosystem Pulse

**Generated:** 2026-10-17T01:49:50Z · **Schema:** `1.0.0` · **Collection time:** 16.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.30 | -0.75% |
| Market cap | $61.47B | rank #7 |
| Total value locked | $5.95B | -0.10% |
| Stablecoin supply | $16.03B | -1.24% |
| DEX volume (24h) | $1.92B | -15.99% |
| Chain fees / REV (24h) | $12.42M | -2.88% |
| Non-vote TPS (1h avg) | 1,831 | peak 5,650 total |
| Active validators | 671 | 10 delinquent |
| Epoch 1059 | 86.05% complete | 60,262 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 108 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,831.4 average over the last 60 minutes; 1,994.7 in the latest sample.
- **Total TPS:** 4,892.8 average, 5,649.7 peak. Consensus votes account for 62.6% of all transactions.
- **Slot time:** 216.3 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 435,895,317 at absolute slot 457,859,738.
- **Epoch 1059:** slot 371,738 of 432,000 (86.05% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.600% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 217 ms |
| `solana-rpc.publicnode.com` | yes | 164 ms |
| `api.mainnet.solana.com` | yes | 169 ms |

## Validators & stake

- **671 active** validators, **10 delinquent** (1.47% by count, 0.004% by stake).
- **Total stake:** 437,782,540 SOL ($45.66B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,561,701 | 4.012% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,460,528 | 3.532% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,362,555 | 2.824% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,093,074 | 2.534% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,200,312 | 2.330% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,428,271 | 2.154% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,248,874 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,743,557 | 1.769% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,910,886 | 1.579% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,417,148 | 1.466% | 0% |

## Economics

- **SOL:** $104.30 (-0.75% 24h, -4.60% 7d, +5.73% 30d). Market cap $61.47B, 24h volume $2.90B (4.72% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 325 protocols - rank #3 of 425 chains, 6.65% of all tracked chain TVL. -3.81% over 7d, -55.2% from its ATH.
- **Stablecoins:** $16.03B circulating on Solana (-1.33% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.92B in 24h, $12.42B over 7d across 136 venues. Volume/TVL turnover 0.323x per day.
- **REV (chain fees):** $12.42M in 24h, $459.75M over 30d. Retained chain revenue $5.08M (41.0% of fees). Annualised fees are 7.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,328,628 SOL circulating of 635,905,356 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +1.2% | +0.7% |
| 2 | Kamino Lend | Lending | $1.31B | -0.9% | -1.1% |
| 3 | Raydium AMM | Dexs | $1.18B | -1.2% | -5.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.09B | -1.1% | -4.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | +0.1% | -2.7% |
| 6 | Jupiter Lend | Lending | $1.09B | -2.0% | -4.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $738.77M | -1.2% | -4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $545.52M | -1.0% | -3.4% |
| 9 | Sentora Curator | Risk Curators | $451.37M | -1.4% | -9.2% |
| 10 | Marinade Native | Staking Pool | $381.51M | -1.1% | -5.6% |
| 11 | PumpSwap | Dexs | $352.35M | -0.1% | -3.2% |
| 12 | Orca DEX | Dexs | $299.17M | -1.0% | -3.4% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 325 protocols the total is $15.93B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.8% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$893.00M of tokenised real-world assets and equities are locked on Solana - 5.607% of chain TVL.

- OnRe (RWA): $293.45M
- Huma (RWA): $280.96M
- Solstice (Basis Trading): $209.32M
- JupUSD (Basis Trading): $43.96M
- Plume Vaults (RWA): $35.50M

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

- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-16
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-16
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-16
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-16
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-15
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-15
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-15

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

### Change over 24h (vs run at 2026-10-16T01:55:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,933.00 | 4,892.76 | -17.53% |
| Average non-vote TPS | 2,860.96 | 1,831.42 | -35.99% |
| Average slot time (ms) | 217.70 | 216.30 | -0.64% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 6,022,784,745.00 | 5,951,786,169.00 | -1.18% |
| SOL price | 105.09 | 104.30 | -0.75% |
| Stablecoin supply | 16,231,219,596.00 | 16,032,051,625.00 | -1.23% |
| 24h DEX volume | 2,423,566,552.03 | 1,921,217,321.11 | -20.73% |
| 24h chain fees | 12,686,735.80 | 12,415,523.82 | -2.14% |

### Change over 7d (vs run at 2026-10-10T03:00:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,740.69 | 4,892.76 | +3.21% |
| Average non-vote TPS | 1,669.34 | 1,831.42 | +9.71% |
| Average slot time (ms) | 218.70 | 216.30 | -1.10% |
| Active validators | 674.00 | 671.00 | -0.45% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 6,187,946,925.00 | 5,951,786,169.00 | -3.82% |
| SOL price | 109.79 | 104.30 | -5.00% |
| Stablecoin supply | 16,427,773,068.00 | 16,032,051,625.00 | -2.41% |
| 24h DEX volume | 2,215,423,677.91 | 1,921,217,321.11 | -13.28% |
| 24h chain fees | 13,940,731.19 | 12,415,523.82 | -10.94% |

### Change over 30d (vs run at 2026-09-16T20:32:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,850.92 | 4,892.76 | +0.86% |
| Average non-vote TPS | 2,744.58 | 1,831.42 | -33.27% |
| Average slot time (ms) | 318.60 | 216.30 | -32.11% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 14.00 | 10.00 | -28.57% |
| Solana TVL | 5,723,932,041.00 | 5,951,786,169.00 | +3.98% |
| SOL price | 98.40 | 104.30 | +6.00% |
| Stablecoin supply | 15,963,602,798.00 | 16,032,051,625.00 | +0.43% |
| 24h DEX volume | 2,703,297,666.22 | 1,921,217,321.11 | -28.93% |
| 24h chain fees | 14,083,156.46 | 12,415,523.82 | -11.84% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
