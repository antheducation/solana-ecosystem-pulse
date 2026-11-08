# Solana Ecosystem Pulse

**Generated:** 2026-11-08T02:57:13Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $88.84 | -1.57% |
| Market cap | $52.51B | rank #7 |
| Total value locked | $5.22B | -0.38% |
| Stablecoin supply | $14.93B | +0.63% |
| DEX volume (24h) | $1.30B | -12.25% |
| Chain fees / REV (24h) | $7.98M | -9.22% |
| Non-vote TPS (1h avg) | 1,494 | peak 1,908 total |
| Active validators | 664 | 33 delinquent |
| Epoch 1080 | 45.21% complete | 236,689 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,494; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,493.6 average over the last 60 minutes; 1,752.0 in the latest sample.
- **Total TPS:** 1,493.6 average, 1,907.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 444,773,739 at absolute slot 466,755,311.
- **Epoch 1080:** slot 195,311 of 432,000 (45.21% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.567% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 154 ms |
| `solana-rpc.publicnode.com` | yes | 148 ms |
| `api.mainnet.solana.com` | yes | 158 ms |

## Validators & stake

- **664 active** validators, **33 delinquent** (4.73% by count, 0.145% by stake).
- **Total stake:** 434,780,965 SOL ($38.63B); stake rate 68.23% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.67% and top 33 hold 46.47% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 223 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,043,402 | 3.926% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,729,016 | 3.853% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,015,291 | 2.998% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,277,563 | 2.367% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,558,411 | 2.202% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,520,070 | 2.193% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,242,930 | 2.129% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,750,589 | 1.785% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,983,623 | 1.609% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,973,337 | 1.606% | 0% |

## Economics

- **SOL:** $88.84 (-1.57% 24h, -7.11% 7d, -18.78% 30d). Market cap $52.51B, 24h volume $854.38M (1.63% of cap). Price source: `coingecko`.
- **TVL:** $5.22B across 341 protocols - rank #3 of 421 chains, 6.43% of all tracked chain TVL. -4.08% over 7d, -59.7% from its ATH.
- **Stablecoins:** $14.93B circulating on Solana (-3.72% 7d) - $2.86 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.30B in 24h, $11.17B over 7d across 141 venues. Volume/TVL turnover 0.249x per day.
- **REV (chain fees):** $7.98M in 24h, $343.78M over 30d. Retained chain revenue $2.59M (32.5% of fees). Annualised fees are 5.55% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,038,169 SOL circulating of 637,188,817 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | -0.9% | -5.6% |
| 2 | Kamino Lend | Lending | $1.18B | -0.3% | -3.8% |
| 3 | Raydium AMM | Dexs | $1.01B | -1.0% | -6.2% |
| 4 | Binance Staked SOL | Liquid Staking | $971.71M | -1.1% | -5.9% |
| 5 | Jupiter Lend | Lending | $926.47M | -0.6% | -0.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $918.02M | -0.8% | -7.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $659.62M | -0.7% | -4.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $455.54M | -1.0% | -6.6% |
| 9 | Sentora Curator | Risk Curators | $373.98M | +0.0% | -0.5% |
| 10 | Marinade Native | Staking Pool | $320.45M | -1.5% | -6.7% |
| 11 | OnRe | RWA | $308.66M | +0.0% | +0.3% |
| 12 | PumpSwap | Dexs | $307.93M | -1.1% | -4.8% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.93B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.9% · Dexs 15.1% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.9%

### Tokenised assets

$845.02M of tokenised real-world assets and equities are locked on Solana - 6.068% of chain TVL.

- OnRe (RWA): $308.66M
- Huma (RWA): $225.16M
- Solstice (Basis Trading): $201.10M
- JupUSD (Basis Trading): $44.33M
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

### Change over 24h (vs run at 2026-11-07T03:28:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,399.54 | 1,493.63 | +6.72% |
| Average non-vote TPS | 1,399.54 | 1,493.63 | +6.72% |
| Average slot time (ms) | 214.20 | 214.30 | +0.05% |
| Active validators | 659.00 | 664.00 | +0.76% |
| Delinquent validators | 37.00 | 33.00 | -10.81% |
| Solana TVL | 5,253,993,812.00 | 5,215,961,212.00 | -0.72% |
| SOL price | 90.17 | 88.84 | -1.47% |
| Stablecoin supply | 14,838,258,165.00 | 14,932,755,317.00 | +0.64% |
| 24h DEX volume | 1,855,725,891.85 | 1,298,696,797.61 | -30.02% |
| 24h chain fees | 9,374,578.15 | 7,982,653.69 | -14.85% |

### Change over 7d (vs run at 2026-11-01T02:51:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,387.39 | 1,493.63 | +7.66% |
| Average non-vote TPS | 1,387.39 | 1,493.63 | +7.66% |
| Average slot time (ms) | 214.00 | 214.30 | +0.14% |
| Active validators | 665.00 | 664.00 | -0.15% |
| Delinquent validators | 27.00 | 33.00 | +22.22% |
| Solana TVL | 5,440,989,525.00 | 5,215,961,212.00 | -4.14% |
| SOL price | 95.46 | 88.84 | -6.93% |
| Stablecoin supply | 15,513,310,673.00 | 14,932,755,317.00 | -3.74% |
| 24h DEX volume | 1,443,069,906.19 | 1,298,696,797.61 | -10.00% |
| 24h chain fees | 8,582,329.70 | 7,982,653.69 | -6.99% |

### Change over 30d (vs run at 2026-10-08T22:33:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,632.43 | 1,493.63 | -67.76% |
| Average non-vote TPS | 2,125.38 | 1,493.63 | -29.72% |
| Average slot time (ms) | 267.50 | 214.30 | -19.89% |
| Active validators | 673.00 | 664.00 | -1.34% |
| Delinquent validators | 8.00 | 33.00 | +312.50% |
| Solana TVL | 6,248,086,909.00 | 5,215,961,212.00 | -16.52% |
| SOL price | 110.19 | 88.84 | -19.38% |
| Stablecoin supply | 16,607,983,518.00 | 14,932,755,317.00 | -10.09% |
| 24h DEX volume | 2,205,685,057.81 | 1,298,696,797.61 | -41.12% |
| 24h chain fees | 13,737,332.90 | 7,982,653.69 | -41.89% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
