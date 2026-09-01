# Solana Ecosystem Pulse

**Generated:** 2026-09-01T20:13:48Z · **Schema:** `1.0.0` · **Collection time:** 22.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.96 | -3.59% |
| Market cap | $58.49B | rank #7 |
| Total value locked | $5.74B | -0.87% |
| Stablecoin supply | $15.97B | +0.03% |
| DEX volume (24h) | $2.50B | +29.63% |
| Chain fees / REV (24h) | $13.50M | +9.70% |
| Non-vote TPS (1h avg) | 2,289 | peak 5,291 total |
| Active validators | 677 | 17 delinquent |
| Epoch 1026 | 64.64% complete | 152,763 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Delinquent validators is above its recent norm | Current 17.00 sits 5.4 sigma above the median of the last 64 runs (9.00, +88.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 677.00 sits 3.0 sigma below the median of the last 64 runs (686.00, -1.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,288.5 average over the last 60 minutes; 2,043.2 in the latest sample.
- **Total TPS:** 4,409.2 average, 5,291.1 peak. Consensus votes account for 48.1% of all transactions.
- **Slot time:** 317.9 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 421,558,777 at absolute slot 443,511,237.
- **Epoch 1026:** slot 279,237 of 432,000 (64.64% complete).
- **Client:** agave `4.3.0-beta.2`, feature set `2409014235`. Inflation 3.669% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 103 ms |
| `solana-rpc.publicnode.com` | yes | 160 ms |
| `api.mainnet.solana.com` | yes | 471 ms |

## Validators & stake

- **677 active** validators, **17 delinquent** (2.45% by count, 0.154% by stake).
- **Total stake:** 438,201,819 SOL ($43.80B); stake rate 69.20% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.20% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 244 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,174,436 | 3.925% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,281,426 | 3.721% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,434,730 | 2.842% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,480,709 | 2.624% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,455,250 | 2.161% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,506 | 2.122% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,044,016 | 2.067% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,216,300 | 1.649% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,930,213 | 1.584% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,591,885 | 1.507% | 0% |

## Economics

- **SOL:** $99.96 (-3.59% 24h, +2.08% 7d, +35.73% 30d). Market cap $58.49B, 24h volume $3.27B (5.60% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 337 protocols - rank #2 of 465 chains, 6.71% of all tracked chain TVL. +0.00% over 7d, -56.7% from its ATH.
- **Stablecoins:** $15.97B circulating on Solana (-1.77% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.50B in 24h, $17.68B over 7d across 120 venues. Volume/TVL turnover 0.436x per day.
- **REV (chain fees):** $13.50M in 24h, $328.19M over 30d. Retained chain revenue $5.55M (41.1% of fees). Annualised fees are 8.43% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,206,540 SOL circulating of 633,266,971 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.54B | -3.3% | +1.3% |
| 2 | Kamino Lend | Lending | $1.23B | -2.4% | +1.7% |
| 3 | Raydium AMM | Dexs | $1.10B | -0.9% | -0.4% |
| 4 | Jupiter Lend | Lending | $1.07B | -0.9% | -1.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | -2.8% | +4.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.02B | -3.1% | +3.1% |
| 7 | BlackRock BUIDL | RWA | $887.01M | +0.0% | +7.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $743.40M | -3.3% | -2.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $523.74M | -3.1% | +2.9% |
| 10 | xStocks | RWA | $433.51M | -1.7% | +2.9% |
| 11 | Marinade Native | Staking Pool | $403.80M | -5.9% | +9.4% |
| 12 | Sentora | Risk Curators | $361.88M | +0.3% | -0.5% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.35B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.8% · Lending 15.7% · Dexs 14.1% · RWA 12.7% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.690% of chain TVL.

- BlackRock BUIDL (RWA): $887.01M
- xStocks (RWA): $433.51M
- OnRe (RWA): $287.71M
- Solstice (Basis Trading): $249.89M
- Ondo Yield Assets (RWA): $179.86M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **872.3 unique fee payers** signed per block (1,208 distinct addresses in the union, 53.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-01
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-31
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27

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

### Change over 24h (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 4,409.25 | +1.86% |
| Average non-vote TPS | 2,195.90 | 2,288.53 | +4.22% |
| Average slot time (ms) | 317.20 | 317.90 | +0.22% |
| Active validators | 681.00 | 677.00 | -0.59% |
| Delinquent validators | 16.00 | 17.00 | +6.25% |
| Solana TVL | 5,791,254,029.00 | 5,737,476,214.00 | -0.93% |
| SOL price | 104.61 | 99.96 | -4.45% |
| Stablecoin supply | 16,123,089,134.00 | 15,969,999,346.00 | -0.95% |
| 24h DEX volume | 1,929,632,644.74 | 2,501,465,620.05 | +29.63% |
| 24h chain fees | 12,307,328.44 | 13,501,461.08 | +9.70% |

### Change over 7d (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 4,409.25 | -3.42% |
| Average non-vote TPS | 2,708.19 | 2,288.53 | -15.50% |
| Average slot time (ms) | 366.20 | 317.90 | -13.19% |
| Active validators | 685.00 | 677.00 | -1.17% |
| Delinquent validators | 10.00 | 17.00 | +70.00% |
| Solana TVL | 5,634,312,506.00 | 5,737,476,214.00 | +1.83% |
| SOL price | 98.47 | 99.96 | +1.51% |
| Stablecoin supply | 16,426,872,816.00 | 15,969,999,346.00 | -2.78% |
| 24h DEX volume | 2,996,141,158.64 | 2,501,465,620.05 | -16.51% |
| 24h chain fees | 14,491,360.16 | 13,501,461.08 | -6.83% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,409.25 | +12.06% |
| Average non-vote TPS | 2,312.46 | 2,288.53 | -1.03% |
| Average slot time (ms) | 424.10 | 317.90 | -25.04% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 17.00 | +112.50% |
| Solana TVL | 4,740,035,266.00 | 5,737,476,214.00 | +21.04% |
| SOL price | 72.81 | 99.96 | +37.29% |
| Stablecoin supply | 16,197,749,831.00 | 15,969,999,346.00 | -1.41% |
| 24h DEX volume | 1,636,927,091.91 | 2,501,465,620.05 | +52.81% |
| 24h chain fees | 7,777,648.77 | 13,501,461.08 | +73.59% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
