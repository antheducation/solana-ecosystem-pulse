# Solana Ecosystem Pulse

**Generated:** 2026-09-29T21:34:58Z · **Schema:** `1.0.0` · **Collection time:** 18.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.62 | +0.33% |
| Market cap | $69.73B | rank #7 |
| Total value locked | $6.52B | -1.77% |
| Stablecoin supply | $16.66B | -0.36% |
| DEX volume (24h) | $2.66B | +38.18% |
| Chain fees / REV (24h) | $17.51M | +13.56% |
| Non-vote TPS (1h avg) | 2,239 | peak 5,318 total |
| Active validators | 673 | 10 delinquent |
| Epoch 1045 | 75.02% complete | 107,917 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,239.2 average over the last 60 minutes; 2,298.0 in the latest sample.
- **Total TPS:** 4,737.1 average, 5,317.6 peak. Consensus votes account for 52.7% of all transactions.
- **Slot time:** 268.6 ms average (target 400 ms), worst 1-minute bucket 283.0 ms.
- **Block height:** 429,803,557 at absolute slot 451,764,083.
- **Epoch 1045:** slot 324,083 of 432,000 (75.02% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 174 ms |
| `solana-rpc.publicnode.com` | yes | 114 ms |
| `api.mainnet.solana.com` | yes | 150 ms |

## Validators & stake

- **673 active** validators, **10 delinquent** (1.46% by count, 0.079% by stake).
- **Total stake:** 441,249,792 SOL ($52.34B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.47% and top 33 hold 45.55% of active stake.
- **Commission:** median 5.0%, mean 12.83%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.043% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.603% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.798% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.563% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.542% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.732% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.520% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.478% | 0% |

## Economics

- **SOL:** $118.62 (+0.33% 24h, +0.56% 7d, +13.22% 30d). Market cap $69.73B, 24h volume $3.69B (5.29% of cap). Price source: `coingecko`.
- **TVL:** $6.52B across 331 protocols - rank #2 of 467 chains, 6.86% of all tracked chain TVL. +0.97% over 7d, -50.7% from its ATH.
- **Stablecoins:** $16.66B circulating on Solana (-2.97% 7d) - $2.55 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.66B in 24h, $17.56B over 7d across 127 venues. Volume/TVL turnover 0.408x per day.
- **REV (chain fees):** $17.51M in 24h, $412.12M over 30d. Retained chain revenue $5.87M (33.5% of fees). Annualised fees are 9.17% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,851,399 SOL circulating of 634,918,101 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.94B | +0.4% | +2.2% |
| 2 | Kamino Lend | Lending | $1.37B | -5.4% | -3.6% |
| 3 | Raydium AMM | Dexs | $1.34B | -1.1% | +0.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.24B | +0.3% | +0.8% |
| 5 | Jupiter Lend | Lending | $1.22B | +4.6% | +4.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.22B | +0.4% | -0.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $811.00M | +0.5% | -1.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $614.99M | +0.1% | +0.2% |
| 9 | Marinade Native | Staking Pool | $448.64M | -2.1% | -0.5% |
| 10 | PumpSwap | Dexs | $390.05M | -0.9% | +3.5% |
| 11 | Sentora Curator | Risk Curators | $350.67M | -3.1% | -3.3% |
| 12 | Drift Staked SOL | Liquid Staking | $336.18M | +0.3% | +0.5% |

The top five protocols hold 41.9% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.95B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 17.1% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.3%

### Tokenised assets

$830.27M of tokenised real-world assets and equities are locked on Solana - 4.898% of chain TVL.

- OnRe (RWA): $292.23M
- Solstice (Basis Trading): $214.97M
- Huma (RWA): $207.46M
- JupUSD (Basis Trading): $44.07M
- Plume Vaults (RWA): $25.76M

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

### Change over 24h (vs run at 2026-09-28T22:41:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,519.28 | 4,737.06 | +4.82% |
| Average non-vote TPS | 2,010.42 | 2,239.20 | +11.38% |
| Average slot time (ms) | 267.20 | 268.60 | +0.52% |
| Active validators | 674.00 | 673.00 | -0.15% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 6,552,189,378.00 | 6,522,003,878.00 | -0.46% |
| SOL price | 118.18 | 118.62 | +0.37% |
| Stablecoin supply | 16,723,366,837.00 | 16,661,913,603.00 | -0.37% |
| 24h DEX volume | 1,926,466,128.71 | 2,662,061,803.25 | +38.18% |
| 24h chain fees | 15,421,946.25 | 17,514,749.35 | +13.57% |

### Change over 7d (vs run at 2026-09-22T20:34:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,893.52 | 4,737.06 | -3.20% |
| Average non-vote TPS | 2,379.33 | 2,239.20 | -5.89% |
| Average slot time (ms) | 268.00 | 268.60 | +0.22% |
| Active validators | 677.00 | 673.00 | -0.59% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 6,505,534,933.00 | 6,522,003,878.00 | +0.25% |
| SOL price | 118.17 | 118.62 | +0.38% |
| Stablecoin supply | 17,173,484,924.00 | 16,661,913,603.00 | -2.98% |
| 24h DEX volume | 3,428,858,820.75 | 2,662,061,803.25 | -22.36% |
| 24h chain fees | 18,642,402.21 | 17,514,749.35 | -6.05% |

### Change over 30d (vs run at 2026-08-30T20:10:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,293.13 | 4,737.06 | +10.34% |
| Average non-vote TPS | 2,167.90 | 2,239.20 | +3.29% |
| Average slot time (ms) | 318.30 | 268.60 | -15.61% |
| Active validators | 680.00 | 673.00 | -1.03% |
| Delinquent validators | 17.00 | 10.00 | -41.18% |
| Solana TVL | 5,956,176,022.00 | 6,522,003,878.00 | +9.50% |
| SOL price | 105.77 | 118.62 | +12.15% |
| Stablecoin supply | 16,297,776,213.00 | 16,661,913,603.00 | +2.23% |
| 24h DEX volume | 1,670,710,752.31 | 2,662,061,803.25 | +59.34% |
| 24h chain fees | 11,213,986.82 | 17,514,749.35 | +56.19% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
