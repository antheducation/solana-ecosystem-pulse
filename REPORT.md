# Solana Ecosystem Pulse

**Generated:** 2026-08-30T10:49:00Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.11 | +1.54% |
| Market cap | $61.49B | rank #7 |
| Total value locked | $5.90B | +0.43% |
| Stablecoin supply | $16.30B | -0.29% |
| DEX volume (24h) | $1.81B | -30.01% |
| Chain fees / REV (24h) | $11.13M | -29.23% |
| Non-vote TPS (1h avg) | 1,087 | peak 3,511 total |
| Active validators | 678 | 19 delinquent |
| Epoch 1025 | 13.98% complete | 371,621 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Delinquent validators is above its recent norm | Current 19.00 sits 6.7 sigma above the median of the last 63 runs (9.00, +111.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average slot time (ms) is below its recent norm | Current 316.20 sits 5.0 sigma below the median of the last 63 runs (413.30, -23.5%). | `zscore` |
| [WARNING] | Active validators is below its recent norm | Current 678.00 sits 3.4 sigma below the median of the last 63 runs (688.00, -1.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,086.6 average over the last 60 minutes; 890.8 in the latest sample.
- **Total TPS:** 3,222.4 average, 3,510.6 peak. Consensus votes account for 66.3% of all transactions.
- **Slot time:** 316.2 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 420,908,162 at absolute slot 442,860,379.
- **Epoch 1025:** slot 60,379 of 432,000 (13.98% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.671% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 287 ms |
| `solana-rpc.publicnode.com` | yes | 145 ms |
| `api.mainnet.solana.com` | yes | 211 ms |

## Validators & stake

- **678 active** validators, **19 delinquent** (2.73% by count, 0.057% by stake).
- **Total stake:** 437,127,890 SOL ($45.95B); stake rate 69.04% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.75% of active stake.
- **Commission:** median 5.0%, mean 12.18%; 247 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,203,741 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,085,807 | 3.682% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,389,824 | 2.836% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,479,512 | 2.628% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,452,658 | 2.164% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,293,056 | 2.127% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,023,631 | 2.065% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,295,972 | 1.670% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,201,762 | 1.648% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,589,845 | 1.508% | 0% |

## Economics

- **SOL:** $105.11 (+1.54% 24h, +12.63% 7d, +43.17% 30d). Market cap $61.49B, 24h volume $2.06B (3.35% of cap). Price source: `coingecko`.
- **TVL:** $5.90B across 338 protocols - rank #2 of 465 chains, 6.70% of all tracked chain TVL. +6.07% over 7d, -55.5% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-0.45% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.81B in 24h, $19.03B over 7d across 120 venues. Volume/TVL turnover 0.307x per day.
- **REV (chain fees):** $11.13M in 24h, $315.47M over 30d. Retained chain revenue $5.16M (46.4% of fees). Annualised fees are 6.61% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,122,074 SOL circulating of 633,173,757 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | +1.1% | +13.3% |
| 2 | Kamino Lend | Lending | $1.25B | +0.9% | +6.0% |
| 3 | Raydium AMM | Dexs | $1.13B | +1.0% | +7.1% |
| 4 | Jupiter Lend | Lending | $1.09B | +0.9% | +2.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | +1.1% | +14.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | +1.4% | +9.4% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $769.19M | +0.5% | +4.5% |
| 9 | Jupiter Staked SOL | Liquid Staking | $541.81M | +0.9% | +11.9% |
| 10 | Marinade Native | Staking Pool | $428.20M | +1.4% | +35.6% |
| 11 | xStocks | RWA | $422.54M | -2.3% | +0.6% |
| 12 | Sentora | Risk Curators | $360.95M | -0.0% | -1.3% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.2% · Lending 15.7% · Dexs 14.2% · RWA 12.3% · Derivatives 5.1% · Staking Pool 3.9%

### Tokenised assets

$2.39B of tokenised real-world assets and equities are locked on Solana - 14.272% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $422.54M
- OnRe (RWA): $284.72M
- Solstice (Basis Trading): $249.90M
- Ondo Yield Assets (RWA): $179.45M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **775.7 unique fee payers** signed per block (1,048 distinct addresses in the union, 55.0% overlap between blocks).

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
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-29T11:51:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,327.43 | 3,222.43 | -3.16% |
| Average non-vote TPS | 1,164.69 | 1,086.62 | -6.70% |
| Average slot time (ms) | 316.90 | 316.20 | -0.22% |
| Active validators | 688.00 | 678.00 | -1.45% |
| Delinquent validators | 9.00 | 19.00 | +111.11% |
| Solana TVL | 5,840,691,031.00 | 5,898,570,612.00 | +0.99% |
| SOL price | 103.63 | 105.11 | +1.43% |
| Stablecoin supply | 16,344,337,520.00 | 16,298,645,275.00 | -0.28% |
| 24h DEX volume | 2,590,586,442.22 | 1,813,163,418.31 | -30.01% |
| 24h chain fees | 15,624,748.43 | 11,130,685.82 | -28.76% |

### Change over 7d (vs run at 2026-08-23T12:14:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,375.74 | 3,222.43 | -4.54% |
| Average non-vote TPS | 1,517.25 | 1,086.62 | -28.38% |
| Average slot time (ms) | 365.10 | 316.20 | -13.39% |
| Active validators | 683.00 | 678.00 | -0.73% |
| Delinquent validators | 12.00 | 19.00 | +58.33% |
| Solana TVL | 5,519,339,285.00 | 5,898,570,612.00 | +6.87% |
| SOL price | 94.24 | 105.11 | +11.53% |
| Stablecoin supply | 16,372,596,016.00 | 16,298,645,275.00 | -0.45% |
| 24h DEX volume | 3,732,294,477.70 | 1,813,163,418.31 | -51.42% |
| 24h chain fees | 11,916,880.26 | 11,130,685.82 | -6.60% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,222.43 | -18.10% |
| Average non-vote TPS | 2,312.46 | 1,086.62 | -53.01% |
| Average slot time (ms) | 424.10 | 316.20 | -25.44% |
| Active validators | 692.00 | 678.00 | -2.02% |
| Delinquent validators | 8.00 | 19.00 | +137.50% |
| Solana TVL | 4,740,035,266.00 | 5,898,570,612.00 | +24.44% |
| SOL price | 72.81 | 105.11 | +44.36% |
| Stablecoin supply | 16,197,749,831.00 | 16,298,645,275.00 | +0.62% |
| 24h DEX volume | 1,636,927,091.91 | 1,813,163,418.31 | +10.77% |
| 24h chain fees | 7,777,648.77 | 11,130,685.82 | +43.11% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
