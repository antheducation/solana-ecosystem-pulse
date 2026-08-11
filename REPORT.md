# Solana Ecosystem Pulse

**Generated:** 2026-08-11T00:45:31Z · **Schema:** `1.0.0` · **Collection time:** 16.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.81 | -0.60% |
| Market cap | $44.16B | rank #7 |
| Total value locked | $4.83B | +0.74% |
| Stablecoin supply | $16.32B | +0.37% |
| DEX volume (24h) | $1.53B | +13.34% |
| Chain fees / REV (24h) | $9.37M | +2.42% |
| Non-vote TPS (1h avg) | 1,807 | peak 4,068 total |
| Active validators | 691 | 7 delinquent |
| Epoch 1015 | 6.09% complete | 405,685 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 21 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply is above its recent norm | Current 16,316,491,104.00 sits 5.1 sigma above the median of the last 21 runs (16,249,875,303.00, +0.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,807.3 average over the last 60 minutes; 1,623.8 in the latest sample.
- **Total TPS:** 3,442.1 average, 4,068.1 peak. Consensus votes account for 47.5% of all transactions.
- **Slot time:** 420.1 ms average (target 400 ms), worst 1-minute bucket 444.4 ms.
- **Block height:** 416,560,071 at absolute slot 438,506,315.
- **Epoch 1015:** slot 26,315 of 432,000 (6.09% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.702% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 368 ms |
| `solana-rpc.publicnode.com` | yes | 56 ms |
| `api.mainnet.solana.com` | yes | 192 ms |

## Validators & stake

- **691 active** validators, **7 delinquent** (1.00% by count, 0.007% by stake).
- **Total stake:** 434,931,021 SOL ($32.97B); stake rate 68.82% of total supply.
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

- **SOL:** $75.81 (-0.60% 24h, +3.17% 7d, -1.18% 30d). Market cap $44.16B, 24h volume $1.38B (3.13% of cap). Price source: `coingecko`.
- **TVL:** $4.83B across 320 protocols - rank #3 of 461 chains, 6.42% of all tracked chain TVL. +2.13% over 7d, -63.4% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+0.47% 7d) - $3.38 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.53B in 24h, $9.43B over 7d across 114 venues. Volume/TVL turnover 0.316x per day.
- **REV (chain fees):** $9.37M in 24h, $220.33M over 30d. Retained chain revenue $4.40M (47.0% of fees). Annualised fees are 7.74% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,481,936 SOL circulating of 632,009,950 total (92.16%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.12B | -0.8% | +3.6% |
| 2 | Kamino Lend | Lending | $1.05B | +0.3% | +1.2% |
| 3 | Jupiter Lend | Lending | $931.27M | +1.2% | +2.2% |
| 4 | Raydium AMM | Dexs | $845.23M | -0.8% | +3.6% |
| 5 | Binance Staked SOL | Liquid Staking | $778.79M | -0.5% | +4.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $759.80M | -0.9% | +4.0% |
| 7 | BlackRock BUIDL | RWA | $712.85M | +0.1% | +5.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $694.42M | -3.1% | -0.9% |
| 9 | Solstice | Basis Trading | $506.56M | -0.0% | -2.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $393.45M | -0.3% | +3.3% |
| 11 | xStocks | RWA | $371.14M | +0.7% | +2.1% |
| 12 | Sentora | Risk Curators | $368.93M | +0.2% | -0.2% |

The top five protocols hold 35.2% of Solana's tracked TVL. Summed across all 320 protocols the total is $13.42B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.6% · Lending 16.5% · RWA 13.7% · Dexs 13.5% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.42B of tokenised real-world assets and equities are locked on Solana - 18.035% of chain TVL.

- BlackRock BUIDL (RWA): $712.85M
- Solstice (Basis Trading): $506.56M
- xStocks (RWA): $371.14M
- OnRe (RWA): $254.94M
- Ondo Yield Assets (RWA): $178.45M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **971.0 unique fee payers** signed per block (1,385 distinct addresses in the union, 52.5% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle) - Tue, 04 Aug 2026 13:05:00 GMT
- [Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles) - Fri, 31 Jul 2026 10:00:00 GMT

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

### Change over 24h (vs run at 2026-08-10T00:45:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,742.49 | 3,442.06 | -8.03% |
| Average non-vote TPS | 2,126.27 | 1,807.32 | -15.00% |
| Average slot time (ms) | 424.20 | 420.10 | -0.97% |
| Active validators | 691.00 | 691.00 | +0.00% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,869,439,966.00 | 4,827,587,784.00 | -0.86% |
| SOL price | 76.37 | 75.81 | -0.73% |
| Stablecoin supply | 16,255,726,010.00 | 16,316,491,104.00 | +0.37% |
| 24h DEX volume | 1,493,144,029.54 | 1,527,198,724.71 | +2.28% |
| 24h chain fees | 9,422,790.90 | 9,367,889.06 | -0.58% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,442.06 | -8.82% |
| Average non-vote TPS | 2,150.39 | 1,807.32 | -15.95% |
| Average slot time (ms) | 422.90 | 420.10 | -0.66% |
| Active validators | 693.00 | 691.00 | -0.29% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,739,955,873.00 | 4,827,587,784.00 | +1.85% |
| SOL price | 72.58 | 75.81 | +4.45% |
| Stablecoin supply | 16,197,749,831.00 | 16,316,491,104.00 | +0.73% |
| 24h DEX volume | 1,636,927,091.91 | 1,527,198,724.71 | -6.70% |
| 24h chain fees | 7,777,648.77 | 9,367,889.06 | +20.45% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 16.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
