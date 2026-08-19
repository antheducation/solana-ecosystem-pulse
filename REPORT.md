# Solana Ecosystem Pulse

**Generated:** 2026-08-19T12:19:09Z · **Schema:** `1.0.0` · **Collection time:** 21.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $77.39 | +1.48% |
| Market cap | $45.12B | rank #7 |
| Total value locked | $4.91B | +1.35% |
| Stablecoin supply | $16.01B | +0.19% |
| DEX volume (24h) | $1.84B | +24.62% |
| Chain fees / REV (24h) | $8.69M | -23.00% |
| Non-vote TPS (1h avg) | 1,850 | peak 4,263 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1019 | 12.98% complete | 375,915 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 55 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,849.6 average over the last 60 minutes; 2,347.7 in the latest sample.
- **Total TPS:** 3,485.5 average, 4,263.3 peak. Consensus votes account for 46.9% of all transactions.
- **Slot time:** 414.1 ms average (target 400 ms), worst 1-minute bucket 431.7 ms.
- **Block height:** 418,314,194 at absolute slot 440,264,085.
- **Epoch 1019:** slot 56,085 of 432,000 (12.98% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.688% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 235 ms |
| `solana-rpc.publicnode.com` | yes | 254 ms |
| `api.mainnet.solana.com` | yes | 219 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.102% by stake).
- **Total stake:** 435,241,268 SOL ($33.68B); stake rate 68.81% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.91% of active stake.
- **Commission:** median 5.0%, mean 11.91%; 255 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 | 3.933% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 | 3.683% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 | 2.854% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 | 2.806% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 | 2.113% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 | 2.068% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 | 1.911% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,431 | 1.838% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,655 | 1.689% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 | 1.506% | 0% |

## Economics

- **SOL:** $77.39 (+1.48% 24h, +0.80% 7d, +0.44% 30d). Market cap $45.12B, 24h volume $1.36B (3.01% of cap). Price source: `coingecko`.
- **TVL:** $4.91B across 327 protocols - rank #2 of 461 chains, 6.45% of all tracked chain TVL. +1.06% over 7d, -62.9% from its ATH.
- **Stablecoins:** $16.01B circulating on Solana (-1.76% 7d) - $3.26 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.84B in 24h, $10.79B over 7d across 119 venues. Volume/TVL turnover 0.374x per day.
- **REV (chain fees):** $8.69M in 24h, $250.57M over 30d. Retained chain revenue $4.04M (46.4% of fees). Annualised fees are 7.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,007,334 SOL circulating of 632,514,586 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.16B | +1.9% | +3.1% |
| 2 | Kamino Lend | Lending | $1.07B | +1.5% | +2.0% |
| 3 | Jupiter Lend | Lending | $958.43M | +1.1% | +1.3% |
| 4 | Raydium AMM | Dexs | $859.90M | +1.4% | +0.9% |
| 5 | Binance Staked SOL | Liquid Staking | $782.23M | +1.5% | -0.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $772.29M | +1.7% | +1.3% |
| 7 | BlackRock BUIDL | RWA | $741.42M | +0.0% | +1.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $688.69M | +1.1% | -1.0% |
| 9 | Solstice | Basis Trading | $506.27M | +0.0% | +0.0% |
| 10 | Jupiter Staked SOL | Liquid Staking | $401.66M | +2.3% | +1.9% |
| 11 | xStocks | RWA | $383.57M | -0.1% | +1.6% |
| 12 | Sentora | Risk Curators | $366.09M | -0.3% | -0.8% |

The top five protocols hold 35.5% of Solana's tracked TVL. Summed across all 327 protocols the total is $13.63B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.7% · RWA 13.8% · Dexs 13.5% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.47B of tokenised real-world assets and equities are locked on Solana - 18.092% of chain TVL.

- BlackRock BUIDL (RWA): $741.42M
- Solstice (Basis Trading): $506.27M
- xStocks (RWA): $383.57M
- OnRe (RWA): $270.32M
- Ondo Yield Assets (RWA): $178.67M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **959.0 unique fee payers** signed per block (1,392 distinct addresses in the union, 51.6% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-18T12:19:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,644.56 | 3,485.50 | -4.36% |
| Average non-vote TPS | 1,998.19 | 1,849.57 | -7.44% |
| Average slot time (ms) | 415.20 | 414.10 | -0.26% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 4,855,232,078.00 | 4,914,919,992.00 | +1.23% |
| SOL price | 76.29 | 77.39 | +1.44% |
| Stablecoin supply | 15,976,327,308.00 | 16,008,130,055.00 | +0.20% |
| 24h DEX volume | 1,474,970,358.36 | 1,838,194,723.04 | +24.63% |
| 24h chain fees | 11,105,286.30 | 8,688,793.23 | -21.76% |

### Change over 7d (vs run at 2026-08-12T12:39:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,481.04 | 3,485.50 | +0.13% |
| Average non-vote TPS | 1,852.50 | 1,849.57 | -0.16% |
| Average slot time (ms) | 420.40 | 414.10 | -1.50% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 4,855,182,857.00 | 4,914,919,992.00 | +1.23% |
| SOL price | 76.81 | 77.39 | +0.76% |
| Stablecoin supply | 16,295,761,438.00 | 16,008,130,055.00 | -1.77% |
| 24h DEX volume | 1,650,837,789.28 | 1,838,194,723.04 | +11.35% |
| 24h chain fees | 9,897,773.23 | 8,688,793.23 | -12.21% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 20.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
