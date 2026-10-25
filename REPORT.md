# Solana Ecosystem Pulse

**Generated:** 2026-10-25T01:59:22Z · **Schema:** `1.0.0` · **Collection time:** 17.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.29 | -0.24% |
| Market cap | $60.33B | rank #7 |
| Total value locked | $5.73B | +0.00% |
| Stablecoin supply | $15.93B | +0.05% |
| DEX volume (24h) | $1.73B | -13.26% |
| Chain fees / REV (24h) | $9.95M | -5.72% |
| Non-vote TPS (1h avg) | 1,713 | peak 2,420 total |
| Active validators | 665 | 25 delinquent |
| Epoch 1067 | 31.41% complete | 296,316 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 121 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,713.48 sits 5.5 sigma below the median of the last 121 runs (4,653.97, -63.2%). | `zscore` |
| [SERIOUS] | Delinquent validators is above its recent norm | Current 25.00 sits 5.1 sigma above the median of the last 121 runs (10.00, +150.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,713.5 average over the last 60 minutes; 1,268.1 in the latest sample.
- **Total TPS:** 1,713.5 average, 2,419.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.1 ms average (target 400 ms), worst 1-minute bucket 216.6 ms.
- **Block height:** 439,108,678 at absolute slot 461,079,684.
- **Epoch 1067:** slot 135,684 of 432,000 (31.41% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.587% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 210 ms |
| `solana-rpc.publicnode.com` | yes | 146 ms |
| `api.mainnet.solana.com` | yes | 146 ms |

## Validators & stake

- **665 active** validators, **25 delinquent** (3.62% by count, 0.049% by stake).
- **Total stake:** 437,191,006 SOL ($44.72B); stake rate 68.70% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 46.04% of active stake.
- **Commission:** median 5.0%, mean 12.91%; 228 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,099,113 | 3.913% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,646,121 | 3.809% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,588,035 | 2.881% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,881,430 | 2.490% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,721,918 | 2.225% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,483,244 | 2.170% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,837 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,036 | 1.782% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,038,249 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,006,653 | 1.603% | 0% |

## Economics

- **SOL:** $102.29 (-0.24% 24h, -1.02% 7d, -12.86% 30d). Market cap $60.33B, 24h volume $2.33B (3.86% of cap). Price source: `coingecko`.
- **TVL:** $5.73B across 332 protocols - rank #4 of 421 chains, 6.43% of all tracked chain TVL. -3.31% over 7d, -55.8% from its ATH.
- **Stablecoins:** $15.93B circulating on Solana (+0.22% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.73B in 24h, $12.96B over 7d across 138 venues. Volume/TVL turnover 0.302x per day.
- **REV (chain fees):** $9.95M in 24h, $433.36M over 30d. Retained chain revenue $3.59M (36.1% of fees). Annualised fees are 6.02% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,764,336 SOL circulating of 636,396,092 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +0.2% | -0.5% |
| 2 | Kamino Lend | Lending | $1.25B | -1.8% | -4.5% |
| 3 | Raydium AMM | Dexs | $1.15B | -2.4% | -1.9% |
| 4 | Binance Staked SOL | Liquid Staking | $1.07B | -1.7% | -1.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.07B | +0.4% | -1.9% |
| 6 | Jupiter Lend | Lending | $993.40M | -2.8% | -8.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $719.39M | -0.5% | -2.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $532.39M | -1.1% | -1.3% |
| 9 | Sentora Curator | Risk Curators | $397.09M | -0.0% | -12.1% |
| 10 | Marinade Native | Staking Pool | $365.00M | -1.2% | -3.3% |
| 11 | PumpSwap | Dexs | $340.08M | +0.3% | -2.5% |
| 12 | Orca DEX | Dexs | $301.75M | -1.2% | +1.1% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.3% · Dexs 15.3% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.8%

### Tokenised assets

$859.52M of tokenised real-world assets and equities are locked on Solana - 5.565% of chain TVL.

- OnRe (RWA): $295.37M
- Huma (RWA): $252.75M
- Solstice (Basis Trading): $201.87M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.46M

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

- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-24
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

### Change over 24h (vs run at 2026-10-24T02:13:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,753.27 | 1,713.48 | -2.27% |
| Average non-vote TPS | 1,753.27 | 1,713.48 | -2.27% |
| Average slot time (ms) | 212.00 | 212.10 | +0.05% |
| Active validators | 664.00 | 665.00 | +0.15% |
| Delinquent validators | 14.00 | 25.00 | +78.57% |
| Solana TVL | 5,818,515,359.00 | 5,728,335,618.00 | -1.55% |
| SOL price | 102.56 | 102.29 | -0.26% |
| Stablecoin supply | 15,925,064,319.00 | 15,931,776,002.00 | +0.04% |
| 24h DEX volume | 2,021,288,711.44 | 1,732,331,185.80 | -14.30% |
| 24h chain fees | 10,537,655.05 | 9,948,217.91 | -5.59% |

### Change over 7d (vs run at 2026-10-18T01:48:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,812.84 | 1,713.48 | -64.40% |
| Average non-vote TPS | 1,736.06 | 1,713.48 | -1.30% |
| Average slot time (ms) | 216.70 | 212.10 | -2.12% |
| Active validators | 669.00 | 665.00 | -0.60% |
| Delinquent validators | 12.00 | 25.00 | +108.33% |
| Solana TVL | 5,882,315,364.00 | 5,728,335,618.00 | -2.62% |
| SOL price | 104.05 | 102.29 | -1.69% |
| Stablecoin supply | 15,897,345,176.00 | 15,931,776,002.00 | +0.22% |
| 24h DEX volume | 1,514,642,363.55 | 1,732,331,185.80 | +14.37% |
| 24h chain fees | 9,315,995.67 | 9,948,217.91 | +6.79% |

### Change over 30d (vs run at 2026-09-24T20:51:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,906.54 | 1,713.48 | -65.08% |
| Average non-vote TPS | 2,393.07 | 1,713.48 | -28.40% |
| Average slot time (ms) | 267.40 | 212.10 | -20.68% |
| Active validators | 676.00 | 665.00 | -1.63% |
| Delinquent validators | 10.00 | 25.00 | +150.00% |
| Solana TVL | 6,484,914,945.00 | 5,728,335,618.00 | -11.67% |
| SOL price | 116.85 | 102.29 | -12.46% |
| Stablecoin supply | 16,427,048,512.00 | 15,931,776,002.00 | -3.01% |
| 24h DEX volume | 2,552,816,117.41 | 1,732,331,185.80 | -32.14% |
| 24h chain fees | 16,120,232.81 | 9,948,217.91 | -38.29% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
