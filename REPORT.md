# Solana Ecosystem Pulse

**Generated:** 2026-08-18T18:18:56Z · **Schema:** `1.0.0` · **Collection time:** 63.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $77.08 | +1.49% |
| Market cap | $44.92B | rank #7 |
| Total value locked | $4.89B | +2.28% |
| Stablecoin supply | $15.98B | -0.16% |
| DEX volume (24h) | $1.47B | +39.75% |
| Chain fees / REV (24h) | $11.19M | +64.49% |
| Non-vote TPS (1h avg) | 2,510 | peak 5,200 total |
| Active validators | 688 | 7 delinquent |
| Epoch 1018 | 76.89% complete | 99,826 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 52 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 64.5% in 24h) | Chain fees changed +64.5% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,510.4 average over the last 60 minutes; 2,692.6 in the latest sample.
- **Total TPS:** 4,157.6 average, 5,199.8 peak. Consensus votes account for 39.6% of all transactions.
- **Slot time:** 414.5 ms average (target 400 ms), worst 1-minute bucket 438.0 ms.
- **Block height:** 418,158,459 at absolute slot 440,108,174.
- **Epoch 1018:** slot 332,174 of 432,000 (76.89% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.692% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 410 ms |
| `solana-rpc.publicnode.com` | yes | 117 ms |
| `api.mainnet.solana.com` | yes | 474 ms |

## Validators & stake

- **688 active** validators, **7 delinquent** (1.01% by count, 0.012% by stake).
- **Total stake:** 435,676,796 SOL ($33.58B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.83% of active stake.
- **Commission:** median 5.0%, mean 12.30%; 255 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,091,057 | 3.923% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,003,006 | 3.674% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,360 | 2.868% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,259,520 | 2.814% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,203,436 | 2.113% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,992,381 | 2.064% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,305,834 | 1.907% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,983,993 | 1.833% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,342,590 | 1.686% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,588,037 | 1.512% | 0% |

## Economics

- **SOL:** $77.08 (+1.49% 24h, +2.54% 7d, +1.54% 30d). Market cap $44.92B, 24h volume $1.37B (3.05% of cap). Price source: `coingecko`.
- **TVL:** $4.89B across 325 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. +0.96% over 7d, -63.1% from its ATH.
- **Stablecoins:** $15.98B circulating on Solana (-2.12% 7d) - $3.27 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.47B in 24h, $10.60B over 7d across 117 venues. Volume/TVL turnover 0.302x per day.
- **REV (chain fees):** $11.19M in 24h, $246.80M over 30d. Retained chain revenue $4.38M (39.1% of fees). Annualised fees are 9.09% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,892,278 SOL circulating of 632,387,462 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.15B | +1.4% | +3.1% |
| 2 | Kamino Lend | Lending | $1.07B | +0.6% | +1.3% |
| 3 | Jupiter Lend | Lending | $954.84M | +1.8% | +2.6% |
| 4 | Raydium AMM | Dexs | $849.03M | +0.4% | +0.2% |
| 5 | Binance Staked SOL | Liquid Staking | $782.17M | +1.3% | +0.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $770.33M | +1.5% | +1.7% |
| 7 | BlackRock BUIDL | RWA | $741.42M | +0.0% | +4.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $687.25M | +0.7% | -0.9% |
| 9 | Solstice | Basis Trading | $506.20M | +0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $398.84M | +1.4% | +1.6% |
| 11 | xStocks | RWA | $384.86M | -1.1% | +3.5% |
| 12 | Sentora | Risk Curators | $367.47M | +0.0% | -0.3% |

The top five protocols hold 35.2% of Solana's tracked TVL. Summed across all 325 protocols the total is $13.64B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 33.0% · Lending 16.6% · RWA 13.8% · Dexs 13.4% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 18.055% of chain TVL.

- BlackRock BUIDL (RWA): $741.42M
- Solstice (Basis Trading): $506.20M
- xStocks (RWA): $384.86M
- OnRe (RWA): $268.28M
- Ondo Yield Assets (RWA): $178.74M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,046.7 unique fee payers** signed per block (1,532 distinct addresses in the union, 51.2% overlap between blocks).

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

- [SIMD-XXXX: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-18
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-18
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

### Change over 24h (vs run at 2026-08-17T18:19:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,422.32 | 4,157.63 | -5.99% |
| Average non-vote TPS | 2,781.61 | 2,510.42 | -9.75% |
| Average slot time (ms) | 415.70 | 414.50 | -0.29% |
| Active validators | 688.00 | 688.00 | +0.00% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,849,572,817.00 | 4,885,957,310.00 | +0.75% |
| SOL price | 75.94 | 77.08 | +1.50% |
| Stablecoin supply | 16,003,787,085.00 | 15,977,966,490.00 | -0.16% |
| 24h DEX volume | 1,055,467,633.95 | 1,474,970,358.36 | +39.75% |
| 24h chain fees | 6,802,409.48 | 11,189,593.30 | +64.49% |

### Change over 7d (vs run at 2026-08-11T18:43:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,160.34 | 4,157.63 | -0.07% |
| Average non-vote TPS | 2,542.89 | 2,510.42 | -1.28% |
| Average slot time (ms) | 422.60 | 414.50 | -1.92% |
| Active validators | 690.00 | 688.00 | -0.29% |
| Delinquent validators | 9.00 | 7.00 | -22.22% |
| Solana TVL | 4,798,590,463.00 | 4,885,957,310.00 | +1.82% |
| SOL price | 75.13 | 77.08 | +2.60% |
| Stablecoin supply | 16,322,733,028.00 | 15,977,966,490.00 | -2.11% |
| 24h DEX volume | 1,581,973,855.56 | 1,474,970,358.36 | -6.76% |
| 24h chain fees | 10,493,090.03 | 11,189,593.30 | +6.64% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 63.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
