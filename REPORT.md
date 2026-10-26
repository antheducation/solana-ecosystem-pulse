# Solana Ecosystem Pulse

**Generated:** 2026-10-26T21:59:11Z · **Schema:** `1.0.0` · **Collection time:** 14.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.45 | -0.68% |
| Market cap | $59.27B | rank #7 |
| Total value locked | $5.71B | -1.59% |
| Stablecoin supply | $15.85B | -0.37% |
| DEX volume (24h) | $1.45B | +1.84% |
| Chain fees / REV (24h) | $9.29M | -7.51% |
| Non-vote TPS (1h avg) | 1,853 | peak 2,770 total |
| Active validators | 665 | 20 delinquent |
| Epoch 1069 | 3.99% complete | 414,771 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 123 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,853.07 sits 4.8 sigma below the median of the last 123 runs (4,602.94, -59.7%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,853.1 average over the last 60 minutes; 2,110.2 in the latest sample.
- **Total TPS:** 1,853.1 average, 2,770.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.9 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 439,851,459 at absolute slot 461,825,229.
- **Epoch 1069:** slot 17,229 of 432,000 (3.99% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.584% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 136 ms |
| `solana-rpc.publicnode.com` | yes | 103 ms |
| `api.mainnet.solana.com` | yes | 103 ms |

## Validators & stake

- **665 active** validators, **20 delinquent** (2.92% by count, 0.085% by stake).
- **Total stake:** 436,873,593 SOL ($43.88B); stake rate 68.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.60% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,059,304 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,636,453 | 3.811% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,660,117 | 2.900% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,812,577 | 2.477% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,716,980 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,494,053 | 2.175% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,206,552 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,754,189 | 1.776% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,040,177 | 1.613% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,375 | 1.603% | 0% |

## Economics

- **SOL:** $100.45 (-0.68% 24h, -3.85% 7d, -16.52% 30d). Market cap $59.27B, 24h volume $2.52B (4.25% of cap). Price source: `coingecko`.
- **TVL:** $5.71B across 333 protocols - rank #3 of 421 chains, 6.46% of all tracked chain TVL. -2.87% over 7d, -56.0% from its ATH.
- **Stablecoins:** $15.85B circulating on Solana (+0.08% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.45B in 24h, $13.44B over 7d across 138 venues. Volume/TVL turnover 0.254x per day.
- **REV (chain fees):** $9.29M in 24h, $426.96M over 30d. Retained chain revenue $3.47M (37.4% of fees). Annualised fees are 5.72% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,874,907 SOL circulating of 636,517,877 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.76B | -1.0% | -2.8% |
| 2 | Kamino Lend | Lending | $1.26B | -1.1% | -3.6% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.9% | -3.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.06B | -1.1% | -2.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.04B | -1.3% | -4.7% |
| 6 | Jupiter Lend | Lending | $1.00B | -1.2% | -1.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $710.96M | -1.1% | -3.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $524.53M | -1.4% | -3.9% |
| 9 | Sentora Curator | Risk Curators | $383.97M | -0.9% | -14.8% |
| 10 | Marinade Native | Staking Pool | $362.28M | -0.9% | -5.0% |
| 11 | PumpSwap | Dexs | $336.14M | -0.6% | -4.1% |
| 12 | Orca DEX | Dexs | $301.03M | -0.4% | +0.6% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.31B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.7% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$858.47M of tokenised real-world assets and equities are locked on Solana - 5.606% of chain TVL.

- OnRe (RWA): $295.81M
- Huma (RWA): $251.41M
- Solstice (Basis Trading): $201.64M
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

- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-26
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-26
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-26
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-26
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-26
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22

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

### Change over 24h (vs run at 2026-10-25T20:04:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,732.39 | 1,853.07 | +6.97% |
| Average non-vote TPS | 1,732.38 | 1,853.06 | +6.97% |
| Average slot time (ms) | 212.20 | 211.90 | -0.14% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 25.00 | 20.00 | -20.00% |
| Solana TVL | 5,770,053,619.00 | 5,710,299,220.00 | -1.04% |
| SOL price | 101.63 | 100.45 | -1.16% |
| Stablecoin supply | 15,930,366,369.00 | 15,849,510,602.00 | -0.51% |
| 24h DEX volume | 1,423,041,369.80 | 1,449,231,950.27 | +1.84% |
| 24h chain fees | 10,045,733.76 | 9,292,855.03 | -7.49% |

### Change over 7d (vs run at 2026-10-19T21:47:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,210.74 | 1,853.07 | -64.44% |
| Average non-vote TPS | 2,163.29 | 1,853.06 | -14.34% |
| Average slot time (ms) | 218.40 | 211.90 | -2.98% |
| Active validators | 669.00 | 665.00 | -0.60% |
| Delinquent validators | 10.00 | 20.00 | +100.00% |
| Solana TVL | 5,846,232,281.00 | 5,710,299,220.00 | -2.33% |
| SOL price | 104.69 | 100.45 | -4.05% |
| Stablecoin supply | 15,840,000,252.00 | 15,849,510,602.00 | +0.06% |
| 24h DEX volume | 1,697,352,650.38 | 1,449,231,950.27 | -14.62% |
| 24h chain fees | 9,839,385.63 | 9,292,855.03 | -5.55% |

### Change over 30d (vs run at 2026-09-26T20:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,730.02 | 1,853.07 | -60.82% |
| Average non-vote TPS | 2,233.16 | 1,853.06 | -17.02% |
| Average slot time (ms) | 269.50 | 211.90 | -21.37% |
| Active validators | 676.00 | 665.00 | -1.63% |
| Delinquent validators | 11.00 | 20.00 | +81.82% |
| Solana TVL | 6,636,693,564.00 | 5,710,299,220.00 | -13.96% |
| SOL price | 120.95 | 100.45 | -16.95% |
| Stablecoin supply | 16,991,136,948.00 | 15,849,510,602.00 | -6.72% |
| 24h DEX volume | 2,613,053,225.63 | 1,449,231,950.27 | -44.54% |
| 24h chain fees | 15,598,587.47 | 9,292,855.03 | -40.43% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
