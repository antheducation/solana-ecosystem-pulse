# Solana Ecosystem Pulse

**Generated:** 2026-08-19T06:21:46Z · **Schema:** `1.0.0` · **Collection time:** 13.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $76.73 | +1.28% |
| Market cap | $44.73B | rank #7 |
| Total value locked | $4.89B | +0.89% |
| Stablecoin supply | $16.01B | +0.20% |
| DEX volume (24h) | $1.82B | +23.44% |
| Chain fees / REV (24h) | $8.71M | -22.77% |
| Non-vote TPS (1h avg) | 1,330 | peak 4,037 total |
| Active validators | 676 | 19 delinquent |
| Epoch 1019 | 1.03% complete | 427,557 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 54 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Active validators is below its recent norm | Current 676.00 sits 5.8 sigma below the median of the last 54 runs (689.00, -1.9%). | `zscore` |
| [SERIOUS] | Delinquent validators is above its recent norm | Current 19.00 sits 7.4 sigma above the median of the last 54 runs (8.00, +137.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,329.7 average over the last 60 minutes; 1,122.3 in the latest sample.
- **Total TPS:** 2,957.2 average, 4,036.7 peak. Consensus votes account for 55.0% of all transactions.
- **Slot time:** 415.4 ms average (target 400 ms), worst 1-minute bucket 451.1 ms.
- **Block height:** 418,262,640 at absolute slot 440,212,443.
- **Epoch 1019:** slot 4,443 of 432,000 (1.03% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 122 ms |
| `solana-rpc.publicnode.com` | yes | 95 ms |
| `api.mainnet.solana.com` | yes | 100 ms |

## Validators & stake

- **676 active** validators, **19 delinquent** (2.73% by count, 0.170% by stake).
- **Total stake:** 435,241,268 SOL ($33.40B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.42% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 11.88%; 252 validators at 0% and 59 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.936% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.685% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.856% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.808% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.115% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.069% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.912% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.839% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.690% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.507% | 0% |

## Economics

- **SOL:** $76.73 (+1.28% 24h, +0.62% 7d, +1.15% 30d). Market cap $44.73B, 24h volume $1.34B (3.00% of cap). Price source: `coingecko`.
- **TVL:** $4.89B across 326 protocols - rank #2 of 461 chains, 6.43% of all tracked chain TVL. +0.64% over 7d, -63.0% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.75% 7d) - $3.27 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.82B in 24h, $10.65B over 7d across 119 venues. Volume/TVL turnover 0.372x per day.
- **REV (chain fees):** $8.71M in 24h, $249.95M over 30d. Retained chain revenue $4.03M (46.3% of fees). Annualised fees are 7.11% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,007,509 SOL circulating of 632,514,762 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.15B | +1.4% | +2.3% |
| 2 | Kamino Lend | Lending | $1.07B | +1.2% | +1.6% |
| 3 | Jupiter Lend | Lending | $953.12M | +0.9% | +0.7% |
| 4 | Raydium AMM | Dexs | $855.40M | +1.4% | +0.4% |
| 5 | Binance Staked SOL | Liquid Staking | $776.14M | +0.8% | -0.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $769.18M | +1.4% | +0.9% |
| 7 | BlackRock BUIDL | RWA | $741.42M | +0.0% | +1.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $685.43M | +0.6% | -1.5% |
| 9 | Solstice | Basis Trading | $506.20M | +0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $398.45M | +1.5% | +1.1% |
| 11 | xStocks | RWA | $380.95M | -1.5% | +0.9% |
| 12 | Sentora | Risk Curators | $366.10M | -0.3% | -0.8% |

The top five protocols hold 35.4% of Solana's tracked TVL. Summed across all 326 protocols the total is $13.57B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.7% · Lending 16.7% · RWA 13.8% · Dexs 13.5% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 18.122% of chain TVL.

- BlackRock BUIDL (RWA): $741.42M
- Solstice (Basis Trading): $506.20M
- xStocks (RWA): $380.95M
- OnRe (RWA): $269.41M
- Ondo Yield Assets (RWA): $179.08M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **836.0 unique fee payers** signed per block (1,051 distinct addresses in the union, 58.1% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-19
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

### Change over 24h (vs run at 2026-08-18T06:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,904.51 | 2,957.15 | +1.81% |
| Average non-vote TPS | 1,251.49 | 1,329.70 | +6.25% |
| Average slot time (ms) | 417.00 | 415.40 | -0.38% |
| Active validators | 689.00 | 676.00 | -1.89% |
| Delinquent validators | 6.00 | 19.00 | +216.67% |
| Solana TVL | 4,846,663,986.00 | 4,894,911,440.00 | +1.00% |
| SOL price | 75.81 | 76.73 | +1.21% |
| Stablecoin supply | 15,980,255,447.00 | 16,009,559,610.00 | +0.18% |
| 24h DEX volume | 1,425,243,228.36 | 1,820,756,097.04 | +27.75% |
| 24h chain fees | 10,772,677.30 | 8,714,303.23 | -19.11% |

### Change over 7d (vs run at 2026-08-12T07:03:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,492.30 | 2,957.15 | -34.17% |
| Average non-vote TPS | 2,077.67 | 1,329.70 | -36.00% |
| Average slot time (ms) | 367.10 | 415.40 | +13.16% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 11.00 | 19.00 | +72.73% |
| Solana TVL | 4,844,614,677.00 | 4,894,911,440.00 | +1.04% |
| SOL price | 75.98 | 76.73 | +0.99% |
| Stablecoin supply | 16,295,779,878.00 | 16,009,559,610.00 | -1.76% |
| 24h DEX volume | 1,652,160,307.28 | 1,820,756,097.04 | +10.20% |
| 24h chain fees | 9,847,992.23 | 8,714,303.23 | -11.51% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 13.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
