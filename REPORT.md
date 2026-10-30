# Solana Ecosystem Pulse

**Generated:** 2026-10-30T11:45:48Z · **Schema:** `1.0.0` · **Collection time:** 21.8s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.65 | -3.69% |
| Market cap | $57.02B | rank #7 |
| Total value locked | $5.43B | -5.17% |
| Stablecoin supply | $15.45B | -1.45% |
| DEX volume (24h) | $2.30B | +32.42% |
| Chain fees / REV (24h) | $12.33M | +16.95% |
| Non-vote TPS (1h avg) | 1,253 | peak 1,592 total |
| Active validators | 667 | 24 delinquent |
| Epoch 1072 | 39.17% complete | 262,784 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,253; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,252.98 sits 4.2 sigma below the median of the last 128 runs (4,415.78, -71.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,253.0 average over the last 60 minutes; 1,249.3 in the latest sample.
- **Total TPS:** 1,253.0 average, 1,592.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.4 ms average (target 400 ms), worst 1-minute bucket 218.2 ms.
- **Block height:** 441,295,610 at absolute slot 463,273,216.
- **Epoch 1072:** slot 169,216 of 432,000 (39.17% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.579% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 209 ms |
| `solana-rpc.publicnode.com` | yes | 114 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **667 active** validators, **24 delinquent** (3.47% by count, 0.623% by stake).
- **Total stake:** 435,357,093 SOL ($42.08B); stake rate 68.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.36% of active stake.
- **Commission:** median 5.0%, mean 12.73%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,965,456 | 3.921% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,678,000 | 3.855% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,919,680 | 2.986% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,502,229 | 2.427% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,659,910 | 2.233% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,473,552 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,406 | 2.132% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,780,140 | 1.798% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,045,150 | 1.628% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,506 | 1.618% | 0% |

## Economics

- **SOL:** $96.65 (-3.69% 24h, -7.01% 7d, -19.31% 30d). Market cap $57.02B, 24h volume $5.81B (10.19% of cap). Price source: `coingecko`.
- **TVL:** $5.43B across 335 protocols - rank #5 of 420 chains, 6.47% of all tracked chain TVL. -7.62% over 7d, -58.0% from its ATH.
- **Stablecoins:** $15.45B circulating on Solana (-3.08% 7d) - $2.85 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.30B in 24h, $12.55B over 7d across 139 venues. Volume/TVL turnover 0.423x per day.
- **REV (chain fees):** $12.33M in 24h, $411.79M over 30d. Retained chain revenue $3.87M (31.4% of fees). Annualised fees are 7.89% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,039,904 SOL circulating of 636,700,299 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.71B | -3.6% | -5.8% |
| 2 | Kamino Lend | Lending | $1.21B | -3.9% | -7.3% |
| 3 | Raydium AMM | Dexs | $1.09B | -3.0% | -7.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.05B | -3.1% | -3.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.00B | -3.8% | -6.8% |
| 6 | Jupiter Lend | Lending | $912.23M | -8.1% | -11.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $697.58M | -1.8% | -4.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $498.97M | -4.4% | -7.9% |
| 9 | Sentora Curator | Risk Curators | $379.54M | -1.1% | -9.3% |
| 10 | Marinade Native | Staking Pool | $348.83M | -3.2% | -6.1% |
| 11 | PumpSwap | Dexs | $328.05M | -2.7% | -5.7% |
| 12 | OnRe | RWA | $304.28M | -0.4% | +3.1% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 335 protocols the total is $14.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.6% · Lending 16.1% · Dexs 15.2% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$873.84M of tokenised real-world assets and equities are locked on Solana - 5.920% of chain TVL.

- OnRe (RWA): $304.28M
- Huma (RWA): $262.45M
- Solstice (Basis Trading): $201.35M
- JupUSD (Basis Trading): $39.68M
- Plume Vaults (RWA): $35.38M

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

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-30
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-29T11:52:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,331.86 | 1,252.98 | -5.92% |
| Average non-vote TPS | 1,331.86 | 1,252.98 | -5.92% |
| Average slot time (ms) | 214.00 | 213.40 | -0.28% |
| Active validators | 666.00 | 667.00 | +0.15% |
| Delinquent validators | 23.00 | 24.00 | +4.35% |
| Solana TVL | 5,646,734,237.00 | 5,427,386,909.00 | -3.88% |
| SOL price | 100.38 | 96.65 | -3.72% |
| Stablecoin supply | 15,688,764,724.00 | 15,453,819,358.00 | -1.50% |
| 24h DEX volume | 1,733,397,982.06 | 2,295,364,281.70 | +32.42% |
| 24h chain fees | 10,346,775.24 | 12,327,710.27 | +19.15% |

### Change over 7d (vs run at 2026-10-23T10:36:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,792.56 | 1,252.98 | -30.10% |
| Average non-vote TPS | 1,792.56 | 1,252.98 | -30.10% |
| Average slot time (ms) | 211.50 | 213.40 | +0.90% |
| Active validators | 656.00 | 667.00 | +1.68% |
| Delinquent validators | 20.00 | 24.00 | +20.00% |
| Solana TVL | 5,868,506,816.00 | 5,427,386,909.00 | -7.52% |
| SOL price | 104.11 | 96.65 | -7.17% |
| Stablecoin supply | 15,966,112,276.00 | 15,453,819,358.00 | -3.21% |
| 24h DEX volume | 2,074,632,771.23 | 2,295,364,281.70 | +10.64% |
| 24h chain fees | 11,333,373.27 | 12,327,710.27 | +8.77% |

### Change over 30d (vs run at 2026-09-30T21:35:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,839.95 | 1,252.98 | -74.11% |
| Average non-vote TPS | 2,344.25 | 1,252.98 | -46.55% |
| Average slot time (ms) | 268.00 | 213.40 | -20.37% |
| Active validators | 672.00 | 667.00 | -0.74% |
| Delinquent validators | 11.00 | 24.00 | +118.18% |
| Solana TVL | 6,529,687,399.00 | 5,427,386,909.00 | -16.88% |
| SOL price | 117.96 | 96.65 | -18.07% |
| Stablecoin supply | 16,483,355,698.00 | 15,453,819,358.00 | -6.25% |
| 24h DEX volume | 2,534,187,471.84 | 2,295,364,281.70 | -9.42% |
| 24h chain fees | 14,686,283.17 | 12,327,710.27 | -16.06% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
