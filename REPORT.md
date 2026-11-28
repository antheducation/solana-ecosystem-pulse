# Solana Ecosystem Pulse

**Generated:** 2026-11-28T00:45:54Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.71 | +0.79% |
| Market cap | $42.48B | rank #7 |
| Total value locked | $4.64B | +0.56% |
| Stablecoin supply | $12.69B | -4.83% |
| DEX volume (24h) | $885.19M | +1.68% |
| Chain fees / REV (24h) | $6.24M | +1.72% |
| Non-vote TPS (1h avg) | 1,311 | peak 1,731 total |
| Active validators | 653 | 35 delinquent |
| Epoch 1098 | 97.27% complete | 11,789 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,311; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 4.8% in 24h) | Stablecoin supply changed -4.8% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 12,691,626,832.00 sits 3.7 sigma below the median of the last 136 runs (15,967,932,747.50, -20.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,311.2 average over the last 60 minutes; 998.0 in the latest sample.
- **Total TPS:** 1,311.2 average, 1,730.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 452,768,777 at absolute slot 474,756,211.
- **Epoch 1098:** slot 420,211 of 432,000 (97.27% complete).
- **Client:** agave `4.4.2`, feature set `2681577653`. Inflation 3.538% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 178 ms |
| `solana-rpc.publicnode.com` | yes | 154 ms |
| `api.mainnet.solana.com` | yes | 109 ms |

## Validators & stake

- **653 active** validators, **35 delinquent** (5.09% by count, 0.096% by stake).
- **Total stake:** 424,207,451 SOL ($30.42B); stake rate 66.46% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.99% and top 33 hold 46.63% of active stake.
- **Commission:** median 5.0%, mean 13.17%; 215 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,245 | 3.968% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,826,052 | 3.734% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,437,388 | 2.935% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,238,108 | 2.416% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,920,637 | 2.341% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,617,109 | 2.269% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,296,651 | 2.194% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,037,877 | 1.897% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,972,141 | 1.645% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,741,351 | 1.591% | 5% |

## Economics

- **SOL:** $71.71 (+0.79% 24h, +4.30% 7d, -29.91% 30d). Market cap $42.48B, 24h volume $2.62B (6.18% of cap). Price source: `coingecko`.
- **TVL:** $4.64B across 345 protocols - rank #2 of 426 chains, 6.82% of all tracked chain TVL. -2.20% over 7d, -61.0% from its ATH.
- **Stablecoins:** $12.69B circulating on Solana (-5.65% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $885.19M in 24h, $8.32B over 7d across 146 venues. Volume/TVL turnover 0.191x per day.
- **REV (chain fees):** $6.24M in 24h, $260.71M over 30d. Retained chain revenue $2.43M (38.9% of fees). Annualised fees are 5.36% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,375,200 SOL circulating of 638,285,327 total (92.81%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.27B | +0.7% | -0.4% |
| 2 | Kamino Lend | Lending | $1.13B | +0.9% | +0.6% |
| 3 | Jupiter Lend | Lending | $959.25M | -0.6% | +1.3% |
| 4 | Raydium AMM | Dexs | $793.92M | -0.1% | +3.8% |
| 5 | Binance Staked SOL | Liquid Staking | $735.29M | +0.7% | +3.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $720.15M | +0.7% | +3.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $569.29M | +0.2% | +1.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $376.14M | +0.9% | +5.7% |
| 9 | Sentora Curator | Risk Curators | $358.40M | +0.4% | +0.8% |
| 10 | OnRe | RWA | $292.28M | +0.8% | +1.0% |
| 11 | Forward Industries SOL | Liquid Staking | $281.54M | +0.8% | +3.7% |
| 12 | CCIP | Bridge | $275.83M | +2.6% | +2.5% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 345 protocols the total is $11.80B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.1% · Lending 19.3% · Dexs 14.5% · Derivatives 5.3% · RWA 4.7% · Risk Curators 4.2%

### Tokenised assets

$805.91M of tokenised real-world assets and equities are locked on Solana - 6.830% of chain TVL.

- OnRe (RWA): $292.28M
- Huma (RWA): $247.09M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $40.48M
- Solomon USDv (Basis Trading): $8.78M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.1) | 2026-11-27 | stable |
| [v4.4.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.2) | 2026-11-27 | stable |
| [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | 2026-11-25 | pre-release |
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-26
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-26
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-25
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-27T01:13:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,474.38 | 1,311.20 | -11.07% |
| Average non-vote TPS | 1,474.38 | 1,311.20 | -11.07% |
| Average slot time (ms) | 214.40 | 214.30 | -0.05% |
| Active validators | 654.00 | 653.00 | -0.15% |
| Delinquent validators | 34.00 | 35.00 | +2.94% |
| Solana TVL | 4,648,654,009.00 | 4,640,931,900.00 | -0.17% |
| SOL price | 71.32 | 71.71 | +0.55% |
| Stablecoin supply | 12,690,450,207.00 | 12,691,626,832.00 | +0.01% |
| 24h DEX volume | 1,258,514,139.56 | 885,191,708.12 | -29.66% |
| 24h chain fees | 6,861,662.16 | 6,237,864.74 | -9.09% |

### Change over 7d (vs run at 2026-11-20T23:26:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,463.53 | 1,311.20 | -10.41% |
| Average non-vote TPS | 1,463.53 | 1,311.20 | -10.41% |
| Average slot time (ms) | 215.10 | 214.30 | -0.37% |
| Active validators | 662.00 | 653.00 | -1.36% |
| Delinquent validators | 23.00 | 35.00 | +52.17% |
| Solana TVL | 4,588,288,121.00 | 4,640,931,900.00 | +1.15% |
| SOL price | 69.14 | 71.71 | +3.72% |
| Stablecoin supply | 13,451,822,446.00 | 12,691,626,832.00 | -5.65% |
| 24h DEX volume | 1,904,105,685.06 | 885,191,708.12 | -53.51% |
| 24h chain fees | 9,305,684.57 | 6,237,864.74 | -32.97% |

### Change over 30d (vs run at 2026-10-28T21:57:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,155.70 | 1,311.20 | -39.18% |
| Average non-vote TPS | 2,155.70 | 1,311.20 | -39.18% |
| Average slot time (ms) | 213.60 | 214.30 | +0.33% |
| Active validators | 661.00 | 653.00 | -1.21% |
| Delinquent validators | 30.00 | 35.00 | +16.67% |
| Solana TVL | 5,748,939,504.00 | 4,640,931,900.00 | -19.27% |
| SOL price | 102.77 | 71.71 | -30.22% |
| Stablecoin supply | 15,784,667,411.00 | 12,691,626,832.00 | -19.60% |
| 24h DEX volume | 1,582,952,703.63 | 885,191,708.12 | -44.08% |
| 24h chain fees | 11,229,097.00 | 6,237,864.74 | -44.45% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
