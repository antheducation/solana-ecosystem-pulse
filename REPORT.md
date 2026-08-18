# Solana Ecosystem Pulse

**Generated:** 2026-08-18T06:20:54Z · **Schema:** `1.0.0` · **Collection time:** 256.7s · **Sources OK:** 34/38

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.81 | +0.42% |
| Market cap | $44.19B | rank #7 |
| Total value locked | $4.85B | +1.46% |
| Stablecoin supply | $15.98B | -0.15% |
| DEX volume (24h) | $1.43B | +35.03% |
| Chain fees / REV (24h) | $10.77M | +58.36% |
| Non-vote TPS (1h avg) | 1,251 | peak 3,969 total |
| Active validators | 689 | 6 delinquent |
| Epoch 1018 | 52.88% complete | 203,561 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 50 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 58.4% in 24h) | Chain fees changed +58.4% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,251.5 average over the last 60 minutes; 1,113.8 in the latest sample.
- **Total TPS:** 2,904.5 average, 3,969.1 peak. Consensus votes account for 56.9% of all transactions.
- **Slot time:** 417.0 ms average (target 400 ms), worst 1-minute bucket 666.7 ms.
- **Block height:** 418,054,826 at absolute slot 440,004,439.
- **Epoch 1018:** slot 228,439 of 432,000 (52.88% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.692% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 118 ms |
| `solana-rpc.publicnode.com` | yes | 156 ms |
| `api.mainnet.solana.com` | yes | 100 ms |

## Validators & stake

- **689 active** validators, **6 delinquent** (0.86% by count, 0.008% by stake).
- **Total stake:** 435,676,796 SOL ($33.03B); stake rate n/a of total supply.
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

- **SOL:** $75.81 (+0.42% 24h, +0.14% 7d, -0.15% 30d). Market cap $44.19B, 24h volume $1.32B (2.98% of cap). Price source: `coingecko`.
- **TVL:** $4.85B across 325 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. +0.15% over 7d, -63.4% from its ATH.
- **Stablecoins:** $15.98B circulating on Solana (-2.11% 7d) - $3.30 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.43B in 24h, $10.47B over 7d across 117 venues. Volume/TVL turnover 0.294x per day.
- **REV (chain fees):** $10.77M in 24h, $244.61M over 30d. Retained chain revenue $4.10M (38.1% of fees). Annualised fees are 8.90% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | +0.4% | +1.6% |
| 2 | Kamino Lend | Lending | $1.06B | +1.4% | +0.5% |
| 3 | Jupiter Lend | Lending | $944.25M | +1.6% | +1.4% |
| 4 | Raydium AMM | Dexs | $843.37M | -0.2% | -0.5% |
| 5 | Binance Staked SOL | Liquid Staking | $770.21M | +0.5% | -0.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $758.36M | +0.4% | +0.1% |
| 7 | BlackRock BUIDL | RWA | $741.35M | +0.1% | +4.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $681.09M | +0.2% | -1.8% |
| 9 | Solstice | Basis Trading | $506.12M | +0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $392.62M | +0.5% | +0.0% |
| 11 | xStocks | RWA | $386.59M | +1.5% | +3.9% |
| 12 | Sentora | Risk Curators | $367.26M | -0.0% | -0.3% |

The top five protocols hold 35.1% of Solana's tracked TVL. Summed across all 325 protocols the total is $13.52B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.6% · RWA 13.9% · Dexs 13.4% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 18.223% of chain TVL.

- BlackRock BUIDL (RWA): $741.35M
- Solstice (Basis Trading): $506.12M
- xStocks (RWA): $386.59M
- OnRe (RWA): $267.59M
- Ondo Yield Assets (RWA): $178.67M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **900.7 unique fee payers** signed per block (1,207 distinct addresses in the union, 55.3% overlap between blocks).

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

- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03

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

### Change over 24h (vs run at 2026-08-17T06:27:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,132.50 | 2,904.51 | -7.28% |
| Average non-vote TPS | 1,482.73 | 1,251.49 | -15.60% |
| Average slot time (ms) | 415.20 | 417.00 | +0.43% |
| Active validators | 689.00 | 689.00 | +0.00% |
| Delinquent validators | 6.00 | 6.00 | +0.00% |
| Solana TVL | 4,813,819,212.00 | 4,846,663,986.00 | +0.68% |
| SOL price | 75.41 | 75.81 | +0.53% |
| Stablecoin supply | 16,004,923,242.00 | 15,980,255,447.00 | -0.15% |
| 24h DEX volume | 1,053,725,616.95 | 1,425,243,228.36 | +35.26% |
| 24h chain fees | 6,617,725.48 | 10,772,677.30 | +62.79% |

### Change over 7d (vs run at 2026-08-11T06:43:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,024.61 | 2,904.51 | -3.97% |
| Average non-vote TPS | 1,404.61 | 1,251.49 | -10.90% |
| Average slot time (ms) | 423.50 | 417.00 | -1.53% |
| Active validators | 691.00 | 689.00 | -0.29% |
| Delinquent validators | 7.00 | 6.00 | -14.29% |
| Solana TVL | 4,831,307,533.00 | 4,846,663,986.00 | +0.32% |
| SOL price | 75.78 | 75.81 | +0.04% |
| Stablecoin supply | 16,323,261,006.00 | 15,980,255,447.00 | -2.10% |
| 24h DEX volume | 1,546,444,167.56 | 1,425,243,228.36 | -7.84% |
| 24h chain fees | 10,453,688.03 | 10,772,677.30 | +3.05% |

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

This run made 38 HTTP calls (34 succeeded, 4 failed) in 256.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `rpc:getSupply@api.mainnet-beta.solana.com` - TimeoutError: The read operation timed out (2 attempts)
- `rpc:getSupply@solana-rpc.publicnode.com` - TimeoutError: The read operation timed out (2 attempts)
- `rpc:getSupply@api.mainnet.solana.com` - TimeoutError: The read operation timed out (2 attempts)
- `rpc:getBlock@api.mainnet-beta.solana.com` - TimeoutError: The read operation timed out (2 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
