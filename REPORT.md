# Solana Ecosystem Pulse

**Generated:** 2026-10-19T02:05:01Z · **Schema:** `1.0.0` · **Collection time:** 16.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.90 | +1.32% |
| Market cap | $61.85B | rank #7 |
| Total value locked | $5.82B | +0.07% |
| Stablecoin supply | $15.84B | -0.37% |
| DEX volume (24h) | $1.57B | +25.03% |
| Chain fees / REV (24h) | $9.71M | +3.62% |
| Non-vote TPS (1h avg) | 1,819 | peak 5,594 total |
| Active validators | 666 | 14 delinquent |
| Epoch 1061 | 71.43% complete | 123,441 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 110 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,819.0 average over the last 60 minutes; 1,541.0 in the latest sample.
- **Total TPS:** 4,870.4 average, 5,593.6 peak. Consensus votes account for 62.7% of all transactions.
- **Slot time:** 217.5 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 436,695,797 at absolute slot 458,660,559.
- **Epoch 1061:** slot 308,559 of 432,000 (71.43% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.597% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 201 ms |
| `solana-rpc.publicnode.com` | yes | 214 ms |
| `api.mainnet.solana.com` | yes | 225 ms |

## Validators & stake

- **666 active** validators, **14 delinquent** (2.06% by count, 0.029% by stake).
- **Total stake:** 437,350,803 SOL ($45.88B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.98% of active stake.
- **Commission:** median 5.0%, mean 13.18%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,091,304 | 3.909% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,762,758 | 3.605% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,730 | 2.864% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,974,352 | 2.510% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,484 | 2.223% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,253 | 2.165% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,164 | 2.116% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,774,268 | 1.778% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,992,811 | 1.599% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,730,670 | 1.539% | 0% |

## Economics

- **SOL:** $104.90 (+1.32% 24h, -5.87% 7d, -7.48% 30d). Market cap $61.85B, 24h volume $2.35B (3.81% of cap). Price source: `coingecko`.
- **TVL:** $5.82B across 325 protocols - rank #3 of 420 chains, 6.57% of all tracked chain TVL. -6.83% over 7d, -55.5% from its ATH.
- **Stablecoins:** $15.84B circulating on Solana (-2.10% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.57B in 24h, $14.03B over 7d across 136 venues. Volume/TVL turnover 0.269x per day.
- **REV (chain fees):** $9.71M in 24h, $447.26M over 30d. Retained chain revenue $3.66M (37.7% of fees). Annualised fees are 5.73% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,437,721 SOL circulating of 636,028,486 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | +0.1% | -1.7% |
| 2 | Kamino Lend | Lending | $1.31B | +0.3% | -2.1% |
| 3 | Raydium AMM | Dexs | $1.14B | -2.2% | -9.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.10B | +0.8% | -6.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | +1.1% | -4.7% |
| 6 | Jupiter Lend | Lending | $1.02B | -6.0% | -10.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $738.36M | +0.3% | -5.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $545.52M | +0.7% | -5.1% |
| 9 | Sentora Curator | Risk Curators | $450.88M | -0.1% | -8.3% |
| 10 | Marinade Native | Staking Pool | $378.56M | +0.3% | -8.2% |
| 11 | PumpSwap | Dexs | $339.08M | -1.4% | -8.4% |
| 12 | Orca DEX | Dexs | $297.04M | -0.0% | -4.7% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 325 protocols the total is $15.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.5% · Dexs 14.9% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.9%

### Tokenised assets

$893.37M of tokenised real-world assets and equities are locked on Solana - 5.667% of chain TVL.

- OnRe (RWA): $293.84M
- Huma (RWA): $280.49M
- Solstice (Basis Trading): $209.29M
- JupUSD (Basis Trading): $43.90M
- Plume Vaults (RWA): $36.12M

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

- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-17
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-17
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-16
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-16
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-15
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-15
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-15

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

### Change over 24h (vs run at 2026-10-18T01:48:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,812.84 | 4,870.39 | +1.20% |
| Average non-vote TPS | 1,736.06 | 1,819.00 | +4.78% |
| Average slot time (ms) | 216.70 | 217.50 | +0.37% |
| Active validators | 669.00 | 666.00 | -0.45% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 5,882,315,364.00 | 5,822,373,107.00 | -1.02% |
| SOL price | 104.05 | 104.90 | +0.82% |
| Stablecoin supply | 15,897,345,176.00 | 15,839,425,505.00 | -0.36% |
| 24h DEX volume | 1,514,642,363.55 | 1,565,959,221.38 | +3.39% |
| 24h chain fees | 9,315,995.67 | 9,714,592.98 | +4.28% |

### Change over 7d (vs run at 2026-10-12T02:55:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,135.89 | 4,870.39 | -5.17% |
| Average non-vote TPS | 2,087.65 | 1,819.00 | -12.87% |
| Average slot time (ms) | 219.70 | 217.50 | -1.00% |
| Active validators | 673.00 | 666.00 | -1.04% |
| Delinquent validators | 8.00 | 14.00 | +75.00% |
| Solana TVL | 6,254,990,671.00 | 5,822,373,107.00 | -6.92% |
| SOL price | 112.07 | 104.90 | -6.40% |
| Stablecoin supply | 16,359,537,345.00 | 15,839,425,505.00 | -3.18% |
| 24h DEX volume | 1,246,835,645.31 | 1,565,959,221.38 | +25.59% |
| 24h chain fees | 11,260,863.80 | 9,714,592.98 | -13.73% |

### Change over 30d (vs run at 2026-09-18T20:04:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,950.64 | 4,870.39 | -1.62% |
| Average non-vote TPS | 2,440.09 | 1,819.00 | -25.45% |
| Average slot time (ms) | 267.70 | 217.50 | -18.75% |
| Active validators | 676.00 | 666.00 | -1.48% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 6,242,343,437.00 | 5,822,373,107.00 | -6.73% |
| SOL price | 113.98 | 104.90 | -7.97% |
| Stablecoin supply | 15,713,039,562.00 | 15,839,425,505.00 | +0.80% |
| 24h DEX volume | 2,592,123,183.29 | 1,565,959,221.38 | -39.59% |
| 24h chain fees | 14,675,830.10 | 9,714,592.98 | -33.81% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
