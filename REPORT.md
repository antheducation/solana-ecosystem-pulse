# Solana Ecosystem Pulse

**Generated:** 2026-09-12T01:50:00Z · **Schema:** `1.0.0` · **Collection time:** 27.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.10 | +2.99% |
| Market cap | $59.89B | rank #7 |
| Total value locked | $5.91B | +0.06% |
| Stablecoin supply | $16.55B | +1.19% |
| DEX volume (24h) | $3.25B | +11.21% |
| Chain fees / REV (24h) | $16.60M | +13.56% |
| Non-vote TPS (1h avg) | 1,649 | peak 4,053 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1033 | 12.18% complete | 379,387 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 78 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,649.2 average over the last 60 minutes; 1,836.4 in the latest sample.
- **Total TPS:** 3,774.0 average, 4,053.5 peak. Consensus votes account for 56.3% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 333.3 ms.
- **Block height:** 424,351,445 at absolute slot 446,308,613.
- **Epoch 1033:** slot 52,613 of 432,000 (12.18% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.652% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 781 ms |
| `solana-rpc.publicnode.com` | yes | 84 ms |
| `api.mainnet.solana.com` | yes | 534 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.389% by stake).
- **Total stake:** 436,837,681 SOL ($44.60B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.49% and top 33 hold 46.09% of active stake.
- **Commission:** median 5.0%, mean 12.52%; 242 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,557,397 | 4.035% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,359,842 | 3.760% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,516,388 | 2.876% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,367,276 | 2.612% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,667,435 | 2.222% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,234,081 | 2.122% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,021,415 | 2.073% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,357,834 | 1.691% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,941,562 | 1.595% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,551,099 | 1.506% | 0% |

## Economics

- **SOL:** $102.10 (+2.99% 24h, +0.24% 7d, +35.12% 30d). Market cap $59.89B, 24h volume $4.57B (7.64% of cap). Price source: `coingecko`.
- **TVL:** $5.91B across 340 protocols - rank #2 of 467 chains, 6.69% of all tracked chain TVL. +0.58% over 7d, -55.4% from its ATH.
- **Stablecoins:** $16.55B circulating on Solana (-0.32% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.25B in 24h, $17.98B over 7d across 122 venues. Volume/TVL turnover 0.550x per day.
- **REV (chain fees):** $16.60M in 24h, $367.77M over 30d. Retained chain revenue $6.42M (38.7% of fees). Annualised fees are 10.12% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,633,260 SOL circulating of 633,924,536 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.57B | +3.3% | +0.8% |
| 2 | Kamino Lend | Lending | $1.35B | +3.5% | +1.8% |
| 3 | Raydium AMM | Dexs | $1.15B | +3.0% | +3.7% |
| 4 | Jupiter Lend | Lending | $1.10B | +3.2% | +0.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | +3.3% | +0.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | +3.1% | +1.6% |
| 7 | BlackRock BUIDL | RWA | $992.60M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.51M | +1.8% | -0.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $529.55M | +3.3% | +0.6% |
| 10 | Marinade Native | Staking Pool | $390.49M | +2.3% | -5.2% |
| 11 | Sentora Curator | Risk Curators | $387.55M | -0.1% | -1.3% |
| 12 | PumpSwap | Dexs | $329.67M | +1.4% | -1.9% |

The top five protocols hold 38.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.37B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.4% · Lending 16.6% · Dexs 14.2% · RWA 11.8% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.644% of chain TVL.

- BlackRock BUIDL (RWA): $992.60M
- OnRe (RWA): $294.84M
- Solstice (Basis Trading): $235.02M
- Huma Finance V2 (RWA): $191.04M
- Ondo Yield Assets (RWA): $180.11M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,055.3 unique fee payers** signed per block (1,686 distinct addresses in the union, 46.7% overlap between blocks).

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

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
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

### Change over 24h (vs run at 2026-09-11T01:44:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,820.46 | 3,774.03 | -1.22% |
| Average non-vote TPS | 1,687.31 | 1,649.21 | -2.26% |
| Average slot time (ms) | 315.10 | 316.10 | +0.32% |
| Active validators | 675.00 | 677.00 | +0.30% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 5,753,733,189.00 | 5,906,350,849.00 | +2.65% |
| SOL price | 98.76 | 102.10 | +3.38% |
| Stablecoin supply | 16,358,256,053.00 | 16,554,576,484.00 | +1.20% |
| 24h DEX volume | 2,947,608,342.01 | 3,249,433,436.43 | +10.24% |
| 24h chain fees | 14,677,343.47 | 16,596,146.14 | +13.07% |

### Change over 7d (vs run at 2026-09-05T01:40:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,469.92 | 3,774.03 | +8.76% |
| Average non-vote TPS | 1,340.66 | 1,649.21 | +23.01% |
| Average slot time (ms) | 314.50 | 316.10 | +0.51% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 18.00 | 12.00 | -33.33% |
| Solana TVL | 5,858,132,654.00 | 5,906,350,849.00 | +0.82% |
| SOL price | 102.06 | 102.10 | +0.04% |
| Stablecoin supply | 16,645,882,037.00 | 16,554,576,484.00 | -0.55% |
| 24h DEX volume | 1,848,928,416.00 | 3,249,433,436.43 | +75.75% |
| 24h chain fees | 10,602,054.70 | 16,596,146.14 | +56.54% |

### Change over 30d (vs run at 2026-08-12T18:43:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,653.97 | 3,774.03 | -18.91% |
| Average non-vote TPS | 3,053.77 | 1,649.21 | -45.99% |
| Average slot time (ms) | 422.30 | 316.10 | -25.15% |
| Active validators | 685.00 | 677.00 | -1.17% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 4,816,384,183.00 | 5,906,350,849.00 | +22.63% |
| SOL price | 75.94 | 102.10 | +34.45% |
| Stablecoin supply | 16,295,860,195.00 | 16,554,576,484.00 | +1.59% |
| 24h DEX volume | 1,650,837,789.28 | 3,249,433,436.43 | +96.84% |
| 24h chain fees | 9,976,052.23 | 16,596,146.14 | +66.36% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
