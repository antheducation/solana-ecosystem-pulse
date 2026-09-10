# Solana Ecosystem Pulse

**Generated:** 2026-09-10T01:45:34Z · **Schema:** `1.0.0` · **Collection time:** 30.6s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.93 | -2.70% |
| Market cap | $59.20B | rank #7 |
| Total value locked | $5.79B | -0.16% |
| Stablecoin supply | $16.63B | -0.40% |
| DEX volume (24h) | $2.56B | -5.73% |
| Chain fees / REV (24h) | $15.51M | -6.36% |
| Non-vote TPS (1h avg) | 1,944 | peak 4,491 total |
| Active validators | 675 | 13 delinquent |
| Epoch 1031 | 85.59% complete | 62,238 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 72 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,943.9 average over the last 60 minutes; 1,761.9 in the latest sample.
- **Total TPS:** 4,072.6 average, 4,491.2 peak. Consensus votes account for 52.3% of all transactions.
- **Slot time:** 315.6 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 423,805,184 at absolute slot 445,761,762.
- **Epoch 1031:** slot 369,762 of 432,000 (85.59% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 608 ms |
| `solana-rpc.publicnode.com` | yes | 61 ms |
| `api.mainnet.solana.com` | yes | 552 ms |

## Validators & stake

- **675 active** validators, **13 delinquent** (1.89% by count, 0.047% by stake).
- **Total stake:** 438,653,505 SOL ($44.27B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.26% and top 33 hold 45.69% of active stake.
- **Commission:** median 5.0%, mean 12.84%; 239 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,436,766 | 3.977% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,345,792 | 3.728% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,527,540 | 2.857% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,388,333 | 2.597% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,566,721 | 2.182% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,286,723 | 2.118% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,027,481 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,322,728 | 1.670% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,860,585 | 1.565% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,604,066 | 1.506% | 0% |

## Economics

- **SOL:** $100.93 (-2.70% 24h, +1.43% 7d, +33.13% 30d). Market cap $59.20B, 24h volume $3.31B (5.59% of cap). Price source: `coingecko`.
- **TVL:** $5.79B across 340 protocols - rank #2 of 466 chains, 6.62% of all tracked chain TVL. +1.38% over 7d, -56.3% from its ATH.
- **Stablecoins:** $16.63B circulating on Solana (+4.91% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.56B in 24h, $16.12B over 7d across 122 venues. Volume/TVL turnover 0.442x per day.
- **REV (chain fees):** $15.51M in 24h, $355.78M over 30d. Retained chain revenue $6.37M (41.1% of fees). Annualised fees are 9.56% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,249,975 SOL circulating of 633,736,201 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -2.0% | +2.1% |
| 2 | Kamino Lend | Lending | $1.31B | -3.6% | +6.5% |
| 3 | Raydium AMM | Dexs | $1.12B | -1.2% | +4.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.05B | -2.0% | +1.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.04B | -2.0% | +3.3% |
| 6 | Jupiter Lend | Lending | $1.04B | -5.8% | -2.6% |
| 7 | BlackRock BUIDL | RWA | $992.17M | +0.5% | +11.4% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $742.88M | -1.0% | -0.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $525.35M | -1.9% | +1.7% |
| 10 | xStocks | RWA | $436.89M | -1.5% | +0.6% |
| 11 | Marinade Native | Staking Pool | $389.40M | -3.4% | -2.8% |
| 12 | Sentora Curator | Risk Curators | $386.94M | +0.6% | +6.5% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.60B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 15.8% · RWA 14.1% · Dexs 13.9% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.999% of chain TVL.

- BlackRock BUIDL (RWA): $992.17M
- xStocks (RWA): $436.89M
- OnRe (RWA): $307.15M
- Solstice (Basis Trading): $235.68M
- Ondo Yield Assets (RWA): $179.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **840.3 unique fee payers** signed per block (1,123 distinct addresses in the union, 55.5% overlap between blocks).

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

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
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

### Change over 24h (vs run at 2026-09-09T01:50:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,448.61 | 4,072.55 | -8.45% |
| Average non-vote TPS | 2,323.56 | 1,943.91 | -16.34% |
| Average slot time (ms) | 317.10 | 315.60 | -0.47% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 10.00 | 13.00 | +30.00% |
| Solana TVL | 5,949,941,999.00 | 5,785,220,596.00 | -2.77% |
| SOL price | 103.84 | 100.93 | -2.80% |
| Stablecoin supply | 16,630,993,220.00 | 16,629,480,845.00 | -0.01% |
| 24h DEX volume | 2,578,119,137.34 | 2,555,510,166.63 | -0.88% |
| 24h chain fees | 15,979,592.70 | 15,507,501.83 | -2.95% |

### Change over 7d (vs run at 2026-09-03T01:45:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,660.97 | 4,072.55 | +11.24% |
| Average non-vote TPS | 1,511.60 | 1,943.91 | +28.60% |
| Average slot time (ms) | 313.50 | 315.60 | +0.67% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,694,231,301.00 | 5,785,220,596.00 | +1.60% |
| SOL price | 100.36 | 100.93 | +0.57% |
| Stablecoin supply | 15,851,692,526.00 | 16,629,480,845.00 | +4.91% |
| 24h DEX volume | 2,328,007,156.32 | 2,555,510,166.63 | +9.77% |
| 24h chain fees | 12,127,495.07 | 15,507,501.83 | +27.87% |

### Change over 30d (vs run at 2026-08-10T18:39:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,162.64 | 4,072.55 | -2.16% |
| Average non-vote TPS | 2,537.28 | 1,943.91 | -23.39% |
| Average slot time (ms) | 422.40 | 315.60 | -25.28% |
| Active validators | 691.00 | 675.00 | -2.32% |
| Delinquent validators | 7.00 | 13.00 | +85.71% |
| Solana TVL | 4,826,095,598.00 | 5,785,220,596.00 | +19.87% |
| SOL price | 75.80 | 100.93 | +33.15% |
| Stablecoin supply | 16,312,056,347.00 | 16,629,480,845.00 | +1.95% |
| 24h DEX volume | 1,347,434,364.98 | 2,555,510,166.63 | +89.66% |
| 24h chain fees | 9,097,906.09 | 15,507,501.83 | +70.45% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 30.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
