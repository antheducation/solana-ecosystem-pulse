# Solana Ecosystem Pulse

**Generated:** 2026-09-27T02:09:06Z · **Schema:** `1.0.0` · **Collection time:** 14.3s · **Sources OK:** 39/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $121.31 | -0.62% |
| Market cap | $71.29B | rank #7 |
| Total value locked | $6.63B | -0.07% |
| Stablecoin supply | $16.80B | -1.10% |
| DEX volume (24h) | $2.35B | -10.06% |
| Chain fees / REV (24h) | $18.30M | +17.37% |
| Non-vote TPS (1h avg) | 1,988 | peak 5,013 total |
| Active validators | 673 | 14 delinquent |
| Epoch 1043 | 65.33% complete | 149,793 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 94 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,988.2 average over the last 60 minutes; 2,308.7 in the latest sample.
- **Total TPS:** 4,487.8 average, 5,013.4 peak. Consensus votes account for 55.7% of all transactions.
- **Slot time:** 268.2 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 428,897,934 at absolute slot 450,858,207.
- **Epoch 1043:** slot 282,207 of 432,000 (65.33% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.630% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 157 ms |
| `solana-rpc.publicnode.com` | yes | 149 ms |
| `api.mainnet.solana.com` | yes | 207 ms |

## Validators & stake

- **673 active** validators, **14 delinquent** (2.04% by count, 0.181% by stake).
- **Total stake:** 437,542,654 SOL ($53.08B); stake rate 68.93% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.66% and top 33 hold 45.73% of active stake.
- **Commission:** median 5.0%, mean 12.94%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,860,284 | 4.089% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,799,204 | 3.617% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,343,056 | 2.826% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,222,561 | 2.570% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,836,562 | 2.481% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,102 | 2.115% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,182,742 | 2.103% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,606,181 | 1.742% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,093,311 | 1.624% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,506,505 | 1.490% | 0% |

## Economics

- **SOL:** $121.31 (-0.62% 24h, +10.19% 7d, +12.46% 30d). Market cap $71.29B, 24h volume $2.87B (4.02% of cap). Price source: `coingecko`.
- **TVL:** $6.63B across 331 protocols - rank #2 of 467 chains, 6.94% of all tracked chain TVL. +7.32% over 7d, -49.9% from its ATH.
- **Stablecoins:** $16.80B circulating on Solana (+6.32% 7d) - $2.54 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.35B in 24h, $18.37B over 7d across 126 venues. Volume/TVL turnover 0.355x per day.
- **REV (chain fees):** $18.30M in 24h, $418.10M over 30d. Retained chain revenue $7.13M (39.0% of fees). Annualised fees are 9.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,712,173 SOL circulating of 634,763,376 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.97B | -0.9% | +11.5% |
| 2 | Kamino Lend | Lending | $1.47B | -0.3% | +6.2% |
| 3 | Raydium AMM | Dexs | $1.36B | -0.2% | +9.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.26B | -0.9% | +9.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.24B | -1.0% | +7.7% |
| 6 | Jupiter Lend | Lending | $1.18B | -0.4% | +5.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $825.63M | -0.5% | +4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $627.13M | -1.0% | +9.7% |
| 9 | Marinade Native | Staking Pool | $466.65M | -0.7% | +10.3% |
| 10 | PumpSwap | Dexs | $402.38M | +1.0% | +13.8% |
| 11 | Sentora Curator | Risk Curators | $362.60M | +0.1% | -0.6% |
| 12 | Drift Staked SOL | Liquid Staking | $341.24M | -1.1% | +9.3% |

The top five protocols hold 42.4% of Solana's tracked TVL. Summed across all 331 protocols the total is $17.21B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.1% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$836.51M of tokenised real-world assets and equities are locked on Solana - 4.861% of chain TVL.

- OnRe (RWA): $296.76M
- Solstice (Basis Trading): $216.16M
- Huma (RWA): $209.72M
- JupUSD (Basis Trading): $44.05M
- Plume Vaults (RWA): $25.46M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT

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

### Change over 24h (vs run at 2026-09-26T02:15:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,172.85 | 4,487.76 | -13.24% |
| Average non-vote TPS | 2,689.69 | 1,988.22 | -26.08% |
| Average slot time (ms) | 270.50 | 268.20 | -0.85% |
| Active validators | 675.00 | 673.00 | -0.30% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 6,640,595,779.00 | 6,628,203,292.00 | -0.19% |
| SOL price | 122.14 | 121.31 | -0.68% |
| Stablecoin supply | 16,991,284,619.00 | 16,803,934,871.00 | -1.10% |
| 24h DEX volume | 2,800,186,102.63 | 2,350,289,556.23 | -16.07% |
| 24h chain fees | 14,941,402.71 | 18,302,413.77 | +22.49% |

### Change over 7d (vs run at 2026-09-20T01:58:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,136.77 | 4,487.76 | +8.48% |
| Average non-vote TPS | 1,601.78 | 1,988.22 | +24.13% |
| Average slot time (ms) | 266.40 | 268.20 | +0.68% |
| Active validators | 678.00 | 673.00 | -0.74% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 6,172,970,932.00 | 6,628,203,292.00 | +7.37% |
| SOL price | 110.06 | 121.31 | +10.22% |
| Stablecoin supply | 15,802,339,067.00 | 16,803,934,871.00 | +6.34% |
| 24h DEX volume | 3,233,773,154.20 | 2,350,289,556.23 | -27.32% |
| 24h chain fees | 16,246,928.52 | 18,302,413.77 | +12.65% |

### Change over 30d (vs run at 2026-08-27T16:57:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,739.80 | 4,487.76 | -5.32% |
| Average non-vote TPS | 2,877.86 | 1,988.22 | -30.91% |
| Average slot time (ms) | 367.20 | 268.20 | -26.96% |
| Active validators | 685.00 | 673.00 | -1.75% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 5,971,320,873.00 | 6,628,203,292.00 | +11.00% |
| SOL price | 109.05 | 121.31 | +11.24% |
| Stablecoin supply | 16,295,559,951.00 | 16,803,934,871.00 | +3.12% |
| 24h DEX volume | 2,351,677,355.00 | 2,350,289,556.23 | -0.06% |
| 24h chain fees | 15,169,688.78 | 18,302,413.77 | +20.65% |

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

This run made 41 HTTP calls (39 succeeded, 2 failed) in 14.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
