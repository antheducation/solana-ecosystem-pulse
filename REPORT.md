# Solana Ecosystem Pulse

**Generated:** 2026-11-09T03:18:22Z · **Schema:** `1.0.0` · **Collection time:** 21.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $87.25 | -2.24% |
| Market cap | $51.59B | rank #7 |
| Total value locked | $5.13B | -1.03% |
| Stablecoin supply | $15.06B | -0.54% |
| DEX volume (24h) | $997.08M | +8.68% |
| Chain fees / REV (24h) | $8.30M | +3.74% |
| Non-vote TPS (1h avg) | 1,452 | peak 2,116 total |
| Active validators | 662 | 35 delinquent |
| Epoch 1081 | 39.77% complete | 260,192 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,452; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,452.4 average over the last 60 minutes; 1,716.3 in the latest sample.
- **Total TPS:** 1,452.4 average, 2,115.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.0 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 445,181,889 at absolute slot 467,163,808.
- **Epoch 1081:** slot 171,808 of 432,000 (39.77% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.565% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 185 ms |
| `solana-rpc.publicnode.com` | yes | 163 ms |
| `api.mainnet.solana.com` | yes | 257 ms |

## Validators & stake

- **662 active** validators, **35 delinquent** (5.02% by count, 0.144% by stake).
- **Total stake:** 433,920,561 SOL ($37.86B); stake rate 68.09% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.66% and top 33 hold 46.52% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 222 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,050,553 | 3.935% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,720,131 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,021,912 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,279,070 | 2.372% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,388 | 2.205% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,550,278 | 2.204% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,876 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,775,137 | 1.794% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,980,319 | 1.611% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,711,284 | 1.549% | 5% |

## Economics

- **SOL:** $87.25 (-2.24% 24h, -8.05% 7d, -20.56% 30d). Market cap $51.59B, 24h volume $2.06B (3.99% of cap). Price source: `coingecko`.
- **TVL:** $5.13B across 341 protocols - rank #3 of 422 chains, 6.47% of all tracked chain TVL. -6.50% over 7d, -60.3% from its ATH.
- **Stablecoins:** $15.06B circulating on Solana (-2.43% 7d) - $2.93 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $997.08M in 24h, $11.26B over 7d across 141 venues. Volume/TVL turnover 0.194x per day.
- **REV (chain fees):** $8.30M in 24h, $337.67M over 30d. Retained chain revenue $2.71M (32.7% of fees). Annualised fees are 5.87% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,093,732 SOL circulating of 637,249,973 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | -1.2% | -6.8% |
| 2 | Kamino Lend | Lending | $1.17B | -0.8% | -4.7% |
| 3 | Raydium AMM | Dexs | $985.28M | -1.7% | -7.8% |
| 4 | Binance Staked SOL | Liquid Staking | $955.63M | -1.4% | -7.2% |
| 5 | Jupiter Lend | Lending | $915.99M | -0.9% | -8.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $893.47M | -2.7% | -9.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $650.25M | -1.4% | -5.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $445.62M | -1.8% | -6.5% |
| 9 | Sentora Curator | Risk Curators | $374.22M | +0.1% | -0.6% |
| 10 | Marinade Native | Staking Pool | $315.74M | -1.2% | -7.8% |
| 11 | OnRe | RWA | $309.31M | +0.2% | +0.5% |
| 12 | PumpSwap | Dexs | $300.89M | -1.1% | -6.3% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.71B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 16.9% · Dexs 15.1% · Derivatives 5.2% · RWA 4.2% · Risk Curators 4.0%

### Tokenised assets

$845.05M of tokenised real-world assets and equities are locked on Solana - 6.162% of chain TVL.

- OnRe (RWA): $309.31M
- Huma (RWA): $224.95M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $44.03M
- Plume Vaults (RWA): $36.84M

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

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-06
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-06
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05

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

### Change over 24h (vs run at 2026-11-08T02:57:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,493.63 | 1,452.40 | -2.76% |
| Average non-vote TPS | 1,493.63 | 1,452.39 | -2.76% |
| Average slot time (ms) | 214.30 | 215.00 | +0.33% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 33.00 | 35.00 | +6.06% |
| Solana TVL | 5,215,961,212.00 | 5,134,576,425.00 | -1.56% |
| SOL price | 88.84 | 87.25 | -1.79% |
| Stablecoin supply | 14,932,755,317.00 | 15,064,026,289.00 | +0.88% |
| 24h DEX volume | 1,298,696,797.61 | 997,083,843.30 | -23.22% |
| 24h chain fees | 7,982,653.69 | 8,295,890.36 | +3.92% |

### Change over 7d (vs run at 2026-11-02T02:58:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,598.99 | 1,452.40 | -9.17% |
| Average non-vote TPS | 1,598.99 | 1,452.39 | -9.17% |
| Average slot time (ms) | 214.30 | 215.00 | +0.33% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 34.00 | 35.00 | +2.94% |
| Solana TVL | 5,488,771,465.00 | 5,134,576,425.00 | -6.45% |
| SOL price | 94.84 | 87.25 | -8.00% |
| Stablecoin supply | 15,444,373,984.00 | 15,064,026,289.00 | -2.46% |
| 24h DEX volume | 832,668,894.19 | 997,083,843.30 | +19.75% |
| 24h chain fees | 8,432,926.72 | 8,295,890.36 | -1.63% |

### Change over 30d (vs run at 2026-10-09T21:56:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,940.51 | 1,452.40 | -70.60% |
| Average non-vote TPS | 1,872.44 | 1,452.39 | -22.43% |
| Average slot time (ms) | 218.80 | 215.00 | -1.74% |
| Active validators | 674.00 | 662.00 | -1.78% |
| Delinquent validators | 6.00 | 35.00 | +483.33% |
| Solana TVL | 6,170,032,842.00 | 5,134,576,425.00 | -16.78% |
| SOL price | 108.92 | 87.25 | -19.90% |
| Stablecoin supply | 16,379,819,991.00 | 15,064,026,289.00 | -8.03% |
| 24h DEX volume | 2,644,852,886.24 | 997,083,843.30 | -62.30% |
| 24h chain fees | 15,072,203.23 | 8,295,890.36 | -44.96% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
