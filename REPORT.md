# Solana Ecosystem Pulse

**Generated:** 2026-10-01T11:56:13Z · **Schema:** `1.0.0` · **Collection time:** 14.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.94 | -1.22% |
| Market cap | $69.35B | rank #7 |
| Total value locked | $6.52B | -0.75% |
| Stablecoin supply | $16.40B | -0.51% |
| DEX volume (24h) | $2.57B | +1.41% |
| Chain fees / REV (24h) | $15.88M | +8.14% |
| Non-vote TPS (1h avg) | 1,401 | peak 4,303 total |
| Active validators | 672 | 11 delinquent |
| Epoch 1046 | 94.55% complete | 23,544 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 98 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,400.8 average over the last 60 minutes; 1,404.4 in the latest sample.
- **Total TPS:** 3,905.7 average, 4,303.5 peak. Consensus votes account for 64.1% of all transactions.
- **Slot time:** 267.1 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 430,319,433 at absolute slot 452,280,456.
- **Epoch 1046:** slot 408,456 of 432,000 (94.55% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.624% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 186 ms |
| `solana-rpc.publicnode.com` | yes | 108 ms |
| `api.mainnet.solana.com` | yes | 172 ms |

## Validators & stake

- **672 active** validators, **11 delinquent** (1.61% by count, 0.051% by stake).
- **Total stake:** 440,549,645 SOL ($51.96B); stake rate 69.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.57% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 227 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,227,376 | 3.912% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,893,945 | 3.610% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,668 | 2.800% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,384,141 | 2.585% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,206,135 | 2.545% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,721 | 2.102% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,232,740 | 2.097% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,652,675 | 1.738% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,092,577 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,513,562 | 1.479% | 0% |

## Economics

- **SOL:** $117.94 (-1.22% 24h, +4.01% 7d, +15.23% 30d). Market cap $69.35B, 24h volume $4.22B (6.08% of cap). Price source: `coingecko`.
- **TVL:** $6.52B across 334 protocols - rank #2 of 468 chains, 6.87% of all tracked chain TVL. +1.98% over 7d, -50.7% from its ATH.
- **Stablecoins:** $16.40B circulating on Solana (+0.94% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.57B in 24h, $16.91B over 7d across 126 venues. Volume/TVL turnover 0.394x per day.
- **REV (chain fees):** $15.88M in 24h, $415.99M over 30d. Retained chain revenue $5.91M (37.2% of fees). Annualised fees are 8.36% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,004,903 SOL circulating of 634,995,262 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.91B | -1.6% | +2.9% |
| 2 | Kamino Lend | Lending | $1.38B | -0.1% | -1.9% |
| 3 | Raydium AMM | Dexs | $1.33B | -1.2% | +1.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.22B | -1.6% | +2.4% |
| 5 | Jupiter Lend | Lending | $1.22B | +0.0% | +4.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.20B | -1.7% | +1.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $805.17M | +0.1% | +0.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $606.12M | -1.7% | +1.5% |
| 9 | Marinade Native | Staking Pool | $442.65M | -1.6% | -0.0% |
| 10 | Sentora Curator | Risk Curators | $394.68M | +12.9% | +8.9% |
| 11 | PumpSwap | Dexs | $389.65M | -0.9% | +4.1% |
| 12 | Drift Staked SOL | Liquid Staking | $331.38M | -1.7% | +2.0% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.18B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.9% · Dexs 15.7% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.5%

### Tokenised assets

$835.18M of tokenised real-world assets and equities are locked on Solana - 4.861% of chain TVL.

- OnRe (RWA): $290.94M
- Solstice (Basis Trading): $214.36M
- Huma (RWA): $207.53M
- JupUSD (Basis Trading): $45.15M
- Plume Vaults (RWA): $26.11M

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

- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-01
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-30
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29

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

### Change over 24h (vs run at 2026-09-30T11:28:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,060.70 | 3,905.71 | -3.82% |
| Average non-vote TPS | 1,550.42 | 1,400.79 | -9.65% |
| Average slot time (ms) | 267.10 | 267.10 | +0.00% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 6,505,973,320.00 | 6,520,822,206.00 | +0.23% |
| SOL price | 119.51 | 117.94 | -1.31% |
| Stablecoin supply | 16,480,011,986.00 | 16,398,738,087.00 | -0.49% |
| 24h DEX volume | 2,534,247,588.84 | 2,569,940,125.73 | +1.41% |
| 24h chain fees | 14,744,507.17 | 15,876,757.05 | +7.68% |

### Change over 7d (vs run at 2026-09-24T10:37:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,214.44 | 3,905.71 | -7.33% |
| Average non-vote TPS | 1,675.25 | 1,400.79 | -16.38% |
| Average slot time (ms) | 265.00 | 267.10 | +0.79% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 6,355,143,831.00 | 6,520,822,206.00 | +2.61% |
| SOL price | 112.79 | 117.94 | +4.57% |
| Stablecoin supply | 16,426,393,329.00 | 16,398,738,087.00 | -0.17% |
| 24h DEX volume | 2,682,822,618.41 | 2,569,940,125.73 | -4.21% |
| 24h chain fees | 16,503,822.03 | 15,876,757.05 | -3.80% |

### Change over 30d (vs run at 2026-09-01T20:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,409.25 | 3,905.71 | -11.42% |
| Average non-vote TPS | 2,288.53 | 1,400.79 | -38.79% |
| Average slot time (ms) | 317.90 | 267.10 | -15.98% |
| Active validators | 677.00 | 672.00 | -0.74% |
| Delinquent validators | 17.00 | 11.00 | -35.29% |
| Solana TVL | 5,737,476,214.00 | 6,520,822,206.00 | +13.65% |
| SOL price | 99.96 | 117.94 | +17.99% |
| Stablecoin supply | 15,969,999,346.00 | 16,398,738,087.00 | +2.68% |
| 24h DEX volume | 2,501,465,620.05 | 2,569,940,125.73 | +2.74% |
| 24h chain fees | 13,501,461.08 | 15,876,757.05 | +17.59% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
