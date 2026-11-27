# Solana Ecosystem Pulse

**Generated:** 2026-11-27T15:42:51Z · **Schema:** `1.0.0` · **Collection time:** 20.2s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $72.06 | +1.98% |
| Market cap | $42.67B | rank #7 |
| Total value locked | $4.68B | +1.24% |
| Stablecoin supply | $12.69B | -4.83% |
| DEX volume (24h) | $870.58M | -42.38% |
| Chain fees / REV (24h) | $6.15M | -13.95% |
| Non-vote TPS (1h avg) | 2,542 | peak 4,098 total |
| Active validators | 654 | 34 delinquent |
| Epoch 1098 | 62.15% complete | 163,497 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 4.8% in 24h) | Stablecoin supply changed -4.8% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 42.4% in 24h) | DEX volume changed -42.4% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 12,691,672,190.00 sits 3.7 sigma below the median of the last 136 runs (15,967,932,747.50, -20.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,542.1 average over the last 60 minutes; 1,678.8 in the latest sample.
- **Total TPS:** 2,542.1 average, 4,098.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 452,617,166 at absolute slot 474,604,503.
- **Epoch 1098:** slot 268,503 of 432,000 (62.15% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.538% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 106 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 120 ms |

## Validators & stake

- **654 active** validators, **34 delinquent** (4.94% by count, 0.060% by stake).
- **Total stake:** 424,207,451 SOL ($30.57B); stake rate 66.46% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.98% and top 33 hold 46.62% of active stake.
- **Commission:** median 5.0%, mean 13.15%; 216 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,245 | 3.966% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,826,052 | 3.733% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,437,388 | 2.934% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,238,108 | 2.415% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,920,637 | 2.340% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,617,109 | 2.268% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,296,651 | 2.193% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,037,877 | 1.896% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,972,141 | 1.645% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,741,351 | 1.590% | 5% |

## Economics

- **SOL:** $72.06 (+1.98% 24h, +1.57% 7d, -28.51% 30d). Market cap $42.67B, 24h volume $2.59B (6.06% of cap). Price source: `coingecko`.
- **TVL:** $4.68B across 345 protocols - rank #3 of 426 chains, 6.75% of all tracked chain TVL. -1.54% over 7d, -60.8% from its ATH.
- **Stablecoins:** $12.69B circulating on Solana (-5.65% 7d) - $2.71 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $870.58M in 24h, $9.85B over 7d across 146 venues. Volume/TVL turnover 0.186x per day.
- **REV (chain fees):** $6.15M in 24h, $270.06M over 30d. Retained chain revenue $2.38M (38.7% of fees). Annualised fees are 5.26% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,238,223 SOL circulating of 638,285,496 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +4.4% | -3.6% |
| 2 | Kamino Lend | Lending | $1.14B | +1.8% | -0.9% |
| 3 | Jupiter Lend | Lending | $970.23M | +2.4% | +0.4% |
| 4 | Raydium AMM | Dexs | $790.74M | +0.6% | -2.2% |
| 5 | Binance Staked SOL | Liquid Staking | $755.11M | +4.4% | +0.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $735.49M | +3.8% | -0.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $579.93M | +1.4% | -0.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $376.82M | +2.1% | +1.3% |
| 9 | Sentora Curator | Risk Curators | $356.68M | +0.1% | -0.1% |
| 10 | OnRe | RWA | $290.34M | +0.1% | -0.5% |
| 11 | Forward Industries SOL | Liquid Staking | $282.53M | +0.8% | -1.8% |
| 12 | CCIP | Bridge | $268.76M | +0.3% | -1.4% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 345 protocols the total is $11.91B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.4% · Lending 19.3% · Dexs 14.4% · Derivatives 5.4% · RWA 4.5% · Risk Curators 4.2%

### Tokenised assets

$797.26M of tokenised real-world assets and equities are locked on Solana - 6.692% of chain TVL.

- OnRe (RWA): $290.34M
- Huma (RWA): $242.60M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $38.23M
- Solomon USDv (Basis Trading): $8.78M

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

### Change over 24h (vs run at 2026-11-26T15:54:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,996.59 | 2,542.14 | +27.32% |
| Average non-vote TPS | 1,996.59 | 2,542.14 | +27.32% |
| Average slot time (ms) | 216.00 | 215.20 | -0.37% |
| Active validators | 657.00 | 654.00 | -0.46% |
| Delinquent validators | 31.00 | 34.00 | +9.68% |
| Solana TVL | 4,618,435,898.00 | 4,676,136,354.00 | +1.25% |
| SOL price | 70.91 | 72.06 | +1.62% |
| Stablecoin supply | 13,335,197,886.00 | 12,691,672,190.00 | -4.83% |
| 24h DEX volume | 1,511,024,370.80 | 870,578,806.17 | -42.38% |
| 24h chain fees | 7,477,459.91 | 6,154,381.14 | -17.69% |

### Change over 7d (vs run at 2026-11-20T14:29:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,759.75 | 2,542.14 | +44.46% |
| Average non-vote TPS | 1,759.75 | 2,542.14 | +44.46% |
| Average slot time (ms) | 215.50 | 215.20 | -0.14% |
| Active validators | 661.00 | 654.00 | -1.06% |
| Delinquent validators | 24.00 | 34.00 | +41.67% |
| Solana TVL | 4,677,758,004.00 | 4,676,136,354.00 | -0.03% |
| SOL price | 71.48 | 72.06 | +0.81% |
| Stablecoin supply | 13,454,137,376.00 | 12,691,672,190.00 | -5.67% |
| 24h DEX volume | 1,904,151,628.06 | 870,578,806.17 | -54.28% |
| 24h chain fees | 9,305,684.54 | 6,154,381.14 | -33.86% |

### Change over 30d (vs run at 2026-10-28T21:57:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,155.70 | 2,542.14 | +17.93% |
| Average non-vote TPS | 2,155.70 | 2,542.14 | +17.93% |
| Average slot time (ms) | 213.60 | 215.20 | +0.75% |
| Active validators | 661.00 | 654.00 | -1.06% |
| Delinquent validators | 30.00 | 34.00 | +13.33% |
| Solana TVL | 5,748,939,504.00 | 4,676,136,354.00 | -18.66% |
| SOL price | 102.77 | 72.06 | -29.88% |
| Stablecoin supply | 15,784,667,411.00 | 12,691,672,190.00 | -19.59% |
| 24h DEX volume | 1,582,952,703.63 | 870,578,806.17 | -45.00% |
| 24h chain fees | 11,229,097.00 | 6,154,381.14 | -45.19% |

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

This run made 41 HTTP calls (38 succeeded, 3 failed) in 20.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)
- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
