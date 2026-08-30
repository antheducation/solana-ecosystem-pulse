# Solana Ecosystem Pulse

**Generated:** 2026-08-30T20:10:22Z · **Schema:** `1.0.0` · **Collection time:** 17.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.77 | +0.36% |
| Market cap | $61.88B | rank #7 |
| Total value locked | $5.96B | +1.47% |
| Stablecoin supply | $16.30B | -0.29% |
| DEX volume (24h) | $1.67B | -35.51% |
| Chain fees / REV (24h) | $11.21M | -28.70% |
| Non-vote TPS (1h avg) | 2,168 | peak 5,697 total |
| Active validators | 680 | 17 delinquent |
| Epoch 1025 | 38.55% complete | 265,445 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Delinquent validators is above its recent norm | Current 17.00 sits 5.4 sigma above the median of the last 63 runs (9.00, +88.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,167.9 average over the last 60 minutes; 2,528.3 in the latest sample.
- **Total TPS:** 4,293.1 average, 5,697.5 peak. Consensus votes account for 49.5% of all transactions.
- **Slot time:** 318.3 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 421,014,311 at absolute slot 442,966,555.
- **Epoch 1025:** slot 166,555 of 432,000 (38.55% complete).
- **Client:** agave `4.3.0-beta.2`, feature set `2409014235`. Inflation 3.671% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 243 ms |
| `solana-rpc.publicnode.com` | yes | 178 ms |
| `api.mainnet.solana.com` | yes | 124 ms |

## Validators & stake

- **680 active** validators, **17 delinquent** (2.44% by count, 0.005% by stake).
- **Total stake:** 437,127,890 SOL ($46.24B); stake rate 69.04% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.73% of active stake.
- **Commission:** median 5.0%, mean 12.15%; 249 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,203,741 | 3.936% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,085,807 | 3.680% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,389,824 | 2.835% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,479,512 | 2.626% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,452,658 | 2.163% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,293,056 | 2.126% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,023,631 | 2.064% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,295,972 | 1.669% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,201,762 | 1.648% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,589,845 | 1.508% | 0% |

## Economics

- **SOL:** $105.77 (+0.36% 24h, +11.27% 7d, +44.71% 30d). Market cap $61.88B, 24h volume $2.40B (3.88% of cap). Price source: `coingecko`.
- **TVL:** $5.96B across 336 protocols - rank #2 of 465 chains, 6.70% of all tracked chain TVL. +7.17% over 7d, -55.0% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-0.46% 7d) - $2.74 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.67B in 24h, $19.18B over 7d across 120 venues. Volume/TVL turnover 0.281x per day.
- **REV (chain fees):** $11.21M in 24h, $316.37M over 30d. Retained chain revenue $5.06M (45.1% of fees). Annualised fees are 6.61% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,121,724 SOL circulating of 633,173,407 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.63B | +1.5% | +15.5% |
| 2 | Kamino Lend | Lending | $1.27B | +1.1% | +7.1% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.6% | +8.7% |
| 4 | Jupiter Lend | Lending | $1.10B | +0.8% | +3.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.10B | +1.6% | +16.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.07B | +1.6% | +11.3% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $779.81M | +1.1% | +5.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $552.10M | +1.3% | +14.1% |
| 10 | Marinade Native | Staking Pool | $437.97M | +2.2% | +38.7% |
| 11 | xStocks | RWA | $437.34M | +0.9% | +4.1% |
| 12 | Sentora | Risk Curators | $360.68M | -0.1% | -1.4% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.96B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.4% · Lending 15.7% · Dexs 14.2% · RWA 12.2% · Derivatives 5.1% · Staking Pool 3.9%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.187% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $437.34M
- OnRe (RWA): $284.80M
- Solstice (Basis Trading): $249.90M
- Ondo Yield Assets (RWA): $179.85M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **915.3 unique fee payers** signed per block (1,271 distinct addresses in the union, 53.7% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-29T20:04:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,144.50 | 4,293.13 | +3.59% |
| Average non-vote TPS | 1,989.40 | 2,167.90 | +8.97% |
| Average slot time (ms) | 318.30 | 318.30 | +0.00% |
| Active validators | 689.00 | 680.00 | -1.31% |
| Delinquent validators | 8.00 | 17.00 | +112.50% |
| Solana TVL | 5,896,456,733.00 | 5,956,176,022.00 | +1.01% |
| SOL price | 105.39 | 105.77 | +0.36% |
| Stablecoin supply | 16,345,994,847.00 | 16,297,776,213.00 | -0.29% |
| 24h DEX volume | 2,590,586,442.22 | 1,670,710,752.31 | -35.51% |
| 24h chain fees | 15,728,868.43 | 11,213,986.82 | -28.70% |

### Change over 7d (vs run at 2026-08-23T18:11:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,174.50 | 4,293.13 | +2.84% |
| Average non-vote TPS | 2,325.35 | 2,167.90 | -6.77% |
| Average slot time (ms) | 365.10 | 318.30 | -12.82% |
| Active validators | 681.00 | 680.00 | -0.15% |
| Delinquent validators | 14.00 | 17.00 | +21.43% |
| Solana TVL | 5,593,098,038.00 | 5,956,176,022.00 | +6.49% |
| SOL price | 94.99 | 105.77 | +11.35% |
| Stablecoin supply | 16,372,086,266.00 | 16,297,776,213.00 | -0.45% |
| 24h DEX volume | 3,732,294,477.70 | 1,670,710,752.31 | -55.24% |
| 24h chain fees | 12,017,709.26 | 11,213,986.82 | -6.69% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,293.13 | +9.11% |
| Average non-vote TPS | 2,312.46 | 2,167.90 | -6.25% |
| Average slot time (ms) | 424.10 | 318.30 | -24.95% |
| Active validators | 692.00 | 680.00 | -1.73% |
| Delinquent validators | 8.00 | 17.00 | +112.50% |
| Solana TVL | 4,740,035,266.00 | 5,956,176,022.00 | +25.66% |
| SOL price | 72.81 | 105.77 | +45.27% |
| Stablecoin supply | 16,197,749,831.00 | 16,297,776,213.00 | +0.62% |
| 24h DEX volume | 1,636,927,091.91 | 1,670,710,752.31 | +2.06% |
| 24h chain fees | 7,777,648.77 | 11,213,986.82 | +44.18% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
