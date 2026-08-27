# Solana Ecosystem Pulse

**Generated:** 2026-08-27T05:23:22Z · **Schema:** `1.0.0` · **Collection time:** 18.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.92 | +4.52% |
| Market cap | $58.94B | rank #7 |
| Total value locked | $5.77B | +2.92% |
| Stablecoin supply | $16.29B | -0.15% |
| DEX volume (24h) | $2.48B | -15.46% |
| Chain fees / REV (24h) | $14.68M | +10.93% |
| Non-vote TPS (1h avg) | 1,522 | peak 3,825 total |
| Active validators | 686 | 11 delinquent |
| Epoch 1023 | 22.51% complete | 334,764 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 364.30 sits 18.1 sigma below the median of the last 63 runs (415.20, -12.3%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 100.92 sits 6.1 sigma above the median of the last 63 runs (77.08, +30.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 5,770,223,599.00 sits 4.2 sigma above the median of the last 63 runs (4,894,911,440.00, +17.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,521.7 average over the last 60 minutes; 1,368.1 in the latest sample.
- **Total TPS:** 3,396.4 average, 3,824.8 peak. Consensus votes account for 55.2% of all transactions.
- **Slot time:** 364.3 ms average (target 400 ms), worst 1-minute bucket 372.7 ms.
- **Block height:** 420,081,539 at absolute slot 442,033,236.
- **Epoch 1023:** slot 97,236 of 432,000 (22.51% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.677% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 279 ms |
| `solana-rpc.publicnode.com` | yes | 54 ms |
| `api.mainnet.solana.com` | yes | 251 ms |

## Validators & stake

- **686 active** validators, **11 delinquent** (1.58% by count, 0.022% by stake).
- **Total stake:** 436,884,837 SOL ($44.09B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.76% of active stake.
- **Commission:** median 5.0%, mean 11.90%; 256 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,062,869 | 3.906% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,029,433 | 3.670% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,314,379 | 2.819% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,751,683 | 2.690% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,852 | 2.110% | 7% |
| 6 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,051,084 | 2.072% | 0% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,904,595 | 2.039% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,849,682 | 1.797% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,301,740 | 1.672% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,578,261 | 1.506% | 0% |

## Economics

- **SOL:** $100.92 (+4.52% 24h, +19.02% 7d, +37.97% 30d). Market cap $58.94B, 24h volume $3.84B (6.52% of cap). Price source: `coingecko`.
- **TVL:** $5.77B across 333 protocols - rank #2 of 465 chains, 6.52% of all tracked chain TVL. +10.39% over 7d, -56.4% from its ATH.
- **Stablecoins:** $16.29B circulating on Solana (-0.22% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.48B in 24h, $21.07B over 7d across 119 venues. Volume/TVL turnover 0.430x per day.
- **REV (chain fees):** $14.68M in 24h, $288.84M over 30d. Retained chain revenue $6.02M (41.0% of fees). Annualised fees are 9.09% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 584,062,983 SOL circulating of 632,969,799 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | +3.9% | +20.0% |
| 2 | Kamino Lend | Lending | $1.21B | +2.5% | +6.8% |
| 3 | Raydium AMM | Dexs | $1.11B | +4.0% | +18.2% |
| 4 | Jupiter Lend | Lending | $1.09B | +3.4% | +8.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | +3.5% | +19.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.01B | +4.0% | +18.6% |
| 7 | BlackRock BUIDL | RWA | $886.37M | +1.1% | +19.7% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $767.21M | +2.1% | +4.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $523.63M | +4.0% | +18.0% |
| 10 | xStocks | RWA | $428.52M | -0.2% | +5.5% |
| 11 | Marinade Native | Staking Pool | $401.65M | +5.7% | +65.8% |
| 12 | Sentora | Risk Curators | $363.16M | +0.0% | -0.7% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.1% · Lending 15.8% · Dexs 14.1% · RWA 12.7% · Derivatives 5.3% · Staking Pool 3.8%

### Tokenised assets

$2.45B of tokenised real-world assets and equities are locked on Solana - 15.026% of chain TVL.

- BlackRock BUIDL (RWA): $886.37M
- xStocks (RWA): $428.52M
- Solstice (Basis Trading): $303.00M
- OnRe (RWA): $277.89M
- Ondo Yield Assets (RWA): $178.87M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **952.3 unique fee payers** signed per block (1,368 distinct addresses in the union, 52.1% overlap between blocks).

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

- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-26
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-26T06:25:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,314.84 | 3,396.37 | +2.46% |
| Average non-vote TPS | 1,443.14 | 1,521.66 | +5.44% |
| Average slot time (ms) | 364.00 | 364.30 | +0.08% |
| Active validators | 685.00 | 686.00 | +0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,599,688,615.00 | 5,770,223,599.00 | +3.05% |
| SOL price | 96.86 | 100.92 | +4.19% |
| Stablecoin supply | 16,315,212,157.00 | 16,290,346,473.00 | -0.15% |
| 24h DEX volume | 2,948,781,265.19 | 2,481,205,722.00 | -15.86% |
| 24h chain fees | 13,026,619.04 | 14,682,184.01 | +12.71% |

### Change over 7d (vs run at 2026-08-20T06:22:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,047.31 | 3,396.37 | +11.45% |
| Average non-vote TPS | 1,404.08 | 1,521.66 | +8.37% |
| Average slot time (ms) | 416.00 | 364.30 | -12.43% |
| Active validators | 688.00 | 686.00 | -0.29% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 5,198,850,712.00 | 5,770,223,599.00 | +10.99% |
| SOL price | 84.84 | 100.92 | +18.95% |
| Stablecoin supply | 16,322,645,608.00 | 16,290,346,473.00 | -0.20% |
| 24h DEX volume | 2,789,524,387.95 | 2,481,205,722.00 | -11.05% |
| 24h chain fees | 13,172,440.83 | 14,682,184.01 | +11.46% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,396.37 | -13.68% |
| Average non-vote TPS | 2,312.46 | 1,521.66 | -34.20% |
| Average slot time (ms) | 424.10 | 364.30 | -14.10% |
| Active validators | 692.00 | 686.00 | -0.87% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 4,740,035,266.00 | 5,770,223,599.00 | +21.73% |
| SOL price | 72.81 | 100.92 | +38.61% |
| Stablecoin supply | 16,197,749,831.00 | 16,290,346,473.00 | +0.57% |
| 24h DEX volume | 1,636,927,091.91 | 2,481,205,722.00 | +51.58% |
| 24h chain fees | 7,777,648.77 | 14,682,184.01 | +88.77% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
