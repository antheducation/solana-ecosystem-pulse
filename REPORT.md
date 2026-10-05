# Solana Ecosystem Pulse

**Generated:** 2026-10-05T23:24:42Z · **Schema:** `1.0.0` · **Collection time:** 16.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.74 | -0.87% |
| Market cap | $71.04B | rank #7 |
| Total value locked | $6.78B | +2.52% |
| Stablecoin supply | $16.89B | +0.02% |
| DEX volume (24h) | $1.71B | +9.92% |
| Chain fees / REV (24h) | $16.12M | +24.70% |
| Non-vote TPS (1h avg) | 2,305 | peak 5,427 total |
| Active validators | 672 | 13 delinquent |
| Epoch 1050 | 29.12% complete | 306,182 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,304.8 average over the last 60 minutes; 1,974.7 in the latest sample.
- **Total TPS:** 4,796.6 average, 5,427.1 peak. Consensus votes account for 51.9% of all transactions.
- **Slot time:** 268.6 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 431,763,701 at absolute slot 453,725,818.
- **Epoch 1050:** slot 125,818 of 432,000 (29.12% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.616% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 285 ms |
| `solana-rpc.publicnode.com` | yes | 158 ms |
| `api.mainnet.solana.com` | yes | 166 ms |

## Validators & stake

- **672 active** validators, **13 delinquent** (1.90% by count, 0.018% by stake).
- **Total stake:** 441,738,541 SOL ($53.34B); stake rate 69.53% of total supply.
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

- **SOL:** $120.74 (-0.87% 24h, +1.85% 7d, +16.80% 30d). Market cap $71.04B, 24h volume $2.66B (3.74% of cap). Price source: `coingecko`.
- **TVL:** $6.78B across 334 protocols - rank #2 of 468 chains, 7.00% of all tracked chain TVL. +2.18% over 7d, -48.8% from its ATH.
- **Stablecoins:** $16.89B circulating on Solana (+0.97% 7d) - $2.49 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.71B in 24h, $16.28B over 7d across 126 venues. Volume/TVL turnover 0.252x per day.
- **REV (chain fees):** $16.12M in 24h, $440.65M over 30d. Retained chain revenue $6.04M (37.5% of fees). Annualised fees are 8.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,384,542 SOL circulating of 635,305,361 total (92.61%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.98B | -0.8% | +0.1% |
| 2 | Jupiter Lend | Lending | $1.40B | +5.0% | +17.1% |
| 3 | Kamino Lend | Lending | $1.40B | -0.2% | -5.3% |
| 4 | Raydium AMM | Dexs | $1.35B | -0.7% | -0.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.26B | -0.4% | -0.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.24B | -0.8% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $819.14M | -0.1% | -1.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $625.55M | -0.7% | -0.5% |
| 9 | Sentora Curator | Risk Curators | $458.86M | +20.4% | +26.4% |
| 10 | Marinade Native | Staking Pool | $449.38M | -0.5% | -4.1% |
| 11 | PumpSwap | Dexs | $399.82M | -1.1% | +0.8% |
| 12 | Drift Staked SOL | Liquid Staking | $340.89M | -0.5% | -0.5% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.90B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.3% · Dexs 15.3% · Derivatives 5.0% · Staking Pool 3.8% · Risk Curators 3.8%

### Tokenised assets

$896.85M of tokenised real-world assets and equities are locked on Solana - 5.011% of chain TVL.

- OnRe (RWA): $292.83M
- Huma (RWA): $259.57M
- Solstice (Basis Trading): $211.88M
- JupUSD (Basis Trading): $48.65M
- Plume Vaults (RWA): $32.54M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-05
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-05
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

### Change over 24h (vs run at 2026-10-04T20:33:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,626.16 | 4,796.58 | +3.68% |
| Average non-vote TPS | 2,127.97 | 2,304.82 | +8.31% |
| Average slot time (ms) | 267.70 | 268.60 | +0.34% |
| Active validators | 671.00 | 672.00 | +0.15% |
| Delinquent validators | 15.00 | 13.00 | -13.33% |
| Solana TVL | 6,715,169,332.00 | 6,781,683,220.00 | +0.99% |
| SOL price | 120.79 | 120.74 | -0.04% |
| Stablecoin supply | 16,881,830,613.00 | 16,885,339,627.00 | +0.02% |
| 24h DEX volume | 1,553,984,451.11 | 1,708,158,585.63 | +9.92% |
| 24h chain fees | 12,930,244.69 | 16,123,937.37 | +24.70% |

### Change over 7d (vs run at 2026-09-28T22:41:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,519.28 | 4,796.58 | +6.14% |
| Average non-vote TPS | 2,010.42 | 2,304.82 | +14.64% |
| Average slot time (ms) | 267.20 | 268.60 | +0.52% |
| Active validators | 674.00 | 672.00 | -0.30% |
| Delinquent validators | 8.00 | 13.00 | +62.50% |
| Solana TVL | 6,552,189,378.00 | 6,781,683,220.00 | +3.50% |
| SOL price | 118.18 | 120.74 | +2.17% |
| Stablecoin supply | 16,723,366,837.00 | 16,885,339,627.00 | +0.97% |
| 24h DEX volume | 1,926,466,128.71 | 1,708,158,585.63 | -11.33% |
| 24h chain fees | 15,421,946.25 | 16,123,937.37 | +4.55% |

### Change over 30d (vs run at 2026-09-05T19:38:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,427.43 | 4,796.58 | +39.95% |
| Average non-vote TPS | 1,291.31 | 2,304.82 | +78.49% |
| Average slot time (ms) | 315.00 | 268.60 | -14.73% |
| Active validators | 675.00 | 672.00 | -0.44% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,915,402,920.00 | 6,781,683,220.00 | +14.64% |
| SOL price | 103.80 | 120.74 | +16.32% |
| Stablecoin supply | 16,607,441,030.00 | 16,885,339,627.00 | +1.67% |
| 24h DEX volume | 1,881,639,252.00 | 1,708,158,585.63 | -9.22% |
| 24h chain fees | 10,436,292.55 | 16,123,937.37 | +54.50% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
