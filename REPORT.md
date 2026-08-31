# Solana Ecosystem Pulse

**Generated:** 2026-08-31T11:58:30Z · **Schema:** `1.0.0` · **Collection time:** 14.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.35 | -1.59% |
| Market cap | $60.48B | rank #7 |
| Total value locked | $5.82B | -1.57% |
| Stablecoin supply | $16.12B | -1.08% |
| DEX volume (24h) | $1.93B | +15.50% |
| Chain fees / REV (24h) | $12.19M | +8.73% |
| Non-vote TPS (1h avg) | 1,318 | peak 3,850 total |
| Active validators | 678 | 19 delinquent |
| Epoch 1025 | 80.03% complete | 86,262 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Delinquent validators is above its recent norm | Current 19.00 sits 6.7 sigma above the median of the last 64 runs (9.00, +111.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 678.00 sits 3.0 sigma below the median of the last 64 runs (687.00, -1.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,317.6 average over the last 60 minutes; 1,489.6 in the latest sample.
- **Total TPS:** 3,455.8 average, 3,849.5 peak. Consensus votes account for 61.9% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 421,193,412 at absolute slot 443,145,738.
- **Epoch 1025:** slot 345,738 of 432,000 (80.03% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.671% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 123 ms |
| `solana-rpc.publicnode.com` | yes | 153 ms |
| `api.mainnet.solana.com` | yes | 106 ms |

## Validators & stake

- **678 active** validators, **19 delinquent** (2.73% by count, 0.031% by stake).
- **Total stake:** 437,127,890 SOL ($45.18B); stake rate 69.04% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.26% and top 33 hold 45.74% of active stake.
- **Commission:** median 5.0%, mean 12.48%; 245 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,203,741 | 3.937% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,085,807 | 3.681% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,389,824 | 2.835% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,479,512 | 2.627% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,452,658 | 2.163% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,293,056 | 2.127% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,023,631 | 2.065% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,295,972 | 1.670% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,201,762 | 1.648% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,589,845 | 1.508% | 0% |

## Economics

- **SOL:** $103.35 (-1.59% 24h, +9.16% 7d, +42.01% 30d). Market cap $60.48B, 24h volume $3.82B (6.31% of cap). Price source: `coingecko`.
- **TVL:** $5.82B across 337 protocols - rank #2 of 465 chains, 6.63% of all tracked chain TVL. +4.62% over 7d, -56.0% from its ATH.
- **Stablecoins:** $16.12B circulating on Solana (-2.02% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.93B in 24h, $18.17B over 7d across 120 venues. Volume/TVL turnover 0.332x per day.
- **REV (chain fees):** $12.19M in 24h, $320.35M over 30d. Retained chain revenue $5.45M (44.7% of fees). Annualised fees are 7.36% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,121,135 SOL circulating of 633,172,819 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.57B | -1.9% | +11.0% |
| 2 | Kamino Lend | Lending | $1.25B | -0.5% | +4.5% |
| 3 | Raydium AMM | Dexs | $1.11B | -1.5% | +6.9% |
| 4 | Jupiter Lend | Lending | $1.08B | -1.1% | +2.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -1.5% | +10.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | -2.0% | +8.4% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $762.63M | -1.1% | +2.8% |
| 9 | Jupiter Staked SOL | Liquid Staking | $534.42M | -1.6% | +9.2% |
| 10 | xStocks | RWA | $433.01M | +2.5% | +2.9% |
| 11 | Marinade Native | Staking Pool | $424.09M | +1.2% | +25.4% |
| 12 | Sentora | Risk Curators | $360.93M | -0.0% | -1.4% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.57B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.0% · Lending 15.7% · Dexs 14.1% · RWA 12.5% · Derivatives 5.1% · Staking Pool 3.9%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.477% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $433.01M
- OnRe (RWA): $284.89M
- Solstice (Basis Trading): $249.84M
- Ondo Yield Assets (RWA): $179.93M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **904.0 unique fee payers** signed per block (1,249 distinct addresses in the union, 53.9% overlap between blocks).

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

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-30T10:49:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,222.43 | 3,455.79 | +7.24% |
| Average non-vote TPS | 1,086.62 | 1,317.61 | +21.26% |
| Average slot time (ms) | 316.20 | 316.10 | -0.03% |
| Active validators | 678.00 | 678.00 | +0.00% |
| Delinquent validators | 19.00 | 19.00 | +0.00% |
| Solana TVL | 5,898,570,612.00 | 5,818,482,572.00 | -1.36% |
| SOL price | 105.11 | 103.35 | -1.67% |
| Stablecoin supply | 16,298,645,275.00 | 16,121,972,675.00 | -1.08% |
| 24h DEX volume | 1,813,163,418.31 | 1,929,632,644.74 | +6.42% |
| 24h chain fees | 11,130,685.82 | 12,193,230.44 | +9.55% |

### Change over 7d (vs run at 2026-08-24T12:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,845.13 | 3,455.79 | -10.13% |
| Average non-vote TPS | 1,971.73 | 1,317.61 | -33.17% |
| Average slot time (ms) | 363.60 | 316.10 | -13.06% |
| Active validators | 685.00 | 678.00 | -1.02% |
| Delinquent validators | 10.00 | 19.00 | +90.00% |
| Solana TVL | 5,550,065,543.00 | 5,818,482,572.00 | +4.84% |
| SOL price | 94.82 | 103.35 | +9.00% |
| Stablecoin supply | 16,453,541,490.00 | 16,121,972,675.00 | -2.02% |
| 24h DEX volume | 2,938,613,605.25 | 1,929,632,644.74 | -34.34% |
| 24h chain fees | 12,561,642.70 | 12,193,230.44 | -2.93% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,455.79 | -12.17% |
| Average non-vote TPS | 2,312.46 | 1,317.61 | -43.02% |
| Average slot time (ms) | 424.10 | 316.10 | -25.47% |
| Active validators | 692.00 | 678.00 | -2.02% |
| Delinquent validators | 8.00 | 19.00 | +137.50% |
| Solana TVL | 4,740,035,266.00 | 5,818,482,572.00 | +22.75% |
| SOL price | 72.81 | 103.35 | +41.94% |
| Stablecoin supply | 16,197,749,831.00 | 16,121,972,675.00 | -0.47% |
| 24h DEX volume | 1,636,927,091.91 | 1,929,632,644.74 | +17.88% |
| 24h chain fees | 7,777,648.77 | 12,193,230.44 | +56.77% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 14.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
