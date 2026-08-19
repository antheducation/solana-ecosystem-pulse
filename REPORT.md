# Solana Ecosystem Pulse

**Generated:** 2026-08-19T00:30:20Z · **Schema:** `1.0.0` · **Collection time:** 15.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $76.89 | +1.24% |
| Market cap | $44.83B | rank #7 |
| Total value locked | $4.90B | +2.56% |
| Stablecoin supply | $15.98B | -0.16% |
| DEX volume (24h) | $1.46B | -1.25% |
| Chain fees / REV (24h) | $10.99M | -2.63% |
| Non-vote TPS (1h avg) | 2,105 | peak 4,349 total |
| Active validators | 689 | 6 delinquent |
| Epoch 1018 | 89.29% complete | 46,268 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 53 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,104.9 average over the last 60 minutes; 2,102.2 in the latest sample.
- **Total TPS:** 3,748.8 average, 4,348.9 peak. Consensus votes account for 43.9% of all transactions.
- **Slot time:** 416.7 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,211,997 at absolute slot 440,161,732.
- **Epoch 1018:** slot 385,732 of 432,000 (89.29% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.692% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 208 ms |
| `solana-rpc.publicnode.com` | yes | 81 ms |
| `api.mainnet.solana.com` | yes | 143 ms |

## Validators & stake

- **689 active** validators, **6 delinquent** (0.86% by count, 0.008% by stake).
- **Total stake:** 435,676,796 SOL ($33.50B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.83% of active stake.
- **Commission:** median 5.0%, mean 12.29%; 255 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,091,057 | 3.923% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,003,006 | 3.673% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,360 | 2.868% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,259,520 | 2.814% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,203,436 | 2.113% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,992,381 | 2.064% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,305,834 | 1.907% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,983,993 | 1.833% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,342,590 | 1.685% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,588,037 | 1.512% | 0% |

## Economics

- **SOL:** $76.89 (+1.24% 24h, +0.89% 7d, +0.76% 30d). Market cap $44.83B, 24h volume $1.42B (3.16% of cap). Price source: `coingecko`.
- **TVL:** $4.90B across 326 protocols - rank #2 of 461 chains, 6.43% of all tracked chain TVL. +1.24% over 7d, -63.0% from its ATH.
- **Stablecoins:** $15.98B circulating on Solana (-2.12% 7d) - $3.26 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.46B in 24h, $9.25B over 7d across 119 venues. Volume/TVL turnover 0.297x per day.
- **REV (chain fees):** $10.99M in 24h, $243.00M over 30d. Retained chain revenue $4.21M (38.3% of fees). Annualised fees are 8.94% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,892,044 SOL circulating of 632,387,229 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.15B | +1.7% | +2.5% |
| 2 | Kamino Lend | Lending | $1.07B | +0.6% | +1.5% |
| 3 | Jupiter Lend | Lending | $954.07M | +2.2% | +0.8% |
| 4 | Raydium AMM | Dexs | $856.44M | +1.2% | +0.5% |
| 5 | Binance Staked SOL | Liquid Staking | $783.53M | +1.9% | +0.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $770.55M | +1.7% | +1.0% |
| 7 | BlackRock BUIDL | RWA | $741.42M | +0.0% | +1.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $687.81M | +0.9% | -1.1% |
| 9 | Solstice | Basis Trading | $506.24M | -0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $399.59M | +1.9% | +1.4% |
| 11 | xStocks | RWA | $381.95M | -1.6% | +1.2% |
| 12 | Sentora | Risk Curators | $366.24M | -0.5% | -0.8% |

The top five protocols hold 35.3% of Solana's tracked TVL. Summed across all 326 protocols the total is $13.65B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 33.0% · Lending 16.6% · RWA 13.7% · Dexs 13.4% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 18.013% of chain TVL.

- BlackRock BUIDL (RWA): $741.42M
- Solstice (Basis Trading): $506.24M
- xStocks (RWA): $381.95M
- OnRe (RWA): $269.40M
- Ondo Yield Assets (RWA): $178.34M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **994.3 unique fee payers** signed per block (1,440 distinct addresses in the union, 51.7% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-18
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-18
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07

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

### Change over 24h (vs run at 2026-08-18T00:30:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,442.13 | 3,748.83 | +8.91% |
| Average non-vote TPS | 1,788.32 | 2,104.87 | +17.70% |
| Average slot time (ms) | 414.30 | 416.70 | +0.58% |
| Active validators | 689.00 | 689.00 | +0.00% |
| Delinquent validators | 6.00 | 6.00 | +0.00% |
| Solana TVL | 4,848,739,935.00 | 4,899,420,258.00 | +1.05% |
| SOL price | 75.95 | 76.89 | +1.24% |
| Stablecoin supply | 16,003,691,443.00 | 15,978,264,279.00 | -0.16% |
| 24h DEX volume | 1,055,467,633.95 | 1,456,594,741.93 | +38.00% |
| 24h chain fees | 6,906,881.24 | 10,986,421.95 | +59.06% |

### Change over 7d (vs run at 2026-08-12T00:53:45Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,974.24 | 3,748.83 | -5.67% |
| Average non-vote TPS | 2,353.21 | 2,104.87 | -10.55% |
| Average slot time (ms) | 421.90 | 416.70 | -1.23% |
| Active validators | 689.00 | 689.00 | +0.00% |
| Delinquent validators | 10.00 | 6.00 | -40.00% |
| Solana TVL | 4,787,487,114.00 | 4,899,420,258.00 | +2.34% |
| SOL price | 76.25 | 76.89 | +0.84% |
| Stablecoin supply | 16,324,318,696.00 | 15,978,264,279.00 | -2.12% |
| 24h DEX volume | 1,650,871,367.28 | 1,456,594,741.93 | -11.77% |
| 24h chain fees | 10,814,593.52 | 10,986,421.95 | +1.59% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
