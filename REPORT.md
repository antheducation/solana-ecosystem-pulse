# Solana Ecosystem Pulse

**Generated:** 2026-08-14T18:37:41Z · **Schema:** `1.0.0` · **Collection time:** 18.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.00 | -0.86% |
| Market cap | $43.70B | rank #7 |
| Total value locked | $4.81B | -0.37% |
| Stablecoin supply | $16.10B | +0.10% |
| DEX volume (24h) | $1.94B | +12.58% |
| Chain fees / REV (24h) | $10.15M | +4.91% |
| Non-vote TPS (1h avg) | 2,556 | peak 5,402 total |
| Active validators | 689 | 9 delinquent |
| Epoch 1016 | 84.99% complete | 64,858 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 36 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average slot time (ms) is below its recent norm | Current 415.90 sits 3.3 sigma below the median of the last 36 runs (422.35, -1.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,555.6 average over the last 60 minutes; 2,086.4 in the latest sample.
- **Total TPS:** 4,201.3 average, 5,402.4 peak. Consensus votes account for 39.2% of all transactions.
- **Slot time:** 415.9 ms average (target 400 ms), worst 1-minute bucket 438.0 ms.
- **Block height:** 417,330,458 at absolute slot 439,279,142.
- **Epoch 1016:** slot 367,142 of 432,000 (84.99% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.698% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 338 ms |
| `solana-rpc.publicnode.com` | yes | 122 ms |
| `api.mainnet.solana.com` | yes | 211 ms |

## Validators & stake

- **689 active** validators, **9 delinquent** (1.29% by count, 0.014% by stake).
- **Total stake:** 434,669,916 SOL ($32.60B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.44% and top 33 hold 45.90% of active stake.
- **Commission:** median 5.0%, mean 12.28%; 255 validators at 0% and 63 at 100%.

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

- **SOL:** $75.00 (-0.86% 24h, +2.16% 7d, -3.56% 30d). Market cap $43.70B, 24h volume $1.04B (2.37% of cap). Price source: `coingecko`.
- **TVL:** $4.81B across 326 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. +1.75% over 7d, -63.7% from its ATH.
- **Stablecoins:** $16.10B circulating on Solana (-1.06% 7d) - $3.35 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.94B in 24h, $11.10B over 7d across 116 venues. Volume/TVL turnover 0.404x per day.
- **REV (chain fees):** $10.15M in 24h, $239.02M over 30d. Retained chain revenue $4.23M (41.7% of fees). Annualised fees are 8.48% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,613,207 SOL circulating of 632,134,828 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | -0.3% | +5.4% |
| 2 | Kamino Lend | Lending | $1.04B | -0.2% | +2.2% |
| 3 | Jupiter Lend | Lending | $926.23M | -0.9% | +1.6% |
| 4 | Raydium AMM | Dexs | $842.33M | -1.1% | +4.5% |
| 5 | Binance Staked SOL | Liquid Staking | $774.37M | -0.2% | +4.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $754.91M | -0.3% | +4.6% |
| 7 | BlackRock BUIDL | RWA | $740.96M | +0.0% | +6.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $683.68M | -0.8% | -1.7% |
| 9 | Solstice | Basis Trading | $505.99M | +0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $391.76M | -0.3% | +3.6% |
| 11 | xStocks | RWA | $380.28M | +0.7% | +3.8% |
| 12 | Sentora | Risk Curators | $368.00M | -0.2% | -0.3% |

The top five protocols hold 35.0% of Solana's tracked TVL. Summed across all 326 protocols the total is $13.46B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.9% · Lending 16.4% · RWA 13.9% · Dexs 13.4% · Derivatives 5.8% · Basis Trading 4.3%

### Tokenised assets

$2.45B of tokenised real-world assets and equities are locked on Solana - 18.240% of chain TVL.

- BlackRock BUIDL (RWA): $740.96M
- Solstice (Basis Trading): $505.99M
- xStocks (RWA): $380.28M
- OnRe (RWA): $260.50M
- Ondo Yield Assets (RWA): $178.69M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,093.0 unique fee payers** signed per block (1,684 distinct addresses in the union, 48.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-12
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03

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

### Change over 24h (vs run at 2026-08-13T18:44:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,039.13 | 4,201.34 | +4.02% |
| Average non-vote TPS | 2,403.37 | 2,555.64 | +6.34% |
| Average slot time (ms) | 416.90 | 415.90 | -0.24% |
| Active validators | 688.00 | 689.00 | +0.15% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 4,832,030,854.00 | 4,805,244,467.00 | -0.55% |
| SOL price | 75.68 | 75.00 | -0.90% |
| Stablecoin supply | 16,079,315,270.00 | 16,096,537,114.00 | +0.11% |
| 24h DEX volume | 1,725,631,800.93 | 1,942,768,290.75 | +12.58% |
| 24h chain fees | 9,673,605.00 | 10,148,326.92 | +4.91% |

### Change over 7d (vs run at 2026-08-07T18:36:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,788.53 | 4,201.34 | +10.90% |
| Average non-vote TPS | 2,156.41 | 2,555.64 | +18.51% |
| Average slot time (ms) | 421.60 | 415.90 | -1.35% |
| Active validators | 693.00 | 689.00 | -0.58% |
| Delinquent validators | 7.00 | 9.00 | +28.57% |
| Solana TVL | 4,734,042,546.00 | 4,805,244,467.00 | +1.50% |
| SOL price | 73.45 | 75.00 | +2.11% |
| Stablecoin supply | 16,250,945,719.00 | 16,096,537,114.00 | -0.95% |
| 24h DEX volume | 1,379,094,026.18 | 1,942,768,290.75 | +40.87% |
| 24h chain fees | 8,978,153.12 | 10,148,326.92 | +13.03% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
