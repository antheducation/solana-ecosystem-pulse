# Solana Ecosystem Pulse

**Generated:** 2026-08-24T00:32:07Z · **Schema:** `1.0.0` · **Collection time:** 22.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.47 | +0.13% |
| Market cap | $55.10B | rank #7 |
| Total value locked | $5.59B | +0.70% |
| Stablecoin supply | $16.37B | -0.31% |
| DEX volume (24h) | $3.41B | -8.70% |
| Chain fees / REV (24h) | $11.68M | -2.80% |
| Non-vote TPS (1h avg) | 2,171 | peak 4,388 total |
| Active validators | 684 | 11 delinquent |
| Epoch 1021 | 47.32% complete | 227,570 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 61 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.40 sits 18.0 sigma below the median of the last 61 runs (416.00, -12.2%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,590,677,164.00 sits 12.8 sigma above the median of the last 61 runs (4,846,663,986.00, +15.4%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.47 sits 14.1 sigma above the median of the last 61 runs (76.22, +23.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 3,407,472,979.70 sits 4.1 sigma above the median of the last 61 runs (1,650,837,789.28, +106.4%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,170.9 average over the last 60 minutes; 2,484.5 in the latest sample.
- **Total TPS:** 4,028.1 average, 4,387.9 peak. Consensus votes account for 46.1% of all transactions.
- **Slot time:** 365.4 ms average (target 400 ms), worst 1-minute bucket 382.2 ms.
- **Block height:** 419,325,455 at absolute slot 441,276,430.
- **Epoch 1021:** slot 204,430 of 432,000 (47.32% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 339 ms |
| `solana-rpc.publicnode.com` | yes | 101 ms |
| `api.mainnet.solana.com` | yes | 339 ms |

## Validators & stake

- **684 active** validators, **11 delinquent** (1.58% by count, 0.042% by stake).
- **Total stake:** 433,436,313 SOL ($40.95B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 11.92%; 256 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 | 3.920% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 | 3.701% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 | 2.819% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 | 2.707% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 | 2.115% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 | 2.049% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 | 1.957% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 | 1.831% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 | 1.699% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 | 1.516% | 0% |

## Economics

- **SOL:** $94.47 (+0.13% 24h, +26.72% 7d, +27.79% 30d). Market cap $55.10B, 24h volume $4.34B (7.87% of cap). Price source: `coingecko`.
- **TVL:** $5.59B across 329 protocols - rank #3 of 462 chains, 6.07% of all tracked chain TVL. +16.26% over 7d, -57.8% from its ATH.
- **Stablecoins:** $16.37B circulating on Solana (+2.34% 7d) - $2.93 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.41B in 24h, $17.25B over 7d across 119 venues. Volume/TVL turnover 0.609x per day.
- **REV (chain fees):** $11.68M in 24h, $266.53M over 30d. Retained chain revenue $4.94M (42.3% of fees). Annualised fees are 7.74% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,276,568 SOL circulating of 632,749,678 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.42B | +1.7% | +27.7% |
| 2 | Kamino Lend | Lending | $1.19B | +1.0% | +15.2% |
| 3 | Jupiter Lend | Lending | $1.06B | +4.1% | +15.5% |
| 4 | Raydium AMM | Dexs | $1.05B | +0.8% | +25.6% |
| 5 | Binance Staked SOL | Liquid Staking | $963.09M | +2.0% | +26.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $955.04M | +1.7% | +28.2% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $746.40M | +1.4% | +10.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $492.14M | +1.7% | +27.2% |
| 10 | xStocks | RWA | $421.11M | +0.8% | +9.8% |
| 11 | Solstice | Basis Trading | $404.34M | -0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $365.92M | +0.0% | -0.4% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 329 protocols the total is $15.54B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.4% · Lending 16.3% · Dexs 14.1% · RWA 12.6% · Derivatives 5.4% · Staking Pool 3.5%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.674% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $421.11M
- Solstice (Basis Trading): $404.34M
- OnRe (RWA): $274.99M
- Ondo Yield Assets (RWA): $178.52M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,033.3 unique fee payers** signed per block (1,568 distinct addresses in the union, 49.4% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-23T00:32:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,801.15 | 4,028.12 | +5.97% |
| Average non-vote TPS | 1,949.33 | 2,170.90 | +11.37% |
| Average slot time (ms) | 368.10 | 365.40 | -0.73% |
| Active validators | 687.00 | 684.00 | -0.44% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 5,520,748,480.00 | 5,590,677,164.00 | +1.27% |
| SOL price | 94.33 | 94.47 | +0.15% |
| Stablecoin supply | 16,423,898,783.00 | 16,372,851,569.00 | -0.31% |
| 24h DEX volume | 3,761,469,856.66 | 3,407,472,979.70 | -9.41% |
| 24h chain fees | 13,746,381.02 | 11,680,746.95 | -15.03% |

### Change over 7d (vs run at 2026-08-17T00:30:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,357.14 | 4,028.12 | +19.99% |
| Average non-vote TPS | 1,709.25 | 2,170.90 | +27.01% |
| Average slot time (ms) | 414.10 | 365.40 | -11.76% |
| Active validators | 688.00 | 684.00 | -0.58% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 4,778,503,787.00 | 5,590,677,164.00 | +17.00% |
| SOL price | 74.43 | 94.47 | +26.92% |
| Stablecoin supply | 15,998,457,281.00 | 16,372,851,569.00 | +2.34% |
| 24h DEX volume | 1,157,787,831.09 | 3,407,472,979.70 | +194.31% |
| 24h chain fees | 8,251,907.01 | 11,680,746.95 | +41.55% |

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
