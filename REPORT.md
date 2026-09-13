# Solana Ecosystem Pulse

**Generated:** 2026-09-13T01:41:21Z · **Schema:** `1.0.0` · **Collection time:** 26.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.91 | -0.10% |
| Market cap | $59.78B | rank #7 |
| Total value locked | $5.90B | +0.02% |
| Stablecoin supply | $16.53B | -0.17% |
| DEX volume (24h) | $2.47B | -22.28% |
| Chain fees / REV (24h) | $15.27M | -14.60% |
| Non-vote TPS (1h avg) | 1,468 | peak 4,059 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1033 | 74.94% complete | 108,276 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 80 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,468.1 average over the last 60 minutes; 1,714.2 in the latest sample.
- **Total TPS:** 3,596.7 average, 4,059.3 peak. Consensus votes account for 59.2% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 424,622,440 at absolute slot 446,579,724.
- **Epoch 1033:** slot 323,724 of 432,000 (74.94% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.652% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 563 ms |
| `solana-rpc.publicnode.com` | yes | 129 ms |
| `api.mainnet.solana.com` | yes | 515 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.419% by stake).
- **Total stake:** 436,837,681 SOL ($44.52B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.50% and top 33 hold 46.10% of active stake.
- **Commission:** median 5.0%, mean 12.95%; 241 validators at 0% and 66 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,557,397 | 4.036% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,359,842 | 3.761% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,516,388 | 2.877% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,367,276 | 2.613% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,667,435 | 2.222% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,234,081 | 2.123% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,021,415 | 2.074% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,357,834 | 1.691% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,941,562 | 1.596% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,551,099 | 1.506% | 0% |

## Economics

- **SOL:** $101.91 (-0.10% 24h, -1.37% 7d, +34.08% 30d). Market cap $59.78B, 24h volume $1.85B (3.10% of cap). Price source: `coingecko`.
- **TVL:** $5.90B across 340 protocols - rank #2 of 467 chains, 6.67% of all tracked chain TVL. -0.28% over 7d, -55.4% from its ATH.
- **Stablecoins:** $16.53B circulating on Solana (-0.95% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.47B in 24h, $18.59B over 7d across 122 venues. Volume/TVL turnover 0.419x per day.
- **REV (chain fees):** $15.27M in 24h, $376.08M over 30d. Retained chain revenue $5.92M (38.8% of fees). Annualised fees are 9.32% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,644,937 SOL circulating of 633,923,714 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -0.4% | -0.1% |
| 2 | Kamino Lend | Lending | $1.35B | +0.5% | +2.3% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.6% | +3.0% |
| 4 | Jupiter Lend | Lending | $1.10B | +1.8% | +0.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | -0.7% | -0.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | -0.4% | +0.7% |
| 7 | BlackRock BUIDL | RWA | $992.60M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.27M | +0.1% | -0.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $524.86M | -0.7% | -0.3% |
| 10 | Sentora Curator | Risk Curators | $389.53M | +0.6% | -0.8% |
| 11 | Marinade Native | Staking Pool | $386.99M | -0.7% | -6.1% |
| 12 | PumpSwap | Dexs | $333.01M | +1.6% | -0.9% |

The top five protocols hold 38.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.30B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.2% · Lending 16.6% · Dexs 14.2% · RWA 11.8% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.702% of chain TVL.

- BlackRock BUIDL (RWA): $992.60M
- OnRe (RWA): $295.64M
- Solstice (Basis Trading): $235.02M
- Huma Finance V2 (RWA): $192.49M
- Ondo Yield Assets (RWA): $179.93M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **924.7 unique fee payers** signed per block (1,313 distinct addresses in the union, 52.7% overlap between blocks).

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

- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-12
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08

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

### Change over 24h (vs run at 2026-09-12T01:50:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,774.03 | 3,596.70 | -4.70% |
| Average non-vote TPS | 1,649.21 | 1,468.09 | -10.98% |
| Average slot time (ms) | 316.10 | 316.10 | +0.00% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 5,906,350,849.00 | 5,902,475,260.00 | -0.07% |
| SOL price | 102.10 | 101.91 | -0.19% |
| Stablecoin supply | 16,554,576,484.00 | 16,527,129,251.00 | -0.17% |
| 24h DEX volume | 3,249,433,436.43 | 2,474,258,713.08 | -23.86% |
| 24h chain fees | 16,596,146.14 | 15,265,567.51 | -8.02% |

### Change over 7d (vs run at 2026-09-06T01:34:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,370.60 | 3,596.70 | +6.71% |
| Average non-vote TPS | 1,244.13 | 1,468.09 | +18.00% |
| Average slot time (ms) | 316.40 | 316.10 | -0.09% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 17.00 | 13.00 | -23.53% |
| Solana TVL | 5,888,838,292.00 | 5,902,475,260.00 | +0.23% |
| SOL price | 103.57 | 101.91 | -1.60% |
| Stablecoin supply | 16,607,547,915.00 | 16,527,129,251.00 | -0.48% |
| 24h DEX volume | 1,960,570,598.81 | 2,474,258,713.08 | +26.20% |
| 24h chain fees | 10,088,304.07 | 15,265,567.51 | +51.32% |

### Change over 30d (vs run at 2026-08-13T18:44:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,039.13 | 3,596.70 | -10.95% |
| Average non-vote TPS | 2,403.37 | 1,468.09 | -38.92% |
| Average slot time (ms) | 416.90 | 316.10 | -24.18% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 9.00 | 13.00 | +44.44% |
| Solana TVL | 4,832,030,854.00 | 5,902,475,260.00 | +22.15% |
| SOL price | 75.68 | 101.91 | +34.66% |
| Stablecoin supply | 16,079,315,270.00 | 16,527,129,251.00 | +2.79% |
| 24h DEX volume | 1,725,631,800.93 | 2,474,258,713.08 | +43.38% |
| 24h chain fees | 9,673,605.00 | 15,265,567.51 | +57.81% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 26.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
