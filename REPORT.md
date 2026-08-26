# Solana Ecosystem Pulse

**Generated:** 2026-08-26T06:25:17Z · **Schema:** `1.0.0` · **Collection time:** 17.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.86 | -4.80% |
| Market cap | $56.53B | rank #7 |
| Total value locked | $5.60B | -2.40% |
| Stablecoin supply | $16.32B | -0.67% |
| DEX volume (24h) | $2.95B | -1.58% |
| Chain fees / REV (24h) | $13.03M | -10.11% |
| Non-vote TPS (1h avg) | 1,443 | peak 3,617 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1022 | 70.17% complete | 128,849 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 364.00 sits 18.2 sigma below the median of the last 63 runs (415.20, -12.3%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,599,688,615.00 sits 8.4 sigma above the median of the last 63 runs (4,855,232,078.00, +15.3%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 96.86 sits 8.6 sigma above the median of the last 63 runs (76.73, +26.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,443.1 average over the last 60 minutes; 1,483.6 in the latest sample.
- **Total TPS:** 3,314.8 average, 3,617.1 peak. Consensus votes account for 56.5% of all transactions.
- **Slot time:** 364.0 ms average (target 400 ms), worst 1-minute bucket 375.0 ms.
- **Block height:** 419,855,676 at absolute slot 441,807,151.
- **Epoch 1022:** slot 303,151 of 432,000 (70.17% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 129 ms |
| `solana-rpc.publicnode.com` | yes | 119 ms |
| `api.mainnet.solana.com` | yes | 151 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.044% by stake).
- **Total stake:** 435,118,104 SOL ($42.15B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.20%; 254 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.687% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.699% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.116% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.052% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.973% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.678% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.512% | 0% |

## Economics

- **SOL:** $96.86 (-4.80% 24h, +26.19% 7d, +26.63% 30d). Market cap $56.53B, 24h volume $4.01B (7.10% of cap). Price source: `coingecko`.
- **TVL:** $5.60B across 331 protocols - rank #2 of 465 chains, 6.36% of all tracked chain TVL. +14.35% over 7d, -57.7% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+1.90% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.95B in 24h, $21.60B over 7d across 119 venues. Volume/TVL turnover 0.527x per day.
- **REV (chain fees):** $13.03M in 24h, $290.32M over 30d. Retained chain revenue $5.74M (44.1% of fees). Annualised fees are 8.41% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,375,348 SOL circulating of 632,859,208 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -3.6% | +28.3% |
| 2 | Kamino Lend | Lending | $1.18B | -4.2% | +10.5% |
| 3 | Raydium AMM | Dexs | $1.06B | -4.0% | +24.3% |
| 4 | Jupiter Lend | Lending | $1.06B | -3.5% | +10.8% |
| 5 | Binance Staked SOL | Liquid Staking | $990.67M | -4.0% | +27.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $974.34M | -4.2% | +26.5% |
| 7 | BlackRock BUIDL | RWA | $876.38M | +5.8% | +18.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.82M | -3.2% | +9.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $502.92M | -4.2% | +26.1% |
| 10 | xStocks | RWA | $429.44M | +0.9% | +12.6% |
| 11 | Marinade Native | Staking Pool | $379.56M | -1.3% | +77.9% |
| 12 | Sentora | Risk Curators | $363.14M | +0.0% | -0.8% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 331 protocols the total is $15.84B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.7% · Lending 15.8% · Dexs 14.0% · RWA 13.0% · Derivatives 5.3% · Staking Pool 3.7%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.409% of chain TVL.

- BlackRock BUIDL (RWA): $876.38M
- xStocks (RWA): $429.44M
- Solstice (Basis Trading): $302.99M
- OnRe (RWA): $277.39M
- Ondo Yield Assets (RWA): $179.27M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **961.0 unique fee payers** signed per block (1,390 distinct addresses in the union, 51.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-26
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-25
- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-25
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-25
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25

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

### Change over 24h (vs run at 2026-08-25T06:23:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,277.72 | 3,314.84 | +1.13% |
| Average non-vote TPS | 1,410.38 | 1,443.14 | +2.32% |
| Average slot time (ms) | 364.70 | 364.00 | -0.19% |
| Active validators | 685.00 | 685.00 | +0.00% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 5,791,641,446.00 | 5,599,688,615.00 | -3.31% |
| SOL price | 101.78 | 96.86 | -4.83% |
| Stablecoin supply | 16,425,378,976.00 | 16,315,212,157.00 | -0.67% |
| 24h DEX volume | 2,987,931,793.43 | 2,948,781,265.19 | -1.31% |
| 24h chain fees | 14,086,550.72 | 13,026,619.04 | -7.52% |

### Change over 7d (vs run at 2026-08-19T06:21:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,957.15 | 3,314.84 | +12.10% |
| Average non-vote TPS | 1,329.70 | 1,443.14 | +8.53% |
| Average slot time (ms) | 415.40 | 364.00 | -12.37% |
| Active validators | 676.00 | 685.00 | +1.33% |
| Delinquent validators | 19.00 | 10.00 | -47.37% |
| Solana TVL | 4,894,911,440.00 | 5,599,688,615.00 | +14.40% |
| SOL price | 76.73 | 96.86 | +26.23% |
| Stablecoin supply | 16,009,559,610.00 | 16,315,212,157.00 | +1.91% |
| 24h DEX volume | 1,820,756,097.04 | 2,948,781,265.19 | +61.95% |
| 24h chain fees | 8,714,303.23 | 13,026,619.04 | +49.49% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,314.84 | -15.75% |
| Average non-vote TPS | 2,312.46 | 1,443.14 | -37.59% |
| Average slot time (ms) | 424.10 | 364.00 | -14.17% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 5,599,688,615.00 | +18.14% |
| SOL price | 72.81 | 96.86 | +33.03% |
| Stablecoin supply | 16,197,749,831.00 | 16,315,212,157.00 | +0.73% |
| 24h DEX volume | 1,636,927,091.91 | 2,948,781,265.19 | +80.14% |
| 24h chain fees | 7,777,648.77 | 13,026,619.04 | +67.49% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
