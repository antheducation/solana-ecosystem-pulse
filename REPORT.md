# Solana Ecosystem Pulse

**Generated:** 2026-11-08T21:25:16Z · **Schema:** `1.0.0` · **Collection time:** 27.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $89.02 | +0.29% |
| Market cap | $52.62B | rank #7 |
| Total value locked | $5.22B | -0.68% |
| Stablecoin supply | $15.15B | +0.62% |
| DEX volume (24h) | $917.44M | -38.01% |
| Chain fees / REV (24h) | $8.03M | -8.71% |
| Non-vote TPS (1h avg) | 1,720 | peak 2,391 total |
| Active validators | 660 | 37 delinquent |
| Epoch 1081 | 16.92% complete | 358,887 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,720.0 average over the last 60 minutes; 1,241.5 in the latest sample.
- **Total TPS:** 1,720.0 average, 2,391.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.6 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 445,083,266 at absolute slot 467,065,113.
- **Epoch 1081:** slot 73,113 of 432,000 (16.92% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.565% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 150 ms |
| `solana-rpc.publicnode.com` | yes | 143 ms |
| `api.mainnet.solana.com` | yes | 271 ms |

## Validators & stake

- **660 active** validators, **37 delinquent** (5.31% by count, 0.166% by stake).
- **Total stake:** 433,920,561 SOL ($38.63B); stake rate 68.09% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.67% and top 33 hold 46.53% of active stake.
- **Commission:** median 5.0%, mean 12.88%; 222 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,050,553 | 3.936% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,720,131 | 3.860% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,021,912 | 3.006% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,279,070 | 2.373% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,388 | 2.205% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,550,278 | 2.205% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,876 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,775,137 | 1.795% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,980,319 | 1.611% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,711,284 | 1.549% | 5% |

## Economics

- **SOL:** $89.02 (+0.29% 24h, -5.54% 7d, -18.29% 30d). Market cap $52.62B, 24h volume $950.64M (1.81% of cap). Price source: `coingecko`.
- **TVL:** $5.22B across 340 protocols - rank #3 of 422 chains, 6.45% of all tracked chain TVL. -4.06% over 7d, -59.6% from its ATH.
- **Stablecoins:** $15.15B circulating on Solana (-2.34% 7d) - $2.90 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $917.44M in 24h, $11.62B over 7d across 141 venues. Volume/TVL turnover 0.176x per day.
- **REV (chain fees):** $8.03M in 24h, $345.60M over 30d. Retained chain revenue $2.59M (32.2% of fees). Annualised fees are 5.57% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,093,734 SOL circulating of 637,250,074 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | -0.0% | -5.5% |
| 2 | Kamino Lend | Lending | $1.19B | +0.3% | -3.5% |
| 3 | Raydium AMM | Dexs | $1.00B | -0.3% | -6.5% |
| 4 | Binance Staked SOL | Liquid Staking | $974.84M | +0.2% | -5.6% |
| 5 | Jupiter Lend | Lending | $928.98M | +0.2% | +0.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $910.28M | -0.9% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $660.78M | -0.0% | -4.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $456.53M | +0.2% | -6.4% |
| 9 | Sentora Curator | Risk Curators | $374.38M | +0.1% | -0.3% |
| 10 | Marinade Native | Staking Pool | $321.95M | +0.0% | -6.2% |
| 11 | OnRe | RWA | $309.33M | +0.2% | +0.5% |
| 12 | PumpSwap | Dexs | $309.17M | +0.2% | -4.4% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 340 protocols the total is $13.93B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 16.9% · Dexs 15.1% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.9%

### Tokenised assets

$845.50M of tokenised real-world assets and equities are locked on Solana - 6.070% of chain TVL.

- OnRe (RWA): $309.33M
- Huma (RWA): $225.00M
- Solstice (Basis Trading): $201.08M
- JupUSD (Basis Trading): $44.34M
- Plume Vaults (RWA): $36.84M

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

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-06
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-06
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04

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

### Change over 24h (vs run at 2026-11-07T21:09:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,746.41 | 1,720.02 | -1.51% |
| Average non-vote TPS | 1,746.41 | 1,720.02 | -1.51% |
| Average slot time (ms) | 214.20 | 214.60 | +0.19% |
| Active validators | 663.00 | 660.00 | -0.45% |
| Delinquent validators | 34.00 | 37.00 | +8.82% |
| Solana TVL | 5,227,801,801.00 | 5,218,639,304.00 | -0.18% |
| SOL price | 88.92 | 89.02 | +0.11% |
| Stablecoin supply | 14,838,386,518.00 | 15,146,574,447.00 | +2.08% |
| 24h DEX volume | 1,479,986,839.85 | 917,438,831.61 | -38.01% |
| 24h chain fees | 9,301,190.12 | 8,033,239.47 | -13.63% |

### Change over 7d (vs run at 2026-11-01T21:25:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,058.00 | 1,720.02 | -16.42% |
| Average non-vote TPS | 2,058.00 | 1,720.02 | -16.42% |
| Average slot time (ms) | 214.50 | 214.60 | +0.05% |
| Active validators | 662.00 | 660.00 | -0.30% |
| Delinquent validators | 34.00 | 37.00 | +8.82% |
| Solana TVL | 5,392,125,548.00 | 5,218,639,304.00 | -3.22% |
| SOL price | 94.18 | 89.02 | -5.48% |
| Stablecoin supply | 15,508,525,506.00 | 15,146,574,447.00 | -2.33% |
| 24h DEX volume | 953,585,251.19 | 917,438,831.61 | -3.79% |
| 24h chain fees | 8,270,455.08 | 8,033,239.47 | -2.87% |

### Change over 30d (vs run at 2026-10-09T21:56:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,940.51 | 1,720.02 | -65.19% |
| Average non-vote TPS | 1,872.44 | 1,720.02 | -8.14% |
| Average slot time (ms) | 218.80 | 214.60 | -1.92% |
| Active validators | 674.00 | 660.00 | -2.08% |
| Delinquent validators | 6.00 | 37.00 | +516.67% |
| Solana TVL | 6,170,032,842.00 | 5,218,639,304.00 | -15.42% |
| SOL price | 108.92 | 89.02 | -18.27% |
| Stablecoin supply | 16,379,819,991.00 | 15,146,574,447.00 | -7.53% |
| 24h DEX volume | 2,644,852,886.24 | 917,438,831.61 | -65.31% |
| 24h chain fees | 15,072,203.23 | 8,033,239.47 | -46.70% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 27.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
