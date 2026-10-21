# Solana Ecosystem Pulse

**Generated:** 2026-10-21T10:43:25Z · **Schema:** `1.0.0` · **Collection time:** 15.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $106.30 | +2.39% |
| Market cap | $62.67B | rank #7 |
| Total value locked | $6.00B | +2.18% |
| Stablecoin supply | $16.01B | +0.62% |
| DEX volume (24h) | $2.24B | +22.56% |
| Chain fees / REV (24h) | $13.20M | +9.96% |
| Non-vote TPS (1h avg) | 1,525 | peak 5,117 total |
| Active validators | 668 | 11 delinquent |
| Epoch 1063 | 88.86% complete | 48,127 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 114 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,524.6 average over the last 60 minutes; 1,334.3 in the latest sample.
- **Total TPS:** 4,602.9 average, 5,116.6 peak. Consensus votes account for 66.9% of all transactions.
- **Slot time:** 216.0 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 437,634,669 at absolute slot 459,599,873.
- **Epoch 1063:** slot 383,873 of 432,000 (88.86% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.594% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 263 ms |
| `solana-rpc.publicnode.com` | yes | 87 ms |
| `api.mainnet.solana.com` | yes | 158 ms |

## Validators & stake

- **668 active** validators, **11 delinquent** (1.62% by count, 0.002% by stake).
- **Total stake:** 438,577,211 SOL ($46.62B); stake rate 68.94% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 13.16%; 227 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,103,015 | 3.900% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,937,532 | 3.634% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,537,315 | 2.859% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,930,434 | 2.492% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,707 | 2.216% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,482,037 | 2.162% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,253,756 | 2.110% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,792,210 | 1.777% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,034,138 | 1.604% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,000,331 | 1.596% | 0% |

## Economics

- **SOL:** $106.30 (+2.39% 24h, -0.26% 7d, -8.23% 30d). Market cap $62.67B, 24h volume $2.67B (4.26% of cap). Price source: `coingecko`.
- **TVL:** $6.00B across 329 protocols - rank #3 of 421 chains, 6.62% of all tracked chain TVL. -0.68% over 7d, -53.7% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.91% 7d) - $2.67 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.24B in 24h, $13.15B over 7d across 136 venues. Volume/TVL turnover 0.372x per day.
- **REV (chain fees):** $13.20M in 24h, $443.42M over 30d. Retained chain revenue $5.59M (42.4% of fees). Annualised fees are 7.69% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,548,769 SOL circulating of 636,151,044 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.86B | +3.3% | +3.0% |
| 2 | Kamino Lend | Lending | $1.34B | +1.9% | +2.4% |
| 3 | Raydium AMM | Dexs | $1.20B | +1.9% | -1.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.12B | +3.3% | +2.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.11B | +2.3% | -2.9% |
| 6 | Jupiter Lend | Lending | $1.05B | +2.4% | -5.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $750.64M | +2.4% | -0.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $561.61M | +3.3% | +0.5% |
| 9 | Sentora Curator | Risk Curators | $432.41M | -3.6% | -8.5% |
| 10 | Marinade Native | Staking Pool | $383.96M | +2.2% | -2.4% |
| 11 | PumpSwap | Dexs | $355.18M | +2.8% | -0.7% |
| 12 | Orca DEX | Dexs | $305.26M | +1.8% | +1.4% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 329 protocols the total is $16.11B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.6% · Dexs 15.1% · Derivatives 5.1% · Risk Curators 3.8% · RWA 3.7%

### Tokenised assets

$865.12M of tokenised real-world assets and equities are locked on Solana - 5.369% of chain TVL.

- OnRe (RWA): $293.98M
- Huma (RWA): $253.77M
- Solstice (Basis Trading): $209.24M
- JupUSD (Basis Trading): $42.95M
- Plume Vaults (RWA): $35.54M

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

- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-21
- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-10-21
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-21
- [SIMD-0529: [SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-20
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-20
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-20
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-20

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

### Change over 24h (vs run at 2026-10-20T10:31:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,654.59 | 4,602.94 | -1.11% |
| Average non-vote TPS | 1,613.52 | 1,524.60 | -5.51% |
| Average slot time (ms) | 217.80 | 216.00 | -0.83% |
| Active validators | 666.00 | 668.00 | +0.30% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 5,879,479,880.00 | 6,001,273,500.00 | +2.07% |
| SOL price | 103.92 | 106.30 | +2.29% |
| Stablecoin supply | 15,910,967,401.00 | 16,008,541,783.00 | +0.61% |
| 24h DEX volume | 1,610,948,501.83 | 2,235,068,600.00 | +38.74% |
| 24h chain fees | 11,969,320.99 | 13,200,582.40 | +10.29% |

### Change over 7d (vs run at 2026-10-14T10:44:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,517.95 | 4,602.94 | +1.88% |
| Average non-vote TPS | 1,423.12 | 1,524.60 | +7.13% |
| Average slot time (ms) | 216.50 | 216.00 | -0.23% |
| Active validators | 673.00 | 668.00 | -0.74% |
| Delinquent validators | 5.00 | 11.00 | +120.00% |
| Solana TVL | 6,066,631,253.00 | 6,001,273,500.00 | -1.08% |
| SOL price | 106.75 | 106.30 | -0.42% |
| Stablecoin supply | 16,500,896,449.00 | 16,008,541,783.00 | -2.98% |
| 24h DEX volume | 2,309,961,007.38 | 2,235,068,600.00 | -3.24% |
| 24h chain fees | 11,690,508.74 | 13,200,582.40 | +12.92% |

### Change over 30d (vs run at 2026-09-21T21:17:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.01 | 4,602.94 | -1.20% |
| Average non-vote TPS | 2,142.85 | 1,524.60 | -28.85% |
| Average slot time (ms) | 266.70 | 216.00 | -19.01% |
| Active validators | 676.00 | 668.00 | -1.18% |
| Delinquent validators | 14.00 | 11.00 | -21.43% |
| Solana TVL | 6,474,683,879.00 | 6,001,273,500.00 | -7.31% |
| SOL price | 118.81 | 106.30 | -10.53% |
| Stablecoin supply | 15,907,385,261.00 | 16,008,541,783.00 | +0.64% |
| 24h DEX volume | 2,795,356,104.36 | 2,235,068,600.00 | -20.04% |
| 24h chain fees | 14,463,382.08 | 13,200,582.40 | -8.73% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
