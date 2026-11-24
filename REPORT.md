# Solana Ecosystem Pulse

**Generated:** 2026-11-24T03:31:46Z · **Schema:** `1.0.0` · **Collection time:** 22.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.79 | -0.71% |
| Market cap | $41.94B | rank #7 |
| Total value locked | $4.67B | +0.24% |
| Stablecoin supply | $13.89B | +3.59% |
| DEX volume (24h) | $1.41B | +44.04% |
| Chain fees / REV (24h) | $8.06M | +36.73% |
| Non-vote TPS (1h avg) | 1,744 | peak 2,740 total |
| Active validators | 659 | 27 delinquent |
| Epoch 1095 | 35.81% complete | 277,286 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 135 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.6% in 24h) | Stablecoin supply changed +3.6% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 44.0% in 24h) | DEX volume changed +44.0% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,744.1 average over the last 60 minutes; 1,710.8 in the latest sample.
- **Total TPS:** 1,744.1 average, 2,739.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 451,207,910 at absolute slot 473,194,714.
- **Epoch 1095:** slot 154,714 of 432,000 (35.81% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.543% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 181 ms |
| `solana-rpc.publicnode.com` | yes | 142 ms |
| `api.mainnet.solana.com` | yes | 180 ms |

## Validators & stake

- **659 active** validators, **27 delinquent** (3.94% by count, 0.053% by stake).
- **Total stake:** 425,856,004 SOL ($30.15B); stake rate 66.74% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.98% and top 33 hold 46.69% of active stake.
- **Commission:** median 5.0%, mean 12.95%; 219 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,046 | 4.001% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,091,420 | 3.781% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,158 | 2.916% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,240,508 | 2.406% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,856,366 | 2.316% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,634,022 | 2.263% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,276,354 | 2.179% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,005,660 | 1.881% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,776 | 1.642% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,778,434 | 1.593% | 5% |

## Economics

- **SOL:** $70.79 (-0.71% 24h, -1.25% 7d, -30.84% 30d). Market cap $41.94B, 24h volume $3.73B (8.90% of cap). Price source: `coingecko`.
- **TVL:** $4.67B across 343 protocols - rank #3 of 426 chains, 6.74% of all tracked chain TVL. -1.33% over 7d, -60.7% from its ATH.
- **Stablecoins:** $13.89B circulating on Solana (-3.11% 7d) - $2.97 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.41B in 24h, $10.30B over 7d across 144 venues. Volume/TVL turnover 0.301x per day.
- **REV (chain fees):** $8.06M in 24h, $281.63M over 30d. Retained chain revenue $3.26M (40.4% of fees). Annualised fees are 7.01% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,071,801 SOL circulating of 638,103,182 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.32B | +2.0% | -1.0% |
| 2 | Kamino Lend | Lending | $1.12B | -1.2% | -1.4% |
| 3 | Jupiter Lend | Lending | $969.77M | +1.6% | +1.5% |
| 4 | Raydium AMM | Dexs | $802.63M | +2.3% | -3.4% |
| 5 | Binance Staked SOL | Liquid Staking | $738.02M | +2.2% | -0.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $719.76M | +1.8% | -0.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $575.57M | +1.3% | -0.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $372.08M | +2.3% | +0.9% |
| 9 | Sentora Curator | Risk Curators | $355.25M | +0.5% | -1.0% |
| 10 | OnRe | RWA | $289.89M | +0.8% | -1.9% |
| 11 | Forward Industries SOL | Liquid Staking | $282.15M | +2.2% | -2.2% |
| 12 | CCIP | Bridge | $263.22M | -1.4% | -4.4% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.92B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.6% · Lending 19.1% · Dexs 14.6% · Derivatives 5.3% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$781.49M of tokenised real-world assets and equities are locked on Solana - 6.558% of chain TVL.

- OnRe (RWA): $289.89M
- Huma (RWA): $227.58M
- Solstice (Basis Trading): $201.06M
- JupUSD (Basis Trading): $39.41M
- Solomon USDv (Basis Trading): $8.73M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-23
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-23
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-23
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-23
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20

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

### Change over 24h (vs run at 2026-11-23T04:22:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,592.63 | 1,744.10 | +9.51% |
| Average non-vote TPS | 1,592.63 | 1,744.10 | +9.51% |
| Average slot time (ms) | 215.20 | 215.10 | -0.05% |
| Active validators | 662.00 | 659.00 | -0.45% |
| Delinquent validators | 23.00 | 27.00 | +17.39% |
| Solana TVL | 4,633,186,578.00 | 4,673,622,755.00 | +0.87% |
| SOL price | 71.26 | 70.79 | -0.66% |
| Stablecoin supply | 13,406,423,988.00 | 13,888,339,896.00 | +3.59% |
| 24h DEX volume | 1,186,396,653.97 | 1,405,495,770.26 | +18.47% |
| 24h chain fees | 6,008,758.23 | 8,059,529.76 | +34.13% |

### Change over 7d (vs run at 2026-11-17T01:12:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,790.21 | 1,744.10 | -2.58% |
| Average non-vote TPS | 1,790.21 | 1,744.10 | -2.58% |
| Average slot time (ms) | 214.50 | 215.10 | +0.28% |
| Active validators | 662.00 | 659.00 | -0.45% |
| Delinquent validators | 37.00 | 27.00 | -27.03% |
| Solana TVL | 4,749,281,028.00 | 4,673,622,755.00 | -1.59% |
| SOL price | 71.58 | 70.79 | -1.10% |
| Stablecoin supply | 14,334,893,337.00 | 13,888,339,896.00 | -3.12% |
| 24h DEX volume | 1,381,573,830.86 | 1,405,495,770.26 | +1.73% |
| 24h chain fees | 7,253,029.76 | 8,059,529.76 | +11.12% |

### Change over 30d (vs run at 2026-10-24T19:54:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,955.01 | 1,744.10 | -10.79% |
| Average non-vote TPS | 1,955.01 | 1,744.10 | -10.79% |
| Average slot time (ms) | 212.50 | 215.10 | +1.22% |
| Active validators | 665.00 | 659.00 | -0.90% |
| Delinquent validators | 25.00 | 27.00 | +8.00% |
| Solana TVL | 5,717,401,347.00 | 4,673,622,755.00 | -18.26% |
| SOL price | 101.01 | 70.79 | -29.92% |
| Stablecoin supply | 15,925,693,948.00 | 13,888,339,896.00 | -12.79% |
| 24h DEX volume | 1,997,070,440.37 | 1,405,495,770.26 | -29.62% |
| 24h chain fees | 10,552,167.09 | 8,059,529.76 | -23.62% |

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
