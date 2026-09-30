# Solana Ecosystem Pulse

**Generated:** 2026-09-30T11:28:09Z · **Schema:** `1.0.0` · **Collection time:** 16.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.51 | +0.15% |
| Market cap | $70.29B | rank #7 |
| Total value locked | $6.51B | +0.77% |
| Stablecoin supply | $16.48B | -1.07% |
| DEX volume (24h) | $2.53B | -4.80% |
| Chain fees / REV (24h) | $14.74M | -15.82% |
| Non-vote TPS (1h avg) | 1,550 | peak 4,796 total |
| Active validators | 672 | 11 delinquent |
| Epoch 1046 | 18.31% complete | 352,911 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 97 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,550.4 average over the last 60 minutes; 1,708.2 in the latest sample.
- **Total TPS:** 4,060.7 average, 4,795.6 peak. Consensus votes account for 61.8% of all transactions.
- **Slot time:** 267.1 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 429,990,461 at absolute slot 451,951,089.
- **Epoch 1046:** slot 79,089 of 432,000 (18.31% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.624% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 127 ms |
| `solana-rpc.publicnode.com` | yes | 180 ms |
| `api.mainnet.solana.com` | yes | 88 ms |

## Validators & stake

- **672 active** validators, **11 delinquent** (1.61% by count, 0.040% by stake).
- **Total stake:** 440,549,645 SOL ($52.65B); stake rate 69.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.57% of active stake.
- **Commission:** median 5.0%, mean 12.58%; 230 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,227,376 | 3.912% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,893,945 | 3.609% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,668 | 2.800% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,384,141 | 2.585% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,206,135 | 2.545% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,721 | 2.102% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,232,740 | 2.097% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,652,675 | 1.738% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,092,577 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,513,562 | 1.479% | 0% |

## Economics

- **SOL:** $119.51 (+0.15% 24h, +1.64% 7d, +15.33% 30d). Market cap $70.29B, 24h volume $3.69B (5.25% of cap). Price source: `coingecko`.
- **TVL:** $6.51B across 331 protocols - rank #2 of 467 chains, 6.86% of all tracked chain TVL. -0.43% over 7d, -50.9% from its ATH.
- **Stablecoins:** $16.48B circulating on Solana (-1.32% 7d) - $2.53 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.53B in 24h, $16.90B over 7d across 127 venues. Volume/TVL turnover 0.390x per day.
- **REV (chain fees):** $14.74M in 24h, $415.67M over 30d. Retained chain revenue $6.11M (41.4% of fees). Annualised fees are 7.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,005,919 SOL circulating of 634,996,292 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | -1.7% | +1.8% |
| 2 | Kamino Lend | Lending | $1.38B | -1.9% | -3.6% |
| 3 | Raydium AMM | Dexs | $1.35B | +0.4% | +0.2% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -1.6% | -0.1% |
| 5 | Jupiter Lend | Lending | $1.21B | +3.6% | +1.9% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | -1.6% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $797.42M | -2.2% | -3.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.82M | -1.6% | -0.7% |
| 9 | Marinade Native | Staking Pool | $446.61M | -3.5% | -1.4% |
| 10 | PumpSwap | Dexs | $393.18M | -0.2% | +3.0% |
| 11 | Sentora Curator | Risk Curators | $349.59M | -3.1% | -3.7% |
| 12 | Drift Staked SOL | Liquid Staking | $332.89M | -1.6% | -0.4% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.87B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.1% · Dexs 16.0% · Derivatives 5.2% · Staking Pool 4.0% · Risk Curators 3.3%

### Tokenised assets

$834.83M of tokenised real-world assets and equities are locked on Solana - 4.949% of chain TVL.

- OnRe (RWA): $291.98M
- Solstice (Basis Trading): $214.73M
- Huma (RWA): $206.12M
- JupUSD (Basis Trading): $45.15M
- Plume Vaults (RWA): $25.70M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-29
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-09-28

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

### Change over 24h (vs run at 2026-09-29T11:41:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,822.03 | 4,060.70 | +6.24% |
| Average non-vote TPS | 1,301.12 | 1,550.42 | +19.16% |
| Average slot time (ms) | 266.70 | 267.10 | +0.15% |
| Active validators | 674.00 | 672.00 | -0.30% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 6,514,543,463.00 | 6,505,973,320.00 | -0.13% |
| SOL price | 119.76 | 119.51 | -0.21% |
| Stablecoin supply | 16,661,562,798.00 | 16,480,011,986.00 | -1.09% |
| 24h DEX volume | 2,635,172,514.25 | 2,534,247,588.84 | -3.83% |
| 24h chain fees | 17,397,216.35 | 14,744,507.17 | -15.25% |

### Change over 7d (vs run at 2026-09-23T10:22:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,085.13 | 4,060.70 | -0.60% |
| Average non-vote TPS | 1,543.26 | 1,550.42 | +0.46% |
| Average slot time (ms) | 264.90 | 267.10 | +0.83% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 6,548,550,262.00 | 6,505,973,320.00 | -0.65% |
| SOL price | 117.38 | 119.51 | +1.81% |
| Stablecoin supply | 16,880,437,780.00 | 16,480,011,986.00 | -2.37% |
| 24h DEX volume | 3,449,152,862.76 | 2,534,247,588.84 | -26.53% |
| 24h chain fees | 17,843,164.76 | 14,744,507.17 | -17.37% |

### Change over 30d (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 4,060.70 | -6.19% |
| Average non-vote TPS | 2,195.90 | 1,550.42 | -29.39% |
| Average slot time (ms) | 317.20 | 267.10 | -15.79% |
| Active validators | 681.00 | 672.00 | -1.32% |
| Delinquent validators | 16.00 | 11.00 | -31.25% |
| Solana TVL | 5,791,254,029.00 | 6,505,973,320.00 | +12.34% |
| SOL price | 104.61 | 119.51 | +14.24% |
| Stablecoin supply | 16,123,089,134.00 | 16,480,011,986.00 | +2.21% |
| 24h DEX volume | 1,929,632,644.74 | 2,534,247,588.84 | +31.33% |
| 24h chain fees | 12,307,328.44 | 14,744,507.17 | +19.80% |

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
