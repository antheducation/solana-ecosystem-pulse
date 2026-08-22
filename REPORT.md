# Solana Ecosystem Pulse

**Generated:** 2026-08-22T12:14:01Z · **Schema:** `1.0.0` · **Collection time:** 27.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $93.74 | +3.96% |
| Market cap | $54.66B | rank #7 |
| Total value locked | $5.54B | +3.89% |
| Stablecoin supply | $16.42B | -0.59% |
| DEX volume (24h) | $3.60B | +30.15% |
| Chain fees / REV (24h) | $13.24M | +19.48% |
| Non-vote TPS (1h avg) | 1,411 | peak 3,797 total |
| Active validators | 686 | 8 delinquent |
| Epoch 1020 | 64.72% complete | 152,414 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 60 historical runs, sigma = 3.0).

Critical 0 · Serious 4 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.70 sits 14.3 sigma below the median of the last 60 runs (416.55, -12.0%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,539,353,430.00 sits 18.2 sigma above the median of the last 60 runs (4,831,669,193.50, +14.6%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 93.74 sits 18.0 sigma above the median of the last 60 runs (75.94, +23.4%). | `zscore` |
| [SERIOUS] | 24h DEX volume is above its recent norm | Current 3,600,948,276.22 sits 5.7 sigma above the median of the last 60 runs (1,608,873,477.06, +123.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,410.7 average over the last 60 minutes; 1,897.2 in the latest sample.
- **Total TPS:** 3,268.7 average, 3,797.4 peak. Consensus votes account for 56.8% of all transactions.
- **Slot time:** 366.7 ms average (target 400 ms), worst 1-minute bucket 379.7 ms.
- **Block height:** 418,968,957 at absolute slot 440,919,586.
- **Epoch 1020:** slot 279,586 of 432,000 (64.72% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.685% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 474 ms |
| `solana-rpc.publicnode.com` | yes | 129 ms |
| `api.mainnet.solana.com` | yes | 490 ms |

## Validators & stake

- **686 active** validators, **8 delinquent** (1.15% by count, 0.014% by stake).
- **Total stake:** 433,485,334 SOL ($40.63B); stake rate 68.52% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.93% of active stake.
- **Commission:** median 5.0%, mean 12.18%; 255 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 | 3.938% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 | 3.704% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 | 2.809% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 | 2.718% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 | 2.118% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 | 2.057% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 | 1.939% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 | 1.511% | 0% |

## Economics

- **SOL:** $93.74 (+3.96% 24h, +24.69% 7d, +20.76% 30d). Market cap $54.66B, 24h volume $8.56B (15.67% of cap). Price source: `coingecko`.
- **TVL:** $5.54B across 330 protocols - rank #2 of 462 chains, 6.37% of all tracked chain TVL. +15.00% over 7d, -58.2% from its ATH.
- **Stablecoins:** $16.42B circulating on Solana (+2.56% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.60B in 24h, $14.92B over 7d across 119 venues. Volume/TVL turnover 0.650x per day.
- **REV (chain fees):** $13.24M in 24h, $266.53M over 30d. Retained chain revenue $5.31M (40.1% of fees). Annualised fees are 8.84% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,177,044 SOL circulating of 632,639,373 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.39B | +2.4% | +23.6% |
| 2 | Kamino Lend | Lending | $1.18B | +1.8% | +12.9% |
| 3 | Jupiter Lend | Lending | $1.05B | -0.8% | +13.2% |
| 4 | Raydium AMM | Dexs | $1.04B | +3.1% | +23.5% |
| 5 | Binance Staked SOL | Liquid Staking | $941.32M | +2.3% | +22.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $935.77M | +2.7% | +24.2% |
| 7 | BlackRock BUIDL | RWA | $777.14M | +4.9% | +4.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $735.71M | -1.6% | +7.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $486.66M | +2.6% | +24.4% |
| 10 | xStocks | RWA | $421.40M | +0.8% | +10.9% |
| 11 | Solstice | Basis Trading | $404.40M | -20.1% | -20.1% |
| 12 | Sentora | Risk Curators | $366.43M | +0.8% | -0.5% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.34B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.1% · Lending 16.3% · Dexs 14.3% · RWA 12.7% · Derivatives 5.4% · Staking Pool 3.4%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.867% of chain TVL.

- BlackRock BUIDL (RWA): $777.14M
- xStocks (RWA): $421.40M
- Solstice (Basis Trading): $404.40M
- OnRe (RWA): $273.35M
- Ondo Yield Assets (RWA): $177.76M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **913.0 unique fee payers** signed per block (1,247 distinct addresses in the union, 54.5% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-21T12:20:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,382.77 | 3,268.67 | -25.42% |
| Average non-vote TPS | 2,533.88 | 1,410.74 | -44.32% |
| Average slot time (ms) | 367.50 | 366.70 | -0.22% |
| Active validators | 683.00 | 686.00 | +0.44% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,464,069,865.00 | 5,539,353,430.00 | +1.38% |
| SOL price | 90.34 | 93.74 | +3.76% |
| Stablecoin supply | 16,514,972,212.00 | 16,419,230,307.00 | -0.58% |
| 24h DEX volume | 2,770,509,439.33 | 3,600,948,276.22 | +29.97% |
| 24h chain fees | 10,987,558.08 | 13,236,625.88 | +20.47% |

### Change over 7d (vs run at 2026-08-15T12:13:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,060.94 | 3,268.67 | +6.79% |
| Average non-vote TPS | 1,416.67 | 1,410.74 | -0.42% |
| Average slot time (ms) | 415.10 | 366.70 | -11.66% |
| Active validators | 687.00 | 686.00 | -0.15% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 4,810,690,401.00 | 5,539,353,430.00 | +15.15% |
| SOL price | 75.17 | 93.74 | +24.70% |
| Stablecoin supply | 16,007,719,197.00 | 16,419,230,307.00 | +2.57% |
| 24h DEX volume | 1,612,403,611.56 | 3,600,948,276.22 | +123.33% |
| 24h chain fees | 7,971,680.79 | 13,236,625.88 | +66.05% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
