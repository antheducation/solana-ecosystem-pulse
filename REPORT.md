# Solana Ecosystem Pulse

**Generated:** 2026-08-20T00:30:35Z · **Schema:** `1.0.0` · **Collection time:** 12.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $85.66 | +11.39% |
| Market cap | $49.93B | rank #7 |
| Total value locked | $5.19B | +6.31% |
| Stablecoin supply | $16.01B | +0.20% |
| DEX volume (24h) | $2.19B | +19.10% |
| Chain fees / REV (24h) | $9.65M | +10.01% |
| Non-vote TPS (1h avg) | 2,638 | peak 5,362 total |
| Active validators | 688 | 8 delinquent |
| Epoch 1019 | 37.33% complete | 270,718 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 57 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,190,256,197.00 sits 9.1 sigma above the median of the last 57 runs (4,820,764,054.00, +7.7%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 85.66 sits 12.2 sigma above the median of the last 57 runs (75.68, +13.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 11.4% in 24h) | SOL price changed +11.4% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 6.3% in 24h) | Solana TVL changed +6.3% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 2,189,292,543.00 sits 3.0 sigma above the median of the last 57 runs (1,527,198,724.71, +43.4%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,638.5 average over the last 60 minutes; 1,718.8 in the latest sample.
- **Total TPS:** 4,289.3 average, 5,362.1 peak. Consensus votes account for 38.5% of all transactions.
- **Slot time:** 414.4 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,419,217 at absolute slot 440,369,282.
- **Epoch 1019:** slot 161,282 of 432,000 (37.33% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 64 ms |
| `solana-rpc.publicnode.com` | yes | 116 ms |
| `api.mainnet.solana.com` | yes | 39 ms |

## Validators & stake

- **688 active** validators, **8 delinquent** (1.15% by count, 0.023% by stake).
- **Total stake:** 435,241,268 SOL ($37.28B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 11.87%; 257 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.930% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.680% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.852% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.803% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.112% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.066% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.909% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.837% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.688% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.504% | 0% |

## Economics

- **SOL:** $85.66 (+11.39% 24h, +13.37% 7d, +10.17% 30d). Market cap $49.93B, 24h volume $4.46B (8.92% of cap). Price source: `coingecko`.
- **TVL:** $5.19B across 327 protocols - rank #3 of 461 chains, 6.33% of all tracked chain TVL. +6.02% over 7d, -61.0% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.75% 7d) - $3.08 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.19B in 24h, $9.73B over 7d across 119 venues. Volume/TVL turnover 0.422x per day.
- **REV (chain fees):** $9.65M in 24h, $245.72M over 30d. Retained chain revenue $4.79M (49.6% of fees). Annualised fees are 7.05% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,006,477 SOL circulating of 632,514,020 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.28B | +10.8% | +14.6% |
| 2 | Kamino Lend | Lending | $1.12B | +6.5% | +7.5% |
| 3 | Jupiter Lend | Lending | $1.02B | +6.6% | +9.0% |
| 4 | Raydium AMM | Dexs | $908.08M | +6.0% | +7.7% |
| 5 | Binance Staked SOL | Liquid Staking | $863.32M | +10.2% | +11.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $853.91M | +10.8% | +13.0% |
| 7 | BlackRock BUIDL | RWA | $740.49M | -0.1% | -0.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $732.94M | +6.6% | +6.1% |
| 9 | Solstice | Basis Trading | $506.21M | -0.0% | +0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $443.51M | +11.0% | +13.2% |
| 11 | xStocks | RWA | $404.36M | +5.9% | +7.3% |
| 12 | Sentora | Risk Curators | $366.20M | -0.0% | -0.7% |

The top five protocols hold 35.9% of Solana's tracked TVL. Summed across all 327 protocols the total is $14.46B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 34.1% · Lending 16.6% · Dexs 13.5% · RWA 13.1% · Derivatives 5.7% · Basis Trading 4.0%

### Tokenised assets

$2.48B of tokenised real-world assets and equities are locked on Solana - 17.183% of chain TVL.

- BlackRock BUIDL (RWA): $740.49M
- Solstice (Basis Trading): $506.21M
- xStocks (RWA): $404.36M
- OnRe (RWA): $272.06M
- Ondo Yield Assets (RWA): $179.08M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **964.7 unique fee payers** signed per block (1,371 distinct addresses in the union, 52.6% overlap between blocks).

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

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-19
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-19
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-19
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07

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

### Change over 24h (vs run at 2026-08-19T00:30:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,748.83 | 4,289.29 | +14.42% |
| Average non-vote TPS | 2,104.87 | 2,638.50 | +25.35% |
| Average slot time (ms) | 416.70 | 414.40 | -0.55% |
| Active validators | 689.00 | 688.00 | -0.15% |
| Delinquent validators | 6.00 | 8.00 | +33.33% |
| Solana TVL | 4,899,420,258.00 | 5,190,256,197.00 | +5.94% |
| SOL price | 76.89 | 85.66 | +11.41% |
| Stablecoin supply | 15,978,264,279.00 | 16,010,344,860.00 | +0.20% |
| 24h DEX volume | 1,456,594,741.93 | 2,189,292,543.00 | +50.30% |
| 24h chain fees | 10,986,421.95 | 9,650,957.28 | -12.16% |

### Change over 7d (vs run at 2026-08-13T00:54:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,733.82 | 4,289.29 | +14.88% |
| Average non-vote TPS | 2,099.07 | 2,638.50 | +25.70% |
| Average slot time (ms) | 416.80 | 414.40 | -0.58% |
| Active validators | 688.00 | 688.00 | +0.00% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 4,752,747,008.00 | 5,190,256,197.00 | +9.21% |
| SOL price | 75.58 | 85.66 | +13.34% |
| Stablecoin supply | 16,294,969,967.00 | 16,010,344,860.00 | -1.75% |
| 24h DEX volume | 1,684,395,735.93 | 2,189,292,543.00 | +29.97% |
| 24h chain fees | 9,848,639.11 | 9,650,957.28 | -2.01% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
