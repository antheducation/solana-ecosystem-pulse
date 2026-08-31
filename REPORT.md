# Solana Ecosystem Pulse

**Generated:** 2026-08-31T18:43:33Z · **Schema:** `1.0.0` · **Collection time:** 14.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.61 | -2.00% |
| Market cap | $61.22B | rank #7 |
| Total value locked | $5.79B | -2.03% |
| Stablecoin supply | $16.12B | -1.07% |
| DEX volume (24h) | $1.93B | +15.50% |
| Chain fees / REV (24h) | $12.31M | +9.75% |
| Non-vote TPS (1h avg) | 2,196 | peak 5,161 total |
| Active validators | 681 | 16 delinquent |
| Epoch 1025 | 97.74% complete | 9,747 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 16.00 sits 4.7 sigma above the median of the last 64 runs (9.00, +77.8%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,195.9 average over the last 60 minutes; 2,766.8 in the latest sample.
- **Total TPS:** 4,328.5 average, 5,161.0 peak. Consensus votes account for 49.3% of all transactions.
- **Slot time:** 317.2 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 421,269,902 at absolute slot 443,222,253.
- **Epoch 1025:** slot 422,253 of 432,000 (97.74% complete).
- **Client:** agave `4.3.0-beta.2`, feature set `2409014235`. Inflation 3.671% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 137 ms |
| `solana-rpc.publicnode.com` | yes | 182 ms |
| `api.mainnet.solana.com` | yes | 150 ms |

## Validators & stake

- **681 active** validators, **16 delinquent** (2.30% by count, 0.005% by stake).
- **Total stake:** 437,127,890 SOL ($45.73B); stake rate 69.04% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.73% of active stake.
- **Commission:** median 5.0%, mean 12.43%; 247 validators at 0% and 63 at 100%.

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

- **SOL:** $104.61 (-2.00% 24h, +9.69% 7d, +45.60% 30d). Market cap $61.22B, 24h volume $3.77B (6.17% of cap). Price source: `coingecko`.
- **TVL:** $5.79B across 336 protocols - rank #2 of 465 chains, 6.59% of all tracked chain TVL. +4.13% over 7d, -56.2% from its ATH.
- **Stablecoins:** $16.12B circulating on Solana (-2.01% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.93B in 24h, $18.17B over 7d across 120 venues. Volume/TVL turnover 0.333x per day.
- **REV (chain fees):** $12.31M in 24h, $320.46M over 30d. Retained chain revenue $5.46M (44.3% of fees). Annualised fees are 7.34% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,120,760 SOL circulating of 633,172,538 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.57B | -3.4% | +10.6% |
| 2 | Kamino Lend | Lending | $1.25B | -1.6% | +4.5% |
| 3 | Raydium AMM | Dexs | $1.10B | -3.8% | +6.4% |
| 4 | Jupiter Lend | Lending | $1.07B | -3.4% | +0.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -3.1% | +9.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -3.4% | +8.1% |
| 7 | BlackRock BUIDL | RWA | $886.79M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $761.28M | -2.4% | +2.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $532.47M | -3.4% | +8.8% |
| 10 | xStocks | RWA | $437.24M | -0.2% | +3.9% |
| 11 | Marinade Native | Staking Pool | $422.50M | -3.4% | +24.9% |
| 12 | Sentora | Risk Curators | $360.92M | +0.1% | -1.4% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.54B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.0% · Lending 15.7% · Dexs 14.0% · RWA 12.6% · Derivatives 5.1% · Staking Pool 3.9%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.547% of chain TVL.

- BlackRock BUIDL (RWA): $886.79M
- xStocks (RWA): $437.24M
- OnRe (RWA): $284.91M
- Solstice (Basis Trading): $249.83M
- Ondo Yield Assets (RWA): $179.39M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **928.7 unique fee payers** signed per block (1,345 distinct addresses in the union, 51.7% overlap between blocks).

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

- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
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

### Change over 24h (vs run at 2026-08-30T20:10:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,293.13 | 4,328.53 | +0.82% |
| Average non-vote TPS | 2,167.90 | 2,195.90 | +1.29% |
| Average slot time (ms) | 318.30 | 317.20 | -0.35% |
| Active validators | 680.00 | 681.00 | +0.15% |
| Delinquent validators | 17.00 | 16.00 | -5.88% |
| Solana TVL | 5,956,176,022.00 | 5,791,254,029.00 | -2.77% |
| SOL price | 105.77 | 104.61 | -1.10% |
| Stablecoin supply | 16,297,776,213.00 | 16,123,089,134.00 | -1.07% |
| 24h DEX volume | 1,670,710,752.31 | 1,929,632,644.74 | +15.50% |
| 24h chain fees | 11,213,986.82 | 12,307,328.44 | +9.75% |

### Change over 7d (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,328.53 | -5.25% |
| Average non-vote TPS | 2,714.40 | 2,195.90 | -19.10% |
| Average slot time (ms) | 367.20 | 317.20 | -13.62% |
| Active validators | 685.00 | 681.00 | -0.58% |
| Delinquent validators | 10.00 | 16.00 | +60.00% |
| Solana TVL | 5,621,355,422.00 | 5,791,254,029.00 | +3.02% |
| SOL price | 96.29 | 104.61 | +8.64% |
| Stablecoin supply | 16,453,918,497.00 | 16,123,089,134.00 | -2.01% |
| 24h DEX volume | 2,938,613,605.25 | 1,929,632,644.74 | -34.34% |
| 24h chain fees | 12,654,048.70 | 12,307,328.44 | -2.74% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,328.53 | +10.01% |
| Average non-vote TPS | 2,312.46 | 2,195.90 | -5.04% |
| Average slot time (ms) | 424.10 | 317.20 | -25.21% |
| Active validators | 692.00 | 681.00 | -1.59% |
| Delinquent validators | 8.00 | 16.00 | +100.00% |
| Solana TVL | 4,740,035,266.00 | 5,791,254,029.00 | +22.18% |
| SOL price | 72.81 | 104.61 | +43.68% |
| Stablecoin supply | 16,197,749,831.00 | 16,123,089,134.00 | -0.46% |
| 24h DEX volume | 1,636,927,091.91 | 1,929,632,644.74 | +17.88% |
| 24h chain fees | 7,777,648.77 | 12,307,328.44 | +58.24% |

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
