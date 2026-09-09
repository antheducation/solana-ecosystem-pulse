# Solana Ecosystem Pulse

**Generated:** 2026-09-09T01:50:03Z · **Schema:** `1.0.0` · **Collection time:** 14.9s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.84 | -0.33% |
| Market cap | $60.87B | rank #7 |
| Total value locked | $5.95B | +0.12% |
| Stablecoin supply | $16.63B | -0.39% |
| DEX volume (24h) | $2.58B | -5.24% |
| Chain fees / REV (24h) | $15.98M | +2.22% |
| Non-vote TPS (1h avg) | 2,324 | peak 4,962 total |
| Active validators | 677 | 10 delinquent |
| Epoch 1031 | 22.67% complete | 334,085 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 71 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,323.6 average over the last 60 minutes; 2,311.1 in the latest sample.
- **Total TPS:** 4,448.6 average, 4,962.3 peak. Consensus votes account for 47.8% of all transactions.
- **Slot time:** 317.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 423,533,798 at absolute slot 445,489,915.
- **Epoch 1031:** slot 97,915 of 432,000 (22.67% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 105 ms |
| `solana-rpc.publicnode.com` | yes | 211 ms |
| `api.mainnet.solana.com` | yes | 86 ms |

## Validators & stake

- **677 active** validators, **10 delinquent** (1.46% by count, 0.012% by stake).
- **Total stake:** 438,653,505 SOL ($45.55B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.67% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 243 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,436,766 | 3.976% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,345,792 | 3.727% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,527,540 | 2.856% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,388,333 | 2.597% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,566,721 | 2.181% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,286,723 | 2.117% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,027,481 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,322,728 | 1.670% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,860,585 | 1.564% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,604,066 | 1.506% | 0% |

## Economics

- **SOL:** $103.84 (-0.33% 24h, +4.24% 7d, +35.75% 30d). Market cap $60.87B, 24h volume $2.93B (4.81% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 341 protocols - rank #2 of 466 chains, 6.75% of all tracked chain TVL. +5.19% over 7d, -55.1% from its ATH.
- **Stablecoins:** $16.63B circulating on Solana (+4.92% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.58B in 24h, $15.86B over 7d across 121 venues. Volume/TVL turnover 0.433x per day.
- **REV (chain fees):** $15.98M in 24h, $349.46M over 30d. Retained chain revenue $6.38M (39.9% of fees). Annualised fees are 9.58% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,250,901 SOL circulating of 633,737,127 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | +0.0% | +3.8% |
| 2 | Kamino Lend | Lending | $1.36B | +2.2% | +12.8% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.3% | +5.4% |
| 4 | Jupiter Lend | Lending | $1.10B | +0.9% | +5.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | -0.0% | +4.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | +0.0% | +5.8% |
| 7 | BlackRock BUIDL | RWA | $987.58M | +1.0% | +11.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.12M | -0.7% | +0.8% |
| 9 | Jupiter Staked SOL | Liquid Staking | $535.80M | -0.1% | +3.8% |
| 10 | xStocks | RWA | $443.41M | -0.6% | +2.6% |
| 11 | Marinade Native | Staking Pool | $402.90M | -1.9% | +1.3% |
| 12 | Sentora Curator | Risk Curators | $384.84M | -0.5% | +6.1% |

The top five protocols hold 37.0% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.92B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.2% · Dexs 13.9% · RWA 13.9% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.716% of chain TVL.

- BlackRock BUIDL (RWA): $987.58M
- xStocks (RWA): $443.41M
- OnRe (RWA): $304.34M
- Solstice (Basis Trading): $235.70M
- Ondo Yield Assets (RWA): $180.10M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,016.7 unique fee payers** signed per block (1,518 distinct addresses in the union, 50.2% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-09-08
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02

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

### Change over 24h (vs run at 2026-09-08T01:42:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,552.09 | 4,448.61 | +25.24% |
| Average non-vote TPS | 1,424.81 | 2,323.56 | +63.08% |
| Average slot time (ms) | 316.10 | 317.10 | +0.32% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,910,151,740.00 | 5,949,941,999.00 | +0.67% |
| SOL price | 104.14 | 103.84 | -0.29% |
| Stablecoin supply | 16,740,790,725.00 | 16,630,993,220.00 | -0.66% |
| 24h DEX volume | 2,872,029,701.66 | 2,578,119,137.34 | -10.23% |
| 24h chain fees | 13,419,392.83 | 15,979,592.70 | +19.08% |

### Change over 7d (vs run at 2026-09-02T01:39:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,115.59 | 4,448.61 | +8.09% |
| Average non-vote TPS | 1,979.08 | 2,323.56 | +17.41% |
| Average slot time (ms) | 316.20 | 317.10 | +0.28% |
| Active validators | 678.00 | 677.00 | -0.15% |
| Delinquent validators | 16.00 | 10.00 | -37.50% |
| Solana TVL | 5,658,999,019.00 | 5,949,941,999.00 | +5.14% |
| SOL price | 99.33 | 103.84 | +4.54% |
| Stablecoin supply | 15,968,502,758.00 | 16,630,993,220.00 | +4.15% |
| 24h DEX volume | 2,358,272,391.49 | 2,578,119,137.34 | +9.32% |
| 24h chain fees | 14,355,983.93 | 15,979,592.70 | +11.31% |

### Change over 30d (vs run at 2026-08-09T18:21:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,304.40 | 4,448.61 | +3.35% |
| Average non-vote TPS | 2,694.81 | 2,323.56 | -13.78% |
| Average slot time (ms) | 426.40 | 317.10 | -25.63% |
| Active validators | 691.00 | 677.00 | -2.03% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,857,325,993.00 | 5,949,941,999.00 | +22.49% |
| SOL price | 77.09 | 103.84 | +34.70% |
| Stablecoin supply | 16,258,695,331.00 | 16,630,993,220.00 | +2.29% |
| 24h DEX volume | 1,493,144,029.54 | 2,578,119,137.34 | +72.66% |
| 24h chain fees | 9,274,886.08 | 15,979,592.70 | +72.29% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 14.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
