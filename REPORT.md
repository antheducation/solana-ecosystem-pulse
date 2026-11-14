# Solana Ecosystem Pulse

**Generated:** 2026-11-14T03:48:05Z · **Schema:** `1.0.0` · **Collection time:** 18.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.18 | -4.72% |
| Market cap | $44.47B | rank #7 |
| Total value locked | $4.90B | -1.76% |
| Stablecoin supply | $14.22B | -1.05% |
| DEX volume (24h) | $1.45B | -3.34% |
| Chain fees / REV (24h) | $9.34M | +16.90% |
| Non-vote TPS (1h avg) | 1,775 | peak 2,784 total |
| Active validators | 663 | 36 delinquent |
| Epoch 1086 | 7.11% complete | 401,287 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,775.5 average over the last 60 minutes; 1,922.6 in the latest sample.
- **Total TPS:** 1,775.5 average, 2,784.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.9 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 447,197,852 at absolute slot 469,182,713.
- **Epoch 1086:** slot 30,713 of 432,000 (7.11% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.557% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 86 ms |
| `solana-rpc.publicnode.com` | yes | 66 ms |
| `api.mainnet.solana.com` | yes | 117 ms |

## Validators & stake

- **663 active** validators, **36 delinquent** (5.15% by count, 0.092% by stake).
- **Total stake:** 429,651,631 SOL ($32.30B); stake rate 67.39% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.74% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 12.69%; 225 validators at 0% and 61 at 100%.

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

- **SOL:** $75.18 (-4.72% 24h, -16.77% 7d, -27.18% 30d). Market cap $44.47B, 24h volume $3.64B (8.18% of cap). Price source: `coingecko`.
- **TVL:** $4.90B across 343 protocols - rank #3 of 423 chains, 6.60% of all tracked chain TVL. -6.84% over 7d, -58.8% from its ATH.
- **Stablecoins:** $14.22B circulating on Solana (-1.98% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.45B in 24h, $8.69B over 7d across 141 venues. Volume/TVL turnover 0.297x per day.
- **REV (chain fees):** $9.34M in 24h, $323.27M over 30d. Retained chain revenue $3.31M (35.4% of fees). Annualised fees are 7.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,573,950 SOL circulating of 637,554,911 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.41B | -2.0% | -11.6% |
| 2 | Kamino Lend | Lending | $1.16B | -1.6% | -2.2% |
| 3 | Jupiter Lend | Lending | $943.72M | -1.6% | +1.3% |
| 4 | Raydium AMM | Dexs | $900.30M | -3.5% | -11.5% |
| 5 | Binance Staked SOL | Liquid Staking | $790.07M | -10.1% | -19.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $766.17M | -7.3% | -17.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $590.23M | -4.6% | -11.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $386.03M | -6.6% | -16.1% |
| 9 | Sentora Curator | Risk Curators | $357.29M | -1.7% | -4.4% |
| 10 | OnRe | RWA | $308.89M | -0.1% | +0.1% |
| 11 | Forward Industries SOL | Liquid Staking | $304.77M | +20.1% | +7.2% |
| 12 | CCIP | Bridge | $287.15M | +9.4% | +8.2% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.67B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.9% · Lending 18.3% · Dexs 15.1% · Derivatives 5.1% · RWA 4.8% · Risk Curators 3.9%

### Tokenised assets

$863.91M of tokenised real-world assets and equities are locked on Solana - 6.818% of chain TVL.

- OnRe (RWA): $308.89M
- Huma (RWA): $248.63M
- Solstice (Basis Trading): $201.01M
- JupUSD (Basis Trading): $40.93M
- Plume Vaults (RWA): $37.04M

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

### Change over 24h (vs run at 2026-11-13T03:50:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,245.44 | 1,775.45 | -20.93% |
| Average non-vote TPS | 2,245.44 | 1,775.45 | -20.93% |
| Average slot time (ms) | 215.80 | 214.90 | -0.42% |
| Active validators | 659.00 | 663.00 | +0.61% |
| Delinquent validators | 40.00 | 36.00 | -10.00% |
| Solana TVL | 5,024,451,399.00 | 4,895,736,754.00 | -2.56% |
| SOL price | 78.76 | 75.18 | -4.55% |
| Stablecoin supply | 14,374,630,148.00 | 14,224,740,618.00 | -1.04% |
| 24h DEX volume | 1,511,008,694.77 | 1,453,256,848.20 | -3.82% |
| 24h chain fees | 8,490,485.20 | 9,338,440.34 | +9.99% |

### Change over 7d (vs run at 2026-11-07T03:28:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,399.54 | 1,775.45 | +26.86% |
| Average non-vote TPS | 1,399.54 | 1,775.45 | +26.86% |
| Average slot time (ms) | 214.20 | 214.90 | +0.33% |
| Active validators | 659.00 | 663.00 | +0.61% |
| Delinquent validators | 37.00 | 36.00 | -2.70% |
| Solana TVL | 5,253,993,812.00 | 4,895,736,754.00 | -6.82% |
| SOL price | 90.17 | 75.18 | -16.62% |
| Stablecoin supply | 14,838,258,165.00 | 14,224,740,618.00 | -4.13% |
| 24h DEX volume | 1,855,725,891.85 | 1,453,256,848.20 | -21.69% |
| 24h chain fees | 9,374,578.15 | 9,338,440.34 | -0.39% |

### Change over 30d (vs run at 2026-10-14T21:02:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,462.84 | 1,775.45 | -67.50% |
| Average non-vote TPS | 2,373.93 | 1,775.45 | -25.21% |
| Average slot time (ms) | 216.90 | 214.90 | -0.92% |
| Active validators | 673.00 | 663.00 | -1.49% |
| Delinquent validators | 5.00 | 36.00 | +620.00% |
| Solana TVL | 5,960,534,531.00 | 4,895,736,754.00 | -17.86% |
| SOL price | 104.03 | 75.18 | -27.73% |
| Stablecoin supply | 16,320,492,053.00 | 14,224,740,618.00 | -12.84% |
| 24h DEX volume | 2,495,170,004.38 | 1,453,256,848.20 | -41.76% |
| 24h chain fees | 11,775,288.16 | 9,338,440.34 | -20.69% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
