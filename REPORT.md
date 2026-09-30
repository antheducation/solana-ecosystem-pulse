# Solana Ecosystem Pulse

**Generated:** 2026-09-30T02:40:43Z · **Schema:** `1.0.0` · **Collection time:** 14.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.30 | +2.17% |
| Market cap | $70.14B | rank #7 |
| Total value locked | $6.57B | +0.07% |
| Stablecoin supply | $16.47B | -1.13% |
| DEX volume (24h) | $2.66B | -0.05% |
| Chain fees / REV (24h) | $14.61M | -16.60% |
| Non-vote TPS (1h avg) | 1,651 | peak 4,810 total |
| Active validators | 674 | 9 delinquent |
| Epoch 1045 | 90.89% complete | 39,374 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,651.3 average over the last 60 minutes; 1,924.9 in the latest sample.
- **Total TPS:** 4,170.0 average, 4,809.5 peak. Consensus votes account for 60.4% of all transactions.
- **Slot time:** 266.9 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 429,872,082 at absolute slot 451,832,626.
- **Epoch 1045:** slot 392,626 of 432,000 (90.89% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 304 ms |
| `solana-rpc.publicnode.com` | yes | 63 ms |
| `api.mainnet.solana.com` | yes | 157 ms |

## Validators & stake

- **674 active** validators, **9 delinquent** (1.32% by count, 0.051% by stake).
- **Total stake:** 441,249,792 SOL ($52.64B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.54% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.042% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.798% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.562% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.542% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.096% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.732% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.519% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.478% | 0% |

## Economics

- **SOL:** $119.30 (+2.17% 24h, +0.88% 7d, +17.58% 30d). Market cap $70.14B, 24h volume $3.55B (5.06% of cap). Price source: `coingecko`.
- **TVL:** $6.57B across 331 protocols - rank #2 of 467 chains, 6.92% of all tracked chain TVL. +0.43% over 7d, -50.4% from its ATH.
- **Stablecoins:** $16.47B circulating on Solana (-1.38% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.66B in 24h, $15.81B over 7d across 127 venues. Volume/TVL turnover 0.405x per day.
- **REV (chain fees):** $14.61M in 24h, $414.95M over 30d. Retained chain revenue $6.01M (41.2% of fees). Annualised fees are 7.60% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,934,902 SOL circulating of 634,917,888 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.94B | +0.6% | +2.6% |
| 2 | Kamino Lend | Lending | $1.42B | +1.2% | -0.9% |
| 3 | Raydium AMM | Dexs | $1.34B | +1.0% | +0.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.24B | +0.6% | +0.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.22B | +0.4% | +0.5% |
| 6 | Jupiter Lend | Lending | $1.21B | +4.3% | +2.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $808.59M | +0.2% | -1.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.41M | +0.3% | +0.1% |
| 9 | Marinade Native | Staking Pool | $447.55M | -0.7% | -1.2% |
| 10 | PumpSwap | Dexs | $393.52M | +2.2% | +3.0% |
| 11 | Sentora Curator | Risk Curators | $350.58M | -2.9% | -3.4% |
| 12 | Drift Staked SOL | Liquid Staking | $335.34M | +0.4% | +0.4% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.98B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 17.3% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.0% · Risk Curators 3.3%

### Tokenised assets

$830.20M of tokenised real-world assets and equities are locked on Solana - 4.888% of chain TVL.

- OnRe (RWA): $292.22M
- Solstice (Basis Trading): $214.97M
- Huma (RWA): $206.46M
- JupUSD (Basis Trading): $45.06M
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

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-09-29
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

### Change over 24h (vs run at 2026-09-29T02:59:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,432.82 | 4,170.00 | -5.93% |
| Average non-vote TPS | 1,921.08 | 1,651.28 | -14.04% |
| Average slot time (ms) | 267.80 | 266.90 | -0.34% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 6,466,752,849.00 | 6,566,587,611.00 | +1.54% |
| SOL price | 116.86 | 119.30 | +2.09% |
| Stablecoin supply | 16,662,008,171.00 | 16,470,357,789.00 | -1.15% |
| 24h DEX volume | 2,290,100,033.25 | 2,660,710,413.84 | +16.18% |
| 24h chain fees | 17,452,720.35 | 14,607,667.17 | -16.30% |

### Change over 7d (vs run at 2026-09-23T02:05:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,466.71 | 4,170.00 | -6.64% |
| Average non-vote TPS | 1,931.92 | 1,651.28 | -14.53% |
| Average slot time (ms) | 265.70 | 266.90 | +0.45% |
| Active validators | 677.00 | 674.00 | -0.44% |
| Delinquent validators | 12.00 | 9.00 | -25.00% |
| Solana TVL | 6,520,724,463.00 | 6,566,587,611.00 | +0.70% |
| SOL price | 118.05 | 119.30 | +1.06% |
| Stablecoin supply | 16,881,209,444.00 | 16,470,357,789.00 | -2.43% |
| 24h DEX volume | 3,448,899,396.17 | 2,660,710,413.84 | -22.85% |
| 24h chain fees | 17,581,633.45 | 14,607,667.17 | -16.92% |

### Change over 30d (vs run at 2026-08-30T20:10:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,293.13 | 4,170.00 | -2.87% |
| Average non-vote TPS | 2,167.90 | 1,651.28 | -23.83% |
| Average slot time (ms) | 318.30 | 266.90 | -16.15% |
| Active validators | 680.00 | 674.00 | -0.88% |
| Delinquent validators | 17.00 | 9.00 | -47.06% |
| Solana TVL | 5,956,176,022.00 | 6,566,587,611.00 | +10.25% |
| SOL price | 105.77 | 119.30 | +12.79% |
| Stablecoin supply | 16,297,776,213.00 | 16,470,357,789.00 | +1.06% |
| 24h DEX volume | 1,670,710,752.31 | 2,660,710,413.84 | +59.26% |
| 24h chain fees | 11,213,986.82 | 14,607,667.17 | +30.26% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
