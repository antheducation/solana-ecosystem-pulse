# Solana Ecosystem Pulse

**Generated:** 2026-08-21T00:33:25Z · **Schema:** `1.0.0` · **Collection time:** 27.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $88.31 | +3.22% |
| Market cap | $51.51B | rank #7 |
| Total value locked | $5.29B | +7.93% |
| Stablecoin supply | $16.33B | +1.97% |
| DEX volume (24h) | $3.15B | +4.68% |
| Chain fees / REV (24h) | $13.76M | +0.59% |
| Non-vote TPS (1h avg) | 2,670 | peak 5,107 total |
| Active validators | 690 | 6 delinquent |
| Epoch 1019 | 85.54% complete | 62,470 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 61 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,285,370,682.00 sits 11.3 sigma above the median of the last 61 runs (4,821,987,992.00, +9.6%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 88.31 sits 14.1 sigma above the median of the last 61 runs (75.80, +16.5%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,150,837,936.95 sits 5.8 sigma above the median of the last 61 runs (1,581,973,855.56, +99.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 7.9% in 24h) | Solana TVL changed +7.9% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | 24h chain fees is above its recent norm | Current 13,758,063.85 sits 3.2 sigma above the median of the last 61 runs (9,097,906.09, +51.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,669.7 average over the last 60 minutes; 2,745.4 in the latest sample.
- **Total TPS:** 4,319.1 average, 5,106.7 peak. Consensus votes account for 38.2% of all transactions.
- **Slot time:** 415.8 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 418,627,259 at absolute slot 440,577,530.
- **Epoch 1019:** slot 369,530 of 432,000 (85.54% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 492 ms |
| `solana-rpc.publicnode.com` | yes | 212 ms |
| `api.mainnet.solana.com` | yes | 457 ms |

## Validators & stake

- **690 active** validators, **6 delinquent** (0.86% by count, 0.001% by stake).
- **Total stake:** 435,241,268 SOL ($38.44B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.38% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.27%; 256 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.929% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.679% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.851% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.803% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.111% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.066% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.909% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.836% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.688% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.504% | 0% |

## Economics

- **SOL:** $88.31 (+3.22% 24h, +15.86% 7d, +13.09% 30d). Market cap $51.51B, 24h volume $4.21B (8.17% of cap). Price source: `coingecko`.
- **TVL:** $5.29B across 328 protocols - rank #3 of 461 chains, 6.29% of all tracked chain TVL. +9.58% over 7d, -60.1% from its ATH.
- **Stablecoins:** $16.33B circulating on Solana (+1.53% 7d) - $3.09 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.15B in 24h, $10.95B over 7d across 119 venues. Volume/TVL turnover 0.596x per day.
- **REV (chain fees):** $13.76M in 24h, $253.21M over 30d. Retained chain revenue $5.98M (43.4% of fees). Annualised fees are 9.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,063,315 SOL circulating of 632,513,124 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.31B | +2.5% | +15.0% |
| 2 | Kamino Lend | Lending | $1.13B | +0.5% | +7.5% |
| 3 | Jupiter Lend | Lending | $975.10M | -0.8% | +5.3% |
| 4 | Raydium AMM | Dexs | $965.69M | +6.3% | +13.6% |
| 5 | Binance Staked SOL | Liquid Staking | $884.49M | +2.5% | +13.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $876.31M | +2.5% | +15.2% |
| 7 | BlackRock BUIDL | RWA | $740.67M | +0.0% | -0.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $721.35M | -1.4% | +4.6% |
| 9 | Solstice | Basis Trading | $506.24M | +0.0% | +0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $454.58M | +2.5% | +15.0% |
| 11 | xStocks | RWA | $407.75M | +0.8% | +6.3% |
| 12 | Sentora | Risk Curators | $365.19M | -0.3% | -0.9% |

The top five protocols hold 35.9% of Solana's tracked TVL. Summed across all 328 protocols the total is $14.66B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 34.4% · Lending 16.1% · Dexs 13.9% · RWA 13.0% · Derivatives 5.6% · Basis Trading 4.0%

### Tokenised assets

$2.49B of tokenised real-world assets and equities are locked on Solana - 16.978% of chain TVL.

- BlackRock BUIDL (RWA): $740.67M
- Solstice (Basis Trading): $506.24M
- xStocks (RWA): $407.75M
- OnRe (RWA): $272.68M
- Ondo Yield Assets (RWA): $178.53M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **993.0 unique fee payers** signed per block (1,392 distinct addresses in the union, 53.3% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-19
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14

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

### Change over 24h (vs run at 2026-08-20T00:30:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,289.29 | 4,319.13 | +0.70% |
| Average non-vote TPS | 2,638.50 | 2,669.71 | +1.18% |
| Average slot time (ms) | 414.40 | 415.80 | +0.34% |
| Active validators | 688.00 | 690.00 | +0.29% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 5,190,256,197.00 | 5,285,370,682.00 | +1.83% |
| SOL price | 85.66 | 88.31 | +3.09% |
| Stablecoin supply | 16,010,344,860.00 | 16,326,513,472.00 | +1.97% |
| 24h DEX volume | 2,189,292,543.00 | 3,150,837,936.95 | +43.92% |
| 24h chain fees | 9,650,957.28 | 13,758,063.85 | +42.56% |

### Change over 7d (vs run at 2026-08-14T00:54:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,556.79 | 4,319.13 | +21.43% |
| Average non-vote TPS | 1,918.34 | 2,669.71 | +39.17% |
| Average slot time (ms) | 416.50 | 415.80 | -0.17% |
| Active validators | 688.00 | 690.00 | +0.29% |
| Delinquent validators | 9.00 | 6.00 | -33.33% |
| Solana TVL | 4,848,077,810.00 | 5,285,370,682.00 | +9.02% |
| SOL price | 76.02 | 88.31 | +16.17% |
| Stablecoin supply | 16,080,626,456.00 | 16,326,513,472.00 | +1.53% |
| 24h DEX volume | 1,981,814,466.75 | 3,150,837,936.95 | +58.99% |
| 24h chain fees | 9,107,820.55 | 13,758,063.85 | +51.06% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
