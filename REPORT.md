# Solana Ecosystem Pulse

**Generated:** 2026-09-22T02:06:14Z · **Schema:** `1.0.0` · **Collection time:** 14.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.51 | +5.50% |
| Market cap | $69.06B | rank #7 |
| Total value locked | $6.48B | +1.79% |
| Stablecoin supply | $17.17B | +7.95% |
| DEX volume (24h) | $3.37B | +20.57% |
| Chain fees / REV (24h) | $17.59M | +21.60% |
| Non-vote TPS (1h avg) | 2,080 | peak 5,410 total |
| Active validators | 677 | 14 delinquent |
| Epoch 1039 | 90.46% complete | 41,229 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 89 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 8.0% in 24h) | Stablecoin supply changed +8.0% over the last day, past the 3% alert band. | `threshold` |
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.00 sits 18.7 sigma below the median of the last 89 runs (316.80, -15.7%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,481,815,506.00 sits 3.7 sigma above the median of the last 89 runs (5,852,308,147.00, +10.8%). | `zscore` |
| [WARNING] | SOL price is above its recent norm | Current 117.51 sits 3.3 sigma above the median of the last 89 runs (101.32, +16.0%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,079.8 average over the last 60 minutes; 1,927.7 in the latest sample.
- **Total TPS:** 4,603.2 average, 5,409.9 peak. Consensus votes account for 54.8% of all transactions.
- **Slot time:** 267.0 ms average (target 400 ms), worst 1-minute bucket 284.4 ms.
- **Block height:** 427,279,301 at absolute slot 449,238,771.
- **Epoch 1039:** slot 390,771 of 432,000 (90.46% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.638% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 259 ms |
| `solana-rpc.publicnode.com` | yes | 67 ms |
| `api.mainnet.solana.com` | yes | 127 ms |

## Validators & stake

- **677 active** validators, **14 delinquent** (2.03% by count, 0.045% by stake).
- **Total stake:** 439,905,519 SOL ($51.69B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.79% of active stake.
- **Commission:** median 5.0%, mean 12.67%; 239 validators at 0% and 64 at 100%.

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

- **SOL:** $117.51 (+5.50% 24h, +14.93% 7d, +22.41% 30d). Market cap $69.06B, 24h volume $6.60B (9.56% of cap). Price source: `coingecko`.
- **TVL:** $6.48B across 333 protocols - rank #2 of 467 chains, 6.72% of all tracked chain TVL. +9.51% over 7d, -51.0% from its ATH.
- **Stablecoins:** $17.17B circulating on Solana (+4.78% 7d) - $2.65 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.37B in 24h, $19.33B over 7d across 125 venues. Volume/TVL turnover 0.520x per day.
- **REV (chain fees):** $17.59M in 24h, $425.31M over 30d. Retained chain revenue $7.15M (40.7% of fees). Annualised fees are 9.29% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,436,769 SOL circulating of 634,452,873 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.90B | +7.2% | +20.9% |
| 2 | Kamino Lend | Lending | $1.42B | +4.0% | +4.6% |
| 3 | Raydium AMM | Dexs | $1.35B | +6.5% | +17.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.23B | +6.9% | +16.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.23B | +6.7% | +16.7% |
| 6 | Jupiter Lend | Lending | $1.17B | +4.4% | +5.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $825.62M | +3.0% | +9.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.87M | +7.1% | +15.8% |
| 9 | Marinade Native | Staking Pool | $450.83M | +4.8% | +15.4% |
| 10 | PumpSwap | Dexs | $376.84M | +4.6% | +13.4% |
| 11 | Sentora Curator | Risk Curators | $362.70M | -0.6% | -5.3% |
| 12 | Drift Staked SOL | Liquid Staking | $334.43M | +5.3% | +15.9% |

The top five protocols hold 42.4% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.81B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 17.1% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$845.24M of tokenised real-world assets and equities are locked on Solana - 5.028% of chain TVL.

- OnRe (RWA): $302.63M
- Solstice (Basis Trading): $220.18M
- Huma Finance V2 (RWA): $177.72M
- JupUSD (Basis Trading): $46.66M
- Plume Vaults (RWA): $28.14M

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
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-21
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-21
- [SIMD-0649: SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) - updated 2026-09-21
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-21
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-21
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19

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

### Change over 24h (vs run at 2026-09-21T01:59:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,670.76 | 4,603.17 | -1.45% |
| Average non-vote TPS | 2,147.21 | 2,079.85 | -3.14% |
| Average slot time (ms) | 266.80 | 267.00 | +0.07% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 14.00 | 14.00 | +0.00% |
| Solana TVL | 6,192,198,747.00 | 6,481,815,506.00 | +4.68% |
| SOL price | 110.98 | 117.51 | +5.88% |
| Stablecoin supply | 15,906,576,030.00 | 17,171,514,140.00 | +7.95% |
| 24h DEX volume | 2,750,992,818.36 | 3,370,332,429.75 | +22.51% |
| 24h chain fees | 14,412,340.37 | 17,586,862.12 | +22.03% |

### Change over 7d (vs run at 2026-09-15T02:07:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,753.31 | 4,603.17 | +22.64% |
| Average non-vote TPS | 1,638.93 | 2,079.85 | +26.90% |
| Average slot time (ms) | 316.10 | 267.00 | -15.53% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 5,932,971,504.00 | 6,481,815,506.00 | +9.25% |
| SOL price | 102.31 | 117.51 | +14.86% |
| Stablecoin supply | 16,390,847,094.00 | 17,171,514,140.00 | +4.76% |
| 24h DEX volume | 2,196,247,156.85 | 3,370,332,429.75 | +53.46% |
| 24h chain fees | 14,419,679.63 | 17,586,862.12 | +21.96% |

### Change over 30d (vs run at 2026-08-22T18:12:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,909.94 | 4,603.17 | +17.73% |
| Average non-vote TPS | 2,049.79 | 2,079.85 | +1.47% |
| Average slot time (ms) | 366.90 | 267.00 | -27.23% |
| Active validators | 687.00 | 677.00 | -1.46% |
| Delinquent validators | 8.00 | 14.00 | +75.00% |
| Solana TVL | 5,514,383,081.00 | 6,481,815,506.00 | +17.54% |
| SOL price | 94.15 | 117.51 | +24.81% |
| Stablecoin supply | 16,420,708,533.00 | 17,171,514,140.00 | +4.57% |
| 24h DEX volume | 3,600,948,276.22 | 3,370,332,429.75 | -6.40% |
| 24h chain fees | 13,332,529.88 | 17,586,862.12 | +31.91% |

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
