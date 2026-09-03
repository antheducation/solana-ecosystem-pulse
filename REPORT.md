# Solana Ecosystem Pulse

**Generated:** 2026-09-03T15:21:29Z · **Schema:** `1.0.0` · **Collection time:** 26.9s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.35 | +5.50% |
| Market cap | $61.07B | rank #7 |
| Total value locked | $5.82B | +2.98% |
| Stablecoin supply | $16.10B | +1.59% |
| DEX volume (24h) | $2.29B | +5.42% |
| Chain fees / REV (24h) | $10.54M | -17.43% |
| Non-vote TPS (1h avg) | 2,451 | peak 5,701 total |
| Active validators | 676 | 19 delinquent |
| Epoch 1027 | 78.74% complete | 91,853 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 66 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 19.00 sits 3.0 sigma above the median of the last 66 runs (10.00, +90.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,450.8 average over the last 60 minutes; 1,965.5 in the latest sample.
- **Total TPS:** 4,565.6 average, 5,701.4 peak. Consensus votes account for 46.3% of all transactions.
- **Slot time:** 316.5 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 422,051,104 at absolute slot 444,004,147.
- **Epoch 1027:** slot 340,147 of 432,000 (78.74% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 167 ms |
| `solana-rpc.publicnode.com` | yes | 116 ms |
| `api.mainnet.solana.com` | yes | 188 ms |

## Validators & stake

- **676 active** validators, **19 delinquent** (2.73% by count, 0.050% by stake).
- **Total stake:** 438,422,357 SOL ($45.75B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.51%; 243 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.959% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,325,737 | 3.726% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,462,274 | 2.844% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,304,498 | 2.580% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,565,273 | 2.183% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,486 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,040,435 | 2.063% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,220,140 | 1.648% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,125,475 | 1.626% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,590,653 | 1.504% | 0% |

## Economics

- **SOL:** $104.35 (+5.50% 24h, -2.24% 7d, +41.45% 30d). Market cap $61.07B, 24h volume $3.69B (6.05% of cap). Price source: `coingecko`.
- **TVL:** $5.82B across 340 protocols - rank #2 of 465 chains, 6.76% of all tracked chain TVL. +0.73% over 7d, -56.1% from its ATH.
- **Stablecoins:** $16.10B circulating on Solana (-0.18% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.29B in 24h, $16.85B over 7d across 121 venues. Volume/TVL turnover 0.394x per day.
- **REV (chain fees):** $10.54M in 24h, $335.65M over 30d. Retained chain revenue $4.05M (38.5% of fees). Annualised fees are 6.30% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,274,754 SOL circulating of 633,360,790 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | +2.3% | +0.9% |
| 2 | Kamino Lend | Lending | $1.30B | +6.7% | +7.6% |
| 3 | Raydium AMM | Dexs | $1.09B | +3.4% | -1.0% |
| 4 | Jupiter Lend | Lending | $1.09B | +2.4% | -0.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | +2.3% | +1.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.02B | +2.3% | +0.9% |
| 7 | BlackRock BUIDL | RWA | $890.69M | +0.4% | +0.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $752.31M | +1.6% | -2.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $524.96M | +2.2% | +0.2% |
| 10 | xStocks | RWA | $438.92M | +1.6% | +2.0% |
| 11 | Marinade Native | Staking Pool | $407.36M | +4.0% | +1.5% |
| 12 | Sentora | Risk Curators | $379.41M | +4.7% | +4.5% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.54B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.5% · Lending 16.1% · Dexs 13.8% · RWA 12.6% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.42B of tokenised real-world assets and equities are locked on Solana - 14.621% of chain TVL.

- BlackRock BUIDL (RWA): $890.69M
- xStocks (RWA): $438.92M
- OnRe (RWA): $295.04M
- Solstice (Basis Trading): $249.87M
- Ondo Yield Assets (RWA): $179.48M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **906.3 unique fee payers** signed per block (1,282 distinct addresses in the union, 52.9% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) - Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT

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

### Change over 24h (vs run at 2026-09-02T15:26:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,963.51 | 4,565.55 | +15.19% |
| Average non-vote TPS | 1,822.14 | 2,450.75 | +34.50% |
| Average slot time (ms) | 314.80 | 316.50 | +0.54% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 18.00 | 19.00 | +5.56% |
| Solana TVL | 5,622,784,841.00 | 5,816,129,783.00 | +3.44% |
| SOL price | 98.97 | 104.35 | +5.44% |
| Stablecoin supply | 15,849,987,390.00 | 16,104,456,527.00 | +1.61% |
| 24h DEX volume | 2,171,560,050.49 | 2,289,285,889.32 | +5.42% |
| 24h chain fees | 12,641,815.67 | 10,535,900.15 | -16.66% |

### Change over 7d (vs run at 2026-08-27T16:57:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,739.80 | 4,565.55 | -3.68% |
| Average non-vote TPS | 2,877.86 | 2,450.75 | -14.84% |
| Average slot time (ms) | 367.20 | 316.50 | -13.81% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 12.00 | 19.00 | +58.33% |
| Solana TVL | 5,971,320,873.00 | 5,816,129,783.00 | -2.60% |
| SOL price | 109.05 | 104.35 | -4.31% |
| Stablecoin supply | 16,295,559,951.00 | 16,104,456,527.00 | -1.17% |
| 24h DEX volume | 2,351,677,355.00 | 2,289,285,889.32 | -2.65% |
| 24h chain fees | 15,169,688.78 | 10,535,900.15 | -30.55% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,565.55 | +16.04% |
| Average non-vote TPS | 2,312.46 | 2,450.75 | +5.98% |
| Average slot time (ms) | 424.10 | 316.50 | -25.37% |
| Active validators | 692.00 | 676.00 | -2.31% |
| Delinquent validators | 8.00 | 19.00 | +137.50% |
| Solana TVL | 4,740,035,266.00 | 5,816,129,783.00 | +22.70% |
| SOL price | 72.81 | 104.35 | +43.32% |
| Stablecoin supply | 16,197,749,831.00 | 16,104,456,527.00 | -0.58% |
| 24h DEX volume | 1,636,927,091.91 | 2,289,285,889.32 | +39.85% |
| 24h chain fees | 7,777,648.77 | 10,535,900.15 | +35.46% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 26.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
