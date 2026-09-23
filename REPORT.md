# Solana Ecosystem Pulse

**Generated:** 2026-09-23T15:39:57Z · **Schema:** `1.0.0` · **Collection time:** 39.6s · **Sources OK:** 39/39

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $114.88 | -1.96% |
| Market cap | $67.48B | rank #7 |
| Total value locked | $6.44B | -0.34% |
| Stablecoin supply | $16.88B | -1.70% |
| DEX volume (24h) | $3.20B | -6.82% |
| Chain fees / REV (24h) | $17.87M | -4.10% |
| Non-vote TPS (1h avg) | 2,345 | peak 5,529 total |
| Active validators | 674 | 13 delinquent |
| Epoch 1041 | 8.00% complete | 397,426 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 91 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.40 sits 11.8 sigma below the median of the last 91 runs (316.50, -15.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,345.0 average over the last 60 minutes; 2,052.4 in the latest sample.
- **Total TPS:** 4,849.8 average, 5,529.3 peak. Consensus votes account for 51.6% of all transactions.
- **Slot time:** 267.4 ms average (target 400 ms), worst 1-minute bucket 281.7 ms.
- **Block height:** 427,786,789 at absolute slot 449,746,574.
- **Epoch 1041:** slot 34,574 of 432,000 (8.00% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 731 ms |
| `solana-rpc.publicnode.com` | yes | 217 ms |
| `api.mainnet.solana.com` | yes | 756 ms |

## Validators & stake

- **674 active** validators, **13 delinquent** (1.89% by count, 0.054% by stake).
- **Total stake:** 439,964,137 SOL ($50.54B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.88% of active stake.
- **Commission:** median 5.0%, mean 12.32%; 235 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.058% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.350% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.098% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.083% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.729% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.491% | 0% |

## Economics

- **SOL:** $114.88 (-1.96% 24h, +18.51% 7d, +19.61% 30d). Market cap $67.48B, 24h volume $5.12B (7.59% of cap). Price source: `coingecko`.
- **TVL:** $6.44B across 332 protocols - rank #2 of 467 chains, 6.72% of all tracked chain TVL. +12.44% over 7d, -51.4% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+5.73% 7d) - $2.62 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.20B in 24h, $21.22B over 7d across 125 venues. Volume/TVL turnover 0.496x per day.
- **REV (chain fees):** $17.87M in 24h, $433.84M over 30d. Retained chain revenue $6.78M (38.0% of fees). Annualised fees are 9.67% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,578,055 SOL circulating of 634,609,178 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.86B | -0.2% | +21.1% |
| 2 | Kamino Lend | Lending | $1.40B | -1.8% | +5.2% |
| 3 | Raydium AMM | Dexs | $1.33B | +0.3% | +21.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.21B | +0.2% | +21.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | -0.2% | +19.0% |
| 6 | Jupiter Lend | Lending | $1.19B | +0.3% | +9.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $797.70M | -1.9% | +9.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $604.00M | +0.1% | +20.2% |
| 9 | Marinade Native | Staking Pool | $448.88M | +0.5% | +21.3% |
| 10 | PumpSwap | Dexs | $382.55M | +0.8% | +21.9% |
| 11 | Sentora Curator | Risk Curators | $362.18M | -0.2% | -5.5% |
| 12 | Drift Staked SOL | Liquid Staking | $320.53M | -2.5% | +17.2% |

The top five protocols hold 42.2% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.60B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 17.3% · Dexs 16.0% · Derivatives 5.2% · Staking Pool 4.0% · Risk Curators 3.5%

### Tokenised assets

$832.37M of tokenised real-world assets and equities are locked on Solana - 5.015% of chain TVL.

- OnRe (RWA): $303.04M
- Solstice (Basis Trading): $218.04M
- Huma Finance V2 (RWA): $195.31M
- JupUSD (Basis Trading): $45.08M
- Plume Vaults (RWA): $28.20M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 1 sampled blocks, an average of **837.0 unique fee payers** signed per block (837 distinct addresses in the union, 0.0% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0249: SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23
- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-22T15:50:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,849.16 | 4,849.84 | +0.01% |
| Average non-vote TPS | 2,344.69 | 2,345.00 | +0.01% |
| Average slot time (ms) | 268.40 | 267.40 | -0.37% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 13.00 | 13.00 | +0.00% |
| Solana TVL | 6,467,273,208.00 | 6,436,874,885.00 | -0.47% |
| SOL price | 117.67 | 114.88 | -2.37% |
| Stablecoin supply | 17,171,768,101.00 | 16,879,859,425.00 | -1.70% |
| 24h DEX volume | 3,428,858,820.75 | 3,195,015,036.76 | -6.82% |
| 24h chain fees | 18,642,402.21 | 17,874,880.76 | -4.12% |

### Change over 7d (vs run at 2026-09-16T15:39:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,416.76 | 4,849.84 | +9.81% |
| Average non-vote TPS | 2,284.69 | 2,345.00 | +2.64% |
| Average slot time (ms) | 316.20 | 267.40 | -15.43% |
| Active validators | 677.00 | 674.00 | -0.44% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,706,209,621.00 | 6,436,874,885.00 | +12.80% |
| SOL price | 97.09 | 114.88 | +18.32% |
| Stablecoin supply | 15,965,868,554.00 | 16,879,859,425.00 | +5.72% |
| 24h DEX volume | 2,703,297,666.22 | 3,195,015,036.76 | +18.19% |
| 24h chain fees | 14,083,156.46 | 17,874,880.76 | +26.92% |

### Change over 30d (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,849.84 | +6.17% |
| Average non-vote TPS | 2,714.40 | 2,345.00 | -13.61% |
| Average slot time (ms) | 367.20 | 267.40 | -27.18% |
| Active validators | 685.00 | 674.00 | -1.61% |
| Delinquent validators | 10.00 | 13.00 | +30.00% |
| Solana TVL | 5,621,355,422.00 | 6,436,874,885.00 | +14.51% |
| SOL price | 96.29 | 114.88 | +19.31% |
| Stablecoin supply | 16,453,918,497.00 | 16,879,859,425.00 | +2.59% |
| 24h DEX volume | 2,938,613,605.25 | 3,195,015,036.76 | +8.73% |
| 24h chain fees | 12,654,048.70 | 17,874,880.76 | +41.26% |

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

This run made 39 HTTP calls (39 succeeded, 0 failed) in 39.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
