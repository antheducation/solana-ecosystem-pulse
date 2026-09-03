# Solana Ecosystem Pulse

**Generated:** 2026-09-03T10:13:49Z · **Schema:** `1.0.0` · **Collection time:** 12.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.09 | +1.66% |
| Market cap | $58.58B | rank #7 |
| Total value locked | $5.75B | +2.06% |
| Stablecoin supply | $16.10B | +1.56% |
| DEX volume (24h) | $2.33B | +7.16% |
| Chain fees / REV (24h) | $11.21M | -11.36% |
| Non-vote TPS (1h avg) | 1,359 | peak 3,993 total |
| Active validators | 677 | 18 delinquent |
| Epoch 1027 | 65.17% complete | 150,470 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 66 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,358.6 average over the last 60 minutes; 1,291.7 in the latest sample.
- **Total TPS:** 3,500.1 average, 3,993.1 peak. Consensus votes account for 61.2% of all transactions.
- **Slot time:** 314.5 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 421,992,743 at absolute slot 443,945,530.
- **Epoch 1027:** slot 281,530 of 432,000 (65.17% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 80 ms |
| `solana-rpc.publicnode.com` | yes | 64 ms |
| `api.mainnet.solana.com` | yes | 75 ms |

## Validators & stake

- **677 active** validators, **18 delinquent** (2.59% by count, 0.046% by stake).
- **Total stake:** 438,422,357 SOL ($43.88B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 244 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.959% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,325,737 | 3.725% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,462,274 | 2.844% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,304,498 | 2.580% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,565,273 | 2.183% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,486 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,040,435 | 2.063% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,220,140 | 1.648% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,125,475 | 1.626% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,590,653 | 1.504% | 0% |

## Economics

- **SOL:** $100.09 (+1.66% 24h, -4.09% 7d, +36.72% 30d). Market cap $58.58B, 24h volume $3.12B (5.33% of cap). Price source: `coingecko`.
- **TVL:** $5.75B across 340 protocols - rank #2 of 465 chains, 6.72% of all tracked chain TVL. -0.16% over 7d, -56.5% from its ATH.
- **Stablecoins:** $16.10B circulating on Solana (-0.22% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.33B in 24h, $16.71B over 7d across 121 venues. Volume/TVL turnover 0.404x per day.
- **REV (chain fees):** $11.21M in 24h, $334.46M over 30d. Retained chain revenue $4.71M (42.0% of fees). Annualised fees are 6.98% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,274,938 SOL circulating of 633,360,974 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.54B | +1.6% | +0.1% |
| 2 | Kamino Lend | Lending | $1.28B | +3.6% | +5.7% |
| 3 | Raydium AMM | Dexs | $1.09B | +0.5% | -1.6% |
| 4 | Jupiter Lend | Lending | $1.07B | +1.0% | -1.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | +1.5% | +1.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.01B | +1.6% | +0.0% |
| 7 | BlackRock BUIDL | RWA | $890.69M | +0.4% | +0.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $748.28M | +0.9% | -2.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $521.03M | +1.3% | -0.6% |
| 10 | xStocks | RWA | $436.72M | +1.3% | +1.5% |
| 11 | Marinade Native | Staking Pool | $402.29M | +1.9% | +0.2% |
| 12 | Sentora | Risk Curators | $376.45M | +3.9% | +3.6% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.40B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.5% · Lending 16.0% · Dexs 13.9% · RWA 12.7% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.690% of chain TVL.

- BlackRock BUIDL (RWA): $890.69M
- xStocks (RWA): $436.72M
- OnRe (RWA): $288.99M
- Solstice (Basis Trading): $249.83M
- Ondo Yield Assets (RWA): $179.13M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **899.0 unique fee payers** signed per block (1,253 distinct addresses in the union, 53.5% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29

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

### Change over 24h (vs run at 2026-09-02T10:03:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,149.23 | 3,500.09 | +11.14% |
| Average non-vote TPS | 1,014.87 | 1,358.56 | +33.87% |
| Average slot time (ms) | 315.10 | 314.50 | -0.19% |
| Active validators | 673.00 | 677.00 | +0.59% |
| Delinquent validators | 22.00 | 18.00 | -18.18% |
| Solana TVL | 5,706,889,294.00 | 5,754,182,822.00 | +0.83% |
| SOL price | 98.48 | 100.09 | +1.63% |
| Stablecoin supply | 15,850,556,625.00 | 16,099,204,296.00 | +1.57% |
| 24h DEX volume | 2,246,687,191.49 | 2,327,024,999.32 | +3.58% |
| 24h chain fees | 12,266,833.67 | 11,210,281.15 | -8.61% |

### Change over 7d (vs run at 2026-08-27T05:23:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,396.37 | 3,500.09 | +3.05% |
| Average non-vote TPS | 1,521.66 | 1,358.56 | -10.72% |
| Average slot time (ms) | 364.30 | 314.50 | -13.67% |
| Active validators | 686.00 | 677.00 | -1.31% |
| Delinquent validators | 11.00 | 18.00 | +63.64% |
| Solana TVL | 5,770,223,599.00 | 5,754,182,822.00 | -0.28% |
| SOL price | 100.92 | 100.09 | -0.82% |
| Stablecoin supply | 16,290,346,473.00 | 16,099,204,296.00 | -1.17% |
| 24h DEX volume | 2,481,205,722.00 | 2,327,024,999.32 | -6.21% |
| 24h chain fees | 14,682,184.01 | 11,210,281.15 | -23.65% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,500.09 | -11.04% |
| Average non-vote TPS | 2,312.46 | 1,358.56 | -41.25% |
| Average slot time (ms) | 424.10 | 314.50 | -25.84% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,754,182,822.00 | +21.40% |
| SOL price | 72.81 | 100.09 | +37.47% |
| Stablecoin supply | 16,197,749,831.00 | 16,099,204,296.00 | -0.61% |
| 24h DEX volume | 1,636,927,091.91 | 2,327,024,999.32 | +42.16% |
| 24h chain fees | 7,777,648.77 | 11,210,281.15 | +44.13% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
