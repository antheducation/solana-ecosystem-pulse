# Solana Ecosystem Pulse

**Generated:** 2026-10-11T02:30:59Z · **Schema:** `1.0.0` · **Collection time:** 15.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $109.93 | +0.25% |
| Market cap | $64.76B | rank #7 |
| Total value locked | $6.22B | +0.18% |
| Stablecoin supply | $16.41B | -0.11% |
| DEX volume (24h) | $1.58B | -20.13% |
| Chain fees / REV (24h) | $11.98M | -13.93% |
| Non-vote TPS (1h avg) | 1,517 | peak 4,988 total |
| Active validators | 674 | 6 delinquent |
| Epoch 1054 | 36.75% complete | 273,227 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 217.60 sits 16.4 sigma below the median of the last 102 runs (268.60, -19.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,517.2 average over the last 60 minutes; 1,407.8 in the latest sample.
- **Total TPS:** 4,606.3 average, 4,987.8 peak. Consensus votes account for 67.1% of all transactions.
- **Slot time:** 217.6 ms average (target 400 ms), worst 1-minute bucket 224.7 ms.
- **Block height:** 433,523,937 at absolute slot 455,486,773.
- **Epoch 1054:** slot 158,773 of 432,000 (36.75% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.608% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 124 ms |
| `solana-rpc.publicnode.com` | yes | 129 ms |
| `api.mainnet.solana.com` | yes | 57 ms |

## Validators & stake

- **674 active** validators, **6 delinquent** (0.88% by count, 0.122% by stake).
- **Total stake:** 438,737,964 SOL ($48.23B); stake rate 69.03% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.50% and top 33 hold 45.88% of active stake.
- **Commission:** median 5.0%, mean 12.92%; 232 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,775,444 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,954,957 | 3.641% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,356 | 2.810% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,145,934 | 2.544% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,754,664 | 2.454% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,328,689 | 2.129% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,266 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,603,786 | 1.735% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,810,142 | 1.554% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,421,774 | 1.465% | 0% |

## Economics

- **SOL:** $109.93 (+0.25% 24h, -8.49% 7d, +10.58% 30d). Market cap $64.76B, 24h volume $1.51B (2.33% of cap). Price source: `coingecko`.
- **TVL:** $6.22B across 336 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -5.95% over 7d, -53.0% from its ATH.
- **Stablecoins:** $16.41B circulating on Solana (-2.80% 7d) - $2.64 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.58B in 24h, $13.34B over 7d across 130 venues. Volume/TVL turnover 0.254x per day.
- **REV (chain fees):** $11.98M in 24h, $474.54M over 30d. Retained chain revenue $4.56M (38.1% of fees). Annualised fees are 6.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,051,450 SOL circulating of 635,598,443 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +0.2% | -7.6% |
| 2 | Kamino Lend | Lending | $1.33B | +0.4% | -4.1% |
| 3 | Raydium AMM | Dexs | $1.25B | +0.9% | -7.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.15B | +0.3% | -7.8% |
| 5 | Jupiter Lend | Lending | $1.14B | +0.3% | -2.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.13B | +0.3% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $770.87M | -0.2% | -5.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $567.90M | +0.3% | -8.1% |
| 9 | Sentora Curator | Risk Curators | $490.85M | -1.2% | +31.0% |
| 10 | Marinade Native | Staking Pool | $407.18M | +0.3% | -8.4% |
| 11 | PumpSwap | Dexs | $367.31M | +0.9% | -8.2% |
| 12 | Orca DEX | Dexs | $310.65M | +0.7% | -2.7% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.54B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.7% · Dexs 15.5% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$883.98M of tokenised real-world assets and equities are locked on Solana - 5.343% of chain TVL.

- OnRe (RWA): $292.40M
- Huma (RWA): $255.91M
- Solstice (Basis Trading): $210.53M
- JupUSD (Basis Trading): $47.33M
- Plume Vaults (RWA): $33.13M

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

- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-11
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-11
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-10
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-10

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

### Change over 24h (vs run at 2026-10-10T03:00:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,740.69 | 4,606.30 | -2.83% |
| Average non-vote TPS | 1,669.34 | 1,517.17 | -9.12% |
| Average slot time (ms) | 218.70 | 217.60 | -0.50% |
| Active validators | 674.00 | 674.00 | +0.00% |
| Delinquent validators | 6.00 | 6.00 | +0.00% |
| Solana TVL | 6,187,946,925.00 | 6,218,958,410.00 | +0.50% |
| SOL price | 109.79 | 109.93 | +0.13% |
| Stablecoin supply | 16,427,773,068.00 | 16,409,963,032.00 | -0.11% |
| 24h DEX volume | 2,215,423,677.91 | 1,579,981,826.57 | -28.68% |
| 24h chain fees | 13,940,731.19 | 11,975,476.33 | -14.10% |

### Change over 7d (vs run at 2026-10-04T03:07:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,226.99 | 4,606.30 | +8.97% |
| Average non-vote TPS | 1,721.51 | 1,517.17 | -11.87% |
| Average slot time (ms) | 266.60 | 217.60 | -18.38% |
| Active validators | 671.00 | 674.00 | +0.45% |
| Delinquent validators | 14.00 | 6.00 | -57.14% |
| Solana TVL | 6,668,023,483.00 | 6,218,958,410.00 | -6.73% |
| SOL price | 120.36 | 109.93 | -8.67% |
| Stablecoin supply | 16,880,130,771.00 | 16,409,963,032.00 | -2.79% |
| 24h DEX volume | 2,132,195,295.11 | 1,579,981,826.57 | -25.90% |
| 24h chain fees | 12,977,249.54 | 11,975,476.33 | -7.72% |

### Change over 30d (vs run at 2026-09-10T20:09:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,122.54 | 4,606.30 | +11.73% |
| Average non-vote TPS | 1,990.17 | 1,517.17 | -23.77% |
| Average slot time (ms) | 315.50 | 217.60 | -31.03% |
| Active validators | 677.00 | 674.00 | -0.44% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 5,779,330,766.00 | 6,218,958,410.00 | +7.61% |
| SOL price | 99.77 | 109.93 | +10.18% |
| Stablecoin supply | 16,576,239,978.00 | 16,409,963,032.00 | -1.00% |
| 24h DEX volume | 3,000,435,429.63 | 1,579,981,826.57 | -47.34% |
| 24h chain fees | 15,717,207.17 | 11,975,476.33 | -23.81% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
