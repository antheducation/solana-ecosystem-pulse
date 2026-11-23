# Solana Ecosystem Pulse

**Generated:** 2026-11-23T16:40:16Z · **Schema:** `1.0.0` · **Collection time:** 17.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $74.68 | +5.95% |
| Market cap | $44.21B | rank #7 |
| Total value locked | $4.80B | +3.93% |
| Stablecoin supply | $13.41B | +0.33% |
| DEX volume (24h) | $975.74M | -27.50% |
| Chain fees / REV (24h) | $5.92M | -21.93% |
| Non-vote TPS (1h avg) | 2,782 | peak 3,736 total |
| Active validators | 659 | 26 delinquent |
| Epoch 1094 | 93.72% complete | 27,113 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 135 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,781.9 average over the last 60 minutes; 3,412.6 in the latest sample.
- **Total TPS:** 2,781.9 average, 3,735.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 451,026,263 at absolute slot 473,012,887.
- **Epoch 1094:** slot 404,887 of 432,000 (93.72% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.544% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 142 ms |
| `solana-rpc.publicnode.com` | yes | 36 ms |
| `api.mainnet.solana.com` | yes | 64 ms |

## Validators & stake

- **659 active** validators, **26 delinquent** (3.80% by count, 0.085% by stake).
- **Total stake:** 425,691,542 SOL ($31.79B); stake rate 66.72% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.02% and top 33 hold 46.69% of active stake.
- **Commission:** median 5.0%, mean 13.07%; 219 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,918,440 | 3.978% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,346,959 | 3.843% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,401,889 | 2.916% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,243,005 | 2.408% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,842,253 | 2.314% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,612,896 | 2.260% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,269,555 | 2.179% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,998,895 | 1.881% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,495 | 1.643% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,775,083 | 1.593% | 5% |

## Economics

- **SOL:** $74.68 (+5.95% 24h, +5.56% 7d, -25.08% 30d). Market cap $44.21B, 24h volume $3.23B (7.31% of cap). Price source: `coingecko`.
- **TVL:** $4.80B across 343 protocols - rank #3 of 426 chains, 6.75% of all tracked chain TVL. +2.12% over 7d, -59.6% from its ATH.
- **Stablecoins:** $13.41B circulating on Solana (-6.51% 7d) - $2.79 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $975.74M in 24h, $10.92B over 7d across 144 venues. Volume/TVL turnover 0.203x per day.
- **REV (chain fees):** $5.92M in 24h, $285.19M over 30d. Retained chain revenue $2.11M (35.7% of fees). Annualised fees are 4.89% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,016,592 SOL circulating of 638,042,193 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.41B | +8.7% | +4.9% |
| 2 | Kamino Lend | Lending | $1.16B | +2.2% | +3.0% |
| 3 | Jupiter Lend | Lending | $995.36M | +4.1% | +7.5% |
| 4 | Raydium AMM | Dexs | $802.56M | +2.3% | -3.5% |
| 5 | Binance Staked SOL | Liquid Staking | $783.77M | +8.4% | +3.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $770.65M | +8.9% | +6.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $602.37M | +5.6% | +4.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $395.34M | +9.2% | +6.0% |
| 9 | Sentora Curator | Risk Curators | $354.02M | -0.7% | -1.2% |
| 10 | Forward Industries SOL | Liquid Staking | $299.82M | +8.3% | +3.0% |
| 11 | OnRe | RWA | $289.67M | +0.8% | -4.2% |
| 12 | CCIP | Bridge | $263.56M | -1.4% | -5.3% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.39B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.6% · Lending 19.0% · Dexs 14.2% · Derivatives 5.3% · RWA 4.2% · Risk Curators 4.0%

### Tokenised assets

$777.44M of tokenised real-world assets and equities are locked on Solana - 6.275% of chain TVL.

- OnRe (RWA): $289.67M
- Huma (RWA): $223.65M
- Solstice (Basis Trading): $201.09M
- JupUSD (Basis Trading): $39.43M
- Solomon USDv (Basis Trading): $8.74M

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

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-23
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-23
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-23
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-23
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

### Change over 24h (vs run at 2026-11-22T13:41:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,279.20 | 2,781.90 | +117.47% |
| Average non-vote TPS | 1,279.20 | 2,781.90 | +117.47% |
| Average slot time (ms) | 215.20 | 215.10 | -0.05% |
| Active validators | 661.00 | 659.00 | -0.30% |
| Delinquent validators | 24.00 | 26.00 | +8.33% |
| Solana TVL | 4,650,170,865.00 | 4,802,924,182.00 | +3.28% |
| SOL price | 70.12 | 74.68 | +6.50% |
| Stablecoin supply | 13,366,255,308.00 | 13,408,007,454.00 | +0.31% |
| 24h DEX volume | 1,345,931,988.87 | 975,738,121.97 | -27.50% |
| 24h chain fees | 7,568,696.38 | 5,919,028.93 | -21.80% |

### Change over 7d (vs run at 2026-11-16T14:07:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,536.76 | 2,781.90 | +81.02% |
| Average non-vote TPS | 1,536.76 | 2,781.90 | +81.02% |
| Average slot time (ms) | 214.90 | 215.10 | +0.09% |
| Active validators | 662.00 | 659.00 | -0.45% |
| Delinquent validators | 37.00 | 26.00 | -29.73% |
| Solana TVL | 4,696,110,297.00 | 4,802,924,182.00 | +2.27% |
| SOL price | 70.75 | 74.68 | +5.55% |
| Stablecoin supply | 14,341,479,831.00 | 13,408,007,454.00 | -6.51% |
| 24h DEX volume | 1,352,559,060.09 | 975,738,121.97 | -27.86% |
| 24h chain fees | 7,199,120.53 | 5,919,028.93 | -17.78% |

### Change over 30d (vs run at 2026-10-24T19:54:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,955.01 | 2,781.90 | +42.30% |
| Average non-vote TPS | 1,955.01 | 2,781.90 | +42.30% |
| Average slot time (ms) | 212.50 | 215.10 | +1.22% |
| Active validators | 665.00 | 659.00 | -0.90% |
| Delinquent validators | 25.00 | 26.00 | +4.00% |
| Solana TVL | 5,717,401,347.00 | 4,802,924,182.00 | -15.99% |
| SOL price | 101.01 | 74.68 | -26.07% |
| Stablecoin supply | 15,925,693,948.00 | 13,408,007,454.00 | -15.81% |
| 24h DEX volume | 1,997,070,440.37 | 975,738,121.97 | -51.14% |
| 24h chain fees | 10,552,167.09 | 5,919,028.93 | -43.91% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 17.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
