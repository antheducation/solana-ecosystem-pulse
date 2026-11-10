# Solana Ecosystem Pulse

**Generated:** 2026-11-10T22:36:44Z · **Schema:** `1.0.0` · **Collection time:** 23.2s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $82.98 | -4.22% |
| Market cap | $49.06B | rank #7 |
| Total value locked | $5.02B | -2.06% |
| Stablecoin supply | $14.83B | -1.54% |
| DEX volume (24h) | $1.49B | +42.59% |
| Chain fees / REV (24h) | $9.38M | +12.88% |
| Non-vote TPS (1h avg) | 1,899 | peak 3,316 total |
| Active validators | 658 | 41 delinquent |
| Epoch 1083 | 8.09% complete | 397,060 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 42.6% in 24h) | DEX volume changed +42.6% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 41.00 sits 3.0 sigma above the median of the last 129 runs (14.00, +192.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,898.7 average over the last 60 minutes; 1,773.4 in the latest sample.
- **Total TPS:** 1,898.7 average, 3,316.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.2 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 445,907,671 at absolute slot 467,890,940.
- **Epoch 1083:** slot 34,940 of 432,000 (8.09% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.562% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 167 ms |
| `solana-rpc.publicnode.com` | yes | 134 ms |
| `api.mainnet.solana.com` | yes | 150 ms |

## Validators & stake

- **658 active** validators, **41 delinquent** (5.87% by count, 0.230% by stake).
- **Total stake:** 433,423,964 SOL ($35.97B); stake rate 68.00% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.62% and top 33 hold 46.58% of active stake.
- **Commission:** median 5.0%, mean 12.63%; 221 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,764,485 | 3.877% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,564,685 | 3.831% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,031,625 | 3.014% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,254 | 2.340% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,644,051 | 2.230% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,571,015 | 2.213% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,999 | 2.135% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,330 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,248 | 1.616% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,729,845 | 1.556% | 5% |

## Economics

- **SOL:** $82.98 (-4.22% 24h, -11.35% 7d, -24.93% 30d). Market cap $49.06B, 24h volume $2.95B (6.02% of cap). Price source: `coingecko`.
- **TVL:** $5.02B across 342 protocols - rank #4 of 423 chains, 6.46% of all tracked chain TVL. -7.66% over 7d, -61.2% from its ATH.
- **Stablecoins:** $14.83B circulating on Solana (-4.27% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.49B in 24h, $11.39B over 7d across 141 venues. Volume/TVL turnover 0.297x per day.
- **REV (chain fees):** $9.38M in 24h, $335.63M over 30d. Retained chain revenue $3.08M (32.9% of fees). Annualised fees are 6.98% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,204,580 SOL circulating of 637,372,126 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.47B | -4.0% | -9.5% |
| 2 | Kamino Lend | Lending | $1.14B | -2.8% | -8.2% |
| 3 | Jupiter Lend | Lending | $960.59M | +5.7% | -5.2% |
| 4 | Raydium AMM | Dexs | $936.35M | -4.4% | -9.3% |
| 5 | Binance Staked SOL | Liquid Staking | $903.84M | -3.8% | -9.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $848.50M | -3.7% | -10.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $631.78M | -2.3% | -5.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $425.70M | -3.4% | -8.7% |
| 9 | Sentora Curator | Risk Curators | $374.53M | -0.0% | +0.3% |
| 10 | OnRe | RWA | $309.23M | -0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $286.06M | -6.2% | -13.4% |
| 12 | Orca DEX | Dexs | $273.56M | -1.6% | -4.7% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 342 protocols the total is $13.25B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.5% · Dexs 14.9% · Derivatives 5.2% · RWA 4.4% · Risk Curators 4.1%

### Tokenised assets

$844.30M of tokenised real-world assets and equities are locked on Solana - 6.373% of chain TVL.

- OnRe (RWA): $309.23M
- Huma (RWA): $225.58M
- Solstice (Basis Trading): $201.00M
- JupUSD (Basis Trading): $43.77M
- Plume Vaults (RWA): $36.89M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-10
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06

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

### Change over 24h (vs run at 2026-11-10T00:55:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,627.58 | 1,898.72 | +16.66% |
| Average non-vote TPS | 1,627.58 | 1,898.72 | +16.66% |
| Average slot time (ms) | 214.40 | 214.20 | -0.09% |
| Active validators | 657.00 | 658.00 | +0.15% |
| Delinquent validators | 41.00 | 41.00 | +0.00% |
| Solana TVL | 5,091,379,326.00 | 5,016,904,733.00 | -1.46% |
| SOL price | 86.31 | 82.98 | -3.86% |
| Stablecoin supply | 15,064,954,013.00 | 14,833,203,510.00 | -1.54% |
| 24h DEX volume | 1,204,191,616.64 | 1,487,777,537.32 | +23.55% |
| 24h chain fees | 8,676,028.36 | 9,382,942.72 | +8.15% |

### Change over 7d (vs run at 2026-11-03T22:38:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,437.77 | 1,898.72 | -22.11% |
| Average non-vote TPS | 2,437.77 | 1,898.72 | -22.11% |
| Average slot time (ms) | 215.00 | 214.20 | -0.37% |
| Active validators | 666.00 | 658.00 | -1.20% |
| Delinquent validators | 27.00 | 41.00 | +51.85% |
| Solana TVL | 5,464,894,047.00 | 5,016,904,733.00 | -8.20% |
| SOL price | 93.28 | 82.98 | -11.04% |
| Stablecoin supply | 15,373,798,720.00 | 14,833,203,510.00 | -3.52% |
| 24h DEX volume | 1,852,604,853.50 | 1,487,777,537.32 | -19.69% |
| 24h chain fees | 11,209,317.50 | 9,382,942.72 | -16.29% |

### Change over 30d (vs run at 2026-10-11T21:08:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.95 | 1,898.72 | -61.83% |
| Average non-vote TPS | 1,917.24 | 1,898.72 | -0.97% |
| Average slot time (ms) | 218.90 | 214.20 | -2.15% |
| Active validators | 672.00 | 658.00 | -2.08% |
| Delinquent validators | 9.00 | 41.00 | +355.56% |
| Solana TVL | 6,251,230,542.00 | 5,016,904,733.00 | -19.75% |
| SOL price | 110.93 | 82.98 | -25.20% |
| Stablecoin supply | 16,405,817,670.00 | 14,833,203,510.00 | -9.59% |
| 24h DEX volume | 1,286,316,590.57 | 1,487,777,537.32 | +15.66% |
| 24h chain fees | 11,936,417.92 | 9,382,942.72 | -21.39% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
