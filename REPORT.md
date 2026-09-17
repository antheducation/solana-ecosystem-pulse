# Solana Ecosystem Pulse

**Generated:** 2026-09-17T20:39:05Z · **Schema:** `1.0.0` · **Collection time:** 27.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.14 | +2.84% |
| Market cap | $59.39B | rank #7 |
| Total value locked | $5.87B | +2.47% |
| Stablecoin supply | $15.77B | -1.20% |
| DEX volume (24h) | $2.80B | +3.59% |
| Chain fees / REV (24h) | $14.07M | -0.10% |
| Non-vote TPS (1h avg) | 2,552 | peak 5,353 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1036 | 77.77% complete | 96,023 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 85 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,551.8 average over the last 60 minutes; 2,088.3 in the latest sample.
- **Total TPS:** 4,673.9 average, 5,352.7 peak. Consensus votes account for 45.4% of all transactions.
- **Slot time:** 318.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 425,929,105 at absolute slot 447,887,977.
- **Epoch 1036:** slot 335,977 of 432,000 (77.77% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.644% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 551 ms |
| `solana-rpc.publicnode.com` | yes | 153 ms |
| `api.mainnet.solana.com` | yes | 485 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.040% by stake).
- **Total stake:** 439,761,083 SOL ($44.48B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.65%; 241 validators at 0% and 64 at 100%.

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

- **SOL:** $101.14 (+2.84% 24h, +1.47% 7d, +31.16% 30d). Market cap $59.39B, 24h volume $3.24B (5.46% of cap). Price source: `coingecko`.
- **TVL:** $5.87B across 334 protocols - rank #2 of 468 chains, 6.63% of all tracked chain TVL. +0.15% over 7d, -55.7% from its ATH.
- **Stablecoins:** $15.77B circulating on Solana (-5.01% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.80B in 24h, $17.85B over 7d across 124 venues. Volume/TVL turnover 0.477x per day.
- **REV (chain fees):** $14.07M in 24h, $404.98M over 30d. Retained chain revenue $4.91M (34.9% of fees). Annualised fees are 8.65% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,211,829 SOL circulating of 634,204,257 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.61B | +3.8% | +4.2% |
| 2 | Kamino Lend | Lending | $1.33B | -0.2% | -0.6% |
| 3 | Raydium AMM | Dexs | $1.14B | +4.3% | +1.1% |
| 4 | Jupiter Lend | Lending | $1.09B | +3.3% | +1.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | +3.5% | -0.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | +3.6% | +0.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $748.87M | +2.3% | +0.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $525.51M | +4.0% | +0.4% |
| 9 | Marinade Native | Staking Pool | $385.32M | +3.5% | -0.6% |
| 10 | Sentora Curator | Risk Curators | $365.42M | -1.6% | -5.5% |
| 11 | PumpSwap | Dexs | $327.86M | +3.9% | +0.4% |
| 12 | OnRe | RWA | $302.97M | +0.2% | -1.4% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.97B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.1% · Lending 17.9% · Dexs 15.6% · Derivatives 5.5% · Staking Pool 4.0% · Risk Curators 3.9%

### Tokenised assets

$883.44M of tokenised real-world assets and equities are locked on Solana - 5.900% of chain TVL.

- OnRe (RWA): $302.97M
- Solstice (Basis Trading): $235.01M
- Huma Finance V2 (RWA): $188.37M
- JupUSD (Basis Trading): $46.82M
- Plume Vaults (RWA): $27.85M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-17
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

### Change over 24h (vs run at 2026-09-16T20:32:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,850.92 | 4,673.89 | -3.65% |
| Average non-vote TPS | 2,744.58 | 2,551.83 | -7.02% |
| Average slot time (ms) | 318.60 | 318.10 | -0.16% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,723,932,041.00 | 5,865,883,806.00 | +2.48% |
| SOL price | 98.40 | 101.14 | +2.78% |
| Stablecoin supply | 15,963,602,798.00 | 15,774,027,557.00 | -1.19% |
| 24h DEX volume | 2,703,297,666.22 | 2,800,249,070.18 | +3.59% |
| 24h chain fees | 14,083,156.46 | 14,069,098.05 | -0.10% |

### Change over 7d (vs run at 2026-09-10T20:09:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,122.54 | 4,673.89 | +13.37% |
| Average non-vote TPS | 1,990.17 | 2,551.83 | +28.22% |
| Average slot time (ms) | 315.50 | 318.10 | +0.82% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 5,779,330,766.00 | 5,865,883,806.00 | +1.50% |
| SOL price | 99.77 | 101.14 | +1.37% |
| Stablecoin supply | 16,576,239,978.00 | 15,774,027,557.00 | -4.84% |
| 24h DEX volume | 3,000,435,429.63 | 2,800,249,070.18 | -6.67% |
| 24h chain fees | 15,717,207.17 | 14,069,098.05 | -10.49% |

### Change over 30d (vs run at 2026-08-18T18:18:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,157.63 | 4,673.89 | +12.42% |
| Average non-vote TPS | 2,510.42 | 2,551.83 | +1.65% |
| Average slot time (ms) | 414.50 | 318.10 | -23.26% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 7.00 | 13.00 | +85.71% |
| Solana TVL | 4,885,957,310.00 | 5,865,883,806.00 | +20.06% |
| SOL price | 77.08 | 101.14 | +31.21% |
| Stablecoin supply | 15,977,966,490.00 | 15,774,027,557.00 | -1.28% |
| 24h DEX volume | 1,474,970,358.36 | 2,800,249,070.18 | +89.85% |
| 24h chain fees | 11,189,593.30 | 14,069,098.05 | +25.73% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 27.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
