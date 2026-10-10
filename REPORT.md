# Solana Ecosystem Pulse

**Generated:** 2026-10-10T03:00:53Z · **Schema:** `1.0.0` · **Collection time:** 16.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $109.79 | -0.43% |
| Market cap | $64.63B | rank #7 |
| Total value locked | $6.19B | -0.43% |
| Stablecoin supply | $16.43B | +0.29% |
| DEX volume (24h) | $2.22B | -16.24% |
| Chain fees / REV (24h) | $13.94M | -7.51% |
| Non-vote TPS (1h avg) | 1,669 | peak 5,230 total |
| Active validators | 674 | 6 delinquent |
| Epoch 1053 | 47.04% complete | 228,804 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 218.70 sits 16.9 sigma below the median of the last 101 runs (268.70, -18.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,669.3 average over the last 60 minutes; 1,426.6 in the latest sample.
- **Total TPS:** 4,740.7 average, 5,229.5 peak. Consensus votes account for 64.8% of all transactions.
- **Slot time:** 218.7 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 433,136,439 at absolute slot 455,099,196.
- **Epoch 1053:** slot 203,196 of 432,000 (47.04% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.610% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 151 ms |
| `solana-rpc.publicnode.com` | yes | 114 ms |
| `api.mainnet.solana.com` | yes | 164 ms |

## Validators & stake

- **674 active** validators, **6 delinquent** (0.88% by count, 0.002% by stake).
- **Total stake:** 437,867,727 SOL ($48.07B); stake rate 68.90% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.63% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 12.77%; 233 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,788,627 | 4.063% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,954,195 | 3.644% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,299,759 | 2.809% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,178,787 | 2.553% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,972,770 | 2.506% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,315,835 | 2.128% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,552 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,589,922 | 1.733% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,809,494 | 1.555% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,692,115 | 1.528% | 0% |

## Economics

- **SOL:** $109.79 (-0.43% 24h, -7.66% 7d, +7.80% 30d). Market cap $64.63B, 24h volume $2.59B (4.01% of cap). Price source: `coingecko`.
- **TVL:** $6.19B across 337 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -5.30% over 7d, -53.3% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (-3.09% 7d) - $2.65 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.22B in 24h, $13.31B over 7d across 130 venues. Volume/TVL turnover 0.358x per day.
- **REV (chain fees):** $13.94M in 24h, $452.44M over 30d. Retained chain revenue $5.16M (37.0% of fees). Annualised fees are 7.87% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,792,064 SOL circulating of 635,536,709 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +0.6% | -7.4% |
| 2 | Kamino Lend | Lending | $1.33B | +0.6% | -4.2% |
| 3 | Raydium AMM | Dexs | $1.24B | +0.3% | -8.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.15B | +0.1% | -7.4% |
| 5 | Jupiter Lend | Lending | $1.14B | -3.3% | -5.4% |
| 6 | Binance Staked SOL | Liquid Staking | $1.12B | +0.0% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $772.43M | +0.5% | -4.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $568.08M | +0.6% | -7.4% |
| 9 | Sentora Curator | Risk Curators | $496.92M | -1.0% | +29.9% |
| 10 | Marinade Native | Staking Pool | $405.85M | -0.2% | -8.1% |
| 11 | PumpSwap | Dexs | $363.95M | -2.0% | -7.8% |
| 12 | Orca DEX | Dexs | $308.50M | -2.6% | -2.6% |

The top five protocols hold 40.4% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.48B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.7% · Dexs 15.4% · Derivatives 5.3% · Risk Curators 4.2% · Staking Pool 3.8%

### Tokenised assets

$884.26M of tokenised real-world assets and equities are locked on Solana - 5.365% of chain TVL.

- OnRe (RWA): $292.71M
- Huma (RWA): $256.01M
- Solstice (Basis Trading): $210.55M
- JupUSD (Basis Trading): $47.32M
- Plume Vaults (RWA): $32.98M

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
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-09
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-08
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-08
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-07
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-07
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-07
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-07

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

### Change over 24h (vs run at 2026-10-09T03:21:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,330.45 | 4,740.69 | +9.47% |
| Average non-vote TPS | 1,832.51 | 1,669.34 | -8.90% |
| Average slot time (ms) | 268.40 | 218.70 | -18.52% |
| Active validators | 673.00 | 674.00 | +0.15% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,221,527,063.00 | 6,187,946,925.00 | -0.54% |
| SOL price | 110.02 | 109.79 | -0.21% |
| Stablecoin supply | 16,377,545,621.00 | 16,427,773,068.00 | +0.31% |
| 24h DEX volume | 2,440,532,233.24 | 2,215,423,677.91 | -9.22% |
| 24h chain fees | 13,520,931.81 | 13,940,731.19 | +3.10% |

### Change over 7d (vs run at 2026-10-03T02:35:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,081.59 | 4,740.69 | +16.15% |
| Average non-vote TPS | 1,576.02 | 1,669.34 | +5.92% |
| Average slot time (ms) | 267.20 | 218.70 | -18.15% |
| Active validators | 672.00 | 674.00 | +0.30% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 6,615,550,945.00 | 6,187,946,925.00 | -6.46% |
| SOL price | 119.15 | 109.79 | -7.86% |
| Stablecoin supply | 16,950,465,224.00 | 16,427,773,068.00 | -3.08% |
| 24h DEX volume | 2,569,613,456.96 | 2,215,423,677.91 | -13.78% |
| 24h chain fees | 17,357,994.82 | 13,940,731.19 | -19.69% |

### Change over 30d (vs run at 2026-09-09T20:07:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,453.09 | 4,740.69 | +6.46% |
| Average non-vote TPS | 2,342.31 | 1,669.34 | -28.73% |
| Average slot time (ms) | 319.30 | 218.70 | -31.51% |
| Active validators | 675.00 | 674.00 | -0.15% |
| Delinquent validators | 13.00 | 6.00 | -53.85% |
| Solana TVL | 5,948,260,786.00 | 6,187,946,925.00 | +4.03% |
| SOL price | 102.19 | 109.79 | +7.44% |
| Stablecoin supply | 16,629,873,212.00 | 16,427,773,068.00 | -1.22% |
| 24h DEX volume | 2,710,734,376.34 | 2,215,423,677.91 | -18.27% |
| 24h chain fees | 16,561,493.38 | 13,940,731.19 | -15.82% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
