# Solana Ecosystem Pulse

**Generated:** 2026-09-30T17:05:55Z · **Schema:** `1.0.0` · **Collection time:** 15.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.26 | +1.81% |
| Market cap | $70.71B | rank #7 |
| Total value locked | $6.57B | +1.73% |
| Stablecoin supply | $16.48B | -1.08% |
| DEX volume (24h) | $2.53B | -4.80% |
| Chain fees / REV (24h) | $14.69M | -15.09% |
| Non-vote TPS (1h avg) | 2,215 | peak 5,379 total |
| Active validators | 671 | 12 delinquent |
| Epoch 1046 | 35.83% complete | 277,231 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 97 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,215.0 average over the last 60 minutes; 2,800.2 in the latest sample.
- **Total TPS:** 4,708.1 average, 5,379.2 peak. Consensus votes account for 53.0% of all transactions.
- **Slot time:** 267.6 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 430,066,049 at absolute slot 452,026,769.
- **Epoch 1046:** slot 154,769 of 432,000 (35.83% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.624% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 198 ms |
| `solana-rpc.publicnode.com` | yes | 168 ms |
| `api.mainnet.solana.com` | yes | 217 ms |

## Validators & stake

- **671 active** validators, **12 delinquent** (1.76% by count, 0.126% by stake).
- **Total stake:** 440,549,645 SOL ($52.98B); stake rate 69.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.50% and top 33 hold 45.61% of active stake.
- **Commission:** median 5.0%, mean 12.72%; 228 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,227,376 | 3.915% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,893,945 | 3.612% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,668 | 2.802% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,384,141 | 2.587% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,206,135 | 2.547% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,721 | 2.104% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,232,740 | 2.098% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,652,675 | 1.739% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,092,577 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,513,562 | 1.480% | 0% |

## Economics

- **SOL:** $120.26 (+1.81% 24h, +5.13% 7d, +16.95% 30d). Market cap $70.71B, 24h volume $4.02B (5.69% of cap). Price source: `coingecko`.
- **TVL:** $6.57B across 331 protocols - rank #2 of 467 chains, 6.90% of all tracked chain TVL. +0.52% over 7d, -50.4% from its ATH.
- **Stablecoins:** $16.48B circulating on Solana (-1.33% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.53B in 24h, $16.89B over 7d across 126 venues. Volume/TVL turnover 0.386x per day.
- **REV (chain fees):** $14.69M in 24h, $412.19M over 30d. Retained chain revenue $5.94M (40.5% of fees). Annualised fees are 7.58% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,005,667 SOL circulating of 634,996,044 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.93B | +0.3% | +2.3% |
| 2 | Kamino Lend | Lending | $1.42B | +3.2% | -0.8% |
| 3 | Raydium AMM | Dexs | $1.34B | +0.5% | -0.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | +0.3% | +0.4% |
| 5 | Jupiter Lend | Lending | $1.22B | +0.3% | +2.5% |
| 6 | Binance Staked SOL | Liquid Staking | $1.22B | -1.5% | +0.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $803.46M | -0.3% | -2.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.24M | +0.5% | +0.0% |
| 9 | Marinade Native | Staking Pool | $447.51M | -3.9% | -1.2% |
| 10 | PumpSwap | Dexs | $396.03M | +0.7% | +3.7% |
| 11 | Sentora Curator | Risk Curators | $348.89M | -0.5% | -3.9% |
| 12 | Drift Staked SOL | Liquid Staking | $335.12M | -1.6% | +0.3% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.98B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.3% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.0% · Risk Curators 3.2%

### Tokenised assets

$835.26M of tokenised real-world assets and equities are locked on Solana - 4.918% of chain TVL.

- OnRe (RWA): $292.51M
- Solstice (Basis Trading): $214.73M
- Huma (RWA): $206.02M
- JupUSD (Basis Trading): $45.16M
- Plume Vaults (RWA): $25.67M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-30
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-09-30
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28

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

### Change over 24h (vs run at 2026-09-29T17:08:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,925.90 | 4,708.15 | -4.42% |
| Average non-vote TPS | 2,434.54 | 2,215.04 | -9.02% |
| Average slot time (ms) | 268.60 | 267.60 | -0.37% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 6,578,087,634.00 | 6,572,150,522.00 | -0.09% |
| SOL price | 118.18 | 120.26 | +1.76% |
| Stablecoin supply | 16,662,773,223.00 | 16,478,505,496.00 | -1.11% |
| 24h DEX volume | 2,662,061,803.25 | 2,534,187,471.84 | -4.80% |
| 24h chain fees | 17,514,749.35 | 14,686,283.17 | -16.15% |

### Change over 7d (vs run at 2026-09-23T15:39:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,849.84 | 4,708.15 | -2.92% |
| Average non-vote TPS | 2,345.00 | 2,215.04 | -5.54% |
| Average slot time (ms) | 267.40 | 267.60 | +0.07% |
| Active validators | 674.00 | 671.00 | -0.45% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 6,436,874,885.00 | 6,572,150,522.00 | +2.10% |
| SOL price | 114.88 | 120.26 | +4.68% |
| Stablecoin supply | 16,879,859,425.00 | 16,478,505,496.00 | -2.38% |
| 24h DEX volume | 3,195,015,036.76 | 2,534,187,471.84 | -20.68% |
| 24h chain fees | 17,874,880.76 | 14,686,283.17 | -17.84% |

### Change over 30d (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 4,708.15 | +8.77% |
| Average non-vote TPS | 2,195.90 | 2,215.04 | +0.87% |
| Average slot time (ms) | 317.20 | 267.60 | -15.64% |
| Active validators | 681.00 | 671.00 | -1.47% |
| Delinquent validators | 16.00 | 12.00 | -25.00% |
| Solana TVL | 5,791,254,029.00 | 6,572,150,522.00 | +13.48% |
| SOL price | 104.61 | 120.26 | +14.96% |
| Stablecoin supply | 16,123,089,134.00 | 16,478,505,496.00 | +2.20% |
| 24h DEX volume | 1,929,632,644.74 | 2,534,187,471.84 | +31.33% |
| 24h chain fees | 12,307,328.44 | 14,686,283.17 | +19.33% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
