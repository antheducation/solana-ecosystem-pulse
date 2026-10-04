# Solana Ecosystem Pulse

**Generated:** 2026-10-04T03:07:00Z · **Schema:** `1.0.0` · **Collection time:** 13.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.36 | +1.22% |
| Market cap | $70.76B | rank #7 |
| Total value locked | $6.67B | +0.55% |
| Stablecoin supply | $16.88B | -0.42% |
| DEX volume (24h) | $2.13B | -22.75% |
| Chain fees / REV (24h) | $12.98M | -25.43% |
| Non-vote TPS (1h avg) | 1,722 | peak 4,771 total |
| Active validators | 671 | 14 delinquent |
| Epoch 1048 | 91.31% complete | 37,553 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 100 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,721.5 average over the last 60 minutes; 1,674.0 in the latest sample.
- **Total TPS:** 4,227.0 average, 4,770.6 peak. Consensus votes account for 59.3% of all transactions.
- **Slot time:** 266.6 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 431,168,891 at absolute slot 453,130,447.
- **Epoch 1048:** slot 394,447 of 432,000 (91.31% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.620% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 135 ms |
| `solana-rpc.publicnode.com` | yes | 118 ms |
| `api.mainnet.solana.com` | yes | 107 ms |

## Validators & stake

- **671 active** validators, **14 delinquent** (2.04% by count, 0.035% by stake).
- **Total stake:** 442,013,190 SOL ($53.20B); stake rate 69.59% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.54% and top 33 hold 45.63% of active stake.
- **Commission:** median 5.0%, mean 13.02%; 226 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,923,954 | 4.057% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,898,894 | 3.598% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,401 | 2.792% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,304,108 | 2.558% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,133,145 | 2.520% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,247,324 | 2.093% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,244,926 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,605,153 | 1.721% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,060,361 | 1.598% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,684,213 | 1.513% | 0% |

## Economics

- **SOL:** $120.36 (+1.22% 24h, -0.61% 7d, +16.03% 30d). Market cap $70.76B, 24h volume $1.56B (2.21% of cap). Price source: `coingecko`.
- **TVL:** $6.67B across 334 protocols - rank #2 of 468 chains, 6.97% of all tracked chain TVL. +0.69% over 7d, -49.6% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+0.46% 7d) - $2.53 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.13B in 24h, $15.86B over 7d across 126 venues. Volume/TVL turnover 0.320x per day.
- **REV (chain fees):** $12.98M in 24h, $432.02M over 30d. Retained chain revenue $5.45M (42.0% of fees). Annualised fees are 6.69% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,145,378 SOL circulating of 635,149,951 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.97B | +0.8% | -0.1% |
| 2 | Kamino Lend | Lending | $1.39B | -0.1% | -5.5% |
| 3 | Raydium AMM | Dexs | $1.35B | +0.3% | -0.6% |
| 4 | Jupiter Lend | Lending | $1.31B | +0.8% | +10.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.25B | +0.8% | -0.5% |
| 6 | Binance Staked SOL | Liquid Staking | $1.23B | +0.7% | -0.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $811.67M | +0.1% | -1.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $620.22M | +0.7% | -1.1% |
| 9 | Marinade Native | Staking Pool | $446.41M | +0.7% | -4.4% |
| 10 | PumpSwap | Dexs | $400.02M | +1.8% | +0.2% |
| 11 | Sentora Curator | Risk Curators | $374.85M | -2.0% | +3.4% |
| 12 | Drift Staked SOL | Liquid Staking | $338.87M | +0.7% | -0.8% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.62B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.91M of tokenised real-world assets and equities are locked on Solana - 5.091% of chain TVL.

- OnRe (RWA): $291.64M
- Huma (RWA): $260.06M
- Solstice (Basis Trading): $212.35M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.41M

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

### Change over 24h (vs run at 2026-10-03T02:35:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,081.59 | 4,226.99 | +3.56% |
| Average non-vote TPS | 1,576.02 | 1,721.51 | +9.23% |
| Average slot time (ms) | 267.20 | 266.60 | -0.22% |
| Active validators | 672.00 | 671.00 | -0.15% |
| Delinquent validators | 12.00 | 14.00 | +16.67% |
| Solana TVL | 6,615,550,945.00 | 6,668,023,483.00 | +0.79% |
| SOL price | 119.15 | 120.36 | +1.02% |
| Stablecoin supply | 16,950,465,224.00 | 16,880,130,771.00 | -0.41% |
| 24h DEX volume | 2,569,613,456.96 | 2,132,195,295.11 | -17.02% |
| 24h chain fees | 17,357,994.82 | 12,977,249.54 | -25.24% |

### Change over 7d (vs run at 2026-09-27T02:09:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,487.76 | 4,226.99 | -5.81% |
| Average non-vote TPS | 1,988.22 | 1,721.51 | -13.41% |
| Average slot time (ms) | 268.20 | 266.60 | -0.60% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 14.00 | 14.00 | +0.00% |
| Solana TVL | 6,628,203,292.00 | 6,668,023,483.00 | +0.60% |
| SOL price | 121.31 | 120.36 | -0.78% |
| Stablecoin supply | 16,803,934,871.00 | 16,880,130,771.00 | +0.45% |
| 24h DEX volume | 2,350,289,556.23 | 2,132,195,295.11 | -9.28% |
| 24h chain fees | 18,302,413.77 | 12,977,249.54 | -29.10% |

### Change over 30d (vs run at 2026-09-03T20:12:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,437.74 | 4,226.99 | -4.75% |
| Average non-vote TPS | 2,316.58 | 1,721.51 | -25.69% |
| Average slot time (ms) | 316.10 | 266.60 | -15.66% |
| Active validators | 676.00 | 671.00 | -0.74% |
| Delinquent validators | 19.00 | 14.00 | -26.32% |
| Solana TVL | 5,969,689,229.00 | 6,668,023,483.00 | +11.70% |
| SOL price | 105.35 | 120.36 | +14.25% |
| Stablecoin supply | 16,102,283,829.00 | 16,880,130,771.00 | +4.83% |
| 24h DEX volume | 2,289,285,889.32 | 2,132,195,295.11 | -6.86% |
| 24h chain fees | 10,535,900.15 | 12,977,249.54 | +23.17% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
