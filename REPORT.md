# Solana Ecosystem Pulse

**Generated:** 2026-11-06T13:20:41Z · **Schema:** `1.0.0` · **Collection time:** 23.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $90.05 | -5.56% |
| Market cap | $53.15B | rank #7 |
| Total value locked | $5.31B | -4.43% |
| Stablecoin supply | $15.03B | -0.99% |
| DEX volume (24h) | $2.20B | -7.85% |
| Chain fees / REV (24h) | $9.63M | -14.28% |
| Non-vote TPS (1h avg) | 1,430 | peak 1,794 total |
| Active validators | 662 | 32 delinquent |
| Epoch 1078 | 99.11% complete | 3,827 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,430; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,430.2 average over the last 60 minutes; 1,536.0 in the latest sample.
- **Total TPS:** 1,430.2 average, 1,793.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.8 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 444,143,678 at absolute slot 466,124,173.
- **Epoch 1078:** slot 428,173 of 432,000 (99.11% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.570% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 126 ms |
| `solana-rpc.publicnode.com` | yes | 122 ms |
| `api.mainnet.solana.com` | yes | 287 ms |

## Validators & stake

- **662 active** validators, **32 delinquent** (4.61% by count, 0.150% by stake).
- **Total stake:** 430,872,482 SOL ($38.80B); stake rate 67.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.78% and top 33 hold 46.50% of active stake.
- **Commission:** median 5.0%, mean 12.84%; 224 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,063,613 | 3.966% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,736,546 | 3.890% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,020,024 | 3.026% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,434,901 | 2.425% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,530,733 | 2.215% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,459,109 | 2.199% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,692 | 2.144% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,860,096 | 1.827% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,477 | 1.625% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,293,076 | 1.463% | 0% |

## Economics

- **SOL:** $90.05 (-5.56% 24h, -6.90% 7d, -22.62% 30d). Market cap $53.15B, 24h volume $3.66B (6.89% of cap). Price source: `coingecko`.
- **TVL:** $5.31B across 340 protocols - rank #3 of 421 chains, 6.55% of all tracked chain TVL. -1.08% over 7d, -58.9% from its ATH.
- **Stablecoins:** $15.03B circulating on Solana (-2.72% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.20B in 24h, $12.29B over 7d across 141 venues. Volume/TVL turnover 0.414x per day.
- **REV (chain fees):** $9.63M in 24h, $356.09M over 30d. Retained chain revenue $3.47M (36.0% of fees). Annualised fees are 6.62% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,287,204 SOL circulating of 637,066,460 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | -5.0% | -4.3% |
| 2 | Kamino Lend | Lending | $1.20B | -4.0% | +0.3% |
| 3 | Raydium AMM | Dexs | $1.01B | -7.1% | -7.7% |
| 4 | Jupiter Lend | Lending | $999.05M | -3.0% | +10.1% |
| 5 | Binance Staked SOL | Liquid Staking | $987.31M | -5.7% | -1.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $926.93M | -7.1% | -5.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $664.92M | -3.7% | -2.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $459.58M | -5.7% | -4.6% |
| 9 | Sentora Curator | Risk Curators | $373.60M | +0.1% | -1.8% |
| 10 | Marinade Native | Staking Pool | $323.98M | -6.4% | -3.3% |
| 11 | PumpSwap | Dexs | $312.70M | -5.9% | -2.9% |
| 12 | OnRe | RWA | $308.54M | +0.3% | +1.5% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $14.10B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.3% · Dexs 15.0% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$855.26M of tokenised real-world assets and equities are locked on Solana - 6.065% of chain TVL.

- OnRe (RWA): $308.54M
- Huma (RWA): $237.64M
- Solstice (Basis Trading): $201.02M
- JupUSD (Basis Trading): $42.24M
- Plume Vaults (RWA): $36.79M

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

- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-05
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-05
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-05
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-05

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

### Change over 24h (vs run at 2026-11-05T13:37:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,603.34 | 1,430.24 | -10.80% |
| Average non-vote TPS | 1,603.34 | 1,430.24 | -10.80% |
| Average slot time (ms) | 213.80 | 213.80 | +0.00% |
| Active validators | 663.00 | 662.00 | -0.15% |
| Delinquent validators | 31.00 | 32.00 | +3.23% |
| Solana TVL | 5,577,510,303.00 | 5,312,901,284.00 | -4.74% |
| SOL price | 95.28 | 90.05 | -5.49% |
| Stablecoin supply | 15,183,394,102.00 | 15,031,918,557.00 | -1.00% |
| 24h DEX volume | 2,385,538,829.94 | 2,198,364,299.20 | -7.85% |
| 24h chain fees | 11,226,354.64 | 9,633,288.35 | -14.19% |

### Change over 7d (vs run at 2026-10-30T11:45:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,252.98 | 1,430.24 | +14.15% |
| Average non-vote TPS | 1,252.98 | 1,430.24 | +14.15% |
| Average slot time (ms) | 213.40 | 213.80 | +0.19% |
| Active validators | 667.00 | 662.00 | -0.75% |
| Delinquent validators | 24.00 | 32.00 | +33.33% |
| Solana TVL | 5,427,386,909.00 | 5,312,901,284.00 | -2.11% |
| SOL price | 96.65 | 90.05 | -6.83% |
| Stablecoin supply | 15,453,819,358.00 | 15,031,918,557.00 | -2.73% |
| 24h DEX volume | 2,295,364,281.70 | 2,198,364,299.20 | -4.23% |
| 24h chain fees | 12,327,710.27 | 9,633,288.35 | -21.86% |

### Change over 30d (vs run at 2026-10-07T22:21:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,609.27 | 1,430.24 | -68.97% |
| Average non-vote TPS | 2,129.60 | 1,430.24 | -32.84% |
| Average slot time (ms) | 269.60 | 213.80 | -20.70% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 10.00 | 32.00 | +220.00% |
| Solana TVL | 6,453,092,289.00 | 5,312,901,284.00 | -17.67% |
| SOL price | 115.61 | 90.05 | -22.11% |
| Stablecoin supply | 16,914,576,986.00 | 15,031,918,557.00 | -11.13% |
| 24h DEX volume | 2,052,545,605.65 | 2,198,364,299.20 | +7.10% |
| 24h chain fees | 16,052,631.31 | 9,633,288.35 | -39.99% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
