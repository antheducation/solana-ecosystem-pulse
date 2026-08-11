# Solana Ecosystem Pulse

**Generated:** 2026-08-11T06:43:16Z · **Schema:** `1.0.0` · **Collection time:** 17.6s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.78 | -1.45% |
| Market cap | $44.14B | rank #7 |
| Total value locked | $4.83B | -0.13% |
| Stablecoin supply | $16.32B | +0.04% |
| DEX volume (24h) | $1.55B | +14.77% |
| Chain fees / REV (24h) | $10.45M | +14.29% |
| Non-vote TPS (1h avg) | 1,405 | peak 3,611 total |
| Active validators | 691 | 7 delinquent |
| Epoch 1015 | 17.86% complete | 354,833 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 22 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply is above its recent norm | Current 16,323,261,006.00 sits 5.8 sigma above the median of the last 22 runs (16,250,158,640.00, +0.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,404.6 average over the last 60 minutes; 1,638.5 in the latest sample.
- **Total TPS:** 3,024.6 average, 3,610.7 peak. Consensus votes account for 53.6% of all transactions.
- **Slot time:** 423.5 ms average (target 400 ms), worst 1-minute bucket 447.8 ms.
- **Block height:** 416,610,876 at absolute slot 438,557,167.
- **Epoch 1015:** slot 77,167 of 432,000 (17.86% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.702% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 247 ms |
| `solana-rpc.publicnode.com` | yes | 148 ms |
| `api.mainnet.solana.com` | yes | 258 ms |

## Validators & stake

- **691 active** validators, **7 delinquent** (1.00% by count, 0.007% by stake).
- **Total stake:** 434,931,021 SOL ($32.96B); stake rate 68.82% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.37% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.09%; 260 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,988,468 | 3.906% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,978,711 | 3.674% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,007 | 2.873% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,334,140 | 2.836% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,151,705 | 2.104% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,964,622 | 2.061% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,172,871 | 1.879% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,954,158 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,367,684 | 1.694% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,577,941 | 1.513% | 0% |

## Economics

- **SOL:** $75.78 (-1.45% 24h, +2.86% 7d, -0.81% 30d). Market cap $44.14B, 24h volume $1.34B (3.04% of cap). Price source: `coingecko`.
- **TVL:** $4.83B across 321 protocols - rank #3 of 461 chains, 6.42% of all tracked chain TVL. +1.72% over 7d, -63.4% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (-0.58% 7d) - $3.38 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.55B in 24h, $10.38B over 7d across 114 venues. Volume/TVL turnover 0.320x per day.
- **REV (chain fees):** $10.45M in 24h, $228.02M over 30d. Retained chain revenue $4.36M (41.7% of fees). Annualised fees are 8.64% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,481,706 SOL circulating of 632,009,765 total (92.16%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.12B | -1.1% | +3.1% |
| 2 | Kamino Lend | Lending | $1.05B | -0.7% | +1.0% |
| 3 | Jupiter Lend | Lending | $936.95M | +1.9% | +2.9% |
| 4 | Raydium AMM | Dexs | $847.33M | -0.3% | +3.9% |
| 5 | Binance Staked SOL | Liquid Staking | $776.32M | -0.8% | +3.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $756.59M | -1.6% | +3.6% |
| 7 | BlackRock BUIDL | RWA | $712.85M | +0.1% | +5.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $693.08M | -3.2% | -1.1% |
| 9 | Solstice | Basis Trading | $506.49M | -0.0% | -2.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $392.00M | -1.1% | +2.9% |
| 11 | xStocks | RWA | $371.11M | -0.6% | +2.1% |
| 12 | Sentora | Risk Curators | $368.68M | +0.1% | -0.3% |

The top five protocols hold 35.3% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.40B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.6% · Lending 16.6% · RWA 13.7% · Dexs 13.6% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.42B of tokenised real-world assets and equities are locked on Solana - 18.050% of chain TVL.

- BlackRock BUIDL (RWA): $712.85M
- Solstice (Basis Trading): $506.49M
- xStocks (RWA): $371.11M
- OnRe (RWA): $255.02M
- Ondo Yield Assets (RWA): $178.53M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,001.7 unique fee payers** signed per block (1,424 distinct addresses in the union, 52.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle) - Tue, 04 Aug 2026 13:05:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Sat, 01 Aug 2026 12:50:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-07-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

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

### Change over 24h (vs run at 2026-08-10T07:04:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,002.24 | 3,024.61 | +0.75% |
| Average non-vote TPS | 1,386.84 | 1,404.61 | +1.28% |
| Average slot time (ms) | 424.10 | 423.50 | -0.14% |
| Active validators | 690.00 | 691.00 | +0.14% |
| Delinquent validators | 8.00 | 7.00 | -12.50% |
| Solana TVL | 4,854,070,595.00 | 4,831,307,533.00 | -0.47% |
| SOL price | 76.90 | 75.78 | -1.46% |
| Stablecoin supply | 16,314,454,803.00 | 16,323,261,006.00 | +0.05% |
| 24h DEX volume | 1,367,879,871.98 | 1,546,444,167.56 | +13.05% |
| 24h chain fees | 8,759,843.77 | 10,453,688.03 | +19.34% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,024.61 | -19.88% |
| Average non-vote TPS | 2,150.39 | 1,404.61 | -34.68% |
| Average slot time (ms) | 422.90 | 423.50 | +0.14% |
| Active validators | 693.00 | 691.00 | -0.29% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,739,955,873.00 | 4,831,307,533.00 | +1.93% |
| SOL price | 72.58 | 75.78 | +4.41% |
| Stablecoin supply | 16,197,749,831.00 | 16,323,261,006.00 | +0.77% |
| 24h DEX volume | 1,636,927,091.91 | 1,546,444,167.56 | -5.53% |
| 24h chain fees | 7,777,648.77 | 10,453,688.03 | +34.41% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
