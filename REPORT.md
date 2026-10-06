# Solana Ecosystem Pulse

**Generated:** 2026-10-06T21:56:40Z · **Schema:** `1.0.0` · **Collection time:** 11.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.95 | +0.13% |
| Market cap | $71.17B | rank #7 |
| Total value locked | $6.62B | -0.18% |
| Stablecoin supply | $17.05B | +0.98% |
| DEX volume (24h) | $2.06B | +20.43% |
| Chain fees / REV (24h) | $16.09M | -0.21% |
| Non-vote TPS (1h avg) | 2,777 | peak 6,188 total |
| Active validators | 670 | 15 delinquent |
| Epoch 1050 | 99.09% complete | 3,931 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,776.8 average over the last 60 minutes; 2,700.4 in the latest sample.
- **Total TPS:** 5,237.2 average, 6,188.5 peak. Consensus votes account for 47.0% of all transactions.
- **Slot time:** 270.7 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 432,065,687 at absolute slot 454,028,069.
- **Epoch 1050:** slot 428,069 of 432,000 (99.09% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.616% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 124 ms |
| `solana-rpc.publicnode.com` | yes | 37 ms |
| `api.mainnet.solana.com` | yes | 133 ms |

## Validators & stake

- **670 active** validators, **15 delinquent** (2.19% by count, 0.150% by stake).
- **Total stake:** 441,738,541 SOL ($53.43B); stake rate 69.53% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.60% and top 33 hold 45.71% of active stake.
- **Commission:** median 5.0%, mean 13.01%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,915,070 | 4.062% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,937,333 | 3.613% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,292,997 | 2.787% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,310,013 | 2.564% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,144,638 | 2.527% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,258,566 | 2.099% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,254,450 | 2.098% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,629,486 | 1.730% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,062,716 | 1.601% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,687,904 | 1.516% | 0% |

## Economics

- **SOL:** $120.95 (+0.13% 24h, +1.62% 7d, +14.43% 30d). Market cap $71.17B, 24h volume $2.56B (3.60% of cap). Price source: `coingecko`.
- **TVL:** $6.62B across 334 protocols - rank #2 of 468 chains, 6.87% of all tracked chain TVL. +2.52% over 7d, -50.0% from its ATH.
- **Stablecoins:** $17.05B circulating on Solana (+2.37% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.06B in 24h, $15.67B over 7d across 126 venues. Volume/TVL turnover 0.311x per day.
- **REV (chain fees):** $16.09M in 24h, $448.32M over 30d. Retained chain revenue $5.86M (36.4% of fees). Annualised fees are 8.25% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,384,878 SOL circulating of 635,304,401 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +1.0% | +3.5% |
| 2 | Kamino Lend | Lending | $1.40B | +0.5% | +0.0% |
| 3 | Raydium AMM | Dexs | $1.35B | -0.1% | +2.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.26B | +0.6% | +2.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.24B | -0.0% | +2.2% |
| 6 | Jupiter Lend | Lending | $1.24B | -11.4% | +6.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $817.00M | +0.1% | +1.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $626.14M | +0.6% | +2.4% |
| 9 | Sentora Curator | Risk Curators | $492.00M | +7.2% | +36.2% |
| 10 | Marinade Native | Staking Pool | $448.92M | +0.4% | -2.0% |
| 11 | PumpSwap | Dexs | $399.94M | +0.0% | +2.8% |
| 12 | Drift Staked SOL | Liquid Staking | $340.85M | +0.5% | +2.0% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.77B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.9% · Lending 16.6% · Dexs 15.4% · Derivatives 5.0% · Risk Curators 4.0% · Staking Pool 3.9%

### Tokenised assets

$892.75M of tokenised real-world assets and equities are locked on Solana - 5.023% of chain TVL.

- OnRe (RWA): $292.96M
- Huma (RWA): $255.27M
- Solstice (Basis Trading): $211.89M
- JupUSD (Basis Trading): $48.58M
- Plume Vaults (RWA): $32.64M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT

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

### Change over 24h (vs run at 2026-10-05T23:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,796.58 | 5,237.18 | +9.19% |
| Average non-vote TPS | 2,304.82 | 2,776.85 | +20.48% |
| Average slot time (ms) | 268.60 | 270.70 | +0.78% |
| Active validators | 672.00 | 670.00 | -0.30% |
| Delinquent validators | 13.00 | 15.00 | +15.38% |
| Solana TVL | 6,781,683,220.00 | 6,619,880,617.00 | -2.39% |
| SOL price | 120.74 | 120.95 | +0.17% |
| Stablecoin supply | 16,885,339,627.00 | 17,052,133,908.00 | +0.99% |
| 24h DEX volume | 1,708,158,585.63 | 2,057,146,062.50 | +20.43% |
| 24h chain fees | 16,123,937.37 | 16,090,422.62 | -0.21% |

### Change over 7d (vs run at 2026-09-29T21:34:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,737.06 | 5,237.18 | +10.56% |
| Average non-vote TPS | 2,239.20 | 2,776.85 | +24.01% |
| Average slot time (ms) | 268.60 | 270.70 | +0.78% |
| Active validators | 673.00 | 670.00 | -0.45% |
| Delinquent validators | 10.00 | 15.00 | +50.00% |
| Solana TVL | 6,522,003,878.00 | 6,619,880,617.00 | +1.50% |
| SOL price | 118.62 | 120.95 | +1.96% |
| Stablecoin supply | 16,661,913,603.00 | 17,052,133,908.00 | +2.34% |
| 24h DEX volume | 2,662,061,803.25 | 2,057,146,062.50 | -22.72% |
| 24h chain fees | 17,514,749.35 | 16,090,422.62 | -8.13% |

### Change over 30d (vs run at 2026-09-06T19:40:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,849.55 | 5,237.18 | +36.05% |
| Average non-vote TPS | 1,725.26 | 2,776.85 | +60.95% |
| Average slot time (ms) | 316.50 | 270.70 | -14.47% |
| Active validators | 676.00 | 670.00 | -0.89% |
| Delinquent validators | 17.00 | 15.00 | -11.76% |
| Solana TVL | 5,924,761,773.00 | 6,619,880,617.00 | +11.73% |
| SOL price | 105.62 | 120.95 | +14.51% |
| Stablecoin supply | 16,686,094,754.00 | 17,052,133,908.00 | +2.19% |
| 24h DEX volume | 1,960,574,882.81 | 2,057,146,062.50 | +4.93% |
| 24h chain fees | 10,482,001.50 | 16,090,422.62 | +53.51% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
