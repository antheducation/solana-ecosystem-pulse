# Solana Ecosystem Pulse

**Generated:** 2026-09-23T20:45:40Z · **Schema:** `1.0.0` · **Collection time:** 14.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $114.36 | -3.23% |
| Market cap | $67.20B | rank #7 |
| Total value locked | $6.39B | -1.11% |
| Stablecoin supply | $16.88B | -1.70% |
| DEX volume (24h) | $3.20B | -6.82% |
| Chain fees / REV (24h) | $17.87M | -4.10% |
| Non-vote TPS (1h avg) | 2,212 | peak 5,468 total |
| Active validators | 674 | 13 delinquent |
| Epoch 1041 | 23.97% complete | 328,436 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 91 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 265.30 sits 10.8 sigma below the median of the last 91 runs (316.50, -16.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,211.7 average over the last 60 minutes; 2,470.2 in the latest sample.
- **Total TPS:** 4,742.0 average, 5,468.2 peak. Consensus votes account for 53.4% of all transactions.
- **Slot time:** 265.3 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 427,855,749 at absolute slot 449,815,564.
- **Epoch 1041:** slot 103,564 of 432,000 (23.97% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 106 ms |
| `solana-rpc.publicnode.com` | yes | 148 ms |
| `api.mainnet.solana.com` | yes | 84 ms |

## Validators & stake

- **674 active** validators, **13 delinquent** (1.89% by count, 0.073% by stake).
- **Total stake:** 439,964,137 SOL ($50.31B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.88% of active stake.
- **Commission:** median 5.0%, mean 12.32%; 236 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.059% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.603% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.351% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.099% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.083% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.729% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.613% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.492% | 0% |

## Economics

- **SOL:** $114.36 (-3.23% 24h, +16.64% 7d, +18.43% 30d). Market cap $67.20B, 24h volume $5.17B (7.70% of cap). Price source: `coingecko`.
- **TVL:** $6.39B across 331 protocols - rank #2 of 467 chains, 6.74% of all tracked chain TVL. +11.57% over 7d, -51.8% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+5.73% 7d) - $2.64 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.20B in 24h, $21.22B over 7d across 125 venues. Volume/TVL turnover 0.500x per day.
- **REV (chain fees):** $17.87M in 24h, $433.84M over 30d. Retained chain revenue $6.78M (38.0% of fees). Annualised fees are 9.71% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,577,826 SOL circulating of 634,608,948 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | -2.1% | +20.2% |
| 2 | Kamino Lend | Lending | $1.40B | -2.0% | +5.5% |
| 3 | Raydium AMM | Dexs | $1.31B | -1.7% | +19.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.19B | -3.4% | +18.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.17B | -3.2% | +16.4% |
| 6 | Jupiter Lend | Lending | $1.17B | -1.1% | +8.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $801.39M | -2.6% | +9.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $593.28M | -3.3% | +18.1% |
| 9 | Marinade Native | Staking Pool | $440.02M | -2.4% | +18.9% |
| 10 | PumpSwap | Dexs | $373.97M | -2.1% | +19.2% |
| 11 | Sentora Curator | Risk Curators | $362.32M | -0.2% | -5.4% |
| 12 | Drift Staked SOL | Liquid Staking | $322.93M | -3.4% | +18.1% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.46B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.3% · Dexs 15.9% · Derivatives 5.3% · Staking Pool 4.0% · Risk Curators 3.5%

### Tokenised assets

$837.90M of tokenised real-world assets and equities are locked on Solana - 5.090% of chain TVL.

- OnRe (RWA): $303.06M
- Solstice (Basis Trading): $218.04M
- Huma Finance V2 (RWA): $197.04M
- JupUSD (Basis Trading): $45.09M
- Plume Vaults (RWA): $28.21M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

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

- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0249: SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23
- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-22T20:34:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,893.52 | 4,741.96 | -3.10% |
| Average non-vote TPS | 2,379.33 | 2,211.74 | -7.04% |
| Average slot time (ms) | 268.00 | 265.30 | -1.01% |
| Active validators | 677.00 | 674.00 | -0.44% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 6,505,534,933.00 | 6,385,088,886.00 | -1.85% |
| SOL price | 118.17 | 114.36 | -3.22% |
| Stablecoin supply | 17,173,484,924.00 | 16,880,373,729.00 | -1.71% |
| 24h DEX volume | 3,428,858,820.75 | 3,195,015,036.76 | -6.82% |
| 24h chain fees | 18,642,402.21 | 17,874,880.76 | -4.12% |

### Change over 7d (vs run at 2026-09-16T20:32:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,850.92 | 4,741.96 | -2.25% |
| Average non-vote TPS | 2,744.58 | 2,211.74 | -19.41% |
| Average slot time (ms) | 318.60 | 265.30 | -16.73% |
| Active validators | 677.00 | 674.00 | -0.44% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,723,932,041.00 | 6,385,088,886.00 | +11.55% |
| SOL price | 98.40 | 114.36 | +16.22% |
| Stablecoin supply | 15,963,602,798.00 | 16,880,373,729.00 | +5.74% |
| 24h DEX volume | 2,703,297,666.22 | 3,195,015,036.76 | +18.19% |
| 24h chain fees | 14,083,156.46 | 17,874,880.76 | +26.92% |

### Change over 30d (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,741.96 | +3.81% |
| Average non-vote TPS | 2,714.40 | 2,211.74 | -18.52% |
| Average slot time (ms) | 367.20 | 265.30 | -27.75% |
| Active validators | 685.00 | 674.00 | -1.61% |
| Delinquent validators | 10.00 | 13.00 | +30.00% |
| Solana TVL | 5,621,355,422.00 | 6,385,088,886.00 | +13.59% |
| SOL price | 96.29 | 114.36 | +18.77% |
| Stablecoin supply | 16,453,918,497.00 | 16,880,373,729.00 | +2.59% |
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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
