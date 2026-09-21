# Solana Ecosystem Pulse

**Generated:** 2026-09-21T11:15:05Z · **Schema:** `1.0.0` · **Collection time:** 15.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $116.20 | +7.58% |
| Market cap | $68.29B | rank #7 |
| Total value locked | $6.38B | +3.37% |
| Stablecoin supply | $15.91B | +0.63% |
| DEX volume (24h) | $2.80B | -2.81% |
| Chain fees / REV (24h) | $14.38M | -5.93% |
| Non-vote TPS (1h avg) | 1,533 | peak 4,577 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1039 | 44.18% complete | 241,124 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 89 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.50 sits 20.0 sigma below the median of the last 89 runs (316.90, -15.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,384,701,956.00 sits 3.5 sigma above the median of the last 89 runs (5,852,308,147.00, +9.1%). | `zscore` |
| [WARNING] | SOL price is above its recent norm | Current 116.20 sits 3.1 sigma above the median of the last 89 runs (101.32, +14.7%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,532.5 average over the last 60 minutes; 1,282.8 in the latest sample.
- **Total TPS:** 4,062.4 average, 4,577.3 peak. Consensus votes account for 62.3% of all transactions.
- **Slot time:** 266.5 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 427,079,513 at absolute slot 449,038,876.
- **Epoch 1039:** slot 190,876 of 432,000 (44.18% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.638% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 170 ms |
| `solana-rpc.publicnode.com` | yes | 59 ms |
| `api.mainnet.solana.com` | yes | 99 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.043% by stake).
- **Total stake:** 439,905,519 SOL ($51.12B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.79% of active stake.
- **Commission:** median 5.0%, mean 12.23%; 242 validators at 0% and 61 at 100%.

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

- **SOL:** $116.20 (+7.58% 24h, +14.21% 7d, +25.15% 30d). Market cap $68.29B, 24h volume $4.83B (7.07% of cap). Price source: `coingecko`.
- **TVL:** $6.38B across 333 protocols - rank #2 of 467 chains, 6.71% of all tracked chain TVL. +9.41% over 7d, -51.8% from its ATH.
- **Stablecoins:** $15.91B circulating on Solana (-2.75% 7d) - $2.49 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.80B in 24h, $19.83B over 7d across 124 venues. Volume/TVL turnover 0.438x per day.
- **REV (chain fees):** $14.38M in 24h, $420.43M over 30d. Retained chain revenue $5.37M (37.4% of fees). Annualised fees are 7.69% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,437,443 SOL circulating of 634,453,548 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | +7.6% | +21.4% |
| 2 | Kamino Lend | Lending | $1.41B | +3.2% | +5.3% |
| 3 | Raydium AMM | Dexs | $1.30B | +5.5% | +14.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.20B | +7.4% | +17.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | +7.1% | +16.3% |
| 6 | Jupiter Lend | Lending | $1.18B | +5.0% | +8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $819.14M | +5.4% | +10.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $597.27M | +6.9% | +15.9% |
| 9 | Marinade Native | Staking Pool | $441.92M | +7.0% | +16.4% |
| 10 | Sentora Curator | Risk Curators | $364.22M | -0.1% | -6.5% |
| 11 | PumpSwap | Dexs | $359.71M | +1.7% | +9.9% |
| 12 | Drift Staked SOL | Liquid Staking | $326.18M | +7.0% | +16.3% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.59B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.3% · Dexs 15.5% · Derivatives 5.4% · Staking Pool 4.2% · RWA 3.5%

### Tokenised assets

$886.79M of tokenised real-world assets and equities are locked on Solana - 5.346% of chain TVL.

- OnRe (RWA): $306.25M
- Solstice (Basis Trading): $232.45M
- Huma Finance V2 (RWA): $203.65M
- JupUSD (Basis Trading): $46.71M
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

### Change over 24h (vs run at 2026-09-20T10:11:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,772.47 | 4,062.42 | +7.69% |
| Average non-vote TPS | 1,239.40 | 1,532.53 | +23.65% |
| Average slot time (ms) | 266.60 | 266.50 | -0.04% |
| Active validators | 678.00 | 677.00 | -0.15% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 6,124,115,707.00 | 6,384,701,956.00 | +4.26% |
| SOL price | 108.07 | 116.20 | +7.52% |
| Stablecoin supply | 15,802,349,869.00 | 15,905,119,382.00 | +0.65% |
| 24h DEX volume | 3,233,490,127.20 | 2,795,356,104.36 | -13.55% |
| 24h chain fees | 15,220,774.85 | 14,383,414.08 | -5.50% |

### Change over 7d (vs run at 2026-09-14T11:05:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,417.38 | 4,062.42 | +18.88% |
| Average non-vote TPS | 1,285.09 | 1,532.53 | +19.25% |
| Average slot time (ms) | 315.30 | 266.50 | -15.48% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,891,617,539.00 | 6,384,701,956.00 | +8.37% |
| SOL price | 101.76 | 116.20 | +14.19% |
| Stablecoin supply | 16,352,362,124.00 | 15,905,119,382.00 | -2.74% |
| 24h DEX volume | 1,790,994,711.97 | 2,795,356,104.36 | +56.08% |
| 24h chain fees | 14,255,438.64 | 14,383,414.08 | +0.90% |

### Change over 30d (vs run at 2026-08-22T18:12:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,909.94 | 4,062.42 | +3.90% |
| Average non-vote TPS | 2,049.79 | 1,532.53 | -25.23% |
| Average slot time (ms) | 366.90 | 266.50 | -27.36% |
| Active validators | 687.00 | 677.00 | -1.46% |
| Delinquent validators | 8.00 | 13.00 | +62.50% |
| Solana TVL | 5,514,383,081.00 | 6,384,701,956.00 | +15.78% |
| SOL price | 94.15 | 116.20 | +23.42% |
| Stablecoin supply | 16,420,708,533.00 | 15,905,119,382.00 | -3.14% |
| 24h DEX volume | 3,600,948,276.22 | 2,795,356,104.36 | -22.37% |
| 24h chain fees | 13,332,529.88 | 14,383,414.08 | +7.88% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
