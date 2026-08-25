# Solana Ecosystem Pulse

**Generated:** 2026-08-25T12:21:53Z · **Schema:** `1.0.0` · **Collection time:** 36.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.21 | +3.38% |
| Market cap | $57.29B | rank #7 |
| Total value locked | $5.74B | +3.29% |
| Stablecoin supply | $16.43B | -0.17% |
| DEX volume (24h) | $3.00B | +1.96% |
| Chain fees / REV (24h) | $14.39M | +13.73% |
| Non-vote TPS (1h avg) | 1,760 | peak 4,333 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1022 | 29.02% complete | 306,622 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 364.50 sits 15.0 sigma below the median of the last 63 runs (415.70, -12.3%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,744,421,267.00 sits 12.4 sigma above the median of the last 63 runs (4,848,739,935.00, +18.5%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 98.21 sits 14.1 sigma above the median of the last 63 runs (76.25, +28.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,760.3 average over the last 60 minutes; 2,053.9 in the latest sample.
- **Total TPS:** 3,629.3 average, 4,333.2 peak. Consensus votes account for 51.5% of all transactions.
- **Slot time:** 364.5 ms average (target 400 ms), worst 1-minute bucket 377.4 ms.
- **Block height:** 419,678,135 at absolute slot 441,629,378.
- **Epoch 1022:** slot 125,378 of 432,000 (29.02% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 705 ms |
| `solana-rpc.publicnode.com` | yes | 115 ms |
| `api.mainnet.solana.com` | yes | 439 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.038% by stake).
- **Total stake:** 435,118,104 SOL ($42.73B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 11.90%; 257 validators at 0% and 60 at 100%.

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

- **SOL:** $98.21 (+3.38% 24h, +28.67% 7d, +31.09% 30d). Market cap $57.29B, 24h volume $7.22B (12.61% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 330 protocols - rank #2 of 465 chains, 6.50% of all tracked chain TVL. +18.45% over 7d, -56.6% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+2.81% 7d) - $2.86 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.00B in 24h, $20.88B over 7d across 119 venues. Volume/TVL turnover 0.522x per day.
- **REV (chain fees):** $14.39M in 24h, $284.12M over 30d. Retained chain revenue $5.78M (40.2% of fees). Annualised fees are 9.17% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,376,056 SOL circulating of 632,859,917 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.50B | +5.8% | +31.9% |
| 2 | Kamino Lend | Lending | $1.22B | +2.8% | +14.8% |
| 3 | Raydium AMM | Dexs | $1.11B | +7.1% | +31.6% |
| 4 | Jupiter Lend | Lending | $1.08B | +2.5% | +15.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.01B | +5.3% | +31.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $997.52M | +4.8% | +31.2% |
| 7 | BlackRock BUIDL | RWA | $828.75M | +6.6% | +11.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $762.99M | +2.6% | +11.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $514.72M | +5.0% | +30.8% |
| 10 | xStocks | RWA | $422.07M | +0.5% | +8.4% |
| 11 | Solstice | Basis Trading | $403.03M | -0.3% | -20.4% |
| 12 | Marinade Native | Staking Pool | $384.74M | +11.8% | +78.7% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 330 protocols the total is $16.15B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.7% · Lending 16.0% · Dexs 14.1% · RWA 12.4% · Derivatives 5.3% · Staking Pool 3.7%

### Tokenised assets

$2.49B of tokenised real-world assets and equities are locked on Solana - 15.391% of chain TVL.

- BlackRock BUIDL (RWA): $828.75M
- xStocks (RWA): $422.07M
- Solstice (Basis Trading): $403.03M
- OnRe (RWA): $276.22M
- Ondo Yield Assets (RWA): $179.26M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **985.3 unique fee payers** signed per block (1,460 distinct addresses in the union, 50.6% overlap between blocks).

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

- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-24
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-24
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-24
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
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

### Change over 24h (vs run at 2026-08-24T12:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,845.13 | 3,629.28 | -5.61% |
| Average non-vote TPS | 1,971.73 | 1,760.33 | -10.72% |
| Average slot time (ms) | 363.60 | 364.50 | +0.25% |
| Active validators | 685.00 | 685.00 | +0.00% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,550,065,543.00 | 5,744,421,267.00 | +3.50% |
| SOL price | 94.82 | 98.21 | +3.58% |
| Stablecoin supply | 16,453,541,490.00 | 16,426,518,373.00 | -0.16% |
| 24h DEX volume | 2,938,613,605.25 | 2,996,141,158.64 | +1.96% |
| 24h chain fees | 12,561,642.70 | 14,392,606.16 | +14.58% |

### Change over 7d (vs run at 2026-08-18T12:19:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,644.56 | 3,629.28 | -0.42% |
| Average non-vote TPS | 1,998.19 | 1,760.33 | -11.90% |
| Average slot time (ms) | 415.20 | 364.50 | -12.21% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 4,855,232,078.00 | 5,744,421,267.00 | +18.31% |
| SOL price | 76.29 | 98.21 | +28.73% |
| Stablecoin supply | 15,976,327,308.00 | 16,426,518,373.00 | +2.82% |
| 24h DEX volume | 1,474,970,358.36 | 2,996,141,158.64 | +103.13% |
| 24h chain fees | 11,105,286.30 | 14,392,606.16 | +29.60% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,629.28 | -7.76% |
| Average non-vote TPS | 2,312.46 | 1,760.33 | -23.88% |
| Average slot time (ms) | 424.10 | 364.50 | -14.05% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 5,744,421,267.00 | +21.19% |
| SOL price | 72.81 | 98.21 | +34.89% |
| Stablecoin supply | 16,197,749,831.00 | 16,426,518,373.00 | +1.41% |
| 24h DEX volume | 1,636,927,091.91 | 2,996,141,158.64 | +83.03% |
| 24h chain fees | 7,777,648.77 | 14,392,606.16 | +85.05% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 36.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
