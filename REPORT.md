# Solana Ecosystem Pulse

**Generated:** 2026-09-27T20:31:24Z · **Schema:** `1.0.0` · **Collection time:** 13.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $122.76 | +1.15% |
| Market cap | $72.16B | rank #7 |
| Total value locked | $6.70B | +0.92% |
| Stablecoin supply | $16.80B | -0.04% |
| DEX volume (24h) | $2.16B | -17.52% |
| Chain fees / REV (24h) | $17.94M | +18.97% |
| Non-vote TPS (1h avg) | 2,151 | peak 5,425 total |
| Active validators | 675 | 8 delinquent |
| Epoch 1044 | 22.45% complete | 335,020 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 95 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,150.7 average over the last 60 minutes; 2,260.9 in the latest sample.
- **Total TPS:** 4,659.1 average, 5,424.6 peak. Consensus votes account for 53.8% of all transactions.
- **Slot time:** 268.1 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 429,144,661 at absolute slot 451,104,980.
- **Epoch 1044:** slot 96,980 of 432,000 (22.45% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.628% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 113 ms |
| `solana-rpc.publicnode.com` | yes | 179 ms |
| `api.mainnet.solana.com` | yes | 84 ms |

## Validators & stake

- **675 active** validators, **8 delinquent** (1.17% by count, 0.005% by stake).
- **Total stake:** 440,549,807 SOL ($54.08B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.56% of active stake.
- **Commission:** median 5.0%, mean 12.66%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,867,779 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,792 | 3.596% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,570 | 2.799% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,215,732 | 2.546% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,838,730 | 2.460% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,238,854 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,209,776 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,623,407 | 1.731% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,094,526 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,511,334 | 1.478% | 0% |

## Economics

- **SOL:** $122.76 (+1.15% 24h, +11.14% 7d, +18.76% 30d). Market cap $72.16B, 24h volume $3.84B (5.32% of cap). Price source: `coingecko`.
- **TVL:** $6.70B across 331 protocols - rank #2 of 467 chains, 6.98% of all tracked chain TVL. +8.42% over 7d, -49.4% from its ATH.
- **Stablecoins:** $16.80B circulating on Solana (+6.31% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.16B in 24h, $19.19B over 7d across 126 venues. Volume/TVL turnover 0.322x per day.
- **REV (chain fees):** $17.94M in 24h, $404.05M over 30d. Retained chain revenue $6.76M (37.7% of fees). Annualised fees are 9.07% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,782,727 SOL circulating of 634,841,438 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $2.00B | +1.2% | +13.1% |
| 2 | Kamino Lend | Lending | $1.48B | +0.7% | +7.1% |
| 3 | Raydium AMM | Dexs | $1.39B | +1.3% | +11.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.28B | +1.3% | +11.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.26B | +1.1% | +9.2% |
| 6 | Jupiter Lend | Lending | $1.20B | +1.3% | +7.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $832.97M | +0.8% | +5.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $635.79M | +1.2% | +11.2% |
| 9 | Marinade Native | Staking Pool | $473.98M | +1.2% | +12.1% |
| 10 | PumpSwap | Dexs | $394.59M | -1.4% | +11.6% |
| 11 | Sentora Curator | Risk Curators | $362.97M | +0.2% | -0.5% |
| 12 | Drift Staked SOL | Liquid Staking | $346.63M | +1.3% | +11.1% |

The top five protocols hold 42.5% of Solana's tracked TVL. Summed across all 331 protocols the total is $17.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 17.1% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.3%

### Tokenised assets

$839.08M of tokenised real-world assets and equities are locked on Solana - 4.818% of chain TVL.

- OnRe (RWA): $296.58M
- Solstice (Basis Trading): $215.94M
- Huma (RWA): $212.13M
- JupUSD (Basis Trading): $44.05M
- Plume Vaults (RWA): $25.47M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) - updated 2026-09-27
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19

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

### Change over 24h (vs run at 2026-09-26T20:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,730.02 | 4,659.15 | -1.50% |
| Average non-vote TPS | 2,233.16 | 2,150.72 | -3.69% |
| Average slot time (ms) | 269.50 | 268.10 | -0.52% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 6,636,693,564.00 | 6,696,462,246.00 | +0.90% |
| SOL price | 120.95 | 122.76 | +1.50% |
| Stablecoin supply | 16,991,136,948.00 | 16,803,216,984.00 | -1.11% |
| 24h DEX volume | 2,613,053,225.63 | 2,155,234,120.21 | -17.52% |
| 24h chain fees | 15,598,587.47 | 17,938,389.57 | +15.00% |

### Change over 7d (vs run at 2026-09-20T19:53:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,829.85 | 4,659.15 | -3.53% |
| Average non-vote TPS | 2,325.58 | 2,150.72 | -7.52% |
| Average slot time (ms) | 268.40 | 268.10 | -0.11% |
| Active validators | 675.00 | 675.00 | +0.00% |
| Delinquent validators | 15.00 | 8.00 | -46.67% |
| Solana TVL | 6,171,179,901.00 | 6,696,462,246.00 | +8.51% |
| SOL price | 110.52 | 122.76 | +11.07% |
| Stablecoin supply | 15,806,405,937.00 | 16,803,216,984.00 | +6.31% |
| 24h DEX volume | 2,876,208,374.20 | 2,155,234,120.21 | -25.07% |
| 24h chain fees | 15,275,214.85 | 17,938,389.57 | +17.43% |

### Change over 30d (vs run at 2026-08-28T17:47:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,145.52 | 4,659.15 | -9.45% |
| Average non-vote TPS | 3,011.73 | 2,150.72 | -28.59% |
| Average slot time (ms) | 321.30 | 268.10 | -16.56% |
| Active validators | 688.00 | 675.00 | -1.89% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 5,895,133,114.00 | 6,696,462,246.00 | +13.59% |
| SOL price | 104.55 | 122.76 | +17.42% |
| Stablecoin supply | 16,380,565,155.00 | 16,803,216,984.00 | +2.58% |
| 24h DEX volume | 3,700,129,857.54 | 2,155,234,120.21 | -41.75% |
| 24h chain fees | 16,302,758.52 | 17,938,389.57 | +10.03% |

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
