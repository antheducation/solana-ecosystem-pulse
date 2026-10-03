# Solana Ecosystem Pulse

**Generated:** 2026-10-03T20:17:01Z · **Schema:** `1.0.0` · **Collection time:** 16.8s · **Sources OK:** 39/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.93 | +1.59% |
| Market cap | $70.54B | rank #7 |
| Total value locked | $6.66B | +1.32% |
| Stablecoin supply | $16.95B | +2.21% |
| DEX volume (24h) | $2.76B | +10.92% |
| Chain fees / REV (24h) | $17.40M | +1.41% |
| Non-vote TPS (1h avg) | 2,415 | peak 5,450 total |
| Active validators | 670 | 15 delinquent |
| Epoch 1048 | 70.02% complete | 129,499 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 100 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,415.3 average over the last 60 minutes; 2,644.6 in the latest sample.
- **Total TPS:** 4,907.6 average, 5,450.4 peak. Consensus votes account for 50.8% of all transactions.
- **Slot time:** 267.6 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 431,077,005 at absolute slot 453,038,501.
- **Epoch 1048:** slot 302,501 of 432,000 (70.02% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.620% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 233 ms |
| `solana-rpc.publicnode.com` | yes | 93 ms |
| `api.mainnet.solana.com` | yes | 169 ms |

## Validators & stake

- **670 active** validators, **15 delinquent** (2.19% by count, 0.099% by stake).
- **Total stake:** 442,013,190 SOL ($53.01B); stake rate 69.59% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.56% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 13.04%; 225 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,923,954 | 4.059% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,898,894 | 3.601% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,401 | 2.794% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,304,108 | 2.560% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,133,145 | 2.521% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,247,324 | 2.094% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,244,926 | 2.094% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,605,153 | 1.722% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,060,361 | 1.599% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,684,213 | 1.514% | 0% |

## Economics

- **SOL:** $119.93 (+1.59% 24h, -0.97% 7d, +14.01% 30d). Market cap $70.54B, 24h volume $1.69B (2.40% of cap). Price source: `coingecko`.
- **TVL:** $6.66B across 334 protocols - rank #2 of 468 chains, 6.97% of all tracked chain TVL. +0.44% over 7d, -49.7% from its ATH.
- **Stablecoins:** $16.95B circulating on Solana (+0.84% 7d) - $2.54 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.76B in 24h, $17.10B over 7d across 126 venues. Volume/TVL turnover 0.414x per day.
- **REV (chain fees):** $17.40M in 24h, $430.10M over 30d. Retained chain revenue $6.25M (35.9% of fees). Annualised fees are 9.01% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,145,673 SOL circulating of 635,150,246 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.96B | +1.9% | -1.3% |
| 2 | Kamino Lend | Lending | $1.39B | +0.8% | -5.2% |
| 3 | Raydium AMM | Dexs | $1.35B | -0.4% | -1.4% |
| 4 | Jupiter Lend | Lending | $1.30B | +2.4% | +9.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.25B | +1.8% | -1.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.23B | +2.1% | -1.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $812.60M | +1.2% | -2.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $620.08M | +2.0% | -2.1% |
| 9 | Marinade Native | Staking Pool | $446.31M | +2.0% | -5.0% |
| 10 | PumpSwap | Dexs | $396.40M | -0.2% | +0.3% |
| 11 | Sentora Curator | Risk Curators | $380.56M | -1.9% | +5.0% |
| 12 | Drift Staked SOL | Liquid Staking | $338.80M | +2.0% | -1.8% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.61B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.91M of tokenised real-world assets and equities are locked on Solana - 5.093% of chain TVL.

- OnRe (RWA): $291.56M
- Huma (RWA): $260.16M
- Solstice (Basis Trading): $212.35M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.41M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT

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

### Change over 24h (vs run at 2026-10-02T21:29:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,922.79 | 4,907.58 | -0.31% |
| Average non-vote TPS | 2,432.94 | 2,415.29 | -0.73% |
| Average slot time (ms) | 268.50 | 267.60 | -0.34% |
| Active validators | 671.00 | 670.00 | -0.15% |
| Delinquent validators | 13.00 | 15.00 | +15.38% |
| Solana TVL | 6,606,723,520.00 | 6,664,651,516.00 | +0.88% |
| SOL price | 117.81 | 119.93 | +1.80% |
| Stablecoin supply | 16,579,831,390.00 | 16,950,775,065.00 | +2.24% |
| 24h DEX volume | 2,488,460,102.88 | 2,760,296,309.96 | +10.92% |
| 24h chain fees | 17,134,431.63 | 17,402,246.04 | +1.56% |

### Change over 7d (vs run at 2026-09-26T20:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,730.02 | 4,907.58 | +3.75% |
| Average non-vote TPS | 2,233.16 | 2,415.29 | +8.16% |
| Average slot time (ms) | 269.50 | 267.60 | -0.71% |
| Active validators | 676.00 | 670.00 | -0.89% |
| Delinquent validators | 11.00 | 15.00 | +36.36% |
| Solana TVL | 6,636,693,564.00 | 6,664,651,516.00 | +0.42% |
| SOL price | 120.95 | 119.93 | -0.84% |
| Stablecoin supply | 16,991,136,948.00 | 16,950,775,065.00 | -0.24% |
| 24h DEX volume | 2,613,053,225.63 | 2,760,296,309.96 | +5.63% |
| 24h chain fees | 15,598,587.47 | 17,402,246.04 | +11.56% |

### Change over 30d (vs run at 2026-09-03T20:12:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,437.74 | 4,907.58 | +10.59% |
| Average non-vote TPS | 2,316.58 | 2,415.29 | +4.26% |
| Average slot time (ms) | 316.10 | 267.60 | -15.34% |
| Active validators | 676.00 | 670.00 | -0.89% |
| Delinquent validators | 19.00 | 15.00 | -21.05% |
| Solana TVL | 5,969,689,229.00 | 6,664,651,516.00 | +11.64% |
| SOL price | 105.35 | 119.93 | +13.84% |
| Stablecoin supply | 16,102,283,829.00 | 16,950,775,065.00 | +5.27% |
| 24h DEX volume | 2,289,285,889.32 | 2,760,296,309.96 | +20.57% |
| 24h chain fees | 10,535,900.15 | 17,402,246.04 | +65.17% |

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

This run made 41 HTTP calls (39 succeeded, 2 failed) in 16.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
