# Solana Ecosystem Pulse

**Generated:** 2026-10-16T10:14:37Z · **Schema:** `1.0.0` · **Collection time:** 13.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.70 | +3.39% |
| Market cap | $62.31B | rank #7 |
| Total value locked | $6.03B | +1.00% |
| Stablecoin supply | $16.23B | +1.11% |
| DEX volume (24h) | $2.42B | +14.26% |
| Chain fees / REV (24h) | $12.67M | +18.63% |
| Non-vote TPS (1h avg) | 1,478 | peak 4,878 total |
| Active validators | 671 | 9 delinquent |
| Epoch 1059 | 25.99% complete | 319,720 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 107 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,477.6 average over the last 60 minutes; 1,240.4 in the latest sample.
- **Total TPS:** 4,584.5 average, 4,878.1 peak. Consensus votes account for 67.8% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 435,636,098 at absolute slot 457,600,280.
- **Epoch 1059:** slot 112,280 of 432,000 (25.99% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.600% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 143 ms |
| `solana-rpc.publicnode.com` | yes | 93 ms |
| `api.mainnet.solana.com` | yes | 117 ms |

## Validators & stake

- **671 active** validators, **9 delinquent** (1.32% by count, 0.000% by stake).
- **Total stake:** 437,782,540 SOL ($46.27B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.68%; 230 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,561,701 | 4.012% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,460,528 | 3.532% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,362,555 | 2.824% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,093,074 | 2.534% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,200,312 | 2.330% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,428,271 | 2.154% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,248,874 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,743,557 | 1.769% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,910,886 | 1.579% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,417,148 | 1.466% | 0% |

## Economics

- **SOL:** $105.70 (+3.39% 24h, -4.21% 7d, +8.71% 30d). Market cap $62.31B, 24h volume $3.23B (5.19% of cap). Price source: `coingecko`.
- **TVL:** $6.03B across 325 protocols - rank #3 of 425 chains, 6.67% of all tracked chain TVL. -2.93% over 7d, -54.7% from its ATH.
- **Stablecoins:** $16.23B circulating on Solana (+0.21% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.42B in 24h, $12.48B over 7d across 136 venues. Volume/TVL turnover 0.402x per day.
- **REV (chain fees):** $12.67M in 24h, $461.88M over 30d. Retained chain revenue $5.13M (40.5% of fees). Annualised fees are 7.42% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,324,376 SOL circulating of 635,906,103 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +4.2% | +0.3% |
| 2 | Kamino Lend | Lending | $1.32B | +1.0% | +1.0% |
| 3 | Raydium AMM | Dexs | $1.19B | +2.4% | -3.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.11B | +3.4% | -2.4% |
| 5 | Jupiter Lend | Lending | $1.10B | -0.9% | -6.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.10B | +3.7% | -2.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $752.18M | +2.9% | -1.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $557.25M | +3.8% | -1.8% |
| 9 | Sentora Curator | Risk Curators | $457.60M | +0.0% | -8.8% |
| 10 | Marinade Native | Staking Pool | $389.73M | +3.5% | -4.6% |
| 11 | PumpSwap | Dexs | $356.87M | +4.1% | -3.9% |
| 12 | Orca DEX | Dexs | $302.54M | +2.3% | -2.3% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 325 protocols the total is $16.09B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 16.8% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.9%

### Tokenised assets

$897.54M of tokenised real-world assets and equities are locked on Solana - 5.579% of chain TVL.

- OnRe (RWA): $292.44M
- Huma (RWA): $287.10M
- Solstice (Basis Trading): $209.36M
- JupUSD (Basis Trading): $44.15M
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

### Change over 24h (vs run at 2026-10-15T10:27:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,660.95 | 4,584.52 | -1.64% |
| Average non-vote TPS | 1,557.56 | 1,477.61 | -5.13% |
| Average slot time (ms) | 215.60 | 215.10 | -0.23% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 5,931,649,344.00 | 6,025,134,675.00 | +1.58% |
| SOL price | 101.81 | 105.70 | +3.82% |
| Stablecoin supply | 16,055,751,684.00 | 16,234,677,076.00 | +1.11% |
| 24h DEX volume | 2,250,924,739.32 | 2,421,172,051.03 | +7.56% |
| 24h chain fees | 10,628,281.63 | 12,667,804.48 | +19.19% |

### Change over 7d (vs run at 2026-10-09T12:11:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,156.32 | 4,584.52 | +10.30% |
| Average non-vote TPS | 1,656.99 | 1,477.61 | -10.83% |
| Average slot time (ms) | 268.30 | 215.10 | -19.83% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 6,231,947,843.00 | 6,025,134,675.00 | -3.32% |
| SOL price | 111.20 | 105.70 | -4.95% |
| Stablecoin supply | 16,377,840,192.00 | 16,234,677,076.00 | -0.87% |
| 24h DEX volume | 2,644,852,886.24 | 2,421,172,051.03 | -8.46% |
| 24h chain fees | 14,970,162.23 | 12,667,804.48 | -15.38% |

### Change over 30d (vs run at 2026-09-16T20:32:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,850.92 | 4,584.52 | -5.49% |
| Average non-vote TPS | 2,744.58 | 1,477.61 | -46.16% |
| Average slot time (ms) | 318.60 | 215.10 | -32.49% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 14.00 | 9.00 | -35.71% |
| Solana TVL | 5,723,932,041.00 | 6,025,134,675.00 | +5.26% |
| SOL price | 98.40 | 105.70 | +7.42% |
| Stablecoin supply | 15,963,602,798.00 | 16,234,677,076.00 | +1.70% |
| 24h DEX volume | 2,703,297,666.22 | 2,421,172,051.03 | -10.44% |
| 24h chain fees | 14,083,156.46 | 12,667,804.48 | -10.05% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
