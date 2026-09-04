# Solana Ecosystem Pulse

**Generated:** 2026-09-04T15:16:43Z · **Schema:** `1.0.0` · **Collection time:** 20.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.02 | -3.26% |
| Market cap | $59.11B | rank #7 |
| Total value locked | $5.89B | +3.24% |
| Stablecoin supply | $16.64B | +3.36% |
| DEX volume (24h) | $2.46B | +7.44% |
| Chain fees / REV (24h) | $11.82M | +4.90% |
| Non-vote TPS (1h avg) | 2,462 | peak 5,119 total |
| Active validators | 676 | 18 delinquent |
| Epoch 1028 | 41.91% complete | 250,961 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 67 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.4% in 24h) | Stablecoin supply changed +3.4% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,461.8 average over the last 60 minutes; 2,188.2 in the latest sample.
- **Total TPS:** 4,567.9 average, 5,118.9 peak. Consensus votes account for 46.1% of all transactions.
- **Slot time:** 318.1 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 422,322,794 at absolute slot 444,277,039.
- **Epoch 1028:** slot 181,039 of 432,000 (41.91% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.664% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 285 ms |
| `solana-rpc.publicnode.com` | yes | 144 ms |
| `api.mainnet.solana.com` | yes | 247 ms |

## Validators & stake

- **676 active** validators, **18 delinquent** (2.59% by count, 0.032% by stake).
- **Total stake:** 436,898,866 SOL ($44.14B); stake rate 68.97% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.22%; 245 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,393,318 | 3.982% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,259 | 3.738% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,459,602 | 2.853% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,379,843 | 2.606% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,567,623 | 2.191% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,278,151 | 2.124% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,042,760 | 2.070% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,376,879 | 1.689% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,127,366 | 1.632% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,593,517 | 1.510% | 0% |

## Economics

- **SOL:** $101.02 (-3.26% 24h, -5.03% 7d, +36.68% 30d). Market cap $59.11B, 24h volume $4.17B (7.05% of cap). Price source: `coingecko`.
- **TVL:** $5.89B across 342 protocols - rank #2 of 465 chains, 6.68% of all tracked chain TVL. -2.11% over 7d, -55.5% from its ATH.
- **Stablecoins:** $16.64B circulating on Solana (+2.59% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.46B in 24h, $15.61B over 7d across 121 venues. Volume/TVL turnover 0.417x per day.
- **REV (chain fees):** $11.82M in 24h, $337.80M over 30d. Retained chain revenue $4.61M (39.0% of fees). Annualised fees are 7.30% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,360,223 SOL circulating of 633,455,248 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | +2.6% | -5.2% |
| 2 | Kamino Lend | Lending | $1.32B | +1.8% | +5.5% |
| 3 | Raydium AMM | Dexs | $1.12B | +2.4% | -3.1% |
| 4 | Jupiter Lend | Lending | $1.07B | -0.8% | -4.6% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | +3.3% | -4.1% |
| 6 | Binance Staked SOL | Liquid Staking | $1.05B | +0.2% | -6.5% |
| 7 | BlackRock BUIDL | RWA | $937.81M | +5.3% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $766.14M | +1.8% | -3.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $538.13M | +2.5% | -5.3% |
| 10 | xStocks | RWA | $458.20M | +4.4% | +3.8% |
| 11 | Marinade Native | Staking Pool | $420.60M | +3.2% | -5.8% |
| 12 | Sentora | Risk Curators | $381.60M | +0.6% | +5.6% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 342 protocols the total is $16.75B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.9% · Lending 16.0% · Dexs 13.9% · RWA 12.9% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.48B of tokenised real-world assets and equities are locked on Solana - 14.777% of chain TVL.

- BlackRock BUIDL (RWA): $937.81M
- xStocks (RWA): $458.20M
- OnRe (RWA): $296.87M
- Solstice (Basis Trading): $237.93M
- Ondo Yield Assets (RWA): $179.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **999.7 unique fee payers** signed per block (1,521 distinct addresses in the union, 49.3% overlap between blocks).

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
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Current Leader Sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-03
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

### Change over 24h (vs run at 2026-09-03T15:21:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.55 | 4,567.87 | +0.05% |
| Average non-vote TPS | 2,450.75 | 2,461.79 | +0.45% |
| Average slot time (ms) | 316.50 | 318.10 | +0.51% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 19.00 | 18.00 | -5.26% |
| Solana TVL | 5,816,129,783.00 | 5,892,160,568.00 | +1.31% |
| SOL price | 104.35 | 101.02 | -3.19% |
| Stablecoin supply | 16,104,456,527.00 | 16,643,633,899.00 | +3.35% |
| 24h DEX volume | 2,289,285,889.32 | 2,459,540,363.80 | +7.44% |
| 24h chain fees | 10,535,900.15 | 11,819,564.49 | +12.18% |

### Change over 7d (vs run at 2026-08-28T17:47:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,145.52 | 4,567.87 | -11.23% |
| Average non-vote TPS | 3,011.73 | 2,461.79 | -18.26% |
| Average slot time (ms) | 321.30 | 318.10 | -1.00% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 9.00 | 18.00 | +100.00% |
| Solana TVL | 5,895,133,114.00 | 5,892,160,568.00 | -0.05% |
| SOL price | 104.55 | 101.02 | -3.38% |
| Stablecoin supply | 16,380,565,155.00 | 16,643,633,899.00 | +1.61% |
| 24h DEX volume | 3,700,129,857.54 | 2,459,540,363.80 | -33.53% |
| 24h chain fees | 16,302,758.52 | 11,819,564.49 | -27.50% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,567.87 | +16.10% |
| Average non-vote TPS | 2,312.46 | 2,461.79 | +6.46% |
| Average slot time (ms) | 424.10 | 318.10 | -24.99% |
| Active validators | 692.00 | 676.00 | -2.31% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,892,160,568.00 | +24.31% |
| SOL price | 72.81 | 101.02 | +38.74% |
| Stablecoin supply | 16,197,749,831.00 | 16,643,633,899.00 | +2.75% |
| 24h DEX volume | 1,636,927,091.91 | 2,459,540,363.80 | +50.25% |
| 24h chain fees | 7,777,648.77 | 11,819,564.49 | +51.97% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 20.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
