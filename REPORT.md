# Solana Ecosystem Pulse

**Generated:** 2026-08-21T06:22:52Z · **Schema:** `1.0.0` · **Collection time:** 21.3s · **Sources OK:** 33/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $90.54 | +6.63% |
| Market cap | $52.82B | rank #7 |
| Total value locked | $5.37B | +2.80% |
| Stablecoin supply | $16.52B | +1.15% |
| DEX volume (24h) | $2.78B | -7.60% |
| Chain fees / REV (24h) | $11.03M | -19.33% |
| Non-vote TPS (1h avg) | 1,668 | peak 3,794 total |
| Active validators | 690 | 6 delinquent |
| Epoch 1019 | 97.21% complete | 12,055 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 58 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,372,223,613.00 sits 14.1 sigma above the median of the last 58 runs (4,825,543,190.50, +11.3%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 90.54 sits 17.9 sigma above the median of the last 58 runs (75.84, +19.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | 24h DEX volume is above its recent norm | Current 2,781,215,932.33 sits 4.9 sigma above the median of the last 58 runs (1,536,821,446.13, +81.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,667.8 average over the last 60 minutes; 1,590.2 in the latest sample.
- **Total TPS:** 3,313.6 average, 3,794.4 peak. Consensus votes account for 49.7% of all transactions.
- **Slot time:** 416.6 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,677,652 at absolute slot 440,627,945.
- **Epoch 1019:** slot 419,945 of 432,000 (97.21% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 260 ms |
| `solana-rpc.publicnode.com` | yes | 93 ms |
| `api.mainnet.solana.com` | yes | 131 ms |

## Validators & stake

- **690 active** validators, **6 delinquent** (0.86% by count, 0.001% by stake).
- **Total stake:** 435,241,268 SOL ($39.41B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.27%; 256 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.929% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.679% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.851% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.803% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.111% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.066% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.909% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.836% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.688% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.504% | 0% |

## Economics

- **SOL:** $90.54 (+6.63% 24h, +19.47% 7d, +16.97% 30d). Market cap $52.82B, 24h volume $5.00B (9.47% of cap). Price source: `coingecko`.
- **TVL:** $5.37B across 328 protocols - rank #3 of 461 chains, 6.32% of all tracked chain TVL. +11.06% over 7d, -59.4% from its ATH.
- **Stablecoins:** $16.52B circulating on Solana (+2.59% 7d) - $3.07 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.78B in 24h, $12.57B over 7d across 119 venues. Volume/TVL turnover 0.518x per day.
- **REV (chain fees):** $11.03M in 24h, $261.52M over 30d. Retained chain revenue $5.23M (47.4% of fees). Annualised fees are 7.62% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,063,108 SOL circulating of 632,512,916 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.33B | +5.1% | +17.3% |
| 2 | Kamino Lend | Lending | $1.15B | +2.6% | +10.0% |
| 3 | Jupiter Lend | Lending | $1.04B | +3.4% | +12.2% |
| 4 | Raydium AMM | Dexs | $982.52M | +5.3% | +15.6% |
| 5 | Binance Staked SOL | Liquid Staking | $906.63M | +5.8% | +16.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $893.86M | +5.2% | +17.5% |
| 7 | BlackRock BUIDL | RWA | $740.67M | +0.0% | -0.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $734.79M | +0.7% | +6.5% |
| 9 | Solstice | Basis Trading | $506.15M | -0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $464.18M | +5.4% | +17.5% |
| 11 | xStocks | RWA | $410.92M | +1.8% | +7.1% |
| 12 | Sentora | Risk Curators | $365.07M | -0.1% | -0.9% |

The top five protocols hold 36.3% of Solana's tracked TVL. Summed across all 328 protocols the total is $14.92B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 34.6% · Lending 16.5% · Dexs 13.8% · RWA 12.8% · Derivatives 5.5% · Basis Trading 3.9%

### Tokenised assets

$2.49B of tokenised real-world assets and equities are locked on Solana - 16.695% of chain TVL.

- BlackRock BUIDL (RWA): $740.67M
- Solstice (Basis Trading): $506.15M
- xStocks (RWA): $410.92M
- OnRe (RWA): $272.73M
- Ondo Yield Assets (RWA): $178.21M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **989.0 unique fee payers** signed per block (1,442 distinct addresses in the union, 51.4% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT

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

### Change over 24h (vs run at 2026-08-20T06:22:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,047.31 | 3,313.55 | +8.74% |
| Average non-vote TPS | 1,404.08 | 1,667.75 | +18.78% |
| Average slot time (ms) | 416.00 | 416.60 | +0.14% |
| Active validators | 688.00 | 690.00 | +0.29% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 5,198,850,712.00 | 5,372,223,613.00 | +3.33% |
| SOL price | 84.84 | 90.54 | +6.72% |
| Stablecoin supply | 16,322,645,608.00 | 16,515,048,692.00 | +1.18% |
| 24h DEX volume | 2,789,524,387.95 | 2,781,215,932.33 | -0.30% |
| 24h chain fees | 13,172,440.83 | 11,033,466.08 | -16.24% |

### Change over 7d (vs run at 2026-08-14T07:03:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,039.98 | 3,313.55 | +9.00% |
| Average non-vote TPS | 1,398.69 | 1,667.75 | +19.24% |
| Average slot time (ms) | 416.00 | 416.60 | +0.14% |
| Active validators | 688.00 | 690.00 | +0.29% |
| Delinquent validators | 9.00 | 6.00 | -33.33% |
| Solana TVL | 4,836,509,599.00 | 5,372,223,613.00 | +11.08% |
| SOL price | 75.45 | 90.54 | +20.00% |
| Stablecoin supply | 16,096,706,018.00 | 16,515,048,692.00 | +2.60% |
| 24h DEX volume | 1,978,176,047.75 | 2,781,215,932.33 | +40.59% |
| 24h chain fees | 10,092,794.92 | 11,033,466.08 | +9.32% |

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

This run made 35 HTTP calls (33 succeeded, 2 failed) in 21.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
