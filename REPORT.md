# Solana Ecosystem Pulse

**Generated:** 2026-09-21T01:59:33Z · **Schema:** `1.0.0` · **Collection time:** 16.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.98 | +0.79% |
| Market cap | $65.14B | rank #7 |
| Total value locked | $6.19B | +0.02% |
| Stablecoin supply | $15.91B | +0.64% |
| DEX volume (24h) | $2.75B | -4.35% |
| Chain fees / REV (24h) | $14.41M | -5.72% |
| Non-vote TPS (1h avg) | 2,147 | peak 5,447 total |
| Active validators | 676 | 14 delinquent |
| Epoch 1039 | 15.23% complete | 366,212 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 88 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.80 sits 19.9 sigma below the median of the last 88 runs (316.90, -15.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,147.2 average over the last 60 minutes; 1,998.8 in the latest sample.
- **Total TPS:** 4,670.8 average, 5,447.1 peak. Consensus votes account for 54.0% of all transactions.
- **Slot time:** 266.8 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 426,954,432 at absolute slot 448,913,788.
- **Epoch 1039:** slot 65,788 of 432,000 (15.23% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.638% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 159 ms |
| `solana-rpc.publicnode.com` | yes | 165 ms |
| `api.mainnet.solana.com` | yes | 120 ms |

## Validators & stake

- **676 active** validators, **14 delinquent** (2.03% by count, 0.045% by stake).
- **Total stake:** 439,905,519 SOL ($48.82B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.79% of active stake.
- **Commission:** median 5.0%, mean 12.24%; 241 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,856,583 | 4.061% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,828,384 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,518,302 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,252,588 | 2.559% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,788,818 | 2.226% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,354 | 2.104% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,106,985 | 2.071% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,443,840 | 1.693% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,088,079 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,572,007 | 1.495% | 0% |

## Economics

- **SOL:** $110.98 (+0.79% 24h, +11.39% 7d, +18.25% 30d). Market cap $65.14B, 24h volume $3.50B (5.38% of cap). Price source: `coingecko`.
- **TVL:** $6.19B across 333 protocols - rank #2 of 467 chains, 6.62% of all tracked chain TVL. +6.11% over 7d, -53.2% from its ATH.
- **Stablecoins:** $15.91B circulating on Solana (-2.74% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.75B in 24h, $18.49B over 7d across 124 venues. Volume/TVL turnover 0.444x per day.
- **REV (chain fees):** $14.41M in 24h, $419.08M over 30d. Retained chain revenue $5.37M (37.3% of fees). Annualised fees are 8.08% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,437,806 SOL circulating of 634,453,910 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.77B | +0.4% | +16.1% |
| 2 | Kamino Lend | Lending | $1.37B | +0.3% | +2.1% |
| 3 | Raydium AMM | Dexs | $1.26B | +0.7% | +11.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.15B | +0.6% | +12.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.15B | +0.3% | +11.6% |
| 6 | Jupiter Lend | Lending | $1.12B | -1.9% | +2.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $792.63M | +0.2% | +6.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $572.94M | -0.1% | +11.2% |
| 9 | Marinade Native | Staking Pool | $423.98M | -0.0% | +11.7% |
| 10 | Sentora Curator | Risk Curators | $364.70M | +0.0% | -6.3% |
| 11 | PumpSwap | Dexs | $360.37M | +0.3% | +10.1% |
| 12 | Drift Staked SOL | Liquid Staking | $312.92M | +0.2% | +11.6% |

The top five protocols hold 41.7% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.06B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.3% · Lending 17.2% · Dexs 15.7% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$884.42M of tokenised real-world assets and equities are locked on Solana - 5.508% of chain TVL.

- OnRe (RWA): $304.24M
- Solstice (Basis Trading): $232.47M
- Huma Finance V2 (RWA): $203.57M
- JupUSD (Basis Trading): $46.72M
- Plume Vaults (RWA): $28.13M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | pre-release |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-19
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17

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

### Change over 24h (vs run at 2026-09-20T01:58:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,136.77 | 4,670.76 | +12.91% |
| Average non-vote TPS | 1,601.78 | 2,147.21 | +34.05% |
| Average slot time (ms) | 266.40 | 266.80 | +0.15% |
| Active validators | 678.00 | 676.00 | -0.29% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 6,172,970,932.00 | 6,192,198,747.00 | +0.31% |
| SOL price | 110.06 | 110.98 | +0.84% |
| Stablecoin supply | 15,802,339,067.00 | 15,906,576,030.00 | +0.66% |
| 24h DEX volume | 3,233,773,154.20 | 2,750,992,818.36 | -14.93% |
| 24h chain fees | 16,246,928.52 | 14,412,340.37 | -11.29% |

### Change over 7d (vs run at 2026-09-14T01:59:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,858.00 | 4,670.76 | +21.07% |
| Average non-vote TPS | 1,717.42 | 2,147.21 | +25.03% |
| Average slot time (ms) | 315.80 | 266.80 | -15.52% |
| Active validators | 678.00 | 676.00 | -0.29% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 5,820,704,370.00 | 6,192,198,747.00 | +6.38% |
| SOL price | 99.80 | 110.98 | +11.20% |
| Stablecoin supply | 16,352,347,705.00 | 15,906,576,030.00 | -2.73% |
| 24h DEX volume | 1,637,064,257.97 | 2,750,992,818.36 | +68.04% |
| 24h chain fees | 14,050,324.45 | 14,412,340.37 | +2.58% |

### Change over 30d (vs run at 2026-08-21T18:19:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,537.20 | 4,670.76 | +2.94% |
| Average non-vote TPS | 2,672.27 | 2,147.21 | -19.65% |
| Average slot time (ms) | 365.30 | 266.80 | -26.96% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 9.00 | 14.00 | +55.56% |
| Solana TVL | 5,439,131,617.00 | 6,192,198,747.00 | +13.85% |
| SOL price | 91.85 | 110.98 | +20.83% |
| Stablecoin supply | 16,516,726,394.00 | 15,906,576,030.00 | -3.69% |
| 24h DEX volume | 2,770,509,439.33 | 2,750,992,818.36 | -0.70% |
| 24h chain fees | 11,078,485.08 | 14,412,340.37 | +30.09% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
