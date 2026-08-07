# Solana Ecosystem Pulse

**Generated:** 2026-08-07T01:58:58Z · **Schema:** `1.0.0` · **Collection time:** 33.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $72.62 | -1.50% |
| Market cap | $42.28B | rank #7 |
| Total value locked | $4.71B | -0.83% |
| Stablecoin supply | $16.20B | -2.13% |
| DEX volume (24h) | $1.40B | -14.50% |
| Chain fees / REV (24h) | $8.68M | +11.57% |
| Non-vote TPS (1h avg) | 1,576 | peak 3,623 total |
| Active validators | 693 | 7 delinquent |
| Epoch 1013 | 19.09% complete | 349,532 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 5 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 3,201.12 sits 225.9 sigma below the median of the last 5 runs (3,780.53, -15.3%). | `zscore` |
| [SERIOUS] | Average non-vote TPS is below its recent norm | Current 1,575.79 sits 136.1 sigma below the median of the last 5 runs (2,157.08, -26.9%). | `zscore` |
| [SERIOUS] | Solana TVL is below its recent norm | Current 4,710,298,956.00 sits 764.5 sigma below the median of the last 5 runs (4,740,035,266.00, -0.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,575.8 average over the last 60 minutes; 1,506.0 in the latest sample.
- **Total TPS:** 3,201.1 average, 3,623.2 peak. Consensus votes account for 50.8% of all transactions.
- **Slot time:** 423.2 ms average (target 400 ms), worst 1-minute bucket 454.5 ms.
- **Block height:** 415,752,718 at absolute slot 437,698,468.
- **Epoch 1013:** slot 82,468 of 432,000 (19.09% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.708% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 741 ms |
| `solana-rpc.publicnode.com` | yes | 122 ms |
| `api.mainnet.solana.com` | yes | 700 ms |

## Validators & stake

- **693 active** validators, **7 delinquent** (1.00% by count, 0.000% by stake).
- **Total stake:** 434,839,888 SOL ($31.58B); stake rate 68.83% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.36% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.20%; 261 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,882,234 | 3.882% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,996,914 | 3.679% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,487,724 | 2.872% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,275,239 | 2.823% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,139,569 | 2.102% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,868,459 | 2.039% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,166,427 | 1.878% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,921,632 | 1.822% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,637,450 | 1.756% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,569,156 | 1.511% | 0% |

## Economics

- **SOL:** $72.62 (-1.50% 24h, -2.70% 7d, -9.58% 30d). Market cap $42.28B, 24h volume $1.43B (3.38% of cap). Price source: `coingecko`.
- **TVL:** $4.71B across 321 protocols - rank #4 of 461 chains, 6.25% of all tracked chain TVL. -2.13% over 7d, -64.3% from its ATH.
- **Stablecoins:** $16.20B circulating on Solana (-0.94% 7d) - $3.44 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.40B in 24h, $10.69B over 7d across 114 venues. Volume/TVL turnover 0.297x per day.
- **REV (chain fees):** $8.68M in 24h, $214.57M over 30d. Retained chain revenue $3.75M (43.3% of fees). Annualised fees are 7.49% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,052,264 SOL circulating of 631,756,884 total (92.13%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.07B | -1.9% | -2.1% |
| 2 | Kamino Lend | Lending | $1.02B | -2.3% | -2.5% |
| 3 | Jupiter Lend | Lending | $911.62M | -2.8% | -2.3% |
| 4 | Raydium AMM | Dexs | $806.41M | -1.7% | -2.7% |
| 5 | Binance Staked SOL | Liquid Staking | $737.56M | -2.2% | -2.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $721.91M | -1.9% | -2.5% |
| 7 | BlackRock BUIDL | RWA | $697.09M | +1.7% | +6.6% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $695.81M | -1.6% | -2.2% |
| 9 | Solstice | Basis Trading | $506.55M | +0.0% | -3.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $378.30M | -1.9% | -2.3% |
| 11 | Sentora | Risk Curators | $369.01M | -0.7% | +0.2% |
| 12 | xStocks | RWA | $366.39M | -0.2% | +1.8% |

The top five protocols hold 34.9% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.02B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.0% · Lending 16.6% · RWA 13.9% · Dexs 13.4% · Derivatives 6.1% · Basis Trading 4.5%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 18.402% of chain TVL.

- BlackRock BUIDL (RWA): $697.09M
- Solstice (Basis Trading): $506.55M
- xStocks (RWA): $366.39M
- OnRe (RWA): $251.59M
- Ondo Yield Assets (RWA): $178.58M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,044.3 unique fee payers** signed per block (1,601 distinct addresses in the union, 48.9% overlap between blocks).

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
| [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) | 2026-08-05 | pre-release |
| [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) | 2026-07-31 | stable |
| [v4.2.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.0) | 2026-07-24 | stable |
| [v4.3.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.2) | 2026-07-21 | pre-release |
| [v4.2.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-beta.2) | 2026-07-17 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-08-03
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-07-29
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-07-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22

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

History exists but is younger than the shortest comparison window (24h).

Source-provided change windows are still available above (24h / 7d / 30d on price, TVL, stablecoins, DEX volume and fees), so the report is never blind on a first run.

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 33.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
