# Solana Ecosystem Pulse

**Generated:** 2026-10-08T03:15:36Z · **Schema:** `1.0.0` · **Collection time:** 12.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $115.92 | -1.90% |
| Market cap | $68.29B | rank #7 |
| Total value locked | $6.47B | -1.72% |
| Stablecoin supply | $16.61B | -1.79% |
| DEX volume (24h) | $2.14B | +4.42% |
| Chain fees / REV (24h) | $13.76M | -14.29% |
| Non-vote TPS (1h avg) | 1,848 | peak 4,827 total |
| Active validators | 671 | 10 delinquent |
| Epoch 1051 | 90.00% complete | 43,220 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,848.0 average over the last 60 minutes; 1,466.2 in the latest sample.
- **Total TPS:** 4,343.1 average, 4,827.2 peak. Consensus votes account for 57.4% of all transactions.
- **Slot time:** 268.0 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 432,458,267 at absolute slot 454,420,780.
- **Epoch 1051:** slot 388,780 of 432,000 (90.00% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.614% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 102 ms |
| `solana-rpc.publicnode.com` | yes | 46 ms |
| `api.mainnet.solana.com` | yes | 79 ms |

## Validators & stake

- **671 active** validators, **10 delinquent** (1.47% by count, 0.008% by stake).
- **Total stake:** 439,343,031 SOL ($50.93B); stake rate 69.15% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,653,055 | 4.018% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,968,869 | 3.635% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,308,201 | 2.802% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,264,081 | 2.564% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,149,017 | 2.538% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,259,685 | 2.108% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,251,538 | 2.106% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,508,703 | 1.709% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,113,963 | 1.619% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,690,032 | 1.523% | 0% |

## Economics

- **SOL:** $115.92 (-1.90% 24h, -1.88% 7d, +12.24% 30d). Market cap $68.29B, 24h volume $2.77B (4.05% of cap). Price source: `coingecko`.
- **TVL:** $6.47B across 335 protocols - rank #2 of 468 chains, 6.90% of all tracked chain TVL. +0.16% over 7d, -51.1% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+1.29% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.14B in 24h, $13.90B over 7d across 126 venues. Volume/TVL turnover 0.331x per day.
- **REV (chain fees):** $13.76M in 24h, $450.54M over 30d. Retained chain revenue $5.43M (39.5% of fees). Annualised fees are 7.35% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,094,051 SOL circulating of 635,381,719 total (92.71%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | -2.4% | -0.0% |
| 2 | Kamino Lend | Lending | $1.36B | -2.6% | -1.9% |
| 3 | Raydium AMM | Dexs | $1.30B | -3.4% | -2.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.21B | -2.7% | -1.2% |
| 5 | Jupiter Lend | Lending | $1.21B | -1.8% | +5.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.20B | -2.8% | -1.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $793.42M | -2.3% | -1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $602.90M | -3.5% | -1.0% |
| 9 | Sentora Curator | Risk Curators | $502.60M | +2.3% | +26.1% |
| 10 | Marinade Native | Staking Pool | $433.95M | -2.9% | -2.5% |
| 11 | PumpSwap | Dexs | $387.71M | -3.2% | -1.3% |
| 12 | Drift Staked SOL | Liquid Staking | $328.24M | -2.9% | -1.4% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 335 protocols the total is $17.28B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 16.6% · Dexs 15.4% · Derivatives 5.1% · Risk Curators 4.1% · Staking Pool 3.8%

### Tokenised assets

$888.21M of tokenised real-world assets and equities are locked on Solana - 5.140% of chain TVL.

- OnRe (RWA): $293.12M
- Huma (RWA): $257.44M
- Solstice (Basis Trading): $211.84M
- JupUSD (Basis Trading): $48.09M
- Plume Vaults (RWA): $32.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) - Mon, 05 Oct 2026 00:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-07
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-07
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-07
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-07
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-07
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-07
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-07

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

### Change over 24h (vs run at 2026-10-07T02:58:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,983.12 | 4,343.08 | -12.84% |
| Average non-vote TPS | 2,500.28 | 1,847.99 | -26.09% |
| Average slot time (ms) | 270.10 | 268.00 | -0.78% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 6,621,064,757.00 | 6,467,832,291.00 | -2.31% |
| SOL price | 118.29 | 115.92 | -2.00% |
| Stablecoin supply | 16,917,902,048.00 | 16,610,992,769.00 | -1.81% |
| 24h DEX volume | 2,039,240,588.65 | 2,143,188,354.81 | +5.10% |
| 24h chain fees | 16,053,410.31 | 13,755,904.90 | -14.31% |

### Change over 7d (vs run at 2026-10-01T02:45:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,555.14 | 4,343.08 | -4.66% |
| Average non-vote TPS | 2,062.19 | 1,847.99 | -10.39% |
| Average slot time (ms) | 268.10 | 268.00 | -0.04% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 6,528,079,711.00 | 6,467,832,291.00 | -0.92% |
| SOL price | 117.98 | 115.92 | -1.75% |
| Stablecoin supply | 16,397,665,769.00 | 16,610,992,769.00 | +1.30% |
| 24h DEX volume | 2,544,678,619.73 | 2,143,188,354.81 | -15.78% |
| 24h chain fees | 15,842,342.66 | 13,755,904.90 | -13.17% |

### Change over 30d (vs run at 2026-09-07T20:51:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,930.66 | 4,343.08 | +10.49% |
| Average non-vote TPS | 1,809.47 | 1,847.99 | +2.13% |
| Average slot time (ms) | 316.70 | 268.00 | -15.38% |
| Active validators | 676.00 | 671.00 | -0.74% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,896,988,391.00 | 6,467,832,291.00 | +9.68% |
| SOL price | 104.08 | 115.92 | +11.38% |
| Stablecoin supply | 16,741,090,548.00 | 16,610,992,769.00 | -0.78% |
| 24h DEX volume | 2,904,503,252.44 | 2,143,188,354.81 | -26.21% |
| 24h chain fees | 14,655,299.70 | 13,755,904.90 | -6.14% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
