# Solana Ecosystem Pulse

**Generated:** 2026-08-22T18:12:00Z · **Schema:** `1.0.0` · **Collection time:** 15.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.15 | +2.52% |
| Market cap | $54.94B | rank #7 |
| Total value locked | $5.51B | +3.42% |
| Stablecoin supply | $16.42B | -0.59% |
| DEX volume (24h) | $3.60B | +30.15% |
| Chain fees / REV (24h) | $13.33M | +20.35% |
| Non-vote TPS (1h avg) | 2,050 | peak 4,676 total |
| Active validators | 687 | 8 delinquent |
| Epoch 1020 | 78.27% complete | 93,886 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 60 historical runs, sigma = 3.0).

Critical 0 · Serious 4 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.90 sits 14.5 sigma below the median of the last 60 runs (416.50, -11.9%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,514,383,081.00 sits 16.8 sigma above the median of the last 60 runs (4,832,885,373.50, +14.1%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.15 sits 18.3 sigma above the median of the last 60 runs (75.95, +24.0%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,600,948,276.22 sits 5.4 sigma above the median of the last 60 runs (1,612,403,611.56, +123.3%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,049.8 average over the last 60 minutes; 1,964.1 in the latest sample.
- **Total TPS:** 3,909.9 average, 4,676.0 peak. Consensus votes account for 47.6% of all transactions.
- **Slot time:** 366.9 ms average (target 400 ms), worst 1-minute bucket 387.1 ms.
- **Block height:** 419,027,468 at absolute slot 440,978,114.
- **Epoch 1020:** slot 338,114 of 432,000 (78.27% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 149 ms |
| `solana-rpc.publicnode.com` | yes | 172 ms |
| `api.mainnet.solana.com` | yes | 99 ms |

## Validators & stake

- **687 active** validators, **8 delinquent** (1.15% by count, 0.014% by stake).
- **Total stake:** 433,485,334 SOL ($40.81B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.16%; 256 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.704% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.718% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.118% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.057% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.939% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.511% | 0% |

## Economics

- **SOL:** $94.15 (+2.52% 24h, +24.57% 7d, +24.57% 30d). Market cap $54.94B, 24h volume $8.26B (15.04% of cap). Price source: `coingecko`.
- **TVL:** $5.51B across 330 protocols - rank #3 of 462 chains, 6.34% of all tracked chain TVL. +14.48% over 7d, -58.4% from its ATH.
- **Stablecoins:** $16.42B circulating on Solana (+2.57% 7d) - $2.98 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.60B in 24h, $14.92B over 7d across 119 venues. Volume/TVL turnover 0.653x per day.
- **REV (chain fees):** $13.33M in 24h, $266.63M over 30d. Retained chain revenue $5.31M (39.8% of fees). Annualised fees are 8.86% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,176,832 SOL circulating of 632,639,162 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.40B | +2.2% | +24.1% |
| 2 | Kamino Lend | Lending | $1.18B | +1.0% | +12.6% |
| 3 | Jupiter Lend | Lending | $1.04B | +0.9% | +12.8% |
| 4 | Raydium AMM | Dexs | $1.03B | +2.4% | +22.3% |
| 5 | Binance Staked SOL | Liquid Staking | $942.36M | +2.1% | +22.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $936.47M | +2.0% | +24.3% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +4.9% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $737.14M | -0.5% | +7.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $483.24M | +1.3% | +23.6% |
| 10 | xStocks | RWA | $419.24M | -0.7% | +10.3% |
| 11 | Solstice | Basis Trading | $404.32M | +0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $365.90M | +0.8% | -0.6% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.32B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.2% · Lending 16.3% · Dexs 14.2% · RWA 12.7% · Derivatives 5.4% · Staking Pool 3.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.878% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $419.24M
- Solstice (Basis Trading): $404.32M
- OnRe (RWA): $273.35M
- Ondo Yield Assets (RWA): $179.06M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **956.3 unique fee payers** signed per block (1,324 distinct addresses in the union, 53.9% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-21T18:19:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,537.20 | 3,909.94 | -13.82% |
| Average non-vote TPS | 2,672.27 | 2,049.79 | -23.29% |
| Average slot time (ms) | 365.30 | 366.90 | +0.44% |
| Active validators | 685.00 | 687.00 | +0.29% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 5,439,131,617.00 | 5,514,383,081.00 | +1.38% |
| SOL price | 91.85 | 94.15 | +2.50% |
| Stablecoin supply | 16,516,726,394.00 | 16,420,708,533.00 | -0.58% |
| 24h DEX volume | 2,770,509,439.33 | 3,600,948,276.22 | +29.97% |
| 24h chain fees | 11,078,485.08 | 13,332,529.88 | +20.35% |

### Change over 7d (vs run at 2026-08-15T18:10:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,866.12 | 3,909.94 | +1.13% |
| Average non-vote TPS | 2,226.46 | 2,049.79 | -7.94% |
| Average slot time (ms) | 416.10 | 366.90 | -11.82% |
| Active validators | 687.00 | 687.00 | +0.00% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 4,817,167,805.00 | 5,514,383,081.00 | +14.47% |
| SOL price | 75.57 | 94.15 | +24.59% |
| Stablecoin supply | 16,008,773,555.00 | 16,420,708,533.00 | +2.57% |
| 24h DEX volume | 1,612,403,611.56 | 3,600,948,276.22 | +123.33% |
| 24h chain fees | 8,047,086.79 | 13,332,529.88 | +65.68% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
