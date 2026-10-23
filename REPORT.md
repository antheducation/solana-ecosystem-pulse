# Solana Ecosystem Pulse

**Generated:** 2026-10-23T02:15:01Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.05 | -1.85% |
| Market cap | $61.37B | rank #7 |
| Total value locked | $5.87B | -1.51% |
| Stablecoin supply | $15.97B | -1.15% |
| DEX volume (24h) | $2.12B | -6.75% |
| Chain fees / REV (24h) | $11.21M | -5.18% |
| Non-vote TPS (1h avg) | 1,828 | peak 2,481 total |
| Active validators | 656 | 20 delinquent |
| Epoch 1065 | 43.78% complete | 242,855 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 118 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,827.63 sits 5.8 sigma below the median of the last 118 runs (4,659.08, -60.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 656.00 sits 4.0 sigma below the median of the last 118 runs (674.00, -2.7%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 20.00 sits 3.4 sigma above the median of the last 118 runs (10.00, +100.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,827.6 average over the last 60 minutes; 1,949.0 in the latest sample.
- **Total TPS:** 1,827.6 average, 2,481.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.6 ms average (target 400 ms), worst 1-minute bucket 216.6 ms.
- **Block height:** 438,301,464 at absolute slot 460,269,145.
- **Epoch 1065:** slot 189,145 of 432,000 (43.78% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.590% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 157 ms |
| `solana-rpc.publicnode.com` | yes | 171 ms |
| `api.mainnet.solana.com` | yes | 108 ms |

## Validators & stake

- **656 active** validators, **20 delinquent** (2.96% by count, 0.295% by stake).
- **Total stake:** 438,318,925 SOL ($45.61B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.99% of active stake.
- **Commission:** median 5.0%, mean 12.92%; 221 validators at 0% and 62 at 100%.

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

- **SOL:** $104.05 (-1.85% 24h, -0.94% 7d, -12.01% 30d). Market cap $61.37B, 24h volume $2.44B (3.98% of cap). Price source: `coingecko`.
- **TVL:** $5.87B across 332 protocols - rank #3 of 421 chains, 6.50% of all tracked chain TVL. -2.28% over 7d, -54.7% from its ATH.
- **Stablecoins:** $15.97B circulating on Solana (-1.65% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.12B in 24h, $12.63B over 7d across 138 venues. Volume/TVL turnover 0.361x per day.
- **REV (chain fees):** $11.21M in 24h, $431.06M over 30d. Retained chain revenue $4.09M (36.5% of fees). Annualised fees are 6.67% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,653,414 SOL circulating of 636,273,824 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | -3.6% | +1.2% |
| 2 | Kamino Lend | Lending | $1.30B | -2.9% | -1.6% |
| 3 | Raydium AMM | Dexs | $1.17B | -3.4% | -1.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.09B | -3.1% | +0.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.08B | -3.1% | -2.0% |
| 6 | Jupiter Lend | Lending | $1.03B | -2.1% | -7.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $729.72M | -2.3% | -2.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $541.96M | -3.6% | -1.6% |
| 9 | Sentora Curator | Risk Curators | $418.32M | +0.3% | -8.6% |
| 10 | Marinade Native | Staking Pool | $371.61M | -3.6% | -3.6% |
| 11 | PumpSwap | Dexs | $347.55M | -3.0% | -1.4% |
| 12 | Orca DEX | Dexs | $306.22M | -1.2% | +1.4% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.75B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 3.9% · RWA 3.8%

### Tokenised assets

$858.23M of tokenised real-world assets and equities are locked on Solana - 5.450% of chain TVL.

- OnRe (RWA): $295.16M
- Huma (RWA): $252.09M
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

- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-23
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-22
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-22
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-22
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-22
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-22
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22

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

### Change over 24h (vs run at 2026-10-22T02:09:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,987.14 | 1,827.63 | -8.03% |
| Average non-vote TPS | 1,987.14 | 1,827.62 | -8.03% |
| Average slot time (ms) | 212.40 | 211.60 | -0.38% |
| Active validators | 668.00 | 656.00 | -1.80% |
| Delinquent validators | 9.00 | 20.00 | +122.22% |
| Solana TVL | 6,031,824,201.00 | 5,871,527,154.00 | -2.66% |
| SOL price | 105.97 | 104.05 | -1.81% |
| Stablecoin supply | 16,153,982,880.00 | 15,965,967,694.00 | -1.16% |
| 24h DEX volume | 2,278,261,933.37 | 2,117,243,398.23 | -7.07% |
| 24h chain fees | 11,875,251.66 | 11,209,587.27 | -5.61% |

### Change over 7d (vs run at 2026-10-16T01:55:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,933.00 | 1,827.63 | -69.20% |
| Average non-vote TPS | 2,860.96 | 1,827.62 | -36.12% |
| Average slot time (ms) | 217.70 | 211.60 | -2.80% |
| Active validators | 672.00 | 656.00 | -2.38% |
| Delinquent validators | 9.00 | 20.00 | +122.22% |
| Solana TVL | 6,022,784,745.00 | 5,871,527,154.00 | -2.51% |
| SOL price | 105.09 | 104.05 | -0.99% |
| Stablecoin supply | 16,231,219,596.00 | 15,965,967,694.00 | -1.63% |
| 24h DEX volume | 2,423,566,552.03 | 2,117,243,398.23 | -12.64% |
| 24h chain fees | 12,686,735.80 | 11,209,587.27 | -11.64% |

### Change over 30d (vs run at 2026-09-22T20:34:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,893.52 | 1,827.63 | -62.65% |
| Average non-vote TPS | 2,379.33 | 1,827.62 | -23.19% |
| Average slot time (ms) | 268.00 | 211.60 | -21.04% |
| Active validators | 677.00 | 656.00 | -3.10% |
| Delinquent validators | 12.00 | 20.00 | +66.67% |
| Solana TVL | 6,505,534,933.00 | 5,871,527,154.00 | -9.75% |
| SOL price | 118.17 | 104.05 | -11.95% |
| Stablecoin supply | 17,173,484,924.00 | 15,965,967,694.00 | -7.03% |
| 24h DEX volume | 3,428,858,820.75 | 2,117,243,398.23 | -38.25% |
| 24h chain fees | 18,642,402.21 | 11,209,587.27 | -39.87% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
