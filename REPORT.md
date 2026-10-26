# Solana Ecosystem Pulse

**Generated:** 2026-10-26T11:41:41Z · **Schema:** `1.0.0` · **Collection time:** 14.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.37 | +0.63% |
| Market cap | $59.79B | rank #7 |
| Total value locked | $5.74B | -1.07% |
| Stablecoin supply | $15.88B | -0.34% |
| DEX volume (24h) | $1.45B | +1.84% |
| Chain fees / REV (24h) | $9.30M | -7.43% |
| Non-vote TPS (1h avg) | 1,478 | peak 1,800 total |
| Active validators | 665 | 25 delinquent |
| Epoch 1068 | 63.62% complete | 157,164 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 122 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,478; the healthy floor used here is 1,500. | `threshold` |
| [SERIOUS] | Average TPS is below its recent norm | Current 1,478.31 sits 5.8 sigma below the median of the last 122 runs (4,617.72, -68.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 25.00 sits 3.8 sigma above the median of the last 122 runs (11.00, +127.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,478.3 average over the last 60 minutes; 1,584.1 in the latest sample.
- **Total TPS:** 1,478.3 average, 1,800.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.9 ms average (target 400 ms), worst 1-minute bucket 215.8 ms.
- **Block height:** 439,678,022 at absolute slot 461,650,836.
- **Epoch 1068:** slot 274,836 of 432,000 (63.62% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.586% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 132 ms |
| `solana-rpc.publicnode.com` | yes | 108 ms |
| `api.mainnet.solana.com` | yes | 162 ms |

## Validators & stake

- **665 active** validators, **25 delinquent** (3.62% by count, 0.123% by stake).
- **Total stake:** 437,716,746 SOL ($44.37B); stake rate 68.77% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.57% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 13.21%; 227 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,102,487 | 3.912% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,635,523 | 3.805% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,594,585 | 2.881% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,882,967 | 2.489% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,720,520 | 2.223% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,492,382 | 2.171% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,187,388 | 2.102% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,787,018 | 1.781% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,039,209 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,989,716 | 1.599% | 0% |

## Economics

- **SOL:** $101.37 (+0.63% 24h, -3.36% 7d, -15.94% 30d). Market cap $59.79B, 24h volume $1.92B (3.21% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 333 protocols - rank #4 of 421 chains, 6.46% of all tracked chain TVL. -2.36% over 7d, -55.7% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (+0.25% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.45B in 24h, $13.44B over 7d across 138 venues. Volume/TVL turnover 0.252x per day.
- **REV (chain fees):** $9.30M in 24h, $426.95M over 30d. Retained chain revenue $3.48M (37.4% of fees). Annualised fees are 5.68% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,819,654 SOL circulating of 636,457,092 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | +1.0% | -1.9% |
| 2 | Kamino Lend | Lending | $1.27B | +0.4% | -3.1% |
| 3 | Raydium AMM | Dexs | $1.14B | -1.3% | -3.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.07B | +0.7% | -1.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | +0.8% | -3.4% |
| 6 | Jupiter Lend | Lending | $1.01B | -0.3% | -0.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $717.08M | +0.3% | -2.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $529.43M | +0.6% | -3.0% |
| 9 | Sentora Curator | Risk Curators | $387.32M | -2.4% | -14.1% |
| 10 | Marinade Native | Staking Pool | $364.67M | +0.7% | -4.4% |
| 11 | PumpSwap | Dexs | $336.93M | -0.5% | -3.9% |
| 12 | Orca DEX | Dexs | $300.04M | -0.1% | +0.3% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.8%

### Tokenised assets

$859.77M of tokenised real-world assets and equities are locked on Solana - 5.578% of chain TVL.

- OnRe (RWA): $295.92M
- Huma (RWA): $252.52M
- Solstice (Basis Trading): $201.79M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.47M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) - Fri, 23 Oct 2026 01:09:00 GMT
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-26
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-25
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21
- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-25T10:16:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,206.01 | 1,478.31 | +22.58% |
| Average non-vote TPS | 1,206.01 | 1,478.31 | +22.58% |
| Average slot time (ms) | 212.20 | 211.90 | -0.14% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 25.00 | 25.00 | +0.00% |
| Solana TVL | 5,778,836,045.00 | 5,740,388,903.00 | -0.67% |
| SOL price | 100.82 | 101.37 | +0.55% |
| Stablecoin supply | 15,930,791,568.00 | 15,877,222,933.00 | -0.34% |
| 24h DEX volume | 1,732,393,737.80 | 1,449,231,950.27 | -16.35% |
| 24h chain fees | 9,945,781.91 | 9,299,425.03 | -6.50% |

### Change over 7d (vs run at 2026-10-19T11:23:55Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,763.24 | 1,478.31 | -68.96% |
| Average non-vote TPS | 1,699.17 | 1,478.31 | -13.00% |
| Average slot time (ms) | 217.00 | 211.90 | -2.35% |
| Active validators | 668.00 | 665.00 | -0.45% |
| Delinquent validators | 11.00 | 25.00 | +127.27% |
| Solana TVL | 5,917,884,285.00 | 5,740,388,903.00 | -3.00% |
| SOL price | 104.52 | 101.37 | -3.01% |
| Stablecoin supply | 15,840,203,152.00 | 15,877,222,933.00 | +0.23% |
| 24h DEX volume | 1,697,352,650.38 | 1,449,231,950.27 | -14.62% |
| 24h chain fees | 9,709,645.63 | 9,299,425.03 | -4.22% |

### Change over 30d (vs run at 2026-09-26T20:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,730.02 | 1,478.31 | -68.75% |
| Average non-vote TPS | 2,233.16 | 1,478.31 | -33.80% |
| Average slot time (ms) | 269.50 | 211.90 | -21.37% |
| Active validators | 676.00 | 665.00 | -1.63% |
| Delinquent validators | 11.00 | 25.00 | +127.27% |
| Solana TVL | 6,636,693,564.00 | 5,740,388,903.00 | -13.51% |
| SOL price | 120.95 | 101.37 | -16.19% |
| Stablecoin supply | 16,991,136,948.00 | 15,877,222,933.00 | -6.56% |
| 24h DEX volume | 2,613,053,225.63 | 1,449,231,950.27 | -44.54% |
| 24h chain fees | 15,598,587.47 | 9,299,425.03 | -40.38% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
