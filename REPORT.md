# Solana Ecosystem Pulse

**Generated:** 2026-08-23T06:19:57Z · **Schema:** `1.0.0` · **Collection time:** 17.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $92.32 | -1.44% |
| Market cap | $53.83B | rank #7 |
| Total value locked | $5.54B | -0.23% |
| Stablecoin supply | $16.37B | -0.32% |
| DEX volume (24h) | $3.65B | +1.31% |
| Chain fees / REV (24h) | $11.92M | -10.62% |
| Non-vote TPS (1h avg) | 1,794 | peak 4,442 total |
| Active validators | 686 | 9 delinquent |
| Epoch 1021 | 5.81% complete | 406,892 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 60 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.10 sits 17.6 sigma below the median of the last 60 runs (416.05, -12.2%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,539,212,933.00 sits 14.5 sigma above the median of the last 60 runs (4,840,562,138.00, +14.4%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 92.32 sits 15.2 sigma above the median of the last 60 runs (76.00, +21.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 3,648,052,188.89 sits 4.9 sigma above the median of the last 60 runs (1,639,619,531.74, +122.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,794.2 average over the last 60 minutes; 1,560.5 in the latest sample.
- **Total TPS:** 3,663.3 average, 4,441.7 peak. Consensus votes account for 51.0% of all transactions.
- **Slot time:** 365.1 ms average (target 400 ms), worst 1-minute bucket 382.2 ms.
- **Block height:** 419,146,284 at absolute slot 441,097,108.
- **Epoch 1021:** slot 25,108 of 432,000 (5.81% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 225 ms |
| `solana-rpc.publicnode.com` | yes | 29 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **686 active** validators, **9 delinquent** (1.29% by count, 0.299% by stake).
- **Total stake:** 433,436,313 SOL ($40.01B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 46.08% of active stake.
- **Commission:** median 5.0%, mean 11.89%; 257 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 | 3.930% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 | 3.710% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 | 2.826% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 | 2.714% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 | 2.121% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 | 2.054% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 | 1.962% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 | 1.835% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 | 1.703% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 | 1.520% | 0% |

## Economics

- **SOL:** $92.32 (-1.44% 24h, +22.58% 7d, +21.93% 30d). Market cap $53.83B, 24h volume $5.35B (9.93% of cap). Price source: `coingecko`.
- **TVL:** $5.54B across 328 protocols - rank #3 of 462 chains, 6.06% of all tracked chain TVL. +15.19% over 7d, -58.2% from its ATH.
- **Stablecoins:** $16.37B circulating on Solana (+2.34% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.65B in 24h, $16.91B over 7d across 119 venues. Volume/TVL turnover 0.659x per day.
- **REV (chain fees):** $11.92M in 24h, $270.54M over 30d. Retained chain revenue $4.99M (41.9% of fees). Annualised fees are 8.08% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,277,583 SOL circulating of 632,750,330 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.40B | -0.4% | +24.2% |
| 2 | Kamino Lend | Lending | $1.18B | -1.9% | +13.7% |
| 3 | Raydium AMM | Dexs | $1.06B | +0.9% | +25.4% |
| 4 | Jupiter Lend | Lending | $1.05B | +0.5% | +12.9% |
| 5 | Binance Staked SOL | Liquid Staking | $945.19M | +0.2% | +23.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $937.95M | -0.5% | +24.6% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $736.14M | -3.4% | +7.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $483.11M | -0.9% | +23.6% |
| 10 | xStocks | RWA | $418.84M | -2.0% | +9.4% |
| 11 | Solstice | Basis Trading | $404.43M | +0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $365.80M | -0.2% | -0.6% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.35B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.1% · Lending 16.3% · Dexs 14.2% · RWA 12.7% · Derivatives 5.4% · Staking Pool 3.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.843% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $418.84M
- Solstice (Basis Trading): $404.43M
- OnRe (RWA): $273.61M
- Ondo Yield Assets (RWA): $178.22M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **880.7 unique fee payers** signed per block (1,169 distinct addresses in the union, 55.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14

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

### Change over 24h (vs run at 2026-08-22T06:18:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,573.18 | 3,663.30 | -19.90% |
| Average non-vote TPS | 2,718.03 | 1,794.20 | -33.99% |
| Average slot time (ms) | 366.40 | 365.10 | -0.35% |
| Active validators | 685.00 | 686.00 | +0.15% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 5,632,028,805.00 | 5,539,212,933.00 | -1.65% |
| SOL price | 93.90 | 92.32 | -1.68% |
| Stablecoin supply | 16,420,329,932.00 | 16,372,140,467.00 | -0.29% |
| 24h DEX volume | 3,465,651,694.33 | 3,648,052,188.89 | +5.26% |
| 24h chain fees | 13,204,850.88 | 11,918,650.26 | -9.74% |

### Change over 7d (vs run at 2026-08-16T06:18:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,746.35 | 3,663.30 | +33.39% |
| Average non-vote TPS | 1,107.30 | 1,794.20 | +62.03% |
| Average slot time (ms) | 417.30 | 365.10 | -12.51% |
| Active validators | 688.00 | 686.00 | -0.29% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 4,812,235,963.00 | 5,539,212,933.00 | +15.11% |
| SOL price | 75.29 | 92.32 | +22.62% |
| Stablecoin supply | 16,002,608,919.00 | 16,372,140,467.00 | +2.31% |
| 24h DEX volume | 1,234,854,042.04 | 3,648,052,188.89 | +195.42% |
| 24h chain fees | 8,078,661.86 | 11,918,650.26 | +47.53% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
