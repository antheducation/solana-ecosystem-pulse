# Solana Ecosystem Pulse

**Generated:** 2026-10-23T10:36:26Z · **Schema:** `1.0.0` · **Collection time:** 15.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.11 | -0.49% |
| Market cap | $61.39B | rank #7 |
| Total value locked | $5.87B | -2.31% |
| Stablecoin supply | $15.97B | -1.15% |
| DEX volume (24h) | $2.07B | -8.62% |
| Chain fees / REV (24h) | $11.33M | -5.19% |
| Non-vote TPS (1h avg) | 1,793 | peak 2,401 total |
| Active validators | 656 | 20 delinquent |
| Epoch 1065 | 76.68% complete | 100,743 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 118 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,792.56 sits 5.9 sigma below the median of the last 118 runs (4,659.08, -61.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 656.00 sits 4.0 sigma below the median of the last 118 runs (674.00, -2.7%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 20.00 sits 3.4 sigma above the median of the last 118 runs (10.00, +100.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,792.6 average over the last 60 minutes; 1,832.5 in the latest sample.
- **Total TPS:** 1,792.6 average, 2,401.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.5 ms average (target 400 ms), worst 1-minute bucket 218.2 ms.
- **Block height:** 438,443,548 at absolute slot 460,411,257.
- **Epoch 1065:** slot 331,257 of 432,000 (76.68% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.590% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 151 ms |
| `solana-rpc.publicnode.com` | yes | 107 ms |
| `api.mainnet.solana.com` | yes | 270 ms |

## Validators & stake

- **656 active** validators, **20 delinquent** (2.96% by count, 0.295% by stake).
- **Total stake:** 438,318,925 SOL ($45.63B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.99% of active stake.
- **Commission:** median 5.0%, mean 13.21%; 221 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,133,144 | 3.920% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,621 | 3.654% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,556,096 | 2.873% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,936,237 | 2.502% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,726,420 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,476,174 | 2.168% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,244,629 | 2.115% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,797,559 | 1.784% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,036,293 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,002,101 | 1.602% | 0% |

## Economics

- **SOL:** $104.11 (-0.49% 24h, -1.97% 7d, -11.30% 30d). Market cap $61.39B, 24h volume $2.05B (3.33% of cap). Price source: `coingecko`.
- **TVL:** $5.87B across 332 protocols - rank #3 of 421 chains, 6.49% of all tracked chain TVL. -2.35% over 7d, -54.8% from its ATH.
- **Stablecoins:** $15.97B circulating on Solana (-1.65% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.07B in 24h, $13.17B over 7d across 138 venues. Volume/TVL turnover 0.354x per day.
- **REV (chain fees):** $11.33M in 24h, $431.33M over 30d. Retained chain revenue $4.10M (36.2% of fees). Annualised fees are 6.74% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,653,271 SOL circulating of 636,273,682 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.83B | +0.7% | +2.3% |
| 2 | Kamino Lend | Lending | $1.29B | -2.5% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.18B | +0.9% | -0.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | +0.8% | +1.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.09B | +0.4% | -1.8% |
| 6 | Jupiter Lend | Lending | $1.02B | -1.4% | -8.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $731.98M | +0.7% | -2.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $547.54M | +0.7% | -0.6% |
| 9 | Sentora Curator | Risk Curators | $408.26M | -2.2% | -10.8% |
| 10 | Marinade Native | Staking Pool | $374.25M | +0.4% | -2.9% |
| 11 | PumpSwap | Dexs | $347.34M | -0.5% | -1.4% |
| 12 | Orca DEX | Dexs | $307.55M | +0.4% | +1.8% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.80B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.4% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 3.8% · RWA 3.8%

### Tokenised assets

$858.45M of tokenised real-world assets and equities are locked on Solana - 5.435% of chain TVL.

- OnRe (RWA): $295.17M
- Huma (RWA): $252.27M
- Solstice (Basis Trading): $201.73M
- JupUSD (Basis Trading): $42.95M
- Plume Vaults (RWA): $36.23M

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
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-23
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-23
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-22
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-22T10:44:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,731.38 | 1,792.56 | +3.53% |
| Average non-vote TPS | 1,731.38 | 1,792.56 | +3.53% |
| Average slot time (ms) | 211.10 | 211.50 | +0.19% |
| Active validators | 668.00 | 656.00 | -1.80% |
| Delinquent validators | 9.00 | 20.00 | +122.22% |
| Solana TVL | 5,896,494,807.00 | 5,868,506,816.00 | -0.47% |
| SOL price | 104.58 | 104.11 | -0.45% |
| Stablecoin supply | 16,155,037,927.00 | 15,966,112,276.00 | -1.17% |
| 24h DEX volume | 2,257,983,009.37 | 2,074,632,771.23 | -8.12% |
| 24h chain fees | 11,864,192.66 | 11,333,373.27 | -4.47% |

### Change over 7d (vs run at 2026-10-16T10:14:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,584.52 | 1,792.56 | -60.90% |
| Average non-vote TPS | 1,477.61 | 1,792.56 | +21.31% |
| Average slot time (ms) | 215.10 | 211.50 | -1.67% |
| Active validators | 671.00 | 656.00 | -2.24% |
| Delinquent validators | 9.00 | 20.00 | +122.22% |
| Solana TVL | 6,025,134,675.00 | 5,868,506,816.00 | -2.60% |
| SOL price | 105.70 | 104.11 | -1.50% |
| Stablecoin supply | 16,234,677,076.00 | 15,966,112,276.00 | -1.65% |
| 24h DEX volume | 2,421,172,051.03 | 2,074,632,771.23 | -14.31% |
| 24h chain fees | 12,667,804.48 | 11,333,373.27 | -10.53% |

### Change over 30d (vs run at 2026-09-23T20:45:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,741.96 | 1,792.56 | -62.20% |
| Average non-vote TPS | 2,211.74 | 1,792.56 | -18.95% |
| Average slot time (ms) | 265.30 | 211.50 | -20.28% |
| Active validators | 674.00 | 656.00 | -2.67% |
| Delinquent validators | 13.00 | 20.00 | +53.85% |
| Solana TVL | 6,385,088,886.00 | 5,868,506,816.00 | -8.09% |
| SOL price | 114.36 | 104.11 | -8.96% |
| Stablecoin supply | 16,880,373,729.00 | 15,966,112,276.00 | -5.42% |
| 24h DEX volume | 3,195,015,036.76 | 2,074,632,771.23 | -35.07% |
| 24h chain fees | 17,874,880.76 | 11,333,373.27 | -36.60% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
