# Solana Ecosystem Pulse

**Generated:** 2026-08-10T18:39:26Z · **Schema:** `1.0.0` · **Collection time:** 14.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.80 | -1.68% |
| Market cap | $44.14B | rank #7 |
| Total value locked | $4.83B | +0.71% |
| Stablecoin supply | $16.31B | +0.35% |
| DEX volume (24h) | $1.35B | -9.76% |
| Chain fees / REV (24h) | $9.10M | -1.21% |
| Non-vote TPS (1h avg) | 2,537 | peak 5,133 total |
| Active validators | 691 | 7 delinquent |
| Epoch 1014 | 94.03% complete | 25,808 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 20 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is above its recent norm | Current 16,312,056,347.00 sits 3.8 sigma above the median of the last 20 runs (16,247,039,949.50, +0.4%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,537.3 average over the last 60 minutes; 2,218.6 in the latest sample.
- **Total TPS:** 4,162.6 average, 5,133.3 peak. Consensus votes account for 39.0% of all transactions.
- **Slot time:** 422.4 ms average (target 400 ms), worst 1-minute bucket 447.8 ms.
- **Block height:** 416,507,961 at absolute slot 438,454,192.
- **Epoch 1014:** slot 406,192 of 432,000 (94.03% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.705% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 125 ms |
| `solana-rpc.publicnode.com` | yes | 63 ms |
| `api.mainnet.solana.com` | yes | 102 ms |

## Validators & stake

- **691 active** validators, **7 delinquent** (1.00% by count, 0.007% by stake).
- **Total stake:** 434,049,016 SOL ($32.90B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.38%; 258 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,917,850 | 3.898% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,982,576 | 3.682% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,486,046 | 2.877% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,292,541 | 2.832% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,183,798 | 2.116% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,954,539 | 2.063% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,169,945 | 1.882% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,938,401 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,370,132 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,573,007 | 1.514% | 0% |

## Economics

- **SOL:** $75.80 (-1.68% 24h, +2.89% 7d, -2.86% 30d). Market cap $44.14B, 24h volume $1.41B (3.20% of cap). Price source: `coingecko`.
- **TVL:** $4.83B across 319 protocols - rank #3 of 461 chains, 6.40% of all tracked chain TVL. +2.10% over 7d, -63.5% from its ATH.
- **Stablecoins:** $16.31B circulating on Solana (+0.44% 7d) - $3.38 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.35B in 24h, $10.68B over 7d across 114 venues. Volume/TVL turnover 0.279x per day.
- **REV (chain fees):** $9.10M in 24h, $222.72M over 30d. Retained chain revenue $4.33M (47.6% of fees). Annualised fees are 7.52% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,164,969 SOL circulating of 631,882,085 total (92.13%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.12B | -1.7% | +3.5% |
| 2 | Kamino Lend | Lending | $1.05B | -0.2% | +0.9% |
| 3 | Jupiter Lend | Lending | $927.51M | +0.4% | +4.5% |
| 4 | Raydium AMM | Dexs | $849.88M | -0.6% | +4.7% |
| 5 | Binance Staked SOL | Liquid Staking | $775.55M | -1.5% | +4.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $759.12M | -1.6% | +4.0% |
| 7 | BlackRock BUIDL | RWA | $712.42M | +0.0% | +5.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $693.59M | -3.7% | -1.5% |
| 9 | Solstice | Basis Trading | $506.59M | -0.0% | -1.9% |
| 10 | Jupiter Staked SOL | Liquid Staking | $392.63M | -1.7% | +2.6% |
| 11 | xStocks | RWA | $370.41M | +0.1% | +4.2% |
| 12 | Sentora | Risk Curators | $368.87M | +0.1% | -0.2% |

The top five protocols hold 35.2% of Solana's tracked TVL. Summed across all 319 protocols the total is $13.40B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.6% · Lending 16.5% · RWA 13.7% · Dexs 13.6% · Derivatives 5.9% · Basis Trading 4.4%

### Tokenised assets

$2.42B of tokenised real-world assets and equities are locked on Solana - 18.062% of chain TVL.

- BlackRock BUIDL (RWA): $712.42M
- Solstice (Basis Trading): $506.59M
- xStocks (RWA): $370.41M
- OnRe (RWA): $254.90M
- Ondo Yield Assets (RWA): $178.38M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,068.3 unique fee payers** signed per block (1,644 distinct addresses in the union, 48.7% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT
- [Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments) - Wed, 05 Aug 2026 18:55:00 GMT
- [Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026) - Wed, 05 Aug 2026 09:33:00 GMT
- [Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle) - Tue, 04 Aug 2026 13:05:00 GMT
- [Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles) - Fri, 31 Jul 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Amend 0529](https://github.com/solana-foundation/solana-improvement-documents/pull/585) - updated 2026-08-07
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-07-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

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

### Change over 24h (vs run at 2026-08-09T18:21:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,304.40 | 4,162.64 | -3.29% |
| Average non-vote TPS | 2,694.81 | 2,537.28 | -5.85% |
| Average slot time (ms) | 426.40 | 422.40 | -0.94% |
| Active validators | 691.00 | 691.00 | +0.00% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,857,325,993.00 | 4,826,095,598.00 | -0.64% |
| SOL price | 77.09 | 75.80 | -1.67% |
| Stablecoin supply | 16,258,695,331.00 | 16,312,056,347.00 | +0.33% |
| 24h DEX volume | 1,493,144,029.54 | 1,347,434,364.98 | -9.76% |
| 24h chain fees | 9,274,886.08 | 9,097,906.09 | -1.91% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 14.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
