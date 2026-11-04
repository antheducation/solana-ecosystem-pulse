# Solana Ecosystem Pulse

**Generated:** 2026-11-04T03:36:32Z · **Schema:** `1.0.0` · **Collection time:** 49.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $91.05 | -0.71% |
| Market cap | $53.74B | rank #7 |
| Total value locked | $5.41B | -0.32% |
| Stablecoin supply | $14.90B | -3.08% |
| DEX volume (24h) | $1.87B | +1.13% |
| Chain fees / REV (24h) | $11.43M | +1.96% |
| Non-vote TPS (1h avg) | 2,160 | peak 3,288 total |
| Active validators | 666 | 27 delinquent |
| Epoch 1076 | 74.31% complete | 110,978 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 3.1% in 24h) | Stablecoin supply changed -3.1% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,159.6 average over the last 60 minutes; 1,886.7 in the latest sample.
- **Total TPS:** 2,159.6 average, 3,288.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.0 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 443,173,603 at absolute slot 465,153,022.
- **Epoch 1076:** slot 321,022 of 432,000 (74.31% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.573% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 1290 ms |
| `solana-rpc.publicnode.com` | yes | 154 ms |
| `api.mainnet.solana.com` | yes | 2611 ms |

## Validators & stake

- **666 active** validators, **27 delinquent** (3.90% by count, 0.419% by stake).
- **Total stake:** 434,699,177 SOL ($39.58B); stake rate 68.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.54% of active stake.
- **Commission:** median 5.0%, mean 12.79%; 225 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,030,641 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,704,340 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,043,664 | 3.013% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,431,126 | 2.410% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,561,007 | 2.209% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,435,905 | 2.180% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,232,746 | 2.133% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,810 | 1.805% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,008,986 | 1.619% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,979,031 | 1.612% | 5% |

## Economics

- **SOL:** $91.05 (-0.71% 24h, -10.32% 7d, -24.86% 30d). Market cap $53.74B, 24h volume $2.34B (4.36% of cap). Price source: `coingecko`.
- **TVL:** $5.41B across 337 protocols - rank #3 of 420 chains, 6.60% of all tracked chain TVL. -5.42% over 7d, -58.1% from its ATH.
- **Stablecoins:** $14.90B circulating on Solana (-5.59% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.87B in 24h, $10.81B over 7d across 141 venues. Volume/TVL turnover 0.346x per day.
- **REV (chain fees):** $11.43M in 24h, $375.54M over 30d. Retained chain revenue $4.27M (37.4% of fees). Annualised fees are 7.76% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,206,755 SOL circulating of 636,944,368 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.61B | -0.9% | -9.7% |
| 2 | Kamino Lend | Lending | $1.22B | -1.8% | -3.6% |
| 3 | Raydium AMM | Dexs | $1.03B | +0.2% | -9.7% |
| 4 | Jupiter Lend | Lending | $1.01B | -0.5% | +1.5% |
| 5 | Binance Staked SOL | Liquid Staking | $998.09M | -0.8% | -8.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $942.30M | -0.7% | -10.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $673.36M | +0.0% | -6.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $463.37M | -0.8% | -12.6% |
| 9 | Sentora Curator | Risk Curators | $373.69M | +0.1% | -2.6% |
| 10 | Marinade Native | Staking Pool | $329.95M | -0.2% | -9.1% |
| 11 | PumpSwap | Dexs | $311.69M | -0.0% | -9.7% |
| 12 | OnRe | RWA | $307.50M | +0.0% | +2.1% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 337 protocols the total is $14.28B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.4% · Dexs 15.2% · Derivatives 5.2% · RWA 4.0% · Risk Curators 3.8%

### Tokenised assets

$829.79M of tokenised real-world assets and equities are locked on Solana - 5.811% of chain TVL.

- OnRe (RWA): $307.50M
- Huma (RWA): $215.84M
- Solstice (Basis Trading): $201.42M
- JupUSD (Basis Trading): $39.08M
- Plume Vaults (RWA): $35.94M

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

- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-03
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-03
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-03
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
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

### Change over 24h (vs run at 2026-11-03T00:07:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,658.77 | 2,159.62 | +30.19% |
| Average non-vote TPS | 1,658.77 | 2,159.62 | +30.19% |
| Average slot time (ms) | 214.20 | 214.00 | -0.09% |
| Active validators | 664.00 | 666.00 | +0.30% |
| Delinquent validators | 29.00 | 27.00 | -6.90% |
| Solana TVL | 5,362,623,249.00 | 5,411,706,032.00 | +0.92% |
| SOL price | 91.88 | 91.05 | -0.90% |
| Stablecoin supply | 15,440,330,579.00 | 14,901,850,212.00 | -3.49% |
| 24h DEX volume | 905,602,298.19 | 1,873,448,962.90 | +106.87% |
| 24h chain fees | 8,394,709.28 | 11,428,987.75 | +36.15% |

### Change over 7d (vs run at 2026-10-28T02:47:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,716.48 | 2,159.62 | +25.82% |
| Average non-vote TPS | 1,716.48 | 2,159.62 | +25.82% |
| Average slot time (ms) | 213.20 | 214.00 | +0.38% |
| Active validators | 662.00 | 666.00 | +0.60% |
| Delinquent validators | 29.00 | 27.00 | -6.90% |
| Solana TVL | 5,734,907,585.00 | 5,411,706,032.00 | -5.64% |
| SOL price | 101.49 | 91.05 | -10.29% |
| Stablecoin supply | 15,779,317,711.00 | 14,901,850,212.00 | -5.56% |
| 24h DEX volume | 1,848,988,925.55 | 1,873,448,962.90 | +1.32% |
| 24h chain fees | 11,083,243.89 | 11,428,987.75 | +3.12% |

### Change over 30d (vs run at 2026-10-04T20:33:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,626.16 | 2,159.62 | -53.32% |
| Average non-vote TPS | 2,127.97 | 2,159.62 | +1.49% |
| Average slot time (ms) | 267.70 | 214.00 | -20.06% |
| Active validators | 671.00 | 666.00 | -0.75% |
| Delinquent validators | 15.00 | 27.00 | +80.00% |
| Solana TVL | 6,715,169,332.00 | 5,411,706,032.00 | -19.41% |
| SOL price | 120.79 | 91.05 | -24.62% |
| Stablecoin supply | 16,881,830,613.00 | 14,901,850,212.00 | -11.73% |
| 24h DEX volume | 1,553,984,451.11 | 1,873,448,962.90 | +20.56% |
| 24h chain fees | 12,930,244.69 | 11,428,987.75 | -11.61% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 49.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
