# Solana Ecosystem Pulse

**Generated:** 2026-09-05T01:40:21Z · **Schema:** `1.0.0` · **Collection time:** 11.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.06 | -1.38% |
| Market cap | $59.74B | rank #7 |
| Total value locked | $5.86B | -0.33% |
| Stablecoin supply | $16.65B | +3.37% |
| DEX volume (24h) | $1.85B | -24.83% |
| Chain fees / REV (24h) | $10.60M | -10.31% |
| Non-vote TPS (1h avg) | 1,341 | peak 3,805 total |
| Active validators | 677 | 18 delinquent |
| Epoch 1028 | 69.40% complete | 132,209 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 67 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.4% in 24h) | Stablecoin supply changed +3.4% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,340.7 average over the last 60 minutes; 1,214.3 in the latest sample.
- **Total TPS:** 3,469.9 average, 3,805.3 peak. Consensus votes account for 61.4% of all transactions.
- **Slot time:** 314.5 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 422,440,872 at absolute slot 444,395,791.
- **Epoch 1028:** slot 299,791 of 432,000 (69.40% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.664% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 70 ms |
| `solana-rpc.publicnode.com` | yes | 32 ms |
| `api.mainnet.solana.com` | yes | 71 ms |

## Validators & stake

- **677 active** validators, **18 delinquent** (2.59% by count, 0.032% by stake).
- **Total stake:** 436,898,866 SOL ($44.59B); stake rate 68.97% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 244 validators at 0% and 63 at 100%.

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

- **SOL:** $102.06 (-1.38% 24h, -1.77% 7d, +37.89% 30d). Market cap $59.74B, 24h volume $3.26B (5.46% of cap). Price source: `coingecko`.
- **TVL:** $5.86B across 341 protocols - rank #2 of 465 chains, 6.73% of all tracked chain TVL. -0.20% over 7d, -55.8% from its ATH.
- **Stablecoins:** $16.65B circulating on Solana (+2.61% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.85B in 24h, $14.32B over 7d across 121 venues. Volume/TVL turnover 0.316x per day.
- **REV (chain fees):** $10.60M in 24h, $336.97M over 30d. Retained chain revenue $4.19M (39.5% of fees). Annualised fees are 6.48% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,359,870 SOL circulating of 633,454,895 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -1.9% | -2.2% |
| 2 | Kamino Lend | Lending | $1.32B | -0.9% | +5.6% |
| 3 | Raydium AMM | Dexs | $1.10B | -1.9% | -1.5% |
| 4 | Jupiter Lend | Lending | $1.09B | -0.1% | +0.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -1.6% | -1.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | -1.4% | -1.1% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +4.3% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $750.96M | -1.9% | -2.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $526.67M | -2.0% | -2.7% |
| 10 | xStocks | RWA | $448.12M | -3.0% | +3.6% |
| 11 | Marinade Native | Staking Pool | $412.04M | -1.4% | -3.1% |
| 12 | Sentora Curator | Risk Curators | $392.49M | +2.3% | +8.7% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.72B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.4% · Lending 16.1% · RWA 14.1% · Dexs 13.8% · Derivatives 5.0% · Staking Pool 3.8%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.992% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $448.12M
- OnRe (RWA): $298.56M
- Solstice (Basis Trading): $237.97M
- Huma Finance V2 (RWA): $192.09M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **847.3 unique fee payers** signed per block (1,133 distinct addresses in the union, 55.4% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-04T01:39:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,565.12 | 3,469.92 | -2.67% |
| Average non-vote TPS | 1,443.12 | 1,340.66 | -7.10% |
| Average slot time (ms) | 315.10 | 314.50 | -0.19% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 18.00 | 18.00 | +0.00% |
| Solana TVL | 5,958,193,076.00 | 5,858,132,654.00 | -1.68% |
| SOL price | 103.48 | 102.06 | -1.37% |
| Stablecoin supply | 16,103,149,858.00 | 16,645,882,037.00 | +3.37% |
| 24h DEX volume | 2,372,074,173.80 | 1,848,928,416.00 | -22.05% |
| 24h chain fees | 10,727,529.99 | 10,602,054.70 | -1.17% |

### Change over 7d (vs run at 2026-08-29T01:13:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,960.85 | 3,469.92 | -12.39% |
| Average non-vote TPS | 1,808.22 | 1,340.66 | -25.86% |
| Average slot time (ms) | 317.40 | 314.50 | -0.91% |
| Active validators | 687.00 | 677.00 | -1.46% |
| Delinquent validators | 10.00 | 18.00 | +80.00% |
| Solana TVL | 5,832,657,009.00 | 5,858,132,654.00 | +0.44% |
| SOL price | 103.93 | 102.06 | -1.80% |
| Stablecoin supply | 16,381,381,392.00 | 16,645,882,037.00 | +1.61% |
| 24h DEX volume | 2,613,991,447.22 | 1,848,928,416.00 | -29.27% |
| 24h chain fees | 16,411,287.12 | 10,602,054.70 | -35.40% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,469.92 | -11.81% |
| Average non-vote TPS | 2,312.46 | 1,340.66 | -42.02% |
| Average slot time (ms) | 424.10 | 314.50 | -25.84% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,858,132,654.00 | +23.59% |
| SOL price | 72.81 | 102.06 | +40.17% |
| Stablecoin supply | 16,197,749,831.00 | 16,645,882,037.00 | +2.77% |
| 24h DEX volume | 1,636,927,091.91 | 1,848,928,416.00 | +12.95% |
| 24h chain fees | 7,777,648.77 | 10,602,054.70 | +36.31% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 11.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
