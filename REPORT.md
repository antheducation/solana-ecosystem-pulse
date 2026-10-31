# Solana Ecosystem Pulse

**Generated:** 2026-10-31T20:43:49Z · **Schema:** `1.0.0` · **Collection time:** 16.2s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $95.56 | +0.62% |
| Market cap | $56.39B | rank #7 |
| Total value locked | $5.45B | +1.50% |
| Stablecoin supply | $15.49B | +0.26% |
| DEX volume (24h) | $2.12B | -7.75% |
| Chain fees / REV (24h) | $11.23M | -8.90% |
| Non-vote TPS (1h avg) | 1,656 | peak 2,804 total |
| Active validators | 665 | 27 delinquent |
| Epoch 1073 | 67.43% complete | 140,682 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 27.00 sits 3.4 sigma above the median of the last 129 runs (12.00, +125.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,655.7 average over the last 60 minutes; 1,596.8 in the latest sample.
- **Total TPS:** 1,655.7 average, 2,804.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.0 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 441,849,144 at absolute slot 463,827,318.
- **Epoch 1073:** slot 291,318 of 432,000 (67.43% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.578% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 89 ms |
| `solana-rpc.publicnode.com` | yes | 51 ms |
| `api.mainnet.solana.com` | yes | 76 ms |

## Validators & stake

- **665 active** validators, **27 delinquent** (3.90% by count, 0.847% by stake).
- **Total stake:** 433,649,347 SOL ($41.44B); stake rate 68.10% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.92% and top 33 hold 46.60% of active stake.
- **Commission:** median 5.0%, mean 13.07%; 225 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,020,574 | 3.959% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,688,715 | 3.881% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,931,864 | 3.008% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,425,467 | 2.425% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,651,671 | 2.245% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,449,481 | 2.198% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,227,526 | 2.146% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,778,595 | 1.809% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,000,338 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,976,145 | 1.622% | 5% |

## Economics

- **SOL:** $95.56 (+0.62% 24h, -5.51% 7d, -19.16% 30d). Market cap $56.39B, 24h volume $1.91B (3.39% of cap). Price source: `coingecko`.
- **TVL:** $5.45B across 334 protocols - rank #4 of 420 chains, 6.40% of all tracked chain TVL. -5.85% over 7d, -57.9% from its ATH.
- **Stablecoins:** $15.49B circulating on Solana (-2.57% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.12B in 24h, $12.67B over 7d across 139 venues. Volume/TVL turnover 0.389x per day.
- **REV (chain fees):** $11.23M in 24h, $404.83M over 30d. Retained chain revenue $4.08M (36.3% of fees). Annualised fees are 7.27% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,095,006 SOL circulating of 636,761,074 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.68B | +1.7% | -5.8% |
| 2 | Kamino Lend | Lending | $1.23B | +4.3% | -3.0% |
| 3 | Raydium AMM | Dexs | $1.08B | +1.7% | -7.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.04B | +2.1% | -3.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $992.02M | +1.0% | -6.6% |
| 6 | Jupiter Lend | Lending | $930.73M | +4.3% | -8.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $694.00M | +1.4% | -4.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $490.47M | +1.3% | -8.9% |
| 9 | Sentora Curator | Risk Curators | $375.74M | -0.0% | -5.4% |
| 10 | Marinade Native | Staking Pool | $344.64M | +1.3% | -6.7% |
| 11 | PumpSwap | Dexs | $323.89M | +0.8% | -4.5% |
| 12 | OnRe | RWA | $307.67M | +0.1% | +4.2% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.67B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.5% · Dexs 15.2% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.7%

### Tokenised assets

$859.95M of tokenised real-world assets and equities are locked on Solana - 5.863% of chain TVL.

- OnRe (RWA): $307.67M
- Huma (RWA): $246.58M
- Solstice (Basis Trading): $201.48M
- JupUSD (Basis Trading): $38.88M
- Plume Vaults (RWA): $35.12M

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

- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-31
- [SIMD-0529: rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-31
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-30
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28

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

### Change over 24h (vs run at 2026-10-30T21:44:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,609.94 | 1,655.68 | +2.84% |
| Average non-vote TPS | 1,609.94 | 1,655.68 | +2.84% |
| Average slot time (ms) | 214.70 | 214.00 | -0.33% |
| Active validators | 666.00 | 665.00 | -0.15% |
| Delinquent validators | 25.00 | 27.00 | +8.00% |
| Solana TVL | 5,346,984,781.00 | 5,449,917,859.00 | +1.93% |
| SOL price | 95.38 | 95.56 | +0.19% |
| Stablecoin supply | 15,450,891,906.00 | 15,493,312,766.00 | +0.27% |
| 24h DEX volume | 2,295,364,281.70 | 2,117,396,479.19 | -7.75% |
| 24h chain fees | 12,329,690.27 | 11,233,221.43 | -8.89% |

### Change over 7d (vs run at 2026-10-24T19:54:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,955.01 | 1,655.68 | -15.31% |
| Average non-vote TPS | 1,955.01 | 1,655.68 | -15.31% |
| Average slot time (ms) | 212.50 | 214.00 | +0.71% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 25.00 | 27.00 | +8.00% |
| Solana TVL | 5,717,401,347.00 | 5,449,917,859.00 | -4.68% |
| SOL price | 101.01 | 95.56 | -5.40% |
| Stablecoin supply | 15,925,693,948.00 | 15,493,312,766.00 | -2.71% |
| 24h DEX volume | 1,997,070,440.37 | 2,117,396,479.19 | +6.03% |
| 24h chain fees | 10,552,167.09 | 11,233,221.43 | +6.45% |

### Change over 30d (vs run at 2026-10-01T22:04:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,821.72 | 1,655.68 | -65.66% |
| Average non-vote TPS | 2,325.69 | 1,655.68 | -28.81% |
| Average slot time (ms) | 268.10 | 214.00 | -20.18% |
| Active validators | 672.00 | 665.00 | -1.04% |
| Delinquent validators | 12.00 | 27.00 | +125.00% |
| Solana TVL | 6,567,199,720.00 | 5,449,917,859.00 | -17.01% |
| SOL price | 117.92 | 95.56 | -18.96% |
| Stablecoin supply | 16,398,651,646.00 | 15,493,312,766.00 | -5.52% |
| 24h DEX volume | 2,569,940,125.73 | 2,117,396,479.19 | -17.61% |
| 24h chain fees | 15,975,862.05 | 11,233,221.43 | -29.69% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 16.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
