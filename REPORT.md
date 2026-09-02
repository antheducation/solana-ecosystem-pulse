# Solana Ecosystem Pulse

**Generated:** 2026-09-02T01:39:46Z · **Schema:** `1.0.0` · **Collection time:** 11.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.33 | -3.66% |
| Market cap | $58.13B | rank #7 |
| Total value locked | $5.66B | -0.82% |
| Stablecoin supply | $15.97B | +0.02% |
| DEX volume (24h) | $2.36B | -5.72% |
| Chain fees / REV (24h) | $14.36M | +6.33% |
| Non-vote TPS (1h avg) | 1,979 | peak 5,551 total |
| Active validators | 678 | 16 delinquent |
| Epoch 1026 | 78.96% complete | 90,908 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,979.1 average over the last 60 minutes; 2,203.8 in the latest sample.
- **Total TPS:** 4,115.6 average, 5,550.8 peak. Consensus votes account for 51.9% of all transactions.
- **Slot time:** 316.2 ms average (target 400 ms), worst 1-minute bucket 333.3 ms.
- **Block height:** 421,620,583 at absolute slot 443,573,092.
- **Epoch 1026:** slot 341,092 of 432,000 (78.96% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.669% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 147 ms |
| `solana-rpc.publicnode.com` | yes | 104 ms |
| `api.mainnet.solana.com` | yes | 43 ms |

## Validators & stake

- **678 active** validators, **16 delinquent** (2.31% by count, 0.039% by stake).
- **Total stake:** 438,201,819 SOL ($43.53B); stake rate 69.20% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.18% and top 33 hold 45.61% of active stake.
- **Commission:** median 5.0%, mean 12.49%; 244 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,174,436 | 3.921% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,281,426 | 3.717% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,434,730 | 2.839% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,480,709 | 2.621% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,455,250 | 2.159% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,506 | 2.120% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,044,016 | 2.065% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,216,300 | 1.647% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,930,213 | 1.582% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,591,885 | 1.505% | 0% |

## Economics

- **SOL:** $99.33 (-3.66% 24h, +2.75% 7d, +35.80% 30d). Market cap $58.13B, 24h volume $3.40B (5.85% of cap). Price source: `coingecko`.
- **TVL:** $5.66B across 338 protocols - rank #2 of 465 chains, 6.64% of all tracked chain TVL. +0.94% over 7d, -57.2% from its ATH.
- **Stablecoins:** $15.97B circulating on Solana (-1.78% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.36B in 24h, $15.91B over 7d across 120 venues. Volume/TVL turnover 0.417x per day.
- **REV (chain fees):** $14.36M in 24h, $323.23M over 30d. Retained chain revenue $5.80M (40.4% of fees). Annualised fees are 9.01% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,206,323 SOL circulating of 633,266,753 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | -3.0% | +4.0% |
| 2 | Kamino Lend | Lending | $1.21B | -13.6% | +2.3% |
| 3 | Raydium AMM | Dexs | $1.08B | -3.0% | +1.9% |
| 4 | Jupiter Lend | Lending | $1.04B | -1.9% | -0.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | -3.0% | +4.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.01B | -2.9% | +4.0% |
| 7 | BlackRock BUIDL | RWA | $887.01M | +0.0% | +1.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $744.53M | -2.4% | -0.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $517.69M | -3.1% | +3.4% |
| 10 | xStocks | RWA | $431.96M | -2.2% | +0.9% |
| 11 | Marinade Native | Staking Pool | $399.16M | -5.8% | +5.6% |
| 12 | Sentora | Risk Curators | $362.57M | +0.5% | -0.2% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.21B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.7% · Lending 15.6% · Dexs 14.1% · RWA 12.8% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.809% of chain TVL.

- BlackRock BUIDL (RWA): $887.01M
- xStocks (RWA): $431.96M
- OnRe (RWA): $287.93M
- Solstice (Basis Trading): $249.87M
- Ondo Yield Assets (RWA): $179.34M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **984.0 unique fee payers** signed per block (1,449 distinct addresses in the union, 50.9% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-01T02:18:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,129.22 | 4,115.59 | -0.33% |
| Average non-vote TPS | 2,000.29 | 1,979.08 | -1.06% |
| Average slot time (ms) | 318.50 | 316.20 | -0.72% |
| Active validators | 680.00 | 678.00 | -0.29% |
| Delinquent validators | 14.00 | 16.00 | +14.29% |
| Solana TVL | 5,962,784,320.00 | 5,658,999,019.00 | -5.09% |
| SOL price | 103.02 | 99.33 | -3.58% |
| Stablecoin supply | 16,123,159,936.00 | 15,968,502,758.00 | -0.96% |
| 24h DEX volume | 2,457,773,259.05 | 2,358,272,391.49 | -4.05% |
| 24h chain fees | 13,276,210.28 | 14,355,983.93 | +8.13% |

### Change over 7d (vs run at 2026-08-26T00:33:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,173.87 | 4,115.59 | -1.40% |
| Average non-vote TPS | 2,307.21 | 1,979.08 | -14.22% |
| Average slot time (ms) | 365.30 | 316.20 | -13.44% |
| Active validators | 686.00 | 678.00 | -1.17% |
| Delinquent validators | 9.00 | 16.00 | +77.78% |
| Solana TVL | 5,601,977,591.00 | 5,658,999,019.00 | +1.02% |
| SOL price | 96.63 | 99.33 | +2.79% |
| Stablecoin supply | 16,424,674,081.00 | 15,968,502,758.00 | -2.78% |
| 24h DEX volume | 3,042,423,812.64 | 2,358,272,391.49 | -22.49% |
| 24h chain fees | 14,624,031.61 | 14,355,983.93 | -1.83% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,115.59 | +4.60% |
| Average non-vote TPS | 2,312.46 | 1,979.08 | -14.42% |
| Average slot time (ms) | 424.10 | 316.20 | -25.44% |
| Active validators | 692.00 | 678.00 | -2.02% |
| Delinquent validators | 8.00 | 16.00 | +100.00% |
| Solana TVL | 4,740,035,266.00 | 5,658,999,019.00 | +19.39% |
| SOL price | 72.81 | 99.33 | +36.42% |
| Stablecoin supply | 16,197,749,831.00 | 15,968,502,758.00 | -1.42% |
| 24h DEX volume | 1,636,927,091.91 | 2,358,272,391.49 | +44.07% |
| 24h chain fees | 7,777,648.77 | 14,355,983.93 | +84.58% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 11.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
