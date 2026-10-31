# Solana Ecosystem Pulse

**Generated:** 2026-10-31T11:19:08Z · **Schema:** `1.0.0` · **Collection time:** 16.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $95.67 | -1.14% |
| Market cap | $56.46B | rank #7 |
| Total value locked | $5.44B | +1.38% |
| Stablecoin supply | $15.49B | +0.25% |
| DEX volume (24h) | $2.12B | -7.75% |
| Chain fees / REV (24h) | $11.22M | -8.97% |
| Non-vote TPS (1h avg) | 992 | peak 1,360 total |
| Active validators | 665 | 27 delinquent |
| Epoch 1073 | 30.82% complete | 298,860 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 992; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 991.93 sits 3.8 sigma below the median of the last 129 runs (4,304.40, -77.0%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 27.00 sits 3.4 sigma above the median of the last 129 runs (12.00, +125.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 991.9 average over the last 60 minutes; 921.7 in the latest sample.
- **Total TPS:** 991.9 average, 1,360.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.7 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 441,690,995 at absolute slot 463,669,140.
- **Epoch 1073:** slot 133,140 of 432,000 (30.82% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.578% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 118 ms |
| `solana-rpc.publicnode.com` | yes | 52 ms |
| `api.mainnet.solana.com` | yes | 59 ms |

## Validators & stake

- **665 active** validators, **27 delinquent** (3.90% by count, 0.847% by stake).
- **Total stake:** 433,649,347 SOL ($41.49B); stake rate 68.10% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.92% and top 33 hold 46.60% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 228 validators at 0% and 63 at 100%.

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

- **SOL:** $95.67 (-1.14% 24h, -5.86% 7d, -18.90% 30d). Market cap $56.46B, 24h volume $2.98B (5.28% of cap). Price source: `coingecko`.
- **TVL:** $5.44B across 334 protocols - rank #5 of 420 chains, 6.41% of all tracked chain TVL. -5.96% over 7d, -57.9% from its ATH.
- **Stablecoins:** $15.49B circulating on Solana (-2.58% 7d) - $2.85 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.12B in 24h, $12.67B over 7d across 139 venues. Volume/TVL turnover 0.389x per day.
- **REV (chain fees):** $11.22M in 24h, $404.82M over 30d. Retained chain revenue $4.07M (36.3% of fees). Annualised fees are 7.26% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,095,150 SOL circulating of 636,761,218 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.68B | -1.9% | -6.2% |
| 2 | Kamino Lend | Lending | $1.24B | +2.2% | -2.8% |
| 3 | Raydium AMM | Dexs | $1.08B | -1.3% | -7.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.03B | -1.4% | -4.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $986.88M | -1.8% | -7.1% |
| 6 | Jupiter Lend | Lending | $927.97M | +1.7% | -9.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $692.07M | -0.8% | -4.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $488.79M | -2.0% | -9.2% |
| 9 | Sentora Curator | Risk Curators | $375.91M | -1.0% | -5.3% |
| 10 | Marinade Native | Staking Pool | $342.61M | -1.8% | -7.3% |
| 11 | PumpSwap | Dexs | $326.18M | -0.6% | -3.8% |
| 12 | OnRe | RWA | $307.67M | +1.1% | +4.2% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.64B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 16.5% · Dexs 15.2% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.7%

### Tokenised assets

$871.62M of tokenised real-world assets and equities are locked on Solana - 5.952% of chain TVL.

- OnRe (RWA): $307.67M
- Huma (RWA): $257.75M
- Solstice (Basis Trading): $201.46M
- JupUSD (Basis Trading): $38.87M
- Plume Vaults (RWA): $35.20M

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

### Change over 24h (vs run at 2026-10-30T11:45:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,252.98 | 991.93 | -20.83% |
| Average non-vote TPS | 1,252.98 | 991.93 | -20.83% |
| Average slot time (ms) | 213.40 | 213.70 | +0.14% |
| Active validators | 667.00 | 665.00 | -0.30% |
| Delinquent validators | 24.00 | 27.00 | +12.50% |
| Solana TVL | 5,427,386,909.00 | 5,443,490,761.00 | +0.30% |
| SOL price | 96.65 | 95.67 | -1.01% |
| Stablecoin supply | 15,453,819,358.00 | 15,491,130,492.00 | +0.24% |
| 24h DEX volume | 2,295,364,281.70 | 2,117,396,479.19 | -7.75% |
| 24h chain fees | 12,327,710.27 | 11,223,116.43 | -8.96% |

### Change over 7d (vs run at 2026-10-24T09:54:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,467.49 | 991.93 | -32.41% |
| Average non-vote TPS | 1,467.49 | 991.93 | -32.41% |
| Average slot time (ms) | 212.60 | 213.70 | +0.52% |
| Active validators | 664.00 | 665.00 | +0.15% |
| Delinquent validators | 14.00 | 27.00 | +92.86% |
| Solana TVL | 5,782,762,976.00 | 5,443,490,761.00 | -5.87% |
| SOL price | 101.24 | 95.67 | -5.50% |
| Stablecoin supply | 15,924,707,128.00 | 15,491,130,492.00 | -2.72% |
| 24h DEX volume | 2,020,963,434.37 | 2,117,396,479.19 | +4.77% |
| 24h chain fees | 10,536,967.05 | 11,223,116.43 | +6.51% |

### Change over 30d (vs run at 2026-10-01T22:04:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,821.72 | 991.93 | -79.43% |
| Average non-vote TPS | 2,325.69 | 991.93 | -57.35% |
| Average slot time (ms) | 268.10 | 213.70 | -20.29% |
| Active validators | 672.00 | 665.00 | -1.04% |
| Delinquent validators | 12.00 | 27.00 | +125.00% |
| Solana TVL | 6,567,199,720.00 | 5,443,490,761.00 | -17.11% |
| SOL price | 117.92 | 95.67 | -18.87% |
| Stablecoin supply | 16,398,651,646.00 | 15,491,130,492.00 | -5.53% |
| 24h DEX volume | 2,569,940,125.73 | 2,117,396,479.19 | -17.61% |
| 24h chain fees | 15,975,862.05 | 11,223,116.43 | -29.75% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 16.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
