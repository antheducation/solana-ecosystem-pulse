# Solana Ecosystem Pulse

**Generated:** 2026-08-07T12:35:20Z · **Schema:** `1.0.0` · **Collection time:** 21.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $73.86 | +0.82% |
| Market cap | $43.00B | rank #7 |
| Total value locked | $4.73B | -1.31% |
| Stablecoin supply | $16.25B | +0.32% |
| DEX volume (24h) | $1.38B | -15.75% |
| Chain fees / REV (24h) | $8.90M | +14.48% |
| Non-vote TPS (1h avg) | 1,794 | peak 5,067 total |
| Active validators | 692 | 8 delinquent |
| Epoch 1013 | 40.08% complete | 258,861 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 7 historical runs, sigma = 3.0).

Critical 0 · Serious 4 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 3,421.98 sits 56.1 sigma below the median of the last 7 runs (3,779.46, -9.5%). | `zscore` |
| [SERIOUS] | Average non-vote TPS is below its recent norm | Current 1,794.41 sits 61.6 sigma below the median of the last 7 runs (2,154.20, -16.7%). | `zscore` |
| [SERIOUS] | Solana TVL is below its recent norm | Current 4,726,921,817.00 sits 110.7 sigma below the median of the last 7 runs (4,739,955,873.00, -0.3%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 73.86 sits 16.1 sigma above the median of the last 7 runs (72.67, +1.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,794.4 average over the last 60 minutes; 2,191.1 in the latest sample.
- **Total TPS:** 3,422.0 average, 5,066.6 peak. Consensus votes account for 47.6% of all transactions.
- **Slot time:** 422.6 ms average (target 400 ms), worst 1-minute bucket 438.0 ms.
- **Block height:** 415,843,202 at absolute slot 437,789,139.
- **Epoch 1013:** slot 173,139 of 432,000 (40.08% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.708% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 380 ms |
| `solana-rpc.publicnode.com` | yes | 151 ms |
| `api.mainnet.solana.com` | yes | 229 ms |

## Validators & stake

- **692 active** validators, **8 delinquent** (1.14% by count, 0.063% by stake).
- **Total stake:** 434,839,888 SOL ($32.12B); stake rate 68.83% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.73% of active stake.
- **Commission:** median 5.0%, mean 12.06%; 262 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,882,234 | 3.885% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,996,914 | 3.681% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,487,724 | 2.874% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,275,239 | 2.825% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,139,569 | 2.103% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,868,459 | 2.041% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,166,427 | 1.879% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,921,632 | 1.823% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,637,450 | 1.757% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,569,156 | 1.512% | 0% |

## Economics

- **SOL:** $73.86 (+0.82% 24h, +0.54% 7d, -4.66% 30d). Market cap $43.00B, 24h volume $1.42B (3.31% of cap). Price source: `coingecko`.
- **TVL:** $4.73B across 321 protocols - rank #4 of 461 chains, 6.26% of all tracked chain TVL. -1.79% over 7d, -64.2% from its ATH.
- **Stablecoins:** $16.25B circulating on Solana (-0.66% 7d) - $3.44 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.38B in 24h, $10.83B over 7d across 114 venues. Volume/TVL turnover 0.292x per day.
- **REV (chain fees):** $8.90M in 24h, $219.01M over 30d. Retained chain revenue $3.73M (41.9% of fees). Annualised fees are 7.56% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,051,945 SOL circulating of 631,756,565 total (92.13%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.08B | -0.0% | -1.1% |
| 2 | Kamino Lend | Lending | $1.03B | -0.7% | -1.7% |
| 3 | Jupiter Lend | Lending | $902.26M | -3.4% | -3.3% |
| 4 | Raydium AMM | Dexs | $815.67M | +0.6% | -1.6% |
| 5 | Binance Staked SOL | Liquid Staking | $748.39M | +0.3% | -1.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $731.07M | +0.4% | -1.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $701.04M | -0.2% | -1.5% |
| 8 | BlackRock BUIDL | RWA | $697.09M | +1.7% | +6.6% |
| 9 | Solstice | Basis Trading | $506.54M | +0.1% | -3.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $380.01M | -0.4% | -1.9% |
| 11 | Sentora | Risk Curators | $369.27M | -0.1% | +0.2% |
| 12 | xStocks | RWA | $368.58M | +0.7% | +2.4% |

The top five protocols hold 34.9% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.10B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.2% · Lending 16.5% · RWA 13.8% · Dexs 13.4% · Derivatives 6.1% · Basis Trading 4.5%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 18.316% of chain TVL.

- BlackRock BUIDL (RWA): $697.09M
- Solstice (Basis Trading): $506.54M
- xStocks (RWA): $368.58M
- OnRe (RWA): $251.58M
- Ondo Yield Assets (RWA): $178.93M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,095.7 unique fee payers** signed per block (1,675 distinct addresses in the union, 49.0% overlap between blocks).

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
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |
| [v4.2.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-beta.2) | 2026-07-17 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-07-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22

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

### Change over 24h (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,421.98 | -9.36% |
| Average non-vote TPS | 2,150.39 | 1,794.41 | -16.55% |
| Average slot time (ms) | 422.90 | 422.60 | -0.07% |
| Active validators | 693.00 | 692.00 | -0.14% |
| Delinquent validators | 7.00 | 8.00 | +14.29% |
| Solana TVL | 4,739,955,873.00 | 4,726,921,817.00 | -0.27% |
| SOL price | 72.58 | 73.86 | +1.76% |
| Stablecoin supply | 16,197,749,831.00 | 16,250,441,977.00 | +0.33% |
| 24h DEX volume | 1,636,927,091.91 | 1,379,094,026.18 | -15.75% |
| 24h chain fees | 7,777,648.77 | 8,904,173.12 | +14.48% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 21.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
