# Solana Ecosystem Pulse

**Generated:** 2026-09-19T19:41:16Z · **Schema:** `1.0.0` · **Collection time:** 14.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $111.27 | -2.12% |
| Market cap | $65.36B | rank #7 |
| Total value locked | $6.24B | +5.87% |
| Stablecoin supply | $15.88B | +1.03% |
| DEX volume (24h) | $3.54B | +36.44% |
| Chain fees / REV (24h) | $17.46M | +18.99% |
| Non-vote TPS (1h avg) | 2,162 | peak 5,542 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1038 | 20.58% complete | 343,108 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 87 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 267.00 sits 22.5 sigma below the median of the last 87 runs (317.10, -15.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,243,262,565.00 sits 3.1 sigma above the median of the last 87 runs (5,851,427,899.00, +6.7%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,161.6 average over the last 60 minutes; 2,163.4 in the latest sample.
- **Total TPS:** 4,683.7 average, 5,541.6 peak. Consensus votes account for 53.8% of all transactions.
- **Slot time:** 267.0 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 426,545,658 at absolute slot 448,504,892.
- **Epoch 1038:** slot 88,892 of 432,000 (20.58% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.640% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 194 ms |
| `solana-rpc.publicnode.com` | yes | 123 ms |
| `api.mainnet.solana.com` | yes | 82 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.036% by stake).
- **Total stake:** 440,227,371 SOL ($48.98B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.23%; 242 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,849,776 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,819,247 | 3.595% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,500,805 | 2.841% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,362,749 | 2.582% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,786,807 | 2.224% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,843 | 2.103% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,116,740 | 2.072% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,434,776 | 1.689% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,086,871 | 1.610% | 5% |
| 10 | `HZKopZYvv8v6un2H6KUNVQCnK5zM9emKKezvqhTBSpEc` | 6,627,951 | 1.506% | 100% |

## Economics

- **SOL:** $111.27 (-2.12% 24h, +9.50% 7d, +28.09% 30d). Market cap $65.36B, 24h volume $3.33B (5.10% of cap). Price source: `coingecko`.
- **TVL:** $6.24B across 333 protocols - rank #2 of 468 chains, 6.66% of all tracked chain TVL. +5.82% over 7d, -52.8% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (-4.37% 7d) - $2.54 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.54B in 24h, $17.70B over 7d across 124 venues. Volume/TVL turnover 0.566x per day.
- **REV (chain fees):** $17.46M in 24h, $415.69M over 30d. Retained chain revenue $6.17M (35.3% of fees). Annualised fees are 9.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,367,707 SOL circulating of 634,376,179 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -0.7% | +13.3% |
| 2 | Kamino Lend | Lending | $1.39B | -0.5% | +3.2% |
| 3 | Raydium AMM | Dexs | $1.26B | +0.1% | +10.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.16B | -0.4% | +8.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.15B | -0.6% | +9.6% |
| 6 | Jupiter Lend | Lending | $1.14B | -0.6% | +3.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $792.27M | -1.2% | +5.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $576.03M | -1.1% | +8.8% |
| 9 | Marinade Native | Staking Pool | $426.13M | -0.6% | +9.1% |
| 10 | Sentora Curator | Risk Curators | $364.43M | -1.3% | -6.0% |
| 11 | PumpSwap | Dexs | $362.43M | -1.1% | +9.3% |
| 12 | Drift Staked SOL | Liquid Staking | $312.89M | -1.1% | +8.5% |

The top five protocols hold 41.8% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.13B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.2% · Lending 17.4% · Dexs 15.7% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$882.27M of tokenised real-world assets and equities are locked on Solana - 5.468% of chain TVL.

- OnRe (RWA): $304.04M
- Solstice (Basis Trading): $232.44M
- Huma Finance V2 (RWA): $201.47M
- JupUSD (Basis Trading): $46.71M
- Plume Vaults (RWA): $28.12M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) - Thu, 10 Sep 2026 20:16:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | pre-release |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-19
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17

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

### Change over 24h (vs run at 2026-09-18T20:04:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,950.64 | 4,683.68 | -5.39% |
| Average non-vote TPS | 2,440.09 | 2,161.60 | -11.41% |
| Average slot time (ms) | 267.70 | 267.00 | -0.26% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 6,242,343,437.00 | 6,243,262,565.00 | +0.01% |
| SOL price | 113.98 | 111.27 | -2.38% |
| Stablecoin supply | 15,713,039,562.00 | 15,875,774,561.00 | +1.04% |
| 24h DEX volume | 2,592,123,183.29 | 3,536,797,881.43 | +36.44% |
| 24h chain fees | 14,675,830.10 | 17,457,812.00 | +18.96% |

### Change over 7d (vs run at 2026-09-12T19:46:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,285.77 | 4,683.68 | +9.28% |
| Average non-vote TPS | 2,164.34 | 2,161.60 | -0.13% |
| Average slot time (ms) | 317.70 | 267.00 | -15.96% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 11.00 | 13.00 | +18.18% |
| Solana TVL | 5,903,101,578.00 | 6,243,262,565.00 | +5.76% |
| SOL price | 101.32 | 111.27 | +9.82% |
| Stablecoin supply | 16,554,268,556.00 | 15,875,774,561.00 | -4.10% |
| 24h DEX volume | 3,183,599,712.43 | 3,536,797,881.43 | +11.09% |
| 24h chain fees | 17,875,390.26 | 17,457,812.00 | -2.34% |

### Change over 30d (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 4,683.68 | -6.96% |
| Average non-vote TPS | 3,388.67 | 2,161.60 | -36.21% |
| Average slot time (ms) | 417.00 | 267.00 | -35.97% |
| Active validators | 690.00 | 677.00 | -1.88% |
| Delinquent validators | 6.00 | 13.00 | +116.67% |
| Solana TVL | 5,300,056,423.00 | 6,243,262,565.00 | +17.80% |
| SOL price | 86.96 | 111.27 | +27.96% |
| Stablecoin supply | 16,325,927,693.00 | 15,875,774,561.00 | -2.76% |
| 24h DEX volume | 3,009,837,694.95 | 3,536,797,881.43 | +17.51% |
| 24h chain fees | 13,676,729.38 | 17,457,812.00 | +27.65% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
