# Solana Ecosystem Pulse

**Generated:** 2026-11-27T01:13:08Z · **Schema:** `1.0.0` · **Collection time:** 21.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.32 | +0.58% |
| Market cap | $42.24B | rank #7 |
| Total value locked | $4.65B | -0.00% |
| Stablecoin supply | $12.69B | -4.84% |
| DEX volume (24h) | $1.26B | -16.71% |
| Chain fees / REV (24h) | $6.86M | -3.73% |
| Non-vote TPS (1h avg) | 1,474 | peak 2,130 total |
| Active validators | 654 | 34 delinquent |
| Epoch 1098 | 5.92% complete | 406,418 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,474; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 4.8% in 24h) | Stablecoin supply changed -4.8% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 12,690,450,207.00 sits 3.7 sigma below the median of the last 136 runs (15,967,932,747.50, -20.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,474.4 average over the last 60 minutes; 1,541.3 in the latest sample.
- **Total TPS:** 1,474.4 average, 2,129.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.4 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 452,374,350 at absolute slot 474,361,582.
- **Epoch 1098:** slot 25,582 of 432,000 (5.92% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.538% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 167 ms |
| `solana-rpc.publicnode.com` | yes | 113 ms |
| `api.mainnet.solana.com` | yes | 221 ms |

## Validators & stake

- **654 active** validators, **34 delinquent** (4.94% by count, 0.060% by stake).
- **Total stake:** 424,207,451 SOL ($30.25B); stake rate 66.46% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.98% and top 33 hold 46.62% of active stake.
- **Commission:** median 5.0%, mean 12.99%; 218 validators at 0% and 62 at 100%.

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

- **SOL:** $71.32 (+0.58% 24h, -2.19% 7d, -29.48% 30d). Market cap $42.24B, 24h volume $1.64B (3.89% of cap). Price source: `coingecko`.
- **TVL:** $4.65B across 345 protocols - rank #3 of 426 chains, 6.80% of all tracked chain TVL. -1.90% over 7d, -60.9% from its ATH.
- **Stablecoins:** $12.69B circulating on Solana (-5.66% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.26B in 24h, $9.31B over 7d across 146 venues. Volume/TVL turnover 0.271x per day.
- **REV (chain fees):** $6.86M in 24h, $265.14M over 30d. Retained chain revenue $2.65M (38.6% of fees). Annualised fees are 5.93% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,238,448 SOL circulating of 638,285,689 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.26B | +0.2% | -6.6% |
| 2 | Kamino Lend | Lending | $1.12B | +1.0% | -2.2% |
| 3 | Jupiter Lend | Lending | $965.08M | +2.1% | -0.2% |
| 4 | Raydium AMM | Dexs | $794.87M | +0.9% | -1.7% |
| 5 | Binance Staked SOL | Liquid Staking | $730.09M | +0.9% | -2.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $714.81M | +0.7% | -2.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $568.21M | -0.6% | -2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $372.64M | +0.2% | +0.2% |
| 9 | Sentora Curator | Risk Curators | $356.88M | +0.1% | -0.0% |
| 10 | OnRe | RWA | $290.09M | +0.0% | -0.6% |
| 11 | Forward Industries SOL | Liquid Staking | $279.32M | +0.0% | -2.9% |
| 12 | CCIP | Bridge | $268.60M | +0.3% | -1.5% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 345 protocols the total is $11.75B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 39.9% · Lending 19.3% · Dexs 14.7% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.2%

### Tokenised assets

$796.95M of tokenised real-world assets and equities are locked on Solana - 6.783% of chain TVL.

- OnRe (RWA): $290.09M
- Huma (RWA): $242.58M
- Solstice (Basis Trading): $201.04M
- JupUSD (Basis Trading): $38.23M
- Solomon USDv (Basis Trading): $8.78M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | 2026-11-25 | pre-release |
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-11-26
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-26
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-26
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-25
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-26T01:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,883.14 | 1,474.38 | -21.71% |
| Average non-vote TPS | 1,883.14 | 1,474.38 | -21.71% |
| Average slot time (ms) | 215.20 | 214.40 | -0.37% |
| Active validators | 655.00 | 654.00 | -0.15% |
| Delinquent validators | 33.00 | 34.00 | +3.03% |
| Solana TVL | 4,594,999,475.00 | 4,648,654,009.00 | +1.17% |
| SOL price | 70.92 | 71.32 | +0.56% |
| Stablecoin supply | 13,335,674,953.00 | 12,690,450,207.00 | -4.84% |
| 24h DEX volume | 1,477,920,816.80 | 1,258,514,139.56 | -14.85% |
| 24h chain fees | 7,164,291.62 | 6,861,662.16 | -4.22% |

### Change over 7d (vs run at 2026-11-19T23:57:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,928.85 | 1,474.38 | -23.56% |
| Average non-vote TPS | 1,928.85 | 1,474.38 | -23.56% |
| Average slot time (ms) | 215.70 | 214.40 | -0.60% |
| Active validators | 659.00 | 654.00 | -0.76% |
| Delinquent validators | 26.00 | 34.00 | +30.77% |
| Solana TVL | 4,721,393,649.00 | 4,648,654,009.00 | -1.54% |
| SOL price | 73.08 | 71.32 | -2.41% |
| Stablecoin supply | 13,055,005,144.00 | 12,690,450,207.00 | -2.79% |
| 24h DEX volume | 1,815,395,819.31 | 1,258,514,139.56 | -30.68% |
| 24h chain fees | 10,954,885.63 | 6,861,662.16 | -37.36% |

### Change over 30d (vs run at 2026-10-27T21:31:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,359.98 | 1,474.38 | -37.53% |
| Average non-vote TPS | 2,359.97 | 1,474.38 | -37.53% |
| Average slot time (ms) | 213.80 | 214.40 | +0.28% |
| Active validators | 665.00 | 654.00 | -1.65% |
| Delinquent validators | 20.00 | 34.00 | +70.00% |
| Solana TVL | 5,721,042,380.00 | 4,648,654,009.00 | -18.74% |
| SOL price | 100.85 | 71.32 | -29.28% |
| Stablecoin supply | 15,763,185,048.00 | 12,690,450,207.00 | -19.49% |
| 24h DEX volume | 2,071,067,618.21 | 1,258,514,139.56 | -39.23% |
| 24h chain fees | 11,672,734.12 | 6,861,662.16 | -41.22% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.9s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
