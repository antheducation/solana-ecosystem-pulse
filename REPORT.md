# Solana Ecosystem Pulse

**Generated:** 2026-08-13T12:40:10Z · **Schema:** `1.0.0` · **Collection time:** 19.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.89 | -1.08% |
| Market cap | $44.22B | rank #7 |
| Total value locked | $4.82B | -0.49% |
| Stablecoin supply | $16.08B | -1.32% |
| DEX volume (24h) | $1.73B | +4.53% |
| Chain fees / REV (24h) | $9.58M | -3.99% |
| Non-vote TPS (1h avg) | 2,066 | peak 4,424 total |
| Active validators | 687 | 10 delinquent |
| Epoch 1016 | 24.98% complete | 324,092 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 31 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average slot time (ms) is below its recent norm | Current 415.80 sits 4.6 sigma below the median of the last 31 runs (422.60, -1.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,066.2 average over the last 60 minutes; 1,980.9 in the latest sample.
- **Total TPS:** 3,709.8 average, 4,424.4 peak. Consensus votes account for 44.3% of all transactions.
- **Slot time:** 415.8 ms average (target 400 ms), worst 1-minute bucket 444.4 ms.
- **Block height:** 417,071,579 at absolute slot 439,019,908.
- **Epoch 1016:** slot 107,908 of 432,000 (24.98% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.698% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 352 ms |
| `solana-rpc.publicnode.com` | yes | 30 ms |
| `api.mainnet.solana.com` | yes | 269 ms |

## Validators & stake

- **687 active** validators, **10 delinquent** (1.43% by count, 0.057% by stake).
- **Total stake:** 434,669,916 SOL ($32.99B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.45% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 12.02%; 257 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,055,967 | 3.926% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,972,699 | 3.677% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,477,808 | 2.872% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,363,210 | 2.846% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,161,872 | 2.109% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,981,437 | 2.067% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,300,271 | 1.911% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,966,398 | 1.834% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,372,731 | 1.697% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,581,887 | 1.515% | 0% |

## Economics

- **SOL:** $75.89 (-1.08% 24h, +3.47% 7d, +0.74% 30d). Market cap $44.22B, 24h volume $1.17B (2.66% of cap). Price source: `coingecko`.
- **TVL:** $4.82B across 322 protocols - rank #4 of 461 chains, 6.41% of all tracked chain TVL. +0.69% over 7d, -63.5% from its ATH.
- **Stablecoins:** $16.08B circulating on Solana (-0.85% 7d) - $3.34 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.73B in 24h, $10.54B over 7d across 115 venues. Volume/TVL turnover 0.358x per day.
- **REV (chain fees):** $9.58M in 24h, $236.77M over 30d. Retained chain revenue $4.81M (50.2% of fees). Annualised fees are 7.91% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,614,278 SOL circulating of 632,135,898 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.12B | -1.0% | +2.6% |
| 2 | Kamino Lend | Lending | $1.05B | -1.0% | +0.5% |
| 3 | Jupiter Lend | Lending | $936.10M | -1.0% | -0.1% |
| 4 | Raydium AMM | Dexs | $847.03M | -0.7% | +3.7% |
| 5 | Binance Staked SOL | Liquid Staking | $776.43M | -1.3% | +3.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $755.23M | -1.4% | +2.6% |
| 7 | BlackRock BUIDL | RWA | $740.62M | +1.7% | +8.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $690.73M | -1.1% | -2.3% |
| 9 | Solstice | Basis Trading | $505.93M | -0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $392.06M | -1.2% | +1.6% |
| 11 | xStocks | RWA | $374.83M | -0.6% | +2.1% |
| 12 | Sentora | Risk Curators | $368.88M | -0.0% | -0.7% |

The top five protocols hold 35.2% of Solana's tracked TVL. Summed across all 322 protocols the total is $13.42B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.5% · Lending 16.6% · RWA 13.9% · Dexs 13.5% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.45B of tokenised real-world assets and equities are locked on Solana - 18.231% of chain TVL.

- BlackRock BUIDL (RWA): $740.62M
- Solstice (Basis Trading): $505.93M
- xStocks (RWA): $374.83M
- OnRe (RWA): $257.33M
- Ondo Yield Assets (RWA): $178.81M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,000.3 unique fee payers** signed per block (1,426 distinct addresses in the union, 52.5% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-13
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-12
- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29

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

### Change over 24h (vs run at 2026-08-12T12:39:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,481.04 | 3,709.85 | +6.57% |
| Average non-vote TPS | 1,852.50 | 2,066.15 | +11.53% |
| Average slot time (ms) | 420.40 | 415.80 | -1.09% |
| Active validators | 689.00 | 687.00 | -0.29% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 4,855,182,857.00 | 4,819,382,015.00 | -0.74% |
| SOL price | 76.81 | 75.89 | -1.20% |
| Stablecoin supply | 16,295,761,438.00 | 16,080,183,048.00 | -1.32% |
| 24h DEX volume | 1,650,837,789.28 | 1,725,631,800.93 | +4.53% |
| 24h chain fees | 9,897,773.23 | 9,577,693.00 | -3.23% |

### Change over 7d (vs run at 2026-08-06T19:36:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,775.16 | 3,709.85 | -1.73% |
| Average non-vote TPS | 2,150.39 | 2,066.15 | -3.92% |
| Average slot time (ms) | 422.90 | 415.80 | -1.68% |
| Active validators | 693.00 | 687.00 | -0.87% |
| Delinquent validators | 7.00 | 10.00 | +42.86% |
| Solana TVL | 4,739,955,873.00 | 4,819,382,015.00 | +1.68% |
| SOL price | 72.58 | 75.89 | +4.56% |
| Stablecoin supply | 16,197,749,831.00 | 16,080,183,048.00 | -0.73% |
| 24h DEX volume | 1,636,927,091.91 | 1,725,631,800.93 | +5.42% |
| 24h chain fees | 7,777,648.77 | 9,577,693.00 | +23.14% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 19.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
