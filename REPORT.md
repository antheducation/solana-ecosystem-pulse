# Solana Ecosystem Pulse

**Generated:** 2026-08-21T12:20:20Z · **Schema:** `1.0.0` · **Collection time:** 19.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $90.34 | +4.15% |
| Market cap | $52.67B | rank #7 |
| Total value locked | $5.46B | +4.55% |
| Stablecoin supply | $16.51B | +1.15% |
| DEX volume (24h) | $2.77B | -7.95% |
| Chain fees / REV (24h) | $10.99M | -19.66% |
| Non-vote TPS (1h avg) | 2,534 | peak 5,910 total |
| Active validators | 683 | 11 delinquent |
| Epoch 1020 | 10.39% complete | 387,129 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 59 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 367.50 sits 13.3 sigma below the median of the last 59 runs (416.80, -11.8%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,464,069,865.00 sits 15.6 sigma above the median of the last 59 runs (4,826,095,598.00, +13.2%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 90.34 sits 17.1 sigma above the median of the last 59 runs (75.86, +19.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 683.00 sits 4.0 sigma below the median of the last 59 runs (689.00, -0.9%). | `zscore` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 2,770,509,439.33 sits 4.6 sigma above the median of the last 59 runs (1,546,444,167.56, +79.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,533.9 average over the last 60 minutes; 2,180.2 in the latest sample.
- **Total TPS:** 4,382.8 average, 5,910.1 peak. Consensus votes account for 42.2% of all transactions.
- **Slot time:** 367.5 ms average (target 400 ms), worst 1-minute bucket 389.6 ms.
- **Block height:** 418,734,526 at absolute slot 440,684,871.
- **Epoch 1020:** slot 44,871 of 432,000 (10.39% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 222 ms |
| `solana-rpc.publicnode.com` | yes | 155 ms |
| `api.mainnet.solana.com` | yes | 180 ms |

## Validators & stake

- **683 active** validators, **11 delinquent** (1.59% by count, 0.117% by stake).
- **Total stake:** 433,485,334 SOL ($39.16B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.97% of active stake.
- **Commission:** median 5.0%, mean 11.77%; 258 validators at 0% and 59 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.942% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.708% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.812% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.721% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.120% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.060% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.941% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.839% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.699% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.512% | 0% |

## Economics

- **SOL:** $90.34 (+4.15% 24h, +19.72% 7d, +16.56% 30d). Market cap $52.67B, 24h volume $5.87B (11.14% of cap). Price source: `coingecko`.
- **TVL:** $5.46B across 328 protocols - rank #3 of 461 chains, 6.34% of all tracked chain TVL. +12.96% over 7d, -58.7% from its ATH.
- **Stablecoins:** $16.51B circulating on Solana (+2.59% 7d) - $3.02 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.77B in 24h, $12.92B over 7d across 119 venues. Volume/TVL turnover 0.507x per day.
- **REV (chain fees):** $10.99M in 24h, $262.12M over 30d. Retained chain revenue $5.17M (47.1% of fees). Annualised fees are 7.61% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,178,349 SOL circulating of 632,640,323 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.37B | +5.4% | +20.6% |
| 2 | Kamino Lend | Lending | $1.16B | +1.9% | +10.8% |
| 3 | Jupiter Lend | Lending | $1.05B | +2.8% | +14.0% |
| 4 | Raydium AMM | Dexs | $1.01B | +5.4% | +19.1% |
| 5 | Binance Staked SOL | Liquid Staking | $920.01M | +4.5% | +17.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $911.05M | +4.5% | +19.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $747.50M | +0.3% | +8.4% |
| 8 | BlackRock BUIDL | RWA | $740.67M | +0.0% | -0.0% |
| 9 | Solstice | Basis Trading | $506.18M | +0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $478.46M | +5.8% | +21.1% |
| 11 | xStocks | RWA | $417.88M | +3.0% | +8.9% |
| 12 | Sentora | Risk Curators | $363.70M | -0.5% | -1.3% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.16B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 34.8% · Lending 16.4% · Dexs 14.0% · RWA 12.6% · Derivatives 5.5% · Basis Trading 3.9%

### Tokenised assets

$2.50B of tokenised real-world assets and equities are locked on Solana - 16.476% of chain TVL.

- BlackRock BUIDL (RWA): $740.67M
- Solstice (Basis Trading): $506.18M
- xStocks (RWA): $417.88M
- OnRe (RWA): $272.78M
- Ondo Yield Assets (RWA): $178.31M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **984.0 unique fee payers** signed per block (1,399 distinct addresses in the union, 52.6% overlap between blocks).

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
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-19
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14

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

### Change over 24h (vs run at 2026-08-20T12:20:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,960.77 | 4,382.77 | +10.65% |
| Average non-vote TPS | 2,305.17 | 2,533.88 | +9.92% |
| Average slot time (ms) | 413.30 | 367.50 | -11.08% |
| Active validators | 688.00 | 683.00 | -0.73% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 5,297,166,576.00 | 5,464,069,865.00 | +3.15% |
| SOL price | 86.73 | 90.34 | +4.16% |
| Stablecoin supply | 16,322,738,591.00 | 16,514,972,212.00 | +1.18% |
| 24h DEX volume | 3,009,837,694.95 | 2,770,509,439.33 | -7.95% |
| 24h chain fees | 13,588,582.38 | 10,987,558.08 | -19.14% |

### Change over 7d (vs run at 2026-08-14T12:36:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,109.81 | 4,382.77 | +40.93% |
| Average non-vote TPS | 1,467.96 | 2,533.88 | +72.61% |
| Average slot time (ms) | 415.90 | 367.50 | -11.64% |
| Active validators | 688.00 | 683.00 | -0.73% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 4,824,731,121.00 | 5,464,069,865.00 | +13.25% |
| SOL price | 75.46 | 90.34 | +19.72% |
| Stablecoin supply | 16,096,024,925.00 | 16,514,972,212.00 | +2.60% |
| 24h DEX volume | 1,942,768,290.75 | 2,770,509,439.33 | +42.61% |
| 24h chain fees | 10,077,524.92 | 10,987,558.08 | +9.03% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
