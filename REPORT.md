# Solana Ecosystem Pulse

**Generated:** 2026-10-19T11:23:55Z · **Schema:** `1.0.0` · **Collection time:** 13.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.52 | +0.41% |
| Market cap | $61.62B | rank #7 |
| Total value locked | $5.92B | -0.09% |
| Stablecoin supply | $15.84B | -0.37% |
| DEX volume (24h) | $1.70B | +35.52% |
| Chain fees / REV (24h) | $9.71M | +3.57% |
| Non-vote TPS (1h avg) | 1,699 | peak 6,111 total |
| Active validators | 668 | 11 delinquent |
| Epoch 1062 | 7.29% complete | 400,514 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 110 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,699.2 average over the last 60 minutes; 1,581.3 in the latest sample.
- **Total TPS:** 4,763.2 average, 6,111.4 peak. Consensus votes account for 64.3% of all transactions.
- **Slot time:** 217.0 ms average (target 400 ms), worst 1-minute bucket 227.3 ms.
- **Block height:** 436,850,706 at absolute slot 458,815,486.
- **Epoch 1062:** slot 31,486 of 432,000 (7.29% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.595% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 171 ms |
| `solana-rpc.publicnode.com` | yes | 144 ms |
| `api.mainnet.solana.com` | yes | 104 ms |

## Validators & stake

- **668 active** validators, **11 delinquent** (1.62% by count, 0.004% by stake).
- **Total stake:** 437,880,622 SOL ($45.77B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 12.85%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,095,415 | 3.904% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,730,365 | 3.593% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,524,168 | 2.860% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,975,836 | 2.507% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,890 | 2.219% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,481,609 | 2.165% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,107 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,119 | 1.778% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,993,888 | 1.597% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,731,556 | 1.537% | 0% |

## Economics

- **SOL:** $104.52 (+0.41% 24h, -6.32% 7d, -6.38% 30d). Market cap $61.62B, 24h volume $2.65B (4.31% of cap). Price source: `coingecko`.
- **TVL:** $5.92B across 325 protocols - rank #3 of 420 chains, 6.61% of all tracked chain TVL. -5.34% over 7d, -54.8% from its ATH.
- **Stablecoins:** $15.84B circulating on Solana (-2.10% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.70B in 24h, $14.76B over 7d across 136 venues. Volume/TVL turnover 0.287x per day.
- **REV (chain fees):** $9.71M in 24h, $447.64M over 30d. Retained chain revenue $3.66M (37.7% of fees). Annualised fees are 5.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,494,172 SOL circulating of 636,090,685 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.83B | +1.1% | -0.2% |
| 2 | Kamino Lend | Lending | $1.32B | -0.3% | -1.7% |
| 3 | Raydium AMM | Dexs | $1.18B | +1.3% | -5.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.11B | +1.7% | -4.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.11B | +1.6% | -3.0% |
| 6 | Jupiter Lend | Lending | $1.03B | -5.6% | -10.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $746.17M | +0.9% | -4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $550.60M | +1.2% | -4.2% |
| 9 | Sentora Curator | Risk Curators | $451.09M | +0.0% | -8.3% |
| 10 | Marinade Native | Staking Pool | $383.43M | +0.8% | -7.0% |
| 11 | PumpSwap | Dexs | $350.71M | +1.8% | -5.2% |
| 12 | Orca DEX | Dexs | $299.84M | +0.5% | -3.8% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 325 protocols the total is $15.97B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.9% · Lending 16.4% · Dexs 15.1% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$892.86M of tokenised real-world assets and equities are locked on Solana - 5.592% of chain TVL.

- OnRe (RWA): $293.84M
- Huma (RWA): $280.23M
- Solstice (Basis Trading): $209.35M
- JupUSD (Basis Trading): $43.61M
- Plume Vaults (RWA): $36.04M

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

- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-19
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

### Change over 24h (vs run at 2026-10-18T10:00:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,455.53 | 4,763.24 | +6.91% |
| Average non-vote TPS | 1,366.94 | 1,699.17 | +24.30% |
| Average slot time (ms) | 216.00 | 217.00 | +0.46% |
| Active validators | 669.00 | 668.00 | -0.15% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 5,918,325,763.00 | 5,917,884,285.00 | -0.01% |
| SOL price | 103.93 | 104.52 | +0.57% |
| Stablecoin supply | 15,896,529,268.00 | 15,840,203,152.00 | -0.35% |
| 24h DEX volume | 1,514,655,503.55 | 1,697,352,650.38 | +12.06% |
| 24h chain fees | 9,324,330.53 | 9,709,645.63 | +4.13% |

### Change over 7d (vs run at 2026-10-12T13:42:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,986.47 | 4,763.24 | -4.48% |
| Average non-vote TPS | 1,921.73 | 1,699.17 | -11.58% |
| Average slot time (ms) | 218.40 | 217.00 | -0.64% |
| Active validators | 673.00 | 668.00 | -0.74% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 6,257,692,157.00 | 5,917,884,285.00 | -5.43% |
| SOL price | 110.09 | 104.52 | -5.06% |
| Stablecoin supply | 16,360,925,699.00 | 15,840,203,152.00 | -3.18% |
| 24h DEX volume | 1,277,019,605.31 | 1,697,352,650.38 | +32.92% |
| 24h chain fees | 11,200,431.37 | 9,709,645.63 | -13.31% |

### Change over 30d (vs run at 2026-09-19T19:41:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,683.68 | 4,763.24 | +1.70% |
| Average non-vote TPS | 2,161.60 | 1,699.17 | -21.39% |
| Average slot time (ms) | 267.00 | 217.00 | -18.73% |
| Active validators | 677.00 | 668.00 | -1.33% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 6,243,262,565.00 | 5,917,884,285.00 | -5.21% |
| SOL price | 111.27 | 104.52 | -6.07% |
| Stablecoin supply | 15,875,774,561.00 | 15,840,203,152.00 | -0.22% |
| 24h DEX volume | 3,536,797,881.43 | 1,697,352,650.38 | -52.01% |
| 24h chain fees | 17,457,812.00 | 9,709,645.63 | -44.38% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
