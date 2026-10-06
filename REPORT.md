# Solana Ecosystem Pulse

**Generated:** 2026-10-06T03:32:50Z · **Schema:** `1.0.0` · **Collection time:** 17.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.95 | -0.90% |
| Market cap | $70.57B | rank #7 |
| Total value locked | $6.80B | +0.93% |
| Stablecoin supply | $17.05B | +0.98% |
| DEX volume (24h) | $1.90B | +11.51% |
| Chain fees / REV (24h) | $16.11M | -0.10% |
| Non-vote TPS (1h avg) | 2,076 | peak 5,397 total |
| Active validators | 672 | 13 delinquent |
| Epoch 1050 | 41.98% complete | 250,650 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 101 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,076.1 average over the last 60 minutes; 1,749.9 in the latest sample.
- **Total TPS:** 4,576.3 average, 5,396.8 peak. Consensus votes account for 54.6% of all transactions.
- **Slot time:** 267.6 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 431,819,193 at absolute slot 453,781,350.
- **Epoch 1050:** slot 181,350 of 432,000 (41.98% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.616% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 307 ms |
| `solana-rpc.publicnode.com` | yes | 204 ms |
| `api.mainnet.solana.com` | yes | 183 ms |

## Validators & stake

- **672 active** validators, **13 delinquent** (1.90% by count, 0.018% by stake).
- **Total stake:** 441,738,541 SOL ($52.99B); stake rate 69.53% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.57% and top 33 hold 45.65% of active stake.
- **Commission:** median 5.0%, mean 12.69%; 231 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,915,070 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,937,333 | 3.609% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,292,997 | 2.783% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,310,013 | 2.561% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,144,638 | 2.523% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,258,566 | 2.096% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,254,450 | 2.095% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,629,486 | 1.727% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,062,716 | 1.599% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,687,904 | 1.514% | 0% |

## Economics

- **SOL:** $119.95 (-0.90% 24h, +2.60% 7d, +14.91% 30d). Market cap $70.57B, 24h volume $2.52B (3.57% of cap). Price source: `coingecko`.
- **TVL:** $6.80B across 334 protocols - rank #2 of 468 chains, 7.03% of all tracked chain TVL. +5.26% over 7d, -48.7% from its ATH.
- **Stablecoins:** $17.05B circulating on Solana (+2.36% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.90B in 24h, $14.83B over 7d across 126 venues. Volume/TVL turnover 0.280x per day.
- **REV (chain fees):** $16.11M in 24h, $447.55M over 30d. Retained chain revenue $5.96M (37.0% of fees). Annualised fees are 8.33% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,385,665 SOL circulating of 635,305,184 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.98B | -0.3% | +2.8% |
| 2 | Kamino Lend | Lending | $1.40B | +0.1% | +0.3% |
| 3 | Jupiter Lend | Lending | $1.40B | +5.3% | +19.9% |
| 4 | Raydium AMM | Dexs | $1.35B | -1.1% | +2.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.26B | -0.4% | +2.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.24B | -0.4% | +2.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $817.52M | -0.4% | +1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $624.72M | -0.5% | +2.2% |
| 9 | Sentora Curator | Risk Curators | $457.33M | +20.3% | +26.6% |
| 10 | Marinade Native | Staking Pool | $448.76M | -0.3% | -2.1% |
| 11 | PumpSwap | Dexs | $406.29M | -0.4% | +4.5% |
| 12 | Drift Staked SOL | Liquid Staking | $340.34M | -0.4% | +1.9% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.90B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.4% · Dexs 15.4% · Derivatives 5.0% · Staking Pool 3.8% · Risk Curators 3.8%

### Tokenised assets

$896.61M of tokenised real-world assets and equities are locked on Solana - 5.010% of chain TVL.

- OnRe (RWA): $292.96M
- Huma (RWA): $259.14M
- Solstice (Basis Trading): $211.92M
- JupUSD (Basis Trading): $48.66M
- Plume Vaults (RWA): $32.54M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-06
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-06
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-10-05
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-05
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-05

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

### Change over 24h (vs run at 2026-10-05T02:39:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,345.78 | 4,576.27 | +5.30% |
| Average non-vote TPS | 1,847.54 | 2,076.07 | +12.37% |
| Average slot time (ms) | 267.50 | 267.60 | +0.04% |
| Active validators | 671.00 | 672.00 | +0.15% |
| Delinquent validators | 15.00 | 13.00 | -13.33% |
| Solana TVL | 6,743,140,234.00 | 6,796,887,845.00 | +0.80% |
| SOL price | 121.39 | 119.95 | -1.19% |
| Stablecoin supply | 16,885,469,670.00 | 17,051,507,064.00 | +0.98% |
| 24h DEX volume | 1,649,284,605.63 | 1,904,732,429.50 | +15.49% |
| 24h chain fees | 15,446,766.41 | 16,107,910.12 | +4.28% |

### Change over 7d (vs run at 2026-09-29T02:59:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,432.82 | 4,576.27 | +3.24% |
| Average non-vote TPS | 1,921.08 | 2,076.07 | +8.07% |
| Average slot time (ms) | 267.80 | 267.60 | -0.07% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 6.00 | 13.00 | +116.67% |
| Solana TVL | 6,466,752,849.00 | 6,796,887,845.00 | +5.11% |
| SOL price | 116.86 | 119.95 | +2.64% |
| Stablecoin supply | 16,662,008,171.00 | 17,051,507,064.00 | +2.34% |
| 24h DEX volume | 2,290,100,033.25 | 1,904,732,429.50 | -16.83% |
| 24h chain fees | 17,452,720.35 | 16,107,910.12 | -7.71% |

### Change over 30d (vs run at 2026-09-05T19:38:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,427.43 | 4,576.27 | +33.52% |
| Average non-vote TPS | 1,291.31 | 2,076.07 | +60.77% |
| Average slot time (ms) | 315.00 | 267.60 | -15.05% |
| Active validators | 675.00 | 672.00 | -0.44% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,915,402,920.00 | 6,796,887,845.00 | +14.90% |
| SOL price | 103.80 | 119.95 | +15.56% |
| Stablecoin supply | 16,607,441,030.00 | 17,051,507,064.00 | +2.67% |
| 24h DEX volume | 1,881,639,252.00 | 1,904,732,429.50 | +1.23% |
| 24h chain fees | 10,436,292.55 | 16,107,910.12 | +54.35% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
