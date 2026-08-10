# Solana Ecosystem Pulse

**Generated:** 2026-08-10T07:04:38Z · **Schema:** `1.0.0` · **Collection time:** 25.9s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $76.90 | +0.75% |
| Market cap | $44.77B | rank #7 |
| Total value locked | $4.85B | +1.29% |
| Stablecoin supply | $16.31B | +0.36% |
| DEX volume (24h) | $1.37B | -8.39% |
| Chain fees / REV (24h) | $8.76M | -4.88% |
| Non-vote TPS (1h avg) | 1,387 | peak 3,630 total |
| Active validators | 690 | 8 delinquent |
| Epoch 1014 | 71.19% complete | 124,480 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 18 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 4,854,070,595.00 sits 3.1 sigma above the median of the last 18 runs (4,740,035,266.00, +2.4%). | `zscore` |
| [WARNING] | Stablecoin supply is above its recent norm | Current 16,314,454,803.00 sits 3.6 sigma above the median of the last 18 runs (16,243,802,494.00, +0.4%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.2.0-rc.1. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,386.8 average over the last 60 minutes; 1,155.1 in the latest sample.
- **Total TPS:** 3,002.2 average, 3,629.7 peak. Consensus votes account for 53.8% of all transactions.
- **Slot time:** 424.1 ms average (target 400 ms), worst 1-minute bucket 451.1 ms.
- **Block height:** 416,409,349 at absolute slot 438,355,520.
- **Epoch 1014:** slot 307,520 of 432,000 (71.19% complete).
- **Client:** agave `4.2.0-rc.1`, feature set `4119855713`. Inflation 3.705% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 172 ms |
| `solana-rpc.publicnode.com` | yes | 147 ms |
| `api.mainnet.solana.com` | yes | 159 ms |

## Validators & stake

- **690 active** validators, **8 delinquent** (1.15% by count, 0.010% by stake).
- **Total stake:** 434,049,016 SOL ($33.38B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.40%; 257 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,917,850 | 3.898% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,982,576 | 3.683% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,486,046 | 2.877% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,292,541 | 2.832% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,183,798 | 2.116% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,954,539 | 2.063% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,169,945 | 1.882% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,938,401 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,370,132 | 1.698% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,573,007 | 1.515% | 0% |

## Economics

- **SOL:** $76.90 (+0.75% 24h, +6.03% 7d, -1.41% 30d). Market cap $44.77B, 24h volume $1.18B (2.64% of cap). Price source: `coingecko`.
- **TVL:** $4.85B across 321 protocols - rank #3 of 461 chains, 6.39% of all tracked chain TVL. +2.69% over 7d, -63.2% from its ATH.
- **Stablecoins:** $16.31B circulating on Solana (+0.46% 7d) - $3.36 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.37B in 24h, $10.55B over 7d across 114 venues. Volume/TVL turnover 0.282x per day.
- **REV (chain fees):** $8.76M in 24h, $219.34M over 30d. Retained chain revenue $4.26M (48.6% of fees). Annualised fees are 7.14% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,165,378 SOL circulating of 631,882,494 total (92.13%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | +0.9% | +4.4% |
| 2 | Kamino Lend | Lending | $1.06B | +1.6% | +1.5% |
| 3 | Jupiter Lend | Lending | $919.43M | +0.5% | +3.6% |
| 4 | Raydium AMM | Dexs | $850.23M | +1.3% | +4.8% |
| 5 | Binance Staked SOL | Liquid Staking | $782.90M | +1.0% | +5.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $765.70M | +1.2% | +4.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $715.92M | +0.5% | +1.7% |
| 8 | BlackRock BUIDL | RWA | $712.22M | +0.0% | +5.5% |
| 9 | Solstice | Basis Trading | $506.64M | +0.0% | -1.9% |
| 10 | Jupiter Staked SOL | Liquid Staking | $396.35M | +0.8% | +3.6% |
| 11 | xStocks | RWA | $373.19M | +0.5% | +5.0% |
| 12 | Sentora | Risk Curators | $368.30M | +0.2% | -0.4% |

The top five protocols hold 35.2% of Solana's tracked TVL. Summed across all 321 protocols the total is $13.46B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.7% · Lending 16.4% · RWA 13.6% · Dexs 13.5% · Derivatives 6.1% · Basis Trading 4.4%

### Tokenised assets

$2.42B of tokenised real-world assets and equities are locked on Solana - 17.964% of chain TVL.

- BlackRock BUIDL (RWA): $712.22M
- Solstice (Basis Trading): $506.64M
- xStocks (RWA): $373.19M
- OnRe (RWA): $252.22M
- Ondo Yield Assets (RWA): $178.56M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **933.0 unique fee payers** signed per block (1,288 distinct addresses in the union, 54.0% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-09T06:34:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,072.08 | 3,002.24 | -2.27% |
| Average non-vote TPS | 1,436.52 | 1,386.84 | -3.46% |
| Average slot time (ms) | 419.70 | 424.10 | +1.05% |
| Active validators | 691.00 | 690.00 | -0.14% |
| Delinquent validators | 7.00 | 8.00 | +14.29% |
| Solana TVL | 4,805,634,165.00 | 4,854,070,595.00 | +1.01% |
| SOL price | 76.26 | 76.90 | +0.84% |
| Stablecoin supply | 16,258,503,935.00 | 16,314,454,803.00 | +0.34% |
| 24h DEX volume | 1,477,664,041.54 | 1,367,879,871.98 | -7.43% |
| 24h chain fees | 9,154,077.08 | 8,759,843.77 | -4.31% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 25.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
