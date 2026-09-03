# Solana Ecosystem Pulse

**Generated:** 2026-09-03T20:12:53Z · **Schema:** `1.0.0` · **Collection time:** 15.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.35 | +5.66% |
| Market cap | $61.67B | rank #7 |
| Total value locked | $5.97B | +5.46% |
| Stablecoin supply | $16.10B | +1.58% |
| DEX volume (24h) | $2.29B | +5.42% |
| Chain fees / REV (24h) | $10.54M | -17.43% |
| Non-vote TPS (1h avg) | 2,317 | peak 5,241 total |
| Active validators | 676 | 19 delinquent |
| Epoch 1027 | 91.56% complete | 36,478 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 66 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 19.00 sits 3.0 sigma above the median of the last 66 runs (10.00, +90.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,316.6 average over the last 60 minutes; 2,833.2 in the latest sample.
- **Total TPS:** 4,437.7 average, 5,240.6 peak. Consensus votes account for 47.8% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 422,106,238 at absolute slot 444,059,522.
- **Epoch 1027:** slot 395,522 of 432,000 (91.56% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 142 ms |
| `solana-rpc.publicnode.com` | yes | 188 ms |
| `api.mainnet.solana.com` | yes | 94 ms |

## Validators & stake

- **676 active** validators, **19 delinquent** (2.73% by count, 0.050% by stake).
- **Total stake:** 438,422,357 SOL ($46.19B); stake rate 69.22% of total supply.
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

- **SOL:** $105.35 (+5.66% 24h, -3.58% 7d, +42.00% 30d). Market cap $61.67B, 24h volume $4.08B (6.62% of cap). Price source: `coingecko`.
- **TVL:** $5.97B across 341 protocols - rank #2 of 465 chains, 6.77% of all tracked chain TVL. +3.16% over 7d, -55.0% from its ATH.
- **Stablecoins:** $16.10B circulating on Solana (-0.20% 7d) - $2.70 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.29B in 24h, $16.85B over 7d across 121 venues. Volume/TVL turnover 0.383x per day.
- **REV (chain fees):** $10.54M in 24h, $335.65M over 30d. Retained chain revenue $4.05M (38.5% of fees). Annualised fees are 6.24% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,274,560 SOL circulating of 633,360,596 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | +5.5% | +4.4% |
| 2 | Kamino Lend | Lending | $1.34B | +9.2% | +11.0% |
| 3 | Raydium AMM | Dexs | $1.13B | +6.0% | +2.6% |
| 4 | Jupiter Lend | Lending | $1.11B | +4.0% | +1.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | +6.1% | +5.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.07B | +6.3% | +5.0% |
| 7 | BlackRock BUIDL | RWA | $890.78M | +0.0% | +0.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $772.57M | +4.1% | +0.5% |
| 9 | Jupiter Staked SOL | Liquid Staking | $545.84M | +6.1% | +4.2% |
| 10 | xStocks | RWA | $462.50M | +6.7% | +7.5% |
| 11 | Marinade Native | Staking Pool | $422.27M | +6.3% | +5.2% |
| 12 | Sentora | Risk Curators | $383.92M | +6.0% | +5.7% |

The top five protocols hold 37.0% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.97B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.9% · Lending 16.1% · Dexs 13.9% · RWA 12.4% · Derivatives 5.0% · Staking Pool 3.8%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 14.302% of chain TVL.

- BlackRock BUIDL (RWA): $890.78M
- xStocks (RWA): $462.50M
- OnRe (RWA): $295.53M
- Solstice (Basis Trading): $237.91M
- Ondo Yield Assets (RWA): $179.25M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **966.7 unique fee payers** signed per block (1,403 distinct addresses in the union, 51.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) - Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Current Leader Sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-03
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31

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

### Change over 24h (vs run at 2026-09-02T20:11:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,022.99 | 4,437.74 | +10.31% |
| Average non-vote TPS | 1,883.92 | 2,316.58 | +22.97% |
| Average slot time (ms) | 314.50 | 316.10 | +0.51% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 18.00 | 19.00 | +5.56% |
| Solana TVL | 5,665,576,869.00 | 5,969,689,229.00 | +5.37% |
| SOL price | 99.75 | 105.35 | +5.61% |
| Stablecoin supply | 15,850,870,070.00 | 16,102,283,829.00 | +1.59% |
| 24h DEX volume | 2,171,560,050.49 | 2,289,285,889.32 | +5.42% |
| 24h chain fees | 12,646,787.67 | 10,535,900.15 | -16.69% |

### Change over 7d (vs run at 2026-08-27T16:57:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,739.80 | 4,437.74 | -6.37% |
| Average non-vote TPS | 2,877.86 | 2,316.58 | -19.50% |
| Average slot time (ms) | 367.20 | 316.10 | -13.92% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 12.00 | 19.00 | +58.33% |
| Solana TVL | 5,971,320,873.00 | 5,969,689,229.00 | -0.03% |
| SOL price | 109.05 | 105.35 | -3.39% |
| Stablecoin supply | 16,295,559,951.00 | 16,102,283,829.00 | -1.19% |
| 24h DEX volume | 2,351,677,355.00 | 2,289,285,889.32 | -2.65% |
| 24h chain fees | 15,169,688.78 | 10,535,900.15 | -30.55% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,437.74 | +12.79% |
| Average non-vote TPS | 2,312.46 | 2,316.58 | +0.18% |
| Average slot time (ms) | 424.10 | 316.10 | -25.47% |
| Active validators | 692.00 | 676.00 | -2.31% |
| Delinquent validators | 8.00 | 19.00 | +137.50% |
| Solana TVL | 4,740,035,266.00 | 5,969,689,229.00 | +25.94% |
| SOL price | 72.81 | 105.35 | +44.69% |
| Stablecoin supply | 16,197,749,831.00 | 16,102,283,829.00 | -0.59% |
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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
