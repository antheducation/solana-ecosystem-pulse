# Solana Ecosystem Pulse

**Generated:** 2026-09-08T20:23:57Z · **Schema:** `1.0.0` · **Collection time:** 29.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.30 | -0.62% |
| Market cap | $60.56B | rank #7 |
| Total value locked | $5.94B | -0.94% |
| Stablecoin supply | $16.70B | -0.27% |
| DEX volume (24h) | $2.72B | -6.33% |
| Chain fees / REV (24h) | $15.65M | +6.81% |
| Non-vote TPS (1h avg) | 2,132 | peak 4,595 total |
| Active validators | 676 | 11 delinquent |
| Epoch 1031 | 8.40% complete | 395,700 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 71 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,131.7 average over the last 60 minutes; 2,376.7 in the latest sample.
- **Total TPS:** 4,250.8 average, 4,594.9 peak. Consensus votes account for 49.9% of all transactions.
- **Slot time:** 317.3 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 423,472,222 at absolute slot 445,428,300.
- **Epoch 1031:** slot 36,300 of 432,000 (8.40% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 501 ms |
| `solana-rpc.publicnode.com` | yes | 198 ms |
| `api.mainnet.solana.com` | yes | 462 ms |

## Validators & stake

- **676 active** validators, **11 delinquent** (1.60% by count, 0.012% by stake).
- **Total stake:** 438,653,505 SOL ($45.31B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.67% of active stake.
- **Commission:** median 5.0%, mean 12.51%; 244 validators at 0% and 63 at 100%.

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

- **SOL:** $103.30 (-0.62% 24h, +3.26% 7d, +33.85% 30d). Market cap $60.56B, 24h volume $2.98B (4.92% of cap). Price source: `coingecko`.
- **TVL:** $5.94B across 341 protocols - rank #2 of 466 chains, 6.74% of all tracked chain TVL. -0.80% over 7d, -55.2% from its ATH.
- **Stablecoins:** $16.70B circulating on Solana (+4.56% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.72B in 24h, $16.29B over 7d across 121 venues. Volume/TVL turnover 0.458x per day.
- **REV (chain fees):** $15.65M in 24h, $354.24M over 30d. Retained chain revenue $6.35M (40.6% of fees). Annualised fees are 9.43% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,251,133 SOL circulating of 633,737,347 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | -0.5% | +0.3% |
| 2 | Kamino Lend | Lending | $1.36B | +2.4% | -2.4% |
| 3 | Raydium AMM | Dexs | $1.14B | +0.2% | +2.3% |
| 4 | Binance Staked SOL | Liquid Staking | $1.08B | +0.3% | +1.6% |
| 5 | Jupiter Lend | Lending | $1.08B | -0.6% | -0.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.07B | +0.3% | +2.8% |
| 7 | BlackRock BUIDL | RWA | $987.58M | +1.0% | +11.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $754.65M | +0.2% | -1.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $539.57M | +0.3% | +1.0% |
| 10 | xStocks | RWA | $444.19M | -0.7% | +0.5% |
| 11 | Marinade Native | Staking Pool | $405.76M | -1.5% | -4.2% |
| 12 | Sentora Curator | Risk Curators | $384.06M | -0.7% | +6.4% |

The top five protocols hold 36.9% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.94B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.7% · Lending 16.1% · Dexs 13.9% · RWA 13.9% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.713% of chain TVL.

- BlackRock BUIDL (RWA): $987.58M
- xStocks (RWA): $444.19M
- OnRe (RWA): $303.99M
- Solstice (Basis Trading): $237.86M
- Ondo Yield Assets (RWA): $180.08M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,023.0 unique fee payers** signed per block (1,537 distinct addresses in the union, 49.9% overlap between blocks).

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
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | pre-release |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-08
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0558: SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
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

### Change over 24h (vs run at 2026-09-07T20:51:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,930.66 | 4,250.75 | +8.14% |
| Average non-vote TPS | 1,809.47 | 2,131.65 | +17.81% |
| Average slot time (ms) | 316.70 | 317.30 | +0.19% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 5,896,988,391.00 | 5,936,538,125.00 | +0.67% |
| SOL price | 104.08 | 103.30 | -0.75% |
| Stablecoin supply | 16,741,090,548.00 | 16,696,076,448.00 | -0.27% |
| 24h DEX volume | 2,904,503,252.44 | 2,720,639,104.66 | -6.33% |
| 24h chain fees | 14,655,299.70 | 15,653,179.21 | +6.81% |

### Change over 7d (vs run at 2026-09-01T20:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,409.25 | 4,250.75 | -3.59% |
| Average non-vote TPS | 2,288.53 | 2,131.65 | -6.86% |
| Average slot time (ms) | 317.90 | 317.30 | -0.19% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 17.00 | 11.00 | -35.29% |
| Solana TVL | 5,737,476,214.00 | 5,936,538,125.00 | +3.47% |
| SOL price | 99.96 | 103.30 | +3.34% |
| Stablecoin supply | 15,969,999,346.00 | 16,696,076,448.00 | +4.55% |
| 24h DEX volume | 2,501,465,620.05 | 2,720,639,104.66 | +8.76% |
| 24h chain fees | 13,501,461.08 | 15,653,179.21 | +15.94% |

### Change over 30d (vs run at 2026-08-09T18:21:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,304.40 | 4,250.75 | -1.25% |
| Average non-vote TPS | 2,694.81 | 2,131.65 | -20.90% |
| Average slot time (ms) | 426.40 | 317.30 | -25.59% |
| Active validators | 691.00 | 676.00 | -2.17% |
| Delinquent validators | 7.00 | 11.00 | +57.14% |
| Solana TVL | 4,857,325,993.00 | 5,936,538,125.00 | +22.22% |
| SOL price | 77.09 | 103.30 | +34.00% |
| Stablecoin supply | 16,258,695,331.00 | 16,696,076,448.00 | +2.69% |
| 24h DEX volume | 1,493,144,029.54 | 2,720,639,104.66 | +82.21% |
| 24h chain fees | 9,274,886.08 | 15,653,179.21 | +68.77% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 29.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
