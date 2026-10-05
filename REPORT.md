# Solana Ecosystem Pulse

**Generated:** 2026-10-05T02:39:57Z · **Schema:** `1.0.0` · **Collection time:** 22.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $121.39 | +1.11% |
| Market cap | $71.36B | rank #7 |
| Total value locked | $6.74B | +1.56% |
| Stablecoin supply | $16.89B | +0.02% |
| DEX volume (24h) | $1.65B | +6.13% |
| Chain fees / REV (24h) | $15.45M | +19.46% |
| Non-vote TPS (1h avg) | 1,848 | peak 5,164 total |
| Active validators | 671 | 15 delinquent |
| Epoch 1049 | 64.58% complete | 153,014 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,847.5 average over the last 60 minutes; 1,915.0 in the latest sample.
- **Total TPS:** 4,345.8 average, 5,164.3 peak. Consensus votes account for 57.5% of all transactions.
- **Slot time:** 267.5 ms average (target 400 ms), worst 1-minute bucket 283.0 ms.
- **Block height:** 431,485,304 at absolute slot 453,446,986.
- **Epoch 1049:** slot 278,986 of 432,000 (64.58% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.618% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 311 ms |
| `solana-rpc.publicnode.com` | yes | 148 ms |
| `api.mainnet.solana.com` | yes | 204 ms |

## Validators & stake

- **671 active** validators, **15 delinquent** (2.19% by count, 0.027% by stake).
- **Total stake:** 441,848,823 SOL ($53.64B); stake rate 69.56% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.57% and top 33 hold 45.65% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,935,562 | 4.060% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,927,649 | 3.606% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,346,574 | 2.795% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,305,935 | 2.559% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,136,537 | 2.521% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,655 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,241,331 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,616,097 | 1.724% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,061,519 | 1.599% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,686,111 | 1.514% | 0% |

## Economics

- **SOL:** $121.39 (+1.11% 24h, +0.57% 7d, +19.15% 30d). Market cap $71.36B, 24h volume $2.20B (3.08% of cap). Price source: `coingecko`.
- **TVL:** $6.74B across 334 protocols - rank #2 of 468 chains, 6.96% of all tracked chain TVL. +1.57% over 7d, -49.1% from its ATH.
- **Stablecoins:** $16.89B circulating on Solana (+0.97% 7d) - $2.50 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.65B in 24h, $15.58B over 7d across 126 venues. Volume/TVL turnover 0.245x per day.
- **REV (chain fees):** $15.45M in 24h, $434.73M over 30d. Retained chain revenue $5.69M (36.8% of fees). Annualised fees are 7.90% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,314,144 SOL circulating of 635,227,608 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +1.1% | +0.6% |
| 2 | Kamino Lend | Lending | $1.40B | +1.0% | -5.1% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.8% | +0.9% |
| 4 | Jupiter Lend | Lending | $1.33B | +1.7% | +11.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.27B | +1.1% | +0.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +1.3% | +0.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $822.24M | +1.3% | -0.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $628.17M | +1.3% | -0.1% |
| 9 | Marinade Native | Staking Pool | $451.61M | +1.2% | -3.6% |
| 10 | PumpSwap | Dexs | $407.92M | +2.0% | +2.8% |
| 11 | Sentora Curator | Risk Curators | $380.16M | +1.4% | +4.7% |
| 12 | Drift Staked SOL | Liquid Staking | $342.85M | +1.2% | +0.0% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.81B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.9% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$895.78M of tokenised real-world assets and equities are locked on Solana - 5.029% of chain TVL.

- OnRe (RWA): $291.76M
- Huma (RWA): $259.15M
- Solstice (Basis Trading): $212.12M
- JupUSD (Basis Trading): $49.05M
- Plume Vaults (RWA): $32.43M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-05
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-04
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-04
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-10-03
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [Bump linkify-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/682) - updated 2026-10-02

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

### Change over 24h (vs run at 2026-10-04T03:07:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,226.99 | 4,345.78 | +2.81% |
| Average non-vote TPS | 1,721.51 | 1,847.54 | +7.32% |
| Average slot time (ms) | 266.60 | 267.50 | +0.34% |
| Active validators | 671.00 | 671.00 | +0.00% |
| Delinquent validators | 14.00 | 15.00 | +7.14% |
| Solana TVL | 6,668,023,483.00 | 6,743,140,234.00 | +1.13% |
| SOL price | 120.36 | 121.39 | +0.86% |
| Stablecoin supply | 16,880,130,771.00 | 16,885,469,670.00 | +0.03% |
| 24h DEX volume | 2,132,195,295.11 | 1,649,284,605.63 | -22.65% |
| 24h chain fees | 12,977,249.54 | 15,446,766.41 | +19.03% |

### Change over 7d (vs run at 2026-09-28T02:14:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,971.25 | 4,345.78 | -12.58% |
| Average non-vote TPS | 2,474.04 | 1,847.54 | -25.32% |
| Average slot time (ms) | 269.20 | 267.50 | -0.63% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 8.00 | 15.00 | +87.50% |
| Solana TVL | 6,666,319,042.00 | 6,743,140,234.00 | +1.15% |
| SOL price | 121.00 | 121.39 | +0.32% |
| Stablecoin supply | 16,722,578,990.00 | 16,885,469,670.00 | +0.97% |
| 24h DEX volume | 2,131,081,291.43 | 1,649,284,605.63 | -22.61% |
| 24h chain fees | 16,217,391.91 | 15,446,766.41 | -4.75% |

### Change over 30d (vs run at 2026-09-04T19:58:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,586.23 | 4,345.78 | +21.18% |
| Average non-vote TPS | 1,457.68 | 1,847.54 | +26.75% |
| Average slot time (ms) | 315.10 | 267.50 | -15.11% |
| Active validators | 678.00 | 671.00 | -1.03% |
| Delinquent validators | 17.00 | 15.00 | -11.76% |
| Solana TVL | 5,805,967,650.00 | 6,743,140,234.00 | +16.14% |
| SOL price | 101.76 | 121.39 | +19.29% |
| Stablecoin supply | 16,644,416,664.00 | 16,885,469,670.00 | +1.45% |
| 24h DEX volume | 2,459,540,363.80 | 1,649,284,605.63 | -32.94% |
| 24h chain fees | 11,820,876.49 | 15,446,766.41 | +30.67% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 22.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
