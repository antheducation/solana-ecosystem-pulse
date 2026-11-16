# Solana Ecosystem Pulse

**Generated:** 2026-11-16T14:07:40Z · **Schema:** `1.0.0` · **Collection time:** 19.1s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.75 | -2.07% |
| Market cap | $41.86B | rank #7 |
| Total value locked | $4.70B | +0.96% |
| Stablecoin supply | $14.34B | +0.81% |
| DEX volume (24h) | $1.35B | -20.09% |
| Chain fees / REV (24h) | $7.20M | -9.54% |
| Non-vote TPS (1h avg) | 1,537 | peak 2,072 total |
| Active validators | 662 | 37 delinquent |
| Epoch 1088 | 33.16% complete | 288,731 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,536.8 average over the last 60 minutes; 1,643.9 in the latest sample.
- **Total TPS:** 1,536.8 average, 2,071.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.9 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 448,174,153 at absolute slot 470,159,269.
- **Epoch 1088:** slot 143,269 of 432,000 (33.16% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.554% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 193 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 217 ms |

## Validators & stake

- **662 active** validators, **37 delinquent** (5.29% by count, 0.035% by stake).
- **Total stake:** 429,145,034 SOL ($30.36B); stake rate 67.30% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.49% of active stake.
- **Commission:** median 5.0%, mean 12.63%; 221 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,936,855 | 3.948% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,432,361 | 3.830% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,687 | 2.911% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,142,842 | 2.364% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,787,748 | 2.282% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,620,150 | 2.242% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,212,350 | 2.147% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,959,108 | 1.855% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,992,227 | 1.630% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,709,566 | 1.564% | 5% |

## Economics

- **SOL:** $70.75 (-2.07% 24h, -18.40% 7d, -31.91% 30d). Market cap $41.86B, 24h volume $2.72B (6.49% of cap). Price source: `coingecko`.
- **TVL:** $4.70B across 342 protocols - rank #3 of 423 chains, 6.61% of all tracked chain TVL. -8.36% over 7d, -60.5% from its ATH.
- **Stablecoins:** $14.34B circulating on Solana (-1.26% 7d) - $3.05 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.35B in 24h, $10.55B over 7d across 142 venues. Volume/TVL turnover 0.288x per day.
- **REV (chain fees):** $7.20M in 24h, $312.32M over 30d. Retained chain revenue $2.56M (35.5% of fees). Annualised fees are 6.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,684,465 SOL circulating of 637,676,951 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.33B | -2.7% | -13.5% |
| 2 | Kamino Lend | Lending | $1.13B | -0.5% | -3.6% |
| 3 | Jupiter Lend | Lending | $937.67M | +0.6% | +3.2% |
| 4 | Raydium AMM | Dexs | $825.75M | -1.9% | -16.2% |
| 5 | Binance Staked SOL | Liquid Staking | $731.07M | -4.1% | -23.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $716.48M | -3.0% | -19.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $568.35M | -2.3% | -12.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $366.65M | -2.7% | -17.7% |
| 9 | Sentora Curator | Risk Curators | $358.19M | +0.1% | -4.3% |
| 10 | OnRe | RWA | $303.06M | -0.1% | -2.0% |
| 11 | Forward Industries SOL | Liquid Staking | $289.47M | -1.5% | +5.6% |
| 12 | CCIP | Bridge | $277.50M | -0.3% | +4.6% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 342 protocols the total is $12.01B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 18.9% · Dexs 14.8% · Derivatives 5.2% · RWA 4.9% · Risk Curators 4.0%

### Tokenised assets

$844.48M of tokenised real-world assets and equities are locked on Solana - 7.032% of chain TVL.

- OnRe (RWA): $303.06M
- Huma (RWA): $236.48M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $40.25M
- Plume Vaults (RWA): $37.52M

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

### Change over 24h (vs run at 2026-11-15T13:02:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,228.19 | 1,536.76 | +25.12% |
| Average non-vote TPS | 1,228.19 | 1,536.76 | +25.12% |
| Average slot time (ms) | 214.30 | 214.90 | +0.28% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 38.00 | 37.00 | -2.63% |
| Solana TVL | 4,718,587,563.00 | 4,696,110,297.00 | -0.48% |
| SOL price | 72.84 | 70.75 | -2.87% |
| Stablecoin supply | 14,225,356,442.00 | 14,341,479,831.00 | +0.82% |
| 24h DEX volume | 1,692,508,944.70 | 1,352,559,060.09 | -20.09% |
| 24h chain fees | 7,874,648.14 | 7,199,120.53 | -8.58% |

### Change over 7d (vs run at 2026-11-09T14:31:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,665.74 | 1,536.76 | -7.74% |
| Average non-vote TPS | 1,665.74 | 1,536.76 | -7.74% |
| Average slot time (ms) | 214.30 | 214.90 | +0.28% |
| Active validators | 663.00 | 662.00 | -0.15% |
| Delinquent validators | 34.00 | 37.00 | +8.82% |
| Solana TVL | 5,081,946,678.00 | 4,696,110,297.00 | -7.59% |
| SOL price | 86.96 | 70.75 | -18.64% |
| Stablecoin supply | 15,065,947,064.00 | 14,341,479,831.00 | -4.81% |
| 24h DEX volume | 1,043,374,478.30 | 1,352,559,060.09 | +29.63% |
| 24h chain fees | 8,307,454.36 | 7,199,120.53 | -13.34% |

### Change over 30d (vs run at 2026-10-17T19:45:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,823.29 | 1,536.76 | -68.14% |
| Average non-vote TPS | 1,758.64 | 1,536.76 | -12.62% |
| Average slot time (ms) | 217.70 | 214.90 | -1.29% |
| Active validators | 670.00 | 662.00 | -1.19% |
| Delinquent validators | 11.00 | 37.00 | +236.36% |
| Solana TVL | 5,922,304,891.00 | 4,696,110,297.00 | -20.70% |
| SOL price | 104.07 | 70.75 | -32.02% |
| Stablecoin supply | 16,030,558,263.00 | 14,341,479,831.00 | -10.54% |
| 24h DEX volume | 2,168,129,752.12 | 1,352,559,060.09 | -37.62% |
| 24h chain fees | 12,431,928.33 | 7,199,120.53 | -42.09% |

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
