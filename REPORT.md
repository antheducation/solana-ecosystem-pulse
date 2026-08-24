# Solana Ecosystem Pulse

**Generated:** 2026-08-24T12:21:24Z · **Schema:** `1.0.0` · **Collection time:** 28.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.82 | +0.45% |
| Market cap | $55.31B | rank #7 |
| Total value locked | $5.55B | -0.14% |
| Stablecoin supply | $16.45B | +0.49% |
| DEX volume (24h) | $2.94B | -21.27% |
| Chain fees / REV (24h) | $12.56M | +4.53% |
| Non-vote TPS (1h avg) | 1,972 | peak 4,459 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1021 | 74.33% complete | 110,896 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 62 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 363.60 sits 17.6 sigma below the median of the last 62 runs (415.90, -12.6%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,550,065,543.00 sits 11.0 sigma above the median of the last 62 runs (4,848,408,872.50, +14.5%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.82 sits 13.9 sigma above the median of the last 62 runs (76.23, +24.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,971.7 average over the last 60 minutes; 1,956.6 in the latest sample.
- **Total TPS:** 3,845.1 average, 4,458.6 peak. Consensus votes account for 48.7% of all transactions.
- **Slot time:** 363.6 ms average (target 400 ms), worst 1-minute bucket 377.4 ms.
- **Block height:** 419,442,092 at absolute slot 441,393,104.
- **Epoch 1021:** slot 321,104 of 432,000 (74.33% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 263 ms |
| `solana-rpc.publicnode.com` | yes | 213 ms |
| `api.mainnet.solana.com` | yes | 229 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.403% by stake).
- **Total stake:** 433,436,313 SOL ($41.10B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 46.12% of active stake.
- **Commission:** median 5.0%, mean 12.19%; 255 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 | 3.714% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 | 2.829% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 | 2.717% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 | 2.123% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 | 2.056% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 | 1.964% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 | 1.837% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 | 1.705% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 | 1.522% | 0% |

## Economics

- **SOL:** $94.82 (+0.45% 24h, +25.39% 7d, +28.38% 30d). Market cap $55.31B, 24h volume $4.05B (7.33% of cap). Price source: `coingecko`.
- **TVL:** $5.55B across 329 protocols - rank #3 of 462 chains, 5.97% of all tracked chain TVL. +16.18% over 7d, -58.1% from its ATH.
- **Stablecoins:** $16.45B circulating on Solana (+2.81% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.94B in 24h, $19.36B over 7d across 119 venues. Volume/TVL turnover 0.529x per day.
- **REV (chain fees):** $12.56M in 24h, $276.98M over 30d. Retained chain revenue $4.96M (39.5% of fees). Annualised fees are 8.29% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,276,168 SOL circulating of 632,749,278 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.42B | +1.1% | +27.2% |
| 2 | Kamino Lend | Lending | $1.19B | -0.0% | +14.6% |
| 3 | Jupiter Lend | Lending | $1.06B | +0.4% | +14.8% |
| 4 | Raydium AMM | Dexs | $1.04B | +0.4% | +24.1% |
| 5 | Binance Staked SOL | Liquid Staking | $961.26M | +1.4% | +26.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $951.58M | +1.3% | +27.7% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $743.51M | +0.2% | +10.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $490.33M | +1.3% | +26.7% |
| 10 | xStocks | RWA | $419.57M | +0.1% | +9.4% |
| 11 | Solstice | Basis Trading | $404.29M | -0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $363.65M | -0.7% | -1.0% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 329 protocols the total is $15.47B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.4% · Lending 16.3% · Dexs 14.0% · RWA 12.6% · Derivatives 5.4% · Staking Pool 3.5%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.723% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $419.57M
- Solstice (Basis Trading): $404.29M
- OnRe (RWA): $275.35M
- Ondo Yield Assets (RWA): $178.22M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **956.3 unique fee payers** signed per block (1,350 distinct addresses in the union, 52.9% overlap between blocks).

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

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-24
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
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

### Change over 24h (vs run at 2026-08-23T12:14:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,375.74 | 3,845.13 | +13.90% |
| Average non-vote TPS | 1,517.25 | 1,971.73 | +29.95% |
| Average slot time (ms) | 365.10 | 363.60 | -0.41% |
| Active validators | 683.00 | 685.00 | +0.29% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,519,339,285.00 | 5,550,065,543.00 | +0.56% |
| SOL price | 94.24 | 94.82 | +0.62% |
| Stablecoin supply | 16,372,596,016.00 | 16,453,541,490.00 | +0.49% |
| 24h DEX volume | 3,732,294,477.70 | 2,938,613,605.25 | -21.27% |
| 24h chain fees | 11,916,880.26 | 12,561,642.70 | +5.41% |

### Change over 7d (vs run at 2026-08-17T12:17:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,280.79 | 3,845.13 | +17.20% |
| Average non-vote TPS | 1,623.97 | 1,971.73 | +21.41% |
| Average slot time (ms) | 413.40 | 363.60 | -12.05% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 4,826,232,773.00 | 5,550,065,543.00 | +15.00% |
| SOL price | 75.55 | 94.82 | +25.51% |
| Stablecoin supply | 16,002,553,141.00 | 16,453,541,490.00 | +2.82% |
| 24h DEX volume | 1,055,467,633.95 | 2,938,613,605.25 | +178.42% |
| 24h chain fees | 6,712,382.48 | 12,561,642.70 | +87.14% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 28.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
