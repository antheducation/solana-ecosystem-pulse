# Solana Ecosystem Pulse

**Generated:** 2026-11-21T04:30:47Z · **Schema:** `1.0.0` · **Collection time:** 17.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $65.28 | -9.68% |
| Market cap | $38.61B | rank #7 |
| Total value locked | $4.55B | -3.91% |
| Stablecoin supply | $13.26B | -1.44% |
| DEX volume (24h) | $1.84B | -3.57% |
| Chain fees / REV (24h) | $8.96M | -3.51% |
| Non-vote TPS (1h avg) | 2,431 | peak 4,121 total |
| Active validators | 662 | 23 delinquent |
| Epoch 1092 | 60.58% complete | 170,298 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 133 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (down 9.7% in 24h) | SOL price changed -9.7% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,257,552,960.00 sits 3.3 sigma below the median of the last 133 runs (15,977,966,490.00, -17.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,430.9 average over the last 60 minutes; 2,099.8 in the latest sample.
- **Total TPS:** 2,430.9 average, 4,121.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.5 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 450,019,668 at absolute slot 472,005,702.
- **Epoch 1092:** slot 261,702 of 432,000 (60.58% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.548% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 187 ms |
| `solana-rpc.publicnode.com` | yes | 263 ms |
| `api.mainnet.solana.com` | yes | 108 ms |

## Validators & stake

- **662 active** validators, **23 delinquent** (3.36% by count, 0.017% by stake).
- **Total stake:** 428,985,797 SOL ($28.00B); stake rate 67.25% of total supply.
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

- **SOL:** $65.28 (-9.68% 24h, -13.02% 7d, -38.08% 30d). Market cap $38.61B, 24h volume $3.79B (9.81% of cap). Price source: `coingecko`.
- **TVL:** $4.55B across 342 protocols - rank #2 of 426 chains, 6.89% of all tracked chain TVL. -6.72% over 7d, -61.7% from its ATH.
- **Stablecoins:** $13.26B circulating on Solana (-6.81% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.84B in 24h, $10.67B over 7d across 144 venues. Volume/TVL turnover 0.403x per day.
- **REV (chain fees):** $8.96M in 24h, $294.00M over 30d. Retained chain revenue $3.01M (33.6% of fees). Annualised fees are 8.47% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,906,406 SOL circulating of 637,920,383 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.23B | -7.9% | -16.6% |
| 2 | Kamino Lend | Lending | $1.12B | -1.9% | -3.8% |
| 3 | Jupiter Lend | Lending | $945.19M | -3.0% | +0.2% |
| 4 | Raydium AMM | Dexs | $764.95M | -5.4% | -13.0% |
| 5 | Binance Staked SOL | Liquid Staking | $706.14M | -6.1% | -16.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $690.15M | -5.4% | -12.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $548.82M | -5.7% | -8.9% |
| 8 | Sentora Curator | Risk Curators | $355.80M | -0.4% | -0.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $342.08M | -8.1% | -13.9% |
| 10 | OnRe | RWA | $289.29M | -0.8% | -6.4% |
| 11 | Forward Industries SOL | Liquid Staking | $269.67M | -6.0% | -14.6% |
| 12 | CCIP | Bridge | $269.48M | -1.0% | -6.2% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 342 protocols the total is $11.50B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 39.7% · Lending 19.6% · Dexs 14.6% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.3%

### Tokenised assets

$784.82M of tokenised real-world assets and equities are locked on Solana - 6.823% of chain TVL.

- OnRe (RWA): $289.29M
- Huma (RWA): $231.27M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $39.81M
- Solomon USDv (Basis Trading): $8.71M

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

### Change over 24h (vs run at 2026-11-20T05:26:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,702.06 | 2,430.89 | +42.82% |
| Average non-vote TPS | 1,702.06 | 2,430.89 | +42.82% |
| Average slot time (ms) | 215.00 | 215.50 | +0.23% |
| Active validators | 659.00 | 662.00 | +0.46% |
| Delinquent validators | 26.00 | 23.00 | -11.54% |
| Solana TVL | 4,734,235,007.00 | 4,553,805,751.00 | -3.81% |
| SOL price | 72.02 | 65.28 | -9.36% |
| Stablecoin supply | 13,453,468,145.00 | 13,257,552,960.00 | -1.46% |
| 24h DEX volume | 1,847,338,570.06 | 1,836,080,739.35 | -0.61% |
| 24h chain fees | 9,565,396.59 | 8,962,669.20 | -6.30% |

### Change over 7d (vs run at 2026-11-14T03:48:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,775.45 | 2,430.89 | +36.92% |
| Average non-vote TPS | 1,775.45 | 2,430.89 | +36.92% |
| Average slot time (ms) | 214.90 | 215.50 | +0.28% |
| Active validators | 663.00 | 662.00 | -0.15% |
| Delinquent validators | 36.00 | 23.00 | -36.11% |
| Solana TVL | 4,895,736,754.00 | 4,553,805,751.00 | -6.98% |
| SOL price | 75.18 | 65.28 | -13.17% |
| Stablecoin supply | 14,224,740,618.00 | 13,257,552,960.00 | -6.80% |
| 24h DEX volume | 1,453,256,848.20 | 1,836,080,739.35 | +26.34% |
| 24h chain fees | 9,338,440.34 | 8,962,669.20 | -4.02% |

### Change over 30d (vs run at 2026-10-21T20:57:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,089.84 | 2,430.89 | +16.32% |
| Average non-vote TPS | 2,089.84 | 2,430.89 | +16.32% |
| Average slot time (ms) | 213.00 | 215.50 | +1.17% |
| Active validators | 668.00 | 662.00 | -0.90% |
| Delinquent validators | 9.00 | 23.00 | +155.56% |
| Solana TVL | 6,055,835,656.00 | 4,553,805,751.00 | -24.80% |
| SOL price | 108.08 | 65.28 | -39.60% |
| Stablecoin supply | 16,012,993,627.00 | 13,257,552,960.00 | -17.21% |
| 24h DEX volume | 2,437,800,216.24 | 1,836,080,739.35 | -24.68% |
| 24h chain fees | 13,174,208.40 | 8,962,669.20 | -31.97% |

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
