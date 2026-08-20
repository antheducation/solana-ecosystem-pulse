# Solana Ecosystem Pulse

**Generated:** 2026-08-20T12:20:56Z · **Schema:** `1.0.0` · **Collection time:** 27.6s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $86.73 | +12.05% |
| Market cap | $50.58B | rank #7 |
| Total value locked | $5.30B | +8.17% |
| Stablecoin supply | $16.32B | +1.95% |
| DEX volume (24h) | $3.01B | +63.74% |
| Chain fees / REV (24h) | $13.59M | +54.89% |
| Non-vote TPS (1h avg) | 2,305 | peak 4,906 total |
| Active validators | 688 | 8 delinquent |
| Epoch 1019 | 61.09% complete | 168,089 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 59 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 6 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,297,166,576.00 sits 11.7 sigma above the median of the last 59 runs (4,821,339,539.00, +9.9%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 86.73 sits 12.5 sigma above the median of the last 59 runs (75.78, +14.4%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,009,837,694.95 sits 6.7 sigma above the median of the last 59 runs (1,546,444,167.56, +94.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 12.1% in 24h) | SOL price changed +12.1% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 8.2% in 24h) | Solana TVL changed +8.2% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 63.7% in 24h) | DEX volume changed +63.7% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 54.9% in 24h) | Chain fees changed +54.9% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | 24h chain fees is above its recent norm | Current 13,588,582.38 sits 3.2 sigma above the median of the last 59 runs (9,008,820.83, +50.8%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,305.2 average over the last 60 minutes; 2,565.2 in the latest sample.
- **Total TPS:** 3,960.8 average, 4,905.6 peak. Consensus votes account for 41.8% of all transactions.
- **Slot time:** 413.3 ms average (target 400 ms), worst 1-minute bucket 425.5 ms.
- **Block height:** 418,521,737 at absolute slot 440,471,911.
- **Epoch 1019:** slot 263,911 of 432,000 (61.09% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 93 ms |
| `solana-rpc.publicnode.com` | yes | 103 ms |
| `api.mainnet.solana.com` | yes | 64 ms |

## Validators & stake

- **688 active** validators, **8 delinquent** (1.15% by count, 0.027% by stake).
- **Total stake:** 435,241,268 SOL ($37.75B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.29%; 255 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.930% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.680% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.852% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.804% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.112% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.066% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.909% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.837% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.688% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.504% | 0% |

## Economics

- **SOL:** $86.73 (+12.05% 24h, +14.73% 7d, +10.75% 30d). Market cap $50.58B, 24h volume $5.78B (11.43% of cap). Price source: `coingecko`.
- **TVL:** $5.30B across 327 protocols - rank #3 of 461 chains, 6.35% of all tracked chain TVL. +9.83% over 7d, -60.0% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+1.51% 7d) - $3.08 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.01B in 24h, $12.09B over 7d across 119 venues. Volume/TVL turnover 0.568x per day.
- **REV (chain fees):** $13.59M in 24h, $256.87M over 30d. Retained chain revenue $6.02M (44.3% of fees). Annualised fees are 9.81% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,006,087 SOL circulating of 632,513,631 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +12.5% | +16.9% |
| 2 | Kamino Lend | Lending | $1.14B | +6.2% | +9.3% |
| 3 | Jupiter Lend | Lending | $1.03B | +7.0% | +10.0% |
| 4 | Raydium AMM | Dexs | $959.72M | +11.6% | +13.8% |
| 5 | Binance Staked SOL | Liquid Staking | $880.28M | +12.5% | +13.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $871.90M | +12.6% | +15.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $746.62M | +8.4% | +8.1% |
| 8 | BlackRock BUIDL | RWA | $740.49M | -0.1% | -0.0% |
| 9 | Solstice | Basis Trading | $506.08M | -0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $454.36M | +13.1% | +16.0% |
| 11 | xStocks | RWA | $405.60M | +6.0% | +7.6% |
| 12 | Sentora | Risk Curators | $365.59M | -0.1% | -0.9% |

The top five protocols hold 36.1% of Solana's tracked TVL. Summed across all 327 protocols the total is $14.69B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 34.2% · Lending 16.5% · Dexs 13.7% · RWA 12.9% · Derivatives 5.7% · Basis Trading 4.0%

### Tokenised assets

$2.48B of tokenised real-world assets and equities are locked on Solana - 16.920% of chain TVL.

- BlackRock BUIDL (RWA): $740.49M
- Solstice (Basis Trading): $506.08M
- xStocks (RWA): $405.60M
- OnRe (RWA): $272.22M
- Ondo Yield Assets (RWA): $179.22M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,088.3 unique fee payers** signed per block (1,648 distinct addresses in the union, 49.5% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-19T12:19:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,485.50 | 3,960.77 | +13.64% |
| Average non-vote TPS | 1,849.57 | 2,305.17 | +24.63% |
| Average slot time (ms) | 414.10 | 413.30 | -0.19% |
| Active validators | 685.00 | 688.00 | +0.44% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 4,914,919,992.00 | 5,297,166,576.00 | +7.78% |
| SOL price | 77.39 | 86.73 | +12.07% |
| Stablecoin supply | 16,008,130,055.00 | 16,322,738,591.00 | +1.97% |
| 24h DEX volume | 1,838,194,723.04 | 3,009,837,694.95 | +63.74% |
| 24h chain fees | 8,688,793.23 | 13,588,582.38 | +56.39% |

### Change over 7d (vs run at 2026-08-13T12:40:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,709.85 | 3,960.77 | +6.76% |
| Average non-vote TPS | 2,066.15 | 2,305.17 | +11.57% |
| Average slot time (ms) | 415.80 | 413.30 | -0.60% |
| Active validators | 687.00 | 688.00 | +0.15% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 4,819,382,015.00 | 5,297,166,576.00 | +9.91% |
| SOL price | 75.89 | 86.73 | +14.28% |
| Stablecoin supply | 16,080,183,048.00 | 16,322,738,591.00 | +1.51% |
| 24h DEX volume | 1,725,631,800.93 | 3,009,837,694.95 | +74.42% |
| 24h chain fees | 9,577,693.00 | 13,588,582.38 | +41.88% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
