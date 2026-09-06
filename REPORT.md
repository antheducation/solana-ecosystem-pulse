# Solana Ecosystem Pulse

**Generated:** 2026-09-06T01:34:12Z · **Schema:** `1.0.0` · **Collection time:** 32.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.57 | +1.49% |
| Market cap | $60.63B | rank #7 |
| Total value locked | $5.89B | -0.52% |
| Stablecoin supply | $16.61B | -0.23% |
| DEX volume (24h) | $1.96B | +4.19% |
| Chain fees / REV (24h) | $10.09M | -3.33% |
| Non-vote TPS (1h avg) | 1,244 | peak 4,026 total |
| Active validators | 676 | 17 delinquent |
| Epoch 1029 | 32.59% complete | 291,217 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 68 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,244.1 average over the last 60 minutes; 1,241.1 in the latest sample.
- **Total TPS:** 3,370.6 average, 4,026.2 peak. Consensus votes account for 63.1% of all transactions.
- **Slot time:** 316.4 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 422,713,181 at absolute slot 444,668,783.
- **Epoch 1029:** slot 140,783 of 432,000 (32.59% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.661% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 737 ms |
| `solana-rpc.publicnode.com` | yes | 91 ms |
| `api.mainnet.solana.com` | yes | 707 ms |

## Validators & stake

- **676 active** validators, **17 delinquent** (2.45% by count, 0.018% by stake).
- **Total stake:** 439,248,820 SOL ($45.49B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.49%; 246 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,421,941 | 3.967% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,321,581 | 3.716% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,507,097 | 2.848% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,374,756 | 2.590% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,561,892 | 2.177% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,268,042 | 2.110% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,037,668 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,352,604 | 1.674% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,128,761 | 1.623% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,594,606 | 1.502% | 0% |

## Economics

- **SOL:** $103.57 (+1.49% 24h, -1.62% 7d, +42.65% 30d). Market cap $60.63B, 24h volume $2.44B (4.03% of cap). Price source: `coingecko`.
- **TVL:** $5.89B across 340 protocols - rank #2 of 466 chains, 6.70% of all tracked chain TVL. +0.33% over 7d, -55.5% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+2.60% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.96B in 24h, $14.51B over 7d across 121 venues. Volume/TVL turnover 0.333x per day.
- **REV (chain fees):** $10.09M in 24h, $334.35M over 30d. Retained chain revenue $4.50M (44.6% of fees). Annualised fees are 6.07% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,445,526 SOL circulating of 633,549,401 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | +1.6% | -1.7% |
| 2 | Kamino Lend | Lending | $1.33B | +0.4% | +5.7% |
| 3 | Raydium AMM | Dexs | $1.12B | +1.5% | -1.3% |
| 4 | Jupiter Lend | Lending | $1.10B | +0.8% | +0.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.07B | +1.4% | -1.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | +2.0% | -0.1% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +0.0% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $756.25M | +0.7% | -2.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $535.00M | +1.6% | -2.2% |
| 10 | xStocks | RWA | $449.76M | +0.4% | +3.5% |
| 11 | Marinade Native | Staking Pool | $408.02M | -1.0% | -5.2% |
| 12 | Sentora Curator | Risk Curators | $391.01M | -0.4% | +8.3% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.97B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.4% · Lending 15.9% · RWA 13.9% · Dexs 13.8% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.68B of tokenised real-world assets and equities are locked on Solana - 15.765% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $449.76M
- OnRe (RWA): $299.10M
- Solstice (Basis Trading): $237.94M
- Huma Finance V2 (RWA): $190.42M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **904.7 unique fee payers** signed per block (1,280 distinct addresses in the union, 52.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) - Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | pre-release |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31

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

### Change over 24h (vs run at 2026-09-05T01:40:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,469.92 | 3,370.60 | -2.86% |
| Average non-vote TPS | 1,340.66 | 1,244.13 | -7.20% |
| Average slot time (ms) | 314.50 | 316.40 | +0.60% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 18.00 | 17.00 | -5.56% |
| Solana TVL | 5,858,132,654.00 | 5,888,838,292.00 | +0.52% |
| SOL price | 102.06 | 103.57 | +1.48% |
| Stablecoin supply | 16,645,882,037.00 | 16,607,547,915.00 | -0.23% |
| 24h DEX volume | 1,848,928,416.00 | 1,960,570,598.81 | +6.04% |
| 24h chain fees | 10,602,054.70 | 10,088,304.07 | -4.85% |

### Change over 7d (vs run at 2026-08-30T02:00:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,858.12 | 3,370.60 | -12.64% |
| Average non-vote TPS | 1,702.15 | 1,244.13 | -26.91% |
| Average slot time (ms) | 317.60 | 316.40 | -0.38% |
| Active validators | 686.00 | 676.00 | -1.46% |
| Delinquent validators | 11.00 | 17.00 | +54.55% |
| Solana TVL | 5,910,477,808.00 | 5,888,838,292.00 | -0.37% |
| SOL price | 105.15 | 103.57 | -1.50% |
| Stablecoin supply | 16,345,475,515.00 | 16,607,547,915.00 | +1.60% |
| 24h DEX volume | 1,813,165,645.31 | 1,960,570,598.81 | +8.13% |
| 24h chain fees | 11,721,762.05 | 10,088,304.07 | -13.94% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,370.60 | -14.33% |
| Average non-vote TPS | 2,312.46 | 1,244.13 | -46.20% |
| Average slot time (ms) | 424.10 | 316.40 | -25.39% |
| Active validators | 692.00 | 676.00 | -2.31% |
| Delinquent validators | 8.00 | 17.00 | +112.50% |
| Solana TVL | 4,740,035,266.00 | 5,888,838,292.00 | +24.24% |
| SOL price | 72.81 | 103.57 | +42.25% |
| Stablecoin supply | 16,197,749,831.00 | 16,607,547,915.00 | +2.53% |
| 24h DEX volume | 1,636,927,091.91 | 1,960,570,598.81 | +19.77% |
| 24h chain fees | 7,777,648.77 | 10,088,304.07 | +29.71% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 32.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
