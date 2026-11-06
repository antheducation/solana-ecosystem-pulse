# Solana Ecosystem Pulse

**Generated:** 2026-11-06T22:28:12Z · **Schema:** `1.0.0` · **Collection time:** 21.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $90.17 | +0.46% |
| Market cap | $53.23B | rank #7 |
| Total value locked | $5.24B | -5.78% |
| Stablecoin supply | $15.03B | -0.98% |
| DEX volume (24h) | $2.20B | -7.85% |
| Chain fees / REV (24h) | $9.71M | -14.17% |
| Non-vote TPS (1h avg) | 2,010 | peak 3,590 total |
| Active validators | 659 | 37 delinquent |
| Epoch 1079 | 34.51% complete | 282,903 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,010.3 average over the last 60 minutes; 2,236.8 in the latest sample.
- **Total TPS:** 2,010.3 average, 3,589.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.7 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 444,296,026 at absolute slot 466,277,097.
- **Epoch 1079:** slot 149,097 of 432,000 (34.51% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.568% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 101 ms |
| `solana-rpc.publicnode.com` | yes | 152 ms |
| `api.mainnet.solana.com` | yes | 137 ms |

## Validators & stake

- **659 active** validators, **37 delinquent** (5.32% by count, 0.321% by stake).
- **Total stake:** 434,917,723 SOL ($39.22B); stake rate 68.26% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.73% and top 33 hold 46.55% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 223 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,039,556 | 3.931% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,722,209 | 3.857% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,017,562 | 3.003% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,436,420 | 2.407% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,531,946 | 2.199% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,519,642 | 2.196% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,519 | 2.132% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,741,933 | 1.786% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,982,918 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,614 | 1.608% | 0% |

## Economics

- **SOL:** $90.17 (+0.46% 24h, -5.44% 7d, -22.02% 30d). Market cap $53.23B, 24h volume $2.62B (4.91% of cap). Price source: `coingecko`.
- **TVL:** $5.24B across 341 protocols - rank #3 of 421 chains, 6.49% of all tracked chain TVL. -2.42% over 7d, -59.5% from its ATH.
- **Stablecoins:** $15.03B circulating on Solana (-2.71% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.20B in 24h, $12.29B over 7d across 141 venues. Volume/TVL turnover 0.419x per day.
- **REV (chain fees):** $9.71M in 24h, $358.27M over 30d. Retained chain revenue $3.50M (36.0% of fees). Annualised fees are 6.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,342,553 SOL circulating of 637,127,790 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | +0.7% | -4.3% |
| 2 | Kamino Lend | Lending | $1.19B | -0.9% | -0.5% |
| 3 | Raydium AMM | Dexs | $1.02B | +1.5% | -6.7% |
| 4 | Binance Staked SOL | Liquid Staking | $975.74M | -0.4% | -3.0% |
| 5 | Jupiter Lend | Lending | $924.98M | -6.3% | +1.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $923.15M | -0.5% | -6.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $662.95M | +0.0% | -2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $458.61M | +1.1% | -4.8% |
| 9 | Sentora Curator | Risk Curators | $373.86M | +0.2% | -1.7% |
| 10 | Marinade Native | Staking Pool | $323.85M | +0.4% | -3.4% |
| 11 | PumpSwap | Dexs | $311.57M | +1.6% | -3.3% |
| 12 | OnRe | RWA | $308.55M | +0.0% | +1.5% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $14.01B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 16.8% · Dexs 15.2% · Derivatives 5.2% · RWA 4.3% · Risk Curators 3.8%

### Tokenised assets

$866.11M of tokenised real-world assets and equities are locked on Solana - 6.182% of chain TVL.

- OnRe (RWA): $308.55M
- Huma (RWA): $245.70M
- Solstice (Basis Trading): $201.04M
- JupUSD (Basis Trading): $45.15M
- Plume Vaults (RWA): $36.80M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-06
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-06
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06
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

### Change over 24h (vs run at 2026-11-05T22:57:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,837.49 | 2,010.28 | +9.40% |
| Average non-vote TPS | 1,837.49 | 2,010.28 | +9.40% |
| Average slot time (ms) | 213.90 | 214.70 | +0.37% |
| Active validators | 662.00 | 659.00 | -0.45% |
| Delinquent validators | 32.00 | 37.00 | +15.62% |
| Solana TVL | 5,293,425,753.00 | 5,241,110,141.00 | -0.99% |
| SOL price | 89.52 | 90.17 | +0.73% |
| Stablecoin supply | 15,182,475,286.00 | 15,033,474,849.00 | -0.98% |
| 24h DEX volume | 2,385,538,829.94 | 2,198,364,299.20 | -7.85% |
| 24h chain fees | 11,227,806.64 | 9,708,551.35 | -13.53% |

### Change over 7d (vs run at 2026-10-30T21:44:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,609.94 | 2,010.28 | +24.87% |
| Average non-vote TPS | 1,609.94 | 2,010.28 | +24.87% |
| Average slot time (ms) | 214.70 | 214.70 | +0.00% |
| Active validators | 666.00 | 659.00 | -1.05% |
| Delinquent validators | 25.00 | 37.00 | +48.00% |
| Solana TVL | 5,346,984,781.00 | 5,241,110,141.00 | -1.98% |
| SOL price | 95.38 | 90.17 | -5.46% |
| Stablecoin supply | 15,450,891,906.00 | 15,033,474,849.00 | -2.70% |
| 24h DEX volume | 2,295,364,281.70 | 2,198,364,299.20 | -4.23% |
| 24h chain fees | 12,329,690.27 | 9,708,551.35 | -21.26% |

### Change over 30d (vs run at 2026-10-07T22:21:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,609.27 | 2,010.28 | -56.39% |
| Average non-vote TPS | 2,129.60 | 2,010.28 | -5.60% |
| Average slot time (ms) | 269.60 | 214.70 | -20.36% |
| Active validators | 671.00 | 659.00 | -1.79% |
| Delinquent validators | 10.00 | 37.00 | +270.00% |
| Solana TVL | 6,453,092,289.00 | 5,241,110,141.00 | -18.78% |
| SOL price | 115.61 | 90.17 | -22.01% |
| Stablecoin supply | 16,914,576,986.00 | 15,033,474,849.00 | -11.12% |
| 24h DEX volume | 2,052,545,605.65 | 2,198,364,299.20 | +7.10% |
| 24h chain fees | 16,052,631.31 | 9,708,551.35 | -39.52% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
