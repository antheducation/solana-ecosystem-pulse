# Solana Ecosystem Pulse

**Generated:** 2026-08-22T06:18:24Z · **Schema:** `1.0.0` · **Collection time:** 28.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $93.90 | +3.47% |
| Market cap | $54.69B | rank #7 |
| Total value locked | $5.63B | +5.62% |
| Stablecoin supply | $16.42B | -0.59% |
| DEX volume (24h) | $3.47B | +25.26% |
| Chain fees / REV (24h) | $13.20M | +19.19% |
| Non-vote TPS (1h avg) | 2,718 | peak 6,700 total |
| Active validators | 685 | 9 delinquent |
| Epoch 1020 | 51.24% complete | 210,628 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 59 historical runs, sigma = 3.0).

Critical 0 · Serious 4 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.40 sits 14.7 sigma below the median of the last 59 runs (416.60, -12.0%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,632,028,805.00 sits 20.8 sigma above the median of the last 59 runs (4,831,307,533.00, +16.6%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 93.90 sits 18.6 sigma above the median of the last 59 runs (75.94, +23.7%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,465,651,694.33 sits 5.4 sigma above the median of the last 59 runs (1,605,343,342.56, +115.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,718.0 average over the last 60 minutes; 1,884.5 in the latest sample.
- **Total TPS:** 4,573.2 average, 6,700.2 peak. Consensus votes account for 40.6% of all transactions.
- **Slot time:** 366.4 ms average (target 400 ms), worst 1-minute bucket 382.2 ms.
- **Block height:** 418,910,805 at absolute slot 440,861,372.
- **Epoch 1020:** slot 221,372 of 432,000 (51.24% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 693 ms |
| `solana-rpc.publicnode.com` | yes | 32 ms |
| `api.mainnet.solana.com` | yes | 515 ms |

## Validators & stake

- **685 active** validators, **9 delinquent** (1.30% by count, 0.019% by stake).
- **Total stake:** 433,485,334 SOL ($40.70B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.20%; 254 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.704% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.718% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.118% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.058% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.939% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.511% | 0% |

## Economics

- **SOL:** $93.90 (+3.47% 24h, +24.69% 7d, +21.17% 30d). Market cap $54.69B, 24h volume $8.95B (16.36% of cap). Price source: `coingecko`.
- **TVL:** $5.63B across 330 protocols - rank #3 of 462 chains, 6.35% of all tracked chain TVL. +16.93% over 7d, -57.5% from its ATH.
- **Stablecoins:** $16.42B circulating on Solana (+2.57% 7d) - $2.92 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.47B in 24h, $14.43B over 7d across 119 venues. Volume/TVL turnover 0.615x per day.
- **REV (chain fees):** $13.20M in 24h, $265.90M over 30d. Retained chain revenue $5.29M (40.0% of fees). Annualised fees are 8.81% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,177,240 SOL circulating of 632,639,570 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.44B | +7.4% | +27.8% |
| 2 | Kamino Lend | Lending | $1.21B | +4.5% | +15.1% |
| 3 | Jupiter Lend | Lending | $1.07B | +3.1% | +16.0% |
| 4 | Raydium AMM | Dexs | $1.05B | +6.6% | +23.9% |
| 5 | Binance Staked SOL | Liquid Staking | $975.47M | +7.6% | +27.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $966.22M | +7.7% | +28.3% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +4.9% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $761.76M | +3.7% | +11.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $504.38M | +7.9% | +29.0% |
| 10 | xStocks | RWA | $427.35M | +3.7% | +12.4% |
| 11 | Solstice | Basis Trading | $404.30M | -20.1% | -20.1% |
| 12 | Sentora | Risk Curators | $366.40M | +0.6% | -0.5% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.64B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.6% · Lending 16.3% · Dexs 14.1% · RWA 12.5% · Derivatives 5.5% · Staking Pool 3.4%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.603% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $427.35M
- Solstice (Basis Trading): $404.30M
- OnRe (RWA): $273.27M
- Ondo Yield Assets (RWA): $179.14M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **880.0 unique fee payers** signed per block (1,163 distinct addresses in the union, 55.9% overlap between blocks).

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
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-20
- [SIMD-0298: Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-17
- [SIMD-0553: simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14

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

### Change over 24h (vs run at 2026-08-21T06:22:52Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,313.55 | 4,573.18 | +38.01% |
| Average non-vote TPS | 1,667.75 | 2,718.03 | +62.98% |
| Average slot time (ms) | 416.60 | 366.40 | -12.05% |
| Active validators | 690.00 | 685.00 | -0.72% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 5,372,223,613.00 | 5,632,028,805.00 | +4.84% |
| SOL price | 90.54 | 93.90 | +3.71% |
| Stablecoin supply | 16,515,048,692.00 | 16,420,329,932.00 | -0.57% |
| 24h DEX volume | 2,781,215,932.33 | 3,465,651,694.33 | +24.61% |
| 24h chain fees | 11,033,466.08 | 13,204,850.88 | +19.68% |

### Change over 7d (vs run at 2026-08-15T06:16:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,806.28 | 4,573.18 | +62.96% |
| Average non-vote TPS | 1,187.72 | 2,718.03 | +128.84% |
| Average slot time (ms) | 416.00 | 366.40 | -11.92% |
| Active validators | 687.00 | 685.00 | -0.29% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 4,820,764,054.00 | 5,632,028,805.00 | +16.83% |
| SOL price | 75.27 | 93.90 | +24.75% |
| Stablecoin supply | 16,009,820,741.00 | 16,420,329,932.00 | +2.56% |
| 24h DEX volume | 1,642,311,971.56 | 3,465,651,694.33 | +111.02% |
| 24h chain fees | 8,004,118.79 | 13,204,850.88 | +64.98% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 28.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
