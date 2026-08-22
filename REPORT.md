# Solana Ecosystem Pulse

**Generated:** 2026-08-22T00:30:17Z · **Schema:** `1.0.0` · **Collection time:** 22.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.02 | +6.28% |
| Market cap | $54.86B | rank #7 |
| Total value locked | $5.52B | +0.00% |
| Stablecoin supply | $16.52B | +1.17% |
| DEX volume (24h) | $2.96B | +7.05% |
| Chain fees / REV (24h) | $10.82M | -2.31% |
| Non-vote TPS (1h avg) | 2,452 | peak 5,158 total |
| Active validators | 682 | 12 delinquent |
| Epoch 1020 | 38.07% complete | 267,523 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 59 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.30 sits 14.4 sigma below the median of the last 59 runs (416.70, -12.3%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,519,461,055.00 sits 17.6 sigma above the median of the last 59 runs (4,827,587,784.00, +14.3%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.02 sits 18.8 sigma above the median of the last 59 runs (75.94, +23.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 682.00 sits 4.7 sigma below the median of the last 59 runs (689.00, -1.0%). | `zscore` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 2,961,868,880.89 sits 4.2 sigma above the median of the last 59 runs (1,581,973,855.56, +87.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,452.3 average over the last 60 minutes; 2,530.5 in the latest sample.
- **Total TPS:** 4,306.1 average, 5,158.4 peak. Consensus votes account for 43.0% of all transactions.
- **Slot time:** 365.3 ms average (target 400 ms), worst 1-minute bucket 387.1 ms.
- **Block height:** 418,854,007 at absolute slot 440,804,477.
- **Epoch 1020:** slot 164,477 of 432,000 (38.07% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 350 ms |
| `solana-rpc.publicnode.com` | yes | 241 ms |
| `api.mainnet.solana.com` | yes | 140 ms |

## Validators & stake

- **682 active** validators, **12 delinquent** (1.73% by count, 0.064% by stake).
- **Total stake:** 433,485,334 SOL ($40.76B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.34% and top 33 hold 45.95% of active stake.
- **Commission:** median 5.0%, mean 11.95%; 254 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.940% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.706% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.720% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.119% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.058% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.940% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.511% | 0% |

## Economics

- **SOL:** $94.02 (+6.28% 24h, +24.79% 7d, +20.63% 30d). Market cap $54.86B, 24h volume $6.75B (12.31% of cap). Price source: `coingecko`.
- **TVL:** $5.52B across 329 protocols - rank #3 of 461 chains, 6.26% of all tracked chain TVL. +14.60% over 7d, -58.3% from its ATH.
- **Stablecoins:** $16.52B circulating on Solana (+2.61% 7d) - $2.99 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.96B in 24h, $12.30B over 7d across 119 venues. Volume/TVL turnover 0.537x per day.
- **REV (chain fees):** $10.82M in 24h, $255.44M over 30d. Retained chain revenue $4.98M (46.0% of fees). Annualised fees are 7.20% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,177,464 SOL circulating of 632,639,796 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.40B | +7.1% | +24.4% |
| 2 | Kamino Lend | Lending | $1.18B | +4.9% | +12.9% |
| 3 | Jupiter Lend | Lending | $1.05B | +7.4% | +13.4% |
| 4 | Raydium AMM | Dexs | $1.03B | +6.7% | +22.0% |
| 5 | Binance Staked SOL | Liquid Staking | $944.75M | +6.8% | +23.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $940.06M | +7.3% | +24.8% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +4.9% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $752.27M | +4.3% | +10.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $490.87M | +8.0% | +25.5% |
| 10 | xStocks | RWA | $426.22M | +4.5% | +12.1% |
| 11 | Solstice | Basis Trading | $404.32M | -20.1% | -20.1% |
| 12 | Sentora | Risk Curators | $365.20M | +0.0% | -0.8% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 329 protocols the total is $15.32B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.3% · Lending 16.3% · Dexs 14.0% · RWA 12.8% · Derivatives 5.5% · Staking Pool 3.2%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.918% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $426.22M
- Solstice (Basis Trading): $404.32M
- OnRe (RWA): $273.03M
- Ondo Yield Assets (RWA): $178.25M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **984.7 unique fee payers** signed per block (1,411 distinct addresses in the union, 52.2% overlap between blocks).

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

- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-20
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

### Change over 24h (vs run at 2026-08-21T00:33:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,319.13 | 4,306.07 | -0.30% |
| Average non-vote TPS | 2,669.71 | 2,452.33 | -8.14% |
| Average slot time (ms) | 415.80 | 365.30 | -12.15% |
| Active validators | 690.00 | 682.00 | -1.16% |
| Delinquent validators | 6.00 | 12.00 | +100.00% |
| Solana TVL | 5,285,370,682.00 | 5,519,461,055.00 | +4.43% |
| SOL price | 88.31 | 94.02 | +6.47% |
| Stablecoin supply | 16,326,513,472.00 | 16,517,448,442.00 | +1.17% |
| 24h DEX volume | 3,150,837,936.95 | 2,961,868,880.89 | -6.00% |
| 24h chain fees | 13,758,063.85 | 10,823,009.54 | -21.33% |

### Change over 7d (vs run at 2026-08-15T00:30:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,332.32 | 4,306.07 | +29.22% |
| Average non-vote TPS | 1,691.60 | 2,452.33 | +44.97% |
| Average slot time (ms) | 416.50 | 365.30 | -12.29% |
| Active validators | 688.00 | 682.00 | -0.87% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 4,800,181,387.00 | 5,519,461,055.00 | +14.98% |
| SOL price | 75.32 | 94.02 | +24.83% |
| Stablecoin supply | 16,097,978,031.00 | 16,517,448,442.00 | +2.61% |
| 24h DEX volume | 1,934,797,865.79 | 2,961,868,880.89 | +53.08% |
| 24h chain fees | 10,271,516.95 | 10,823,009.54 | +5.37% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
