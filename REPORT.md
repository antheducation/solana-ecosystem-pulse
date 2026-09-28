# Solana Ecosystem Pulse

**Generated:** 2026-09-28T22:41:17Z · **Schema:** `1.0.0` · **Collection time:** 14.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.18 | -2.48% |
| Market cap | $69.48B | rank #7 |
| Total value locked | $6.55B | -1.09% |
| Stablecoin supply | $16.72B | -0.48% |
| DEX volume (24h) | $1.93B | -10.61% |
| Chain fees / REV (24h) | $15.42M | -14.03% |
| Non-vote TPS (1h avg) | 2,010 | peak 5,123 total |
| Active validators | 674 | 8 delinquent |
| Epoch 1045 | 3.75% complete | 415,820 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,010.4 average over the last 60 minutes; 1,659.0 in the latest sample.
- **Total TPS:** 4,519.3 average, 5,123.3 peak. Consensus votes account for 55.5% of all transactions.
- **Slot time:** 267.2 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 429,495,774 at absolute slot 451,456,180.
- **Epoch 1045:** slot 16,180 of 432,000 (3.75% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 235 ms |
| `solana-rpc.publicnode.com` | yes | 58 ms |
| `api.mainnet.solana.com` | yes | 188 ms |

## Validators & stake

- **674 active** validators, **8 delinquent** (1.17% by count, 0.572% by stake).
- **Total stake:** 441,249,792 SOL ($52.15B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.39%; 229 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.063% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.621% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.812% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.576% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.555% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.107% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.103% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.741% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.527% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.486% | 0% |

## Economics

- **SOL:** $118.18 (-2.48% 24h, -0.80% 7d, +12.51% 30d). Market cap $69.48B, 24h volume $4.07B (5.86% of cap). Price source: `coingecko`.
- **TVL:** $6.55B across 331 protocols - rank #2 of 467 chains, 6.90% of all tracked chain TVL. +5.58% over 7d, -50.5% from its ATH.
- **Stablecoins:** $16.72B circulating on Solana (+5.14% 7d) - $2.55 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.93B in 24h, $18.32B over 7d across 126 venues. Volume/TVL turnover 0.294x per day.
- **REV (chain fees):** $15.42M in 24h, $404.79M over 30d. Retained chain revenue $5.30M (34.4% of fees). Annualised fees are 8.10% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,853,181 SOL circulating of 634,919,041 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.93B | -3.1% | +7.8% |
| 2 | Kamino Lend | Lending | $1.45B | -2.3% | +5.8% |
| 3 | Raydium AMM | Dexs | $1.35B | -2.5% | +6.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -3.7% | +6.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.22B | -3.1% | +4.1% |
| 6 | Jupiter Lend | Lending | $1.17B | -2.3% | +4.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $807.26M | -3.0% | +1.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.79M | -4.0% | +6.3% |
| 9 | Marinade Native | Staking Pool | $458.16M | -3.1% | +8.1% |
| 10 | PumpSwap | Dexs | $393.55M | -1.6% | +6.9% |
| 11 | Sentora Curator | Risk Curators | $361.95M | -0.3% | -0.7% |
| 12 | Drift Staked SOL | Liquid Staking | $335.10M | -3.1% | +7.1% |

The top five protocols hold 42.3% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.96B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.2% · Dexs 16.0% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$834.10M of tokenised real-world assets and equities are locked on Solana - 4.918% of chain TVL.

- OnRe (RWA): $294.70M
- Solstice (Basis Trading): $215.10M
- Huma (RWA): $208.97M
- JupUSD (Basis Trading): $44.05M
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

- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-28
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

### Change over 24h (vs run at 2026-09-27T20:31:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.15 | 4,519.28 | -3.00% |
| Average non-vote TPS | 2,150.72 | 2,010.42 | -6.52% |
| Average slot time (ms) | 268.10 | 267.20 | -0.34% |
| Active validators | 675.00 | 674.00 | -0.15% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 6,696,462,246.00 | 6,552,189,378.00 | -2.15% |
| SOL price | 122.76 | 118.18 | -3.73% |
| Stablecoin supply | 16,803,216,984.00 | 16,723,366,837.00 | -0.48% |
| 24h DEX volume | 2,155,234,120.21 | 1,926,466,128.71 | -10.61% |
| 24h chain fees | 17,938,389.57 | 15,421,946.25 | -14.03% |

### Change over 7d (vs run at 2026-09-21T21:17:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.01 | 4,519.28 | -3.00% |
| Average non-vote TPS | 2,142.85 | 2,010.42 | -6.18% |
| Average slot time (ms) | 266.70 | 267.20 | +0.19% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 14.00 | 8.00 | -42.86% |
| Solana TVL | 6,474,683,879.00 | 6,552,189,378.00 | +1.20% |
| SOL price | 118.81 | 118.18 | -0.53% |
| Stablecoin supply | 15,907,385,261.00 | 16,723,366,837.00 | +5.13% |
| 24h DEX volume | 2,795,356,104.36 | 1,926,466,128.71 | -31.08% |
| 24h chain fees | 14,463,382.08 | 15,421,946.25 | +6.63% |

### Change over 30d (vs run at 2026-08-29T20:04:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,144.50 | 4,519.28 | +9.04% |
| Average non-vote TPS | 1,989.40 | 2,010.42 | +1.06% |
| Average slot time (ms) | 318.30 | 267.20 | -16.05% |
| Active validators | 689.00 | 674.00 | -2.18% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 5,896,456,733.00 | 6,552,189,378.00 | +11.12% |
| SOL price | 105.39 | 118.18 | +12.14% |
| Stablecoin supply | 16,345,994,847.00 | 16,723,366,837.00 | +2.31% |
| 24h DEX volume | 2,590,586,442.22 | 1,926,466,128.71 | -25.64% |
| 24h chain fees | 15,728,868.43 | 15,421,946.25 | -1.95% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
