# Solana Ecosystem Pulse

**Generated:** 2026-11-25T01:41:19Z · **Schema:** `1.0.0` · **Collection time:** 18.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $69.29 | -4.38% |
| Market cap | $41.03B | rank #7 |
| Total value locked | $4.57B | -0.32% |
| Stablecoin supply | $13.52B | -2.68% |
| DEX volume (24h) | $1.65B | -8.48% |
| Chain fees / REV (24h) | $7.65M | -9.38% |
| Non-vote TPS (1h avg) | 2,306 | peak 9,217 total |
| Active validators | 660 | 27 delinquent |
| Epoch 1096 | 21.70% complete | 338,274 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Throughput spike inside the sample window | Peak TPS 9,217 is 4.0x the window average (2,306) - a burst, not a steady load. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,306.0 average over the last 60 minutes; 1,626.5 in the latest sample.
- **Total TPS:** 2,306.0 average, 9,217.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 203.0 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 451,578,835 at absolute slot 473,565,726.
- **Epoch 1096:** slot 93,726 of 432,000 (21.70% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.541% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 186 ms |
| `solana-rpc.publicnode.com` | yes | 51 ms |
| `api.mainnet.solana.com` | yes | 154 ms |

## Validators & stake

- **660 active** validators, **27 delinquent** (3.93% by count, 0.019% by stake).
- **Total stake:** 424,794,569 SOL ($29.43B); stake rate 66.57% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.00% and top 33 hold 46.65% of active stake.
- **Commission:** median 5.0%, mean 12.92%; 220 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,003,542 | 4.004% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,962,658 | 3.758% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,418,812 | 2.924% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,242,949 | 2.412% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,885,209 | 2.328% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,269 | 2.264% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,283,847 | 2.186% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,016,085 | 1.887% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,968,432 | 1.641% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,779,378 | 1.596% | 5% |

## Economics

- **SOL:** $69.29 (-4.38% 24h, -7.50% 7d, -31.67% 30d). Market cap $41.03B, 24h volume $2.37B (5.77% of cap). Price source: `coingecko`.
- **TVL:** $4.57B across 343 protocols - rank #3 of 426 chains, 6.66% of all tracked chain TVL. -5.64% over 7d, -61.7% from its ATH.
- **Stablecoins:** $13.52B circulating on Solana (-3.28% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.65B in 24h, $10.30B over 7d across 145 venues. Volume/TVL turnover 0.362x per day.
- **REV (chain fees):** $7.65M in 24h, $274.51M over 30d. Retained chain revenue $2.81M (36.8% of fees). Annualised fees are 6.81% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,128,402 SOL circulating of 638,164,041 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.29B | -3.2% | -7.8% |
| 2 | Kamino Lend | Lending | $1.10B | -1.1% | -5.7% |
| 3 | Jupiter Lend | Lending | $954.65M | -1.5% | -2.2% |
| 4 | Raydium AMM | Dexs | $769.37M | -4.1% | -7.2% |
| 5 | Binance Staked SOL | Liquid Staking | $717.54M | -3.0% | -7.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $705.49M | -2.8% | -7.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $564.64M | -2.0% | -5.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $366.70M | -1.7% | -5.2% |
| 9 | Sentora Curator | Risk Curators | $354.92M | +0.4% | -0.7% |
| 10 | OnRe | RWA | $289.90M | +0.0% | -1.2% |
| 11 | Forward Industries SOL | Liquid Staking | $275.43M | -2.6% | -9.4% |
| 12 | CCIP | Bridge | $267.29M | +1.6% | +1.6% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.67B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.4% · Lending 19.2% · Dexs 14.4% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.2%

### Tokenised assets

$794.65M of tokenised real-world assets and equities are locked on Solana - 6.807% of chain TVL.

- OnRe (RWA): $289.90M
- Huma (RWA): $241.36M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $38.22M
- Solomon USDv (Basis Trading): $8.74M

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

- [100M CUs Pt2](https://github.com/solana-foundation/solana-improvement-documents/pull/698) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-24
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-11-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-24
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-24T03:31:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,744.10 | 2,306.02 | +32.22% |
| Average non-vote TPS | 1,744.10 | 2,306.02 | +32.22% |
| Average slot time (ms) | 215.10 | 203.00 | -5.63% |
| Active validators | 659.00 | 660.00 | +0.15% |
| Delinquent validators | 27.00 | 27.00 | +0.00% |
| Solana TVL | 4,673,622,755.00 | 4,568,842,954.00 | -2.24% |
| SOL price | 70.79 | 69.29 | -2.12% |
| Stablecoin supply | 13,888,339,896.00 | 13,518,061,358.00 | -2.67% |
| 24h DEX volume | 1,405,495,770.26 | 1,652,785,326.76 | +17.59% |
| 24h chain fees | 8,059,529.76 | 7,654,322.42 | -5.03% |

### Change over 7d (vs run at 2026-11-18T00:06:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,864.62 | 2,306.02 | +23.67% |
| Average non-vote TPS | 1,864.62 | 2,306.02 | +23.67% |
| Average slot time (ms) | 216.30 | 203.00 | -6.15% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 5.00 | 27.00 | +440.00% |
| Solana TVL | 4,761,137,008.00 | 4,568,842,954.00 | -4.04% |
| SOL price | 74.98 | 69.29 | -7.59% |
| Stablecoin supply | 14,334,785,302.00 | 13,518,061,358.00 | -5.70% |
| 24h DEX volume | 1,479,924,560.31 | 1,652,785,326.76 | +11.68% |
| 24h chain fees | 8,328,289.41 | 7,654,322.42 | -8.09% |

### Change over 30d (vs run at 2026-10-25T20:04:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,732.39 | 2,306.02 | +33.11% |
| Average non-vote TPS | 1,732.38 | 2,306.02 | +33.11% |
| Average slot time (ms) | 212.20 | 203.00 | -4.34% |
| Active validators | 665.00 | 660.00 | -0.75% |
| Delinquent validators | 25.00 | 27.00 | +8.00% |
| Solana TVL | 5,770,053,619.00 | 4,568,842,954.00 | -20.82% |
| SOL price | 101.63 | 69.29 | -31.82% |
| Stablecoin supply | 15,930,366,369.00 | 13,518,061,358.00 | -15.14% |
| 24h DEX volume | 1,423,041,369.80 | 1,652,785,326.76 | +16.14% |
| 24h chain fees | 10,045,733.76 | 7,654,322.42 | -23.81% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
