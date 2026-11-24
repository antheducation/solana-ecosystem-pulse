# Solana Ecosystem Pulse

**Generated:** 2026-11-24T16:36:28Z · **Schema:** `1.0.0` · **Collection time:** 18.8s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $68.97 | -7.97% |
| Market cap | $40.83B | rank #7 |
| Total value locked | $4.57B | -1.78% |
| Stablecoin supply | $13.89B | +3.60% |
| DEX volume (24h) | $1.81B | +85.09% |
| Chain fees / REV (24h) | $8.46M | +43.17% |
| Non-vote TPS (1h avg) | 2,986 | peak 13,489 total |
| Active validators | 661 | 25 delinquent |
| Epoch 1095 | 86.49% complete | 58,377 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | DEX volume moved sharply (up 85.1% in 24h) | DEX volume changed +85.1% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.6% in 24h) | Stablecoin supply changed +3.6% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 43.2% in 24h) | Chain fees changed +43.2% over the last day, past the 40% alert band. | `threshold` |
| [INFO] | Throughput spike inside the sample window | Peak TPS 13,489 is 4.5x the window average (2,986) - a burst, not a steady load. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,985.7 average over the last 60 minutes; 2,548.1 in the latest sample.
- **Total TPS:** 2,985.7 average, 13,489.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 205.3 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 451,426,749 at absolute slot 473,413,623.
- **Epoch 1095:** slot 373,623 of 432,000 (86.49% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.543% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 206 ms |
| `solana-rpc.publicnode.com` | yes | 134 ms |
| `api.mainnet.solana.com` | yes | 149 ms |

## Validators & stake

- **661 active** validators, **25 delinquent** (3.64% by count, 0.012% by stake).
- **Total stake:** 425,856,004 SOL ($29.37B); stake rate 66.74% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.97% and top 33 hold 46.67% of active stake.
- **Commission:** median 5.0%, mean 13.07%; 219 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,046 | 3.999% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,091,420 | 3.779% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,158 | 2.915% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,240,508 | 2.405% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,856,366 | 2.315% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,634,022 | 2.263% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,276,354 | 2.179% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,005,660 | 1.880% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,776 | 1.641% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,778,434 | 1.592% | 5% |

## Economics

- **SOL:** $68.97 (-7.97% 24h, -4.75% 7d, -32.07% 30d). Market cap $40.83B, 24h volume $2.91B (7.12% of cap). Price source: `coingecko`.
- **TVL:** $4.57B across 342 protocols - rank #3 of 426 chains, 6.65% of all tracked chain TVL. -3.69% over 7d, -61.6% from its ATH.
- **Stablecoins:** $13.89B circulating on Solana (-3.11% 7d) - $3.04 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.81B in 24h, $11.24B over 7d across 145 venues. Volume/TVL turnover 0.396x per day.
- **REV (chain fees):** $8.46M in 24h, $282.89M over 30d. Retained chain revenue $3.33M (39.4% of fees). Annualised fees are 7.56% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,071,588 SOL circulating of 638,102,970 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.27B | -8.1% | -4.7% |
| 2 | Kamino Lend | Lending | $1.10B | -5.0% | -3.2% |
| 3 | Jupiter Lend | Lending | $942.15M | -5.3% | -1.4% |
| 4 | Raydium AMM | Dexs | $767.89M | -4.3% | -7.6% |
| 5 | Binance Staked SOL | Liquid Staking | $707.18M | -9.8% | -4.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $694.01M | -9.9% | -4.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $565.69M | -6.1% | -2.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $359.59M | -9.0% | -2.4% |
| 9 | Sentora Curator | Risk Curators | $354.07M | +0.0% | -1.3% |
| 10 | OnRe | RWA | $289.81M | +0.1% | -2.0% |
| 11 | Forward Industries SOL | Liquid Staking | $270.54M | -9.8% | -6.2% |
| 12 | CCIP | Bridge | $267.40M | +1.4% | -2.8% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 342 protocols the total is $11.61B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.1% · Lending 19.2% · Dexs 14.6% · Derivatives 5.4% · RWA 4.7% · Risk Curators 4.2%

### Tokenised assets

$794.29M of tokenised real-world assets and equities are locked on Solana - 6.842% of chain TVL.

- OnRe (RWA): $289.81M
- Huma (RWA): $242.45M
- Solstice (Basis Trading): $201.06M
- JupUSD (Basis Trading): $36.83M
- Solomon USDv (Basis Trading): $8.74M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

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

### Change over 24h (vs run at 2026-11-23T16:40:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,781.90 | 2,985.71 | +7.33% |
| Average non-vote TPS | 2,781.90 | 2,985.71 | +7.33% |
| Average slot time (ms) | 215.10 | 205.30 | -4.56% |
| Active validators | 659.00 | 661.00 | +0.30% |
| Delinquent validators | 26.00 | 25.00 | -3.85% |
| Solana TVL | 4,802,924,182.00 | 4,565,087,427.00 | -4.95% |
| SOL price | 74.68 | 68.97 | -7.65% |
| Stablecoin supply | 13,408,007,454.00 | 13,889,158,688.00 | +3.59% |
| 24h DEX volume | 975,738,121.97 | 1,805,966,413.26 | +85.09% |
| 24h chain fees | 5,919,028.93 | 8,461,387.38 | +42.95% |

### Change over 7d (vs run at 2026-11-17T15:00:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,920.75 | 2,985.71 | +55.45% |
| Average non-vote TPS | 1,920.75 | 2,985.71 | +55.45% |
| Average slot time (ms) | 215.30 | 205.30 | -4.64% |
| Active validators | 661.00 | 661.00 | +0.00% |
| Delinquent validators | 5.00 | 25.00 | +400.00% |
| Solana TVL | 4,802,561,637.00 | 4,565,087,427.00 | -4.94% |
| SOL price | 73.69 | 68.97 | -6.41% |
| Stablecoin supply | 14,334,215,667.00 | 13,889,158,688.00 | -3.10% |
| 24h DEX volume | 1,479,923,822.31 | 1,805,966,413.26 | +22.03% |
| 24h chain fees | 8,328,280.55 | 8,461,387.38 | +1.60% |

### Change over 30d (vs run at 2026-10-25T20:04:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,732.39 | 2,985.71 | +72.35% |
| Average non-vote TPS | 1,732.38 | 2,985.71 | +72.35% |
| Average slot time (ms) | 212.20 | 205.30 | -3.25% |
| Active validators | 665.00 | 661.00 | -0.60% |
| Delinquent validators | 25.00 | 25.00 | +0.00% |
| Solana TVL | 5,770,053,619.00 | 4,565,087,427.00 | -20.88% |
| SOL price | 101.63 | 68.97 | -32.14% |
| Stablecoin supply | 15,930,366,369.00 | 13,889,158,688.00 | -12.81% |
| 24h DEX volume | 1,423,041,369.80 | 1,805,966,413.26 | +26.91% |
| 24h chain fees | 10,045,733.76 | 8,461,387.38 | -15.77% |

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

This run made 41 HTTP calls (38 succeeded, 3 failed) in 18.8s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)
- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
