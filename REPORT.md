# Solana Ecosystem Pulse

**Generated:** 2026-10-28T02:47:18Z · **Schema:** `1.0.0` · **Collection time:** 12.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.49 | +1.31% |
| Market cap | $59.86B | rank #7 |
| Total value locked | $5.73B | +0.34% |
| Stablecoin supply | $15.78B | +0.10% |
| DEX volume (24h) | $1.85B | -10.72% |
| Chain fees / REV (24h) | $11.08M | -5.05% |
| Non-vote TPS (1h avg) | 1,716 | peak 2,308 total |
| Active validators | 662 | 29 delinquent |
| Epoch 1070 | 16.80% complete | 359,443 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 126 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,716.48 sits 4.7 sigma below the median of the last 126 runs (4,551.33, -62.3%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 29.00 sits 4.0 sigma above the median of the last 126 runs (11.00, +163.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,716.5 average over the last 60 minutes; 1,508.6 in the latest sample.
- **Total TPS:** 1,716.5 average, 2,308.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.2 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 440,337,229 at absolute slot 462,312,557.
- **Epoch 1070:** slot 72,557 of 432,000 (16.80% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.583% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 143 ms |
| `solana-rpc.publicnode.com` | yes | 55 ms |
| `api.mainnet.solana.com` | yes | 101 ms |

## Validators & stake

- **662 active** validators, **29 delinquent** (4.20% by count, 0.886% by stake).
- **Total stake:** 437,290,026 SOL ($44.38B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.34% of active stake.
- **Commission:** median 5.0%, mean 12.71%; 230 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,006,422 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,661,096 | 3.844% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,791,931 | 2.951% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,815,143 | 2.495% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,548 | 2.242% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,464,443 | 2.184% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,208,877 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,757,994 | 1.790% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,041,146 | 1.625% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,044 | 1.614% | 0% |

## Economics

- **SOL:** $101.49 (+1.31% 24h, -4.83% 7d, -15.92% 30d). Market cap $59.86B, 24h volume $2.03B (3.38% of cap). Price source: `coingecko`.
- **TVL:** $5.73B across 335 protocols - rank #4 of 421 chains, 6.45% of all tracked chain TVL. -4.32% over 7d, -55.8% from its ATH.
- **Stablecoins:** $15.78B circulating on Solana (-1.45% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.85B in 24h, $11.94B over 7d across 138 venues. Volume/TVL turnover 0.322x per day.
- **REV (chain fees):** $11.08M in 24h, $409.65M over 30d. Retained chain revenue $4.15M (37.5% of fees). Annualised fees are 6.76% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,928,530 SOL circulating of 636,578,323 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +1.2% | -3.6% |
| 2 | Kamino Lend | Lending | $1.27B | +0.3% | -5.2% |
| 3 | Raydium AMM | Dexs | $1.14B | +1.1% | -5.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.09B | +2.0% | -2.6% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.05B | +0.3% | -5.0% |
| 6 | Jupiter Lend | Lending | $1.01B | +0.0% | -3.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $717.11M | +0.7% | -4.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $529.96M | +0.8% | -5.1% |
| 9 | Sentora Curator | Risk Curators | $383.87M | -0.0% | -11.3% |
| 10 | Marinade Native | Staking Pool | $363.12M | +0.5% | -5.8% |
| 11 | PumpSwap | Dexs | $334.05M | -0.2% | -5.7% |
| 12 | Orca DEX | Dexs | $303.16M | +1.1% | -0.4% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 335 protocols the total is $15.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.9% · Lending 16.5% · Dexs 15.2% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$866.73M of tokenised real-world assets and equities are locked on Solana - 5.609% of chain TVL.

- OnRe (RWA): $301.23M
- Huma (RWA): $253.66M
- Solstice (Basis Trading): $201.51M
- JupUSD (Basis Trading): $42.98M
- Plume Vaults (RWA): $37.18M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup) - Mon, 26 Oct 2026 10:00:00 GMT
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) - Fri, 23 Oct 2026 01:09:00 GMT
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-27
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-27T02:38:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,931.02 | 1,716.48 | -11.11% |
| Average non-vote TPS | 1,931.02 | 1,716.48 | -11.11% |
| Average slot time (ms) | 212.70 | 213.20 | +0.24% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 21.00 | 29.00 | +38.10% |
| Solana TVL | 5,713,801,800.00 | 5,734,907,585.00 | +0.37% |
| SOL price | 100.22 | 101.49 | +1.27% |
| Stablecoin supply | 15,762,408,098.00 | 15,779,317,711.00 | +0.11% |
| 24h DEX volume | 1,715,656,452.15 | 1,848,988,925.55 | +7.77% |
| 24h chain fees | 11,607,021.57 | 11,083,243.89 | -4.51% |

### Change over 7d (vs run at 2026-10-21T02:14:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,925.73 | 1,716.48 | -65.15% |
| Average non-vote TPS | 1,852.43 | 1,716.48 | -7.34% |
| Average slot time (ms) | 216.20 | 213.20 | -1.39% |
| Active validators | 669.00 | 662.00 | -1.05% |
| Delinquent validators | 10.00 | 29.00 | +190.00% |
| Solana TVL | 5,993,789,217.00 | 5,734,907,585.00 | -4.32% |
| SOL price | 106.33 | 101.49 | -4.55% |
| Stablecoin supply | 16,013,636,672.00 | 15,779,317,711.00 | -1.46% |
| 24h DEX volume | 2,235,070,439.00 | 1,848,988,925.55 | -17.27% |
| 24h chain fees | 13,196,843.63 | 11,083,243.89 | -16.02% |

### Change over 30d (vs run at 2026-09-27T20:31:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.15 | 1,716.48 | -63.16% |
| Average non-vote TPS | 2,150.72 | 1,716.48 | -20.19% |
| Average slot time (ms) | 268.10 | 213.20 | -20.48% |
| Active validators | 675.00 | 662.00 | -1.93% |
| Delinquent validators | 8.00 | 29.00 | +262.50% |
| Solana TVL | 6,696,462,246.00 | 5,734,907,585.00 | -14.36% |
| SOL price | 122.76 | 101.49 | -17.33% |
| Stablecoin supply | 16,803,216,984.00 | 15,779,317,711.00 | -6.09% |
| 24h DEX volume | 2,155,234,120.21 | 1,848,988,925.55 | -14.21% |
| 24h chain fees | 17,938,389.57 | 11,083,243.89 | -38.21% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
