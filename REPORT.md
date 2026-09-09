# Solana Ecosystem Pulse

**Generated:** 2026-09-09T15:25:47Z · **Schema:** `1.0.0` · **Collection time:** 30.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.20 | -1.26% |
| Market cap | $59.92B | rank #7 |
| Total value locked | $5.97B | +0.81% |
| Stablecoin supply | $16.63B | -0.40% |
| DEX volume (24h) | $2.71B | -0.36% |
| Chain fees / REV (24h) | $16.56M | +5.92% |
| Non-vote TPS (1h avg) | 2,374 | peak 6,036 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1031 | 58.47% complete | 179,415 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 72 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,374.2 average over the last 60 minutes; 2,694.2 in the latest sample.
- **Total TPS:** 4,504.5 average, 6,036.4 peak. Consensus votes account for 47.3% of all transactions.
- **Slot time:** 315.9 ms average (target 400 ms), worst 1-minute bucket 337.1 ms.
- **Block height:** 423,688,152 at absolute slot 445,644,585.
- **Epoch 1031:** slot 252,585 of 432,000 (58.47% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 461 ms |
| `solana-rpc.publicnode.com` | yes | 340 ms |
| `api.mainnet.solana.com` | yes | 454 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.422% by stake).
- **Total stake:** 438,653,505 SOL ($44.83B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 242 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,436,766 | 3.992% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,345,792 | 3.742% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,527,540 | 2.868% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,388,333 | 2.607% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,566,721 | 2.190% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,286,723 | 2.126% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,027,481 | 2.067% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,322,728 | 1.676% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,860,585 | 1.571% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,604,066 | 1.512% | 0% |

## Economics

- **SOL:** $102.20 (-1.26% 24h, +3.36% 7d, +34.11% 30d). Market cap $59.92B, 24h volume $2.97B (4.95% of cap). Price source: `coingecko`.
- **TVL:** $5.97B across 340 protocols - rank #2 of 466 chains, 6.73% of all tracked chain TVL. +5.51% over 7d, -54.9% from its ATH.
- **Stablecoins:** $16.63B circulating on Solana (+4.91% 7d) - $2.79 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.71B in 24h, $16.83B over 7d across 121 venues. Volume/TVL turnover 0.454x per day.
- **REV (chain fees):** $16.56M in 24h, $361.78M over 30d. Retained chain revenue $6.74M (40.7% of fees). Annualised fees are 10.09% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,250,392 SOL circulating of 633,736,618 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | +0.9% | +3.7% |
| 2 | Kamino Lend | Lending | $1.36B | +2.2% | +12.3% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.3% | +6.5% |
| 4 | Jupiter Lend | Lending | $1.10B | +3.4% | +5.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | +1.3% | +4.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | +0.7% | +5.8% |
| 7 | BlackRock BUIDL | RWA | $987.58M | +1.0% | +11.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $755.14M | +1.2% | +1.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $537.88M | +1.3% | +4.2% |
| 10 | xStocks | RWA | $442.49M | +0.2% | +2.4% |
| 11 | Marinade Native | Staking Pool | $403.92M | +1.1% | +1.5% |
| 12 | Sentora Curator | Risk Curators | $386.34M | -0.3% | +6.5% |

The top five protocols hold 37.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.95B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.1% · Dexs 14.0% · RWA 13.9% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.703% of chain TVL.

- BlackRock BUIDL (RWA): $987.58M
- xStocks (RWA): $442.49M
- OnRe (RWA): $305.13M
- Solstice (Basis Trading): $235.70M
- Ondo Yield Assets (RWA): $180.08M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,012.7 unique fee payers** signed per block (1,526 distinct addresses in the union, 49.8% overlap between blocks).

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

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-09-08
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

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

### Change over 24h (vs run at 2026-09-08T15:29:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,461.84 | 4,504.48 | +0.96% |
| Average non-vote TPS | 2,356.32 | 2,374.24 | +0.76% |
| Average slot time (ms) | 318.60 | 315.90 | -0.85% |
| Active validators | 675.00 | 676.00 | +0.15% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,858,003,246.00 | 5,967,895,613.00 | +1.88% |
| SOL price | 103.44 | 102.20 | -1.20% |
| Stablecoin supply | 16,694,571,293.00 | 16,629,871,831.00 | -0.39% |
| 24h DEX volume | 2,720,639,104.66 | 2,710,734,376.34 | -0.36% |
| 24h chain fees | 15,653,179.21 | 16,561,493.38 | +5.80% |

### Change over 7d (vs run at 2026-09-02T15:26:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,963.51 | 4,504.48 | +13.65% |
| Average non-vote TPS | 1,822.14 | 2,374.24 | +30.30% |
| Average slot time (ms) | 314.80 | 315.90 | +0.35% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 18.00 | 12.00 | -33.33% |
| Solana TVL | 5,622,784,841.00 | 5,967,895,613.00 | +6.14% |
| SOL price | 98.97 | 102.20 | +3.26% |
| Stablecoin supply | 15,849,987,390.00 | 16,629,871,831.00 | +4.92% |
| 24h DEX volume | 2,171,560,050.49 | 2,710,734,376.34 | +24.83% |
| 24h chain fees | 12,641,815.67 | 16,561,493.38 | +31.01% |

### Change over 30d (vs run at 2026-08-10T18:39:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,162.64 | 4,504.48 | +8.21% |
| Average non-vote TPS | 2,537.28 | 2,374.24 | -6.43% |
| Average slot time (ms) | 422.40 | 315.90 | -25.21% |
| Active validators | 691.00 | 676.00 | -2.17% |
| Delinquent validators | 7.00 | 12.00 | +71.43% |
| Solana TVL | 4,826,095,598.00 | 5,967,895,613.00 | +23.66% |
| SOL price | 75.80 | 102.20 | +34.83% |
| Stablecoin supply | 16,312,056,347.00 | 16,629,871,831.00 | +1.95% |
| 24h DEX volume | 1,347,434,364.98 | 2,710,734,376.34 | +101.18% |
| 24h chain fees | 9,097,906.09 | 16,561,493.38 | +82.04% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 30.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
