# Solana Ecosystem Pulse

**Generated:** 2026-10-09T21:56:06Z · **Schema:** `1.0.0` · **Collection time:** 15.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $108.92 | -1.59% |
| Market cap | $64.13B | rank #7 |
| Total value locked | $6.17B | -4.39% |
| Stablecoin supply | $16.38B | -1.37% |
| DEX volume (24h) | $2.64B | +19.91% |
| Chain fees / REV (24h) | $15.07M | +5.35% |
| Non-vote TPS (1h avg) | 1,872 | peak 5,516 total |
| Active validators | 674 | 6 delinquent |
| Epoch 1053 | 27.64% complete | 312,578 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 218.80 sits 16.8 sigma below the median of the last 102 runs (268.70, -18.6%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,872.4 average over the last 60 minutes; 1,990.1 in the latest sample.
- **Total TPS:** 4,940.5 average, 5,515.9 peak. Consensus votes account for 62.1% of all transactions.
- **Slot time:** 218.8 ms average (target 400 ms), worst 1-minute bucket 228.1 ms.
- **Block height:** 433,052,670 at absolute slot 455,015,422.
- **Epoch 1053:** slot 119,422 of 432,000 (27.64% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.610% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 186 ms |
| `solana-rpc.publicnode.com` | yes | 115 ms |
| `api.mainnet.solana.com` | yes | 185 ms |

## Validators & stake

- **674 active** validators, **6 delinquent** (0.88% by count, 0.002% by stake).
- **Total stake:** 437,867,727 SOL ($47.69B); stake rate 68.90% of total supply.
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

- **SOL:** $108.92 (-1.59% 24h, -7.51% 7d, +6.21% 30d). Market cap $64.13B, 24h volume $2.95B (4.60% of cap). Price source: `coingecko`.
- **TVL:** $6.17B across 337 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -5.12% over 7d, -53.4% from its ATH.
- **Stablecoins:** $16.38B circulating on Solana (-1.23% 7d) - $2.65 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.64B in 24h, $14.98B over 7d across 130 venues. Volume/TVL turnover 0.429x per day.
- **REV (chain fees):** $15.07M in 24h, $453.03M over 30d. Retained chain revenue $5.33M (35.4% of fees). Annualised fees are 8.58% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,768,200 SOL circulating of 635,536,938 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | -0.7% | -6.7% |
| 2 | Kamino Lend | Lending | $1.32B | +0.1% | -3.5% |
| 3 | Raydium AMM | Dexs | $1.23B | -0.1% | -8.6% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.14B | -2.9% | -8.0% |
| 5 | Jupiter Lend | Lending | $1.13B | -3.9% | -4.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.11B | -1.4% | -8.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $769.98M | +0.4% | -5.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $563.85M | -3.2% | -7.7% |
| 9 | Sentora Curator | Risk Curators | $496.76M | -1.1% | +26.0% |
| 10 | Marinade Native | Staking Pool | $405.04M | -3.4% | -8.0% |
| 11 | PumpSwap | Dexs | $366.14M | -2.5% | -7.2% |
| 12 | Orca DEX | Dexs | $308.48M | -2.6% | -2.6% |

The top five protocols hold 40.4% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 16.7% · Dexs 15.5% · Derivatives 5.3% · Risk Curators 4.3% · Staking Pool 3.8%

### Tokenised assets

$884.88M of tokenised real-world assets and equities are locked on Solana - 5.392% of chain TVL.

- OnRe (RWA): $293.13M
- Huma (RWA): $256.22M
- Solstice (Basis Trading): $210.58M
- JupUSD (Basis Trading): $47.32M
- Plume Vaults (RWA): $32.97M

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
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-07
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

### Change over 24h (vs run at 2026-10-08T22:33:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,632.43 | 4,940.51 | +6.65% |
| Average non-vote TPS | 2,125.38 | 1,872.44 | -11.90% |
| Average slot time (ms) | 267.50 | 218.80 | -18.21% |
| Active validators | 673.00 | 674.00 | +0.15% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,248,086,909.00 | 6,170,032,842.00 | -1.25% |
| SOL price | 110.19 | 108.92 | -1.15% |
| Stablecoin supply | 16,607,983,518.00 | 16,379,819,991.00 | -1.37% |
| 24h DEX volume | 2,205,685,057.81 | 2,644,852,886.24 | +19.91% |
| 24h chain fees | 13,737,332.90 | 15,072,203.23 | +9.72% |

### Change over 7d (vs run at 2026-10-02T21:29:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,922.79 | 4,940.51 | +0.36% |
| Average non-vote TPS | 2,432.94 | 1,872.44 | -23.04% |
| Average slot time (ms) | 268.50 | 218.80 | -18.51% |
| Active validators | 671.00 | 674.00 | +0.45% |
| Delinquent validators | 13.00 | 6.00 | -53.85% |
| Solana TVL | 6,606,723,520.00 | 6,170,032,842.00 | -6.61% |
| SOL price | 117.81 | 108.92 | -7.55% |
| Stablecoin supply | 16,579,831,390.00 | 16,379,819,991.00 | -1.21% |
| 24h DEX volume | 2,488,460,102.88 | 2,644,852,886.24 | +6.28% |
| 24h chain fees | 17,134,431.63 | 15,072,203.23 | -12.04% |

### Change over 30d (vs run at 2026-09-09T20:07:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,453.09 | 4,940.51 | +10.95% |
| Average non-vote TPS | 2,342.31 | 1,872.44 | -20.06% |
| Average slot time (ms) | 319.30 | 218.80 | -31.48% |
| Active validators | 675.00 | 674.00 | -0.15% |
| Delinquent validators | 13.00 | 6.00 | -53.85% |
| Solana TVL | 5,948,260,786.00 | 6,170,032,842.00 | +3.73% |
| SOL price | 102.19 | 108.92 | +6.59% |
| Stablecoin supply | 16,629,873,212.00 | 16,379,819,991.00 | -1.50% |
| 24h DEX volume | 2,710,734,376.34 | 2,644,852,886.24 | -2.43% |
| 24h chain fees | 16,561,493.38 | 15,072,203.23 | -8.99% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
