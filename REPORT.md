# Solana Ecosystem Pulse

**Generated:** 2026-10-02T21:29:53Z · **Schema:** `1.0.0` · **Collection time:** 21.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.81 | -0.04% |
| Market cap | $69.28B | rank #7 |
| Total value locked | $6.61B | +1.44% |
| Stablecoin supply | $16.58B | +1.10% |
| DEX volume (24h) | $2.49B | -3.17% |
| Chain fees / REV (24h) | $17.13M | +7.25% |
| Non-vote TPS (1h avg) | 2,433 | peak 5,271 total |
| Active validators | 671 | 13 delinquent |
| Epoch 1047 | 98.95% complete | 4,535 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 99 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,432.9 average over the last 60 minutes; 1,853.2 in the latest sample.
- **Total TPS:** 4,922.8 average, 5,271.0 peak. Consensus votes account for 50.6% of all transactions.
- **Slot time:** 268.5 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 430,770,097 at absolute slot 452,731,465.
- **Epoch 1047:** slot 427,465 of 432,000 (98.95% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.622% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 271 ms |
| `solana-rpc.publicnode.com` | yes | 167 ms |
| `api.mainnet.solana.com` | yes | 318 ms |

## Validators & stake

- **671 active** validators, **13 delinquent** (1.90% by count, 0.035% by stake).
- **Total stake:** 440,810,473 SOL ($51.93B); stake rate 69.41% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.76% of active stake.
- **Commission:** median 5.0%, mean 13.02%; 226 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,839,408 | 4.048% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,905,145 | 3.609% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,328,203 | 2.798% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,357,265 | 2.577% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,121 | 2.544% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,267,704 | 2.103% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,246,451 | 2.098% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,601,711 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,063,975 | 1.603% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,682,305 | 1.516% | 0% |

## Economics

- **SOL:** $117.81 (-0.04% 24h, -3.09% 7d, +18.18% 30d). Market cap $69.28B, 24h volume $4.76B (6.87% of cap). Price source: `coingecko`.
- **TVL:** $6.61B across 334 protocols - rank #2 of 468 chains, 6.95% of all tracked chain TVL. +1.84% over 7d, -50.1% from its ATH.
- **Stablecoins:** $16.58B circulating on Solana (-5.30% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.49B in 24h, $16.95B over 7d across 126 venues. Volume/TVL turnover 0.377x per day.
- **REV (chain fees):** $17.13M in 24h, $422.26M over 30d. Retained chain revenue $6.20M (36.2% of fees). Annualised fees are 9.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,074,821 SOL circulating of 635,072,483 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.93B | +0.2% | +1.6% |
| 2 | Kamino Lend | Lending | $1.38B | -0.6% | -3.1% |
| 3 | Raydium AMM | Dexs | $1.36B | +1.5% | +2.4% |
| 4 | Jupiter Lend | Lending | $1.27B | +2.3% | +7.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.23B | -0.2% | +0.7% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | -0.6% | +0.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $803.01M | -0.8% | -1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $607.61M | -0.2% | -0.2% |
| 9 | Marinade Native | Staking Pool | $437.42M | -0.3% | -3.1% |
| 10 | PumpSwap | Dexs | $397.15M | +0.8% | +4.0% |
| 11 | Sentora Curator | Risk Curators | $387.92M | -1.3% | +7.0% |
| 12 | Drift Staked SOL | Liquid Staking | $332.05M | -0.2% | +0.2% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.38B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 17.0% · Dexs 15.7% · Derivatives 5.0% · Staking Pool 3.9% · Risk Curators 3.5%

### Tokenised assets

$897.36M of tokenised real-world assets and equities are locked on Solana - 5.163% of chain TVL.

- OnRe (RWA): $291.34M
- Huma (RWA): $260.62M
- Solstice (Basis Trading): $212.61M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.37M

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

- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [Bump linkify-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/682) - updated 2026-10-02
- [Bump uuid and @actions/core](https://github.com/solana-foundation/solana-improvement-documents/pull/681) - updated 2026-10-02
- [Bump js-yaml from 4.1.0 to 4.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/680) - updated 2026-10-02
- [Bump picomatch from 2.3.1 to 2.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/679) - updated 2026-10-02
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-01
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01

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

### Change over 24h (vs run at 2026-10-01T22:04:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,821.72 | 4,922.79 | +2.10% |
| Average non-vote TPS | 2,325.69 | 2,432.94 | +4.61% |
| Average slot time (ms) | 268.10 | 268.50 | +0.15% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 6,567,199,720.00 | 6,606,723,520.00 | +0.60% |
| SOL price | 117.92 | 117.81 | -0.09% |
| Stablecoin supply | 16,398,651,646.00 | 16,579,831,390.00 | +1.10% |
| 24h DEX volume | 2,569,940,125.73 | 2,488,460,102.88 | -3.17% |
| 24h chain fees | 15,975,862.05 | 17,134,431.63 | +7.25% |

### Change over 7d (vs run at 2026-09-25T20:48:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,794.44 | 4,922.79 | +2.68% |
| Average non-vote TPS | 2,280.07 | 2,432.94 | +6.70% |
| Average slot time (ms) | 267.80 | 268.50 | +0.26% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 8.00 | 13.00 | +62.50% |
| Solana TVL | 6,627,822,265.00 | 6,606,723,520.00 | -0.32% |
| SOL price | 122.48 | 117.81 | -3.81% |
| Stablecoin supply | 17,687,473,650.00 | 16,579,831,390.00 | -6.26% |
| 24h DEX volume | 2,450,711,180.43 | 2,488,460,102.88 | +1.54% |
| 24h chain fees | 15,979,712.80 | 17,134,431.63 | +7.23% |

### Change over 30d (vs run at 2026-09-02T20:11:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,022.99 | 4,922.79 | +22.37% |
| Average non-vote TPS | 1,883.92 | 2,432.94 | +29.14% |
| Average slot time (ms) | 314.50 | 268.50 | -14.63% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,665,576,869.00 | 6,606,723,520.00 | +16.61% |
| SOL price | 99.75 | 117.81 | +18.11% |
| Stablecoin supply | 15,850,870,070.00 | 16,579,831,390.00 | +4.60% |
| 24h DEX volume | 2,171,560,050.49 | 2,488,460,102.88 | +14.59% |
| 24h chain fees | 12,646,787.67 | 17,134,431.63 | +35.48% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 21.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
