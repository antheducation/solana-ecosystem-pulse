# Solana Ecosystem Pulse

**Generated:** 2026-10-05T12:50:28Z · **Schema:** `1.0.0` · **Collection time:** 13.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.44 | -0.77% |
| Market cap | $70.85B | rank #7 |
| Total value locked | $6.72B | +1.60% |
| Stablecoin supply | $16.88B | +0.01% |
| DEX volume (24h) | $1.71B | +9.92% |
| Chain fees / REV (24h) | $16.13M | +24.72% |
| Non-vote TPS (1h avg) | 1,378 | peak 4,293 total |
| Active validators | 671 | 15 delinquent |
| Epoch 1049 | 96.35% complete | 15,756 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,378.3 average over the last 60 minutes; 1,257.1 in the latest sample.
- **Total TPS:** 3,875.1 average, 4,293.4 peak. Consensus votes account for 64.4% of all transactions.
- **Slot time:** 267.7 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 431,622,351 at absolute slot 453,584,244.
- **Epoch 1049:** slot 416,244 of 432,000 (96.35% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.618% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 95 ms |
| `solana-rpc.publicnode.com` | yes | 163 ms |
| `api.mainnet.solana.com` | yes | 99 ms |

## Validators & stake

- **671 active** validators, **15 delinquent** (2.19% by count, 0.027% by stake).
- **Total stake:** 441,848,823 SOL ($53.22B); stake rate 69.56% of total supply.
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

- **SOL:** $120.44 (-0.77% 24h, +1.49% 7d, +17.67% 30d). Market cap $70.85B, 24h volume $2.51B (3.54% of cap). Price source: `coingecko`.
- **TVL:** $6.72B across 334 protocols - rank #2 of 468 chains, 6.94% of all tracked chain TVL. +1.25% over 7d, -49.2% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+0.97% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.71B in 24h, $16.28B over 7d across 126 venues. Volume/TVL turnover 0.254x per day.
- **REV (chain fees):** $16.13M in 24h, $440.48M over 30d. Retained chain revenue $6.04M (37.4% of fees). Annualised fees are 8.31% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,313,758 SOL circulating of 635,227,225 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.98B | -0.6% | -0.1% |
| 2 | Kamino Lend | Lending | $1.40B | -0.0% | -5.2% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.2% | +0.7% |
| 4 | Jupiter Lend | Lending | $1.32B | +0.5% | +10.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.26B | -0.4% | -0.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +0.7% | +0.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $817.95M | -0.2% | -1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $623.68M | -0.5% | -0.8% |
| 9 | Marinade Native | Staking Pool | $448.54M | -0.6% | -4.3% |
| 10 | PumpSwap | Dexs | $404.97M | +0.4% | +2.0% |
| 11 | Sentora Curator | Risk Curators | $379.39M | +1.3% | +4.5% |
| 12 | Drift Staked SOL | Liquid Staking | $340.80M | -0.5% | -0.6% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.55M of tokenised real-world assets and equities are locked on Solana - 5.049% of chain TVL.

- OnRe (RWA): $292.81M
- Huma (RWA): $259.14M
- Solstice (Basis Trading): $212.12M
- JupUSD (Basis Trading): $48.65M
- Plume Vaults (RWA): $32.51M

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

- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-05
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-05
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-05
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-05
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-05

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

### Change over 24h (vs run at 2026-10-04T11:25:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,957.72 | 3,875.14 | -2.09% |
| Average non-vote TPS | 1,450.73 | 1,378.28 | -4.99% |
| Average slot time (ms) | 266.70 | 267.70 | +0.37% |
| Active validators | 671.00 | 671.00 | +0.00% |
| Delinquent validators | 15.00 | 15.00 | +0.00% |
| Solana TVL | 6,697,034,306.00 | 6,721,988,816.00 | +0.37% |
| SOL price | 121.32 | 120.44 | -0.73% |
| Stablecoin supply | 16,881,455,761.00 | 16,884,585,049.00 | +0.02% |
| 24h DEX volume | 1,553,984,451.11 | 1,708,158,585.63 | +9.92% |
| 24h chain fees | 12,836,094.54 | 16,126,162.37 | +25.63% |

### Change over 7d (vs run at 2026-09-28T12:10:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,130.98 | 3,875.14 | -6.19% |
| Average non-vote TPS | 1,618.33 | 1,378.28 | -14.83% |
| Average slot time (ms) | 268.00 | 267.70 | -0.11% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 8.00 | 15.00 | +87.50% |
| Solana TVL | 6,503,643,660.00 | 6,721,988,816.00 | +3.36% |
| SOL price | 119.58 | 120.44 | +0.72% |
| Stablecoin supply | 16,722,135,325.00 | 16,884,585,049.00 | +0.97% |
| 24h DEX volume | 1,926,466,128.71 | 1,708,158,585.63 | -11.33% |
| 24h chain fees | 15,306,075.25 | 16,126,162.37 | +5.36% |

### Change over 30d (vs run at 2026-09-05T19:38:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,427.43 | 3,875.14 | +13.06% |
| Average non-vote TPS | 1,291.31 | 1,378.28 | +6.74% |
| Average slot time (ms) | 315.00 | 267.70 | -15.02% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 18.00 | 15.00 | -16.67% |
| Solana TVL | 5,915,402,920.00 | 6,721,988,816.00 | +13.64% |
| SOL price | 103.80 | 120.44 | +16.03% |
| Stablecoin supply | 16,607,441,030.00 | 16,884,585,049.00 | +1.67% |
| 24h DEX volume | 1,881,639,252.00 | 1,708,158,585.63 | -9.22% |
| 24h chain fees | 10,436,292.55 | 16,126,162.37 | +54.52% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
