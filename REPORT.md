# Solana Ecosystem Pulse

**Generated:** 2026-10-21T16:12:15Z · **Schema:** `1.0.0` · **Collection time:** 16.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $108.45 | +2.61% |
| Market cap | $63.95B | rank #7 |
| Total value locked | $6.03B | +2.63% |
| Stablecoin supply | $16.01B | +0.62% |
| DEX volume (24h) | $2.44B | +33.68% |
| Chain fees / REV (24h) | $13.17M | +9.65% |
| Non-vote TPS (1h avg) | 2,383 | peak 3,034 total |
| Active validators | 666 | 11 delinquent |
| Epoch 1064 | 10.21% complete | 387,889 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 115 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,382.73 sits 4.9 sigma below the median of the last 115 runs (4,673.89, -49.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,382.7 average over the last 60 minutes; 2,579.0 in the latest sample.
- **Total TPS:** 2,382.7 average, 3,033.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.4 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 437,726,464 at absolute slot 459,692,111.
- **Epoch 1064:** slot 44,111 of 432,000 (10.21% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.592% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 193 ms |
| `solana-rpc.publicnode.com` | yes | 172 ms |
| `api.mainnet.solana.com` | yes | 180 ms |

## Validators & stake

- **666 active** validators, **11 delinquent** (1.62% by count, 0.018% by stake).
- **Total stake:** 438,868,046 SOL ($47.60B); stake rate 68.98% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.36% and top 33 hold 45.95% of active stake.
- **Commission:** median 5.0%, mean 12.89%; 228 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,130,984 | 3.904% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,955,653 | 3.636% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,545,894 | 2.859% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,933,491 | 2.492% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,728,193 | 2.217% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,480,474 | 2.161% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,296 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,808,122 | 1.779% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,035,085 | 1.603% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,557 | 1.596% | 0% |

## Economics

- **SOL:** $108.45 (+2.61% 24h, +4.45% 7d, -8.09% 30d). Market cap $63.95B, 24h volume $2.44B (3.82% of cap). Price source: `coingecko`.
- **TVL:** $6.03B across 329 protocols - rank #3 of 421 chains, 6.53% of all tracked chain TVL. -0.24% over 7d, -53.5% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.90% 7d) - $2.66 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.44B in 24h, $14.30B over 7d across 137 venues. Volume/TVL turnover 0.404x per day.
- **REV (chain fees):** $13.17M in 24h, $443.82M over 30d. Retained chain revenue $5.61M (42.6% of fees). Annualised fees are 7.51% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,604,856 SOL circulating of 636,212,885 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.88B | +2.4% | +3.8% |
| 2 | Kamino Lend | Lending | $1.35B | +1.2% | +2.8% |
| 3 | Raydium AMM | Dexs | $1.21B | +3.0% | +0.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.12B | +1.5% | +2.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.11B | +0.7% | -3.0% |
| 6 | Jupiter Lend | Lending | $1.05B | +1.3% | -5.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $753.81M | +1.7% | -0.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $559.03M | +1.5% | +0.1% |
| 9 | Sentora Curator | Risk Curators | $432.17M | -0.2% | -8.5% |
| 10 | Marinade Native | Staking Pool | $386.12M | +1.4% | -1.9% |
| 11 | PumpSwap | Dexs | $361.10M | +4.1% | +1.0% |
| 12 | Orca DEX | Dexs | $307.32M | +1.8% | +2.0% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 329 protocols the total is $16.18B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 3.8% · RWA 3.7%

### Tokenised assets

$864.73M of tokenised real-world assets and equities are locked on Solana - 5.345% of chain TVL.

- OnRe (RWA): $294.26M
- Huma (RWA): $253.88M
- Solstice (Basis Trading): $208.42M
- JupUSD (Basis Trading): $42.95M
- Plume Vaults (RWA): $35.55M

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

- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-21
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [SIMD-0529: [SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21
- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-10-21
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/702) - updated 2026-10-21
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-20T15:55:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,972.94 | 2,382.73 | -60.11% |
| Average non-vote TPS | 2,923.71 | 2,382.73 | -18.50% |
| Average slot time (ms) | 218.50 | 212.40 | -2.79% |
| Active validators | 669.00 | 666.00 | -0.45% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,919,592,225.00 | 6,027,723,667.00 | +1.83% |
| SOL price | 105.27 | 108.45 | +3.02% |
| Stablecoin supply | 15,910,894,936.00 | 16,009,406,077.00 | +0.62% |
| 24h DEX volume | 1,823,579,289.83 | 2,437,800,207.00 | +33.68% |
| 24h chain fees | 11,986,038.75 | 13,166,309.40 | +9.85% |

### Change over 7d (vs run at 2026-10-14T16:03:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,476.80 | 2,382.73 | -56.49% |
| Average non-vote TPS | 2,393.65 | 2,382.73 | -0.46% |
| Average slot time (ms) | 217.10 | 212.40 | -2.16% |
| Active validators | 672.00 | 666.00 | -0.89% |
| Delinquent validators | 6.00 | 11.00 | +83.33% |
| Solana TVL | 5,957,694,019.00 | 6,027,723,667.00 | +1.18% |
| SOL price | 103.88 | 108.45 | +4.40% |
| Stablecoin supply | 16,320,610,416.00 | 16,009,406,077.00 | -1.91% |
| 24h DEX volume | 2,495,170,004.38 | 2,437,800,207.00 | -2.30% |
| 24h chain fees | 11,649,593.74 | 13,166,309.40 | +13.02% |

### Change over 30d (vs run at 2026-09-21T21:17:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.01 | 2,382.73 | -48.86% |
| Average non-vote TPS | 2,142.85 | 2,382.73 | +11.19% |
| Average slot time (ms) | 266.70 | 212.40 | -20.36% |
| Active validators | 676.00 | 666.00 | -1.48% |
| Delinquent validators | 14.00 | 11.00 | -21.43% |
| Solana TVL | 6,474,683,879.00 | 6,027,723,667.00 | -6.90% |
| SOL price | 118.81 | 108.45 | -8.72% |
| Stablecoin supply | 15,907,385,261.00 | 16,009,406,077.00 | +0.64% |
| 24h DEX volume | 2,795,356,104.36 | 2,437,800,207.00 | -12.79% |
| 24h chain fees | 14,463,382.08 | 13,166,309.40 | -8.97% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
