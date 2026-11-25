# Solana Ecosystem Pulse

**Generated:** 2026-11-25T16:18:44Z · **Schema:** `1.0.0` · **Collection time:** 21.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $67.77 | -1.46% |
| Market cap | $40.13B | rank #7 |
| Total value locked | $4.44B | -4.74% |
| Stablecoin supply | $13.52B | -2.68% |
| DEX volume (24h) | $1.46B | -19.33% |
| Chain fees / REV (24h) | $7.15M | -15.53% |
| Non-vote TPS (1h avg) | 2,791 | peak 4,392 total |
| Active validators | 659 | 28 delinquent |
| Epoch 1096 | 78.39% complete | 93,335 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,791.2 average over the last 60 minutes; 3,441.3 in the latest sample.
- **Total TPS:** 2,791.2 average, 4,391.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.8 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 451,823,691 at absolute slot 473,810,665.
- **Epoch 1096:** slot 338,665 of 432,000 (78.39% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.541% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 192 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 176 ms |

## Validators & stake

- **659 active** validators, **28 delinquent** (4.08% by count, 0.042% by stake).
- **Total stake:** 424,794,569 SOL ($28.79B); stake rate 66.57% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.01% and top 33 hold 46.66% of active stake.
- **Commission:** median 5.0%, mean 13.13%; 219 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,003,542 | 4.004% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,962,658 | 3.759% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,418,812 | 2.925% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,242,949 | 2.412% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,885,209 | 2.328% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,269 | 2.264% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,283,847 | 2.186% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,016,085 | 1.888% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,968,432 | 1.641% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,779,378 | 1.597% | 5% |

## Economics

- **SOL:** $67.77 (-1.46% 24h, -7.72% 7d, -33.42% 30d). Market cap $40.13B, 24h volume $2.79B (6.96% of cap). Price source: `coingecko`.
- **TVL:** $4.44B across 344 protocols - rank #3 of 426 chains, 6.59% of all tracked chain TVL. -7.98% over 7d, -62.7% from its ATH.
- **Stablecoins:** $13.52B circulating on Solana (-3.28% 7d) - $3.04 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.46B in 24h, $11.19B over 7d across 145 venues. Volume/TVL turnover 0.328x per day.
- **REV (chain fees):** $7.15M in 24h, $280.18M over 30d. Retained chain revenue $2.67M (37.3% of fees). Annualised fees are 6.51% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,128,159 SOL circulating of 638,163,798 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.18B | -7.4% | -15.6% |
| 2 | Kamino Lend | Lending | $1.08B | -1.6% | -7.2% |
| 3 | Jupiter Lend | Lending | $915.99M | -2.8% | -6.2% |
| 4 | Raydium AMM | Dexs | $743.26M | -3.2% | -10.3% |
| 5 | Binance Staked SOL | Liquid Staking | $685.47M | -3.1% | -11.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $674.88M | -2.8% | -11.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $547.01M | -3.3% | -8.2% |
| 8 | Sentora Curator | Risk Curators | $355.23M | +0.3% | -0.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $351.05M | -2.4% | -9.2% |
| 10 | OnRe | RWA | $289.91M | +0.0% | -1.2% |
| 11 | CCIP | Bridge | $267.62M | +0.1% | +1.8% |
| 12 | Forward Industries SOL | Liquid Staking | $263.17M | -2.7% | -13.4% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 344 protocols the total is $11.23B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 39.5% · Lending 19.4% · Dexs 14.6% · Derivatives 5.4% · RWA 4.7% · Risk Curators 4.4%

### Tokenised assets

$779.19M of tokenised real-world assets and equities are locked on Solana - 6.940% of chain TVL.

- OnRe (RWA): $289.91M
- Huma (RWA): $225.91M
- Solstice (Basis Trading): $201.02M
- JupUSD (Basis Trading): $38.22M
- Solomon USDv (Basis Trading): $8.76M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-25
- [SIMD-0506: Withdraw SIMD-0506](https://github.com/solana-foundation/solana-improvement-documents/pull/738) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [100M CUs Pt2](https://github.com/solana-foundation/solana-improvement-documents/pull/698) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-11-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-24T16:36:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,985.71 | 2,791.23 | -6.51% |
| Average non-vote TPS | 2,985.71 | 2,791.23 | -6.51% |
| Average slot time (ms) | 205.30 | 214.80 | +4.63% |
| Active validators | 661.00 | 659.00 | -0.30% |
| Delinquent validators | 25.00 | 28.00 | +12.00% |
| Solana TVL | 4,565,087,427.00 | 4,442,324,165.00 | -2.69% |
| SOL price | 68.97 | 67.77 | -1.74% |
| Stablecoin supply | 13,889,158,688.00 | 13,517,716,588.00 | -2.67% |
| 24h DEX volume | 1,805,966,413.26 | 1,456,787,101.44 | -19.33% |
| 24h chain fees | 8,461,387.38 | 7,153,686.50 | -15.45% |

### Change over 7d (vs run at 2026-11-18T14:41:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,964.18 | 2,791.23 | +42.11% |
| Average non-vote TPS | 1,964.17 | 2,791.23 | +42.11% |
| Average slot time (ms) | 215.80 | 214.80 | -0.46% |
| Active validators | 660.00 | 659.00 | -0.15% |
| Delinquent validators | 25.00 | 28.00 | +12.00% |
| Solana TVL | 4,793,648,732.00 | 4,442,324,165.00 | -7.33% |
| SOL price | 73.81 | 67.77 | -8.18% |
| Stablecoin supply | 13,976,278,030.00 | 13,517,716,588.00 | -3.28% |
| 24h DEX volume | 1,509,645,641.17 | 1,456,787,101.44 | -3.50% |
| 24h chain fees | 8,200,781.62 | 7,153,686.50 | -12.77% |

### Change over 30d (vs run at 2026-10-26T21:59:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,853.07 | 2,791.23 | +50.63% |
| Average non-vote TPS | 1,853.06 | 2,791.23 | +50.63% |
| Average slot time (ms) | 211.90 | 214.80 | +1.37% |
| Active validators | 665.00 | 659.00 | -0.90% |
| Delinquent validators | 20.00 | 28.00 | +40.00% |
| Solana TVL | 5,710,299,220.00 | 4,442,324,165.00 | -22.21% |
| SOL price | 100.45 | 67.77 | -32.53% |
| Stablecoin supply | 15,849,510,602.00 | 13,517,716,588.00 | -14.71% |
| 24h DEX volume | 1,449,231,950.27 | 1,456,787,101.44 | +0.52% |
| 24h chain fees | 9,292,855.03 | 7,153,686.50 | -23.02% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
