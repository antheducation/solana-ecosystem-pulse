# Solana Ecosystem Pulse

**Generated:** 2026-09-18T10:08:58Z · **Schema:** `1.0.0` · **Collection time:** 10.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $106.42 | +6.60% |
| Market cap | $62.50B | rank #7 |
| Total value locked | $6.02B | +4.38% |
| Stablecoin supply | $15.71B | -0.41% |
| DEX volume (24h) | $2.55B | -8.77% |
| Chain fees / REV (24h) | $13.90M | -1.17% |
| Non-vote TPS (1h avg) | 1,540 | peak 4,411 total |
| Active validators | 677 | 11 delinquent |
| Epoch 1037 | 15.77% complete | 363,866 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 86 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 265.90 sits 24.7 sigma below the median of the last 86 runs (317.20, -16.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,539.8 average over the last 60 minutes; 1,716.4 in the latest sample.
- **Total TPS:** 4,071.9 average, 4,410.9 peak. Consensus votes account for 62.2% of all transactions.
- **Slot time:** 265.9 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 426,093,122 at absolute slot 448,052,134.
- **Epoch 1037:** slot 68,134 of 432,000 (15.77% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.642% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 61 ms |
| `solana-rpc.publicnode.com` | yes | 50 ms |
| `api.mainnet.solana.com` | yes | 43 ms |

## Validators & stake

- **677 active** validators, **11 delinquent** (1.60% by count, 0.036% by stake).
- **Total stake:** 439,612,408 SOL ($46.78B); stake rate 69.31% of total supply.
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

- **SOL:** $106.42 (+6.60% 24h, +7.07% 7d, +37.74% 30d). Market cap $62.50B, 24h volume $4.41B (7.06% of cap). Price source: `coingecko`.
- **TVL:** $6.02B across 333 protocols - rank #2 of 468 chains, 6.72% of all tracked chain TVL. +4.93% over 7d, -54.4% from its ATH.
- **Stablecoins:** $15.71B circulating on Solana (-3.97% 7d) - $2.61 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.55B in 24h, $16.06B over 7d across 124 venues. Volume/TVL turnover 0.424x per day.
- **REV (chain fees):** $13.90M in 24h, $409.66M over 30d. Retained chain revenue $5.64M (40.6% of fees). Annualised fees are 8.12% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,297,324 SOL circulating of 634,298,578 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.69B | +6.3% | +11.3% |
| 2 | Kamino Lend | Lending | $1.36B | +0.8% | +4.5% |
| 3 | Raydium AMM | Dexs | $1.18B | +5.0% | +6.5% |
| 4 | Jupiter Lend | Lending | $1.12B | +2.8% | +4.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.10B | +5.9% | +6.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.10B | +6.2% | +7.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $768.36M | +3.3% | +4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $548.49M | +6.0% | +6.7% |
| 9 | Marinade Native | Staking Pool | $403.50M | +5.8% | +5.8% |
| 10 | Sentora Curator | Risk Curators | $369.80M | -0.6% | -4.6% |
| 11 | PumpSwap | Dexs | $342.24M | +5.0% | +5.7% |
| 12 | OnRe | RWA | $303.12M | +0.1% | -2.1% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.47B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.7% · Lending 17.7% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.8%

### Tokenised assets

$882.06M of tokenised real-world assets and equities are locked on Solana - 5.701% of chain TVL.

- OnRe (RWA): $303.12M
- Solstice (Basis Trading): $234.95M
- Huma Finance V2 (RWA): $193.37M
- JupUSD (Basis Trading): $46.77M
- Plume Vaults (RWA): $28.08M

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
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [SIMD-0123: SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-16
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

### Change over 24h (vs run at 2026-09-17T10:32:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,552.39 | 4,071.90 | +14.62% |
| Average non-vote TPS | 1,435.43 | 1,539.85 | +7.27% |
| Average slot time (ms) | 316.90 | 265.90 | -16.09% |
| Active validators | 674.00 | 677.00 | +0.45% |
| Delinquent validators | 16.00 | 11.00 | -31.25% |
| Solana TVL | 5,840,847,957.00 | 6,020,571,779.00 | +3.08% |
| SOL price | 99.67 | 106.42 | +6.77% |
| Stablecoin supply | 15,772,866,527.00 | 15,709,402,844.00 | -0.40% |
| 24h DEX volume | 2,733,441,991.18 | 2,553,904,323.29 | -6.57% |
| 24h chain fees | 14,202,548.05 | 13,898,915.10 | -2.14% |

### Change over 7d (vs run at 2026-09-11T10:06:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,482.12 | 4,071.90 | +16.94% |
| Average non-vote TPS | 1,349.41 | 1,539.85 | +14.11% |
| Average slot time (ms) | 315.10 | 265.90 | -15.61% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 5,802,516,859.00 | 6,020,571,779.00 | +3.76% |
| SOL price | 99.49 | 106.42 | +6.97% |
| Stablecoin supply | 16,356,714,023.00 | 15,709,402,844.00 | -3.96% |
| 24h DEX volume | 2,948,479,741.01 | 2,553,904,323.29 | -13.38% |
| 24h chain fees | 14,817,128.44 | 13,898,915.10 | -6.20% |

### Change over 30d (vs run at 2026-08-19T18:15:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,093.61 | 4,071.90 | -20.06% |
| Average non-vote TPS | 3,460.99 | 1,539.85 | -55.51% |
| Average slot time (ms) | 416.70 | 265.90 | -36.19% |
| Active validators | 686.00 | 677.00 | -1.31% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 5,060,698,995.00 | 6,020,571,779.00 | +18.97% |
| SOL price | 81.32 | 106.42 | +30.87% |
| Stablecoin supply | 16,009,704,067.00 | 15,709,402,844.00 | -1.88% |
| 24h DEX volume | 1,838,194,723.04 | 2,553,904,323.29 | +38.94% |
| 24h chain fees | 8,772,755.23 | 13,898,915.10 | +58.43% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 10.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
