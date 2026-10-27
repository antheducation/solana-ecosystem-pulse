# Solana Ecosystem Pulse

**Generated:** 2026-10-27T11:09:43Z · **Schema:** `1.0.0` · **Collection time:** 15.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.18 | -0.91% |
| Market cap | $59.10B | rank #7 |
| Total value locked | $5.68B | -0.88% |
| Stablecoin supply | $15.76B | -0.55% |
| DEX volume (24h) | $2.07B | +42.91% |
| Chain fees / REV (24h) | $11.67M | +25.55% |
| Non-vote TPS (1h avg) | 1,485 | peak 2,084 total |
| Active validators | 665 | 20 delinquent |
| Epoch 1069 | 55.63% complete | 191,661 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 124 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,485; the healthy floor used here is 1,500. | `threshold` |
| [SERIOUS] | Average TPS is below its recent norm | Current 1,484.87 sits 5.2 sigma below the median of the last 124 runs (4,576.33, -67.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 42.9% in 24h) | DEX volume changed +42.9% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,484.9 average over the last 60 minutes; 1,249.6 in the latest sample.
- **Total TPS:** 1,484.9 average, 2,083.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.8 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 440,074,096 at absolute slot 462,048,339.
- **Epoch 1069:** slot 240,339 of 432,000 (55.63% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.584% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 123 ms |
| `solana-rpc.publicnode.com` | yes | 175 ms |
| `api.mainnet.solana.com` | yes | 113 ms |

## Validators & stake

- **665 active** validators, **20 delinquent** (2.92% by count, 0.085% by stake).
- **Total stake:** 436,873,593 SOL ($43.77B); stake rate 68.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.60% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 13.06%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,059,304 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,636,453 | 3.811% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,660,117 | 2.900% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,812,577 | 2.477% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,716,980 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,494,053 | 2.175% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,206,552 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,754,189 | 1.776% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,040,177 | 1.613% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,375 | 1.603% | 0% |

## Economics

- **SOL:** $100.18 (-0.91% 24h, -3.80% 7d, -19.19% 30d). Market cap $59.10B, 24h volume $2.39B (4.04% of cap). Price source: `coingecko`.
- **TVL:** $5.68B across 333 protocols - rank #3 of 421 chains, 6.46% of all tracked chain TVL. -3.30% over 7d, -56.2% from its ATH.
- **Stablecoins:** $15.76B circulating on Solana (-0.92% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.07B in 24h, $13.69B over 7d across 138 venues. Volume/TVL turnover 0.365x per day.
- **REV (chain fees):** $11.67M in 24h, $418.37M over 30d. Retained chain revenue $4.58M (39.3% of fees). Annualised fees are 7.21% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,874,602 SOL circulating of 636,517,676 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.75B | -1.6% | -3.4% |
| 2 | Kamino Lend | Lending | $1.26B | -0.8% | -3.5% |
| 3 | Raydium AMM | Dexs | $1.13B | -1.0% | -4.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.06B | -1.0% | -3.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.04B | -1.9% | -5.2% |
| 6 | Jupiter Lend | Lending | $1.00B | -0.8% | -1.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $708.05M | -1.3% | -4.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $522.39M | -1.6% | -4.3% |
| 9 | Sentora Curator | Risk Curators | $383.96M | -0.9% | -14.4% |
| 10 | Marinade Native | Staking Pool | $358.71M | -1.6% | -5.1% |
| 11 | PumpSwap | Dexs | $330.56M | -1.9% | -5.2% |
| 12 | OnRe | RWA | $301.12M | +1.8% | +2.4% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.25B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.6% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · RWA 4.0% · Risk Curators 3.7%

### Tokenised assets

$869.71M of tokenised real-world assets and equities are locked on Solana - 5.703% of chain TVL.

- OnRe (RWA): $301.12M
- Huma (RWA): $257.43M
- Solstice (Basis Trading): $201.51M
- JupUSD (Basis Trading): $42.96M
- Plume Vaults (RWA): $36.55M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup) - Mon, 26 Oct 2026 10:00:00 GMT
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) - Fri, 23 Oct 2026 01:09:00 GMT
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | pre-release |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-27
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-27
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-27
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-26
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-26
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23

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

### Change over 24h (vs run at 2026-10-26T11:41:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,478.31 | 1,484.87 | +0.44% |
| Average non-vote TPS | 1,478.31 | 1,484.87 | +0.44% |
| Average slot time (ms) | 211.90 | 212.80 | +0.42% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 25.00 | 20.00 | -20.00% |
| Solana TVL | 5,740,388,903.00 | 5,681,242,565.00 | -1.03% |
| SOL price | 101.37 | 100.18 | -1.17% |
| Stablecoin supply | 15,877,222,933.00 | 15,762,299,946.00 | -0.72% |
| 24h DEX volume | 1,449,231,950.27 | 2,071,067,618.15 | +42.91% |
| 24h chain fees | 9,299,425.03 | 11,666,989.55 | +25.46% |

### Change over 7d (vs run at 2026-10-20T10:31:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,654.59 | 1,484.87 | -68.10% |
| Average non-vote TPS | 1,613.52 | 1,484.87 | -7.97% |
| Average slot time (ms) | 217.80 | 212.80 | -2.30% |
| Active validators | 666.00 | 665.00 | -0.15% |
| Delinquent validators | 13.00 | 20.00 | +53.85% |
| Solana TVL | 5,879,479,880.00 | 5,681,242,565.00 | -3.37% |
| SOL price | 103.92 | 100.18 | -3.60% |
| Stablecoin supply | 15,910,967,401.00 | 15,762,299,946.00 | -0.93% |
| 24h DEX volume | 1,610,948,501.83 | 2,071,067,618.15 | +28.56% |
| 24h chain fees | 11,969,320.99 | 11,666,989.55 | -2.53% |

### Change over 30d (vs run at 2026-09-27T20:31:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.15 | 1,484.87 | -68.13% |
| Average non-vote TPS | 2,150.72 | 1,484.87 | -30.96% |
| Average slot time (ms) | 268.10 | 212.80 | -20.63% |
| Active validators | 675.00 | 665.00 | -1.48% |
| Delinquent validators | 8.00 | 20.00 | +150.00% |
| Solana TVL | 6,696,462,246.00 | 5,681,242,565.00 | -15.16% |
| SOL price | 122.76 | 100.18 | -18.39% |
| Stablecoin supply | 16,803,216,984.00 | 15,762,299,946.00 | -6.19% |
| 24h DEX volume | 2,155,234,120.21 | 2,071,067,618.15 | -3.91% |
| 24h chain fees | 17,938,389.57 | 11,666,989.55 | -34.96% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
