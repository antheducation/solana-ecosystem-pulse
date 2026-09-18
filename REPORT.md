# Solana Ecosystem Pulse

**Generated:** 2026-09-18T01:50:33Z · **Schema:** `1.0.0` · **Collection time:** 13.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.31 | +3.03% |
| Market cap | $60.09B | rank #7 |
| Total value locked | $5.88B | +0.30% |
| Stablecoin supply | $15.71B | -0.41% |
| DEX volume (24h) | $2.56B | -8.72% |
| Chain fees / REV (24h) | $13.10M | -6.84% |
| Non-vote TPS (1h avg) | 1,979 | peak 4,641 total |
| Active validators | 676 | 14 delinquent |
| Epoch 1036 | 91.41% complete | 37,100 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 85 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,978.7 average over the last 60 minutes; 2,175.7 in the latest sample.
- **Total TPS:** 4,099.5 average, 4,640.9 peak. Consensus votes account for 51.7% of all transactions.
- **Slot time:** 316.7 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 425,987,964 at absolute slot 447,946,900.
- **Epoch 1036:** slot 394,900 of 432,000 (91.41% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.644% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 100 ms |
| `solana-rpc.publicnode.com` | yes | 141 ms |
| `api.mainnet.solana.com` | yes | 80 ms |

## Validators & stake

- **676 active** validators, **14 delinquent** (2.03% by count, 0.040% by stake).
- **Total stake:** 439,761,083 SOL ($44.99B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.52%; 241 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,767,428 | 4.042% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,352,114 | 3.720% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,485,145 | 2.840% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,383,247 | 2.590% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,740,877 | 2.216% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,273 | 2.106% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,049,051 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,386,183 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,076,306 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,558,592 | 1.492% | 0% |

## Economics

- **SOL:** $102.31 (+3.03% 24h, +3.21% 7d, +33.08% 30d). Market cap $60.09B, 24h volume $3.27B (5.45% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 333 protocols - rank #2 of 468 chains, 6.66% of all tracked chain TVL. +2.08% over 7d, -55.6% from its ATH.
- **Stablecoins:** $15.71B circulating on Solana (-3.97% 7d) - $2.67 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.56B in 24h, $16.07B over 7d across 124 venues. Volume/TVL turnover 0.435x per day.
- **REV (chain fees):** $13.10M in 24h, $400.21M over 30d. Retained chain revenue $5.18M (39.6% of fees). Annualised fees are 7.96% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,211,618 SOL circulating of 634,204,046 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.62B | +2.8% | +6.7% |
| 2 | Kamino Lend | Lending | $1.33B | -0.1% | +2.6% |
| 3 | Raydium AMM | Dexs | $1.15B | +3.3% | +3.5% |
| 4 | Jupiter Lend | Lending | $1.09B | +1.6% | +2.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | +2.9% | +1.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | +2.6% | +3.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $748.27M | +1.4% | +1.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $528.07M | +3.4% | +2.8% |
| 9 | Marinade Native | Staking Pool | $387.27M | +3.0% | +1.5% |
| 10 | Sentora Curator | Risk Curators | $368.46M | -1.0% | -5.0% |
| 11 | PumpSwap | Dexs | $329.08M | +2.5% | +1.6% |
| 12 | OnRe | RWA | $302.98M | +0.1% | -2.1% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.02B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.2% · Lending 17.8% · Dexs 15.6% · Derivatives 5.5% · Staking Pool 4.0% · Risk Curators 3.9%

### Tokenised assets

$879.94M of tokenised real-world assets and equities are locked on Solana - 5.859% of chain TVL.

- OnRe (RWA): $302.98M
- Solstice (Basis Trading): $234.98M
- Huma Finance V2 (RWA): $191.84M
- JupUSD (Basis Trading): $46.82M
- Plume Vaults (RWA): $27.91M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-17
- [SIMD-0123: SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-16
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-16

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

### Change over 24h (vs run at 2026-09-17T02:03:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,281.28 | 4,099.51 | -4.25% |
| Average non-vote TPS | 2,153.15 | 1,978.66 | -8.10% |
| Average slot time (ms) | 317.20 | 316.70 | -0.16% |
| Active validators | 679.00 | 676.00 | -0.44% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 5,738,424,911.00 | 5,875,684,850.00 | +2.39% |
| SOL price | 99.21 | 102.31 | +3.12% |
| Stablecoin supply | 15,774,289,704.00 | 15,710,182,138.00 | -0.41% |
| 24h DEX volume | 2,733,437,291.18 | 2,555,388,156.29 | -6.51% |
| 24h chain fees | 14,036,672.88 | 13,101,763.60 | -6.66% |

### Change over 7d (vs run at 2026-09-11T01:44:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,820.46 | 4,099.51 | +7.30% |
| Average non-vote TPS | 1,687.31 | 1,978.66 | +17.27% |
| Average slot time (ms) | 315.10 | 316.70 | +0.51% |
| Active validators | 675.00 | 676.00 | +0.15% |
| Delinquent validators | 14.00 | 14.00 | +0.00% |
| Solana TVL | 5,753,733,189.00 | 5,875,684,850.00 | +2.12% |
| SOL price | 98.76 | 102.31 | +3.59% |
| Stablecoin supply | 16,358,256,053.00 | 15,710,182,138.00 | -3.96% |
| 24h DEX volume | 2,947,608,342.01 | 2,555,388,156.29 | -13.31% |
| 24h chain fees | 14,677,343.47 | 13,101,763.60 | -10.73% |

### Change over 30d (vs run at 2026-08-18T18:18:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,157.63 | 4,099.51 | -1.40% |
| Average non-vote TPS | 2,510.42 | 1,978.66 | -21.18% |
| Average slot time (ms) | 414.50 | 316.70 | -23.59% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 7.00 | 14.00 | +100.00% |
| Solana TVL | 4,885,957,310.00 | 5,875,684,850.00 | +20.26% |
| SOL price | 77.08 | 102.31 | +32.73% |
| Stablecoin supply | 15,977,966,490.00 | 15,710,182,138.00 | -1.68% |
| 24h DEX volume | 1,474,970,358.36 | 2,555,388,156.29 | +73.25% |
| 24h chain fees | 11,189,593.30 | 13,101,763.60 | +17.09% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
