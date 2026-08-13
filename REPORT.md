# Solana Ecosystem Pulse

**Generated:** 2026-08-13T00:54:54Z · **Schema:** `1.0.0` · **Collection time:** 15.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.58 | -0.90% |
| Market cap | $44.03B | rank #7 |
| Total value locked | $4.75B | +0.00% |
| Stablecoin supply | $16.29B | -0.18% |
| DEX volume (24h) | $1.68B | +2.03% |
| Chain fees / REV (24h) | $9.85M | -1.28% |
| Non-vote TPS (1h avg) | 2,099 | peak 4,693 total |
| Active validators | 688 | 9 delinquent |
| Epoch 1016 | 1.51% complete | 425,471 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 29 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average slot time (ms) is below its recent norm | Current 416.80 sits 4.3 sigma below the median of the last 29 runs (422.60, -1.4%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,099.1 average over the last 60 minutes; 2,071.8 in the latest sample.
- **Total TPS:** 3,733.8 average, 4,693.0 peak. Consensus votes account for 43.8% of all transactions.
- **Slot time:** 416.8 ms average (target 400 ms), worst 1-minute bucket 441.2 ms.
- **Block height:** 416,970,388 at absolute slot 438,918,529.
- **Epoch 1016:** slot 6,529 of 432,000 (1.51% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.698% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 173 ms |
| `solana-rpc.publicnode.com` | yes | 121 ms |
| `api.mainnet.solana.com` | yes | 119 ms |

## Validators & stake

- **688 active** validators, **9 delinquent** (1.29% by count, 0.014% by stake).
- **Total stake:** 434,669,916 SOL ($32.85B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.44% and top 33 hold 45.90% of active stake.
- **Commission:** median 5.0%, mean 12.00%; 258 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,055,967 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,972,699 | 3.675% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,477,808 | 2.871% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,363,210 | 2.845% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,161,872 | 2.108% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,981,437 | 2.067% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,300,271 | 1.910% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,966,398 | 1.833% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,372,731 | 1.696% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,581,887 | 1.514% | 0% |

## Economics

- **SOL:** $75.58 (-0.90% 24h, +2.13% 7d, +0.87% 30d). Market cap $44.03B, 24h volume $1.23B (2.79% of cap). Price source: `coingecko`.
- **TVL:** $4.75B across 322 protocols - rank #4 of 461 chains, 6.35% of all tracked chain TVL. -0.78% over 7d, -64.0% from its ATH.
- **Stablecoins:** $16.29B circulating on Solana (-1.63% 7d) - $3.43 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.68B in 24h, $10.33B over 7d across 115 venues. Volume/TVL turnover 0.354x per day.
- **REV (chain fees):** $9.85M in 24h, $231.69M over 30d. Retained chain revenue $4.95M (50.2% of fees). Annualised fees are 8.16% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,615,004 SOL circulating of 632,136,274 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.11B | -0.8% | +2.1% |
| 2 | Kamino Lend | Lending | $1.02B | -0.9% | -1.6% |
| 3 | Jupiter Lend | Lending | $896.19M | -1.3% | -4.4% |
| 4 | Raydium AMM | Dexs | $844.84M | -0.8% | +3.4% |
| 5 | Binance Staked SOL | Liquid Staking | $775.41M | -0.7% | +2.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $754.62M | -0.9% | +2.5% |
| 7 | BlackRock BUIDL | RWA | $740.62M | +1.7% | +8.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $688.78M | -0.8% | -2.6% |
| 9 | Solstice | Basis Trading | $505.89M | -0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $391.30M | -0.8% | +1.4% |
| 11 | xStocks | RWA | $376.27M | -0.1% | +2.5% |
| 12 | Sentora | Risk Curators | $368.90M | -0.1% | -0.7% |

The top five protocols hold 34.9% of Solana's tracked TVL. Summed across all 322 protocols the total is $13.34B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.6% · Lending 16.2% · RWA 13.9% · Dexs 13.6% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.45B of tokenised real-world assets and equities are locked on Solana - 18.342% of chain TVL.

- BlackRock BUIDL (RWA): $740.62M
- Solstice (Basis Trading): $505.89M
- xStocks (RWA): $376.27M
- OnRe (RWA): $256.15M
- Ondo Yield Assets (RWA): $178.55M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **945.3 unique fee payers** signed per block (1,302 distinct addresses in the union, 54.1% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-12
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29

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

### Change over 24h (vs run at 2026-08-12T00:53:45Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,974.24 | 3,733.82 | -6.05% |
| Average non-vote TPS | 2,353.21 | 2,099.07 | -10.80% |
| Average slot time (ms) | 421.90 | 416.80 | -1.21% |
| Active validators | 689.00 | 688.00 | -0.15% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 4,787,487,114.00 | 4,752,747,008.00 | -0.73% |
| SOL price | 76.25 | 75.58 | -0.88% |
| Stablecoin supply | 16,324,318,696.00 | 16,294,969,967.00 | -0.18% |
| 24h DEX volume | 1,650,871,367.28 | 1,684,395,735.93 | +2.03% |
| 24h chain fees | 10,814,593.52 | 9,848,639.11 | -8.93% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,733.82 | -1.10% |
| Average non-vote TPS | 2,150.39 | 2,099.07 | -2.39% |
| Average slot time (ms) | 422.90 | 416.80 | -1.44% |
| Active validators | 693.00 | 688.00 | -0.72% |
| Delinquent validators | 7.00 | 9.00 | +28.57% |
| Solana TVL | 4,739,955,873.00 | 4,752,747,008.00 | +0.27% |
| SOL price | 72.58 | 75.58 | +4.13% |
| Stablecoin supply | 16,197,749,831.00 | 16,294,969,967.00 | +0.60% |
| 24h DEX volume | 1,636,927,091.91 | 1,684,395,735.93 | +2.90% |
| 24h chain fees | 7,777,648.77 | 9,848,639.11 | +26.63% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
