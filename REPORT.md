# Solana Ecosystem Pulse

**Generated:** 2026-09-09T10:14:14Z · **Schema:** `1.0.0` · **Collection time:** 27.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.79 | +0.18% |
| Market cap | $60.84B | rank #7 |
| Total value locked | $5.99B | +1.13% |
| Stablecoin supply | $16.63B | -0.40% |
| DEX volume (24h) | $2.58B | -5.25% |
| Chain fees / REV (24h) | $16.44M | +5.16% |
| Non-vote TPS (1h avg) | 1,718 | peak 4,309 total |
| Active validators | 677 | 10 delinquent |
| Epoch 1031 | 44.79% complete | 238,487 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 72 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,717.9 average over the last 60 minutes; 1,706.5 in the latest sample.
- **Total TPS:** 3,846.2 average, 4,308.9 peak. Consensus votes account for 55.3% of all transactions.
- **Slot time:** 316.2 ms average (target 400 ms), worst 1-minute bucket 324.3 ms.
- **Block height:** 423,629,116 at absolute slot 445,585,513.
- **Epoch 1031:** slot 193,513 of 432,000 (44.79% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 460 ms |
| `solana-rpc.publicnode.com` | yes | 341 ms |
| `api.mainnet.solana.com` | yes | 439 ms |

## Validators & stake

- **677 active** validators, **10 delinquent** (1.46% by count, 0.007% by stake).
- **Total stake:** 438,653,505 SOL ($45.53B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.67% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 244 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,436,766 | 3.975% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,345,792 | 3.727% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,527,540 | 2.856% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,388,333 | 2.596% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,566,721 | 2.181% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,286,723 | 2.117% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,027,481 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,322,728 | 1.669% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,860,585 | 1.564% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,604,066 | 1.506% | 0% |

## Economics

- **SOL:** $103.79 (+0.18% 24h, +5.28% 7d, +35.65% 30d). Market cap $60.84B, 24h volume $2.81B (4.63% of cap). Price source: `coingecko`.
- **TVL:** $5.99B across 340 protocols - rank #2 of 466 chains, 6.76% of all tracked chain TVL. +5.85% over 7d, -54.8% from its ATH.
- **Stablecoins:** $16.63B circulating on Solana (+4.91% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.58B in 24h, $15.86B over 7d across 121 venues. Volume/TVL turnover 0.431x per day.
- **REV (chain fees):** $16.44M in 24h, $359.85M over 30d. Retained chain revenue $6.63M (40.3% of fees). Annualised fees are 9.86% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,250,596 SOL circulating of 633,736,822 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | +2.2% | +5.1% |
| 2 | Kamino Lend | Lending | $1.36B | +2.4% | +12.9% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.7% | +6.3% |
| 4 | Jupiter Lend | Lending | $1.11B | +2.5% | +6.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | +1.9% | +5.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.08B | +1.9% | +7.2% |
| 7 | BlackRock BUIDL | RWA | $987.58M | +1.0% | +11.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $759.64M | +1.5% | +2.0% |
| 9 | Jupiter Staked SOL | Liquid Staking | $542.66M | +1.8% | +5.2% |
| 10 | xStocks | RWA | $443.55M | +0.4% | +2.7% |
| 11 | Marinade Native | Staking Pool | $407.50M | +0.4% | +2.4% |
| 12 | Sentora Curator | Risk Curators | $386.00M | -0.3% | +6.5% |

The top five protocols hold 37.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $17.05B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.8% · Lending 16.2% · Dexs 13.9% · RWA 13.8% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.604% of chain TVL.

- BlackRock BUIDL (RWA): $987.58M
- xStocks (RWA): $443.55M
- OnRe (RWA): $304.56M
- Solstice (Basis Trading): $235.70M
- Ondo Yield Assets (RWA): $180.11M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,027.3 unique fee payers** signed per block (1,607 distinct addresses in the union, 47.9% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-08T10:11:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,448.21 | 3,846.21 | +11.54% |
| Average non-vote TPS | 1,336.54 | 1,717.92 | +28.53% |
| Average slot time (ms) | 315.40 | 316.20 | +0.25% |
| Active validators | 675.00 | 677.00 | +0.30% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 5,869,138,160.00 | 5,987,012,086.00 | +2.01% |
| SOL price | 103.55 | 103.79 | +0.23% |
| Stablecoin supply | 16,695,009,953.00 | 16,629,962,371.00 | -0.39% |
| 24h DEX volume | 2,872,025,884.66 | 2,577,833,806.34 | -10.24% |
| 24h chain fees | 15,999,657.21 | 16,439,615.38 | +2.75% |

### Change over 7d (vs run at 2026-09-02T10:03:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,149.23 | 3,846.21 | +22.13% |
| Average non-vote TPS | 1,014.87 | 1,717.92 | +69.27% |
| Average slot time (ms) | 315.10 | 316.20 | +0.35% |
| Active validators | 673.00 | 677.00 | +0.59% |
| Delinquent validators | 22.00 | 10.00 | -54.55% |
| Solana TVL | 5,706,889,294.00 | 5,987,012,086.00 | +4.91% |
| SOL price | 98.48 | 103.79 | +5.39% |
| Stablecoin supply | 15,850,556,625.00 | 16,629,962,371.00 | +4.92% |
| 24h DEX volume | 2,246,687,191.49 | 2,577,833,806.34 | +14.74% |
| 24h chain fees | 12,266,833.67 | 16,439,615.38 | +34.02% |

### Change over 30d (vs run at 2026-08-10T18:39:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,162.64 | 3,846.21 | -7.60% |
| Average non-vote TPS | 2,537.28 | 1,717.92 | -32.29% |
| Average slot time (ms) | 422.40 | 316.20 | -25.14% |
| Active validators | 691.00 | 677.00 | -2.03% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,826,095,598.00 | 5,987,012,086.00 | +24.05% |
| SOL price | 75.80 | 103.79 | +36.93% |
| Stablecoin supply | 16,312,056,347.00 | 16,629,962,371.00 | +1.95% |
| 24h DEX volume | 1,347,434,364.98 | 2,577,833,806.34 | +91.31% |
| 24h chain fees | 9,097,906.09 | 16,439,615.38 | +80.70% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
