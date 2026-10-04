# Solana Ecosystem Pulse

**Generated:** 2026-10-04T20:33:38Z · **Schema:** `1.0.0` · **Collection time:** 18.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.79 | +0.66% |
| Market cap | $71.07B | rank #7 |
| Total value locked | $6.72B | +1.30% |
| Stablecoin supply | $16.88B | -0.41% |
| DEX volume (24h) | $1.55B | -43.70% |
| Chain fees / REV (24h) | $12.93M | -25.70% |
| Non-vote TPS (1h avg) | 2,128 | peak 5,294 total |
| Active validators | 671 | 15 delinquent |
| Epoch 1049 | 45.61% complete | 234,979 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 43.7% in 24h) | DEX volume changed -43.7% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,128.0 average over the last 60 minutes; 1,779.4 in the latest sample.
- **Total TPS:** 4,626.2 average, 5,293.6 peak. Consensus votes account for 54.0% of all transactions.
- **Slot time:** 267.7 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 431,403,387 at absolute slot 453,365,021.
- **Epoch 1049:** slot 197,021 of 432,000 (45.61% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.618% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 168 ms |
| `solana-rpc.publicnode.com` | yes | 153 ms |
| `api.mainnet.solana.com` | yes | 144 ms |

## Validators & stake

- **671 active** validators, **15 delinquent** (2.19% by count, 0.027% by stake).
- **Total stake:** 441,848,823 SOL ($53.37B); stake rate 69.56% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.57% and top 33 hold 45.65% of active stake.
- **Commission:** median 5.0%, mean 12.71%; 230 validators at 0% and 62 at 100%.

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

- **SOL:** $120.79 (+0.66% 24h, -1.83% 7d, +18.76% 30d). Market cap $71.07B, 24h volume $1.87B (2.64% of cap). Price source: `coingecko`.
- **TVL:** $6.72B across 334 protocols - rank #2 of 468 chains, 6.98% of all tracked chain TVL. +1.35% over 7d, -49.3% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+0.47% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.55B in 24h, $16.50B over 7d across 126 venues. Volume/TVL turnover 0.231x per day.
- **REV (chain fees):** $12.93M in 24h, $432.74M over 30d. Retained chain revenue $5.32M (41.1% of fees). Annualised fees are 6.64% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,314,411 SOL circulating of 635,227,873 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +1.3% | +0.9% |
| 2 | Kamino Lend | Lending | $1.39B | -0.0% | -4.9% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.4% | -0.4% |
| 4 | Jupiter Lend | Lending | $1.32B | +1.3% | +11.6% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.26B | +1.3% | +0.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +1.4% | +0.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $819.72M | +0.9% | -0.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $627.56M | +1.4% | +0.1% |
| 9 | Marinade Native | Staking Pool | $451.59M | +1.4% | -3.3% |
| 10 | PumpSwap | Dexs | $402.93M | +1.6% | +0.9% |
| 11 | Sentora Curator | Risk Curators | $374.45M | -1.6% | +3.3% |
| 12 | Drift Staked SOL | Liquid Staking | $342.77M | +1.4% | +0.4% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.77B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.36M of tokenised real-world assets and equities are locked on Solana - 5.044% of chain TVL.

- OnRe (RWA): $291.67M
- Huma (RWA): $259.81M
- Solstice (Basis Trading): $212.11M
- JupUSD (Basis Trading): $49.04M
- Plume Vaults (RWA): $32.42M

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

- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-10-03
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [Bump linkify-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/682) - updated 2026-10-02
- [Bump uuid and @actions/core](https://github.com/solana-foundation/solana-improvement-documents/pull/681) - updated 2026-10-02
- [Bump js-yaml from 4.1.0 to 4.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/680) - updated 2026-10-02
- [Bump picomatch from 2.3.1 to 2.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/679) - updated 2026-10-02
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01

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

### Change over 24h (vs run at 2026-10-03T20:17:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,907.58 | 4,626.16 | -5.73% |
| Average non-vote TPS | 2,415.29 | 2,127.97 | -11.90% |
| Average slot time (ms) | 267.60 | 267.70 | +0.04% |
| Active validators | 670.00 | 671.00 | +0.15% |
| Delinquent validators | 15.00 | 15.00 | +0.00% |
| Solana TVL | 6,664,651,516.00 | 6,715,169,332.00 | +0.76% |
| SOL price | 119.93 | 120.79 | +0.72% |
| Stablecoin supply | 16,950,775,065.00 | 16,881,830,613.00 | -0.41% |
| 24h DEX volume | 2,760,296,309.96 | 1,553,984,451.11 | -43.70% |
| 24h chain fees | 17,402,246.04 | 12,930,244.69 | -25.70% |

### Change over 7d (vs run at 2026-09-27T20:31:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.15 | 4,626.16 | -0.71% |
| Average non-vote TPS | 2,150.72 | 2,127.97 | -1.06% |
| Average slot time (ms) | 268.10 | 267.70 | -0.15% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 8.00 | 15.00 | +87.50% |
| Solana TVL | 6,696,462,246.00 | 6,715,169,332.00 | +0.28% |
| SOL price | 122.76 | 120.79 | -1.60% |
| Stablecoin supply | 16,803,216,984.00 | 16,881,830,613.00 | +0.47% |
| 24h DEX volume | 2,155,234,120.21 | 1,553,984,451.11 | -27.90% |
| 24h chain fees | 17,938,389.57 | 12,930,244.69 | -27.92% |

### Change over 30d (vs run at 2026-09-04T19:58:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,586.23 | 4,626.16 | +29.00% |
| Average non-vote TPS | 1,457.68 | 2,127.97 | +45.98% |
| Average slot time (ms) | 315.10 | 267.70 | -15.04% |
| Active validators | 678.00 | 671.00 | -1.03% |
| Delinquent validators | 17.00 | 15.00 | -11.76% |
| Solana TVL | 5,805,967,650.00 | 6,715,169,332.00 | +15.66% |
| SOL price | 101.76 | 120.79 | +18.70% |
| Stablecoin supply | 16,644,416,664.00 | 16,881,830,613.00 | +1.43% |
| 24h DEX volume | 2,459,540,363.80 | 1,553,984,451.11 | -36.82% |
| 24h chain fees | 11,820,876.49 | 12,930,244.69 | +9.38% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
