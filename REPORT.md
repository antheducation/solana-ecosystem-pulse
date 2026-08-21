# Solana Ecosystem Pulse

**Generated:** 2026-08-21T18:19:03Z · **Schema:** `1.0.0` · **Collection time:** 13.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $91.85 | +5.62% |
| Market cap | $53.56B | rank #7 |
| Total value locked | $5.44B | +4.08% |
| Stablecoin supply | $16.52B | +1.17% |
| DEX volume (24h) | $2.77B | -7.95% |
| Chain fees / REV (24h) | $11.08M | -19.00% |
| Non-vote TPS (1h avg) | 2,672 | peak 5,921 total |
| Active validators | 685 | 9 delinquent |
| Epoch 1020 | 23.99% complete | 328,358 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 59 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.30 sits 14.4 sigma below the median of the last 59 runs (416.70, -12.3%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,439,131,617.00 sits 15.0 sigma above the median of the last 59 runs (4,826,232,773.00, +12.7%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 91.85 sits 17.9 sigma above the median of the last 59 runs (75.89, +21.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 2,770,509,439.33 sits 3.7 sigma above the median of the last 59 runs (1,581,973,855.56, +75.1%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,672.3 average over the last 60 minutes; 2,233.9 in the latest sample.
- **Total TPS:** 4,537.2 average, 5,920.6 peak. Consensus votes account for 41.1% of all transactions.
- **Slot time:** 365.3 ms average (target 400 ms), worst 1-minute bucket 382.2 ms.
- **Block height:** 418,793,230 at absolute slot 440,743,642.
- **Epoch 1020:** slot 103,642 of 432,000 (23.99% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 86 ms |
| `solana-rpc.publicnode.com` | yes | 63 ms |
| `api.mainnet.solana.com` | yes | 291 ms |

## Validators & stake

- **685 active** validators, **9 delinquent** (1.30% by count, 0.020% by stake).
- **Total stake:** 433,485,334 SOL ($39.82B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 11.89%; 258 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.704% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.719% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.118% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.058% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.939% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.511% | 0% |

## Economics

- **SOL:** $91.85 (+5.62% 24h, +22.30% 7d, +17.49% 30d). Market cap $53.56B, 24h volume $5.90B (11.01% of cap). Price source: `coingecko`.
- **TVL:** $5.44B across 329 protocols - rank #3 of 461 chains, 6.29% of all tracked chain TVL. +12.45% over 7d, -58.9% from its ATH.
- **Stablecoins:** $16.52B circulating on Solana (+2.60% 7d) - $3.04 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.77B in 24h, $12.92B over 7d across 119 venues. Volume/TVL turnover 0.509x per day.
- **REV (chain fees):** $11.08M in 24h, $262.21M over 30d. Retained chain revenue $5.17M (46.7% of fees). Annualised fees are 7.55% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,178,089 SOL circulating of 632,640,050 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.36B | +4.7% | +20.1% |
| 2 | Kamino Lend | Lending | $1.17B | +3.1% | +11.8% |
| 3 | Jupiter Lend | Lending | $1.03B | +0.5% | +11.4% |
| 4 | Raydium AMM | Dexs | $1.00B | +5.0% | +17.8% |
| 5 | Binance Staked SOL | Liquid Staking | $920.80M | +4.7% | +17.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $916.18M | +5.1% | +20.4% |
| 7 | BlackRock BUIDL | RWA | $740.74M | +0.0% | -0.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $739.06M | -0.6% | +7.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $476.01M | +5.4% | +20.4% |
| 10 | xStocks | RWA | $423.65M | +4.8% | +10.4% |
| 11 | Solstice | Basis Trading | $404.23M | -20.2% | -20.1% |
| 12 | Sentora | Risk Curators | $362.84M | -0.9% | -1.5% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 329 protocols the total is $15.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.1% · Lending 16.4% · Dexs 14.1% · RWA 12.8% · Derivatives 5.5% · Basis Trading 3.2%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 15.975% of chain TVL.

- BlackRock BUIDL (RWA): $740.74M
- xStocks (RWA): $423.65M
- Solstice (Basis Trading): $404.23M
- OnRe (RWA): $272.76M
- Ondo Yield Assets (RWA): $178.30M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **959.3 unique fee payers** signed per block (1,349 distinct addresses in the union, 53.1% overlap between blocks).

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

- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-21
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
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

### Change over 24h (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 4,537.20 | -9.86% |
| Average non-vote TPS | 3,388.67 | 2,672.27 | -21.14% |
| Average slot time (ms) | 417.00 | 365.30 | -12.40% |
| Active validators | 690.00 | 685.00 | -0.72% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 5,300,056,423.00 | 5,439,131,617.00 | +2.62% |
| SOL price | 86.96 | 91.85 | +5.62% |
| Stablecoin supply | 16,325,927,693.00 | 16,516,726,394.00 | +1.17% |
| 24h DEX volume | 3,009,837,694.95 | 2,770,509,439.33 | -7.95% |
| 24h chain fees | 13,676,729.38 | 11,078,485.08 | -19.00% |

### Change over 7d (vs run at 2026-08-14T18:37:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,201.34 | 4,537.20 | +7.99% |
| Average non-vote TPS | 2,555.64 | 2,672.27 | +4.56% |
| Average slot time (ms) | 415.90 | 365.30 | -12.17% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 4,805,244,467.00 | 5,439,131,617.00 | +13.19% |
| SOL price | 75.00 | 91.85 | +22.47% |
| Stablecoin supply | 16,096,537,114.00 | 16,516,726,394.00 | +2.61% |
| 24h DEX volume | 1,942,768,290.75 | 2,770,509,439.33 | +42.61% |
| 24h chain fees | 10,148,326.92 | 11,078,485.08 | +9.17% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 13.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
