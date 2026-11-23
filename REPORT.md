# Solana Ecosystem Pulse

**Generated:** 2026-11-23T04:22:19Z · **Schema:** `1.0.0` · **Collection time:** 25.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.26 | +2.66% |
| Market cap | $42.18B | rank #7 |
| Total value locked | $4.63B | +0.26% |
| Stablecoin supply | $13.41B | +0.31% |
| DEX volume (24h) | $1.19B | -11.85% |
| Chain fees / REV (24h) | $6.01M | -20.49% |
| Non-vote TPS (1h avg) | 1,593 | peak 2,712 total |
| Active validators | 662 | 23 delinquent |
| Epoch 1094 | 46.05% complete | 233,052 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 134 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,406,423,988.00 sits 3.1 sigma below the median of the last 134 runs (15,973,982,918.00, -16.1%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,592.6 average over the last 60 minutes; 1,346.1 in the latest sample.
- **Total TPS:** 1,592.6 average, 2,712.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 450,820,528 at absolute slot 472,806,948.
- **Epoch 1094:** slot 198,948 of 432,000 (46.05% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.544% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 213 ms |
| `solana-rpc.publicnode.com` | yes | 107 ms |
| `api.mainnet.solana.com` | yes | 159 ms |

## Validators & stake

- **662 active** validators, **23 delinquent** (3.36% by count, 0.012% by stake).
- **Total stake:** 425,691,542 SOL ($30.33B); stake rate 66.72% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.00% and top 33 hold 46.65% of active stake.
- **Commission:** median 5.0%, mean 12.89%; 220 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,918,440 | 3.975% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,346,959 | 3.841% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,401,889 | 2.914% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,243,005 | 2.406% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,842,253 | 2.312% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,612,896 | 2.258% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,269,555 | 2.178% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,998,895 | 1.879% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,495 | 1.642% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,775,083 | 1.592% | 5% |

## Economics

- **SOL:** $71.26 (+2.66% 24h, -1.19% 7d, -30.50% 30d). Market cap $42.18B, 24h volume $1.91B (4.52% of cap). Price source: `coingecko`.
- **TVL:** $4.63B across 344 protocols - rank #3 of 426 chains, 6.70% of all tracked chain TVL. -1.51% over 7d, -61.1% from its ATH.
- **Stablecoins:** $13.41B circulating on Solana (-6.52% 7d) - $2.89 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.19B in 24h, $10.37B over 7d across 144 venues. Volume/TVL turnover 0.256x per day.
- **REV (chain fees):** $6.01M in 24h, $284.30M over 30d. Retained chain revenue $2.12M (35.3% of fees). Annualised fees are 5.20% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,016,789 SOL circulating of 638,042,390 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.30B | +1.4% | -3.4% |
| 2 | Kamino Lend | Lending | $1.14B | +0.3% | +0.4% |
| 3 | Jupiter Lend | Lending | $954.99M | +0.8% | +3.1% |
| 4 | Raydium AMM | Dexs | $784.70M | +0.6% | -5.7% |
| 5 | Binance Staked SOL | Liquid Staking | $721.83M | +1.2% | -4.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $707.35M | +0.9% | -2.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $568.32M | +1.1% | -1.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $363.82M | +2.1% | -2.5% |
| 9 | Sentora Curator | Risk Curators | $353.47M | -0.8% | -1.3% |
| 10 | OnRe | RWA | $287.55M | +0.0% | -4.9% |
| 11 | Forward Industries SOL | Liquid Staking | $276.10M | +1.3% | -5.2% |
| 12 | CCIP | Bridge | $266.92M | -0.1% | -4.1% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 344 protocols the total is $11.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.3% · Dexs 14.6% · Derivatives 5.3% · RWA 4.4% · Risk Curators 4.2%

### Tokenised assets

$777.39M of tokenised real-world assets and equities are locked on Solana - 6.610% of chain TVL.

- OnRe (RWA): $287.55M
- Huma (RWA): $225.89M
- Solstice (Basis Trading): $200.98M
- JupUSD (Basis Trading): $39.45M
- Solomon USDv (Basis Trading): $8.73M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19

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

### Change over 24h (vs run at 2026-11-22T03:45:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,378.16 | 1,592.63 | +15.56% |
| Average non-vote TPS | 1,378.16 | 1,592.63 | +15.56% |
| Average slot time (ms) | 215.60 | 215.20 | -0.19% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 24.00 | 23.00 | -4.17% |
| Solana TVL | 4,619,778,328.00 | 4,633,186,578.00 | +0.29% |
| SOL price | 69.24 | 71.26 | +2.92% |
| Stablecoin supply | 13,364,640,996.00 | 13,406,423,988.00 | +0.31% |
| 24h DEX volume | 1,560,546,106.87 | 1,186,396,653.97 | -23.98% |
| 24h chain fees | 7,893,685.33 | 6,008,758.23 | -23.88% |

### Change over 7d (vs run at 2026-11-16T03:28:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,633.48 | 1,592.63 | -2.50% |
| Average non-vote TPS | 1,633.48 | 1,592.63 | -2.50% |
| Average slot time (ms) | 214.30 | 215.20 | +0.42% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 38.00 | 23.00 | -39.47% |
| Solana TVL | 4,706,399,962.00 | 4,633,186,578.00 | -1.56% |
| SOL price | 72.23 | 71.26 | -1.34% |
| Stablecoin supply | 14,340,765,034.00 | 13,406,423,988.00 | -6.52% |
| 24h DEX volume | 1,543,698,435.09 | 1,186,396,653.97 | -23.15% |
| 24h chain fees | 7,303,225.20 | 6,008,758.23 | -17.72% |

### Change over 30d (vs run at 2026-10-23T20:43:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,163.30 | 1,592.63 | -26.38% |
| Average non-vote TPS | 2,163.30 | 1,592.63 | -26.38% |
| Average slot time (ms) | 212.20 | 215.20 | +1.41% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 14.00 | 23.00 | +64.29% |
| Solana TVL | 5,856,286,188.00 | 4,633,186,578.00 | -20.89% |
| SOL price | 103.58 | 71.26 | -31.20% |
| Stablecoin supply | 15,965,866,149.00 | 13,406,423,988.00 | -16.03% |
| 24h DEX volume | 2,039,384,832.23 | 1,186,396,653.97 | -41.83% |
| 24h chain fees | 11,472,475.22 | 6,008,758.23 | -47.62% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 25.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
