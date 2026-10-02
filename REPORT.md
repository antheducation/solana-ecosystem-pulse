# Solana Ecosystem Pulse

**Generated:** 2026-10-02T16:55:09Z · **Schema:** `1.0.0` · **Collection time:** 14.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.98 | +2.42% |
| Market cap | $70.57B | rank #7 |
| Total value locked | $6.70B | +2.73% |
| Stablecoin supply | $16.58B | +1.10% |
| DEX volume (24h) | $2.49B | -3.17% |
| Chain fees / REV (24h) | $17.13M | +7.25% |
| Non-vote TPS (1h avg) | 2,381 | peak 5,441 total |
| Active validators | 672 | 12 delinquent |
| Epoch 1047 | 84.74% complete | 65,904 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 99 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,381.0 average over the last 60 minutes; 2,120.7 in the latest sample.
- **Total TPS:** 4,879.9 average, 5,441.4 peak. Consensus votes account for 51.2% of all transactions.
- **Slot time:** 267.8 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 430,708,775 at absolute slot 452,670,096.
- **Epoch 1047:** slot 366,096 of 432,000 (84.74% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.622% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 123 ms |
| `solana-rpc.publicnode.com` | yes | 124 ms |
| `api.mainnet.solana.com` | yes | 113 ms |

## Validators & stake

- **672 active** validators, **12 delinquent** (1.75% by count, 0.020% by stake).
- **Total stake:** 440,810,473 SOL ($52.89B); stake rate 69.41% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.76% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 227 validators at 0% and 64 at 100%.

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

- **SOL:** $119.98 (+2.42% 24h, -0.08% 7d, +20.90% 30d). Market cap $70.57B, 24h volume $4.56B (6.46% of cap). Price source: `coingecko`.
- **TVL:** $6.70B across 334 protocols - rank #2 of 468 chains, 6.96% of all tracked chain TVL. +3.13% over 7d, -49.5% from its ATH.
- **Stablecoins:** $16.58B circulating on Solana (-5.30% 7d) - $2.47 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.49B in 24h, $16.95B over 7d across 126 venues. Volume/TVL turnover 0.371x per day.
- **REV (chain fees):** $17.13M in 24h, $422.26M over 30d. Retained chain revenue $6.20M (36.2% of fees). Annualised fees are 8.86% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,075,038 SOL circulating of 635,072,700 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +3.5% | +4.8% |
| 2 | Kamino Lend | Lending | $1.40B | +1.8% | -1.8% |
| 3 | Raydium AMM | Dexs | $1.37B | +3.5% | +3.7% |
| 4 | Jupiter Lend | Lending | $1.27B | +2.8% | +7.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.26B | +3.4% | +3.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +3.1% | +3.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $824.08M | +2.0% | +1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $627.71M | +3.4% | +3.1% |
| 9 | Marinade Native | Staking Pool | $452.20M | +3.5% | +0.2% |
| 10 | PumpSwap | Dexs | $406.59M | +3.6% | +6.5% |
| 11 | Sentora Curator | Risk Curators | $389.23M | -1.3% | +7.4% |
| 12 | Drift Staked SOL | Liquid Staking | $338.67M | +1.7% | +2.2% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.70B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.8% · Dexs 15.7% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.4%

### Tokenised assets

$868.28M of tokenised real-world assets and equities are locked on Solana - 4.905% of chain TVL.

- OnRe (RWA): $291.30M
- Huma (RWA): $231.54M
- Solstice (Basis Trading): $212.62M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.36M

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

### Change over 24h (vs run at 2026-10-01T17:43:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,216.34 | 4,879.88 | -6.45% |
| Average non-vote TPS | 2,718.82 | 2,381.02 | -12.42% |
| Average slot time (ms) | 267.80 | 267.80 | +0.00% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 6,537,090,216.00 | 6,698,957,933.00 | +2.48% |
| SOL price | 118.55 | 119.98 | +1.21% |
| Stablecoin supply | 16,399,435,798.00 | 16,579,751,140.00 | +1.10% |
| 24h DEX volume | 2,569,940,125.73 | 2,488,460,102.88 | -3.17% |
| 24h chain fees | 15,975,862.05 | 17,134,431.63 | +7.25% |

### Change over 7d (vs run at 2026-09-25T16:01:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,941.47 | 4,879.88 | -1.25% |
| Average non-vote TPS | 2,435.17 | 2,381.02 | -2.22% |
| Average slot time (ms) | 268.30 | 267.80 | -0.19% |
| Active validators | 675.00 | 672.00 | -0.44% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 6,543,782,193.00 | 6,698,957,933.00 | +2.37% |
| SOL price | 119.95 | 119.98 | +0.03% |
| Stablecoin supply | 17,687,227,712.00 | 16,579,751,140.00 | -6.26% |
| 24h DEX volume | 2,450,711,180.43 | 2,488,460,102.88 | +1.54% |
| 24h chain fees | 15,979,712.80 | 17,134,431.63 | +7.23% |

### Change over 30d (vs run at 2026-09-02T20:11:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,022.99 | 4,879.88 | +21.30% |
| Average non-vote TPS | 1,883.92 | 2,381.02 | +26.39% |
| Average slot time (ms) | 314.50 | 267.80 | -14.85% |
| Active validators | 677.00 | 672.00 | -0.74% |
| Delinquent validators | 18.00 | 12.00 | -33.33% |
| Solana TVL | 5,665,576,869.00 | 6,698,957,933.00 | +18.24% |
| SOL price | 99.75 | 119.98 | +20.28% |
| Stablecoin supply | 15,850,870,070.00 | 16,579,751,140.00 | +4.60% |
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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
