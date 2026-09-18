# Solana Ecosystem Pulse

**Generated:** 2026-09-18T15:18:38Z · **Schema:** `1.0.0` · **Collection time:** 14.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.21 | +9.65% |
| Market cap | $64.72B | rank #7 |
| Total value locked | $6.07B | +5.45% |
| Stablecoin supply | $15.71B | -0.40% |
| DEX volume (24h) | $2.59B | -7.41% |
| Chain fees / REV (24h) | $14.68M | -1.45% |
| Non-vote TPS (1h avg) | 2,804 | peak 5,781 total |
| Active validators | 677 | 11 delinquent |
| Epoch 1037 | 31.89% complete | 294,232 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 86 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.40 sits 24.0 sigma below the median of the last 86 runs (317.20, -15.7%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 9.7% in 24h) | SOL price changed +9.7% over the last day, past the 8% alert band. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,803.9 average over the last 60 minutes; 2,671.0 in the latest sample.
- **Total TPS:** 5,324.8 average, 5,781.0 peak. Consensus votes account for 47.3% of all transactions.
- **Slot time:** 267.4 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 426,162,715 at absolute slot 448,121,768.
- **Epoch 1037:** slot 137,768 of 432,000 (31.89% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.642% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 317 ms |
| `solana-rpc.publicnode.com` | yes | 72 ms |
| `api.mainnet.solana.com` | yes | 122 ms |

## Validators & stake

- **677 active** validators, **11 delinquent** (1.60% by count, 0.036% by stake).
- **Total stake:** 439,612,408 SOL ($48.45B); stake rate 69.31% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.77% of active stake.
- **Commission:** median 5.0%, mean 12.22%; 243 validators at 0% and 61 at 100%.

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

- **SOL:** $110.21 (+9.65% 24h, +6.73% 7d, +36.31% 30d). Market cap $64.72B, 24h volume $5.42B (8.37% of cap). Price source: `coingecko`.
- **TVL:** $6.07B across 332 protocols - rank #2 of 468 chains, 6.75% of all tracked chain TVL. +6.02% over 7d, -53.9% from its ATH.
- **Stablecoins:** $15.71B circulating on Solana (-3.97% 7d) - $2.59 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.59B in 24h, $17.44B over 7d across 124 venues. Volume/TVL turnover 0.427x per day.
- **REV (chain fees):** $14.68M in 24h, $411.97M over 30d. Retained chain revenue $6.23M (42.5% of fees). Annualised fees are 8.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,297,102 SOL circulating of 634,298,356 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.75B | +8.4% | +15.1% |
| 2 | Kamino Lend | Lending | $1.36B | +1.7% | +4.5% |
| 3 | Raydium AMM | Dexs | $1.20B | +5.4% | +8.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.14B | +8.6% | +10.2% |
| 5 | Jupiter Lend | Lending | $1.13B | +4.3% | +6.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.09B | +4.7% | +7.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $768.77M | +2.7% | +4.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $548.30M | +4.8% | +6.7% |
| 9 | Marinade Native | Staking Pool | $418.59M | +8.6% | +9.7% |
| 10 | Sentora Curator | Risk Curators | $368.11M | +0.8% | -5.1% |
| 11 | PumpSwap | Dexs | $344.15M | +6.0% | +6.3% |
| 12 | OnRe | RWA | $303.70M | +0.2% | -1.9% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.65B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.6% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.2% · Risk Curators 3.7%

### Tokenised assets

$873.32M of tokenised real-world assets and equities are locked on Solana - 5.581% of chain TVL.

- OnRe (RWA): $303.70M
- Solstice (Basis Trading): $232.34M
- Huma Finance V2 (RWA): $193.28M
- JupUSD (Basis Trading): $46.77M
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
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | pre-release |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [SIMD-0123: SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-16

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

### Change over 24h (vs run at 2026-09-17T15:46:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,671.71 | 5,324.84 | +13.98% |
| Average non-vote TPS | 2,543.87 | 2,803.86 | +10.22% |
| Average slot time (ms) | 316.80 | 267.40 | -15.59% |
| Active validators | 678.00 | 677.00 | -0.15% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 5,852,308,147.00 | 6,074,970,771.00 | +3.80% |
| SOL price | 101.10 | 110.21 | +9.01% |
| Stablecoin supply | 15,773,094,526.00 | 15,710,184,327.00 | -0.40% |
| 24h DEX volume | 2,800,249,070.18 | 2,592,123,183.29 | -7.43% |
| 24h chain fees | 14,068,828.05 | 14,675,830.10 | +4.31% |

### Change over 7d (vs run at 2026-09-11T15:22:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,526.83 | 5,324.84 | +17.63% |
| Average non-vote TPS | 2,427.26 | 2,803.86 | +15.52% |
| Average slot time (ms) | 318.00 | 267.40 | -15.91% |
| Active validators | 674.00 | 677.00 | +0.45% |
| Delinquent validators | 16.00 | 11.00 | -31.25% |
| Solana TVL | 5,829,321,373.00 | 6,074,970,771.00 | +4.21% |
| SOL price | 103.12 | 110.21 | +6.88% |
| Stablecoin supply | 16,356,744,456.00 | 15,710,184,327.00 | -3.95% |
| 24h DEX volume | 2,921,890,110.01 | 2,592,123,183.29 | -11.29% |
| 24h chain fees | 14,614,973.44 | 14,675,830.10 | +0.42% |

### Change over 30d (vs run at 2026-08-19T18:15:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,093.61 | 5,324.84 | +4.54% |
| Average non-vote TPS | 3,460.99 | 2,803.86 | -18.99% |
| Average slot time (ms) | 416.70 | 267.40 | -35.83% |
| Active validators | 686.00 | 677.00 | -1.31% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 5,060,698,995.00 | 6,074,970,771.00 | +20.04% |
| SOL price | 81.32 | 110.21 | +35.53% |
| Stablecoin supply | 16,009,704,067.00 | 15,710,184,327.00 | -1.87% |
| 24h DEX volume | 1,838,194,723.04 | 2,592,123,183.29 | +41.01% |
| 24h chain fees | 8,772,755.23 | 14,675,830.10 | +67.29% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
