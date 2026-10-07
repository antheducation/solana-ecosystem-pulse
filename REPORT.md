# Solana Ecosystem Pulse

**Generated:** 2026-10-07T02:58:07Z · **Schema:** `1.0.0` · **Collection time:** 16.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.29 | -1.58% |
| Market cap | $69.68B | rank #7 |
| Total value locked | $6.62B | -2.46% |
| Stablecoin supply | $16.92B | -0.78% |
| DEX volume (24h) | $2.04B | -0.87% |
| Chain fees / REV (24h) | $16.05M | -0.23% |
| Non-vote TPS (1h avg) | 2,500 | peak 8,055 total |
| Active validators | 673 | 8 delinquent |
| Epoch 1051 | 14.64% complete | 368,772 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,500.3 average over the last 60 minutes; 1,982.2 in the latest sample.
- **Total TPS:** 4,983.1 average, 8,054.6 peak. Consensus votes account for 49.8% of all transactions.
- **Slot time:** 270.1 ms average (target 400 ms), worst 1-minute bucket 295.6 ms.
- **Block height:** 432,132,825 at absolute slot 454,095,228.
- **Epoch 1051:** slot 63,228 of 432,000 (14.64% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.614% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 229 ms |
| `solana-rpc.publicnode.com` | yes | 107 ms |
| `api.mainnet.solana.com` | yes | 247 ms |

## Validators & stake

- **673 active** validators, **8 delinquent** (1.17% by count, 0.004% by stake).
- **Total stake:** 439,343,031 SOL ($51.97B); stake rate 69.15% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 12.67%; 232 validators at 0% and 62 at 100%.

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

- **SOL:** $118.29 (-1.58% 24h, -0.95% 7d, +12.32% 30d). Market cap $69.68B, 24h volume $2.80B (4.01% of cap). Price source: `coingecko`.
- **TVL:** $6.62B across 334 protocols - rank #2 of 468 chains, 6.88% of all tracked chain TVL. +0.77% over 7d, -50.0% from its ATH.
- **Stablecoins:** $16.92B circulating on Solana (+2.63% 7d) - $2.56 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.04B in 24h, $14.33B over 7d across 126 venues. Volume/TVL turnover 0.308x per day.
- **REV (chain fees):** $16.05M in 24h, $450.81M over 30d. Retained chain revenue $5.80M (36.1% of fees). Annualised fees are 8.41% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,094,850 SOL circulating of 635,382,749 total (92.71%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.98B | +0.2% | +2.4% |
| 2 | Kamino Lend | Lending | $1.40B | -0.3% | -1.2% |
| 3 | Raydium AMM | Dexs | $1.35B | -0.2% | +0.3% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.26B | -0.1% | +1.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.24B | -0.1% | +1.6% |
| 6 | Jupiter Lend | Lending | $1.23B | -11.8% | +5.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $815.13M | -0.3% | +0.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $624.63M | -0.0% | +1.8% |
| 9 | Sentora Curator | Risk Curators | $492.01M | +7.6% | +40.3% |
| 10 | Marinade Native | Staking Pool | $449.19M | +0.1% | +0.4% |
| 11 | PumpSwap | Dexs | $405.19M | -0.3% | +2.7% |
| 12 | Drift Staked SOL | Liquid Staking | $339.82M | -0.1% | +1.3% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.74B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.6% · Dexs 15.5% · Derivatives 5.0% · Risk Curators 4.0% · Staking Pool 3.9%

### Tokenised assets

$893.21M of tokenised real-world assets and equities are locked on Solana - 5.034% of chain TVL.

- OnRe (RWA): $293.07M
- Huma (RWA): $255.72M
- Solstice (Basis Trading): $211.88M
- JupUSD (Basis Trading): $48.48M
- Plume Vaults (RWA): $32.69M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026) - Thu, 24 Sep 2026 19:24:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-06
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-06
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

### Change over 24h (vs run at 2026-10-06T03:32:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,576.27 | 4,983.12 | +8.89% |
| Average non-vote TPS | 2,076.07 | 2,500.28 | +20.43% |
| Average slot time (ms) | 267.60 | 270.10 | +0.93% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 6,796,887,845.00 | 6,621,064,757.00 | -2.59% |
| SOL price | 119.95 | 118.29 | -1.38% |
| Stablecoin supply | 17,051,507,064.00 | 16,917,902,048.00 | -0.78% |
| 24h DEX volume | 1,904,732,429.50 | 2,039,240,588.65 | +7.06% |
| 24h chain fees | 16,107,910.12 | 16,053,410.31 | -0.34% |

### Change over 7d (vs run at 2026-09-30T02:40:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,170.00 | 4,983.12 | +19.50% |
| Average non-vote TPS | 1,651.28 | 2,500.28 | +51.41% |
| Average slot time (ms) | 266.90 | 270.10 | +1.20% |
| Active validators | 674.00 | 673.00 | -0.15% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 6,566,587,611.00 | 6,621,064,757.00 | +0.83% |
| SOL price | 119.30 | 118.29 | -0.85% |
| Stablecoin supply | 16,470,357,789.00 | 16,917,902,048.00 | +2.72% |
| 24h DEX volume | 2,660,710,413.84 | 2,039,240,588.65 | -23.36% |
| 24h chain fees | 14,607,667.17 | 16,053,410.31 | +9.90% |

### Change over 30d (vs run at 2026-09-06T19:40:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,849.55 | 4,983.12 | +29.45% |
| Average non-vote TPS | 1,725.26 | 2,500.28 | +44.92% |
| Average slot time (ms) | 316.50 | 270.10 | -14.66% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 17.00 | 8.00 | -52.94% |
| Solana TVL | 5,924,761,773.00 | 6,621,064,757.00 | +11.75% |
| SOL price | 105.62 | 118.29 | +12.00% |
| Stablecoin supply | 16,686,094,754.00 | 16,917,902,048.00 | +1.39% |
| 24h DEX volume | 1,960,574,882.81 | 2,039,240,588.65 | +4.01% |
| 24h chain fees | 10,482,001.50 | 16,053,410.31 | +53.15% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
