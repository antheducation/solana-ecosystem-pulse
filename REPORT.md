# Solana Ecosystem Pulse

**Generated:** 2026-09-19T14:55:49Z · **Schema:** `1.0.0` · **Collection time:** 23.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $111.73 | +0.98% |
| Market cap | $65.63B | rank #7 |
| Total value locked | $6.25B | +5.92% |
| Stablecoin supply | $15.88B | +1.03% |
| DEX volume (24h) | $3.54B | +36.44% |
| Chain fees / REV (24h) | $17.46M | +18.99% |
| Non-vote TPS (1h avg) | 1,777 | peak 4,764 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1038 | 5.75% complete | 407,171 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 87 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.80 sits 22.6 sigma below the median of the last 87 runs (317.10, -15.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,245,959,676.00 sits 3.2 sigma above the median of the last 87 runs (5,851,427,899.00, +6.7%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,776.9 average over the last 60 minutes; 2,101.8 in the latest sample.
- **Total TPS:** 4,303.7 average, 4,764.0 peak. Consensus votes account for 58.7% of all transactions.
- **Slot time:** 266.8 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 426,481,639 at absolute slot 448,440,829.
- **Epoch 1038:** slot 24,829 of 432,000 (5.75% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.640% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 776 ms |
| `solana-rpc.publicnode.com` | yes | 29 ms |
| `api.mainnet.solana.com` | yes | 522 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.036% by stake).
- **Total stake:** 440,227,371 SOL ($49.19B); stake rate 69.40% of total supply.
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

- **SOL:** $111.73 (+0.98% 24h, +9.59% 7d, +29.18% 30d). Market cap $65.63B, 24h volume $4.39B (6.70% of cap). Price source: `coingecko`.
- **TVL:** $6.25B across 333 protocols - rank #2 of 468 chains, 6.68% of all tracked chain TVL. +5.87% over 7d, -52.8% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (-4.37% 7d) - $2.54 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.54B in 24h, $17.70B over 7d across 124 venues. Volume/TVL turnover 0.566x per day.
- **REV (chain fees):** $17.46M in 24h, $415.69M over 30d. Retained chain revenue $6.17M (35.3% of fees). Annualised fees are 9.71% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,367,918 SOL circulating of 634,376,390 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | +4.0% | +13.4% |
| 2 | Kamino Lend | Lending | $1.39B | +2.4% | +3.4% |
| 3 | Raydium AMM | Dexs | $1.26B | +4.9% | +10.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.16B | +5.7% | +9.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.16B | +5.7% | +9.9% |
| 6 | Jupiter Lend | Lending | $1.14B | +2.5% | +3.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $795.22M | +3.4% | +6.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $576.14M | +5.1% | +8.8% |
| 9 | Marinade Native | Staking Pool | $426.80M | +5.8% | +9.3% |
| 10 | Sentora Curator | Risk Curators | $363.96M | -1.4% | -6.1% |
| 11 | PumpSwap | Dexs | $363.50M | +5.6% | +9.7% |
| 12 | Drift Staked SOL | Liquid Staking | $315.08M | +5.8% | +9.3% |

The top five protocols hold 41.8% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.15B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.2% · Lending 17.4% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$881.69M of tokenised real-world assets and equities are locked on Solana - 5.459% of chain TVL.

- OnRe (RWA): $304.05M
- Solstice (Basis Trading): $232.46M
- Huma Finance V2 (RWA): $200.85M
- JupUSD (Basis Trading): $46.71M
- Plume Vaults (RWA): $28.12M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) - Thu, 10 Sep 2026 20:16:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT

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

### Change over 24h (vs run at 2026-09-18T15:18:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,324.84 | 4,303.74 | -19.18% |
| Average non-vote TPS | 2,803.86 | 1,776.90 | -36.63% |
| Average slot time (ms) | 267.40 | 266.80 | -0.22% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 11.00 | 13.00 | +18.18% |
| Solana TVL | 6,074,970,771.00 | 6,245,959,676.00 | +2.81% |
| SOL price | 110.21 | 111.73 | +1.38% |
| Stablecoin supply | 15,710,184,327.00 | 15,876,497,310.00 | +1.06% |
| 24h DEX volume | 2,592,123,183.29 | 3,536,797,881.43 | +36.44% |
| 24h chain fees | 14,675,830.10 | 17,457,812.00 | +18.96% |

### Change over 7d (vs run at 2026-09-12T14:30:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,491.18 | 4,303.74 | +23.27% |
| Average non-vote TPS | 1,366.96 | 1,776.90 | +29.99% |
| Average slot time (ms) | 317.40 | 266.80 | -15.94% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 13.00 | 13.00 | +0.00% |
| Solana TVL | 5,898,998,874.00 | 6,245,959,676.00 | +5.88% |
| SOL price | 101.97 | 111.73 | +9.57% |
| Stablecoin supply | 16,553,783,165.00 | 15,876,497,310.00 | -4.09% |
| 24h DEX volume | 3,183,599,712.43 | 3,536,797,881.43 | +11.09% |
| 24h chain fees | 17,875,390.26 | 17,457,812.00 | -2.34% |

### Change over 30d (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 4,303.74 | -14.50% |
| Average non-vote TPS | 3,388.67 | 1,776.90 | -47.56% |
| Average slot time (ms) | 417.00 | 266.80 | -36.02% |
| Active validators | 690.00 | 677.00 | -1.88% |
| Delinquent validators | 6.00 | 13.00 | +116.67% |
| Solana TVL | 5,300,056,423.00 | 6,245,959,676.00 | +17.85% |
| SOL price | 86.96 | 111.73 | +28.48% |
| Stablecoin supply | 16,325,927,693.00 | 15,876,497,310.00 | -2.75% |
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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 23.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
