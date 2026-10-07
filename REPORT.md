# Solana Ecosystem Pulse

**Generated:** 2026-10-07T22:21:16Z · **Schema:** `1.0.0` · **Collection time:** 13.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $115.61 | -4.64% |
| Market cap | $68.11B | rank #7 |
| Total value locked | $6.45B | -2.39% |
| Stablecoin supply | $16.91B | -0.80% |
| DEX volume (24h) | $2.05B | -0.22% |
| Chain fees / REV (24h) | $16.05M | -0.23% |
| Non-vote TPS (1h avg) | 2,130 | peak 5,007 total |
| Active validators | 671 | 10 delinquent |
| Epoch 1051 | 74.76% complete | 109,053 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,129.6 average over the last 60 minutes; 2,263.4 in the latest sample.
- **Total TPS:** 4,609.3 average, 5,007.2 peak. Consensus votes account for 53.8% of all transactions.
- **Slot time:** 269.6 ms average (target 400 ms), worst 1-minute bucket 288.5 ms.
- **Block height:** 432,392,450 at absolute slot 454,354,947.
- **Epoch 1051:** slot 322,947 of 432,000 (74.76% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.614% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 198 ms |
| `solana-rpc.publicnode.com` | yes | 112 ms |
| `api.mainnet.solana.com` | yes | 130 ms |

## Validators & stake

- **671 active** validators, **10 delinquent** (1.47% by count, 0.008% by stake).
- **Total stake:** 439,343,031 SOL ($50.79B); stake rate 69.15% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,653,055 | 4.018% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,869 | 3.635% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,308,201 | 2.802% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,264,081 | 2.564% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,149,017 | 2.538% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,259,685 | 2.108% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,251,538 | 2.106% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,508,703 | 1.709% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,113,963 | 1.619% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,690,032 | 1.523% | 0% |

## Economics

- **SOL:** $115.61 (-4.64% 24h, -2.01% 7d, +11.32% 30d). Market cap $68.11B, 24h volume $3.11B (4.57% of cap). Price source: `coingecko`.
- **TVL:** $6.45B across 335 protocols - rank #2 of 468 chains, 6.89% of all tracked chain TVL. -0.97% over 7d, -51.2% from its ATH.
- **Stablecoins:** $16.91B circulating on Solana (+2.61% 7d) - $2.62 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.05B in 24h, $15.19B over 7d across 126 venues. Volume/TVL turnover 0.318x per day.
- **REV (chain fees):** $16.05M in 24h, $451.55M over 30d. Retained chain revenue $5.79M (36.1% of fees). Annualised fees are 8.60% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,094,026 SOL circulating of 635,381,926 total (92.71%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.91B | -4.1% | -1.5% |
| 2 | Kamino Lend | Lending | $1.36B | -3.1% | -4.2% |
| 3 | Raydium AMM | Dexs | $1.30B | -3.4% | -3.2% |
| 4 | Jupiter Lend | Lending | $1.21B | -1.9% | +3.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.21B | -4.1% | -2.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.19B | -4.1% | -2.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $791.06M | -3.1% | -2.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $600.13M | -4.2% | -2.2% |
| 9 | Sentora Curator | Risk Curators | $491.08M | -0.2% | +40.1% |
| 10 | Marinade Native | Staking Pool | $432.37M | -4.0% | -3.4% |
| 11 | PumpSwap | Dexs | $390.48M | -3.6% | -1.0% |
| 12 | Drift Staked SOL | Liquid Staking | $326.74M | -4.2% | -2.6% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 335 protocols the total is $17.22B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.6% · Dexs 15.4% · Derivatives 5.1% · Risk Curators 4.1% · Staking Pool 3.8%

### Tokenised assets

$888.46M of tokenised real-world assets and equities are locked on Solana - 5.160% of chain TVL.

- OnRe (RWA): $293.03M
- Huma (RWA): $257.77M
- Solstice (Basis Trading): $211.83M
- JupUSD (Basis Trading): $48.10M
- Plume Vaults (RWA): $32.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) - Mon, 05 Oct 2026 00:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) - Thu, 01 Oct 2026 09:30:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-07
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-07
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-07
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-07
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-07
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-07
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-07

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

### Change over 24h (vs run at 2026-10-06T21:56:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,237.18 | 4,609.27 | -11.99% |
| Average non-vote TPS | 2,776.85 | 2,129.60 | -23.31% |
| Average slot time (ms) | 270.70 | 269.60 | -0.41% |
| Active validators | 670.00 | 671.00 | +0.15% |
| Delinquent validators | 15.00 | 10.00 | -33.33% |
| Solana TVL | 6,619,880,617.00 | 6,453,092,289.00 | -2.52% |
| SOL price | 120.95 | 115.61 | -4.42% |
| Stablecoin supply | 17,052,133,908.00 | 16,914,576,986.00 | -0.81% |
| 24h DEX volume | 2,057,146,062.50 | 2,052,545,605.65 | -0.22% |
| 24h chain fees | 16,090,422.62 | 16,052,631.31 | -0.23% |

### Change over 7d (vs run at 2026-09-30T21:35:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,839.95 | 4,609.27 | -4.77% |
| Average non-vote TPS | 2,344.25 | 2,129.60 | -9.16% |
| Average slot time (ms) | 268.00 | 269.60 | +0.60% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 11.00 | 10.00 | -9.09% |
| Solana TVL | 6,529,687,399.00 | 6,453,092,289.00 | -1.17% |
| SOL price | 117.96 | 115.61 | -1.99% |
| Stablecoin supply | 16,483,355,698.00 | 16,914,576,986.00 | +2.62% |
| 24h DEX volume | 2,534,187,471.84 | 2,052,545,605.65 | -19.01% |
| 24h chain fees | 14,686,283.17 | 16,052,631.31 | +9.30% |

### Change over 30d (vs run at 2026-09-07T20:51:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,930.66 | 4,609.27 | +17.26% |
| Average non-vote TPS | 1,809.47 | 2,129.60 | +17.69% |
| Average slot time (ms) | 316.70 | 269.60 | -14.87% |
| Active validators | 676.00 | 671.00 | -0.74% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,896,988,391.00 | 6,453,092,289.00 | +9.43% |
| SOL price | 104.08 | 115.61 | +11.08% |
| Stablecoin supply | 16,741,090,548.00 | 16,914,576,986.00 | +1.04% |
| 24h DEX volume | 2,904,503,252.44 | 2,052,545,605.65 | -29.33% |
| 24h chain fees | 14,655,299.70 | 16,052,631.31 | +9.53% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
