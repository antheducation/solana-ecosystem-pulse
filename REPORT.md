# Solana Ecosystem Pulse

**Generated:** 2026-08-12T12:39:21Z · **Schema:** `1.0.0` · **Collection time:** 22.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $76.81 | +1.12% |
| Market cap | $44.74B | rank #7 |
| Total value locked | $4.86B | +0.67% |
| Stablecoin supply | $16.30B | -0.17% |
| DEX volume (24h) | $1.65B | +4.35% |
| Chain fees / REV (24h) | $9.90M | -5.67% |
| Non-vote TPS (1h avg) | 1,852 | peak 5,462 total |
| Active validators | 689 | 10 delinquent |
| Epoch 1015 | 77.16% complete | 98,665 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 27 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,852.5 average over the last 60 minutes; 1,868.3 in the latest sample.
- **Total TPS:** 3,481.0 average, 5,462.5 peak. Consensus votes account for 46.8% of all transactions.
- **Slot time:** 420.4 ms average (target 400 ms), worst 1-minute bucket 454.5 ms.
- **Block height:** 416,865,535 at absolute slot 438,813,335.
- **Epoch 1015:** slot 333,335 of 432,000 (77.16% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.702% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 304 ms |
| `solana-rpc.publicnode.com` | yes | 106 ms |
| `api.mainnet.solana.com` | yes | 259 ms |

## Validators & stake

- **689 active** validators, **10 delinquent** (1.43% by count, 0.057% by stake).
- **Total stake:** 434,931,021 SOL ($33.41B); stake rate 68.82% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.80% of active stake.
- **Commission:** median 5.0%, mean 12.27%; 257 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,988,468 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,978,711 | 3.676% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,007 | 2.875% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,334,140 | 2.838% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,151,705 | 2.105% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,964,622 | 2.062% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,172,871 | 1.880% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,954,158 | 1.830% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,367,684 | 1.695% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,577,941 | 1.513% | 0% |

## Economics

- **SOL:** $76.81 (+1.12% 24h, +4.14% 7d, +0.60% 30d). Market cap $44.74B, 24h volume $1.39B (3.10% of cap). Price source: `coingecko`.
- **TVL:** $4.86B across 321 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. +1.37% over 7d, -63.2% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-1.63% 7d) - $3.36 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.65B in 24h, $10.45B over 7d across 114 venues. Volume/TVL turnover 0.340x per day.
- **REV (chain fees):** $9.90M in 24h, $232.92M over 30d. Retained chain revenue $4.85M (49.0% of fees). Annualised fees are 8.07% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,499,699 SOL circulating of 632,008,765 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | +0.8% | +4.1% |
| 2 | Kamino Lend | Lending | $1.06B | +0.1% | +1.0% |
| 3 | Jupiter Lend | Lending | $944.93M | -0.0% | +2.3% |
| 4 | Raydium AMM | Dexs | $845.88M | +0.1% | +2.9% |
| 5 | Binance Staked SOL | Liquid Staking | $786.90M | +0.9% | +4.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $765.68M | +1.1% | +4.5% |
| 7 | BlackRock BUIDL | RWA | $728.16M | +2.1% | +7.6% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $698.00M | +0.3% | -0.9% |
| 9 | Solstice | Basis Trading | $506.05M | -0.1% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $396.66M | +0.7% | +3.3% |
| 11 | xStocks | RWA | $377.47M | +1.5% | +1.8% |
| 12 | Sentora | Risk Curators | $368.86M | +0.1% | -0.8% |

The top five protocols hold 35.3% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.49B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.6% · RWA 13.7% · Dexs 13.4% · Derivatives 5.9% · Basis Trading 4.3%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 18.050% of chain TVL.

- BlackRock BUIDL (RWA): $728.16M
- Solstice (Basis Trading): $506.05M
- xStocks (RWA): $377.47M
- OnRe (RWA): $256.08M
- Ondo Yield Assets (RWA): $178.78M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **982.3 unique fee payers** signed per block (1,408 distinct addresses in the union, 52.2% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-11T12:36:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,265.38 | 3,481.04 | +6.60% |
| Average non-vote TPS | 1,632.48 | 1,852.50 | +13.48% |
| Average slot time (ms) | 421.10 | 420.40 | -0.17% |
| Active validators | 692.00 | 689.00 | -0.43% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,844,754,288.00 | 4,855,182,857.00 | +0.22% |
| SOL price | 75.86 | 76.81 | +1.25% |
| Stablecoin supply | 16,324,544,582.00 | 16,295,761,438.00 | -0.18% |
| 24h DEX volume | 1,581,973,855.56 | 1,650,837,789.28 | +4.35% |
| 24h chain fees | 10,390,906.03 | 9,897,773.23 | -4.75% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,481.04 | -7.79% |
| Average non-vote TPS | 2,150.39 | 1,852.50 | -13.85% |
| Average slot time (ms) | 422.90 | 420.40 | -0.59% |
| Active validators | 693.00 | 689.00 | -0.58% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,739,955,873.00 | 4,855,182,857.00 | +2.43% |
| SOL price | 72.58 | 76.81 | +5.83% |
| Stablecoin supply | 16,197,749,831.00 | 16,295,761,438.00 | +0.61% |
| 24h DEX volume | 1,636,927,091.91 | 1,650,837,789.28 | +0.85% |
| 24h chain fees | 7,777,648.77 | 9,897,773.23 | +27.26% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
