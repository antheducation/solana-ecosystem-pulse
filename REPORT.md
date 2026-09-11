# Solana Ecosystem Pulse

**Generated:** 2026-09-11T20:08:43Z · **Schema:** `1.0.0` · **Collection time:** 12.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.41 | +2.80% |
| Market cap | $60.07B | rank #7 |
| Total value locked | $5.88B | +0.40% |
| Stablecoin supply | $16.36B | -1.49% |
| DEX volume (24h) | $2.92B | -2.61% |
| Chain fees / REV (24h) | $14.61M | -6.98% |
| Non-vote TPS (1h avg) | 2,154 | peak 4,682 total |
| Active validators | 678 | 12 delinquent |
| Epoch 1032 | 97.22% complete | 12,026 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 78 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,154.3 average over the last 60 minutes; 2,527.5 in the latest sample.
- **Total TPS:** 4,273.4 average, 4,682.3 peak. Consensus votes account for 49.6% of all transactions.
- **Slot time:** 317.2 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 424,287,008 at absolute slot 446,243,974.
- **Epoch 1032:** slot 419,974 of 432,000 (97.22% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.654% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 108 ms |
| `solana-rpc.publicnode.com` | yes | 47 ms |
| `api.mainnet.solana.com` | yes | 109 ms |

## Validators & stake

- **678 active** validators, **12 delinquent** (1.74% by count, 0.385% by stake).
- **Total stake:** 439,188,213 SOL ($44.98B); stake rate 69.29% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 240 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.987% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.731% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.863% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.601% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.187% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,795 | 2.121% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.065% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.679% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.573% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.497% | 0% |

## Economics

- **SOL:** $102.41 (+2.80% 24h, +0.76% 7d, +35.39% 30d). Market cap $60.07B, 24h volume $4.39B (7.31% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 340 protocols - rank #2 of 467 chains, 6.66% of all tracked chain TVL. -0.86% over 7d, -55.6% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-1.62% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.92B in 24h, $18.00B over 7d across 122 venues. Volume/TVL turnover 0.497x per day.
- **REV (chain fees):** $14.61M in 24h, $371.97M over 30d. Retained chain revenue $5.78M (39.5% of fees). Annualised fees are 8.88% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,537,142 SOL circulating of 633,829,707 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | +2.1% | -1.5% |
| 2 | Kamino Lend | Lending | $1.35B | +1.9% | +1.0% |
| 3 | Raydium AMM | Dexs | $1.14B | +2.7% | +2.1% |
| 4 | Jupiter Lend | Lending | $1.08B | +0.6% | -1.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | +1.8% | -1.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | +2.0% | -0.3% |
| 7 | BlackRock BUIDL | RWA | $992.60M | +0.0% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.91M | +1.4% | -1.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $526.79M | +1.8% | -2.0% |
| 10 | Marinade Native | Staking Pool | $387.98M | +1.0% | -7.1% |
| 11 | Sentora Curator | Risk Curators | $387.49M | -0.1% | +1.0% |
| 12 | PumpSwap | Dexs | $334.67M | +4.6% | -2.1% |

The top five protocols hold 38.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.27B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.5% · Lending 16.5% · Dexs 14.3% · RWA 11.7% · Derivatives 5.1% · Staking Pool 3.7%

### Tokenised assets

$2.22B of tokenised real-world assets and equities are locked on Solana - 13.636% of chain TVL.

- BlackRock BUIDL (RWA): $992.60M
- OnRe (RWA): $294.74M
- Solstice (Basis Trading): $235.02M
- Ondo Yield Assets (RWA): $179.71M
- Huma Finance V2 (RWA): $173.85M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **956.7 unique fee payers** signed per block (1,392 distinct addresses in the union, 51.5% overlap between blocks).

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
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | pre-release |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-09-08

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

### Change over 24h (vs run at 2026-09-10T20:09:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,122.54 | 4,273.36 | +3.66% |
| Average non-vote TPS | 1,990.17 | 2,154.29 | +8.25% |
| Average slot time (ms) | 315.50 | 317.20 | +0.54% |
| Active validators | 677.00 | 678.00 | +0.15% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,779,330,766.00 | 5,878,734,141.00 | +1.72% |
| SOL price | 99.77 | 102.41 | +2.65% |
| Stablecoin supply | 16,576,239,978.00 | 16,358,198,746.00 | -1.32% |
| 24h DEX volume | 3,000,435,429.63 | 2,921,890,110.01 | -2.62% |
| 24h chain fees | 15,717,207.17 | 14,614,973.44 | -7.01% |

### Change over 7d (vs run at 2026-09-04T19:58:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,586.23 | 4,273.36 | +19.16% |
| Average non-vote TPS | 1,457.68 | 2,154.29 | +47.79% |
| Average slot time (ms) | 315.10 | 317.20 | +0.67% |
| Active validators | 678.00 | 678.00 | +0.00% |
| Delinquent validators | 17.00 | 12.00 | -29.41% |
| Solana TVL | 5,805,967,650.00 | 5,878,734,141.00 | +1.25% |
| SOL price | 101.76 | 102.41 | +0.64% |
| Stablecoin supply | 16,644,416,664.00 | 16,358,198,746.00 | -1.72% |
| 24h DEX volume | 2,459,540,363.80 | 2,921,890,110.01 | +18.80% |
| 24h chain fees | 11,820,876.49 | 14,614,973.44 | +23.64% |

### Change over 30d (vs run at 2026-08-12T18:43:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,653.97 | 4,273.36 | -8.18% |
| Average non-vote TPS | 3,053.77 | 2,154.29 | -29.45% |
| Average slot time (ms) | 422.30 | 317.20 | -24.89% |
| Active validators | 685.00 | 678.00 | -1.02% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 4,816,384,183.00 | 5,878,734,141.00 | +22.06% |
| SOL price | 75.94 | 102.41 | +34.86% |
| Stablecoin supply | 16,295,860,195.00 | 16,358,198,746.00 | +0.38% |
| 24h DEX volume | 1,650,837,789.28 | 2,921,890,110.01 | +76.99% |
| 24h chain fees | 9,976,052.23 | 14,614,973.44 | +46.50% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 11.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
