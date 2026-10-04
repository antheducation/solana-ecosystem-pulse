# Solana Ecosystem Pulse

**Generated:** 2026-10-04T16:03:23Z · **Schema:** `1.0.0` · **Collection time:** 13.7s · **Sources OK:** 39/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $121.57 | +1.63% |
| Market cap | $71.52B | rank #7 |
| Total value locked | $6.72B | +1.38% |
| Stablecoin supply | $16.88B | -0.42% |
| DEX volume (24h) | $1.55B | -43.70% |
| Chain fees / REV (24h) | $12.93M | -25.67% |
| Non-vote TPS (1h avg) | 2,034 | peak 5,243 total |
| Active validators | 671 | 15 delinquent |
| Epoch 1049 | 31.65% complete | 295,253 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 43.7% in 24h) | DEX volume changed -43.7% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,034.0 average over the last 60 minutes; 2,184.3 in the latest sample.
- **Total TPS:** 4,533.5 average, 5,242.7 peak. Consensus votes account for 55.1% of all transactions.
- **Slot time:** 267.5 ms average (target 400 ms), worst 1-minute bucket 283.0 ms.
- **Block height:** 431,343,138 at absolute slot 453,304,747.
- **Epoch 1049:** slot 136,747 of 432,000 (31.65% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.618% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 155 ms |
| `solana-rpc.publicnode.com` | yes | 65 ms |
| `api.mainnet.solana.com` | yes | 201 ms |

## Validators & stake

- **671 active** validators, **15 delinquent** (2.19% by count, 0.027% by stake).
- **Total stake:** 441,848,823 SOL ($53.72B); stake rate 69.56% of total supply.
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

- **SOL:** $121.57 (+1.63% 24h, -0.14% 7d, +19.84% 30d). Market cap $71.52B, 24h volume $1.87B (2.62% of cap). Price source: `coingecko`.
- **TVL:** $6.72B across 334 protocols - rank #2 of 468 chains, 7.00% of all tracked chain TVL. +1.43% over 7d, -49.3% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+0.45% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.55B in 24h, $16.50B over 7d across 126 venues. Volume/TVL turnover 0.231x per day.
- **REV (chain fees):** $12.93M in 24h, $432.74M over 30d. Retained chain revenue $5.32M (41.1% of fees). Annualised fees are 6.60% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,314,615 SOL circulating of 635,228,077 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +1.4% | +0.9% |
| 2 | Kamino Lend | Lending | $1.40B | +0.6% | -4.6% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.8% | -0.1% |
| 4 | Jupiter Lend | Lending | $1.32B | +1.3% | +11.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.27B | +1.9% | +0.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +2.0% | +0.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $820.82M | +1.0% | -0.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $629.26M | +2.0% | +0.3% |
| 9 | Marinade Native | Staking Pool | $452.83M | +1.8% | -3.0% |
| 10 | PumpSwap | Dexs | $403.46M | +1.8% | +1.1% |
| 11 | Sentora Curator | Risk Curators | $374.42M | -1.9% | +3.3% |
| 12 | Drift Staked SOL | Liquid Staking | $343.73M | +1.8% | +0.6% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.79B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.75M of tokenised real-world assets and equities are locked on Solana - 5.040% of chain TVL.

- OnRe (RWA): $291.66M
- Huma (RWA): $260.11M
- Solstice (Basis Trading): $212.11M
- JupUSD (Basis Trading): $49.18M
- Plume Vaults (RWA): $32.41M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT

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

### Change over 24h (vs run at 2026-10-03T15:18:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,322.31 | 4,533.46 | +4.89% |
| Average non-vote TPS | 1,813.38 | 2,034.00 | +12.17% |
| Average slot time (ms) | 267.30 | 267.50 | +0.07% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 12.00 | 15.00 | +25.00% |
| Solana TVL | 6,649,842,310.00 | 6,719,553,426.00 | +1.05% |
| SOL price | 119.56 | 121.57 | +1.68% |
| Stablecoin supply | 16,950,098,411.00 | 16,879,996,235.00 | -0.41% |
| 24h DEX volume | 2,760,296,309.96 | 1,553,984,451.11 | -43.70% |
| 24h chain fees | 17,402,246.04 | 12,934,775.54 | -25.67% |

### Change over 7d (vs run at 2026-09-27T15:54:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,484.29 | 4,533.46 | +1.10% |
| Average non-vote TPS | 1,984.20 | 2,034.00 | +2.51% |
| Average slot time (ms) | 268.80 | 267.50 | -0.48% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 8.00 | 15.00 | +87.50% |
| Solana TVL | 6,683,441,069.00 | 6,719,553,426.00 | +0.54% |
| SOL price | 121.70 | 121.57 | -0.11% |
| Stablecoin supply | 16,804,553,195.00 | 16,879,996,235.00 | +0.45% |
| 24h DEX volume | 2,155,234,120.21 | 1,553,984,451.11 | -27.90% |
| 24h chain fees | 17,934,741.57 | 12,934,775.54 | -27.88% |

### Change over 30d (vs run at 2026-09-04T19:58:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,586.23 | 4,533.46 | +26.41% |
| Average non-vote TPS | 1,457.68 | 2,034.00 | +39.54% |
| Average slot time (ms) | 315.10 | 267.50 | -15.11% |
| Active validators | 678.00 | 671.00 | -1.03% |
| Delinquent validators | 17.00 | 15.00 | -11.76% |
| Solana TVL | 5,805,967,650.00 | 6,719,553,426.00 | +15.74% |
| SOL price | 101.76 | 121.57 | +19.47% |
| Stablecoin supply | 16,644,416,664.00 | 16,879,996,235.00 | +1.42% |
| 24h DEX volume | 2,459,540,363.80 | 1,553,984,451.11 | -36.82% |
| 24h chain fees | 11,820,876.49 | 12,934,775.54 | +9.42% |

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

This run made 41 HTTP calls (39 succeeded, 2 failed) in 13.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
