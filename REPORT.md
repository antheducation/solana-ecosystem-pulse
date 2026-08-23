# Solana Ecosystem Pulse

**Generated:** 2026-08-23T12:14:34Z · **Schema:** `1.0.0` · **Collection time:** 17.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.24 | +0.50% |
| Market cap | $54.99B | rank #7 |
| Total value locked | $5.52B | -0.84% |
| Stablecoin supply | $16.37B | -0.31% |
| DEX volume (24h) | $3.73B | +3.65% |
| Chain fees / REV (24h) | $11.92M | -10.63% |
| Non-vote TPS (1h avg) | 1,517 | peak 3,879 total |
| Active validators | 683 | 12 delinquent |
| Epoch 1021 | 19.30% complete | 348,637 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 61 historical runs, sigma = 3.0).

Critical 0 · Serious 4 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.10 sits 18.1 sigma below the median of the last 61 runs (416.00, -12.2%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,519,339,285.00 sits 11.7 sigma above the median of the last 61 runs (4,844,614,677.00, +13.9%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.24 sits 16.8 sigma above the median of the last 61 runs (76.02, +24.0%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,732,294,477.70 sits 5.0 sigma above the median of the last 61 runs (1,642,311,971.56, +127.3%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 683.00 sits 3.4 sigma below the median of the last 61 runs (688.00, -0.7%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,517.2 average over the last 60 minutes; 1,429.3 in the latest sample.
- **Total TPS:** 3,375.7 average, 3,879.3 peak. Consensus votes account for 55.1% of all transactions.
- **Slot time:** 365.1 ms average (target 400 ms), worst 1-minute bucket 384.6 ms.
- **Block height:** 419,204,519 at absolute slot 441,155,363.
- **Epoch 1021:** slot 83,363 of 432,000 (19.30% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 278 ms |
| `solana-rpc.publicnode.com` | yes | 32 ms |
| `api.mainnet.solana.com` | yes | 267 ms |

## Validators & stake

- **683 active** validators, **12 delinquent** (1.73% by count, 0.343% by stake).
- **Total stake:** 433,436,313 SOL ($40.85B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 46.10% of active stake.
- **Commission:** median 5.0%, mean 11.93%; 255 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 | 3.932% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 | 3.712% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 | 2.827% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 | 2.715% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 | 2.122% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 | 2.055% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 | 1.963% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 | 1.836% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 | 1.704% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 | 1.521% | 0% |

## Economics

- **SOL:** $94.24 (+0.50% 24h, +25.30% 7d, +25.53% 30d). Market cap $54.99B, 24h volume $4.42B (8.05% of cap). Price source: `coingecko`.
- **TVL:** $5.52B across 328 protocols - rank #3 of 462 chains, 6.06% of all tracked chain TVL. +14.49% over 7d, -58.4% from its ATH.
- **Stablecoins:** $16.37B circulating on Solana (+2.34% 7d) - $2.97 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.73B in 24h, $17.48B over 7d across 119 venues. Volume/TVL turnover 0.676x per day.
- **REV (chain fees):** $11.92M in 24h, $271.17M over 30d. Retained chain revenue $4.99M (41.9% of fees). Annualised fees are 7.91% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,277,030 SOL circulating of 632,750,140 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.40B | +0.5% | +24.4% |
| 2 | Kamino Lend | Lending | $1.18B | +0.4% | +13.6% |
| 3 | Jupiter Lend | Lending | $1.05B | +0.0% | +12.8% |
| 4 | Raydium AMM | Dexs | $1.03B | +0.3% | +22.6% |
| 5 | Binance Staked SOL | Liquid Staking | $947.78M | +0.7% | +23.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $939.22M | +0.4% | +24.8% |
| 7 | BlackRock BUIDL | RWA | $777.14M | -0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $736.84M | +0.1% | +8.0% |
| 9 | Jupiter Staked SOL | Liquid Staking | $484.02M | -0.1% | +23.9% |
| 10 | xStocks | RWA | $418.36M | -0.6% | +9.3% |
| 11 | Solstice | Basis Trading | $404.37M | -0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $366.05M | -0.1% | -0.6% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.35B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.2% · Lending 16.3% · Dexs 14.1% · RWA 12.7% · Derivatives 5.4% · Staking Pool 3.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.846% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $418.36M
- Solstice (Basis Trading): $404.37M
- OnRe (RWA): $274.07M
- Ondo Yield Assets (RWA): $178.70M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **904.3 unique fee payers** signed per block (1,247 distinct addresses in the union, 54.0% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-22T12:14:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,268.67 | 3,375.74 | +3.28% |
| Average non-vote TPS | 1,410.74 | 1,517.25 | +7.55% |
| Average slot time (ms) | 366.70 | 365.10 | -0.44% |
| Active validators | 686.00 | 683.00 | -0.44% |
| Delinquent validators | 8.00 | 12.00 | +50.00% |
| Solana TVL | 5,539,353,430.00 | 5,519,339,285.00 | -0.36% |
| SOL price | 93.74 | 94.24 | +0.53% |
| Stablecoin supply | 16,419,230,307.00 | 16,372,596,016.00 | -0.28% |
| 24h DEX volume | 3,600,948,276.22 | 3,732,294,477.70 | +3.65% |
| 24h chain fees | 13,236,625.88 | 11,916,880.26 | -9.97% |

### Change over 7d (vs run at 2026-08-16T12:14:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,832.98 | 3,375.74 | +19.16% |
| Average non-vote TPS | 1,185.63 | 1,517.25 | +27.97% |
| Average slot time (ms) | 415.20 | 365.10 | -12.07% |
| Active validators | 688.00 | 683.00 | -0.73% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,805,328,364.00 | 5,519,339,285.00 | +14.86% |
| SOL price | 75.20 | 94.24 | +25.32% |
| Stablecoin supply | 15,999,096,240.00 | 16,372,596,016.00 | +2.33% |
| 24h DEX volume | 1,169,008,711.04 | 3,732,294,477.70 | +219.27% |
| 24h chain fees | 8,054,343.86 | 11,916,880.26 | +47.96% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 16.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
