# Solana Ecosystem Pulse

**Generated:** 2026-08-15T06:16:42Z · **Schema:** `1.0.0` · **Collection time:** 16.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.27 | -0.58% |
| Market cap | $43.87B | rank #7 |
| Total value locked | $4.82B | -0.35% |
| Stablecoin supply | $16.01B | -0.55% |
| DEX volume (24h) | $1.64B | -15.47% |
| Chain fees / REV (24h) | $8.00M | -21.13% |
| Non-vote TPS (1h avg) | 1,188 | peak 3,458 total |
| Active validators | 687 | 10 delinquent |
| Epoch 1017 | 8.34% complete | 395,961 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 38 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 16,009,820,741.00 sits 3.1 sigma below the median of the last 38 runs (16,250,158,640.00, -1.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,187.7 average over the last 60 minutes; 1,121.7 in the latest sample.
- **Total TPS:** 2,806.3 average, 3,457.8 peak. Consensus votes account for 57.7% of all transactions.
- **Slot time:** 416.0 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 417,430,958 at absolute slot 439,380,039.
- **Epoch 1017:** slot 36,039 of 432,000 (8.34% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.695% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 275 ms |
| `solana-rpc.publicnode.com` | yes | 102 ms |
| `api.mainnet.solana.com` | yes | 316 ms |

## Validators & stake

- **687 active** validators, **10 delinquent** (1.43% by count, 0.020% by stake).
- **Total stake:** 435,491,340 SOL ($32.78B); stake rate 68.88% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.01%; 257 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,161,316 | 3.941% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,969,044 | 3.668% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,492,108 | 2.869% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,274,846 | 2.819% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,181,197 | 2.109% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,981,926 | 2.063% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,303,340 | 1.907% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,969,078 | 1.830% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,340,396 | 1.686% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,586,185 | 1.513% | 0% |

## Economics

- **SOL:** $75.27 (-0.58% 24h, +0.88% 7d, -2.78% 30d). Market cap $43.87B, 24h volume $1.06B (2.41% of cap). Price source: `coingecko`.
- **TVL:** $4.82B across 326 protocols - rank #3 of 461 chains, 6.42% of all tracked chain TVL. +1.50% over 7d, -63.6% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.42% 7d) - $3.32 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.64B in 24h, $11.21B over 7d across 117 venues. Volume/TVL turnover 0.341x per day.
- **REV (chain fees):** $8.00M in 24h, $240.18M over 30d. Retained chain revenue $3.84M (48.0% of fees). Annualised fees are 6.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,728,379 SOL circulating of 632,262,356 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | -0.4% | +4.2% |
| 2 | Kamino Lend | Lending | $1.05B | +0.1% | +2.1% |
| 3 | Jupiter Lend | Lending | $925.56M | -0.8% | +3.0% |
| 4 | Raydium AMM | Dexs | $844.72M | -0.3% | +2.4% |
| 5 | Binance Staked SOL | Liquid Staking | $768.41M | -1.4% | +2.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $754.98M | -0.5% | +3.1% |
| 7 | BlackRock BUIDL | RWA | $740.96M | +0.0% | +4.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $683.83M | -0.6% | -2.4% |
| 9 | Solstice | Basis Trading | $505.89M | -0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $391.76M | -0.4% | +2.9% |
| 11 | xStocks | RWA | $380.11M | -0.7% | +1.5% |
| 12 | Sentora | Risk Curators | $368.12M | -0.1% | -0.2% |

The top five protocols hold 35.0% of Solana's tracked TVL. Summed across all 326 protocols the total is $13.47B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.4% · RWA 13.9% · Dexs 13.4% · Derivatives 5.8% · Basis Trading 4.3%

### Tokenised assets

$2.45B of tokenised real-world assets and equities are locked on Solana - 18.226% of chain TVL.

- BlackRock BUIDL (RWA): $740.96M
- Solstice (Basis Trading): $505.89M
- xStocks (RWA): $380.11M
- OnRe (RWA): $260.89M
- Ondo Yield Assets (RWA): $178.73M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **868.7 unique fee payers** signed per block (1,120 distinct addresses in the union, 57.0% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-12
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
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

### Change over 24h (vs run at 2026-08-14T07:03:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,039.98 | 2,806.28 | -7.69% |
| Average non-vote TPS | 1,398.69 | 1,187.72 | -15.08% |
| Average slot time (ms) | 416.00 | 416.00 | +0.00% |
| Active validators | 688.00 | 687.00 | -0.15% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 4,836,509,599.00 | 4,820,764,054.00 | -0.33% |
| SOL price | 75.45 | 75.27 | -0.24% |
| Stablecoin supply | 16,096,706,018.00 | 16,009,820,741.00 | -0.54% |
| 24h DEX volume | 1,978,176,047.75 | 1,642,311,971.56 | -16.98% |
| 24h chain fees | 10,092,794.92 | 8,004,118.79 | -20.69% |

### Change over 7d (vs run at 2026-08-08T06:30:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,175.17 | 2,806.28 | -11.62% |
| Average non-vote TPS | 1,547.82 | 1,187.72 | -23.26% |
| Average slot time (ms) | 421.90 | 416.00 | -1.40% |
| Active validators | 692.00 | 687.00 | -0.72% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,760,556,768.00 | 4,820,764,054.00 | +1.26% |
| SOL price | 74.65 | 75.27 | +0.83% |
| Stablecoin supply | 16,244,204,596.00 | 16,009,820,741.00 | -1.44% |
| 24h DEX volume | 1,361,153,628.02 | 1,642,311,971.56 | +20.66% |
| 24h chain fees | 8,222,506.02 | 8,004,118.79 | -2.66% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 16.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
