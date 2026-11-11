# Solana Ecosystem Pulse

**Generated:** 2026-11-11T13:03:35Z · **Schema:** `1.0.0` · **Collection time:** 19.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $83.71 | -1.25% |
| Market cap | $49.53B | rank #7 |
| Total value locked | $5.07B | -0.17% |
| Stablecoin supply | $14.78B | -0.33% |
| DEX volume (24h) | $1.34B | -9.79% |
| Chain fees / REV (24h) | $8.40M | -10.16% |
| Non-vote TPS (1h avg) | 1,607 | peak 2,088 total |
| Active validators | 659 | 40 delinquent |
| Epoch 1083 | 64.18% complete | 154,746 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,606.6 average over the last 60 minutes; 1,644.0 in the latest sample.
- **Total TPS:** 1,606.6 average, 2,087.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.6 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 446,149,624 at absolute slot 468,133,254.
- **Epoch 1083:** slot 277,254 of 432,000 (64.18% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.562% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 199 ms |
| `solana-rpc.publicnode.com` | yes | 132 ms |
| `api.mainnet.solana.com` | yes | 207 ms |

## Validators & stake

- **659 active** validators, **40 delinquent** (5.72% by count, 0.221% by stake).
- **Total stake:** 433,423,964 SOL ($36.28B); stake rate 68.00% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 46.58% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 221 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,764,485 | 3.876% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,564,685 | 3.830% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,031,625 | 3.013% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,254 | 2.339% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,644,051 | 2.230% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,571,015 | 2.213% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,999 | 2.135% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,330 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,248 | 1.616% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,729,845 | 1.556% | 5% |

## Economics

- **SOL:** $83.71 (-1.25% 24h, -9.55% 7d, -24.02% 30d). Market cap $49.53B, 24h volume $2.88B (5.82% of cap). Price source: `coingecko`.
- **TVL:** $5.07B across 343 protocols - rank #3 of 423 chains, 6.53% of all tracked chain TVL. -6.35% over 7d, -60.3% from its ATH.
- **Stablecoins:** $14.78B circulating on Solana (-1.58% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.34B in 24h, $10.85B over 7d across 141 venues. Volume/TVL turnover 0.265x per day.
- **REV (chain fees):** $8.40M in 24h, $332.15M over 30d. Retained chain revenue $2.77M (33.0% of fees). Annualised fees are 6.19% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,408,400 SOL circulating of 637,371,902 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.49B | -0.8% | -7.6% |
| 2 | Kamino Lend | Lending | $1.16B | -0.2% | -5.2% |
| 3 | Jupiter Lend | Lending | $973.06M | +8.5% | -3.7% |
| 4 | Raydium AMM | Dexs | $950.63M | -1.0% | -8.1% |
| 5 | Binance Staked SOL | Liquid Staking | $908.96M | -1.2% | -10.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $857.94M | -1.1% | -9.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $634.39M | -0.5% | -5.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $427.64M | -1.0% | -8.2% |
| 9 | Sentora Curator | Risk Curators | $373.40M | -0.3% | -0.1% |
| 10 | OnRe | RWA | $309.26M | -0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $288.69M | -3.4% | -13.2% |
| 12 | PumpSwap | Dexs | $270.62M | -1.0% | -13.2% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.36B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.7% · Dexs 14.9% · Derivatives 5.2% · RWA 4.4% · Risk Curators 4.0%

### Tokenised assets

$844.79M of tokenised real-world assets and equities are locked on Solana - 6.324% of chain TVL.

- OnRe (RWA): $309.26M
- Huma (RWA): $225.88M
- Solstice (Basis Trading): $201.13M
- JupUSD (Basis Trading): $43.70M
- Plume Vaults (RWA): $36.90M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-10
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06

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

### Change over 24h (vs run at 2026-11-10T13:51:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,797.16 | 1,606.62 | -10.60% |
| Average non-vote TPS | 1,797.16 | 1,606.62 | -10.60% |
| Average slot time (ms) | 214.20 | 214.60 | +0.19% |
| Active validators | 657.00 | 659.00 | +0.30% |
| Delinquent validators | 41.00 | 40.00 | -2.44% |
| Solana TVL | 5,023,282,930.00 | 5,072,108,301.00 | +0.97% |
| SOL price | 84.45 | 83.71 | -0.88% |
| Stablecoin supply | 14,832,999,164.00 | 14,784,717,550.00 | -0.33% |
| 24h DEX volume | 1,487,777,537.32 | 1,342,063,202.34 | -9.79% |
| 24h chain fees | 9,381,055.72 | 8,399,659.99 | -10.46% |

### Change over 7d (vs run at 2026-11-04T13:23:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,488.22 | 1,606.62 | +7.96% |
| Average non-vote TPS | 1,488.22 | 1,606.62 | +7.96% |
| Average slot time (ms) | 214.10 | 214.60 | +0.23% |
| Active validators | 662.00 | 659.00 | -0.45% |
| Delinquent validators | 31.00 | 40.00 | +29.03% |
| Solana TVL | 5,464,731,305.00 | 5,072,108,301.00 | -7.18% |
| SOL price | 92.65 | 83.71 | -9.65% |
| Stablecoin supply | 14,903,033,514.00 | 14,784,717,550.00 | -0.79% |
| 24h DEX volume | 1,881,110,224.90 | 1,342,063,202.34 | -28.66% |
| 24h chain fees | 11,334,057.17 | 8,399,659.99 | -25.89% |

### Change over 30d (vs run at 2026-10-12T23:52:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,094.70 | 1,606.62 | -68.46% |
| Average non-vote TPS | 2,039.01 | 1,606.62 | -21.21% |
| Average slot time (ms) | 218.80 | 214.60 | -1.92% |
| Active validators | 672.00 | 659.00 | -1.93% |
| Delinquent validators | 8.00 | 40.00 | +400.00% |
| Solana TVL | 6,087,233,347.00 | 5,072,108,301.00 | -16.68% |
| SOL price | 105.47 | 83.71 | -20.63% |
| Stablecoin supply | 16,359,920,349.00 | 14,784,717,550.00 | -9.63% |
| 24h DEX volume | 1,277,023,682.31 | 1,342,063,202.34 | +5.09% |
| 24h chain fees | 11,301,815.14 | 8,399,659.99 | -25.68% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.9s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
