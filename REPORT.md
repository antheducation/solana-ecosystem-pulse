# Solana Ecosystem Pulse

**Generated:** 2026-10-16T20:09:55Z · **Schema:** `1.0.0` · **Collection time:** 16.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.59 | -2.19% |
| Market cap | $61.03B | rank #7 |
| Total value locked | $5.95B | -0.29% |
| Stablecoin supply | $16.23B | +1.11% |
| DEX volume (24h) | $2.54B | +19.84% |
| Chain fees / REV (24h) | $12.78M | +19.71% |
| Non-vote TPS (1h avg) | 2,482 | peak 6,113 total |
| Active validators | 671 | 9 delinquent |
| Epoch 1059 | 64.22% complete | 154,580 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 108 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,482.3 average over the last 60 minutes; 2,064.5 in the latest sample.
- **Total TPS:** 5,572.5 average, 6,112.9 peak. Consensus votes account for 55.5% of all transactions.
- **Slot time:** 216.2 ms average (target 400 ms), worst 1-minute bucket 224.7 ms.
- **Block height:** 435,801,205 at absolute slot 457,765,420.
- **Epoch 1059:** slot 277,420 of 432,000 (64.22% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.600% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 241 ms |
| `solana-rpc.publicnode.com` | yes | 174 ms |
| `api.mainnet.solana.com` | yes | 191 ms |

## Validators & stake

- **671 active** validators, **9 delinquent** (1.32% by count, 0.000% by stake).
- **Total stake:** 437,782,540 SOL ($45.35B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.98%; 228 validators at 0% and 64 at 100%.

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

- **SOL:** $103.59 (-2.19% 24h, -4.58% 7d, +5.66% 30d). Market cap $61.03B, 24h volume $2.92B (4.79% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 325 protocols - rank #3 of 425 chains, 6.66% of all tracked chain TVL. -4.16% over 7d, -55.2% from its ATH.
- **Stablecoins:** $16.23B circulating on Solana (+0.20% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.54B in 24h, $13.68B over 7d across 136 venues. Volume/TVL turnover 0.427x per day.
- **REV (chain fees):** $12.78M in 24h, $462.25M over 30d. Retained chain revenue $5.14M (40.2% of fees). Annualised fees are 7.65% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,323,889 SOL circulating of 635,905,617 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.76B | -1.3% | -2.2% |
| 2 | Kamino Lend | Lending | $1.32B | -0.7% | +0.4% |
| 3 | Raydium AMM | Dexs | $1.18B | -0.9% | -4.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.09B | -1.8% | -4.6% |
| 5 | Jupiter Lend | Lending | $1.08B | -3.6% | -7.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.08B | -0.6% | -3.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $737.03M | -1.6% | -3.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $543.49M | -1.8% | -4.2% |
| 9 | Sentora Curator | Risk Curators | $450.91M | -1.5% | -10.2% |
| 10 | Marinade Native | Staking Pool | $375.53M | -3.0% | -8.1% |
| 11 | PumpSwap | Dexs | $347.54M | -2.3% | -6.4% |
| 12 | Orca DEX | Dexs | $298.63M | -1.3% | -3.5% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 325 protocols the total is $15.80B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 16.9% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.9%

### Tokenised assets

$894.08M of tokenised real-world assets and equities are locked on Solana - 5.659% of chain TVL.

- OnRe (RWA): $293.31M
- Huma (RWA): $282.44M
- Solstice (Basis Trading): $209.33M
- JupUSD (Basis Trading): $43.84M
- Plume Vaults (RWA): $35.40M

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

- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-16
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-16
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-16
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

### Change over 24h (vs run at 2026-10-15T20:36:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,323.17 | 5,572.51 | +4.68% |
| Average non-vote TPS | 2,236.62 | 2,482.29 | +10.98% |
| Average slot time (ms) | 216.50 | 216.20 | -0.14% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 6,044,693,032.00 | 5,951,004,332.00 | -1.55% |
| SOL price | 105.91 | 103.59 | -2.19% |
| Stablecoin supply | 16,055,865,871.00 | 16,233,803,204.00 | +1.11% |
| 24h DEX volume | 2,118,350,659.32 | 2,539,283,878.03 | +19.87% |
| 24h chain fees | 10,654,111.63 | 12,783,602.89 | +19.99% |

### Change over 7d (vs run at 2026-10-09T21:56:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,940.51 | 5,572.51 | +12.79% |
| Average non-vote TPS | 1,872.44 | 2,482.29 | +32.57% |
| Average slot time (ms) | 218.80 | 216.20 | -1.19% |
| Active validators | 674.00 | 671.00 | -0.45% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 6,170,032,842.00 | 5,951,004,332.00 | -3.55% |
| SOL price | 108.92 | 103.59 | -4.89% |
| Stablecoin supply | 16,379,819,991.00 | 16,233,803,204.00 | -0.89% |
| 24h DEX volume | 2,644,852,886.24 | 2,539,283,878.03 | -3.99% |
| 24h chain fees | 15,072,203.23 | 12,783,602.89 | -15.18% |

### Change over 30d (vs run at 2026-09-16T20:32:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,850.92 | 5,572.51 | +14.88% |
| Average non-vote TPS | 2,744.58 | 2,482.29 | -9.56% |
| Average slot time (ms) | 318.60 | 216.20 | -32.14% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 14.00 | 9.00 | -35.71% |
| Solana TVL | 5,723,932,041.00 | 5,951,004,332.00 | +3.97% |
| SOL price | 98.40 | 103.59 | +5.27% |
| Stablecoin supply | 15,963,602,798.00 | 16,233,803,204.00 | +1.69% |
| 24h DEX volume | 2,703,297,666.22 | 2,539,283,878.03 | -6.07% |
| 24h chain fees | 14,083,156.46 | 12,783,602.89 | -9.23% |

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
