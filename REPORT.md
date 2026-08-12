# Solana Ecosystem Pulse

**Generated:** 2026-08-12T18:43:42Z · **Schema:** `1.0.0` · **Collection time:** 15.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.94 | +1.08% |
| Market cap | $44.24B | rank #7 |
| Total value locked | $4.82B | -0.14% |
| Stablecoin supply | $16.30B | -0.17% |
| DEX volume (24h) | $1.65B | +4.35% |
| Chain fees / REV (24h) | $9.98M | -4.93% |
| Non-vote TPS (1h avg) | 3,054 | peak 5,566 total |
| Active validators | 685 | 14 delinquent |
| Epoch 1015 | 89.19% complete | 46,679 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 28 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Delinquent validators is above its recent norm | Current 14.00 sits 6.3 sigma above the median of the last 28 runs (7.00, +100.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 685.00 sits 4.0 sigma below the median of the last 28 runs (691.00, -0.9%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 3,053.8 average over the last 60 minutes; 2,538.8 in the latest sample.
- **Total TPS:** 4,654.0 average, 5,566.1 peak. Consensus votes account for 34.4% of all transactions.
- **Slot time:** 422.3 ms average (target 400 ms), worst 1-minute bucket 444.4 ms.
- **Block height:** 416,917,343 at absolute slot 438,865,321.
- **Epoch 1015:** slot 385,321 of 432,000 (89.19% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.702% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 79 ms |
| `solana-rpc.publicnode.com` | yes | 28 ms |
| `api.mainnet.solana.com` | yes | 122 ms |

## Validators & stake

- **685 active** validators, **14 delinquent** (2.00% by count, 0.186% by stake).
- **Total stake:** 434,931,021 SOL ($33.03B); stake rate 68.82% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.34%; 254 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,988,468 | 3.913% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,978,711 | 3.681% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,007 | 2.878% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,334,140 | 2.841% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,151,705 | 2.108% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,964,622 | 2.065% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,172,871 | 1.883% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,954,158 | 1.832% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,367,684 | 1.697% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,577,941 | 1.515% | 0% |

## Economics

- **SOL:** $75.94 (+1.08% 24h, +1.91% 7d, +1.87% 30d). Market cap $44.24B, 24h volume $1.36B (3.07% of cap). Price source: `coingecko`.
- **TVL:** $4.82B across 321 protocols - rank #4 of 461 chains, 6.39% of all tracked chain TVL. +0.55% over 7d, -63.5% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-1.63% 7d) - $3.38 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.65B in 24h, $10.45B over 7d across 114 venues. Volume/TVL turnover 0.343x per day.
- **REV (chain fees):** $9.98M in 24h, $233.00M over 30d. Retained chain revenue $4.85M (48.6% of fees). Annualised fees are 8.23% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,499,452 SOL circulating of 632,008,518 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.12B | +1.2% | +3.1% |
| 2 | Kamino Lend | Lending | $1.05B | +0.7% | +0.6% |
| 3 | Jupiter Lend | Lending | $935.40M | +0.1% | +1.2% |
| 4 | Raydium AMM | Dexs | $843.14M | +0.8% | +2.6% |
| 5 | Binance Staked SOL | Liquid Staking | $779.50M | +1.4% | +3.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $756.21M | +0.9% | +3.2% |
| 7 | BlackRock BUIDL | RWA | $728.23M | +2.1% | +7.7% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $691.35M | +0.3% | -1.8% |
| 9 | Solstice | Basis Trading | $505.96M | +0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $391.70M | +0.9% | +2.0% |
| 11 | xStocks | RWA | $373.79M | +0.1% | +0.8% |
| 12 | Sentora | Risk Curators | $368.81M | +0.2% | -0.8% |

The top five protocols hold 35.3% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.6% · Lending 16.6% · RWA 13.8% · Dexs 13.5% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 18.144% of chain TVL.

- BlackRock BUIDL (RWA): $728.23M
- Solstice (Basis Trading): $505.96M
- xStocks (RWA): $373.79M
- OnRe (RWA): $256.13M
- Ondo Yield Assets (RWA): $178.81M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **990.7 unique fee payers** signed per block (1,402 distinct addresses in the union, 52.8% overlap between blocks).

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

- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-12
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

### Change over 24h (vs run at 2026-08-11T18:43:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,160.34 | 4,653.97 | +11.87% |
| Average non-vote TPS | 2,542.89 | 3,053.77 | +20.09% |
| Average slot time (ms) | 422.60 | 422.30 | -0.07% |
| Active validators | 690.00 | 685.00 | -0.72% |
| Delinquent validators | 9.00 | 14.00 | +55.56% |
| Solana TVL | 4,798,590,463.00 | 4,816,384,183.00 | +0.37% |
| SOL price | 75.13 | 75.94 | +1.08% |
| Stablecoin supply | 16,322,733,028.00 | 16,295,860,195.00 | -0.16% |
| 24h DEX volume | 1,581,973,855.56 | 1,650,837,789.28 | +4.35% |
| 24h chain fees | 10,493,090.03 | 9,976,052.23 | -4.93% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 4,653.97 | +23.28% |
| Average non-vote TPS | 2,150.39 | 3,053.77 | +42.01% |
| Average slot time (ms) | 422.90 | 422.30 | -0.14% |
| Active validators | 693.00 | 685.00 | -1.15% |
| Delinquent validators | 7.00 | 14.00 | +100.00% |
| Solana TVL | 4,739,955,873.00 | 4,816,384,183.00 | +1.61% |
| SOL price | 72.58 | 75.94 | +4.63% |
| Stablecoin supply | 16,197,749,831.00 | 16,295,860,195.00 | +0.61% |
| 24h DEX volume | 1,636,927,091.91 | 1,650,837,789.28 | +0.85% |
| 24h chain fees | 7,777,648.77 | 9,976,052.23 | +28.27% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
