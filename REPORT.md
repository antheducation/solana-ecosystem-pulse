# Solana Ecosystem Pulse

**Generated:** 2026-08-17T18:19:42Z · **Schema:** `1.0.0` · **Collection time:** 35.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.94 | +1.13% |
| Market cap | $44.26B | rank #7 |
| Total value locked | $4.85B | +0.85% |
| Stablecoin supply | $16.00B | +0.03% |
| DEX volume (24h) | $1.06B | -9.71% |
| Chain fees / REV (24h) | $6.80M | -16.49% |
| Non-vote TPS (1h avg) | 2,782 | peak 5,077 total |
| Active validators | 688 | 7 delinquent |
| Epoch 1018 | 28.74% complete | 307,843 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 48 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,781.6 average over the last 60 minutes; 2,950.9 in the latest sample.
- **Total TPS:** 4,422.3 average, 5,077.1 peak. Consensus votes account for 37.1% of all transactions.
- **Slot time:** 415.7 ms average (target 400 ms), worst 1-minute bucket 434.8 ms.
- **Block height:** 417,950,622 at absolute slot 439,900,157.
- **Epoch 1018:** slot 124,157 of 432,000 (28.74% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.692% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 760 ms |
| `solana-rpc.publicnode.com` | yes | 59 ms |
| `api.mainnet.solana.com` | yes | 821 ms |

## Validators & stake

- **688 active** validators, **7 delinquent** (1.01% by count, 0.083% by stake).
- **Total stake:** 435,676,796 SOL ($33.09B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.01%; 256 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,091,057 | 3.926% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,003,006 | 3.676% | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,495,360 | 2.870% | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,259,520 | 2.816% | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,203,436 | 2.114% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,992,381 | 2.066% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,305,834 | 1.908% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,983,993 | 1.834% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,342,590 | 1.687% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,588,037 | 1.513% | 0% |

## Economics

- **SOL:** $75.94 (+1.13% 24h, +0.03% 7d, +0.84% 30d). Market cap $44.26B, 24h volume $1.31B (2.96% of cap). Price source: `coingecko`.
- **TVL:** $4.85B across 325 protocols - rank #3 of 461 chains, 6.41% of all tracked chain TVL. -0.09% over 7d, -63.4% from its ATH.
- **Stablecoins:** $16.00B circulating on Solana (-1.92% 7d) - $3.30 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.06B in 24h, $10.69B over 7d across 117 venues. Volume/TVL turnover 0.218x per day.
- **REV (chain fees):** $6.80M in 24h, $242.40M over 30d. Retained chain revenue $3.35M (49.3% of fees). Annualised fees are 5.61% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 582,896,033 SOL circulating of 632,388,292 total (92.17%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.13B | +0.4% | +0.9% |
| 2 | Kamino Lend | Lending | $1.06B | +1.9% | +1.0% |
| 3 | Jupiter Lend | Lending | $936.11M | +0.9% | +1.8% |
| 4 | Raydium AMM | Dexs | $845.93M | +0.3% | -0.1% |
| 5 | Binance Staked SOL | Liquid Staking | $770.05M | +0.3% | -1.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $759.92M | +0.6% | -0.5% |
| 7 | BlackRock BUIDL | RWA | $741.17M | +0.0% | +4.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $681.16M | +0.0% | -4.7% |
| 9 | Solstice | Basis Trading | $506.20M | +0.1% | -0.1% |
| 10 | Jupiter Staked SOL | Liquid Staking | $392.61M | +0.2% | -0.6% |
| 11 | xStocks | RWA | $388.99M | +1.2% | +5.0% |
| 12 | Sentora | Risk Curators | $367.36M | -0.1% | -0.2% |

The top five protocols hold 35.1% of Solana's tracked TVL. Summed across all 325 protocols the total is $13.53B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 32.8% · Lending 16.5% · RWA 13.9% · Dexs 13.4% · Derivatives 5.7% · Basis Trading 4.3%

### Tokenised assets

$2.47B of tokenised real-world assets and equities are locked on Solana - 18.245% of chain TVL.

- BlackRock BUIDL (RWA): $741.17M
- Solstice (Basis Trading): $506.20M
- xStocks (RWA): $388.99M
- OnRe (RWA): $266.62M
- Ondo Yield Assets (RWA): $178.97M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,085.7 unique fee payers** signed per block (1,659 distinct addresses in the union, 49.1% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) - Wed, 12 Aug 2026 12:57:00 GMT
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) - Tue, 11 Aug 2026 10:00:00 GMT
- [Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026) - Thu, 06 Aug 2026 17:57:00 GMT

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

### Change over 24h (vs run at 2026-08-16T18:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,797.96 | 4,422.32 | +16.44% |
| Average non-vote TPS | 2,151.97 | 2,781.61 | +29.26% |
| Average slot time (ms) | 415.20 | 415.70 | +0.12% |
| Active validators | 688.00 | 688.00 | +0.00% |
| Delinquent validators | 9.00 | 7.00 | -22.22% |
| Solana TVL | 4,804,122,508.00 | 4,849,572,817.00 | +0.95% |
| SOL price | 75.15 | 75.94 | +1.05% |
| Stablecoin supply | 15,997,960,401.00 | 16,003,787,085.00 | +0.04% |
| 24h DEX volume | 1,169,008,711.04 | 1,055,467,633.95 | -9.71% |
| 24h chain fees | 8,145,711.86 | 6,802,409.48 | -16.49% |

### Change over 7d (vs run at 2026-08-10T18:39:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,162.64 | 4,422.32 | +6.24% |
| Average non-vote TPS | 2,537.28 | 2,781.61 | +9.63% |
| Average slot time (ms) | 422.40 | 415.70 | -1.59% |
| Active validators | 691.00 | 688.00 | -0.43% |
| Delinquent validators | 7.00 | 7.00 | +0.00% |
| Solana TVL | 4,826,095,598.00 | 4,849,572,817.00 | +0.49% |
| SOL price | 75.80 | 75.94 | +0.18% |
| Stablecoin supply | 16,312,056,347.00 | 16,003,787,085.00 | -1.89% |
| 24h DEX volume | 1,347,434,364.98 | 1,055,467,633.95 | -21.67% |
| 24h chain fees | 9,097,906.09 | 6,802,409.48 | -25.23% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 35.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
