# Solana Ecosystem Pulse

**Generated:** 2026-08-12T00:53:45Z · **Schema:** `1.0.0` · **Collection time:** 13.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $76.25 | +0.54% |
| Market cap | $44.41B | rank #7 |
| Total value locked | $4.79B | +0.00% |
| Stablecoin supply | $16.32B | +0.05% |
| DEX volume (24h) | $1.65B | +4.36% |
| Chain fees / REV (24h) | $10.81M | +3.07% |
| Non-vote TPS (1h avg) | 2,353 | peak 5,301 total |
| Active validators | 689 | 10 delinquent |
| Epoch 1015 | 53.83% complete | 199,458 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 25 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 10.00 sits 4.3 sigma above the median of the last 25 runs (7.00, +42.9%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,353.2 average over the last 60 minutes; 2,793.6 in the latest sample.
- **Total TPS:** 3,974.2 average, 5,301.1 peak. Consensus votes account for 40.8% of all transactions.
- **Slot time:** 421.9 ms average (target 400 ms), worst 1-minute bucket 458.0 ms.
- **Block height:** 416,766,143 at absolute slot 438,712,542.
- **Epoch 1015:** slot 232,542 of 432,000 (53.83% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.702% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 185 ms |
| `solana-rpc.publicnode.com` | yes | 45 ms |
| `api.mainnet.solana.com` | yes | 62 ms |

## Validators & stake

- **689 active** validators, **10 delinquent** (1.43% by count, 0.095% by stake).
- **Total stake:** 434,931,021 SOL ($33.16B); stake rate 68.82% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.82% of active stake.
- **Commission:** median 5.0%, mean 12.28%; 256 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,988,468 | 3.910% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,978,711 | 3.677% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,007 | 2.876% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,334,140 | 2.839% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,151,705 | 2.106% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,964,622 | 2.063% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,172,871 | 1.881% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,954,158 | 1.831% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,367,684 | 1.696% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,577,941 | 1.514% | 0% |

## Economics

- **SOL:** $76.25 (+0.54% 24h, +3.47% 7d, -0.81% 30d). Market cap $44.41B, 24h volume $1.37B (3.09% of cap). Price source: `coingecko`.
- **TVL:** $4.79B across 320 protocols - rank #4 of 461 chains, 6.39% of all tracked chain TVL. -0.05% over 7d, -63.8% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (-0.58% 7d) - $3.41 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.65B in 24h, $10.28B over 7d across 114 venues. Volume/TVL turnover 0.345x per day.
- **REV (chain fees):** $10.81M in 24h, $225.41M over 30d. Retained chain revenue $4.41M (40.8% of fees). Annualised fees are 8.89% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,500,050 SOL circulating of 632,009,116 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | +0.7% | +3.9% |
| 2 | Kamino Lend | Lending | $1.03B | -1.9% | -1.2% |
| 3 | Jupiter Lend | Lending | $907.63M | -2.5% | -1.8% |
| 4 | Raydium AMM | Dexs | $851.38M | +0.7% | +3.6% |
| 5 | Binance Staked SOL | Liquid Staking | $780.73M | +0.2% | +4.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $761.51M | +0.2% | +3.9% |
| 7 | BlackRock BUIDL | RWA | $728.16M | +2.1% | +7.6% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $694.67M | +0.0% | -1.4% |
| 9 | Solstice | Basis Trading | $506.06M | -0.1% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $396.28M | +0.7% | +3.2% |
| 11 | xStocks | RWA | $376.82M | +1.5% | +1.7% |
| 12 | Sentora | Risk Curators | $369.08M | +0.0% | -0.7% |

The top five protocols hold 35.1% of Solana's tracked TVL. Summed across all 320 protocols the total is $13.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.2% · RWA 13.8% · Dexs 13.6% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 18.150% of chain TVL.

- BlackRock BUIDL (RWA): $728.16M
- Solstice (Basis Trading): $506.06M
- xStocks (RWA): $376.82M
- OnRe (RWA): $255.94M
- Ondo Yield Assets (RWA): $178.54M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **953.3 unique fee payers** signed per block (1,311 distinct addresses in the union, 54.2% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle) - Tue, 04 Aug 2026 13:05:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-11
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-07-28

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

### Change over 24h (vs run at 2026-08-11T00:45:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,442.06 | 3,974.24 | +15.46% |
| Average non-vote TPS | 1,807.32 | 2,353.21 | +30.20% |
| Average slot time (ms) | 420.10 | 421.90 | +0.43% |
| Active validators | 691.00 | 689.00 | -0.29% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,827,587,784.00 | 4,787,487,114.00 | -0.83% |
| SOL price | 75.81 | 76.25 | +0.58% |
| Stablecoin supply | 16,316,491,104.00 | 16,324,318,696.00 | +0.05% |
| 24h DEX volume | 1,527,198,724.71 | 1,650,871,367.28 | +8.10% |
| 24h chain fees | 9,367,889.06 | 10,814,593.52 | +15.44% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,974.24 | +5.27% |
| Average non-vote TPS | 2,150.39 | 2,353.21 | +9.43% |
| Average slot time (ms) | 422.90 | 421.90 | -0.24% |
| Active validators | 693.00 | 689.00 | -0.58% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,739,955,873.00 | 4,787,487,114.00 | +1.00% |
| SOL price | 72.58 | 76.25 | +5.06% |
| Stablecoin supply | 16,197,749,831.00 | 16,324,318,696.00 | +0.78% |
| 24h DEX volume | 1,636,927,091.91 | 1,650,871,367.28 | +0.85% |
| 24h chain fees | 7,777,648.77 | 10,814,593.52 | +39.05% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 13.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
