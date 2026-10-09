# Solana Ecosystem Pulse

**Generated:** 2026-10-09T12:11:10Z · **Schema:** `1.0.0` · **Collection time:** 17.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $111.20 | -1.55% |
| Market cap | $65.38B | rank #7 |
| Total value locked | $6.23B | -3.36% |
| Stablecoin supply | $16.38B | -1.39% |
| DEX volume (24h) | $2.64B | +19.91% |
| Chain fees / REV (24h) | $14.97M | +4.64% |
| Non-vote TPS (1h avg) | 1,657 | peak 5,406 total |
| Active validators | 673 | 8 delinquent |
| Epoch 1052 | 92.24% complete | 33,527 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,657.0 average over the last 60 minutes; 1,530.7 in the latest sample.
- **Total TPS:** 4,156.3 average, 5,406.0 peak. Consensus votes account for 60.1% of all transactions.
- **Slot time:** 268.3 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 432,899,782 at absolute slot 454,862,473.
- **Epoch 1052:** slot 398,473 of 432,000 (92.24% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.612% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 134 ms |
| `solana-rpc.publicnode.com` | yes | 105 ms |
| `api.mainnet.solana.com` | yes | 258 ms |

## Validators & stake

- **673 active** validators, **8 delinquent** (1.17% by count, 0.007% by stake).
- **Total stake:** 439,005,453 SOL ($48.82B); stake rate 69.08% of total supply.
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

- **SOL:** $111.20 (-1.55% 24h, -8.73% 7d, +6.68% 30d). Market cap $65.38B, 24h volume $4.89B (7.48% of cap). Price source: `coingecko`.
- **TVL:** $6.23B across 336 protocols - rank #2 of 469 chains, 6.80% of all tracked chain TVL. -5.12% over 7d, -52.9% from its ATH.
- **Stablecoins:** $16.38B circulating on Solana (-1.24% 7d) - $2.63 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.64B in 24h, $14.98B over 7d across 126 venues. Volume/TVL turnover 0.424x per day.
- **REV (chain fees):** $14.97M in 24h, $452.77M over 30d. Retained chain revenue $5.32M (35.6% of fees). Annualised fees are 8.36% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,697,417 SOL circulating of 635,458,896 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | -3.0% | -5.6% |
| 2 | Kamino Lend | Lending | $1.33B | -2.0% | -3.2% |
| 3 | Raydium AMM | Dexs | $1.24B | -3.3% | -7.9% |
| 4 | Jupiter Lend | Lending | $1.16B | -3.7% | -2.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.15B | -3.2% | -7.0% |
| 6 | Binance Staked SOL | Liquid Staking | $1.13B | -4.4% | -7.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $775.52M | -1.5% | -4.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $570.76M | -3.5% | -6.6% |
| 9 | Sentora Curator | Risk Curators | $497.50M | -0.9% | +26.2% |
| 10 | Marinade Native | Staking Pool | $408.92M | -4.9% | -7.1% |
| 11 | PumpSwap | Dexs | $372.91M | -3.3% | -5.5% |
| 12 | Orca DEX | Dexs | $309.52M | -3.1% | -2.3% |

The top five protocols hold 40.4% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.59B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.7% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.8%

### Tokenised assets

$887.04M of tokenised real-world assets and equities are locked on Solana - 5.347% of chain TVL.

- OnRe (RWA): $293.57M
- Huma (RWA): $256.90M
- Solstice (Basis Trading): $211.54M
- JupUSD (Basis Trading): $47.35M
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

### Change over 24h (vs run at 2026-10-08T12:21:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,241.77 | 4,156.32 | -2.01% |
| Average non-vote TPS | 1,740.45 | 1,656.99 | -4.80% |
| Average slot time (ms) | 267.20 | 268.30 | +0.41% |
| Active validators | 670.00 | 673.00 | +0.45% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 6,406,632,483.00 | 6,231,947,843.00 | -2.73% |
| SOL price | 113.01 | 111.20 | -1.60% |
| Stablecoin supply | 16,610,278,482.00 | 16,377,840,192.00 | -1.40% |
| 24h DEX volume | 2,205,685,057.81 | 2,644,852,886.24 | +19.91% |
| 24h chain fees | 13,669,849.90 | 14,970,162.23 | +9.51% |

### Change over 7d (vs run at 2026-10-02T11:27:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,940.87 | 4,156.32 | +5.47% |
| Average non-vote TPS | 1,426.72 | 1,656.99 | +16.14% |
| Average slot time (ms) | 266.20 | 268.30 | +0.79% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 12.00 | 8.00 | -33.33% |
| Solana TVL | 6,693,361,792.00 | 6,231,947,843.00 | -6.89% |
| SOL price | 122.06 | 111.20 | -8.90% |
| Stablecoin supply | 16,579,036,964.00 | 16,377,840,192.00 | -1.21% |
| 24h DEX volume | 2,488,460,102.88 | 2,644,852,886.24 | +6.28% |
| 24h chain fees | 16,959,932.19 | 14,970,162.23 | -11.73% |

### Change over 30d (vs run at 2026-09-09T20:07:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,453.09 | 4,156.32 | -6.66% |
| Average non-vote TPS | 2,342.31 | 1,656.99 | -29.26% |
| Average slot time (ms) | 319.30 | 268.30 | -15.97% |
| Active validators | 675.00 | 673.00 | -0.30% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 5,948,260,786.00 | 6,231,947,843.00 | +4.77% |
| SOL price | 102.19 | 111.20 | +8.82% |
| Stablecoin supply | 16,629,873,212.00 | 16,377,840,192.00 | -1.52% |
| 24h DEX volume | 2,710,734,376.34 | 2,644,852,886.24 | -2.43% |
| 24h chain fees | 16,561,493.38 | 14,970,162.23 | -9.61% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
