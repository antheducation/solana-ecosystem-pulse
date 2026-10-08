# Solana Ecosystem Pulse

**Generated:** 2026-10-08T12:21:06Z · **Schema:** `1.0.0` · **Collection time:** 18.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $113.01 | -3.51% |
| Market cap | $66.60B | rank #7 |
| Total value locked | $6.41B | -3.16% |
| Stablecoin supply | $16.61B | -1.79% |
| DEX volume (24h) | $2.21B | +7.46% |
| Chain fees / REV (24h) | $13.67M | -14.83% |
| Non-vote TPS (1h avg) | 1,740 | peak 4,881 total |
| Active validators | 670 | 9 delinquent |
| Epoch 1052 | 18.32% complete | 352,854 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,740.5 average over the last 60 minutes; 2,084.3 in the latest sample.
- **Total TPS:** 4,241.8 average, 4,880.8 peak. Consensus votes account for 59.0% of all transactions.
- **Slot time:** 267.2 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 432,580,618 at absolute slot 454,543,146.
- **Epoch 1052:** slot 79,146 of 432,000 (18.32% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.612% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 101 ms |
| `solana-rpc.publicnode.com` | yes | 367 ms |
| `api.mainnet.solana.com` | yes | 86 ms |

## Validators & stake

- **670 active** validators, **9 delinquent** (1.33% by count, 0.021% by stake).
- **Total stake:** 439,005,453 SOL ($49.61B); stake rate 69.08% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.68%; 231 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,819,094 | 4.060% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,944,778 | 3.633% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,318,266 | 2.807% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,224,868 | 2.557% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,075,222 | 2.523% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,267,423 | 2.111% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,257,645 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,512,076 | 1.712% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,812,500 | 1.552% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,691,194 | 1.524% | 0% |

## Economics

- **SOL:** $113.01 (-3.51% 24h, -4.18% 7d, +9.95% 30d). Market cap $66.60B, 24h volume $3.11B (4.67% of cap). Price source: `coingecko`.
- **TVL:** $6.41B across 335 protocols - rank #2 of 468 chains, 6.90% of all tracked chain TVL. -1.36% over 7d, -51.5% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+1.28% 7d) - $2.59 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.21B in 24h, $14.83B over 7d across 126 venues. Volume/TVL turnover 0.344x per day.
- **REV (chain fees):** $13.67M in 24h, $451.09M over 30d. Retained chain revenue $5.35M (39.2% of fees). Annualised fees are 7.49% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,164,989 SOL circulating of 635,459,911 total (92.71%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.88B | -3.2% | -2.3% |
| 2 | Kamino Lend | Lending | $1.35B | -2.0% | -2.8% |
| 3 | Raydium AMM | Dexs | $1.29B | -2.5% | -4.0% |
| 4 | Jupiter Lend | Lending | $1.20B | -2.0% | +5.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.19B | -3.2% | -3.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.18B | -2.3% | -2.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $787.21M | -1.5% | -2.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $591.29M | -3.2% | -2.9% |
| 9 | Sentora Curator | Risk Curators | $502.17M | +2.0% | +26.0% |
| 10 | Marinade Native | Staking Pool | $425.91M | -3.0% | -4.3% |
| 11 | PumpSwap | Dexs | $385.79M | -2.4% | -1.8% |
| 12 | Orca DEX | Dexs | $319.55M | -0.4% | +1.3% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 335 protocols the total is $17.05B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 16.7% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.8%

### Tokenised assets

$887.84M of tokenised real-world assets and equities are locked on Solana - 5.206% of chain TVL.

- OnRe (RWA): $293.14M
- Huma (RWA): $257.43M
- Solstice (Basis Trading): $211.80M
- JupUSD (Basis Trading): $47.82M
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
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-08
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-08
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

### Change over 24h (vs run at 2026-10-07T12:10:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,150.69 | 4,241.77 | +2.19% |
| Average non-vote TPS | 1,657.06 | 1,740.45 | +5.03% |
| Average slot time (ms) | 268.60 | 267.20 | -0.52% |
| Active validators | 670.00 | 670.00 | +0.00% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 6,507,392,132.00 | 6,406,632,483.00 | -1.55% |
| SOL price | 117.28 | 113.01 | -3.64% |
| Stablecoin supply | 16,916,603,331.00 | 16,610,278,482.00 | -1.81% |
| 24h DEX volume | 2,052,545,605.65 | 2,205,685,057.81 | +7.46% |
| 24h chain fees | 16,043,229.31 | 13,669,849.90 | -14.79% |

### Change over 7d (vs run at 2026-10-01T11:56:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,905.71 | 4,241.77 | +8.60% |
| Average non-vote TPS | 1,400.79 | 1,740.45 | +24.25% |
| Average slot time (ms) | 267.10 | 267.20 | +0.04% |
| Active validators | 672.00 | 670.00 | -0.30% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 6,520,822,206.00 | 6,406,632,483.00 | -1.75% |
| SOL price | 117.94 | 113.01 | -4.18% |
| Stablecoin supply | 16,398,738,087.00 | 16,610,278,482.00 | +1.29% |
| 24h DEX volume | 2,569,940,125.73 | 2,205,685,057.81 | -14.17% |
| 24h chain fees | 15,876,757.05 | 13,669,849.90 | -13.90% |

### Change over 30d (vs run at 2026-09-08T20:23:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,250.75 | 4,241.77 | -0.21% |
| Average non-vote TPS | 2,131.65 | 1,740.45 | -18.35% |
| Average slot time (ms) | 317.30 | 267.20 | -15.79% |
| Active validators | 676.00 | 670.00 | -0.89% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 5,936,538,125.00 | 6,406,632,483.00 | +7.92% |
| SOL price | 103.30 | 113.01 | +9.40% |
| Stablecoin supply | 16,696,076,448.00 | 16,610,278,482.00 | -0.51% |
| 24h DEX volume | 2,720,639,104.66 | 2,205,685,057.81 | -18.93% |
| 24h chain fees | 15,653,179.21 | 13,669,849.90 | -12.67% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
