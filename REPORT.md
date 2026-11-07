# Solana Ecosystem Pulse

**Generated:** 2026-11-07T03:28:30Z · **Schema:** `1.0.0` · **Collection time:** 20.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $90.17 | +0.18% |
| Market cap | $53.29B | rank #7 |
| Total value locked | $5.25B | -0.99% |
| Stablecoin supply | $14.84B | -1.30% |
| DEX volume (24h) | $1.86B | -15.59% |
| Chain fees / REV (24h) | $9.37M | -3.37% |
| Non-vote TPS (1h avg) | 1,400 | peak 1,849 total |
| Active validators | 659 | 37 delinquent |
| Epoch 1079 | 53.96% complete | 198,895 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,400; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,399.5 average over the last 60 minutes; 1,445.3 in the latest sample.
- **Total TPS:** 1,399.5 average, 1,849.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.2 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 444,379,906 at absolute slot 466,361,105.
- **Epoch 1079:** slot 233,105 of 432,000 (53.96% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.568% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 226 ms |
| `solana-rpc.publicnode.com` | yes | 289 ms |
| `api.mainnet.solana.com` | yes | 135 ms |

## Validators & stake

- **659 active** validators, **37 delinquent** (5.32% by count, 0.284% by stake).
- **Total stake:** 434,917,723 SOL ($39.22B); stake rate 68.26% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.72% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 221 validators at 0% and 61 at 100%.

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

- **SOL:** $90.17 (+0.18% 24h, -6.80% 7d, -22.55% 30d). Market cap $53.29B, 24h volume $2.19B (4.10% of cap). Price source: `coingecko`.
- **TVL:** $5.25B across 341 protocols - rank #3 of 421 chains, 6.48% of all tracked chain TVL. -4.11% over 7d, -59.4% from its ATH.
- **Stablecoins:** $14.84B circulating on Solana (-4.24% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.86B in 24h, $10.83B over 7d across 141 venues. Volume/TVL turnover 0.353x per day.
- **REV (chain fees):** $9.37M in 24h, $350.84M over 30d. Retained chain revenue $3.32M (35.4% of fees). Annualised fees are 6.42% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,982,624 SOL circulating of 637,127,710 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | +0.5% | -5.6% |
| 2 | Kamino Lend | Lending | $1.19B | -0.9% | -4.2% |
| 3 | Raydium AMM | Dexs | $1.02B | +2.3% | -6.2% |
| 4 | Binance Staked SOL | Liquid Staking | $982.13M | +0.1% | -5.7% |
| 5 | Jupiter Lend | Lending | $932.34M | -5.6% | -0.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $925.91M | +0.3% | -7.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $664.31M | -0.0% | -4.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $460.20M | +0.7% | -7.0% |
| 9 | Sentora Curator | Risk Curators | $373.84M | +0.1% | -0.5% |
| 10 | Marinade Native | Staking Pool | $325.44M | +0.2% | -6.0% |
| 11 | PumpSwap | Dexs | $311.29M | +0.7% | -5.6% |
| 12 | OnRe | RWA | $308.61M | +0.0% | +0.3% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 341 protocols the total is $14.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.9% · Dexs 15.2% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.8%

### Tokenised assets

$845.82M of tokenised real-world assets and equities are locked on Solana - 6.027% of chain TVL.

- OnRe (RWA): $308.61M
- Huma (RWA): $225.88M
- Solstice (Basis Trading): $201.06M
- JupUSD (Basis Trading): $44.56M
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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-06
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-06
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-11-04

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

### Change over 24h (vs run at 2026-11-06T03:54:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,607.08 | 1,399.54 | -12.91% |
| Average non-vote TPS | 1,607.08 | 1,399.54 | -12.91% |
| Average slot time (ms) | 214.00 | 214.20 | +0.09% |
| Active validators | 663.00 | 659.00 | -0.60% |
| Delinquent validators | 31.00 | 37.00 | +19.35% |
| Solana TVL | 5,291,216,002.00 | 5,253,993,812.00 | -0.70% |
| SOL price | 89.73 | 90.17 | +0.49% |
| Stablecoin supply | 15,032,733,630.00 | 14,838,258,165.00 | -1.29% |
| 24h DEX volume | 2,182,575,633.20 | 1,855,725,891.85 | -14.98% |
| 24h chain fees | 9,790,369.15 | 9,374,578.15 | -4.25% |

### Change over 7d (vs run at 2026-10-31T02:57:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,388.58 | 1,399.54 | +0.79% |
| Average non-vote TPS | 1,388.58 | 1,399.54 | +0.79% |
| Average slot time (ms) | 214.40 | 214.20 | -0.09% |
| Active validators | 665.00 | 659.00 | -0.90% |
| Delinquent validators | 26.00 | 37.00 | +42.31% |
| Solana TVL | 5,463,465,803.00 | 5,253,993,812.00 | -3.83% |
| SOL price | 96.84 | 90.17 | -6.89% |
| Stablecoin supply | 15,490,673,443.00 | 14,838,258,165.00 | -4.21% |
| 24h DEX volume | 2,398,568,001.19 | 1,855,725,891.85 | -22.63% |
| 24h chain fees | 11,030,452.47 | 9,374,578.15 | -15.01% |

### Change over 30d (vs run at 2026-10-07T22:21:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,609.27 | 1,399.54 | -69.64% |
| Average non-vote TPS | 2,129.60 | 1,399.54 | -34.28% |
| Average slot time (ms) | 269.60 | 214.20 | -20.55% |
| Active validators | 671.00 | 659.00 | -1.79% |
| Delinquent validators | 10.00 | 37.00 | +270.00% |
| Solana TVL | 6,453,092,289.00 | 5,253,993,812.00 | -18.58% |
| SOL price | 115.61 | 90.17 | -22.01% |
| Stablecoin supply | 16,914,576,986.00 | 14,838,258,165.00 | -12.28% |
| 24h DEX volume | 2,052,545,605.65 | 1,855,725,891.85 | -9.59% |
| 24h chain fees | 16,052,631.31 | 9,374,578.15 | -41.60% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
