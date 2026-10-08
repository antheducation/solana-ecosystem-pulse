# Solana Ecosystem Pulse

**Generated:** 2026-10-08T22:33:53Z · **Schema:** `1.0.0` · **Collection time:** 15.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.19 | -5.02% |
| Market cap | $64.88B | rank #7 |
| Total value locked | $6.25B | -5.66% |
| Stablecoin supply | $16.61B | -1.81% |
| DEX volume (24h) | $2.21B | +7.46% |
| Chain fees / REV (24h) | $13.74M | -14.41% |
| Non-vote TPS (1h avg) | 2,125 | peak 5,332 total |
| Active validators | 673 | 8 delinquent |
| Epoch 1052 | 49.89% complete | 216,464 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,125.4 average over the last 60 minutes; 2,118.1 in the latest sample.
- **Total TPS:** 4,632.4 average, 5,331.8 peak. Consensus votes account for 54.1% of all transactions.
- **Slot time:** 267.5 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 432,716,901 at absolute slot 454,679,536.
- **Epoch 1052:** slot 215,536 of 432,000 (49.89% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.612% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 139 ms |
| `solana-rpc.publicnode.com` | yes | 126 ms |
| `api.mainnet.solana.com` | yes | 119 ms |

## Validators & stake

- **673 active** validators, **8 delinquent** (1.17% by count, 0.007% by stake).
- **Total stake:** 439,005,453 SOL ($48.37B); stake rate 69.08% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.94%; 231 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,819,094 | 4.059% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,944,778 | 3.632% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,318,266 | 2.806% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,224,868 | 2.557% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,075,222 | 2.523% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,267,423 | 2.111% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,645 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,512,076 | 1.711% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,812,500 | 1.552% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,691,194 | 1.524% | 0% |

## Economics

- **SOL:** $110.19 (-5.02% 24h, -6.35% 7d, +6.99% 30d). Market cap $64.88B, 24h volume $4.84B (7.46% of cap). Price source: `coingecko`.
- **TVL:** $6.25B across 335 protocols - rank #2 of 468 chains, 6.81% of all tracked chain TVL. -3.91% over 7d, -52.8% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+1.27% 7d) - $2.66 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.21B in 24h, $14.83B over 7d across 126 venues. Volume/TVL turnover 0.353x per day.
- **REV (chain fees):** $13.74M in 24h, $451.16M over 30d. Retained chain revenue $5.35M (39.0% of fees). Annualised fees are 7.73% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,697,954 SOL circulating of 635,459,433 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | -5.2% | -5.8% |
| 2 | Kamino Lend | Lending | $1.32B | -2.9% | -4.9% |
| 3 | Raydium AMM | Dexs | $1.24B | -4.9% | -7.8% |
| 4 | Jupiter Lend | Lending | $1.18B | -3.1% | +3.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.17B | -3.1% | -4.7% |
| 6 | Binance Staked SOL | Liquid Staking | $1.12B | -5.5% | -6.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $766.59M | -3.1% | -4.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $582.61M | -3.0% | -4.3% |
| 9 | Sentora Curator | Risk Curators | $502.08M | +2.2% | +25.9% |
| 10 | Marinade Native | Staking Pool | $419.39M | -3.0% | -5.8% |
| 11 | PumpSwap | Dexs | $375.58M | -3.8% | -4.3% |
| 12 | Orca DEX | Dexs | $316.74M | -1.3% | +0.4% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 335 protocols the total is $16.66B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.8% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.8%

### Tokenised assets

$886.84M of tokenised real-world assets and equities are locked on Solana - 5.322% of chain TVL.

- OnRe (RWA): $293.48M
- Huma (RWA): $256.52M
- Solstice (Basis Trading): $211.82M
- JupUSD (Basis Trading): $47.40M
- Plume Vaults (RWA): $32.96M

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

- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-08
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-08
- [SIMD-0083: amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-07
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-07
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

### Change over 24h (vs run at 2026-10-07T22:21:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,609.27 | 4,632.43 | +0.50% |
| Average non-vote TPS | 2,129.60 | 2,125.38 | -0.20% |
| Average slot time (ms) | 269.60 | 267.50 | -0.78% |
| Active validators | 671.00 | 673.00 | +0.30% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 6,453,092,289.00 | 6,248,086,909.00 | -3.18% |
| SOL price | 115.61 | 110.19 | -4.69% |
| Stablecoin supply | 16,914,576,986.00 | 16,607,983,518.00 | -1.81% |
| 24h DEX volume | 2,052,545,605.65 | 2,205,685,057.81 | +7.46% |
| 24h chain fees | 16,052,631.31 | 13,737,332.90 | -14.42% |

### Change over 7d (vs run at 2026-10-01T22:04:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,821.72 | 4,632.43 | -3.93% |
| Average non-vote TPS | 2,325.69 | 2,125.38 | -8.61% |
| Average slot time (ms) | 268.10 | 267.50 | -0.22% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 12.00 | 8.00 | -33.33% |
| Solana TVL | 6,567,199,720.00 | 6,248,086,909.00 | -4.86% |
| SOL price | 117.92 | 110.19 | -6.56% |
| Stablecoin supply | 16,398,651,646.00 | 16,607,983,518.00 | +1.28% |
| 24h DEX volume | 2,569,940,125.73 | 2,205,685,057.81 | -14.17% |
| 24h chain fees | 15,975,862.05 | 13,737,332.90 | -14.01% |

### Change over 30d (vs run at 2026-09-08T20:23:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,250.75 | 4,632.43 | +8.98% |
| Average non-vote TPS | 2,131.65 | 2,125.38 | -0.29% |
| Average slot time (ms) | 317.30 | 267.50 | -15.69% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,936,538,125.00 | 6,248,086,909.00 | +5.25% |
| SOL price | 103.30 | 110.19 | +6.67% |
| Stablecoin supply | 16,696,076,448.00 | 16,607,983,518.00 | -0.53% |
| 24h DEX volume | 2,720,639,104.66 | 2,205,685,057.81 | -18.93% |
| 24h chain fees | 15,653,179.21 | 13,737,332.90 | -12.24% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
