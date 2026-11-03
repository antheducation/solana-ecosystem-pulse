# Solana Ecosystem Pulse

**Generated:** 2026-11-03T00:07:05Z · **Schema:** `1.0.0` · **Collection time:** 15.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $91.88 | -2.96% |
| Market cap | $54.23B | rank #7 |
| Total value locked | $5.36B | -1.30% |
| Stablecoin supply | $15.44B | -0.44% |
| DEX volume (24h) | $905.60M | -5.03% |
| Chain fees / REV (24h) | $8.39M | +1.48% |
| Non-vote TPS (1h avg) | 1,659 | peak 2,341 total |
| Active validators | 664 | 29 delinquent |
| Epoch 1075 | 67.33% complete | 141,147 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,658.8 average over the last 60 minutes; 1,853.5 in the latest sample.
- **Total TPS:** 1,658.8 average, 2,340.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.2 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 442,711,931 at absolute slot 464,690,853.
- **Epoch 1075:** slot 290,853 of 432,000 (67.33% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.575% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 88 ms |
| `solana-rpc.publicnode.com` | yes | 48 ms |
| `api.mainnet.solana.com` | yes | 166 ms |

## Validators & stake

- **664 active** validators, **29 delinquent** (4.18% by count, 1.043% by stake).
- **Total stake:** 434,160,766 SOL ($39.89B); stake rate 68.17% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.96% and top 33 hold 46.75% of active stake.
- **Commission:** median 5.0%, mean 12.83%; 224 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,034,354 | 3.965% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,199 | 3.889% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,037,180 | 3.035% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,429,501 | 2.428% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,109 | 2.230% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,453,055 | 2.200% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,805 | 2.148% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,803,392 | 1.816% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,891 | 1.630% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,978,080 | 1.624% | 5% |

## Economics

- **SOL:** $91.88 (-2.96% 24h, -8.81% 7d, -23.18% 30d). Market cap $54.23B, 24h volume $2.62B (4.84% of cap). Price source: `coingecko`.
- **TVL:** $5.36B across 336 protocols - rank #3 of 420 chains, 6.54% of all tracked chain TVL. -6.22% over 7d, -58.5% from its ATH.
- **Stablecoins:** $15.44B circulating on Solana (-2.59% 7d) - $2.88 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $905.60M in 24h, $11.66B over 7d across 141 venues. Volume/TVL turnover 0.169x per day.
- **REV (chain fees):** $8.39M in 24h, $381.61M over 30d. Retained chain revenue $3.12M (37.2% of fees). Annualised fees are 5.65% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,205,681 SOL circulating of 636,883,316 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.62B | -1.9% | -8.6% |
| 2 | Kamino Lend | Lending | $1.21B | -1.7% | -4.7% |
| 3 | Raydium AMM | Dexs | $1.03B | -2.5% | -9.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.00B | -2.4% | -6.5% |
| 5 | Jupiter Lend | Lending | $985.59M | -1.0% | -2.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $946.05M | -2.9% | -10.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $670.10M | -2.4% | -6.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $465.16M | -2.4% | -12.3% |
| 9 | Sentora Curator | Risk Curators | $373.23M | -0.8% | -3.6% |
| 10 | Marinade Native | Staking Pool | $329.40M | -3.1% | -9.5% |
| 11 | PumpSwap | Dexs | $311.53M | -1.5% | -7.5% |
| 12 | OnRe | RWA | $307.36M | -0.1% | +4.0% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 336 protocols the total is $14.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.1% · Dexs 15.1% · Derivatives 5.1% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$859.05M of tokenised real-world assets and equities are locked on Solana - 6.012% of chain TVL.

- OnRe (RWA): $307.36M
- Huma (RWA): $245.48M
- Solstice (Basis Trading): $201.45M
- JupUSD (Basis Trading): $39.04M
- Plume Vaults (RWA): $35.67M

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

- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-02
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-02
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-02
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-02
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-02
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
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

### Change over 24h (vs run at 2026-11-01T21:25:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,058.00 | 1,658.77 | -19.40% |
| Average non-vote TPS | 2,058.00 | 1,658.77 | -19.40% |
| Average slot time (ms) | 214.50 | 214.20 | -0.14% |
| Active validators | 662.00 | 664.00 | +0.30% |
| Delinquent validators | 34.00 | 29.00 | -14.71% |
| Solana TVL | 5,392,125,548.00 | 5,362,623,249.00 | -0.55% |
| SOL price | 94.18 | 91.88 | -2.44% |
| Stablecoin supply | 15,508,525,506.00 | 15,440,330,579.00 | -0.44% |
| 24h DEX volume | 953,585,251.19 | 905,602,298.19 | -5.03% |
| 24h chain fees | 8,270,455.08 | 8,394,709.28 | +1.50% |

### Change over 7d (vs run at 2026-10-26T21:59:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,853.07 | 1,658.77 | -10.49% |
| Average non-vote TPS | 1,853.06 | 1,658.77 | -10.48% |
| Average slot time (ms) | 211.90 | 214.20 | +1.09% |
| Active validators | 665.00 | 664.00 | -0.15% |
| Delinquent validators | 20.00 | 29.00 | +45.00% |
| Solana TVL | 5,710,299,220.00 | 5,362,623,249.00 | -6.09% |
| SOL price | 100.45 | 91.88 | -8.53% |
| Stablecoin supply | 15,849,510,602.00 | 15,440,330,579.00 | -2.58% |
| 24h DEX volume | 1,449,231,950.27 | 905,602,298.19 | -37.51% |
| 24h chain fees | 9,292,855.03 | 8,394,709.28 | -9.66% |

### Change over 30d (vs run at 2026-10-03T20:17:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,907.58 | 1,658.77 | -66.20% |
| Average non-vote TPS | 2,415.29 | 1,658.77 | -31.32% |
| Average slot time (ms) | 267.60 | 214.20 | -19.96% |
| Active validators | 670.00 | 664.00 | -0.90% |
| Delinquent validators | 15.00 | 29.00 | +93.33% |
| Solana TVL | 6,664,651,516.00 | 5,362,623,249.00 | -19.54% |
| SOL price | 119.93 | 91.88 | -23.39% |
| Stablecoin supply | 16,950,775,065.00 | 15,440,330,579.00 | -8.91% |
| 24h DEX volume | 2,760,296,309.96 | 905,602,298.19 | -67.19% |
| 24h chain fees | 17,402,246.04 | 8,394,709.28 | -51.76% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 15.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
