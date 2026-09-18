# Solana Ecosystem Pulse

**Generated:** 2026-09-18T20:04:06Z · **Schema:** `1.0.0` · **Collection time:** 17.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $113.98 | +12.86% |
| Market cap | $66.94B | rank #7 |
| Total value locked | $6.24B | +8.02% |
| Stablecoin supply | $15.71B | -0.38% |
| DEX volume (24h) | $2.59B | -7.41% |
| Chain fees / REV (24h) | $14.68M | -1.45% |
| Non-vote TPS (1h avg) | 2,440 | peak 5,704 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1037 | 46.73% complete | 230,136 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 86 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 5 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.70 sits 23.8 sigma below the median of the last 86 runs (317.20, -15.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 12.9% in 24h) | SOL price changed +12.9% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 8.0% in 24h) | Solana TVL changed +8.0% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,242,343,437.00 sits 3.4 sigma above the median of the last 86 runs (5,850,649,762.00, +6.7%). | `zscore` |
| [WARNING] | SOL price is above its recent norm | Current 113.98 sits 3.2 sigma above the median of the last 86 runs (101.12, +12.7%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,440.1 average over the last 60 minutes; 2,397.6 in the latest sample.
- **Total TPS:** 4,950.6 average, 5,703.5 peak. Consensus votes account for 50.7% of all transactions.
- **Slot time:** 267.7 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 426,226,783 at absolute slot 448,185,864.
- **Epoch 1037:** slot 201,864 of 432,000 (46.73% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.642% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 268 ms |
| `solana-rpc.publicnode.com` | yes | 161 ms |
| `api.mainnet.solana.com` | yes | 241 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.040% by stake).
- **Total stake:** 439,612,408 SOL ($50.11B); stake rate 69.31% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.24%; 242 validators at 0% and 61 at 100%.

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

- **SOL:** $113.98 (+12.86% 24h, +11.73% 7d, +38.44% 30d). Market cap $66.94B, 24h volume $6.49B (9.70% of cap). Price source: `coingecko`.
- **TVL:** $6.24B across 332 protocols - rank #2 of 468 chains, 6.78% of all tracked chain TVL. +8.60% over 7d, -52.8% from its ATH.
- **Stablecoins:** $15.71B circulating on Solana (-3.95% 7d) - $2.52 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.59B in 24h, $17.44B over 7d across 124 venues. Volume/TVL turnover 0.415x per day.
- **REV (chain fees):** $14.68M in 24h, $411.97M over 30d. Retained chain revenue $6.23M (42.5% of fees). Annualised fees are 8.00% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,296,877 SOL circulating of 634,298,132 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +11.1% | +17.9% |
| 2 | Kamino Lend | Lending | $1.40B | +5.0% | +7.4% |
| 3 | Raydium AMM | Dexs | $1.26B | +10.4% | +13.6% |
| 4 | Binance Staked SOL | Liquid Staking | $1.17B | +11.3% | +12.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.16B | +11.1% | +14.0% |
| 6 | Jupiter Lend | Lending | $1.15B | +5.2% | +7.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $801.69M | +7.0% | +8.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $582.62M | +10.9% | +13.4% |
| 9 | Marinade Native | Staking Pool | $428.67M | +11.2% | +12.3% |
| 10 | Sentora Curator | Risk Curators | $369.08M | +1.0% | -4.8% |
| 11 | PumpSwap | Dexs | $366.39M | +11.8% | +13.2% |
| 12 | Drift Staked SOL | Liquid Staking | $316.46M | +11.2% | +13.5% |

The top five protocols hold 41.8% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.19B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.3% · Lending 17.4% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.2% · Risk Curators 3.6%

### Tokenised assets

$877.89M of tokenised real-world assets and equities are locked on Solana - 5.424% of chain TVL.

- OnRe (RWA): $303.96M
- Solstice (Basis Trading): $232.42M
- Huma Finance V2 (RWA): $197.18M
- JupUSD (Basis Trading): $46.80M
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

### Change over 24h (vs run at 2026-09-17T20:39:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,673.89 | 4,950.64 | +5.92% |
| Average non-vote TPS | 2,551.83 | 2,440.09 | -4.38% |
| Average slot time (ms) | 318.10 | 267.70 | -15.84% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,865,883,806.00 | 6,242,343,437.00 | +6.42% |
| SOL price | 101.14 | 113.98 | +12.70% |
| Stablecoin supply | 15,774,027,557.00 | 15,713,039,562.00 | -0.39% |
| 24h DEX volume | 2,800,249,070.18 | 2,592,123,183.29 | -7.43% |
| 24h chain fees | 14,069,098.05 | 14,675,830.10 | +4.31% |

### Change over 7d (vs run at 2026-09-11T20:08:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,273.36 | 4,950.64 | +15.85% |
| Average non-vote TPS | 2,154.29 | 2,440.09 | +13.27% |
| Average slot time (ms) | 317.20 | 267.70 | -15.61% |
| Active validators | 678.00 | 676.00 | -0.29% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,878,734,141.00 | 6,242,343,437.00 | +6.19% |
| SOL price | 102.41 | 113.98 | +11.30% |
| Stablecoin supply | 16,358,198,746.00 | 15,713,039,562.00 | -3.94% |
| 24h DEX volume | 2,921,890,110.01 | 2,592,123,183.29 | -11.29% |
| 24h chain fees | 14,614,973.44 | 14,675,830.10 | +0.42% |

### Change over 30d (vs run at 2026-08-19T18:15:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,093.61 | 4,950.64 | -2.81% |
| Average non-vote TPS | 3,460.99 | 2,440.09 | -29.50% |
| Average slot time (ms) | 416.70 | 267.70 | -35.76% |
| Active validators | 686.00 | 676.00 | -1.46% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 5,060,698,995.00 | 6,242,343,437.00 | +23.35% |
| SOL price | 81.32 | 113.98 | +40.16% |
| Stablecoin supply | 16,009,704,067.00 | 15,713,039,562.00 | -1.85% |
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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
