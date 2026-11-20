# Solana Ecosystem Pulse

**Generated:** 2026-11-20T14:29:13Z · **Schema:** `1.0.0` · **Collection time:** 17.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.48 | -4.79% |
| Market cap | $42.30B | rank #7 |
| Total value locked | $4.68B | -1.42% |
| Stablecoin supply | $13.45B | +3.05% |
| DEX volume (24h) | $1.90B | +4.89% |
| Chain fees / REV (24h) | $9.31M | -14.66% |
| Non-vote TPS (1h avg) | 1,760 | peak 2,237 total |
| Active validators | 661 | 24 delinquent |
| Epoch 1092 | 6.25% complete | 404,983 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 133 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.0% in 24h) | Stablecoin supply changed +3.0% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,454,137,376.00 sits 3.1 sigma below the median of the last 133 runs (15,977,966,490.00, -15.8%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,759.8 average over the last 60 minutes; 1,869.2 in the latest sample.
- **Total TPS:** 1,759.8 average, 2,236.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.5 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 449,785,065 at absolute slot 471,771,017.
- **Epoch 1092:** slot 27,017 of 432,000 (6.25% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.548% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 109 ms |
| `solana-rpc.publicnode.com` | yes | 52 ms |
| `api.mainnet.solana.com` | yes | 94 ms |

## Validators & stake

- **661 active** validators, **24 delinquent** (3.50% by count, 0.017% by stake).
- **Total stake:** 428,985,797 SOL ($30.66B); stake rate 67.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.82% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 220 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,041,638 | 3.973% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,354,101 | 3.813% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,891 | 2.896% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,309,121 | 2.404% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,779,397 | 2.280% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,564,403 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,683 | 2.152% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,986,182 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,985,765 | 1.629% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,773,182 | 1.579% | 5% |

## Economics

- **SOL:** $71.48 (-4.79% 24h, -12.24% 7d, -33.01% 30d). Market cap $42.30B, 24h volume $2.65B (6.28% of cap). Price source: `coingecko`.
- **TVL:** $4.68B across 342 protocols - rank #3 of 426 chains, 6.76% of all tracked chain TVL. -7.07% over 7d, -60.7% from its ATH.
- **Stablecoins:** $13.45B circulating on Solana (-6.41% 7d) - $2.88 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.90B in 24h, $11.31B over 7d across 144 venues. Volume/TVL turnover 0.407x per day.
- **REV (chain fees):** $9.31M in 24h, $300.21M over 30d. Retained chain revenue $2.99M (32.2% of fees). Annualised fees are 8.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,906,697 SOL circulating of 637,920,672 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | -5.8% | -10.2% |
| 2 | Kamino Lend | Lending | $1.14B | -1.6% | -3.4% |
| 3 | Jupiter Lend | Lending | $961.02M | -0.5% | -0.0% |
| 4 | Raydium AMM | Dexs | $788.34M | -4.1% | -15.5% |
| 5 | Binance Staked SOL | Liquid Staking | $732.68M | -5.4% | -17.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $712.66M | -5.6% | -14.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $575.48M | -3.6% | -7.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $361.62M | -5.7% | -13.3% |
| 9 | Sentora Curator | Risk Curators | $357.56M | -0.1% | -1.6% |
| 10 | OnRe | RWA | $291.33M | -0.2% | -5.8% |
| 11 | Forward Industries SOL | Liquid Staking | $279.95M | -5.3% | +8.8% |
| 12 | CCIP | Bridge | $271.83M | +3.9% | +3.6% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 342 protocols the total is $11.91B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.2% · Lending 19.2% · Dexs 14.5% · Derivatives 5.3% · RWA 4.8% · Risk Curators 4.1%

### Tokenised assets

$827.18M of tokenised real-world assets and equities are locked on Solana - 6.946% of chain TVL.

- OnRe (RWA): $291.33M
- Huma (RWA): $231.29M
- Solstice (Basis Trading): $201.07M
- Plume Vaults (RWA): $40.05M
- JupUSD (Basis Trading): $39.98M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14

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

### Change over 24h (vs run at 2026-11-19T14:47:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,967.50 | 1,759.75 | -10.56% |
| Average non-vote TPS | 1,967.50 | 1,759.75 | -10.56% |
| Average slot time (ms) | 214.80 | 215.50 | +0.33% |
| Active validators | 659.00 | 661.00 | +0.30% |
| Delinquent validators | 26.00 | 24.00 | -7.69% |
| Solana TVL | 4,789,689,320.00 | 4,677,758,004.00 | -2.34% |
| SOL price | 75.26 | 71.48 | -5.02% |
| Stablecoin supply | 13,054,966,449.00 | 13,454,137,376.00 | +3.06% |
| 24h DEX volume | 1,815,395,819.31 | 1,904,151,628.06 | +4.89% |
| 24h chain fees | 10,954,885.63 | 9,305,684.54 | -15.05% |

### Change over 7d (vs run at 2026-11-13T13:31:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,486.03 | 1,759.75 | +18.42% |
| Average non-vote TPS | 1,486.03 | 1,759.75 | +18.42% |
| Average slot time (ms) | 215.70 | 215.50 | -0.09% |
| Active validators | 661.00 | 661.00 | +0.00% |
| Delinquent validators | 38.00 | 24.00 | -36.84% |
| Solana TVL | 5,000,564,115.00 | 4,677,758,004.00 | -6.46% |
| SOL price | 80.81 | 71.48 | -11.55% |
| Stablecoin supply | 14,375,541,339.00 | 13,454,137,376.00 | -6.41% |
| 24h DEX volume | 1,503,485,412.77 | 1,904,151,628.06 | +26.65% |
| 24h chain fees | 8,005,893.20 | 9,305,684.54 | +16.24% |

### Change over 30d (vs run at 2026-10-21T20:57:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,089.84 | 1,759.75 | -15.79% |
| Average non-vote TPS | 2,089.84 | 1,759.75 | -15.79% |
| Average slot time (ms) | 213.00 | 215.50 | +1.17% |
| Active validators | 668.00 | 661.00 | -1.05% |
| Delinquent validators | 9.00 | 24.00 | +166.67% |
| Solana TVL | 6,055,835,656.00 | 4,677,758,004.00 | -22.76% |
| SOL price | 108.08 | 71.48 | -33.86% |
| Stablecoin supply | 16,012,993,627.00 | 13,454,137,376.00 | -15.98% |
| 24h DEX volume | 2,437,800,216.24 | 1,904,151,628.06 | -21.89% |
| 24h chain fees | 13,174,208.40 | 9,305,684.54 | -29.36% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 17.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
