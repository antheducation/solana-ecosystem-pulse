# Solana Ecosystem Pulse

**Generated:** 2026-11-03T13:07:24Z · **Schema:** `1.0.0` · **Collection time:** 16.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $92.81 | -1.22% |
| Market cap | $54.78B | rank #7 |
| Total value locked | $5.40B | -1.52% |
| Stablecoin supply | $15.37B | -0.44% |
| DEX volume (24h) | $1.83B | +102.16% |
| Chain fees / REV (24h) | $11.14M | +31.26% |
| Non-vote TPS (1h avg) | 1,523 | peak 2,418 total |
| Active validators | 664 | 29 delinquent |
| Epoch 1076 | 18.02% complete | 354,147 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | DEX volume moved sharply (up 102.2% in 24h) | DEX volume changed +102.2% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,522.6 average over the last 60 minutes; 1,337.9 in the latest sample.
- **Total TPS:** 1,522.6 average, 2,417.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.9 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 442,930,632 at absolute slot 464,909,853.
- **Epoch 1076:** slot 77,853 of 432,000 (18.02% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.573% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 70 ms |
| `solana-rpc.publicnode.com` | yes | 44 ms |
| `api.mainnet.solana.com` | yes | 60 ms |

## Validators & stake

- **664 active** validators, **29 delinquent** (4.18% by count, 0.508% by stake).
- **Total stake:** 434,699,177 SOL ($40.34B); stake rate 68.25% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.80% and top 33 hold 46.59% of active stake.
- **Commission:** median 5.0%, mean 12.66%; 226 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,030,641 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,704,340 | 3.862% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,043,664 | 3.016% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,431,126 | 2.412% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,561,007 | 2.211% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,435,905 | 2.182% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,232,746 | 2.135% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,810 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,008,986 | 1.621% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,979,031 | 1.614% | 5% |

## Economics

- **SOL:** $92.81 (-1.22% 24h, -7.93% 7d, -23.49% 30d). Market cap $54.78B, 24h volume $2.49B (4.55% of cap). Price source: `coingecko`.
- **TVL:** $5.40B across 336 protocols - rank #3 of 420 chains, 6.58% of all tracked chain TVL. -4.86% over 7d, -58.2% from its ATH.
- **Stablecoins:** $15.37B circulating on Solana (-2.49% 7d) - $2.85 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.83B in 24h, $11.39B over 7d across 141 venues. Volume/TVL turnover 0.339x per day.
- **REV (chain fees):** $11.14M in 24h, $385.25M over 30d. Retained chain revenue $3.74M (33.6% of fees). Annualised fees are 7.42% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,262,011 SOL circulating of 636,944,681 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.63B | -0.6% | -7.8% |
| 2 | Kamino Lend | Lending | $1.22B | -0.8% | -2.1% |
| 3 | Raydium AMM | Dexs | $1.03B | -2.3% | -8.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.01B | -1.6% | -6.0% |
| 5 | Jupiter Lend | Lending | $1.00B | +0.1% | -1.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $953.86M | -1.8% | -9.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $673.72M | -2.1% | -5.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $467.07M | -2.2% | -11.5% |
| 9 | Sentora Curator | Risk Curators | $373.34M | -1.1% | -2.8% |
| 10 | Marinade Native | Staking Pool | $332.06M | -2.0% | -8.5% |
| 11 | PumpSwap | Dexs | $313.92M | -2.0% | -4.7% |
| 12 | OnRe | RWA | $307.40M | +0.0% | +3.9% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 336 protocols the total is $14.33B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 17.2% · Dexs 15.1% · Derivatives 5.2% · RWA 3.9% · Risk Curators 3.8%

### Tokenised assets

$819.24M of tokenised real-world assets and equities are locked on Solana - 5.716% of chain TVL.

- OnRe (RWA): $307.40M
- Huma (RWA): $205.73M
- Solstice (Basis Trading): $201.37M
- JupUSD (Basis Trading): $39.05M
- Plume Vaults (RWA): $35.66M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-03
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-03
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-03
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-02
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-11-02T13:58:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,735.94 | 1,522.59 | -12.29% |
| Average non-vote TPS | 1,735.94 | 1,522.59 | -12.29% |
| Average slot time (ms) | 215.10 | 213.90 | -0.56% |
| Active validators | 666.00 | 664.00 | -0.30% |
| Delinquent validators | 28.00 | 29.00 | +3.57% |
| Solana TVL | 5,468,197,763.00 | 5,402,051,428.00 | -1.21% |
| SOL price | 94.34 | 92.81 | -1.62% |
| Stablecoin supply | 15,442,364,185.00 | 15,370,716,122.00 | -0.46% |
| 24h DEX volume | 905,602,298.19 | 1,830,732,933.50 | +102.16% |
| 24h chain fees | 8,395,340.05 | 11,140,650.50 | +32.70% |

### Change over 7d (vs run at 2026-10-27T11:09:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,484.87 | 1,522.59 | +2.54% |
| Average non-vote TPS | 1,484.87 | 1,522.59 | +2.54% |
| Average slot time (ms) | 212.80 | 213.90 | +0.52% |
| Active validators | 665.00 | 664.00 | -0.15% |
| Delinquent validators | 20.00 | 29.00 | +45.00% |
| Solana TVL | 5,681,242,565.00 | 5,402,051,428.00 | -4.91% |
| SOL price | 100.18 | 92.81 | -7.36% |
| Stablecoin supply | 15,762,299,946.00 | 15,370,716,122.00 | -2.48% |
| 24h DEX volume | 2,071,067,618.15 | 1,830,732,933.50 | -11.60% |
| 24h chain fees | 11,666,989.55 | 11,140,650.50 | -4.51% |

### Change over 30d (vs run at 2026-10-04T20:33:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,626.16 | 1,522.59 | -67.09% |
| Average non-vote TPS | 2,127.97 | 1,522.59 | -28.45% |
| Average slot time (ms) | 267.70 | 213.90 | -20.10% |
| Active validators | 671.00 | 664.00 | -1.04% |
| Delinquent validators | 15.00 | 29.00 | +93.33% |
| Solana TVL | 6,715,169,332.00 | 5,402,051,428.00 | -19.55% |
| SOL price | 120.79 | 92.81 | -23.16% |
| Stablecoin supply | 16,881,830,613.00 | 15,370,716,122.00 | -8.95% |
| 24h DEX volume | 1,553,984,451.11 | 1,830,732,933.50 | +17.81% |
| 24h chain fees | 12,930,244.69 | 11,140,650.50 | -13.84% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 16.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
