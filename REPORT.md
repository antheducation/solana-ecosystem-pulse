# Solana Ecosystem Pulse

**Generated:** 2026-09-19T09:50:08Z · **Schema:** `1.0.0` · **Collection time:** 24.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $111.89 | +5.42% |
| Market cap | $65.70B | rank #7 |
| Total value locked | $6.26B | +6.13% |
| Stablecoin supply | $15.88B | +1.03% |
| DEX volume (24h) | $3.26B | +25.68% |
| Chain fees / REV (24h) | $17.92M | +22.14% |
| Non-vote TPS (1h avg) | 1,405 | peak 4,205 total |
| Active validators | 677 | 11 delinquent |
| Epoch 1037 | 89.79% complete | 44,093 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 87 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 265.90 sits 23.0 sigma below the median of the last 87 runs (317.10, -16.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 6.1% in 24h) | Solana TVL changed +6.1% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,258,605,935.00 sits 3.4 sigma above the median of the last 87 runs (5,851,427,899.00, +7.0%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,404.8 average over the last 60 minutes; 1,659.2 in the latest sample.
- **Total TPS:** 3,941.0 average, 4,204.8 peak. Consensus votes account for 64.4% of all transactions.
- **Slot time:** 265.9 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 426,412,753 at absolute slot 448,371,907.
- **Epoch 1037:** slot 387,907 of 432,000 (89.79% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.642% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 567 ms |
| `solana-rpc.publicnode.com` | yes | 28 ms |
| `api.mainnet.solana.com` | yes | 803 ms |

## Validators & stake

- **677 active** validators, **11 delinquent** (1.60% by count, 0.036% by stake).
- **Total stake:** 439,612,408 SOL ($49.19B); stake rate 69.31% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.77% of active stake.
- **Commission:** median 5.0%, mean 12.53%; 240 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,815,472 | 4.054% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,816,148 | 3.599% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,510,308 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,398,202 | 2.594% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,784,908 | 2.227% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,526 | 2.106% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,077,527 | 2.066% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,397,869 | 1.683% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,085,578 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,940 | 1.492% | 0% |

## Economics

- **SOL:** $111.89 (+5.42% 24h, +9.91% 7d, +27.91% 30d). Market cap $65.70B, 24h volume $5.56B (8.46% of cap). Price source: `coingecko`.
- **TVL:** $6.26B across 333 protocols - rank #2 of 468 chains, 6.71% of all tracked chain TVL. +6.08% over 7d, -52.7% from its ATH.
- **Stablecoins:** $15.88B circulating on Solana (-4.37% 7d) - $2.54 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.26B in 24h, $16.04B over 7d across 124 venues. Volume/TVL turnover 0.521x per day.
- **REV (chain fees):** $17.92M in 24h, $414.87M over 30d. Retained chain revenue $6.64M (37.1% of fees). Annualised fees are 9.96% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,296,318 SOL circulating of 634,297,568 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +5.8% | +14.0% |
| 2 | Kamino Lend | Lending | $1.39B | +2.7% | +3.6% |
| 3 | Raydium AMM | Dexs | $1.26B | +5.2% | +10.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.16B | +5.8% | +9.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.16B | +6.0% | +10.3% |
| 6 | Jupiter Lend | Lending | $1.15B | +2.8% | +4.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $797.01M | +3.6% | +6.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $579.96M | +5.7% | +9.5% |
| 9 | Marinade Native | Staking Pool | $426.79M | +5.8% | +9.3% |
| 10 | PumpSwap | Dexs | $367.35M | +7.3% | +10.8% |
| 11 | Sentora Curator | Risk Curators | $364.20M | -1.5% | -6.0% |
| 12 | Drift Staked SOL | Liquid Staking | $316.23M | +5.9% | +9.7% |

The top five protocols hold 41.8% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.20B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.3% · Lending 17.4% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$881.77M of tokenised real-world assets and equities are locked on Solana - 5.445% of chain TVL.

- OnRe (RWA): $304.05M
- Solstice (Basis Trading): $232.44M
- Huma Finance V2 (RWA): $200.86M
- JupUSD (Basis Trading): $46.78M
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

### Change over 24h (vs run at 2026-09-18T10:08:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,071.90 | 3,941.04 | -3.21% |
| Average non-vote TPS | 1,539.85 | 1,404.77 | -8.77% |
| Average slot time (ms) | 265.90 | 265.90 | +0.00% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 6,020,571,779.00 | 6,258,605,935.00 | +3.95% |
| SOL price | 106.42 | 111.89 | +5.14% |
| Stablecoin supply | 15,709,402,844.00 | 15,875,833,367.00 | +1.06% |
| 24h DEX volume | 2,553,904,323.29 | 3,257,762,192.43 | +27.56% |
| 24h chain fees | 13,898,915.10 | 17,919,652.00 | +28.93% |

### Change over 7d (vs run at 2026-09-12T09:41:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,219.41 | 3,941.04 | +22.41% |
| Average non-vote TPS | 1,084.86 | 1,404.77 | +29.49% |
| Average slot time (ms) | 316.00 | 265.90 | -15.85% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 14.00 | 11.00 | -21.43% |
| Solana TVL | 5,892,056,482.00 | 6,258,605,935.00 | +6.22% |
| SOL price | 102.10 | 111.89 | +9.59% |
| Stablecoin supply | 16,554,130,892.00 | 15,875,833,367.00 | -4.10% |
| 24h DEX volume | 3,247,771,790.43 | 3,257,762,192.43 | +0.31% |
| 24h chain fees | 17,542,312.26 | 17,919,652.00 | +2.15% |

### Change over 30d (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 3,941.04 | -21.71% |
| Average non-vote TPS | 3,388.67 | 1,404.77 | -58.55% |
| Average slot time (ms) | 417.00 | 265.90 | -36.24% |
| Active validators | 690.00 | 677.00 | -1.88% |
| Delinquent validators | 6.00 | 11.00 | +83.33% |
| Solana TVL | 5,300,056,423.00 | 6,258,605,935.00 | +18.09% |
| SOL price | 86.96 | 111.89 | +28.67% |
| Stablecoin supply | 16,325,927,693.00 | 15,875,833,367.00 | -2.76% |
| 24h DEX volume | 3,009,837,694.95 | 3,257,762,192.43 | +8.24% |
| 24h chain fees | 13,676,729.38 | 17,919,652.00 | +31.02% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 24.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
