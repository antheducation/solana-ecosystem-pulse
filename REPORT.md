# Solana Ecosystem Pulse

**Generated:** 2026-10-01T02:45:11Z · **Schema:** `1.0.0` · **Collection time:** 17.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.98 | -1.22% |
| Market cap | $69.35B | rank #7 |
| Total value locked | $6.53B | -0.70% |
| Stablecoin supply | $16.40B | -0.52% |
| DEX volume (24h) | $2.54B | +0.41% |
| Chain fees / REV (24h) | $15.84M | +7.90% |
| Non-vote TPS (1h avg) | 2,062 | peak 5,200 total |
| Active validators | 673 | 10 delinquent |
| Epoch 1046 | 65.85% complete | 147,532 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 97 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,062.2 average over the last 60 minutes; 1,945.6 in the latest sample.
- **Total TPS:** 4,555.1 average, 5,200.4 peak. Consensus votes account for 54.7% of all transactions.
- **Slot time:** 268.1 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 430,195,585 at absolute slot 452,156,468.
- **Epoch 1046:** slot 284,468 of 432,000 (65.85% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.624% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 254 ms |
| `solana-rpc.publicnode.com` | yes | 126 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **673 active** validators, **10 delinquent** (1.46% by count, 0.048% by stake).
- **Total stake:** 440,549,645 SOL ($51.98B); stake rate 69.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.57% of active stake.
- **Commission:** median 5.0%, mean 12.98%; 228 validators at 0% and 64 at 100%.

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

- **SOL:** $117.98 (-1.22% 24h, +2.86% 7d, +14.36% 30d). Market cap $69.35B, 24h volume $4.25B (6.12% of cap). Price source: `coingecko`.
- **TVL:** $6.53B across 334 protocols - rank #2 of 468 chains, 6.88% of all tracked chain TVL. +2.10% over 7d, -50.7% from its ATH.
- **Stablecoins:** $16.40B circulating on Solana (+0.93% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.54B in 24h, $15.80B over 7d across 126 venues. Volume/TVL turnover 0.390x per day.
- **REV (chain fees):** $15.84M in 24h, $412.90M over 30d. Retained chain revenue $5.93M (37.5% of fees). Annualised fees are 8.34% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,005,256 SOL circulating of 634,995,610 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | -0.8% | +3.4% |
| 2 | Kamino Lend | Lending | $1.38B | -2.8% | -2.3% |
| 3 | Raydium AMM | Dexs | $1.33B | -0.6% | +2.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -0.7% | +2.9% |
| 5 | Jupiter Lend | Lending | $1.21B | -0.6% | +3.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | -0.7% | +2.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $803.70M | -0.6% | -0.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $609.04M | -0.7% | +2.0% |
| 9 | Marinade Native | Staking Pool | $444.65M | -0.7% | +0.4% |
| 10 | Sentora Curator | Risk Curators | $398.69M | +13.7% | +10.0% |
| 11 | PumpSwap | Dexs | $392.64M | -0.2% | +4.9% |
| 12 | Drift Staked SOL | Liquid Staking | $332.99M | -0.7% | +2.5% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.23B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.9% · Lending 16.8% · Dexs 15.7% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.5%

### Tokenised assets

$835.19M of tokenised real-world assets and equities are locked on Solana - 4.849% of chain TVL.

- OnRe (RWA): $291.14M
- Solstice (Basis Trading): $214.42M
- Huma (RWA): $207.51M
- JupUSD (Basis Trading): $45.14M
- Plume Vaults (RWA): $25.82M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT

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
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-30
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28

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

### Change over 24h (vs run at 2026-09-30T02:40:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,170.00 | 4,555.14 | +9.24% |
| Average non-vote TPS | 1,651.28 | 2,062.19 | +24.88% |
| Average slot time (ms) | 266.90 | 268.10 | +0.45% |
| Active validators | 674.00 | 673.00 | -0.15% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 6,566,587,611.00 | 6,528,079,711.00 | -0.59% |
| SOL price | 119.30 | 117.98 | -1.11% |
| Stablecoin supply | 16,470,357,789.00 | 16,397,665,769.00 | -0.44% |
| 24h DEX volume | 2,660,710,413.84 | 2,544,678,619.73 | -4.36% |
| 24h chain fees | 14,607,667.17 | 15,842,342.66 | +8.45% |

### Change over 7d (vs run at 2026-09-24T01:53:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,513.62 | 4,555.14 | +0.92% |
| Average non-vote TPS | 1,982.83 | 2,062.19 | +4.00% |
| Average slot time (ms) | 265.70 | 268.10 | +0.90% |
| Active validators | 675.00 | 673.00 | -0.30% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 6,391,344,724.00 | 6,528,079,711.00 | +2.14% |
| SOL price | 114.66 | 117.98 | +2.90% |
| Stablecoin supply | 16,427,876,539.00 | 16,397,665,769.00 | -0.18% |
| 24h DEX volume | 2,682,816,608.00 | 2,544,678,619.73 | -5.15% |
| 24h chain fees | 17,125,745.95 | 15,842,342.66 | -7.49% |

### Change over 30d (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 4,555.14 | +5.24% |
| Average non-vote TPS | 2,195.90 | 2,062.19 | -6.09% |
| Average slot time (ms) | 317.20 | 268.10 | -15.48% |
| Active validators | 681.00 | 673.00 | -1.17% |
| Delinquent validators | 16.00 | 10.00 | -37.50% |
| Solana TVL | 5,791,254,029.00 | 6,528,079,711.00 | +12.72% |
| SOL price | 104.61 | 117.98 | +12.78% |
| Stablecoin supply | 16,123,089,134.00 | 16,397,665,769.00 | +1.70% |
| 24h DEX volume | 1,929,632,644.74 | 2,544,678,619.73 | +31.87% |
| 24h chain fees | 12,307,328.44 | 15,842,342.66 | +28.72% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
