# Solana Ecosystem Pulse

**Generated:** 2026-10-31T02:57:22Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.84 | +1.87% |
| Market cap | $57.14B | rank #7 |
| Total value locked | $5.46B | +2.09% |
| Stablecoin supply | $15.49B | +0.24% |
| DEX volume (24h) | $2.40B | +4.50% |
| Chain fees / REV (24h) | $11.03M | -10.54% |
| Non-vote TPS (1h avg) | 1,389 | peak 1,796 total |
| Active validators | 665 | 26 delinquent |
| Epoch 1072 | 98.27% complete | 7,458 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,389; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,388.58 sits 3.4 sigma below the median of the last 128 runs (4,316.47, -67.8%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 26.00 sits 3.1 sigma above the median of the last 128 runs (12.00, +116.7%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,388.6 average over the last 60 minutes; 1,240.6 in the latest sample.
- **Total TPS:** 1,388.6 average, 1,796.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.4 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 441,550,740 at absolute slot 463,528,542.
- **Epoch 1072:** slot 424,542 of 432,000 (98.27% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.579% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 160 ms |
| `solana-rpc.publicnode.com` | yes | 131 ms |
| `api.mainnet.solana.com` | yes | 123 ms |

## Validators & stake

- **665 active** validators, **26 delinquent** (3.76% by count, 0.703% by stake).
- **Total stake:** 435,357,093 SOL ($42.16B); stake rate 68.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.81% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 13.06%; 227 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,965,456 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,678,000 | 3.858% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,919,680 | 2.989% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,502,229 | 2.429% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,659,910 | 2.235% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,473,552 | 2.191% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,406 | 2.133% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,780,140 | 1.800% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,045,150 | 1.630% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,506 | 1.620% | 0% |

## Economics

- **SOL:** $96.84 (+1.87% 24h, -5.53% 7d, -17.99% 30d). Market cap $57.14B, 24h volume $3.28B (5.74% of cap). Price source: `coingecko`.
- **TVL:** $5.46B across 335 protocols - rank #5 of 420 chains, 6.42% of all tracked chain TVL. -5.61% over 7d, -57.7% from its ATH.
- **Stablecoins:** $15.49B circulating on Solana (-2.59% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.40B in 24h, $11.78B over 7d across 139 venues. Volume/TVL turnover 0.439x per day.
- **REV (chain fees):** $11.03M in 24h, $404.05M over 30d. Retained chain revenue $4.13M (37.4% of fees). Annualised fees are 7.05% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,039,626 SOL circulating of 636,700,021 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.70B | +3.0% | -4.8% |
| 2 | Kamino Lend | Lending | $1.24B | +4.0% | -2.5% |
| 3 | Raydium AMM | Dexs | $1.07B | -1.3% | -7.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.05B | +4.0% | -2.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.00B | +3.4% | -5.5% |
| 6 | Jupiter Lend | Lending | $940.94M | +4.2% | -7.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $697.39M | +1.4% | -3.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $498.61M | +1.9% | -7.4% |
| 9 | Sentora Curator | Risk Curators | $375.95M | -1.0% | -5.3% |
| 10 | Marinade Native | Staking Pool | $348.54M | +2.2% | -5.7% |
| 11 | PumpSwap | Dexs | $324.51M | -0.3% | -4.3% |
| 12 | OnRe | RWA | $307.63M | +1.2% | +4.1% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 335 protocols the total is $14.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 16.5% · Dexs 15.1% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.7%

### Tokenised assets

$870.52M of tokenised real-world assets and equities are locked on Solana - 5.896% of chain TVL.

- OnRe (RWA): $307.63M
- Huma (RWA): $256.68M
- Solstice (Basis Trading): $201.43M
- JupUSD (Basis Trading): $38.86M
- Plume Vaults (RWA): $35.18M

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

- [SIMD-0529: rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-31
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-30
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

### Change over 24h (vs run at 2026-10-30T03:12:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,784.28 | 1,388.58 | -22.18% |
| Average non-vote TPS | 1,784.28 | 1,388.58 | -22.18% |
| Average slot time (ms) | 213.50 | 214.40 | +0.42% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 26.00 | 26.00 | +0.00% |
| Solana TVL | 5,381,303,759.00 | 5,463,465,803.00 | +1.53% |
| SOL price | 95.76 | 96.84 | +1.13% |
| Stablecoin supply | 15,441,453,836.00 | 15,490,673,443.00 | +0.32% |
| 24h DEX volume | 1,924,354,203.70 | 2,398,568,001.19 | +24.64% |
| 24h chain fees | 11,363,568.43 | 11,030,452.47 | -2.93% |

### Change over 7d (vs run at 2026-10-24T02:13:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,753.27 | 1,388.58 | -20.80% |
| Average non-vote TPS | 1,753.27 | 1,388.58 | -20.80% |
| Average slot time (ms) | 212.00 | 214.40 | +1.13% |
| Active validators | 664.00 | 665.00 | +0.15% |
| Delinquent validators | 14.00 | 26.00 | +85.71% |
| Solana TVL | 5,818,515,359.00 | 5,463,465,803.00 | -6.10% |
| SOL price | 102.56 | 96.84 | -5.58% |
| Stablecoin supply | 15,925,064,319.00 | 15,490,673,443.00 | -2.73% |
| 24h DEX volume | 2,021,288,711.44 | 2,398,568,001.19 | +18.67% |
| 24h chain fees | 10,537,655.05 | 11,030,452.47 | +4.68% |

### Change over 30d (vs run at 2026-09-30T21:35:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,839.95 | 1,388.58 | -71.31% |
| Average non-vote TPS | 2,344.25 | 1,388.58 | -40.77% |
| Average slot time (ms) | 268.00 | 214.40 | -20.00% |
| Active validators | 672.00 | 665.00 | -1.04% |
| Delinquent validators | 11.00 | 26.00 | +136.36% |
| Solana TVL | 6,529,687,399.00 | 5,463,465,803.00 | -16.33% |
| SOL price | 117.96 | 96.84 | -17.90% |
| Stablecoin supply | 16,483,355,698.00 | 15,490,673,443.00 | -6.02% |
| 24h DEX volume | 2,534,187,471.84 | 2,398,568,001.19 | -5.35% |
| 24h chain fees | 14,686,283.17 | 11,030,452.47 | -24.89% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
