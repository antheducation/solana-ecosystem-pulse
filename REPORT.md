# Solana Ecosystem Pulse

**Generated:** 2026-11-04T13:23:03Z · **Schema:** `1.0.0` · **Collection time:** 16.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $92.65 | -0.02% |
| Market cap | $54.67B | rank #7 |
| Total value locked | $5.46B | +0.70% |
| Stablecoin supply | $14.90B | -3.07% |
| DEX volume (24h) | $1.88B | +1.54% |
| Chain fees / REV (24h) | $11.33M | +1.11% |
| Non-vote TPS (1h avg) | 1,488 | peak 2,132 total |
| Active validators | 662 | 31 delinquent |
| Epoch 1077 | 12.32% complete | 378,757 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,488; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 3.1% in 24h) | Stablecoin supply changed -3.1% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 31.00 sits 3.0 sigma above the median of the last 129 runs (13.00, +138.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,488.2 average over the last 60 minutes; 1,539.5 in the latest sample.
- **Total TPS:** 1,488.2 average, 2,131.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.1 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 443,337,679 at absolute slot 465,317,243.
- **Epoch 1077:** slot 53,243 of 432,000 (12.32% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.571% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 132 ms |
| `solana-rpc.publicnode.com` | yes | 86 ms |
| `api.mainnet.solana.com` | yes | 134 ms |

## Validators & stake

- **662 active** validators, **31 delinquent** (4.47% by count, 0.457% by stake).
- **Total stake:** 433,017,789 SOL ($40.12B); stake rate 67.98% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.86% and top 33 hold 46.76% of active stake.
- **Commission:** median 5.0%, mean 12.55%; 225 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,036,631 | 3.952% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,689 | 3.877% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,012,272 | 3.019% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,433,406 | 2.421% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,524,736 | 2.210% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,439,186 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,217,930 | 2.139% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,826,697 | 1.816% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,981,457 | 1.620% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,980,105 | 1.619% | 5% |

## Economics

- **SOL:** $92.65 (-0.02% 24h, -8.65% 7d, -23.01% 30d). Market cap $54.67B, 24h volume $2.78B (5.08% of cap). Price source: `coingecko`.
- **TVL:** $5.46B across 337 protocols - rank #3 of 420 chains, 6.56% of all tracked chain TVL. -4.49% over 7d, -57.7% from its ATH.
- **Stablecoins:** $14.90B circulating on Solana (-5.58% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.88B in 24h, $11.74B over 7d across 141 venues. Volume/TVL turnover 0.344x per day.
- **REV (chain fees):** $11.33M in 24h, $371.93M over 30d. Retained chain revenue $4.29M (37.8% of fees). Annualised fees are 7.57% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,262,415 SOL circulating of 637,005,817 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.64B | -0.2% | -8.4% |
| 2 | Kamino Lend | Lending | $1.23B | +0.5% | -3.1% |
| 3 | Raydium AMM | Dexs | $1.05B | +2.0% | -8.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.02B | +1.5% | -6.1% |
| 5 | Jupiter Lend | Lending | $1.02B | +1.3% | +2.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $956.51M | -0.1% | -9.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $681.57M | +0.8% | -5.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $469.20M | +0.5% | -11.5% |
| 9 | Sentora Curator | Risk Curators | $373.81M | +0.1% | -2.6% |
| 10 | Marinade Native | Staking Pool | $333.17M | +0.3% | -8.2% |
| 11 | PumpSwap | Dexs | $318.21M | +1.4% | -7.8% |
| 12 | OnRe | RWA | $307.51M | +0.0% | +2.1% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 337 protocols the total is $14.43B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 17.3% · Dexs 15.2% · Derivatives 5.2% · RWA 4.0% · Risk Curators 3.8%

### Tokenised assets

$829.86M of tokenised real-world assets and equities are locked on Solana - 5.749% of chain TVL.

- OnRe (RWA): $307.51M
- Huma (RWA): $215.84M
- Solstice (Basis Trading): $201.42M
- JupUSD (Basis Trading): $39.09M
- Plume Vaults (RWA): $35.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-03
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-03
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-03
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-11-03T13:07:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,522.59 | 1,488.22 | -2.26% |
| Average non-vote TPS | 1,522.59 | 1,488.22 | -2.26% |
| Average slot time (ms) | 213.90 | 214.10 | +0.09% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 29.00 | 31.00 | +6.90% |
| Solana TVL | 5,402,051,428.00 | 5,464,731,305.00 | +1.16% |
| SOL price | 92.81 | 92.65 | -0.17% |
| Stablecoin supply | 15,370,716,122.00 | 14,903,033,514.00 | -3.04% |
| 24h DEX volume | 1,830,732,933.50 | 1,881,110,224.90 | +2.75% |
| 24h chain fees | 11,140,650.50 | 11,334,057.17 | +1.74% |

### Change over 7d (vs run at 2026-10-28T11:44:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,323.46 | 1,488.22 | +12.45% |
| Average non-vote TPS | 1,323.46 | 1,488.22 | +12.45% |
| Average slot time (ms) | 212.60 | 214.10 | +0.71% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 29.00 | 31.00 | +6.90% |
| Solana TVL | 5,789,213,551.00 | 5,464,731,305.00 | -5.60% |
| SOL price | 102.71 | 92.65 | -9.79% |
| Stablecoin supply | 15,780,319,313.00 | 14,903,033,514.00 | -5.56% |
| 24h DEX volume | 1,582,952,703.63 | 1,881,110,224.90 | +18.84% |
| 24h chain fees | 10,908,125.93 | 11,334,057.17 | +3.90% |

### Change over 30d (vs run at 2026-10-05T23:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,796.58 | 1,488.22 | -68.97% |
| Average non-vote TPS | 2,304.82 | 1,488.22 | -35.43% |
| Average slot time (ms) | 268.60 | 214.10 | -20.29% |
| Active validators | 672.00 | 662.00 | -1.49% |
| Delinquent validators | 13.00 | 31.00 | +138.46% |
| Solana TVL | 6,781,683,220.00 | 5,464,731,305.00 | -19.42% |
| SOL price | 120.74 | 92.65 | -23.26% |
| Stablecoin supply | 16,885,339,627.00 | 14,903,033,514.00 | -11.74% |
| 24h DEX volume | 1,708,158,585.63 | 1,881,110,224.90 | +10.13% |
| 24h chain fees | 16,123,937.37 | 11,334,057.17 | -29.71% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 16.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
