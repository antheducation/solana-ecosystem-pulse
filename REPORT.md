# Solana Ecosystem Pulse

**Generated:** 2026-10-01T22:04:10Z · **Schema:** `1.0.0` · **Collection time:** 15.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.92 | +0.01% |
| Market cap | $69.34B | rank #7 |
| Total value locked | $6.57B | -0.01% |
| Stablecoin supply | $16.40B | -0.52% |
| DEX volume (24h) | $2.57B | +1.41% |
| Chain fees / REV (24h) | $15.98M | +8.81% |
| Non-vote TPS (1h avg) | 2,326 | peak 5,558 total |
| Active validators | 672 | 12 delinquent |
| Epoch 1047 | 26.00% complete | 319,664 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 98 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,325.7 average over the last 60 minutes; 2,269.8 in the latest sample.
- **Total TPS:** 4,821.7 average, 5,557.7 peak. Consensus votes account for 51.8% of all transactions.
- **Slot time:** 268.1 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 430,455,165 at absolute slot 452,416,336.
- **Epoch 1047:** slot 112,336 of 432,000 (26.00% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.622% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 274 ms |
| `solana-rpc.publicnode.com` | yes | 111 ms |
| `api.mainnet.solana.com` | yes | 191 ms |

## Validators & stake

- **672 active** validators, **12 delinquent** (1.75% by count, 0.020% by stake).
- **Total stake:** 440,810,473 SOL ($51.98B); stake rate 69.41% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.76% of active stake.
- **Commission:** median 5.0%, mean 12.70%; 229 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,839,408 | 4.048% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,905,145 | 3.609% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,328,203 | 2.797% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,357,265 | 2.577% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,121 | 2.543% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,267,704 | 2.103% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,246,451 | 2.098% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,601,711 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,063,975 | 1.603% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,682,305 | 1.516% | 0% |

## Economics

- **SOL:** $117.92 (+0.01% 24h, +0.95% 7d, +18.45% 30d). Market cap $69.34B, 24h volume $3.42B (4.93% of cap). Price source: `coingecko`.
- **TVL:** $6.57B across 333 protocols - rank #2 of 468 chains, 6.88% of all tracked chain TVL. +2.73% over 7d, -50.4% from its ATH.
- **Stablecoins:** $16.40B circulating on Solana (+0.94% 7d) - $2.50 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.57B in 24h, $16.91B over 7d across 126 venues. Volume/TVL turnover 0.391x per day.
- **REV (chain fees):** $15.98M in 24h, $416.09M over 30d. Retained chain revenue $5.91M (37.0% of fees). Annualised fees are 8.41% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,075,842 SOL circulating of 635,073,501 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | +0.0% | +3.4% |
| 2 | Kamino Lend | Lending | $1.39B | +0.2% | -1.2% |
| 3 | Raydium AMM | Dexs | $1.34B | +0.0% | +2.0% |
| 4 | Jupiter Lend | Lending | $1.24B | +2.7% | +6.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.23B | +0.1% | +2.9% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | +0.4% | +2.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $809.19M | +0.8% | +0.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.67M | +0.0% | +2.0% |
| 9 | Marinade Native | Staking Pool | $438.66M | -1.3% | -0.9% |
| 10 | PumpSwap | Dexs | $393.78M | +0.6% | +5.2% |
| 11 | Sentora Curator | Risk Curators | $393.17M | -1.4% | +8.5% |
| 12 | Drift Staked SOL | Liquid Staking | $332.81M | +0.0% | +2.4% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 333 protocols the total is $17.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.0% · Dexs 15.6% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.5%

### Tokenised assets

$861.06M of tokenised real-world assets and equities are locked on Solana - 4.980% of chain TVL.

- OnRe (RWA): $291.15M
- Huma (RWA): $226.88M
- Solstice (Basis Trading): $214.38M
- JupUSD (Basis Trading): $45.15M
- Plume Vaults (RWA): $32.28M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-01
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-30
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29

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

### Change over 24h (vs run at 2026-09-30T21:35:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,839.95 | 4,821.72 | -0.38% |
| Average non-vote TPS | 2,344.25 | 2,325.69 | -0.79% |
| Average slot time (ms) | 268.00 | 268.10 | +0.04% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 6,529,687,399.00 | 6,567,199,720.00 | +0.57% |
| SOL price | 117.96 | 117.92 | -0.03% |
| Stablecoin supply | 16,483,355,698.00 | 16,398,651,646.00 | -0.51% |
| 24h DEX volume | 2,534,187,471.84 | 2,569,940,125.73 | +1.41% |
| 24h chain fees | 14,686,283.17 | 15,975,862.05 | +8.78% |

### Change over 7d (vs run at 2026-09-24T20:51:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,906.54 | 4,821.72 | -1.73% |
| Average non-vote TPS | 2,393.07 | 2,325.69 | -2.82% |
| Average slot time (ms) | 267.40 | 268.10 | +0.26% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 6,484,914,945.00 | 6,567,199,720.00 | +1.27% |
| SOL price | 116.85 | 117.92 | +0.92% |
| Stablecoin supply | 16,427,048,512.00 | 16,398,651,646.00 | -0.17% |
| 24h DEX volume | 2,552,816,117.41 | 2,569,940,125.73 | +0.67% |
| 24h chain fees | 16,120,232.81 | 15,975,862.05 | -0.90% |

### Change over 30d (vs run at 2026-09-01T20:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,409.25 | 4,821.72 | +9.35% |
| Average non-vote TPS | 2,288.53 | 2,325.69 | +1.62% |
| Average slot time (ms) | 317.90 | 268.10 | -15.67% |
| Active validators | 677.00 | 672.00 | -0.74% |
| Delinquent validators | 17.00 | 12.00 | -29.41% |
| Solana TVL | 5,737,476,214.00 | 6,567,199,720.00 | +14.46% |
| SOL price | 99.96 | 117.92 | +17.97% |
| Stablecoin supply | 15,969,999,346.00 | 16,398,651,646.00 | +2.68% |
| 24h DEX volume | 2,501,465,620.05 | 2,569,940,125.73 | +2.74% |
| 24h chain fees | 13,501,461.08 | 15,975,862.05 | +18.33% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
