# Solana Ecosystem Pulse

**Generated:** 2026-10-23T16:00:22Z · **Schema:** `1.0.0` · **Collection time:** 18.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.63 | +0.10% |
| Market cap | $61.69B | rank #7 |
| Total value locked | $5.86B | -2.36% |
| Stablecoin supply | $15.96B | -1.15% |
| DEX volume (24h) | $2.04B | -10.18% |
| Chain fees / REV (24h) | $11.29M | -5.61% |
| Non-vote TPS (1h avg) | 2,334 | peak 2,983 total |
| Active validators | 656 | 20 delinquent |
| Epoch 1065 | 97.93% complete | 8,925 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 119 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,333.57 sits 4.7 sigma below the median of the last 119 runs (4,659.01, -49.9%). | `zscore` |
| [WARNING] | Active validators is below its recent norm | Current 656.00 sits 4.0 sigma below the median of the last 119 runs (674.00, -2.7%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 20.00 sits 3.4 sigma above the median of the last 119 runs (10.00, +100.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,333.6 average over the last 60 minutes; 2,097.9 in the latest sample.
- **Total TPS:** 2,333.6 average, 2,983.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.9 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 438,535,266 at absolute slot 460,503,075.
- **Epoch 1065:** slot 423,075 of 432,000 (97.93% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.590% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 171 ms |
| `solana-rpc.publicnode.com` | yes | 147 ms |
| `api.mainnet.solana.com` | yes | 200 ms |

## Validators & stake

- **656 active** validators, **20 delinquent** (2.96% by count, 0.295% by stake).
- **Total stake:** 438,318,925 SOL ($45.86B); stake rate 68.89% of total supply.
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

- **SOL:** $104.63 (+0.10% 24h, -0.90% 7d, -9.07% 30d). Market cap $61.69B, 24h volume $2.17B (3.51% of cap). Price source: `coingecko`.
- **TVL:** $5.86B across 332 protocols - rank #3 of 421 chains, 6.48% of all tracked chain TVL. -2.41% over 7d, -54.8% from its ATH.
- **Stablecoins:** $15.96B circulating on Solana (-1.65% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.04B in 24h, $13.69B over 7d across 138 venues. Volume/TVL turnover 0.348x per day.
- **REV (chain fees):** $11.29M in 24h, $431.73M over 30d. Retained chain revenue $4.07M (36.0% of fees). Annualised fees are 6.68% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,653,165 SOL circulating of 636,273,575 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.84B | +0.1% | +2.6% |
| 2 | Kamino Lend | Lending | $1.29B | -2.8% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.18B | -0.1% | -0.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | +0.1% | +1.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.09B | +0.2% | -1.1% |
| 6 | Jupiter Lend | Lending | $1.01B | -2.4% | -8.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $730.70M | +0.1% | -2.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $549.10M | -0.1% | -0.3% |
| 9 | Sentora Curator | Risk Curators | $408.30M | -2.2% | -10.8% |
| 10 | Marinade Native | Staking Pool | $376.68M | +0.0% | -2.3% |
| 11 | PumpSwap | Dexs | $349.95M | -0.6% | -0.7% |
| 12 | Orca DEX | Dexs | $305.93M | -0.1% | +1.3% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.82B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.3% · Dexs 15.3% · Derivatives 5.0% · Risk Curators 3.8% · RWA 3.8%

### Tokenised assets

$858.47M of tokenised real-world assets and equities are locked on Solana - 5.428% of chain TVL.

- OnRe (RWA): $295.18M
- Huma (RWA): $252.03M
- Solstice (Basis Trading): $201.75M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.43M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-23
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-22T16:10:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,291.15 | 2,333.57 | +1.85% |
| Average non-vote TPS | 2,291.14 | 2,333.57 | +1.85% |
| Average slot time (ms) | 211.10 | 211.90 | +0.38% |
| Active validators | 656.00 | 656.00 | +0.00% |
| Delinquent validators | 20.00 | 20.00 | +0.00% |
| Solana TVL | 5,931,668,789.00 | 5,864,633,004.00 | -1.13% |
| SOL price | 104.58 | 104.63 | +0.05% |
| Stablecoin supply | 16,154,815,750.00 | 15,964,212,870.00 | -1.18% |
| 24h DEX volume | 2,270,402,206.37 | 2,039,384,832.23 | -10.18% |
| 24h chain fees | 11,887,074.66 | 11,291,169.22 | -5.01% |

### Change over 7d (vs run at 2026-10-16T15:39:44Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,269.25 | 2,333.57 | -55.71% |
| Average non-vote TPS | 2,179.57 | 2,333.57 | +7.07% |
| Average slot time (ms) | 216.60 | 211.90 | -2.17% |
| Active validators | 672.00 | 656.00 | -2.38% |
| Delinquent validators | 9.00 | 20.00 | +122.22% |
| Solana TVL | 6,025,302,280.00 | 5,864,633,004.00 | -2.67% |
| SOL price | 104.63 | 104.63 | +0.00% |
| Stablecoin supply | 16,234,288,263.00 | 15,964,212,870.00 | -1.66% |
| 24h DEX volume | 2,539,283,878.03 | 2,039,384,832.23 | -19.69% |
| 24h chain fees | 12,783,602.89 | 11,291,169.22 | -11.67% |

### Change over 30d (vs run at 2026-09-23T20:45:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,741.96 | 2,333.57 | -50.79% |
| Average non-vote TPS | 2,211.74 | 2,333.57 | +5.51% |
| Average slot time (ms) | 265.30 | 211.90 | -20.13% |
| Active validators | 674.00 | 656.00 | -2.67% |
| Delinquent validators | 13.00 | 20.00 | +53.85% |
| Solana TVL | 6,385,088,886.00 | 5,864,633,004.00 | -8.15% |
| SOL price | 114.36 | 104.63 | -8.51% |
| Stablecoin supply | 16,880,373,729.00 | 15,964,212,870.00 | -5.43% |
| 24h DEX volume | 3,195,015,036.76 | 2,039,384,832.23 | -36.17% |
| 24h chain fees | 17,874,880.76 | 11,291,169.22 | -36.83% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
