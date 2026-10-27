# Solana Ecosystem Pulse

**Generated:** 2026-10-27T02:38:23Z · **Schema:** `1.0.0` · **Collection time:** 16.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.22 | -0.35% |
| Market cap | $59.12B | rank #7 |
| Total value locked | $5.71B | -0.13% |
| Stablecoin supply | $15.76B | -0.55% |
| DEX volume (24h) | $1.72B | +18.38% |
| Chain fees / REV (24h) | $11.61M | +24.90% |
| Non-vote TPS (1h avg) | 1,931 | peak 2,649 total |
| Active validators | 664 | 21 delinquent |
| Epoch 1069 | 22.23% complete | 335,971 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 124 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,931.02 sits 4.6 sigma below the median of the last 124 runs (4,593.73, -58.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,931.0 average over the last 60 minutes; 1,915.7 in the latest sample.
- **Total TPS:** 1,931.0 average, 2,649.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.7 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 439,929,963 at absolute slot 461,904,029.
- **Epoch 1069:** slot 96,029 of 432,000 (22.23% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.584% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 236 ms |
| `solana-rpc.publicnode.com` | yes | 179 ms |
| `api.mainnet.solana.com` | yes | 177 ms |

## Validators & stake

- **664 active** validators, **21 delinquent** (3.07% by count, 0.128% by stake).
- **Total stake:** 436,873,593 SOL ($43.78B); stake rate 68.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.61% and top 33 hold 45.98% of active stake.
- **Commission:** median 5.0%, mean 12.77%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,059,304 | 3.910% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,636,453 | 3.813% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,660,117 | 2.902% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,812,577 | 2.478% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,716,980 | 2.227% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,494,053 | 2.176% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,206,552 | 2.110% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,754,189 | 1.777% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,040,177 | 1.614% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,375 | 1.604% | 0% |

## Economics

- **SOL:** $100.22 (-0.35% 24h, -4.36% 7d, -17.45% 30d). Market cap $59.12B, 24h volume $2.38B (4.02% of cap). Price source: `coingecko`.
- **TVL:** $5.71B across 333 protocols - rank #3 of 421 chains, 6.47% of all tracked chain TVL. -2.75% over 7d, -55.9% from its ATH.
- **Stablecoins:** $15.76B circulating on Solana (-0.92% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.72B in 24h, $12.70B over 7d across 138 venues. Volume/TVL turnover 0.300x per day.
- **REV (chain fees):** $11.61M in 24h, $417.85M over 30d. Retained chain revenue $4.57M (39.4% of fees). Annualised fees are 7.17% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,874,718 SOL circulating of 636,517,793 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.77B | -0.4% | -2.4% |
| 2 | Kamino Lend | Lending | $1.26B | -0.1% | -3.2% |
| 3 | Raydium AMM | Dexs | $1.13B | -0.9% | -4.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.07B | +0.3% | -2.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.05B | -0.4% | -4.0% |
| 6 | Jupiter Lend | Lending | $1.01B | +0.4% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $714.12M | -0.3% | -3.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $525.84M | -0.9% | -3.7% |
| 9 | Sentora Curator | Risk Curators | $384.03M | -0.8% | -14.3% |
| 10 | Marinade Native | Staking Pool | $362.94M | -0.3% | -4.0% |
| 11 | PumpSwap | Dexs | $334.57M | -1.0% | -4.1% |
| 12 | Orca DEX | Dexs | $299.78M | -0.4% | +0.5% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.36B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.6% · Dexs 15.1% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$864.65M of tokenised real-world assets and equities are locked on Solana - 5.630% of chain TVL.

- OnRe (RWA): $295.91M
- Huma (RWA): $257.38M
- Solstice (Basis Trading): $201.69M
- JupUSD (Basis Trading): $42.96M
- Plume Vaults (RWA): $36.55M

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
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | pre-release |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-27
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-27
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-26
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-26
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-26
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23

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

### Change over 24h (vs run at 2026-10-26T02:00:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,938.20 | 1,931.02 | -0.37% |
| Average non-vote TPS | 1,938.20 | 1,931.02 | -0.37% |
| Average slot time (ms) | 212.80 | 212.70 | -0.05% |
| Active validators | 665.00 | 664.00 | -0.15% |
| Delinquent validators | 25.00 | 21.00 | -16.00% |
| Solana TVL | 5,735,902,141.00 | 5,713,801,800.00 | -0.39% |
| SOL price | 100.91 | 100.22 | -0.68% |
| Stablecoin supply | 15,877,624,594.00 | 15,762,408,098.00 | -0.73% |
| 24h DEX volume | 1,348,643,859.27 | 1,715,656,452.15 | +27.21% |
| 24h chain fees | 10,086,756.26 | 11,607,021.57 | +15.07% |

### Change over 7d (vs run at 2026-10-20T02:21:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,836.27 | 1,931.02 | -60.07% |
| Average non-vote TPS | 1,787.15 | 1,931.02 | +8.05% |
| Average slot time (ms) | 218.30 | 212.70 | -2.57% |
| Active validators | 668.00 | 664.00 | -0.60% |
| Delinquent validators | 11.00 | 21.00 | +90.91% |
| Solana TVL | 5,874,392,428.00 | 5,713,801,800.00 | -2.73% |
| SOL price | 104.78 | 100.22 | -4.35% |
| Stablecoin supply | 15,910,715,203.00 | 15,762,408,098.00 | -0.93% |
| 24h DEX volume | 1,610,955,050.83 | 1,715,656,452.15 | +6.50% |
| 24h chain fees | 11,948,280.30 | 11,607,021.57 | -2.86% |

### Change over 30d (vs run at 2026-09-26T20:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,730.02 | 1,931.02 | -59.18% |
| Average non-vote TPS | 2,233.16 | 1,931.02 | -13.53% |
| Average slot time (ms) | 269.50 | 212.70 | -21.08% |
| Active validators | 676.00 | 664.00 | -1.78% |
| Delinquent validators | 11.00 | 21.00 | +90.91% |
| Solana TVL | 6,636,693,564.00 | 5,713,801,800.00 | -13.91% |
| SOL price | 120.95 | 100.22 | -17.14% |
| Stablecoin supply | 16,991,136,948.00 | 15,762,408,098.00 | -7.23% |
| 24h DEX volume | 2,613,053,225.63 | 1,715,656,452.15 | -34.34% |
| 24h chain fees | 15,598,587.47 | 11,607,021.57 | -25.59% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
