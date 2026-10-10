# Solana Ecosystem Pulse

**Generated:** 2026-10-10T11:28:34Z · **Schema:** `1.0.0` · **Collection time:** 33.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $109.48 | -0.34% |
| Market cap | $64.47B | rank #7 |
| Total value locked | $6.20B | -0.17% |
| Stablecoin supply | $16.43B | +0.28% |
| DEX volume (24h) | $1.98B | -25.21% |
| Chain fees / REV (24h) | $13.93M | -7.57% |
| Non-vote TPS (1h avg) | 1,231 | peak 4,568 total |
| Active validators | 675 | 6 delinquent |
| Epoch 1053 | 79.41% complete | 88,950 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 217.40 sits 17.3 sigma below the median of the last 102 runs (268.70, -19.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,230.9 average over the last 60 minutes; 1,050.5 in the latest sample.
- **Total TPS:** 4,325.8 average, 4,568.2 peak. Consensus votes account for 71.5% of all transactions.
- **Slot time:** 217.4 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 433,276,275 at absolute slot 455,239,050.
- **Epoch 1053:** slot 343,050 of 432,000 (79.41% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.610% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 196 ms |
| `solana-rpc.publicnode.com` | yes | 145 ms |
| `api.mainnet.solana.com` | yes | 144 ms |

## Validators & stake

- **675 active** validators, **6 delinquent** (0.88% by count, 0.002% by stake).
- **Total stake:** 437,867,727 SOL ($47.94B); stake rate 68.90% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.63% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 13.19%; 231 validators at 0% and 66 at 100%.

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

- **SOL:** $109.48 (-0.34% 24h, -8.38% 7d, +8.38% 30d). Market cap $64.47B, 24h volume $2.18B (3.38% of cap). Price source: `coingecko`.
- **TVL:** $6.20B across 336 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -5.10% over 7d, -53.2% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (-3.09% 7d) - $2.65 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.98B in 24h, $14.20B over 7d across 130 venues. Volume/TVL turnover 0.319x per day.
- **REV (chain fees):** $13.93M in 24h, $454.77M over 30d. Retained chain revenue $5.16M (37.1% of fees). Annualised fees are 7.89% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,791,707 SOL circulating of 635,536,352 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | -0.7% | -7.4% |
| 2 | Kamino Lend | Lending | $1.33B | -0.1% | -4.2% |
| 3 | Raydium AMM | Dexs | $1.24B | +0.1% | -7.8% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.14B | -0.5% | -7.4% |
| 5 | Jupiter Lend | Lending | $1.13B | -1.8% | -5.5% |
| 6 | Binance Staked SOL | Liquid Staking | $1.12B | -0.4% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $768.65M | -0.9% | -5.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $567.37M | -0.6% | -7.5% |
| 9 | Sentora Curator | Risk Curators | $490.94M | -1.3% | +28.4% |
| 10 | Marinade Native | Staking Pool | $405.43M | -0.8% | -8.2% |
| 11 | PumpSwap | Dexs | $367.05M | -1.6% | -7.0% |
| 12 | Orca DEX | Dexs | $309.62M | +0.0% | -2.2% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.50B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 16.7% · Dexs 15.5% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$884.27M of tokenised real-world assets and equities are locked on Solana - 5.358% of chain TVL.

- OnRe (RWA): $292.66M
- Huma (RWA): $256.01M
- Solstice (Basis Trading): $210.59M
- JupUSD (Basis Trading): $47.33M
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

- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-10
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-09
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-08
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-08
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
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

### Change over 24h (vs run at 2026-10-09T12:11:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,156.32 | 4,325.84 | +4.08% |
| Average non-vote TPS | 1,656.99 | 1,230.91 | -25.71% |
| Average slot time (ms) | 268.30 | 217.40 | -18.97% |
| Active validators | 673.00 | 675.00 | +0.30% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,231,947,843.00 | 6,201,943,177.00 | -0.48% |
| SOL price | 111.20 | 109.48 | -1.55% |
| Stablecoin supply | 16,377,840,192.00 | 16,426,938,969.00 | +0.30% |
| 24h DEX volume | 2,644,852,886.24 | 1,978,097,665.91 | -25.21% |
| 24h chain fees | 14,970,162.23 | 13,931,064.19 | -6.94% |

### Change over 7d (vs run at 2026-10-03T10:43:45Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,058.70 | 4,325.84 | +6.58% |
| Average non-vote TPS | 1,554.03 | 1,230.91 | -20.79% |
| Average slot time (ms) | 267.20 | 217.40 | -18.64% |
| Active validators | 672.00 | 675.00 | +0.45% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 6,644,736,603.00 | 6,201,943,177.00 | -6.66% |
| SOL price | 119.47 | 109.48 | -8.36% |
| Stablecoin supply | 16,950,680,446.00 | 16,426,938,969.00 | -3.09% |
| 24h DEX volume | 2,699,245,511.96 | 1,978,097,665.91 | -26.72% |
| 24h chain fees | 17,261,998.04 | 13,931,064.19 | -19.30% |

### Change over 30d (vs run at 2026-09-10T20:09:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,122.54 | 4,325.84 | +4.93% |
| Average non-vote TPS | 1,990.17 | 1,230.91 | -38.15% |
| Average slot time (ms) | 315.50 | 217.40 | -31.09% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 5,779,330,766.00 | 6,201,943,177.00 | +7.31% |
| SOL price | 99.77 | 109.48 | +9.73% |
| Stablecoin supply | 16,576,239,978.00 | 16,426,938,969.00 | -0.90% |
| 24h DEX volume | 3,000,435,429.63 | 1,978,097,665.91 | -34.07% |
| 24h chain fees | 15,717,207.17 | 13,931,064.19 | -11.36% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 32.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
