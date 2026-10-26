# Solana Ecosystem Pulse

**Generated:** 2026-10-26T02:00:57Z · **Schema:** `1.0.0` · **Collection time:** 14.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.91 | -1.41% |
| Market cap | $59.52B | rank #7 |
| Total value locked | $5.74B | -0.45% |
| Stablecoin supply | $15.88B | -0.34% |
| DEX volume (24h) | $1.35B | -5.23% |
| Chain fees / REV (24h) | $10.09M | +0.41% |
| Non-vote TPS (1h avg) | 1,938 | peak 2,631 total |
| Active validators | 665 | 25 delinquent |
| Epoch 1068 | 25.65% complete | 321,177 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 122 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,938.20 sits 4.9 sigma below the median of the last 122 runs (4,629.30, -58.1%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 25.00 sits 3.8 sigma above the median of the last 122 runs (11.00, +127.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,938.2 average over the last 60 minutes; 2,525.2 in the latest sample.
- **Total TPS:** 1,938.2 average, 2,630.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.8 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 439,514,149 at absolute slot 461,486,823.
- **Epoch 1068:** slot 110,823 of 432,000 (25.65% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.586% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 157 ms |
| `solana-rpc.publicnode.com` | yes | 136 ms |
| `api.mainnet.solana.com` | yes | 208 ms |

## Validators & stake

- **665 active** validators, **25 delinquent** (3.62% by count, 0.123% by stake).
- **Total stake:** 437,716,746 SOL ($44.17B); stake rate 68.77% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.57% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 12.91%; 229 validators at 0% and 63 at 100%.

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

- **SOL:** $100.91 (-1.41% 24h, -3.71% 7d, -17.30% 30d). Market cap $59.52B, 24h volume $1.60B (2.69% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 333 protocols - rank #4 of 421 chains, 6.45% of all tracked chain TVL. -2.22% over 7d, -55.7% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (+0.25% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.35B in 24h, $12.50B over 7d across 138 venues. Volume/TVL turnover 0.235x per day.
- **REV (chain fees):** $10.09M in 24h, $421.75M over 30d. Retained chain revenue $3.66M (36.3% of fees). Annualised fees are 6.19% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,819,794 SOL circulating of 636,457,232 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -0.8% | -2.1% |
| 2 | Kamino Lend | Lending | $1.27B | -0.0% | -3.4% |
| 3 | Raydium AMM | Dexs | $1.15B | +0.3% | -2.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.07B | -0.9% | -1.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | -0.9% | -3.6% |
| 6 | Jupiter Lend | Lending | $1.01B | -1.9% | -1.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $717.64M | -0.7% | -2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $530.55M | -1.0% | -2.7% |
| 9 | Sentora Curator | Risk Curators | $387.28M | -2.5% | -14.1% |
| 10 | Marinade Native | Staking Pool | $364.40M | -0.2% | -4.5% |
| 11 | PumpSwap | Dexs | $338.04M | -0.6% | -3.5% |
| 12 | Orca DEX | Dexs | $301.10M | -0.2% | +0.7% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 333 protocols the total is $15.42B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.5% · Dexs 15.3% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$858.50M of tokenised real-world assets and equities are locked on Solana - 5.569% of chain TVL.

- OnRe (RWA): $295.48M
- Huma (RWA): $252.00M
- Solstice (Basis Trading): $201.78M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.47M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0) | 2026-10-24 | pre-release |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-25
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-25T01:59:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,713.48 | 1,938.20 | +13.11% |
| Average non-vote TPS | 1,713.48 | 1,938.20 | +13.11% |
| Average slot time (ms) | 212.10 | 212.80 | +0.33% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 25.00 | 25.00 | +0.00% |
| Solana TVL | 5,728,335,618.00 | 5,735,902,141.00 | +0.13% |
| SOL price | 102.29 | 100.91 | -1.35% |
| Stablecoin supply | 15,931,776,002.00 | 15,877,624,594.00 | -0.34% |
| 24h DEX volume | 1,732,331,185.80 | 1,348,643,859.27 | -22.15% |
| 24h chain fees | 9,948,217.91 | 10,086,756.26 | +1.39% |

### Change over 7d (vs run at 2026-10-19T02:05:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,870.39 | 1,938.20 | -60.20% |
| Average non-vote TPS | 1,819.00 | 1,938.20 | +6.55% |
| Average slot time (ms) | 217.50 | 212.80 | -2.16% |
| Active validators | 666.00 | 665.00 | -0.15% |
| Delinquent validators | 14.00 | 25.00 | +78.57% |
| Solana TVL | 5,822,373,107.00 | 5,735,902,141.00 | -1.49% |
| SOL price | 104.90 | 100.91 | -3.80% |
| Stablecoin supply | 15,839,425,505.00 | 15,877,624,594.00 | +0.24% |
| 24h DEX volume | 1,565,959,221.38 | 1,348,643,859.27 | -13.88% |
| 24h chain fees | 9,714,592.98 | 10,086,756.26 | +3.83% |

### Change over 30d (vs run at 2026-09-25T20:48:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,794.44 | 1,938.20 | -59.57% |
| Average non-vote TPS | 2,280.07 | 1,938.20 | -14.99% |
| Average slot time (ms) | 267.80 | 212.80 | -20.54% |
| Active validators | 677.00 | 665.00 | -1.77% |
| Delinquent validators | 8.00 | 25.00 | +212.50% |
| Solana TVL | 6,627,822,265.00 | 5,735,902,141.00 | -13.46% |
| SOL price | 122.48 | 100.91 | -17.61% |
| Stablecoin supply | 17,687,473,650.00 | 15,877,624,594.00 | -10.23% |
| 24h DEX volume | 2,450,711,180.43 | 1,348,643,859.27 | -44.97% |
| 24h chain fees | 15,979,712.80 | 10,086,756.26 | -36.88% |

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
