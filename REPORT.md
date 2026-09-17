# Solana Ecosystem Pulse

**Generated:** 2026-09-17T02:03:12Z · **Schema:** `1.0.0` · **Collection time:** 12.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.21 | +2.78% |
| Market cap | $58.25B | rank #7 |
| Total value locked | $5.74B | +0.02% |
| Stablecoin supply | $15.77B | -1.19% |
| DEX volume (24h) | $2.73B | +1.11% |
| Chain fees / REV (24h) | $14.04M | -0.21% |
| Non-vote TPS (1h avg) | 2,153 | peak 5,080 total |
| Active validators | 679 | 12 delinquent |
| Epoch 1036 | 28.85% complete | 307,350 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 84 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,153.2 average over the last 60 minutes; 1,771.4 in the latest sample.
- **Total TPS:** 4,281.3 average, 5,079.6 peak. Consensus votes account for 49.7% of all transactions.
- **Slot time:** 317.2 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 425,717,938 at absolute slot 447,676,650.
- **Epoch 1036:** slot 124,650 of 432,000 (28.85% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.644% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 159 ms |
| `solana-rpc.publicnode.com` | yes | 126 ms |
| `api.mainnet.solana.com` | yes | 48 ms |

## Validators & stake

- **679 active** validators, **12 delinquent** (1.74% by count, 0.035% by stake).
- **Total stake:** 439,761,083 SOL ($43.63B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.48%; 243 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,767,428 | 4.042% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,352,114 | 3.720% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,485,145 | 2.840% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,383,247 | 2.589% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,740,877 | 2.216% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,273 | 2.106% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,049,051 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,386,183 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,076,306 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,558,592 | 1.492% | 0% |

## Economics

- **SOL:** $99.21 (+2.78% 24h, -1.80% 7d, +31.34% 30d). Market cap $58.25B, 24h volume $3.42B (5.87% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 332 protocols - rank #2 of 468 chains, 6.61% of all tracked chain TVL. -2.02% over 7d, -56.6% from its ATH.
- **Stablecoins:** $15.77B circulating on Solana (-5.01% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.73B in 24h, $16.51B over 7d across 123 venues. Volume/TVL turnover 0.476x per day.
- **REV (chain fees):** $14.04M in 24h, $394.49M over 30d. Retained chain revenue $5.00M (35.6% of fees). Annualised fees are 8.80% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,212,565 SOL circulating of 634,204,991 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | +1.1% | +0.5% |
| 2 | Kamino Lend | Lending | $1.33B | +0.1% | -0.7% |
| 3 | Raydium AMM | Dexs | $1.11B | +1.3% | -2.1% |
| 4 | Jupiter Lend | Lending | $1.06B | -1.7% | -2.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.02B | +1.9% | -1.4% |
| 6 | Binance Staked SOL | Liquid Staking | $1.02B | +1.7% | -2.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $730.63M | +0.2% | -1.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $508.77M | +1.3% | -2.8% |
| 9 | Sentora Curator | Risk Curators | $372.26M | -2.8% | -3.8% |
| 10 | Marinade Native | Staking Pool | $371.48M | +0.4% | -4.2% |
| 11 | PumpSwap | Dexs | $321.14M | +1.1% | -1.6% |
| 12 | OnRe | RWA | $302.48M | +0.6% | -1.6% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 332 protocols the total is $14.64B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.8% · Lending 18.0% · Dexs 15.5% · Derivatives 5.5% · Risk Curators 4.1% · Staking Pool 4.0%

### Tokenised assets

$878.83M of tokenised real-world assets and equities are locked on Solana - 6.002% of chain TVL.

- OnRe (RWA): $302.48M
- Solstice (Basis Trading): $234.93M
- Huma Finance V2 (RWA): $184.08M
- JupUSD (Basis Trading): $46.81M
- Plume Vaults (RWA): $28.45M

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

- [SIMD-0123: SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-16
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-16
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-15
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11

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

### Change over 24h (vs run at 2026-09-16T01:59:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,022.26 | 4,281.28 | -14.75% |
| Average non-vote TPS | 2,919.81 | 2,153.15 | -26.26% |
| Average slot time (ms) | 319.70 | 317.20 | -0.78% |
| Active validators | 679.00 | 679.00 | +0.00% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,720,302,510.00 | 5,738,424,911.00 | +0.32% |
| SOL price | 96.37 | 99.21 | +2.95% |
| Stablecoin supply | 15,965,873,344.00 | 15,774,289,704.00 | -1.20% |
| 24h DEX volume | 2,497,627,822.22 | 2,733,437,291.18 | +9.44% |
| 24h chain fees | 13,951,641.96 | 14,036,672.88 | +0.61% |

### Change over 7d (vs run at 2026-09-10T01:45:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,072.55 | 4,281.28 | +5.13% |
| Average non-vote TPS | 1,943.91 | 2,153.15 | +10.76% |
| Average slot time (ms) | 315.60 | 317.20 | +0.51% |
| Active validators | 675.00 | 679.00 | +0.59% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,785,220,596.00 | 5,738,424,911.00 | -0.81% |
| SOL price | 100.93 | 99.21 | -1.70% |
| Stablecoin supply | 16,629,480,845.00 | 15,774,289,704.00 | -5.14% |
| 24h DEX volume | 2,555,510,166.63 | 2,733,437,291.18 | +6.96% |
| 24h chain fees | 15,507,501.83 | 14,036,672.88 | -9.48% |

### Change over 30d (vs run at 2026-08-17T18:19:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,422.32 | 4,281.28 | -3.19% |
| Average non-vote TPS | 2,781.61 | 2,153.15 | -22.59% |
| Average slot time (ms) | 415.70 | 317.20 | -23.69% |
| Active validators | 688.00 | 679.00 | -1.31% |
| Delinquent validators | 7.00 | 12.00 | +71.43% |
| Solana TVL | 4,849,572,817.00 | 5,738,424,911.00 | +18.33% |
| SOL price | 75.94 | 99.21 | +30.64% |
| Stablecoin supply | 16,003,787,085.00 | 15,774,289,704.00 | -1.43% |
| 24h DEX volume | 1,055,467,633.95 | 2,733,437,291.18 | +158.98% |
| 24h chain fees | 6,802,409.48 | 14,036,672.88 | +106.35% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
