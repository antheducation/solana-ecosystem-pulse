# Solana Ecosystem Pulse

**Generated:** 2026-09-16T20:32:05Z · **Schema:** `1.0.0` · **Collection time:** 17.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.40 | +1.68% |
| Market cap | $57.73B | rank #7 |
| Total value locked | $5.72B | -3.29% |
| Stablecoin supply | $15.96B | -2.59% |
| DEX volume (24h) | $2.70B | +6.84% |
| Chain fees / REV (24h) | $14.08M | +3.71% |
| Non-vote TPS (1h avg) | 2,745 | peak 5,502 total |
| Active validators | 677 | 14 delinquent |
| Epoch 1036 | 14.36% complete | 369,971 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 84 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,744.6 average over the last 60 minutes; 2,406.7 in the latest sample.
- **Total TPS:** 4,850.9 average, 5,502.0 peak. Consensus votes account for 43.4% of all transactions.
- **Slot time:** 318.6 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 425,655,379 at absolute slot 447,614,029.
- **Epoch 1036:** slot 62,029 of 432,000 (14.36% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.644% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 223 ms |
| `solana-rpc.publicnode.com` | yes | 253 ms |
| `api.mainnet.solana.com` | yes | 155 ms |

## Validators & stake

- **677 active** validators, **14 delinquent** (2.03% by count, 0.044% by stake).
- **Total stake:** 439,761,083 SOL ($43.27B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.36%; 243 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,767,428 | 4.042% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,352,114 | 3.720% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,485,145 | 2.840% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,383,247 | 2.590% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,740,877 | 2.216% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,273 | 2.106% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,049,051 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,386,183 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,076,306 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,558,592 | 1.492% | 0% |

## Economics

- **SOL:** $98.40 (+1.68% 24h, -3.82% 7d, +29.93% 30d). Market cap $57.73B, 24h volume $3.49B (6.05% of cap). Price source: `coingecko`.
- **TVL:** $5.72B across 331 protocols - rank #2 of 468 chains, 6.62% of all tracked chain TVL. -3.87% over 7d, -56.8% from its ATH.
- **Stablecoins:** $15.96B circulating on Solana (-4.01% 7d) - $2.79 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.70B in 24h, $18.12B over 7d across 123 venues. Volume/TVL turnover 0.472x per day.
- **REV (chain fees):** $14.08M in 24h, $402.21M over 30d. Retained chain revenue $5.22M (37.1% of fees). Annualised fees are 8.90% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,150,284 SOL circulating of 634,205,210 total (92.58%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | +0.6% | -2.0% |
| 2 | Kamino Lend | Lending | $1.33B | -0.7% | -2.1% |
| 3 | Raydium AMM | Dexs | $1.10B | -1.5% | -3.9% |
| 4 | Jupiter Lend | Lending | $1.06B | -2.0% | -4.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.01B | -1.9% | -6.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.01B | -2.0% | -5.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $732.25M | -0.9% | -2.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $505.36M | -1.8% | -5.7% |
| 9 | Marinade Native | Staking Pool | $372.48M | -1.8% | -7.5% |
| 10 | Sentora Curator | Risk Curators | $371.20M | -3.2% | -3.5% |
| 11 | PumpSwap | Dexs | $315.57M | -2.8% | -6.0% |
| 12 | OnRe | RWA | $302.27M | +0.6% | -0.7% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 331 protocols the total is $14.57B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.7% · Lending 18.1% · Dexs 15.4% · Derivatives 5.5% · Risk Curators 4.1% · Staking Pool 4.0%

### Tokenised assets

$871.95M of tokenised real-world assets and equities are locked on Solana - 5.984% of chain TVL.

- OnRe (RWA): $302.27M
- Solstice (Basis Trading): $234.93M
- Huma Finance V2 (RWA): $177.51M
- JupUSD (Basis Trading): $46.81M
- Plume Vaults (RWA): $28.34M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-16
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-16
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-15
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09

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

### Change over 24h (vs run at 2026-09-15T20:32:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,770.98 | 4,850.92 | +1.68% |
| Average non-vote TPS | 2,641.86 | 2,744.58 | +3.89% |
| Average slot time (ms) | 317.40 | 318.60 | +0.38% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 5,793,334,701.00 | 5,723,932,041.00 | -1.20% |
| SOL price | 96.94 | 98.40 | +1.51% |
| Stablecoin supply | 16,388,645,734.00 | 15,963,602,798.00 | -2.59% |
| 24h DEX volume | 2,530,223,236.85 | 2,703,297,666.22 | +6.84% |
| 24h chain fees | 13,579,950.58 | 14,083,156.46 | +3.71% |

### Change over 7d (vs run at 2026-09-09T20:07:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,453.09 | 4,850.92 | +8.93% |
| Average non-vote TPS | 2,342.31 | 2,744.58 | +17.17% |
| Average slot time (ms) | 319.30 | 318.60 | -0.22% |
| Active validators | 675.00 | 677.00 | +0.30% |
| Delinquent validators | 13.00 | 14.00 | +7.69% |
| Solana TVL | 5,948,260,786.00 | 5,723,932,041.00 | -3.77% |
| SOL price | 102.19 | 98.40 | -3.71% |
| Stablecoin supply | 16,629,873,212.00 | 15,963,602,798.00 | -4.01% |
| 24h DEX volume | 2,710,734,376.34 | 2,703,297,666.22 | -0.27% |
| 24h chain fees | 16,561,493.38 | 14,083,156.46 | -14.96% |

### Change over 30d (vs run at 2026-08-17T18:19:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,422.32 | 4,850.92 | +9.69% |
| Average non-vote TPS | 2,781.61 | 2,744.58 | -1.33% |
| Average slot time (ms) | 415.70 | 318.60 | -23.36% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 7.00 | 14.00 | +100.00% |
| Solana TVL | 4,849,572,817.00 | 5,723,932,041.00 | +18.03% |
| SOL price | 75.94 | 98.40 | +29.58% |
| Stablecoin supply | 16,003,787,085.00 | 15,963,602,798.00 | -0.25% |
| 24h DEX volume | 1,055,467,633.95 | 2,703,297,666.22 | +156.12% |
| 24h chain fees | 6,802,409.48 | 14,083,156.46 | +107.03% |

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
