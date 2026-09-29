# Solana Ecosystem Pulse

**Generated:** 2026-09-29T02:59:13Z · **Schema:** `1.0.0` · **Collection time:** 18.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $116.86 | -2.59% |
| Market cap | $68.69B | rank #7 |
| Total value locked | $6.47B | -2.10% |
| Stablecoin supply | $16.66B | -0.36% |
| DEX volume (24h) | $2.29B | +18.88% |
| Chain fees / REV (24h) | $17.45M | +13.17% |
| Non-vote TPS (1h avg) | 1,921 | peak 4,997 total |
| Active validators | 676 | 6 delinquent |
| Epoch 1045 | 17.11% complete | 358,074 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 95 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,921.1 average over the last 60 minutes; 1,522.8 in the latest sample.
- **Total TPS:** 4,432.8 average, 4,997.5 peak. Consensus votes account for 56.7% of all transactions.
- **Slot time:** 267.8 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 429,553,505 at absolute slot 451,513,926.
- **Epoch 1045:** slot 73,926 of 432,000 (17.11% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 215 ms |
| `solana-rpc.publicnode.com` | yes | 173 ms |
| `api.mainnet.solana.com` | yes | 219 ms |

## Validators & stake

- **676 active** validators, **6 delinquent** (0.88% by count, 0.003% by stake).
- **Total stake:** 441,249,792 SOL ($51.56B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.45% and top 33 hold 45.52% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 230 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.040% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.796% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.561% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.541% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.731% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.518% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.477% | 0% |

## Economics

- **SOL:** $116.86 (-2.59% 24h, -0.58% 7d, +11.05% 30d). Market cap $68.69B, 24h volume $3.91B (5.69% of cap). Price source: `coingecko`.
- **TVL:** $6.47B across 331 protocols - rank #2 of 467 chains, 6.82% of all tracked chain TVL. +0.09% over 7d, -51.2% from its ATH.
- **Stablecoins:** $16.66B circulating on Solana (-2.97% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.29B in 24h, $16.34B over 7d across 126 venues. Volume/TVL turnover 0.354x per day.
- **REV (chain fees):** $17.45M in 24h, $411.41M over 30d. Retained chain revenue $5.92M (33.9% of fees). Annualised fees are 9.27% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,852,776 SOL circulating of 634,918,861 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | -2.6% | +1.5% |
| 2 | Kamino Lend | Lending | $1.40B | -5.1% | -1.5% |
| 3 | Raydium AMM | Dexs | $1.33B | -3.1% | +0.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -2.7% | +0.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.21B | -2.2% | -1.5% |
| 6 | Jupiter Lend | Lending | $1.17B | -2.5% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $807.33M | -2.6% | -2.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $611.39M | -2.4% | -0.4% |
| 9 | Marinade Native | Staking Pool | $450.68M | -3.8% | -0.0% |
| 10 | PumpSwap | Dexs | $385.20M | -2.9% | +2.2% |
| 11 | Sentora Curator | Risk Curators | $361.21M | -0.4% | -0.4% |
| 12 | Drift Staked SOL | Liquid Staking | $334.09M | -2.2% | -0.1% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.86B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 17.0% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$833.81M of tokenised real-world assets and equities are locked on Solana - 4.947% of chain TVL.

- OnRe (RWA): $294.78M
- Solstice (Basis Trading): $215.10M
- Huma (RWA): $208.56M
- JupUSD (Basis Trading): $44.06M
- Plume Vaults (RWA): $25.48M

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

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-09-28
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-28T02:14:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,971.25 | 4,432.82 | -10.83% |
| Average non-vote TPS | 2,474.04 | 1,921.08 | -22.35% |
| Average slot time (ms) | 269.20 | 267.80 | -0.52% |
| Active validators | 675.00 | 676.00 | +0.15% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,666,319,042.00 | 6,466,752,849.00 | -2.99% |
| SOL price | 121.00 | 116.86 | -3.42% |
| Stablecoin supply | 16,722,578,990.00 | 16,662,008,171.00 | -0.36% |
| 24h DEX volume | 2,131,081,291.43 | 2,290,100,033.25 | +7.46% |
| 24h chain fees | 16,217,391.91 | 17,452,720.35 | +7.62% |

### Change over 7d (vs run at 2026-09-22T02:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,603.17 | 4,432.82 | -3.70% |
| Average non-vote TPS | 2,079.85 | 1,921.08 | -7.63% |
| Average slot time (ms) | 267.00 | 267.80 | +0.30% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 14.00 | 6.00 | -57.14% |
| Solana TVL | 6,481,815,506.00 | 6,466,752,849.00 | -0.23% |
| SOL price | 117.51 | 116.86 | -0.55% |
| Stablecoin supply | 17,171,514,140.00 | 16,662,008,171.00 | -2.97% |
| 24h DEX volume | 3,370,332,429.75 | 2,290,100,033.25 | -32.05% |
| 24h chain fees | 17,586,862.12 | 17,452,720.35 | -0.76% |

### Change over 30d (vs run at 2026-08-29T20:04:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,144.50 | 4,432.82 | +6.96% |
| Average non-vote TPS | 1,989.40 | 1,921.08 | -3.43% |
| Average slot time (ms) | 318.30 | 267.80 | -15.87% |
| Active validators | 689.00 | 676.00 | -1.89% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 5,896,456,733.00 | 6,466,752,849.00 | +9.67% |
| SOL price | 105.39 | 116.86 | +10.88% |
| Stablecoin supply | 16,345,994,847.00 | 16,662,008,171.00 | +1.93% |
| 24h DEX volume | 2,590,586,442.22 | 2,290,100,033.25 | -11.60% |
| 24h chain fees | 15,728,868.43 | 17,452,720.35 | +10.96% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
