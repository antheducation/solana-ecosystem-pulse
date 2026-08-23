# Solana Ecosystem Pulse

**Generated:** 2026-08-23T18:11:19Z · **Schema:** `1.0.0` · **Collection time:** 30.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.99 | +0.87% |
| Market cap | $55.40B | rank #7 |
| Total value locked | $5.59B | +0.74% |
| Stablecoin supply | $16.37B | -0.32% |
| DEX volume (24h) | $3.73B | +3.65% |
| Chain fees / REV (24h) | $12.02M | -9.88% |
| Non-vote TPS (1h avg) | 2,325 | peak 4,897 total |
| Active validators | 681 | 14 delinquent |
| Epoch 1021 | 32.85% complete | 290,069 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 61 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.10 sits 18.1 sigma below the median of the last 61 runs (416.00, -12.2%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,593,098,038.00 sits 12.9 sigma above the median of the last 61 runs (4,844,754,288.00, +15.4%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 94.99 sits 14.7 sigma above the median of the last 61 runs (76.22, +24.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 681.00 sits 4.7 sigma below the median of the last 61 runs (688.00, -1.0%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 14.00 sits 3.4 sigma above the median of the last 61 runs (9.00, +55.6%). | `zscore` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 3,732,294,477.70 sits 4.9 sigma above the median of the last 61 runs (1,650,837,789.28, +126.1%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,325.3 average over the last 60 minutes; 2,856.3 in the latest sample.
- **Total TPS:** 4,174.5 average, 4,896.8 peak. Consensus votes account for 44.3% of all transactions.
- **Slot time:** 365.1 ms average (target 400 ms), worst 1-minute bucket 382.2 ms.
- **Block height:** 419,263,008 at absolute slot 441,213,931.
- **Epoch 1021:** slot 141,931 of 432,000 (32.85% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.682% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 545 ms |
| `solana-rpc.publicnode.com` | yes | 102 ms |
| `api.mainnet.solana.com` | yes | 536 ms |

## Validators & stake

- **681 active** validators, **14 delinquent** (2.01% by count, 0.384% by stake).
- **Total stake:** 433,436,313 SOL ($41.17B); stake rate 68.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 46.12% of active stake.
- **Commission:** median 5.0%, mean 11.92%; 256 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 | 3.713% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 | 2.828% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 | 2.716% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 | 2.123% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 | 2.056% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 | 1.964% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 | 1.837% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 | 1.704% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 | 1.521% | 0% |

## Economics

- **SOL:** $94.99 (+0.87% 24h, +26.28% 7d, +28.49% 30d). Market cap $55.40B, 24h volume $4.46B (8.05% of cap). Price source: `coingecko`.
- **TVL:** $5.59B across 329 protocols - rank #3 of 462 chains, 6.07% of all tracked chain TVL. +16.31% over 7d, -57.8% from its ATH.
- **Stablecoins:** $16.37B circulating on Solana (+2.34% 7d) - $2.93 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.73B in 24h, $17.48B over 7d across 119 venues. Volume/TVL turnover 0.667x per day.
- **REV (chain fees):** $12.02M in 24h, $271.27M over 30d. Retained chain revenue $4.99M (41.6% of fees). Annualised fees are 7.92% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,276,808 SOL circulating of 632,749,918 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.42B | +1.0% | +26.4% |
| 2 | Kamino Lend | Lending | $1.19B | +0.8% | +14.7% |
| 3 | Jupiter Lend | Lending | $1.06B | +1.5% | +14.6% |
| 4 | Raydium AMM | Dexs | $1.05B | +1.2% | +24.2% |
| 5 | Binance Staked SOL | Liquid Staking | $965.46M | +2.5% | +26.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $956.49M | +1.2% | +27.1% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +0.0% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $746.31M | +1.2% | +9.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $493.27M | +1.3% | +26.2% |
| 10 | xStocks | RWA | $420.26M | +0.6% | +9.8% |
| 11 | Solstice | Basis Trading | $404.34M | +0.0% | -20.1% |
| 12 | Sentora | Risk Curators | $366.60M | +0.2% | -0.4% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 329 protocols the total is $15.55B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.4% · Lending 16.3% · Dexs 14.1% · RWA 12.6% · Derivatives 5.4% · Staking Pool 3.5%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.660% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $420.26M
- Solstice (Basis Trading): $404.34M
- OnRe (RWA): $274.97M
- Ondo Yield Assets (RWA): $178.54M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,030.3 unique fee payers** signed per block (1,559 distinct addresses in the union, 49.6% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-22T18:12:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,909.94 | 4,174.50 | +6.77% |
| Average non-vote TPS | 2,049.79 | 2,325.35 | +13.44% |
| Average slot time (ms) | 366.90 | 365.10 | -0.49% |
| Active validators | 687.00 | 681.00 | -0.87% |
| Delinquent validators | 8.00 | 14.00 | +75.00% |
| Solana TVL | 5,514,383,081.00 | 5,593,098,038.00 | +1.43% |
| SOL price | 94.15 | 94.99 | +0.89% |
| Stablecoin supply | 16,420,708,533.00 | 16,372,086,266.00 | -0.30% |
| 24h DEX volume | 3,600,948,276.22 | 3,732,294,477.70 | +3.65% |
| 24h chain fees | 13,332,529.88 | 12,017,709.26 | -9.86% |

### Change over 7d (vs run at 2026-08-16T18:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,797.96 | 4,174.50 | +9.91% |
| Average non-vote TPS | 2,151.97 | 2,325.35 | +8.06% |
| Average slot time (ms) | 415.20 | 365.10 | -12.07% |
| Active validators | 688.00 | 681.00 | -1.02% |
| Delinquent validators | 9.00 | 14.00 | +55.56% |
| Solana TVL | 4,804,122,508.00 | 5,593,098,038.00 | +16.42% |
| SOL price | 75.15 | 94.99 | +26.40% |
| Stablecoin supply | 15,997,960,401.00 | 16,372,086,266.00 | +2.34% |
| 24h DEX volume | 1,169,008,711.04 | 3,732,294,477.70 | +219.27% |
| 24h chain fees | 8,145,711.86 | 12,017,709.26 | +47.53% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 30.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
