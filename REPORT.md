# Solana Ecosystem Pulse

**Generated:** 2026-08-16T06:18:33Z · **Schema:** `1.0.0` · **Collection time:** 12.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.29 | +0.04% |
| Market cap | $43.87B | rank #7 |
| Total value locked | $4.81B | -0.08% |
| Stablecoin supply | $16.00B | -0.04% |
| DEX volume (24h) | $1.23B | -23.08% |
| Chain fees / REV (24h) | $8.08M | +0.32% |
| Non-vote TPS (1h avg) | 1,107 | peak 3,061 total |
| Active validators | 688 | 9 delinquent |
| Epoch 1017 | 56.49% complete | 187,956 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 42 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 16,002,608,919.00 sits 3.1 sigma below the median of the last 42 runs (16,243,802,494.00, -1.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,107.3 average over the last 60 minutes; 1,058.6 in the latest sample.
- **Total TPS:** 2,746.3 average, 3,061.2 peak. Consensus votes account for 59.7% of all transactions.
- **Slot time:** 417.3 ms average (target 400 ms), worst 1-minute bucket 461.5 ms.
- **Block height:** 417,638,649 at absolute slot 439,588,044.
- **Epoch 1017:** slot 244,044 of 432,000 (56.49% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.695% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 83 ms |
| `solana-rpc.publicnode.com` | yes | 63 ms |
| `api.mainnet.solana.com` | yes | 41 ms |

## Validators & stake

- **688 active** validators, **9 delinquent** (1.29% by count, 0.017% by stake).
- **Total stake:** 435,491,340 SOL ($32.79B); stake rate 68.88% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.30%; 255 validators at 0% and 63 at 100%.

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

- **SOL:** $75.29 (+0.04% 24h, -0.85% 7d, +1.27% 30d). Market cap $43.87B, 24h volume $583.55M (1.33% of cap). Price source: `coingecko`.
- **TVL:** $4.81B across 325 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. +0.11% over 7d, -63.6% from its ATH.
- **Stablecoins:** $16.00B circulating on Solana (-1.61% 7d) - $3.33 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.23B in 24h, $10.90B over 7d across 117 venues. Volume/TVL turnover 0.257x per day.
- **REV (chain fees):** $8.08M in 24h, $241.19M over 30d. Retained chain revenue $3.21M (39.7% of fees). Annualised fees are 6.72% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,784,707 SOL circulating of 632,261,617 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | -0.2% | +0.8% |
| 2 | Kamino Lend | Lending | $1.04B | -0.6% | +1.6% |
| 3 | Jupiter Lend | Lending | $928.97M | +0.4% | +1.5% |
| 4 | Raydium AMM | Dexs | $842.14M | -0.3% | +0.4% |
| 5 | Binance Staked SOL | Liquid Staking | $766.81M | -0.2% | -1.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $754.87M | -0.0% | -0.2% |
| 7 | BlackRock BUIDL | RWA | $740.96M | +0.0% | +4.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $682.72M | -0.2% | -4.2% |
| 9 | Solstice | Basis Trading | $506.09M | +0.0% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $391.21M | -0.1% | -0.5% |
| 11 | xStocks | RWA | $383.60M | +0.9% | +1.8% |
| 12 | Sentora | Risk Curators | $368.08M | -0.0% | +0.1% |

The top five protocols hold 35.0% of Solana's tracked TVL. Summed across all 325 protocols the total is $13.46B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.9% · Lending 16.4% · RWA 13.9% · Dexs 13.4% · Derivatives 5.8% · Basis Trading 4.3%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 18.270% of chain TVL.

- BlackRock BUIDL (RWA): $740.96M
- Solstice (Basis Trading): $506.09M
- xStocks (RWA): $383.60M
- OnRe (RWA): $261.48M
- Ondo Yield Assets (RWA): $178.89M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **910.7 unique fee payers** signed per block (1,245 distinct addresses in the union, 54.4% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-15T06:16:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,806.28 | 2,746.35 | -2.14% |
| Average non-vote TPS | 1,187.72 | 1,107.30 | -6.77% |
| Average slot time (ms) | 416.00 | 417.30 | +0.31% |
| Active validators | 687.00 | 688.00 | +0.15% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 4,820,764,054.00 | 4,812,235,963.00 | -0.18% |
| SOL price | 75.27 | 75.29 | +0.03% |
| Stablecoin supply | 16,009,820,741.00 | 16,002,608,919.00 | -0.05% |
| 24h DEX volume | 1,642,311,971.56 | 1,234,854,042.04 | -24.81% |
| 24h chain fees | 8,004,118.79 | 8,078,661.86 | +0.93% |

### Change over 7d (vs run at 2026-08-09T06:34:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,072.08 | 2,746.35 | -10.60% |
| Average non-vote TPS | 1,436.52 | 1,107.30 | -22.92% |
| Average slot time (ms) | 419.70 | 417.30 | -0.57% |
| Active validators | 691.00 | 688.00 | -0.43% |
| Delinquent validators | 7.00 | 9.00 | +28.57% |
| Solana TVL | 4,805,634,165.00 | 4,812,235,963.00 | +0.14% |
| SOL price | 76.26 | 75.29 | -1.27% |
| Stablecoin supply | 16,258,503,935.00 | 16,002,608,919.00 | -1.57% |
| 24h DEX volume | 1,477,664,041.54 | 1,234,854,042.04 | -16.43% |
| 24h chain fees | 9,154,077.08 | 8,078,661.86 | -11.75% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
