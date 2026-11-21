# Solana Ecosystem Pulse

**Generated:** 2026-11-21T13:47:47Z · **Schema:** `1.0.0` · **Collection time:** 22.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.37 | -0.48% |
| Market cap | $41.65B | rank #7 |
| Total value locked | $4.55B | -3.92% |
| Stablecoin supply | $13.26B | -1.43% |
| DEX volume (24h) | $1.88B | -1.02% |
| Chain fees / REV (24h) | $8.29M | -10.86% |
| Non-vote TPS (1h avg) | 1,480 | peak 3,218 total |
| Active validators | 662 | 23 delinquent |
| Epoch 1092 | 96.58% complete | 14,795 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 134 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,480; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,258,597,026.00 sits 3.2 sigma below the median of the last 134 runs (15,973,982,918.00, -17.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,480.3 average over the last 60 minutes; 1,782.4 in the latest sample.
- **Total TPS:** 1,480.3 average, 3,218.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.8 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 450,175,163 at absolute slot 472,161,205.
- **Epoch 1092:** slot 417,205 of 432,000 (96.58% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.548% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 616 ms |
| `solana-rpc.publicnode.com` | yes | 106 ms |
| `api.mainnet.solana.com` | yes | 327 ms |

## Validators & stake

- **662 active** validators, **23 delinquent** (3.36% by count, 0.017% by stake).
- **Total stake:** 428,985,797 SOL ($30.19B); stake rate 67.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.82% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 13.02%; 219 validators at 0% and 63 at 100%.

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

- **SOL:** $70.37 (-0.48% 24h, -6.87% 7d, -32.54% 30d). Market cap $41.65B, 24h volume $4.91B (11.79% of cap). Price source: `coingecko`.
- **TVL:** $4.55B across 342 protocols - rank #2 of 426 chains, 6.80% of all tracked chain TVL. -6.73% over 7d, -61.7% from its ATH.
- **Stablecoins:** $13.26B circulating on Solana (-6.81% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.88B in 24h, $11.64B over 7d across 144 venues. Volume/TVL turnover 0.414x per day.
- **REV (chain fees):** $8.29M in 24h, $295.33M over 30d. Retained chain revenue $2.82M (34.0% of fees). Annualised fees are 7.26% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,906,279 SOL circulating of 637,920,261 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.27B | -3.0% | -14.0% |
| 2 | Kamino Lend | Lending | $1.12B | -1.9% | -3.9% |
| 3 | Jupiter Lend | Lending | $941.78M | -2.0% | -0.2% |
| 4 | Raydium AMM | Dexs | $765.50M | -4.5% | -12.9% |
| 5 | Binance Staked SOL | Liquid Staking | $712.03M | -4.1% | -16.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $693.22M | -3.0% | -12.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $557.42M | -3.0% | -7.5% |
| 8 | Sentora Curator | Risk Curators | $356.30M | -0.3% | -0.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $354.41M | -2.0% | -10.8% |
| 10 | OnRe | RWA | $287.66M | -1.3% | -6.9% |
| 11 | Forward Industries SOL | Liquid Staking | $271.92M | -2.6% | -13.9% |
| 12 | CCIP | Bridge | $268.16M | -1.4% | -6.6% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 342 protocols the total is $11.59B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.1% · Lending 19.4% · Dexs 14.4% · Derivatives 5.3% · RWA 4.5% · Risk Curators 4.3%

### Tokenised assets

$777.22M of tokenised real-world assets and equities are locked on Solana - 6.708% of chain TVL.

- OnRe (RWA): $287.66M
- Huma (RWA): $225.65M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $39.47M
- Solomon USDv (Basis Trading): $8.72M

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

- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19

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

### Change over 24h (vs run at 2026-11-20T14:29:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,759.75 | 1,480.30 | -15.88% |
| Average non-vote TPS | 1,759.75 | 1,480.30 | -15.88% |
| Average slot time (ms) | 215.50 | 214.80 | -0.32% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 24.00 | 23.00 | -4.17% |
| Solana TVL | 4,677,758,004.00 | 4,553,427,239.00 | -2.66% |
| SOL price | 71.48 | 70.37 | -1.55% |
| Stablecoin supply | 13,454,137,376.00 | 13,258,597,026.00 | -1.45% |
| 24h DEX volume | 1,904,151,628.06 | 1,884,688,033.35 | -1.02% |
| 24h chain fees | 9,305,684.54 | 8,289,486.06 | -10.92% |

### Change over 7d (vs run at 2026-11-14T12:36:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,007.94 | 1,480.30 | +46.86% |
| Average non-vote TPS | 1,007.94 | 1,480.30 | +46.86% |
| Average slot time (ms) | 215.10 | 214.80 | -0.14% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 37.00 | 23.00 | -37.84% |
| Solana TVL | 4,838,103,678.00 | 4,553,427,239.00 | -5.88% |
| SOL price | 75.83 | 70.37 | -7.20% |
| Stablecoin supply | 14,224,715,424.00 | 13,258,597,026.00 | -6.79% |
| 24h DEX volume | 1,560,618,093.20 | 1,884,688,033.35 | +20.77% |
| 24h chain fees | 9,143,724.07 | 8,289,486.06 | -9.34% |

### Change over 30d (vs run at 2026-10-22T20:55:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,984.31 | 1,480.30 | -50.40% |
| Average non-vote TPS | 2,984.31 | 1,480.30 | -50.40% |
| Average slot time (ms) | 196.40 | 214.80 | +9.37% |
| Active validators | 655.00 | 662.00 | +1.07% |
| Delinquent validators | 21.00 | 23.00 | +9.52% |
| Solana TVL | 5,883,924,131.00 | 4,553,427,239.00 | -22.61% |
| SOL price | 103.14 | 70.37 | -31.77% |
| Stablecoin supply | 16,152,572,344.00 | 13,258,597,026.00 | -17.92% |
| 24h DEX volume | 2,270,402,206.37 | 1,884,688,033.35 | -16.99% |
| 24h chain fees | 11,957,946.66 | 8,289,486.06 | -30.68% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
