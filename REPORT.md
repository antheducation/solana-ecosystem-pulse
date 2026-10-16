# Solana Ecosystem Pulse

**Generated:** 2026-10-16T01:55:25Z · **Schema:** `1.0.0` · **Collection time:** 13.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.09 | +0.81% |
| Market cap | $61.93B | rank #7 |
| Total value locked | $6.02B | -0.39% |
| Stablecoin supply | $16.23B | +1.09% |
| DEX volume (24h) | $2.42B | +14.38% |
| Chain fees / REV (24h) | $12.69M | +18.81% |
| Non-vote TPS (1h avg) | 2,861 | peak 6,940 total |
| Active validators | 672 | 9 delinquent |
| Epoch 1058 | 93.85% complete | 26,562 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 107 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,861.0 average over the last 60 minutes; 2,820.7 in the latest sample.
- **Total TPS:** 5,933.0 average, 6,940.2 peak. Consensus votes account for 51.8% of all transactions.
- **Slot time:** 217.7 ms average (target 400 ms), worst 1-minute bucket 226.4 ms.
- **Block height:** 435,497,272 at absolute slot 457,461,438.
- **Epoch 1058:** slot 405,438 of 432,000 (93.85% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.602% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 218 ms |
| `solana-rpc.publicnode.com` | yes | 106 ms |
| `api.mainnet.solana.com` | yes | 150 ms |

## Validators & stake

- **672 active** validators, **9 delinquent** (1.32% by count, 0.000% by stake).
- **Total stake:** 437,887,641 SOL ($46.02B); stake rate 68.87% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 12.96%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,556,681 | 4.009% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,475,284 | 3.534% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,340,406 | 2.818% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,132,168 | 2.542% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,777,829 | 2.461% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,409,309 | 2.149% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,227,345 | 2.107% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,737,484 | 1.767% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,912,081 | 1.579% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,640,641 | 1.517% | 0% |

## Economics

- **SOL:** $105.09 (+0.81% 24h, -3.81% 7d, +8.31% 30d). Market cap $61.93B, 24h volume $4.16B (6.72% of cap). Price source: `coingecko`.
- **TVL:** $6.02B across 325 protocols - rank #3 of 425 chains, 6.67% of all tracked chain TVL. -6.64% over 7d, -54.7% from its ATH.
- **Stablecoins:** $16.23B circulating on Solana (+0.19% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.42B in 24h, $12.48B over 7d across 136 venues. Volume/TVL turnover 0.402x per day.
- **REV (chain fees):** $12.69M in 24h, $461.48M over 30d. Retained chain revenue $5.14M (40.5% of fees). Annualised fees are 7.48% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,267,953 SOL circulating of 635,843,796 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +1.8% | -0.7% |
| 2 | Kamino Lend | Lending | $1.32B | +0.3% | +0.9% |
| 3 | Raydium AMM | Dexs | $1.19B | +1.0% | -3.2% |
| 4 | Jupiter Lend | Lending | $1.11B | +0.4% | -5.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.10B | +1.1% | -3.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.09B | +1.3% | -3.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $746.96M | +1.3% | -2.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $550.88M | +1.3% | -2.9% |
| 9 | Sentora Curator | Risk Curators | $457.64M | -0.0% | -8.8% |
| 10 | Marinade Native | Staking Pool | $385.47M | +1.0% | -5.7% |
| 11 | PumpSwap | Dexs | $352.80M | +1.7% | -5.0% |
| 12 | Orca DEX | Dexs | $302.10M | +0.7% | -2.4% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 325 protocols the total is $16.00B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 16.9% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.8%

### Tokenised assets

$875.34M of tokenised real-world assets and equities are locked on Solana - 5.472% of chain TVL.

- OnRe (RWA): $292.39M
- Huma (RWA): $264.55M
- Solstice (Basis Trading): $209.31M
- JupUSD (Basis Trading): $44.64M
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
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | pre-release |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

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

### Change over 24h (vs run at 2026-10-15T02:04:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,158.40 | 5,933.00 | +15.02% |
| Average non-vote TPS | 2,079.66 | 2,860.96 | +37.57% |
| Average slot time (ms) | 216.60 | 217.70 | +0.51% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 5,995,764,710.00 | 6,022,784,745.00 | +0.45% |
| SOL price | 103.85 | 105.09 | +1.19% |
| Stablecoin supply | 16,056,807,804.00 | 16,231,219,596.00 | +1.09% |
| 24h DEX volume | 2,248,882,317.32 | 2,423,566,552.03 | +7.77% |
| 24h chain fees | 10,646,585.63 | 12,686,735.80 | +19.16% |

### Change over 7d (vs run at 2026-10-09T03:21:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,330.45 | 5,933.00 | +37.01% |
| Average non-vote TPS | 1,832.51 | 2,860.96 | +56.12% |
| Average slot time (ms) | 268.40 | 217.70 | -18.89% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 6,221,527,063.00 | 6,022,784,745.00 | -3.19% |
| SOL price | 110.02 | 105.09 | -4.48% |
| Stablecoin supply | 16,377,545,621.00 | 16,231,219,596.00 | -0.89% |
| 24h DEX volume | 2,440,532,233.24 | 2,423,566,552.03 | -0.70% |
| 24h chain fees | 13,520,931.81 | 12,686,735.80 | -6.17% |

### Change over 30d (vs run at 2026-09-15T20:32:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,770.98 | 5,933.00 | +24.36% |
| Average non-vote TPS | 2,641.86 | 2,860.96 | +8.29% |
| Average slot time (ms) | 317.40 | 217.70 | -31.41% |
| Active validators | 679.00 | 672.00 | -1.03% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 5,793,334,701.00 | 6,022,784,745.00 | +3.96% |
| SOL price | 96.94 | 105.09 | +8.41% |
| Stablecoin supply | 16,388,645,734.00 | 16,231,219,596.00 | -0.96% |
| 24h DEX volume | 2,530,223,236.85 | 2,423,566,552.03 | -4.22% |
| 24h chain fees | 13,579,950.58 | 12,686,735.80 | -6.58% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
