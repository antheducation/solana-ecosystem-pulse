# Solana Ecosystem Pulse

**Generated:** 2026-11-13T13:31:11Z · **Schema:** `1.0.0` · **Collection time:** 20.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $80.81 | -0.69% |
| Market cap | $47.80B | rank #7 |
| Total value locked | $5.00B | -1.24% |
| Stablecoin supply | $14.38B | +1.06% |
| DEX volume (24h) | $1.50B | -7.06% |
| Chain fees / REV (24h) | $8.01M | -21.45% |
| Non-vote TPS (1h avg) | 1,486 | peak 2,853 total |
| Active validators | 661 | 38 delinquent |
| Epoch 1085 | 51.84% complete | 208,056 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,486; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,486.0 average over the last 60 minutes; 2,853.1 in the latest sample.
- **Total TPS:** 1,486.0 average, 2,853.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.7 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 446,959,146 at absolute slot 468,943,944.
- **Epoch 1085:** slot 223,944 of 432,000 (51.84% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.559% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 176 ms |
| `solana-rpc.publicnode.com` | yes | 132 ms |
| `api.mainnet.solana.com` | yes | 168 ms |

## Validators & stake

- **661 active** validators, **38 delinquent** (5.44% by count, 0.132% by stake).
- **Total stake:** 432,410,499 SOL ($34.94B); stake rate 67.83% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.58% and top 33 hold 46.41% of active stake.
- **Commission:** median 5.0%, mean 12.73%; 223 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,755 | 3.894% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,140,175 | 3.738% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,976,229 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,722 | 2.343% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,699,456 | 2.246% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,578,398 | 2.218% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,076 | 2.140% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,863,387 | 1.821% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,989,060 | 1.618% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,712,617 | 1.554% | 5% |

## Economics

- **SOL:** $80.81 (-0.69% 24h, -10.35% 7d, -23.35% 30d). Market cap $47.80B, 24h volume $3.28B (6.86% of cap). Price source: `coingecko`.
- **TVL:** $5.00B across 343 protocols - rank #3 of 423 chains, 6.62% of all tracked chain TVL. -5.45% over 7d, -60.1% from its ATH.
- **Stablecoins:** $14.38B circulating on Solana (-1.41% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.50B in 24h, $9.39B over 7d across 141 venues. Volume/TVL turnover 0.301x per day.
- **REV (chain fees):** $8.01M in 24h, $327.36M over 30d. Retained chain revenue $2.93M (36.6% of fees). Annualised fees are 6.11% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,511,014 SOL circulating of 637,493,735 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.44B | -1.7% | -9.0% |
| 2 | Kamino Lend | Lending | $1.18B | +2.7% | -1.3% |
| 3 | Jupiter Lend | Lending | $954.21M | +0.1% | -3.0% |
| 4 | Raydium AMM | Dexs | $922.99M | -2.4% | -8.0% |
| 5 | Binance Staked SOL | Liquid Staking | $875.27M | -2.2% | -10.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $824.68M | -2.6% | -10.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $613.75M | -2.1% | -7.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $413.04M | -1.8% | -9.0% |
| 9 | Sentora Curator | Risk Curators | $363.54M | -0.0% | -2.7% |
| 10 | OnRe | RWA | $308.93M | -0.2% | +0.1% |
| 11 | Orca DEX | Dexs | $268.17M | -0.3% | -5.3% |
| 12 | PumpSwap | Dexs | $266.40M | -1.4% | -13.9% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.5% · Lending 18.1% · Dexs 14.9% · Derivatives 5.2% · RWA 4.5% · Risk Curators 4.0%

### Tokenised assets

$839.17M of tokenised real-world assets and equities are locked on Solana - 6.441% of chain TVL.

- OnRe (RWA): $308.93M
- Huma (RWA): $224.17M
- Solstice (Basis Trading): $201.04M
- JupUSD (Basis Trading): $41.14M
- Plume Vaults (RWA): $37.06M

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

### Change over 24h (vs run at 2026-11-12T14:06:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,949.09 | 1,486.03 | -23.76% |
| Average non-vote TPS | 1,949.09 | 1,486.03 | -23.76% |
| Average slot time (ms) | 215.20 | 215.70 | +0.23% |
| Active validators | 661.00 | 661.00 | +0.00% |
| Delinquent validators | 37.00 | 38.00 | +2.70% |
| Solana TVL | 5,045,244,828.00 | 5,000,564,115.00 | -0.89% |
| SOL price | 81.25 | 80.81 | -0.54% |
| Stablecoin supply | 14,223,898,249.00 | 14,375,541,339.00 | +1.07% |
| 24h DEX volume | 1,617,758,399.95 | 1,503,485,412.77 | -7.06% |
| 24h chain fees | 10,185,070.88 | 8,005,893.20 | -21.40% |

### Change over 7d (vs run at 2026-11-06T13:20:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,430.24 | 1,486.03 | +3.90% |
| Average non-vote TPS | 1,430.24 | 1,486.03 | +3.90% |
| Average slot time (ms) | 213.80 | 215.70 | +0.89% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 32.00 | 38.00 | +18.75% |
| Solana TVL | 5,312,901,284.00 | 5,000,564,115.00 | -5.88% |
| SOL price | 90.05 | 80.81 | -10.26% |
| Stablecoin supply | 15,031,918,557.00 | 14,375,541,339.00 | -4.37% |
| 24h DEX volume | 2,198,364,299.20 | 1,503,485,412.77 | -31.61% |
| 24h chain fees | 9,633,288.35 | 8,005,893.20 | -16.89% |

### Change over 30d (vs run at 2026-10-14T21:02:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,462.84 | 1,486.03 | -72.80% |
| Average non-vote TPS | 2,373.93 | 1,486.03 | -37.40% |
| Average slot time (ms) | 216.90 | 215.70 | -0.55% |
| Active validators | 673.00 | 661.00 | -1.78% |
| Delinquent validators | 5.00 | 38.00 | +660.00% |
| Solana TVL | 5,960,534,531.00 | 5,000,564,115.00 | -16.11% |
| SOL price | 104.03 | 80.81 | -22.32% |
| Stablecoin supply | 16,320,492,053.00 | 14,375,541,339.00 | -11.92% |
| 24h DEX volume | 2,495,170,004.38 | 1,503,485,412.77 | -39.74% |
| 24h chain fees | 11,775,288.16 | 8,005,893.20 | -32.01% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
