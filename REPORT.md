# Solana Ecosystem Pulse

**Generated:** 2026-08-19T18:15:30Z · **Schema:** `1.0.0` · **Collection time:** 13.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $81.32 | +5.64% |
| Market cap | $47.41B | rank #7 |
| Total value locked | $5.06B | +4.35% |
| Stablecoin supply | $16.01B | +0.20% |
| DEX volume (24h) | $1.84B | +24.62% |
| Chain fees / REV (24h) | $8.77M | -22.25% |
| Non-vote TPS (1h avg) | 3,461 | peak 5,856 total |
| Active validators | 686 | 9 delinquent |
| Epoch 1019 | 24.83% complete | 324,713 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 56 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,060,698,995.00 sits 5.9 sigma above the median of the last 56 runs (4,820,073,034.50, +5.0%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 81.32 sits 7.0 sigma above the median of the last 56 runs (75.63, +7.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is above its recent norm | Current 5,093.61 sits 3.1 sigma above the median of the last 56 runs (3,461.59, +47.1%). | `zscore` |
| [WARNING] | Average non-vote TPS is above its recent norm | Current 3,460.99 sits 3.1 sigma above the median of the last 56 runs (1,828.44, +89.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 3,461.0 average over the last 60 minutes; 3,447.0 in the latest sample.
- **Total TPS:** 5,093.6 average, 5,855.8 peak. Consensus votes account for 32.1% of all transactions.
- **Slot time:** 416.7 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,365,294 at absolute slot 440,315,287.
- **Epoch 1019:** slot 107,287 of 432,000 (24.83% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 132 ms |
| `solana-rpc.publicnode.com` | yes | 42 ms |
| `api.mainnet.solana.com` | yes | 46 ms |

## Validators & stake

- **686 active** validators, **9 delinquent** (1.29% by count, 0.099% by stake).
- **Total stake:** 435,241,268 SOL ($35.39B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.90% of active stake.
- **Commission:** median 5.0%, mean 11.90%; 255 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.933% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.682% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.854% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.806% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.113% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.068% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.911% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.689% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.506% | 0% |

## Economics

- **SOL:** $81.32 (+5.64% 24h, +7.21% 7d, +4.66% 30d). Market cap $47.41B, 24h volume $2.97B (6.26% of cap). Price source: `coingecko`.
- **TVL:** $5.06B across 327 protocols - rank #3 of 461 chains, 6.37% of all tracked chain TVL. +4.06% over 7d, -61.8% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.75% 7d) - $3.16 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.84B in 24h, $10.79B over 7d across 119 venues. Volume/TVL turnover 0.363x per day.
- **REV (chain fees):** $8.77M in 24h, $250.65M over 30d. Retained chain revenue $4.04M (46.1% of fees). Annualised fees are 6.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,007,047 SOL circulating of 632,514,300 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.23B | +6.8% | +9.5% |
| 2 | Kamino Lend | Lending | $1.10B | +3.0% | +4.3% |
| 3 | Jupiter Lend | Lending | $977.43M | +2.4% | +3.3% |
| 4 | Raydium AMM | Dexs | $904.95M | +6.6% | +6.2% |
| 5 | Binance Staked SOL | Liquid Staking | $832.29M | +6.4% | +6.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $822.65M | +6.8% | +7.9% |
| 7 | BlackRock BUIDL | RWA | $741.49M | +0.0% | +1.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $715.88M | +4.2% | +2.9% |
| 9 | Solstice | Basis Trading | $504.39M | -0.4% | -0.3% |
| 10 | Jupiter Staked SOL | Liquid Staking | $427.37M | +7.2% | +8.4% |
| 11 | xStocks | RWA | $399.43M | +4.3% | +5.8% |
| 12 | Sentora | Risk Curators | $365.97M | -0.4% | -0.8% |

The top five protocols hold 35.7% of Solana's tracked TVL. Summed across all 327 protocols the total is $14.11B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 33.7% · Lending 16.5% · Dexs 13.5% · RWA 13.5% · Derivatives 5.7% · Basis Trading 4.1%

### Tokenised assets

$2.48B of tokenised real-world assets and equities are locked on Solana - 17.590% of chain TVL.

- BlackRock BUIDL (RWA): $741.49M
- Solstice (Basis Trading): $504.39M
- xStocks (RWA): $399.43M
- OnRe (RWA): $272.01M
- Ondo Yield Assets (RWA): $179.14M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,047.7 unique fee payers** signed per block (1,568 distinct addresses in the union, 50.1% overlap between blocks).

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
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-19
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-18
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

### Change over 24h (vs run at 2026-08-18T18:18:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,157.63 | 5,093.61 | +22.51% |
| Average non-vote TPS | 2,510.42 | 3,460.99 | +37.86% |
| Average slot time (ms) | 414.50 | 416.70 | +0.53% |
| Active validators | 688.00 | 686.00 | -0.29% |
| Delinquent validators | 7.00 | 9.00 | +28.57% |
| Solana TVL | 4,885,957,310.00 | 5,060,698,995.00 | +3.58% |
| SOL price | 77.08 | 81.32 | +5.50% |
| Stablecoin supply | 15,977,966,490.00 | 16,009,704,067.00 | +0.20% |
| 24h DEX volume | 1,474,970,358.36 | 1,838,194,723.04 | +24.63% |
| 24h chain fees | 11,189,593.30 | 8,772,755.23 | -21.60% |

### Change over 7d (vs run at 2026-08-12T18:43:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,653.97 | 5,093.61 | +9.45% |
| Average non-vote TPS | 3,053.77 | 3,460.99 | +13.33% |
| Average slot time (ms) | 422.30 | 416.70 | -1.33% |
| Active validators | 685.00 | 686.00 | +0.15% |
| Delinquent validators | 14.00 | 9.00 | -35.71% |
| Solana TVL | 4,816,384,183.00 | 5,060,698,995.00 | +5.07% |
| SOL price | 75.94 | 81.32 | +7.08% |
| Stablecoin supply | 16,295,860,195.00 | 16,009,704,067.00 | -1.76% |
| 24h DEX volume | 1,650,837,789.28 | 1,838,194,723.04 | +11.35% |
| 24h chain fees | 9,976,052.23 | 8,772,755.23 | -12.06% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 13.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
