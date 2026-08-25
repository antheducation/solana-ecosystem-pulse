# Solana Ecosystem Pulse

**Generated:** 2026-08-25T18:20:54Z · **Schema:** `1.0.0` · **Collection time:** 13.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.47 | +2.23% |
| Market cap | $57.44B | rank #7 |
| Total value locked | $5.63B | +1.31% |
| Stablecoin supply | $16.43B | -0.17% |
| DEX volume (24h) | $3.00B | +1.96% |
| Chain fees / REV (24h) | $14.49M | +14.51% |
| Non-vote TPS (1h avg) | 2,708 | peak 5,534 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1022 | 42.62% complete | 247,876 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.20 sits 16.6 sigma below the median of the last 63 runs (415.40, -11.8%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,634,312,506.00 sits 10.6 sigma above the median of the last 63 runs (4,849,572,817.00, +16.2%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 98.47 sits 13.6 sigma above the median of the last 63 runs (76.29, +29.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,708.2 average over the last 60 minutes; 2,754.2 in the latest sample.
- **Total TPS:** 4,565.5 average, 5,534.0 peak. Consensus votes account for 40.7% of all transactions.
- **Slot time:** 366.2 ms average (target 400 ms), worst 1-minute bucket 379.7 ms.
- **Block height:** 419,736,798 at absolute slot 441,688,124.
- **Epoch 1022:** slot 184,124 of 432,000 (42.62% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 99 ms |
| `solana-rpc.publicnode.com` | yes | 73 ms |
| `api.mainnet.solana.com` | yes | 73 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.113% by stake).
- **Total stake:** 435,118,104 SOL ($42.85B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.89% of active stake.
- **Commission:** median 5.0%, mean 12.05%; 256 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.927% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.690% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.823% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.701% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.117% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.053% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.974% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.830% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.680% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.513% | 0% |

## Economics

- **SOL:** $98.47 (+2.23% 24h, +28.04% 7d, +30.75% 30d). Market cap $57.44B, 24h volume $6.36B (11.07% of cap). Price source: `coingecko`.
- **TVL:** $5.63B across 330 protocols - rank #2 of 465 chains, 6.38% of all tracked chain TVL. +16.18% over 7d, -57.4% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+2.81% 7d) - $2.92 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.00B in 24h, $20.88B over 7d across 119 venues. Volume/TVL turnover 0.532x per day.
- **REV (chain fees):** $14.49M in 24h, $284.22M over 30d. Retained chain revenue $5.79M (39.9% of fees). Annualised fees are 9.21% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,375,803 SOL circulating of 632,859,664 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.47B | +1.7% | +29.8% |
| 2 | Kamino Lend | Lending | $1.18B | -1.6% | +11.5% |
| 3 | Raydium AMM | Dexs | $1.08B | +2.8% | +27.7% |
| 4 | Jupiter Lend | Lending | $1.06B | -0.8% | +13.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.01B | +4.0% | +30.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $984.47M | +1.1% | +29.5% |
| 7 | BlackRock BUIDL | RWA | $828.83M | +6.6% | +11.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $756.44M | -0.1% | +10.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $507.89M | +2.2% | +29.0% |
| 10 | xStocks | RWA | $430.29M | +1.1% | +10.5% |
| 11 | Marinade Native | Staking Pool | $384.39M | +7.9% | +78.5% |
| 12 | Sentora | Risk Curators | $363.10M | -0.1% | -1.3% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.87B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.9% · Lending 15.9% · Dexs 14.1% · RWA 12.7% · Derivatives 5.3% · Staking Pool 3.8%

### Tokenised assets

$2.39B of tokenised real-world assets and equities are locked on Solana - 15.083% of chain TVL.

- BlackRock BUIDL (RWA): $828.83M
- xStocks (RWA): $430.29M
- Solstice (Basis Trading): $303.02M
- OnRe (RWA): $276.51M
- Ondo Yield Assets (RWA): $179.30M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,033.0 unique fee payers** signed per block (1,531 distinct addresses in the union, 50.6% overlap between blocks).

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

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-25
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-24
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-24
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-24
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-24

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

### Change over 24h (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,565.46 | -0.06% |
| Average non-vote TPS | 2,714.40 | 2,708.19 | -0.23% |
| Average slot time (ms) | 367.20 | 366.20 | -0.27% |
| Active validators | 685.00 | 685.00 | +0.00% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,621,355,422.00 | 5,634,312,506.00 | +0.23% |
| SOL price | 96.29 | 98.47 | +2.26% |
| Stablecoin supply | 16,453,918,497.00 | 16,426,872,816.00 | -0.16% |
| 24h DEX volume | 2,938,613,605.25 | 2,996,141,158.64 | +1.96% |
| 24h chain fees | 12,654,048.70 | 14,491,360.16 | +14.52% |

### Change over 7d (vs run at 2026-08-18T18:18:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,157.63 | 4,565.46 | +9.81% |
| Average non-vote TPS | 2,510.42 | 2,708.19 | +7.88% |
| Average slot time (ms) | 414.50 | 366.20 | -11.65% |
| Active validators | 688.00 | 685.00 | -0.44% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,885,957,310.00 | 5,634,312,506.00 | +15.32% |
| SOL price | 77.08 | 98.47 | +27.75% |
| Stablecoin supply | 15,977,966,490.00 | 16,426,872,816.00 | +2.81% |
| 24h DEX volume | 1,474,970,358.36 | 2,996,141,158.64 | +103.13% |
| 24h chain fees | 11,189,593.30 | 14,491,360.16 | +29.51% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,565.46 | +16.03% |
| Average non-vote TPS | 2,312.46 | 2,708.19 | +17.11% |
| Average slot time (ms) | 424.10 | 366.20 | -13.65% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 5,634,312,506.00 | +18.87% |
| SOL price | 72.81 | 98.47 | +35.24% |
| Stablecoin supply | 16,197,749,831.00 | 16,426,872,816.00 | +1.41% |
| 24h DEX volume | 1,636,927,091.91 | 2,996,141,158.64 | +83.03% |
| 24h chain fees | 7,777,648.77 | 14,491,360.16 | +86.32% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 13.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
