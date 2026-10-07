# Solana Ecosystem Pulse

**Generated:** 2026-10-07T12:10:29Z · **Schema:** `1.0.0` · **Collection time:** 16.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.28 | -2.63% |
| Market cap | $69.09B | rank #7 |
| Total value locked | $6.51B | -4.10% |
| Stablecoin supply | $16.92B | -0.79% |
| DEX volume (24h) | $2.05B | -0.22% |
| Chain fees / REV (24h) | $16.04M | -0.29% |
| Non-vote TPS (1h avg) | 1,657 | peak 5,002 total |
| Active validators | 670 | 11 delinquent |
| Epoch 1051 | 43.29% complete | 245,004 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,657.1 average over the last 60 minutes; 1,666.4 in the latest sample.
- **Total TPS:** 4,150.7 average, 5,002.2 peak. Consensus votes account for 60.1% of all transactions.
- **Slot time:** 268.6 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 432,256,580 at absolute slot 454,218,996.
- **Epoch 1051:** slot 186,996 of 432,000 (43.29% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.614% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 203 ms |
| `solana-rpc.publicnode.com` | yes | 172 ms |
| `api.mainnet.solana.com` | yes | 182 ms |

## Validators & stake

- **670 active** validators, **11 delinquent** (1.62% by count, 0.022% by stake).
- **Total stake:** 439,343,031 SOL ($51.53B); stake rate 69.15% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.63% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.68%; 231 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,653,055 | 4.019% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,869 | 3.636% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,308,201 | 2.802% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,264,081 | 2.564% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,149,017 | 2.538% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,259,685 | 2.108% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,251,538 | 2.106% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,508,703 | 1.709% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,113,963 | 1.620% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,690,032 | 1.523% | 0% |

## Economics

- **SOL:** $117.28 (-2.63% 24h, -1.80% 7d, +11.78% 30d). Market cap $69.09B, 24h volume $2.80B (4.05% of cap). Price source: `coingecko`.
- **TVL:** $6.51B across 334 protocols - rank #2 of 468 chains, 6.93% of all tracked chain TVL. -0.89% over 7d, -50.8% from its ATH.
- **Stablecoins:** $16.92B circulating on Solana (+2.63% 7d) - $2.60 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.05B in 24h, $15.19B over 7d across 126 venues. Volume/TVL turnover 0.315x per day.
- **REV (chain fees):** $16.04M in 24h, $451.44M over 30d. Retained chain revenue $5.79M (36.1% of fees). Annualised fees are 8.48% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,094,493 SOL circulating of 635,382,392 total (92.71%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.94B | -2.3% | +0.0% |
| 2 | Kamino Lend | Lending | $1.38B | -1.3% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.32B | -1.3% | -1.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -1.8% | -0.6% |
| 5 | Jupiter Lend | Lending | $1.23B | -12.8% | +4.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | -1.8% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $799.51M | -2.1% | -1.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.08M | -1.8% | -0.1% |
| 9 | Sentora Curator | Risk Curators | $492.17M | +7.2% | +40.4% |
| 10 | Marinade Native | Staking Pool | $440.91M | -1.6% | -1.5% |
| 11 | PumpSwap | Dexs | $394.32M | -1.7% | -0.1% |
| 12 | Drift Staked SOL | Liquid Staking | $332.15M | -2.3% | -0.9% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.6% · Lending 16.7% · Dexs 15.4% · Derivatives 5.0% · Risk Curators 4.0% · Staking Pool 3.9%

### Tokenised assets

$893.05M of tokenised real-world assets and equities are locked on Solana - 5.117% of chain TVL.

- OnRe (RWA): $293.07M
- Huma (RWA): $255.70M
- Solstice (Basis Trading): $211.86M
- JupUSD (Basis Trading): $48.33M
- Plume Vaults (RWA): $32.76M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) - Thu, 01 Oct 2026 09:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-07
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-06
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-06
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-06
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-06
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-05
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05

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

### Change over 24h (vs run at 2026-10-06T12:19:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,451.96 | 4,150.69 | -6.77% |
| Average non-vote TPS | 1,940.48 | 1,657.06 | -14.61% |
| Average slot time (ms) | 266.50 | 268.60 | +0.79% |
| Active validators | 672.00 | 670.00 | -0.30% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 6,784,753,894.00 | 6,507,392,132.00 | -4.09% |
| SOL price | 120.40 | 117.28 | -2.59% |
| Stablecoin supply | 17,051,522,484.00 | 16,916,603,331.00 | -0.79% |
| 24h DEX volume | 2,057,146,062.50 | 2,052,545,605.65 | -0.22% |
| 24h chain fees | 15,987,778.12 | 16,043,229.31 | +0.35% |

### Change over 7d (vs run at 2026-09-30T11:28:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,060.70 | 4,150.69 | +2.22% |
| Average non-vote TPS | 1,550.42 | 1,657.06 | +6.88% |
| Average slot time (ms) | 267.10 | 268.60 | +0.56% |
| Active validators | 672.00 | 670.00 | -0.30% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 6,505,973,320.00 | 6,507,392,132.00 | +0.02% |
| SOL price | 119.51 | 117.28 | -1.87% |
| Stablecoin supply | 16,480,011,986.00 | 16,916,603,331.00 | +2.65% |
| 24h DEX volume | 2,534,247,588.84 | 2,052,545,605.65 | -19.01% |
| 24h chain fees | 14,744,507.17 | 16,043,229.31 | +8.81% |

### Change over 30d (vs run at 2026-09-07T20:51:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,930.66 | 4,150.69 | +5.60% |
| Average non-vote TPS | 1,809.47 | 1,657.06 | -8.42% |
| Average slot time (ms) | 316.70 | 268.60 | -15.19% |
| Active validators | 676.00 | 670.00 | -0.89% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 5,896,988,391.00 | 6,507,392,132.00 | +10.35% |
| SOL price | 104.08 | 117.28 | +12.68% |
| Stablecoin supply | 16,741,090,548.00 | 16,916,603,331.00 | +1.05% |
| 24h DEX volume | 2,904,503,252.44 | 2,052,545,605.65 | -29.33% |
| 24h chain fees | 14,655,299.70 | 16,043,229.31 | +9.47% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
