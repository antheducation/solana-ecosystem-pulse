# Solana Ecosystem Pulse

**Generated:** 2026-11-07T21:09:21Z · **Schema:** `1.0.0` · **Collection time:** 18.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $88.92 | -1.10% |
| Market cap | $52.55B | rank #7 |
| Total value locked | $5.23B | -1.12% |
| Stablecoin supply | $14.84B | -1.30% |
| DEX volume (24h) | $1.48B | -32.68% |
| Chain fees / REV (24h) | $9.30M | -4.65% |
| Non-vote TPS (1h avg) | 1,746 | peak 2,351 total |
| Active validators | 663 | 34 delinquent |
| Epoch 1080 | 22.69% complete | 333,981 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,746.4 average over the last 60 minutes; 1,665.7 in the latest sample.
- **Total TPS:** 1,746.4 average, 2,350.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.2 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 444,676,512 at absolute slot 466,658,019.
- **Epoch 1080:** slot 98,019 of 432,000 (22.69% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.567% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 217 ms |
| `solana-rpc.publicnode.com` | yes | 182 ms |
| `api.mainnet.solana.com` | yes | 140 ms |

## Validators & stake

- **663 active** validators, **34 delinquent** (4.88% by count, 0.152% by stake).
- **Total stake:** 434,780,965 SOL ($38.66B); stake rate 68.23% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.67% and top 33 hold 46.47% of active stake.
- **Commission:** median 5.0%, mean 12.98%; 223 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,043,402 | 3.926% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,729,016 | 3.854% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,015,291 | 2.998% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,277,563 | 2.367% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,558,411 | 2.202% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,520,070 | 2.193% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,242,930 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,750,589 | 1.785% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,983,623 | 1.609% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,973,337 | 1.606% | 0% |

## Economics

- **SOL:** $88.92 (-1.10% 24h, -7.02% 7d, -19.00% 30d). Market cap $52.55B, 24h volume $868.57M (1.65% of cap). Price source: `coingecko`.
- **TVL:** $5.23B across 341 protocols - rank #3 of 421 chains, 6.45% of all tracked chain TVL. -4.58% over 7d, -59.6% from its ATH.
- **Stablecoins:** $14.84B circulating on Solana (-4.24% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.48B in 24h, $11.66B over 7d across 141 venues. Volume/TVL turnover 0.283x per day.
- **REV (chain fees):** $9.30M in 24h, $353.30M over 30d. Retained chain revenue $3.34M (35.9% of fees). Annualised fees are 6.46% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,038,259 SOL circulating of 637,188,907 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | -0.4% | -6.3% |
| 2 | Kamino Lend | Lending | $1.19B | -0.0% | -4.3% |
| 3 | Raydium AMM | Dexs | $1.01B | -1.0% | -7.2% |
| 4 | Binance Staked SOL | Liquid Staking | $975.61M | -0.0% | -6.4% |
| 5 | Jupiter Lend | Lending | $927.75M | +0.2% | -0.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $919.00M | -0.5% | -7.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $660.89M | -0.2% | -4.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $457.19M | -0.3% | -7.7% |
| 9 | Sentora Curator | Risk Curators | $373.92M | +0.0% | -0.5% |
| 10 | Marinade Native | Staking Pool | $322.22M | -0.5% | -6.9% |
| 11 | OnRe | RWA | $308.53M | -0.0% | +0.3% |
| 12 | PumpSwap | Dexs | $308.48M | -1.0% | -6.5% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.95B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.9% · Dexs 15.1% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.9%

### Tokenised assets

$845.75M of tokenised real-world assets and equities are locked on Solana - 6.062% of chain TVL.

- OnRe (RWA): $308.53M
- Huma (RWA): $225.96M
- Solstice (Basis Trading): $201.16M
- JupUSD (Basis Trading): $44.35M
- Plume Vaults (RWA): $36.83M

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

### Change over 24h (vs run at 2026-11-06T22:28:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,010.28 | 1,746.41 | -13.13% |
| Average non-vote TPS | 2,010.28 | 1,746.41 | -13.13% |
| Average slot time (ms) | 214.70 | 214.20 | -0.23% |
| Active validators | 659.00 | 663.00 | +0.61% |
| Delinquent validators | 37.00 | 34.00 | -8.11% |
| Solana TVL | 5,241,110,141.00 | 5,227,801,801.00 | -0.25% |
| SOL price | 90.17 | 88.92 | -1.39% |
| Stablecoin supply | 15,033,474,849.00 | 14,838,386,518.00 | -1.30% |
| 24h DEX volume | 2,198,364,299.20 | 1,479,986,839.85 | -32.68% |
| 24h chain fees | 9,708,551.35 | 9,301,190.12 | -4.20% |

### Change over 7d (vs run at 2026-10-31T20:43:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,655.68 | 1,746.41 | +5.48% |
| Average non-vote TPS | 1,655.68 | 1,746.41 | +5.48% |
| Average slot time (ms) | 214.00 | 214.20 | +0.09% |
| Active validators | 665.00 | 663.00 | -0.30% |
| Delinquent validators | 27.00 | 34.00 | +25.93% |
| Solana TVL | 5,449,917,859.00 | 5,227,801,801.00 | -4.08% |
| SOL price | 95.56 | 88.92 | -6.95% |
| Stablecoin supply | 15,493,312,766.00 | 14,838,386,518.00 | -4.23% |
| 24h DEX volume | 2,117,396,479.19 | 1,479,986,839.85 | -30.10% |
| 24h chain fees | 11,233,221.43 | 9,301,190.12 | -17.20% |

### Change over 30d (vs run at 2026-10-08T22:33:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,632.43 | 1,746.41 | -62.30% |
| Average non-vote TPS | 2,125.38 | 1,746.41 | -17.83% |
| Average slot time (ms) | 267.50 | 214.20 | -19.93% |
| Active validators | 673.00 | 663.00 | -1.49% |
| Delinquent validators | 8.00 | 34.00 | +325.00% |
| Solana TVL | 6,248,086,909.00 | 5,227,801,801.00 | -16.33% |
| SOL price | 110.19 | 88.92 | -19.30% |
| Stablecoin supply | 16,607,983,518.00 | 14,838,386,518.00 | -10.66% |
| 24h DEX volume | 2,205,685,057.81 | 1,479,986,839.85 | -32.90% |
| 24h chain fees | 13,737,332.90 | 9,301,190.12 | -32.29% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
