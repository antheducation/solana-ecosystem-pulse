# Solana Ecosystem Pulse

**Generated:** 2026-10-15T20:36:57Z · **Schema:** `1.0.0` · **Collection time:** 15.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.91 | +1.80% |
| Market cap | $62.42B | rank #7 |
| Total value locked | $6.04B | -0.04% |
| Stablecoin supply | $16.06B | -1.62% |
| DEX volume (24h) | $2.12B | -15.10% |
| Chain fees / REV (24h) | $10.65M | -10.54% |
| Non-vote TPS (1h avg) | 2,237 | peak 6,115 total |
| Active validators | 672 | 9 delinquent |
| Epoch 1058 | 73.41% complete | 114,849 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 107 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,236.6 average over the last 60 minutes; 2,212.3 in the latest sample.
- **Total TPS:** 5,323.2 average, 6,114.7 peak. Consensus votes account for 58.0% of all transactions.
- **Slot time:** 216.5 ms average (target 400 ms), worst 1-minute bucket 224.7 ms.
- **Block height:** 435,409,006 at absolute slot 457,373,151.
- **Epoch 1058:** slot 317,151 of 432,000 (73.41% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.602% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 138 ms |
| `solana-rpc.publicnode.com` | yes | 157 ms |
| `api.mainnet.solana.com` | yes | 123 ms |

## Validators & stake

- **672 active** validators, **9 delinquent** (1.32% by count, 0.024% by stake).
- **Total stake:** 437,887,641 SOL ($46.38B); stake rate 68.87% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.49% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.96%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,556,681 | 4.010% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,475,284 | 3.535% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,340,406 | 2.819% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,132,168 | 2.543% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,777,829 | 2.462% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,409,309 | 2.149% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,227,345 | 2.108% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,737,484 | 1.767% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,912,081 | 1.579% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,640,641 | 1.517% | 0% |

## Economics

- **SOL:** $105.91 (+1.80% 24h, -3.00% 7d, +8.24% 30d). Market cap $62.42B, 24h volume $4.31B (6.91% of cap). Price source: `coingecko`.
- **TVL:** $6.04B across 324 protocols - rank #3 of 425 chains, 6.69% of all tracked chain TVL. -6.32% over 7d, -54.5% from its ATH.
- **Stablecoins:** $16.06B circulating on Solana (-2.27% 7d) - $2.66 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.12B in 24h, $14.03B over 7d across 134 venues. Volume/TVL turnover 0.350x per day.
- **REV (chain fees):** $10.65M in 24h, $463.34M over 30d. Retained chain revenue $4.25M (39.9% of fees). Annualised fees are 6.23% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,268,216 SOL circulating of 635,844,059 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +1.6% | -6.7% |
| 2 | Kamino Lend | Lending | $1.32B | +0.3% | -2.8% |
| 3 | Raydium AMM | Dexs | $1.19B | +1.2% | -8.1% |
| 4 | Jupiter Lend | Lending | $1.13B | +3.9% | -6.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.11B | +1.6% | -8.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.09B | +1.7% | -8.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $749.33M | +1.5% | -5.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $553.32M | +1.7% | -8.2% |
| 9 | Sentora Curator | Risk Curators | $457.70M | +0.2% | -8.9% |
| 10 | Marinade Native | Staking Pool | $387.26M | +1.5% | -10.8% |
| 11 | PumpSwap | Dexs | $355.82M | +1.8% | -8.2% |
| 12 | Orca DEX | Dexs | $300.44M | -0.2% | -6.8% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 324 protocols the total is $16.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.0% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.8%

### Tokenised assets

$875.28M of tokenised real-world assets and equities are locked on Solana - 5.461% of chain TVL.

- OnRe (RWA): $292.25M
- Huma (RWA): $264.58M
- Solstice (Basis Trading): $209.34M
- JupUSD (Basis Trading): $44.66M
- Plume Vaults (RWA): $34.77M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-15
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-15
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-15
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-15
- [SIMD-0088: SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-14
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-14

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

### Change over 24h (vs run at 2026-10-14T21:02:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,462.84 | 5,323.17 | -2.56% |
| Average non-vote TPS | 2,373.93 | 2,236.62 | -5.78% |
| Average slot time (ms) | 216.90 | 216.50 | -0.18% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 5.00 | 9.00 | +80.00% |
| Solana TVL | 5,960,534,531.00 | 6,044,693,032.00 | +1.41% |
| SOL price | 104.03 | 105.91 | +1.81% |
| Stablecoin supply | 16,320,492,053.00 | 16,055,865,871.00 | -1.62% |
| 24h DEX volume | 2,495,170,004.38 | 2,118,350,659.32 | -15.10% |
| 24h chain fees | 11,775,288.16 | 10,654,111.63 | -9.52% |

### Change over 7d (vs run at 2026-10-08T22:33:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,632.43 | 5,323.17 | +14.91% |
| Average non-vote TPS | 2,125.38 | 2,236.62 | +5.23% |
| Average slot time (ms) | 267.50 | 216.50 | -19.07% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 6,248,086,909.00 | 6,044,693,032.00 | -3.26% |
| SOL price | 110.19 | 105.91 | -3.88% |
| Stablecoin supply | 16,607,983,518.00 | 16,055,865,871.00 | -3.32% |
| 24h DEX volume | 2,205,685,057.81 | 2,118,350,659.32 | -3.96% |
| 24h chain fees | 13,737,332.90 | 10,654,111.63 | -22.44% |

### Change over 30d (vs run at 2026-09-15T20:32:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,770.98 | 5,323.17 | +11.57% |
| Average non-vote TPS | 2,641.86 | 2,236.62 | -15.34% |
| Average slot time (ms) | 317.40 | 216.50 | -31.79% |
| Active validators | 679.00 | 672.00 | -1.03% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 5,793,334,701.00 | 6,044,693,032.00 | +4.34% |
| SOL price | 96.94 | 105.91 | +9.25% |
| Stablecoin supply | 16,388,645,734.00 | 16,055,865,871.00 | -2.03% |
| 24h DEX volume | 2,530,223,236.85 | 2,118,350,659.32 | -16.28% |
| 24h chain fees | 13,579,950.58 | 10,654,111.63 | -21.55% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
