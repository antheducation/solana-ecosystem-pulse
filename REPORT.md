# Solana Ecosystem Pulse

**Generated:** 2026-08-26T00:33:01Z · **Schema:** `1.0.0` · **Collection time:** 17.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.63 | -3.12% |
| Market cap | $56.37B | rank #7 |
| Total value locked | $5.60B | +0.73% |
| Stablecoin supply | $16.42B | -0.18% |
| DEX volume (24h) | $3.04B | +1.54% |
| Chain fees / REV (24h) | $14.62M | +0.92% |
| Non-vote TPS (1h avg) | 2,307 | peak 4,974 total |
| Active validators | 686 | 9 delinquent |
| Epoch 1022 | 56.77% complete | 186,772 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.30 sits 16.9 sigma below the median of the last 63 runs (415.30, -12.0%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,601,977,591.00 sits 8.9 sigma above the median of the last 63 runs (4,855,182,857.00, +15.4%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 96.63 sits 11.4 sigma above the median of the last 63 runs (76.37, +26.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,307.2 average over the last 60 minutes; 2,145.3 in the latest sample.
- **Total TPS:** 4,173.9 average, 4,974.4 peak. Consensus votes account for 44.7% of all transactions.
- **Slot time:** 365.3 ms average (target 400 ms), worst 1-minute bucket 377.4 ms.
- **Block height:** 419,797,793 at absolute slot 441,749,228.
- **Epoch 1022:** slot 245,228 of 432,000 (56.77% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 414 ms |
| `solana-rpc.publicnode.com` | yes | 103 ms |
| `api.mainnet.solana.com` | yes | 211 ms |

## Validators & stake

- **686 active** validators, **9 delinquent** (1.29% by count, 0.045% by stake).
- **Total stake:** 435,118,104 SOL ($42.05B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.17%; 256 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.687% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.699% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.116% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.052% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.973% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.678% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.512% | 0% |

## Economics

- **SOL:** $96.63 (-3.12% 24h, +25.50% 7d, +26.14% 30d). Market cap $56.37B, 24h volume $5.54B (9.82% of cap). Price source: `coingecko`.
- **TVL:** $5.60B across 331 protocols - rank #2 of 465 chains, 6.38% of all tracked chain TVL. +15.51% over 7d, -57.7% from its ATH.
- **Stablecoins:** $16.42B circulating on Solana (+2.79% 7d) - $2.93 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.04B in 24h, $19.98B over 7d across 119 venues. Volume/TVL turnover 0.543x per day.
- **REV (chain fees):** $14.62M in 24h, $280.32M over 30d. Retained chain revenue $5.85M (40.0% of fees). Annualised fees are 9.47% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,375,554 SOL circulating of 632,859,414 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -0.1% | +28.8% |
| 2 | Kamino Lend | Lending | $1.18B | -1.7% | +10.8% |
| 3 | Jupiter Lend | Lending | $1.06B | -1.2% | +10.9% |
| 4 | Raydium AMM | Dexs | $1.06B | -1.1% | +23.8% |
| 5 | Binance Staked SOL | Liquid Staking | $999.33M | +0.9% | +28.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $978.08M | +0.2% | +27.0% |
| 7 | BlackRock BUIDL | RWA | $876.38M | +5.8% | +18.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $751.62M | -0.7% | +9.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $505.01M | +0.3% | +26.6% |
| 10 | xStocks | RWA | $430.26M | +2.0% | +12.8% |
| 11 | Marinade Native | Staking Pool | $380.02M | +5.8% | +78.1% |
| 12 | Sentora | Risk Curators | $363.03M | -0.2% | -0.9% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 331 protocols the total is $15.86B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.8% · Lending 15.8% · Dexs 14.0% · RWA 13.0% · Derivatives 5.3% · Staking Pool 3.7%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.380% of chain TVL.

- BlackRock BUIDL (RWA): $876.38M
- xStocks (RWA): $430.26M
- Solstice (Basis Trading): $302.99M
- OnRe (RWA): $277.20M
- Ondo Yield Assets (RWA): $178.40M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **975.7 unique fee payers** signed per block (1,358 distinct addresses in the union, 53.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-25
- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-25
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-25
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-24

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

### Change over 24h (vs run at 2026-08-25T00:31:55Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,191.70 | 4,173.87 | -0.43% |
| Average non-vote TPS | 2,343.72 | 2,307.21 | -1.56% |
| Average slot time (ms) | 366.70 | 365.30 | -0.38% |
| Active validators | 686.00 | 686.00 | +0.00% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 5,650,096,546.00 | 5,601,977,591.00 | -0.85% |
| SOL price | 99.62 | 96.63 | -3.00% |
| Stablecoin supply | 16,454,057,808.00 | 16,424,674,081.00 | -0.18% |
| 24h DEX volume | 3,004,603,140.25 | 3,042,423,812.64 | +1.26% |
| 24h chain fees | 12,733,845.33 | 14,624,031.61 | +14.84% |

### Change over 7d (vs run at 2026-08-19T00:30:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,748.83 | 4,173.87 | +11.34% |
| Average non-vote TPS | 2,104.87 | 2,307.21 | +9.61% |
| Average slot time (ms) | 416.70 | 365.30 | -12.34% |
| Active validators | 689.00 | 686.00 | -0.44% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 4,899,420,258.00 | 5,601,977,591.00 | +14.34% |
| SOL price | 76.89 | 96.63 | +25.67% |
| Stablecoin supply | 15,978,264,279.00 | 16,424,674,081.00 | +2.79% |
| 24h DEX volume | 1,456,594,741.93 | 3,042,423,812.64 | +108.87% |
| 24h chain fees | 10,986,421.95 | 14,624,031.61 | +33.11% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,173.87 | +6.08% |
| Average non-vote TPS | 2,312.46 | 2,307.21 | -0.23% |
| Average slot time (ms) | 424.10 | 365.30 | -13.86% |
| Active validators | 692.00 | 686.00 | -0.87% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 4,740,035,266.00 | 5,601,977,591.00 | +18.18% |
| SOL price | 72.81 | 96.63 | +32.72% |
| Stablecoin supply | 16,197,749,831.00 | 16,424,674,081.00 | +1.40% |
| 24h DEX volume | 1,636,927,091.91 | 3,042,423,812.64 | +85.86% |
| 24h chain fees | 7,777,648.77 | 14,624,031.61 | +88.03% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
