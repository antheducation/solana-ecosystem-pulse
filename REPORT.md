# Solana Ecosystem Pulse

**Generated:** 2026-09-04T19:58:05Z · **Schema:** `1.0.0` · **Collection time:** 12.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.76 | -3.24% |
| Market cap | $59.55B | rank #7 |
| Total value locked | $5.81B | +1.84% |
| Stablecoin supply | $16.64B | +3.36% |
| DEX volume (24h) | $2.46B | +7.44% |
| Chain fees / REV (24h) | $11.82M | +4.91% |
| Non-vote TPS (1h avg) | 1,458 | peak 4,298 total |
| Active validators | 678 | 17 delinquent |
| Epoch 1028 | 54.29% complete | 197,472 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 67 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.4% in 24h) | Stablecoin supply changed +3.4% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,457.7 average over the last 60 minutes; 1,397.1 in the latest sample.
- **Total TPS:** 3,586.2 average, 4,298.4 peak. Consensus votes account for 59.4% of all transactions.
- **Slot time:** 315.1 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 422,375,989 at absolute slot 444,330,528.
- **Epoch 1028:** slot 234,528 of 432,000 (54.29% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.664% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 74 ms |
| `solana-rpc.publicnode.com` | yes | 45 ms |
| `api.mainnet.solana.com` | yes | 161 ms |

## Validators & stake

- **678 active** validators, **17 delinquent** (2.45% by count, 0.028% by stake).
- **Total stake:** 436,898,866 SOL ($44.46B); stake rate 68.97% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.48%; 245 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,393,318 | 3.982% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,259 | 3.737% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,459,602 | 2.853% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,379,843 | 2.605% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,567,623 | 2.190% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,278,151 | 2.124% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,042,760 | 2.070% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,376,879 | 1.689% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,127,366 | 1.632% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,593,517 | 1.510% | 0% |

## Economics

- **SOL:** $101.76 (-3.24% 24h, -1.24% 7d, +36.65% 30d). Market cap $59.55B, 24h volume $3.73B (6.26% of cap). Price source: `coingecko`.
- **TVL:** $5.81B across 342 protocols - rank #2 of 465 chains, 6.66% of all tracked chain TVL. -3.44% over 7d, -56.1% from its ATH.
- **Stablecoins:** $16.64B circulating on Solana (+2.60% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.46B in 24h, $15.61B over 7d across 121 venues. Volume/TVL turnover 0.424x per day.
- **REV (chain fees):** $11.82M in 24h, $337.81M over 30d. Retained chain revenue $4.61M (39.0% of fees). Annualised fees are 7.25% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,360,055 SOL circulating of 633,455,081 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -3.3% | -7.6% |
| 2 | Kamino Lend | Lending | $1.31B | -1.6% | +4.5% |
| 3 | Raydium AMM | Dexs | $1.11B | -2.5% | -4.5% |
| 4 | Jupiter Lend | Lending | $1.07B | -3.0% | -5.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | -3.8% | -6.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -2.8% | -6.5% |
| 7 | BlackRock BUIDL | RWA | $937.90M | +5.3% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $747.70M | -3.2% | -6.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $523.50M | -4.1% | -7.9% |
| 10 | xStocks | RWA | $447.28M | -3.4% | +1.3% |
| 11 | Marinade Native | Staking Pool | $409.51M | -3.0% | -8.3% |
| 12 | Sentora Curator | Risk Curators | $378.36M | -1.4% | +4.7% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 342 protocols the total is $16.52B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.1% · RWA 14.1% · Dexs 13.9% · Derivatives 5.0% · Staking Pool 3.8%

### Tokenised assets

$2.64B of tokenised real-world assets and equities are locked on Solana - 15.989% of chain TVL.

- BlackRock BUIDL (RWA): $937.90M
- xStocks (RWA): $447.28M
- OnRe (RWA): $296.87M
- Solstice (Basis Trading): $237.94M
- Ondo Yield Assets (RWA): $179.09M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **873.3 unique fee payers** signed per block (1,226 distinct addresses in the union, 53.2% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-03T20:12:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,437.74 | 3,586.23 | -19.19% |
| Average non-vote TPS | 2,316.58 | 1,457.68 | -37.08% |
| Average slot time (ms) | 316.10 | 315.10 | -0.32% |
| Active validators | 676.00 | 678.00 | +0.30% |
| Delinquent validators | 19.00 | 17.00 | -10.53% |
| Solana TVL | 5,969,689,229.00 | 5,805,967,650.00 | -2.74% |
| SOL price | 105.35 | 101.76 | -3.41% |
| Stablecoin supply | 16,102,283,829.00 | 16,644,416,664.00 | +3.37% |
| 24h DEX volume | 2,289,285,889.32 | 2,459,540,363.80 | +7.44% |
| 24h chain fees | 10,535,900.15 | 11,820,876.49 | +12.20% |

### Change over 7d (vs run at 2026-08-28T17:47:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,145.52 | 3,586.23 | -30.30% |
| Average non-vote TPS | 3,011.73 | 1,457.68 | -51.60% |
| Average slot time (ms) | 321.30 | 315.10 | -1.93% |
| Active validators | 688.00 | 678.00 | -1.45% |
| Delinquent validators | 9.00 | 17.00 | +88.89% |
| Solana TVL | 5,895,133,114.00 | 5,805,967,650.00 | -1.51% |
| SOL price | 104.55 | 101.76 | -2.67% |
| Stablecoin supply | 16,380,565,155.00 | 16,644,416,664.00 | +1.61% |
| 24h DEX volume | 3,700,129,857.54 | 2,459,540,363.80 | -33.53% |
| 24h chain fees | 16,302,758.52 | 11,820,876.49 | -27.49% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,586.23 | -8.85% |
| Average non-vote TPS | 2,312.46 | 1,457.68 | -36.96% |
| Average slot time (ms) | 424.10 | 315.10 | -25.70% |
| Active validators | 692.00 | 678.00 | -2.02% |
| Delinquent validators | 8.00 | 17.00 | +112.50% |
| Solana TVL | 4,740,035,266.00 | 5,805,967,650.00 | +22.49% |
| SOL price | 72.81 | 101.76 | +39.76% |
| Stablecoin supply | 16,197,749,831.00 | 16,644,416,664.00 | +2.76% |
| 24h DEX volume | 1,636,927,091.91 | 2,459,540,363.80 | +50.25% |
| 24h chain fees | 7,777,648.77 | 11,820,876.49 | +51.99% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
