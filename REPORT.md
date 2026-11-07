# Solana Ecosystem Pulse

**Generated:** 2026-11-07T11:59:16Z · **Schema:** `1.0.0` · **Collection time:** 15.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $89.91 | -0.41% |
| Market cap | $53.14B | rank #7 |
| Total value locked | $5.25B | -0.83% |
| Stablecoin supply | $14.84B | -1.30% |
| DEX volume (24h) | $1.48B | -32.68% |
| Chain fees / REV (24h) | $9.26M | -4.50% |
| Non-vote TPS (1h avg) | 1,054 | peak 1,368 total |
| Active validators | 660 | 36 delinquent |
| Epoch 1079 | 87.08% complete | 55,813 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,054; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,054.2 average over the last 60 minutes; 1,122.0 in the latest sample.
- **Total TPS:** 1,054.2 average, 1,368.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.5 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 444,522,864 at absolute slot 466,504,187.
- **Epoch 1079:** slot 376,187 of 432,000 (87.08% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.568% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 67 ms |
| `solana-rpc.publicnode.com` | yes | 27 ms |
| `api.mainnet.solana.com` | yes | 102 ms |

## Validators & stake

- **660 active** validators, **36 delinquent** (5.17% by count, 0.284% by stake).
- **Total stake:** 434,917,723 SOL ($39.10B); stake rate 68.26% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.72% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 12.89%; 221 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,039,556 | 3.929% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,722,209 | 3.856% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,017,562 | 3.002% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,436,420 | 2.406% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,531,946 | 2.198% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,519,642 | 2.195% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,519 | 2.131% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,741,933 | 1.785% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,982,918 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,614 | 1.608% | 0% |

## Economics

- **SOL:** $89.91 (-0.41% 24h, -5.87% 7d, -21.37% 30d). Market cap $53.14B, 24h volume $1.73B (3.25% of cap). Price source: `coingecko`.
- **TVL:** $5.25B across 341 protocols - rank #3 of 421 chains, 6.46% of all tracked chain TVL. -4.30% over 7d, -59.5% from its ATH.
- **Stablecoins:** $14.84B circulating on Solana (-4.23% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.48B in 24h, $11.66B over 7d across 141 venues. Volume/TVL turnover 0.282x per day.
- **REV (chain fees):** $9.26M in 24h, $351.74M over 30d. Retained chain revenue $3.30M (35.7% of fees). Annualised fees are 6.36% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,982,527 SOL circulating of 637,127,613 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | +0.1% | -6.0% |
| 2 | Kamino Lend | Lending | $1.19B | -0.9% | -4.4% |
| 3 | Raydium AMM | Dexs | $1.01B | +0.8% | -6.5% |
| 4 | Binance Staked SOL | Liquid Staking | $978.51M | -0.1% | -6.1% |
| 5 | Jupiter Lend | Lending | $932.19M | -6.5% | -0.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $924.08M | -0.1% | -7.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $664.64M | +0.3% | -4.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $457.41M | +0.3% | -7.6% |
| 9 | Sentora Curator | Risk Curators | $373.89M | +0.1% | -0.5% |
| 10 | Marinade Native | Staking Pool | $322.65M | -0.4% | -6.8% |
| 11 | PumpSwap | Dexs | $308.86M | -0.1% | -6.3% |
| 12 | OnRe | RWA | $308.53M | +0.0% | +0.3% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 341 protocols the total is $14.00B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.9% · Dexs 15.2% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$845.53M of tokenised real-world assets and equities are locked on Solana - 6.041% of chain TVL.

- OnRe (RWA): $308.53M
- Huma (RWA): $225.87M
- Solstice (Basis Trading): $201.10M
- JupUSD (Basis Trading): $44.34M
- Plume Vaults (RWA): $36.80M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-06
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-06
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04

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

### Change over 24h (vs run at 2026-11-06T13:20:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,430.24 | 1,054.19 | -26.29% |
| Average non-vote TPS | 1,430.24 | 1,054.19 | -26.29% |
| Average slot time (ms) | 213.80 | 214.50 | +0.33% |
| Active validators | 662.00 | 660.00 | -0.30% |
| Delinquent validators | 32.00 | 36.00 | +12.50% |
| Solana TVL | 5,312,901,284.00 | 5,246,632,455.00 | -1.25% |
| SOL price | 90.05 | 89.91 | -0.16% |
| Stablecoin supply | 15,031,918,557.00 | 14,838,782,561.00 | -1.28% |
| 24h DEX volume | 2,198,364,299.20 | 1,479,986,839.85 | -32.68% |
| 24h chain fees | 9,633,288.35 | 9,264,218.12 | -3.83% |

### Change over 7d (vs run at 2026-10-31T11:19:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 991.93 | 1,054.19 | +6.28% |
| Average non-vote TPS | 991.93 | 1,054.19 | +6.28% |
| Average slot time (ms) | 213.70 | 214.50 | +0.37% |
| Active validators | 665.00 | 660.00 | -0.75% |
| Delinquent validators | 27.00 | 36.00 | +33.33% |
| Solana TVL | 5,443,490,761.00 | 5,246,632,455.00 | -3.62% |
| SOL price | 95.67 | 89.91 | -6.02% |
| Stablecoin supply | 15,491,130,492.00 | 14,838,782,561.00 | -4.21% |
| 24h DEX volume | 2,117,396,479.19 | 1,479,986,839.85 | -30.10% |
| 24h chain fees | 11,223,116.43 | 9,264,218.12 | -17.45% |

### Change over 30d (vs run at 2026-10-08T22:33:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,632.43 | 1,054.19 | -77.24% |
| Average non-vote TPS | 2,125.38 | 1,054.19 | -50.40% |
| Average slot time (ms) | 267.50 | 214.50 | -19.81% |
| Active validators | 673.00 | 660.00 | -1.93% |
| Delinquent validators | 8.00 | 36.00 | +350.00% |
| Solana TVL | 6,248,086,909.00 | 5,246,632,455.00 | -16.03% |
| SOL price | 110.19 | 89.91 | -18.40% |
| Stablecoin supply | 16,607,983,518.00 | 14,838,782,561.00 | -10.65% |
| 24h DEX volume | 2,205,685,057.81 | 1,479,986,839.85 | -32.90% |
| 24h chain fees | 13,737,332.90 | 9,264,218.12 | -32.56% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 15.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
