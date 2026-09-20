# Solana Ecosystem Pulse

**Generated:** 2026-09-20T10:11:40Z · **Schema:** `1.0.0` · **Collection time:** 15.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $108.07 | -3.33% |
| Market cap | $63.48B | rank #7 |
| Total value locked | $6.12B | -2.88% |
| Stablecoin supply | $15.80B | -0.44% |
| DEX volume (24h) | $3.23B | -8.58% |
| Chain fees / REV (24h) | $15.22M | -12.81% |
| Non-vote TPS (1h avg) | 1,239 | peak 4,218 total |
| Active validators | 678 | 12 delinquent |
| Epoch 1038 | 65.92% complete | 147,216 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 88 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.60 sits 21.9 sigma below the median of the last 88 runs (317.00, -15.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,239.4 average over the last 60 minutes; 1,335.4 in the latest sample.
- **Total TPS:** 3,772.5 average, 4,217.5 peak. Consensus votes account for 67.1% of all transactions.
- **Slot time:** 266.6 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 426,741,507 at absolute slot 448,700,784.
- **Epoch 1038:** slot 284,784 of 432,000 (65.92% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.640% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 168 ms |
| `solana-rpc.publicnode.com` | yes | 143 ms |
| `api.mainnet.solana.com` | yes | 127 ms |

## Validators & stake

- **678 active** validators, **12 delinquent** (1.74% by count, 0.007% by stake).
- **Total stake:** 440,227,371 SOL ($47.58B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.80% of active stake.
- **Commission:** median 5.0%, mean 12.52%; 240 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,849,776 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,819,247 | 3.594% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,500,805 | 2.840% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,362,749 | 2.581% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,786,807 | 2.223% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,843 | 2.102% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,116,740 | 2.071% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,434,776 | 1.689% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,086,871 | 1.610% | 5% |
| 10 | `HZKopZYvv8v6un2H6KUNVQCnK5zM9emKKezvqhTBSpEc` | 6,627,951 | 1.506% | 100% |

## Economics

- **SOL:** $108.07 (-3.33% 24h, +8.24% 7d, +17.93% 30d). Market cap $63.48B, 24h volume $2.93B (4.62% of cap). Price source: `coingecko`.
- **TVL:** $6.12B across 332 protocols - rank #2 of 467 chains, 6.63% of all tracked chain TVL. +3.68% over 7d, -53.7% from its ATH.
- **Stablecoins:** $15.80B circulating on Solana (-4.36% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.23B in 24h, $17.53B over 7d across 124 venues. Volume/TVL turnover 0.528x per day.
- **REV (chain fees):** $15.22M in 24h, $419.10M over 30d. Retained chain revenue $5.52M (36.3% of fees). Annualised fees are 8.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,366,920 SOL circulating of 634,375,600 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.73B | -3.2% | +11.1% |
| 2 | Kamino Lend | Lending | $1.37B | -2.0% | +1.1% |
| 3 | Raydium AMM | Dexs | $1.23B | -2.1% | +7.8% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.13B | -3.0% | +7.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.12B | -3.6% | +6.4% |
| 6 | Jupiter Lend | Lending | $1.12B | -2.2% | +1.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $777.59M | -2.4% | +3.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $561.17M | -3.6% | +6.7% |
| 9 | Marinade Native | Staking Pool | $414.96M | -3.1% | +7.0% |
| 10 | Sentora Curator | Risk Curators | $364.48M | +0.1% | -6.4% |
| 11 | PumpSwap | Dexs | $353.62M | -3.0% | +6.0% |
| 12 | Drift Staked SOL | Liquid Staking | $304.91M | -3.6% | +6.5% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.80B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.0% · Lending 17.5% · Dexs 15.7% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.7%

### Tokenised assets

$885.40M of tokenised real-world assets and equities are locked on Solana - 5.605% of chain TVL.

- OnRe (RWA): $304.13M
- Solstice (Basis Trading): $232.43M
- Huma Finance V2 (RWA): $202.32M
- JupUSD (Basis Trading): $46.70M
- Plume Vaults (RWA): $28.13M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT

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

### Change over 24h (vs run at 2026-09-19T09:50:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,941.04 | 3,772.47 | -4.28% |
| Average non-vote TPS | 1,404.77 | 1,239.40 | -11.77% |
| Average slot time (ms) | 265.90 | 266.60 | +0.26% |
| Active validators | 677.00 | 678.00 | +0.15% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 6,258,605,935.00 | 6,124,115,707.00 | -2.15% |
| SOL price | 111.89 | 108.07 | -3.41% |
| Stablecoin supply | 15,875,833,367.00 | 15,802,349,869.00 | -0.46% |
| 24h DEX volume | 3,257,762,192.43 | 3,233,490,127.20 | -0.75% |
| 24h chain fees | 17,919,652.00 | 15,220,774.85 | -15.06% |

### Change over 7d (vs run at 2026-09-13T10:42:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,492.32 | 3,772.47 | +8.02% |
| Average non-vote TPS | 1,356.21 | 1,239.40 | -8.61% |
| Average slot time (ms) | 315.60 | 266.60 | -15.53% |
| Active validators | 677.00 | 678.00 | +0.15% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,849,871,625.00 | 6,124,115,707.00 | +4.69% |
| SOL price | 99.67 | 108.07 | +8.43% |
| Stablecoin supply | 16,524,914,648.00 | 15,802,349,869.00 | -4.37% |
| 24h DEX volume | 2,473,369,329.08 | 3,233,490,127.20 | +30.73% |
| 24h chain fees | 13,897,813.40 | 15,220,774.85 | +9.52% |

### Change over 30d (vs run at 2026-08-21T18:19:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,537.20 | 3,772.47 | -16.85% |
| Average non-vote TPS | 2,672.27 | 1,239.40 | -53.62% |
| Average slot time (ms) | 365.30 | 266.60 | -27.02% |
| Active validators | 685.00 | 678.00 | -1.02% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 5,439,131,617.00 | 6,124,115,707.00 | +12.59% |
| SOL price | 91.85 | 108.07 | +17.66% |
| Stablecoin supply | 16,516,726,394.00 | 15,802,349,869.00 | -4.33% |
| 24h DEX volume | 2,770,509,439.33 | 3,233,490,127.20 | +16.71% |
| 24h chain fees | 11,078,485.08 | 15,220,774.85 | +37.39% |

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
