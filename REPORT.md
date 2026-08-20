# Solana Ecosystem Pulse

**Generated:** 2026-08-20T06:22:42Z · **Schema:** `1.0.0` · **Collection time:** 32.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $84.84 | +10.45% |
| Market cap | $49.46B | rank #7 |
| Total value locked | $5.20B | +6.17% |
| Stablecoin supply | $16.32B | +1.95% |
| DEX volume (24h) | $2.79B | +51.75% |
| Chain fees / REV (24h) | $13.17M | +50.15% |
| Non-vote TPS (1h avg) | 1,404 | peak 3,773 total |
| Active validators | 688 | 8 delinquent |
| Epoch 1019 | 49.10% complete | 219,893 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 58 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 6 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,198,850,712.00 sits 9.3 sigma above the median of the last 58 runs (4,821,051,796.50, +7.8%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 84.84 sits 11.0 sigma above the median of the last 58 runs (75.73, +12.0%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 2,789,524,387.95 sits 5.7 sigma above the median of the last 58 runs (1,536,821,446.13, +81.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 10.4% in 24h) | SOL price changed +10.4% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 6.2% in 24h) | Solana TVL changed +6.2% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 51.8% in 24h) | DEX volume changed +51.8% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 50.1% in 24h) | Chain fees changed +50.1% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | 24h chain fees is above its recent norm | Current 13,172,440.83 sits 3.0 sigma above the median of the last 58 runs (8,993,486.97, +46.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,404.1 average over the last 60 minutes; 1,783.3 in the latest sample.
- **Total TPS:** 3,047.3 average, 3,772.9 peak. Consensus votes account for 53.9% of all transactions.
- **Slot time:** 416.0 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,470,009 at absolute slot 440,420,107.
- **Epoch 1019:** slot 212,107 of 432,000 (49.10% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 593 ms |
| `solana-rpc.publicnode.com` | yes | 186 ms |
| `api.mainnet.solana.com` | yes | 286 ms |

## Validators & stake

- **688 active** validators, **8 delinquent** (1.15% by count, 0.023% by stake).
- **Total stake:** 435,241,268 SOL ($36.93B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.01%; 256 validators at 0% and 61 at 100%.

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

- **SOL:** $84.84 (+10.45% 24h, +11.02% 7d, +8.21% 30d). Market cap $49.46B, 24h volume $4.79B (9.69% of cap). Price source: `coingecko`.
- **TVL:** $5.20B across 327 protocols - rank #2 of 461 chains, 6.36% of all tracked chain TVL. +7.79% over 7d, -60.7% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+1.51% 7d) - $3.14 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.79B in 24h, $11.73B over 7d across 119 venues. Volume/TVL turnover 0.537x per day.
- **REV (chain fees):** $13.17M in 24h, $255.81M over 30d. Retained chain revenue $5.93M (45.0% of fees). Annualised fees are 9.72% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,006,283 SOL circulating of 632,513,828 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.27B | +10.4% | +14.0% |
| 2 | Kamino Lend | Lending | $1.12B | +5.0% | +7.5% |
| 3 | Jupiter Lend | Lending | $1.00B | +5.3% | +7.6% |
| 4 | Raydium AMM | Dexs | $935.13M | +9.3% | +10.9% |
| 5 | Binance Staked SOL | Liquid Staking | $854.00M | +10.0% | +10.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $849.31M | +10.4% | +12.4% |
| 7 | BlackRock BUIDL | RWA | $740.49M | -0.1% | -0.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $729.39M | +6.4% | +5.6% |
| 9 | Solstice | Basis Trading | $506.19M | -0.0% | +0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $440.36M | +10.5% | +12.4% |
| 11 | xStocks | RWA | $402.91M | +5.8% | +6.9% |
| 12 | Sentora | Risk Curators | $365.55M | -0.1% | -0.9% |

The top five protocols hold 35.9% of Solana's tracked TVL. Summed across all 327 protocols the total is $14.42B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 33.9% · Lending 16.5% · Dexs 13.7% · RWA 13.2% · Derivatives 5.7% · Basis Trading 4.0%

### Tokenised assets

$2.48B of tokenised real-world assets and equities are locked on Solana - 17.215% of chain TVL.

- BlackRock BUIDL (RWA): $740.49M
- Solstice (Basis Trading): $506.19M
- xStocks (RWA): $402.91M
- OnRe (RWA): $272.17M
- Ondo Yield Assets (RWA): $179.10M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,029.0 unique fee payers** signed per block (1,612 distinct addresses in the union, 47.8% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-19T06:21:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,957.15 | 3,047.31 | +3.05% |
| Average non-vote TPS | 1,329.70 | 1,404.08 | +5.59% |
| Average slot time (ms) | 415.40 | 416.00 | +0.14% |
| Active validators | 676.00 | 688.00 | +1.78% |
| Delinquent validators | 19.00 | 8.00 | -57.89% |
| Solana TVL | 4,894,911,440.00 | 5,198,850,712.00 | +6.21% |
| SOL price | 76.73 | 84.84 | +10.57% |
| Stablecoin supply | 16,009,559,610.00 | 16,322,645,608.00 | +1.96% |
| 24h DEX volume | 1,820,756,097.04 | 2,789,524,387.95 | +53.21% |
| 24h chain fees | 8,714,303.23 | 13,172,440.83 | +51.16% |

### Change over 7d (vs run at 2026-08-13T07:07:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,029.81 | 3,047.31 | +0.58% |
| Average non-vote TPS | 1,395.25 | 1,404.08 | +0.63% |
| Average slot time (ms) | 418.10 | 416.00 | -0.50% |
| Active validators | 688.00 | 688.00 | +0.00% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 4,833,739,893.00 | 5,198,850,712.00 | +7.55% |
| SOL price | 76.37 | 84.84 | +11.09% |
| Stablecoin supply | 16,079,497,125.00 | 16,322,645,608.00 | +1.51% |
| 24h DEX volume | 1,683,289,146.93 | 2,789,524,387.95 | +65.72% |
| 24h chain fees | 9,636,717.00 | 13,172,440.83 | +36.69% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 32.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
