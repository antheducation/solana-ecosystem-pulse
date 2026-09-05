# Solana Ecosystem Pulse

**Generated:** 2026-09-05T09:33:02Z · **Schema:** `1.0.0` · **Collection time:** 17.9s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.57 | -1.48% |
| Market cap | $60.04B | rank #7 |
| Total value locked | $5.86B | -0.96% |
| Stablecoin supply | $16.61B | -0.23% |
| DEX volume (24h) | $1.85B | -24.89% |
| Chain fees / REV (24h) | $9.54M | -19.33% |
| Non-vote TPS (1h avg) | 1,012 | peak 3,415 total |
| Active validators | 676 | 19 delinquent |
| Epoch 1028 | 90.25% complete | 42,133 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 68 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 19.00 sits 3.0 sigma above the median of the last 68 runs (10.00, +90.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,012.1 average over the last 60 minutes; 963.0 in the latest sample.
- **Total TPS:** 3,150.6 average, 3,415.0 peak. Consensus votes account for 67.9% of all transactions.
- **Slot time:** 313.9 ms average (target 400 ms), worst 1-minute bucket 320.9 ms.
- **Block height:** 422,530,552 at absolute slot 444,485,867.
- **Epoch 1028:** slot 389,867 of 432,000 (90.25% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.664% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 114 ms |
| `solana-rpc.publicnode.com` | yes | 100 ms |
| `api.mainnet.solana.com` | yes | 391 ms |

## Validators & stake

- **676 active** validators, **19 delinquent** (2.73% by count, 0.075% by stake).
- **Total stake:** 436,898,866 SOL ($44.81B); stake rate 68.97% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.95% of active stake.
- **Commission:** median 5.0%, mean 12.65%; 244 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,393,318 | 3.984% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,259 | 3.739% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,459,602 | 2.854% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,379,843 | 2.607% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,567,623 | 2.192% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,278,151 | 2.125% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,042,760 | 2.071% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,376,879 | 1.690% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,127,366 | 1.633% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,593,517 | 1.510% | 0% |

## Economics

- **SOL:** $102.57 (-1.48% 24h, -0.85% 7d, +38.74% 30d). Market cap $60.04B, 24h volume $2.87B (4.78% of cap). Price source: `coingecko`.
- **TVL:** $5.86B across 341 protocols - rank #2 of 466 chains, 6.70% of all tracked chain TVL. -0.12% over 7d, -55.7% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+2.60% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.85B in 24h, $14.32B over 7d across 121 venues. Volume/TVL turnover 0.315x per day.
- **REV (chain fees):** $9.54M in 24h, $338.06M over 30d. Retained chain revenue $4.14M (43.5% of fees). Annualised fees are 5.80% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,359,633 SOL circulating of 633,454,658 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | -1.1% | -1.6% |
| 2 | Kamino Lend | Lending | $1.32B | -1.2% | +5.3% |
| 3 | Raydium AMM | Dexs | $1.10B | -1.4% | -1.6% |
| 4 | Jupiter Lend | Lending | $1.10B | +0.4% | +0.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -1.2% | -1.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | -0.5% | -0.1% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +4.3% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $753.08M | -1.4% | -2.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $529.66M | -1.0% | -2.2% |
| 10 | xStocks | RWA | $447.66M | -2.6% | +3.5% |
| 11 | Marinade Native | Staking Pool | $404.01M | -3.5% | -5.0% |
| 12 | Sentora Curator | Risk Curators | $388.55M | +1.1% | +7.6% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.85B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.3% · Lending 15.9% · RWA 14.0% · Dexs 13.7% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.870% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $447.66M
- OnRe (RWA): $298.66M
- Solstice (Basis Trading): $237.91M
- Huma Finance V2 (RWA): $192.14M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **806.7 unique fee payers** signed per block (1,112 distinct addresses in the union, 54.0% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-04T10:03:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,392.95 | 3,150.57 | -7.14% |
| Average non-vote TPS | 1,264.70 | 1,012.13 | -19.97% |
| Average slot time (ms) | 315.80 | 313.90 | -0.60% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 18.00 | 19.00 | +5.56% |
| Solana TVL | 5,913,237,547.00 | 5,862,625,040.00 | -0.86% |
| SOL price | 104.06 | 102.57 | -1.43% |
| Stablecoin supply | 16,642,782,149.00 | 16,607,457,517.00 | -0.21% |
| 24h DEX volume | 2,373,588,819.80 | 1,847,410,950.00 | -22.17% |
| 24h chain fees | 10,960,933.49 | 9,536,106.55 | -13.00% |

### Change over 7d (vs run at 2026-08-29T11:51:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,327.43 | 3,150.57 | -5.32% |
| Average non-vote TPS | 1,164.69 | 1,012.13 | -13.10% |
| Average slot time (ms) | 316.90 | 313.90 | -0.95% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 9.00 | 19.00 | +111.11% |
| Solana TVL | 5,840,691,031.00 | 5,862,625,040.00 | +0.38% |
| SOL price | 103.63 | 102.57 | -1.02% |
| Stablecoin supply | 16,344,337,520.00 | 16,607,457,517.00 | +1.61% |
| 24h DEX volume | 2,590,586,442.22 | 1,847,410,950.00 | -28.69% |
| 24h chain fees | 15,624,748.43 | 9,536,106.55 | -38.97% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,150.57 | -19.93% |
| Average non-vote TPS | 2,312.46 | 1,012.13 | -56.23% |
| Average slot time (ms) | 424.10 | 313.90 | -25.98% |
| Active validators | 692.00 | 676.00 | -2.31% |
| Delinquent validators | 8.00 | 19.00 | +137.50% |
| Solana TVL | 4,740,035,266.00 | 5,862,625,040.00 | +23.68% |
| SOL price | 72.81 | 102.57 | +40.87% |
| Stablecoin supply | 16,197,749,831.00 | 16,607,457,517.00 | +2.53% |
| 24h DEX volume | 1,636,927,091.91 | 1,847,410,950.00 | +12.86% |
| 24h chain fees | 7,777,648.77 | 9,536,106.55 | +22.61% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
