# Solana Ecosystem Pulse

**Generated:** 2026-11-22T22:53:49Z · **Schema:** `1.0.0` · **Collection time:** 16.2s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.17 | +0.13% |
| Market cap | $41.53B | rank #7 |
| Total value locked | $4.63B | +1.17% |
| Stablecoin supply | $13.37B | +0.82% |
| DEX volume (24h) | $1.35B | -28.59% |
| Chain fees / REV (24h) | $7.59M | -8.71% |
| Non-vote TPS (1h avg) | 1,892 | peak 2,681 total |
| Active validators | 662 | 23 delinquent |
| Epoch 1094 | 24.86% complete | 324,597 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 134 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,365,903,932.00 sits 3.1 sigma below the median of the last 134 runs (15,973,982,918.00, -16.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,892.4 average over the last 60 minutes; 2,314.2 in the latest sample.
- **Total TPS:** 1,892.4 average, 2,680.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.3 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 450,728,999 at absolute slot 472,715,403.
- **Epoch 1094:** slot 107,403 of 432,000 (24.86% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.544% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 139 ms |
| `solana-rpc.publicnode.com` | yes | 42 ms |
| `api.mainnet.solana.com` | yes | 42 ms |

## Validators & stake

- **662 active** validators, **23 delinquent** (3.36% by count, 0.012% by stake).
- **Total stake:** 425,691,542 SOL ($29.87B); stake rate 66.72% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.00% and top 33 hold 46.65% of active stake.
- **Commission:** median 5.0%, mean 12.89%; 220 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,918,440 | 3.975% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,346,959 | 3.841% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,401,889 | 2.914% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,243,005 | 2.406% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,842,253 | 2.312% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,612,896 | 2.258% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,269,555 | 2.178% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,998,895 | 1.879% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,495 | 1.642% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,775,083 | 1.592% | 5% |

## Economics

- **SOL:** $70.17 (+0.13% 24h, -2.39% 7d, -32.25% 30d). Market cap $41.53B, 24h volume $1.83B (4.40% of cap). Price source: `coingecko`.
- **TVL:** $4.63B across 343 protocols - rank #4 of 426 chains, 6.62% of all tracked chain TVL. -0.26% over 7d, -61.1% from its ATH.
- **Stablecoins:** $13.37B circulating on Solana (-6.05% 7d) - $2.89 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.35B in 24h, $11.29B over 7d across 144 venues. Volume/TVL turnover 0.291x per day.
- **REV (chain fees):** $7.59M in 24h, $290.62M over 30d. Retained chain revenue $2.59M (34.2% of fees). Annualised fees are 6.67% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,016,883 SOL circulating of 638,042,480 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | -0.2% | -2.0% |
| 2 | Kamino Lend | Lending | $1.14B | -0.0% | +1.1% |
| 3 | Jupiter Lend | Lending | $956.99M | +0.1% | +5.2% |
| 4 | Raydium AMM | Dexs | $780.56M | -0.0% | -6.0% |
| 5 | Binance Staked SOL | Liquid Staking | $723.09M | +0.2% | -2.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $708.75M | -0.1% | +0.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $570.06M | +0.5% | +2.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $360.02M | -0.1% | -1.4% |
| 9 | Sentora Curator | Risk Curators | $353.24M | -0.8% | -1.5% |
| 10 | OnRe | RWA | $287.47M | +0.0% | -5.5% |
| 11 | Forward Industries SOL | Liquid Staking | $275.55M | -0.6% | -0.9% |
| 12 | CCIP | Bridge | $267.23M | -0.2% | -4.0% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.75B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.4% · Dexs 14.5% · Derivatives 5.4% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$776.66M of tokenised real-world assets and equities are locked on Solana - 6.609% of chain TVL.

- OnRe (RWA): $287.47M
- Huma (RWA): $225.32M
- Solstice (Basis Trading): $200.98M
- JupUSD (Basis Trading): $39.44M
- Solomon USDv (Basis Trading): $8.72M

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

### Change over 24h (vs run at 2026-11-21T22:30:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,844.50 | 1,892.44 | +2.60% |
| Average non-vote TPS | 1,844.50 | 1,892.44 | +2.60% |
| Average slot time (ms) | 215.40 | 215.30 | -0.05% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 24.00 | 23.00 | -4.17% |
| Solana TVL | 4,634,019,893.00 | 4,630,499,032.00 | -0.08% |
| SOL price | 70.20 | 70.17 | -0.04% |
| Stablecoin supply | 13,256,078,315.00 | 13,365,903,932.00 | +0.83% |
| 24h DEX volume | 1,884,688,072.35 | 1,345,931,988.87 | -28.59% |
| 24h chain fees | 8,298,729.06 | 7,588,213.38 | -8.56% |

### Change over 7d (vs run at 2026-11-15T22:11:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,936.81 | 1,892.44 | -2.29% |
| Average non-vote TPS | 1,936.81 | 1,892.44 | -2.29% |
| Average slot time (ms) | 214.60 | 215.30 | +0.33% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 38.00 | 23.00 | -39.47% |
| Solana TVL | 4,706,449,733.00 | 4,630,499,032.00 | -1.61% |
| SOL price | 72.09 | 70.17 | -2.66% |
| Stablecoin supply | 14,224,861,314.00 | 13,365,903,932.00 | -6.04% |
| 24h DEX volume | 1,677,928,733.70 | 1,345,931,988.87 | -19.79% |
| 24h chain fees | 7,947,344.14 | 7,588,213.38 | -4.52% |

### Change over 30d (vs run at 2026-10-23T20:43:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,163.30 | 1,892.44 | -12.52% |
| Average non-vote TPS | 2,163.30 | 1,892.44 | -12.52% |
| Average slot time (ms) | 212.20 | 215.30 | +1.46% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 14.00 | 23.00 | +64.29% |
| Solana TVL | 5,856,286,188.00 | 4,630,499,032.00 | -20.93% |
| SOL price | 103.58 | 70.17 | -32.26% |
| Stablecoin supply | 15,965,866,149.00 | 13,365,903,932.00 | -16.28% |
| 24h DEX volume | 2,039,384,832.23 | 1,345,931,988.87 | -34.00% |
| 24h chain fees | 11,472,475.22 | 7,588,213.38 | -33.86% |

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

This run made 41 HTTP calls (38 succeeded, 3 failed) in 16.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)
- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
