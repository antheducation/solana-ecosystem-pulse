# Solana Ecosystem Pulse

**Generated:** 2026-11-14T12:36:32Z · **Schema:** `1.0.0` · **Collection time:** 17.8s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.83 | -6.11% |
| Market cap | $44.85B | rank #7 |
| Total value locked | $4.84B | -3.77% |
| Stablecoin supply | $14.22B | -1.05% |
| DEX volume (24h) | $1.56B | +3.80% |
| Chain fees / REV (24h) | $9.14M | +14.46% |
| Non-vote TPS (1h avg) | 1,008 | peak 1,207 total |
| Active validators | 662 | 37 delinquent |
| Epoch 1086 | 41.23% complete | 253,890 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,008; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,007.9 average over the last 60 minutes; 978.5 in the latest sample.
- **Total TPS:** 1,007.9 average, 1,207.2 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 447,345,201 at absolute slot 469,330,110.
- **Epoch 1086:** slot 178,110 of 432,000 (41.23% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.557% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 96 ms |
| `solana-rpc.publicnode.com` | yes | 78 ms |
| `api.mainnet.solana.com` | yes | 118 ms |

## Validators & stake

- **662 active** validators, **37 delinquent** (5.29% by count, 0.092% by stake).
- **Total stake:** 429,651,631 SOL ($32.58B); stake rate 67.39% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.74% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 12.57%; 223 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,955,905 | 3.950% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,374,909 | 3.815% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,611,498 | 2.938% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,140,468 | 2.362% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,736,890 | 2.268% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,439 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,199,377 | 2.143% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,914,792 | 1.844% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,990,062 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,707,745 | 1.563% | 5% |

## Economics

- **SOL:** $75.83 (-6.11% 24h, -15.67% 7d, -25.75% 30d). Market cap $44.85B, 24h volume $3.32B (7.40% of cap). Price source: `coingecko`.
- **TVL:** $4.84B across 343 protocols - rank #3 of 423 chains, 6.54% of all tracked chain TVL. -7.94% over 7d, -59.3% from its ATH.
- **Stablecoins:** $14.22B circulating on Solana (-1.98% 7d) - $2.94 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.56B in 24h, $9.47B over 7d across 141 venues. Volume/TVL turnover 0.323x per day.
- **REV (chain fees):** $9.14M in 24h, $324.83M over 30d. Retained chain revenue $3.29M (36.0% of fees). Annualised fees are 7.44% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,573,843 SOL circulating of 637,554,805 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.42B | -1.5% | -11.4% |
| 2 | Kamino Lend | Lending | $1.15B | -2.2% | -2.9% |
| 3 | Jupiter Lend | Lending | $942.31M | -1.2% | +1.1% |
| 4 | Raydium AMM | Dexs | $872.27M | -4.5% | -14.3% |
| 5 | Binance Staked SOL | Liquid Staking | $792.87M | -9.1% | -19.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $770.83M | -6.3% | -16.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $590.78M | -3.6% | -11.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $387.83M | -6.1% | -15.7% |
| 9 | Sentora Curator | Risk Curators | $357.63M | -1.6% | -4.3% |
| 10 | OnRe | RWA | $308.37M | -0.2% | -0.1% |
| 11 | Forward Industries SOL | Liquid Staking | $305.85M | +20.4% | +7.6% |
| 12 | CCIP | Bridge | $287.17M | +9.4% | +8.2% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.60B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.1% · Lending 18.3% · Dexs 14.8% · Derivatives 5.2% · RWA 4.8% · Risk Curators 3.9%

### Tokenised assets

$863.38M of tokenised real-world assets and equities are locked on Solana - 6.852% of chain TVL.

- OnRe (RWA): $308.37M
- Huma (RWA): $248.61M
- Solstice (Basis Trading): $201.01M
- JupUSD (Basis Trading): $40.92M
- Plume Vaults (RWA): $37.01M

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

- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-12
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-12
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09

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

### Change over 24h (vs run at 2026-11-13T13:31:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,486.03 | 1,007.94 | -32.17% |
| Average non-vote TPS | 1,486.03 | 1,007.94 | -32.17% |
| Average slot time (ms) | 215.70 | 215.10 | -0.28% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 38.00 | 37.00 | -2.63% |
| Solana TVL | 5,000,564,115.00 | 4,838,103,678.00 | -3.25% |
| SOL price | 80.81 | 75.83 | -6.16% |
| Stablecoin supply | 14,375,541,339.00 | 14,224,715,424.00 | -1.05% |
| 24h DEX volume | 1,503,485,412.77 | 1,560,618,093.20 | +3.80% |
| 24h chain fees | 8,005,893.20 | 9,143,724.07 | +14.21% |

### Change over 7d (vs run at 2026-11-07T11:59:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,054.19 | 1,007.94 | -4.39% |
| Average non-vote TPS | 1,054.19 | 1,007.94 | -4.39% |
| Average slot time (ms) | 214.50 | 215.10 | +0.28% |
| Active validators | 660.00 | 662.00 | +0.30% |
| Delinquent validators | 36.00 | 37.00 | +2.78% |
| Solana TVL | 5,246,632,455.00 | 4,838,103,678.00 | -7.79% |
| SOL price | 89.91 | 75.83 | -15.66% |
| Stablecoin supply | 14,838,782,561.00 | 14,224,715,424.00 | -4.14% |
| 24h DEX volume | 1,479,986,839.85 | 1,560,618,093.20 | +5.45% |
| 24h chain fees | 9,264,218.12 | 9,143,724.07 | -1.30% |

### Change over 30d (vs run at 2026-10-15T20:36:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,323.17 | 1,007.94 | -81.07% |
| Average non-vote TPS | 2,236.62 | 1,007.94 | -54.93% |
| Average slot time (ms) | 216.50 | 215.10 | -0.65% |
| Active validators | 672.00 | 662.00 | -1.49% |
| Delinquent validators | 9.00 | 37.00 | +311.11% |
| Solana TVL | 6,044,693,032.00 | 4,838,103,678.00 | -19.96% |
| SOL price | 105.91 | 75.83 | -28.40% |
| Stablecoin supply | 16,055,865,871.00 | 14,224,715,424.00 | -11.40% |
| 24h DEX volume | 2,118,350,659.32 | 1,560,618,093.20 | -26.33% |
| 24h chain fees | 10,654,111.63 | 9,143,724.07 | -14.18% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 17.8s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
