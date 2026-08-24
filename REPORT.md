# Solana Ecosystem Pulse

**Generated:** 2026-08-24T06:32:07Z · **Schema:** `1.0.0` · **Collection time:** 28.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.29 | +2.08% |
| Market cap | $55.00B | rank #7 |
| Total value locked | $5.53B | -0.42% |
| Stablecoin supply | $16.45B | +0.49% |
| DEX volume (24h) | $3.12B | -16.41% |
| Chain fees / REV (24h) | $12.45M | +3.57% |
| Non-vote TPS (1h avg) | 1,534 | peak 3,912 total |
| Active validators | 684 | 11 delinquent |
| Epoch 1021 | 61.02% complete | 168,386 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 61 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 364.50 sits 19.3 sigma below the median of the last 61 runs (415.90, -12.4%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,534,492,880.00 sits 10.8 sigma above the median of the last 61 runs (4,848,077,810.00, +14.2%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.29 sits 14.0 sigma above the median of the last 61 runs (76.22, +23.7%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 3,119,842,862.16 sits 3.4 sigma above the median of the last 61 runs (1,650,871,367.28, +89.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,533.9 average over the last 60 minutes; 1,333.5 in the latest sample.
- **Total TPS:** 3,404.1 average, 3,911.8 peak. Consensus votes account for 54.9% of all transactions.
- **Slot time:** 364.5 ms average (target 400 ms), worst 1-minute bucket 379.7 ms.
- **Block height:** 419,384,614 at absolute slot 441,335,614.
- **Epoch 1021:** slot 263,614 of 432,000 (61.02% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 156 ms |
| `solana-rpc.publicnode.com` | yes | 191 ms |
| `api.mainnet.solana.com` | yes | 217 ms |

## Validators & stake

- **684 active** validators, **11 delinquent** (1.58% by count, 0.287% by stake).
- **Total stake:** 433,436,313 SOL ($40.87B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.37% and top 33 hold 46.07% of active stake.
- **Commission:** median 5.0%, mean 12.21%; 253 validators at 0% and 62 at 100%.

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

- **SOL:** $94.29 (+2.08% 24h, +25.10% 7d, +27.53% 30d). Market cap $55.00B, 24h volume $3.57B (6.49% of cap). Price source: `coingecko`.
- **TVL:** $5.53B across 328 protocols - rank #3 of 462 chains, 5.96% of all tracked chain TVL. +15.86% over 7d, -58.2% from its ATH.
- **Stablecoins:** $16.45B circulating on Solana (+2.81% 7d) - $2.97 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.12B in 24h, $18.98B over 7d across 119 venues. Volume/TVL turnover 0.564x per day.
- **REV (chain fees):** $12.45M in 24h, $276.23M over 30d. Retained chain revenue $4.84M (38.9% of fees). Annualised fees are 8.26% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,276,360 SOL circulating of 632,749,470 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.41B | +0.6% | +26.2% |
| 2 | Kamino Lend | Lending | $1.18B | +0.1% | +14.3% |
| 3 | Jupiter Lend | Lending | $1.05B | +0.8% | +13.9% |
| 4 | Raydium AMM | Dexs | $1.04B | -1.7% | +24.3% |
| 5 | Binance Staked SOL | Liquid Staking | $954.36M | +1.7% | +25.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $944.54M | +0.7% | +26.8% |
| 7 | BlackRock BUIDL | RWA | $777.14M | -0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $738.86M | +0.4% | +9.8% |
| 9 | Jupiter Staked SOL | Liquid Staking | $486.81M | +1.5% | +25.8% |
| 10 | xStocks | RWA | $417.43M | -0.3% | +8.9% |
| 11 | Solstice | Basis Trading | $404.33M | -0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $365.89M | +0.0% | -0.4% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.40B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.3% · Lending 16.3% · Dexs 14.1% · RWA 12.7% · Derivatives 5.4% · Staking Pool 3.5%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.781% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $417.43M
- Solstice (Basis Trading): $404.33M
- OnRe (RWA): $275.37M
- Ondo Yield Assets (RWA): $178.05M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **961.7 unique fee payers** signed per block (1,365 distinct addresses in the union, 52.7% overlap between blocks).

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

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-24
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17

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

### Change over 24h (vs run at 2026-08-23T06:19:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,663.30 | 3,404.07 | -7.08% |
| Average non-vote TPS | 1,794.20 | 1,533.89 | -14.51% |
| Average slot time (ms) | 365.10 | 364.50 | -0.16% |
| Active validators | 686.00 | 684.00 | -0.29% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 5,539,212,933.00 | 5,534,492,880.00 | -0.09% |
| SOL price | 92.32 | 94.29 | +2.13% |
| Stablecoin supply | 16,372,140,467.00 | 16,453,046,975.00 | +0.49% |
| 24h DEX volume | 3,648,052,188.89 | 3,119,842,862.16 | -14.48% |
| 24h chain fees | 11,918,650.26 | 12,447,100.70 | +4.43% |

### Change over 7d (vs run at 2026-08-17T06:27:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,132.50 | 3,404.07 | +8.67% |
| Average non-vote TPS | 1,482.73 | 1,533.89 | +3.45% |
| Average slot time (ms) | 415.20 | 364.50 | -12.21% |
| Active validators | 689.00 | 684.00 | -0.73% |
| Delinquent validators | 6.00 | 11.00 | +83.33% |
| Solana TVL | 4,813,819,212.00 | 5,534,492,880.00 | +14.97% |
| SOL price | 75.41 | 94.29 | +25.04% |
| Stablecoin supply | 16,004,923,242.00 | 16,453,046,975.00 | +2.80% |
| 24h DEX volume | 1,053,725,616.95 | 3,119,842,862.16 | +196.08% |
| 24h chain fees | 6,617,725.48 | 12,447,100.70 | +88.09% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 28.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
