# Solana Ecosystem Pulse

**Generated:** 2026-11-18T00:06:11Z · **Schema:** `1.0.0` · **Collection time:** 19.0s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $74.98 | +5.04% |
| Market cap | $44.37B | rank #7 |
| Total value locked | $4.76B | +1.23% |
| Stablecoin supply | $14.33B | -0.05% |
| DEX volume (24h) | $1.48B | +9.42% |
| Chain fees / REV (24h) | $8.33M | +16.23% |
| Non-vote TPS (1h avg) | 1,865 | peak 2,733 total |
| Active validators | 661 | 5 delinquent |
| Epoch 1089 | 64.86% complete | 151,788 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 131 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,864.6 average over the last 60 minutes; 1,852.7 in the latest sample.
- **Total TPS:** 1,864.6 average, 2,732.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 216.3 ms average (target 400 ms), worst 1-minute bucket 224.7 ms.
- **Block height:** 448,742,979 at absolute slot 470,728,212.
- **Epoch 1089:** slot 280,212 of 432,000 (64.86% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.552% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 275 ms |
| `solana-rpc.publicnode.com` | yes | 127 ms |
| `api.mainnet.solana.com` | yes | 200 ms |

## Validators & stake

- **661 active** validators, **5 delinquent** (0.75% by count, 0.013% by stake).
- **Total stake:** 428,796,576 SOL ($32.15B); stake rate 67.24% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.48% of active stake.
- **Commission:** median 5.0%, mean 12.85%; 219 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,834,343 | 3.926% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,442,668 | 3.835% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,432,778 | 2.900% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,144,846 | 2.366% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,802,677 | 2.286% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,625,021 | 2.245% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,745 | 2.150% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,970,891 | 1.859% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,288 | 1.632% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,472 | 1.570% | 5% |

## Economics

- **SOL:** $74.98 (+5.04% 24h, -9.95% 7d, -27.90% 30d). Market cap $44.37B, 24h volume $3.22B (7.26% of cap). Price source: `coingecko`.
- **TVL:** $4.76B across 342 protocols - rank #3 of 424 chains, 6.69% of all tracked chain TVL. -6.32% over 7d, -60.0% from its ATH.
- **Stablecoins:** $14.33B circulating on Solana (-0.06% 7d) - $3.01 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.48B in 24h, $10.55B over 7d across 144 venues. Volume/TVL turnover 0.311x per day.
- **REV (chain fees):** $8.33M in 24h, $310.12M over 30d. Retained chain revenue $3.19M (38.3% of fees). Annualised fees are 6.85% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,739,515 SOL circulating of 637,737,764 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.39B | +3.7% | -9.5% |
| 2 | Kamino Lend | Lending | $1.15B | +1.1% | -1.7% |
| 3 | Jupiter Lend | Lending | $979.03M | +3.2% | +7.7% |
| 4 | Raydium AMM | Dexs | $803.09M | -3.4% | -17.4% |
| 5 | Binance Staked SOL | Liquid Staking | $759.45M | +3.0% | -19.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $746.51M | +2.8% | -15.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $587.75M | +1.1% | -9.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $380.50M | +2.8% | -13.7% |
| 9 | Sentora Curator | Risk Curators | $356.57M | -0.6% | -4.8% |
| 10 | Forward Industries SOL | Liquid Staking | $298.35M | +3.0% | +9.5% |
| 11 | OnRe | RWA | $293.31M | -0.9% | -5.2% |
| 12 | CCIP | Bridge | $263.30M | -4.8% | -0.5% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 342 protocols the total is $12.26B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.0% · Lending 19.0% · Dexs 14.3% · Derivatives 5.3% · RWA 4.7% · Risk Curators 4.1%

### Tokenised assets

$829.50M of tokenised real-world assets and equities are locked on Solana - 6.767% of chain TVL.

- OnRe (RWA): $293.31M
- Huma (RWA): $231.55M
- Solstice (Basis Trading): $201.04M
- JupUSD (Basis Trading): $40.11M
- Plume Vaults (RWA): $39.33M

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

### Change over 24h (vs run at 2026-11-17T01:12:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,790.21 | 1,864.62 | +4.16% |
| Average non-vote TPS | 1,790.21 | 1,864.62 | +4.16% |
| Average slot time (ms) | 214.50 | 216.30 | +0.84% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 37.00 | 5.00 | -86.49% |
| Solana TVL | 4,749,281,028.00 | 4,761,137,008.00 | +0.25% |
| SOL price | 71.58 | 74.98 | +4.75% |
| Stablecoin supply | 14,334,893,337.00 | 14,334,785,302.00 | -0.00% |
| 24h DEX volume | 1,381,573,830.86 | 1,479,924,560.31 | +7.12% |
| 24h chain fees | 7,253,029.76 | 8,328,289.41 | +14.82% |

### Change over 7d (vs run at 2026-11-10T22:36:44Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,898.72 | 1,864.62 | -1.80% |
| Average non-vote TPS | 1,898.72 | 1,864.62 | -1.80% |
| Average slot time (ms) | 214.20 | 216.30 | +0.98% |
| Active validators | 658.00 | 661.00 | +0.46% |
| Delinquent validators | 41.00 | 5.00 | -87.80% |
| Solana TVL | 5,016,904,733.00 | 4,761,137,008.00 | -5.10% |
| SOL price | 82.98 | 74.98 | -9.64% |
| Stablecoin supply | 14,833,203,510.00 | 14,334,785,302.00 | -3.36% |
| 24h DEX volume | 1,487,777,537.32 | 1,479,924,560.31 | -0.53% |
| 24h chain fees | 9,382,942.72 | 8,328,289.41 | -11.24% |

### Change over 30d (vs run at 2026-10-18T19:46:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.46 | 1,864.62 | -62.52% |
| Average non-vote TPS | 1,911.38 | 1,864.62 | -2.45% |
| Average slot time (ms) | 217.10 | 216.30 | -0.37% |
| Active validators | 668.00 | 661.00 | -1.05% |
| Delinquent validators | 12.00 | 5.00 | -58.33% |
| Solana TVL | 5,875,275,842.00 | 4,761,137,008.00 | -18.96% |
| SOL price | 100.82 | 74.98 | -25.63% |
| Stablecoin supply | 15,898,071,483.00 | 14,334,785,302.00 | -9.83% |
| 24h DEX volume | 1,252,516,756.55 | 1,479,924,560.31 | +18.16% |
| 24h chain fees | 9,375,340.79 | 8,328,289.41 | -11.17% |

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

This run made 41 HTTP calls (38 succeeded, 3 failed) in 19.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)
- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
