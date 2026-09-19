# Solana Ecosystem Pulse

**Generated:** 2026-09-19T01:55:43Z · **Schema:** `1.0.0` · **Collection time:** 13.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $113.63 | +10.70% |
| Market cap | $66.73B | rank #7 |
| Total value locked | $6.40B | +0.06% |
| Stablecoin supply | $15.88B | +1.03% |
| DEX volume (24h) | $3.10B | +19.49% |
| Chain fees / REV (24h) | $15.27M | +4.07% |
| Non-vote TPS (1h avg) | 1,894 | peak 5,057 total |
| Active validators | 677 | 11 delinquent |
| Epoch 1037 | 65.02% complete | 151,105 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 86 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 4 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.10 sits 23.3 sigma below the median of the last 86 runs (317.15, -15.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 10.7% in 24h) | SOL price changed +10.7% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,396,701,682.00 sits 4.5 sigma above the median of the last 86 runs (5,850,649,762.00, +9.3%). | `zscore` |
| [WARNING] | SOL price is above its recent norm | Current 113.63 sits 3.2 sigma above the median of the last 86 runs (101.18, +12.3%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,894.4 average over the last 60 minutes; 2,099.1 in the latest sample.
- **Total TPS:** 4,416.0 average, 5,056.7 peak. Consensus votes account for 57.1% of all transactions.
- **Slot time:** 267.1 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 426,305,762 at absolute slot 448,264,895.
- **Epoch 1037:** slot 280,895 of 432,000 (65.02% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.642% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 220 ms |
| `solana-rpc.publicnode.com` | yes | 97 ms |
| `api.mainnet.solana.com` | yes | 170 ms |

## Validators & stake

- **677 active** validators, **11 delinquent** (1.60% by count, 0.036% by stake).
- **Total stake:** 439,612,408 SOL ($49.95B); stake rate 69.31% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.77% of active stake.
- **Commission:** median 5.0%, mean 12.53%; 240 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,815,472 | 4.054% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,816,148 | 3.599% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,510,308 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,398,202 | 2.594% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,784,908 | 2.227% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,526 | 2.106% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,077,527 | 2.066% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,397,869 | 1.683% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,085,578 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,940 | 1.492% | 0% |

## Economics

- **SOL:** $113.63 (+10.70% 24h, +11.51% 7d, +33.82% 30d). Market cap $66.73B, 24h volume $6.75B (10.11% of cap). Price source: `coingecko`.
- **TVL:** $6.40B across 332 protocols - rank #2 of 468 chains, 6.92% of all tracked chain TVL. +8.42% over 7d, -51.7% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (-4.37% 7d) - $2.48 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.10B in 24h, $15.53B over 7d across 124 venues. Volume/TVL turnover 0.484x per day.
- **REV (chain fees):** $15.27M in 24h, $402.14M over 30d. Retained chain revenue $6.10M (39.9% of fees). Annualised fees are 8.35% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,296,623 SOL circulating of 634,297,872 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | +11.7% | +14.9% |
| 2 | Kamino Lend | Lending | $1.52B | +14.2% | +12.9% |
| 3 | Raydium AMM | Dexs | $1.27B | +10.5% | +11.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.17B | +11.5% | +10.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.17B | +11.9% | +11.1% |
| 6 | Jupiter Lend | Lending | $1.14B | +5.1% | +3.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $800.06M | +7.1% | +6.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $586.81M | +11.5% | +10.8% |
| 9 | Marinade Native | Staking Pool | $431.92M | +11.9% | +10.6% |
| 10 | PumpSwap | Dexs | $369.73M | +12.6% | +11.5% |
| 11 | Sentora Curator | Risk Curators | $364.91M | -1.0% | -5.8% |
| 12 | Drift Staked SOL | Liquid Staking | $318.85M | +11.8% | +10.6% |

The top five protocols hold 42.3% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.38B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.1% · Lending 17.9% · Dexs 15.6% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$881.68M of tokenised real-world assets and equities are locked on Solana - 5.383% of chain TVL.

- OnRe (RWA): $303.96M
- Solstice (Basis Trading): $232.45M
- Huma Finance V2 (RWA): $200.76M
- JupUSD (Basis Trading): $46.78M
- Plume Vaults (RWA): $28.12M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | pre-release |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [SIMD-0123: SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16

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

### Change over 24h (vs run at 2026-09-18T01:50:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,099.51 | 4,416.04 | +7.72% |
| Average non-vote TPS | 1,978.66 | 1,894.43 | -4.26% |
| Average slot time (ms) | 316.70 | 267.10 | -15.66% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 14.00 | 11.00 | -21.43% |
| Solana TVL | 5,875,684,850.00 | 6,396,701,682.00 | +8.87% |
| SOL price | 102.31 | 113.63 | +11.06% |
| Stablecoin supply | 15,710,182,138.00 | 15,876,163,466.00 | +1.06% |
| 24h DEX volume | 2,555,388,156.29 | 3,097,318,491.84 | +21.21% |
| 24h chain fees | 13,101,763.60 | 15,267,932.07 | +16.53% |

### Change over 7d (vs run at 2026-09-12T01:50:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,774.03 | 4,416.04 | +17.01% |
| Average non-vote TPS | 1,649.21 | 1,894.43 | +14.87% |
| Average slot time (ms) | 316.10 | 267.10 | -15.50% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 5,906,350,849.00 | 6,396,701,682.00 | +8.30% |
| SOL price | 102.10 | 113.63 | +11.29% |
| Stablecoin supply | 16,554,576,484.00 | 15,876,163,466.00 | -4.10% |
| 24h DEX volume | 3,249,433,436.43 | 3,097,318,491.84 | -4.68% |
| 24h chain fees | 16,596,146.14 | 15,267,932.07 | -8.00% |

### Change over 30d (vs run at 2026-08-19T18:15:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,093.61 | 4,416.04 | -13.30% |
| Average non-vote TPS | 3,460.99 | 1,894.43 | -45.26% |
| Average slot time (ms) | 416.70 | 267.10 | -35.90% |
| Active validators | 686.00 | 677.00 | -1.31% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 5,060,698,995.00 | 6,396,701,682.00 | +26.40% |
| SOL price | 81.32 | 113.63 | +39.73% |
| Stablecoin supply | 16,009,704,067.00 | 15,876,163,466.00 | -0.83% |
| 24h DEX volume | 1,838,194,723.04 | 3,097,318,491.84 | +68.50% |
| 24h chain fees | 8,772,755.23 | 15,267,932.07 | +74.04% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
