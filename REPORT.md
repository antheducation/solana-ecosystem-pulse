# Solana Ecosystem Pulse

**Generated:** 2026-09-20T14:59:09Z · **Schema:** `1.0.0` · **Collection time:** 17.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $108.22 | -3.18% |
| Market cap | $63.57B | rank #7 |
| Total value locked | $6.12B | -2.96% |
| Stablecoin supply | $15.80B | -0.43% |
| DEX volume (24h) | $2.88B | -18.70% |
| Chain fees / REV (24h) | $15.28M | -12.50% |
| Non-vote TPS (1h avg) | 1,628 | peak 4,531 total |
| Active validators | 677 | 13 delinquent |
| Epoch 1038 | 80.93% complete | 82,401 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 88 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.50 sits 21.3 sigma below the median of the last 88 runs (317.00, -15.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,628.3 average over the last 60 minutes; 1,708.4 in the latest sample.
- **Total TPS:** 4,161.3 average, 4,531.0 peak. Consensus votes account for 60.9% of all transactions.
- **Slot time:** 266.5 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 426,806,321 at absolute slot 448,765,599.
- **Epoch 1038:** slot 349,599 of 432,000 (80.93% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.640% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 257 ms |
| `solana-rpc.publicnode.com` | yes | 227 ms |
| `api.mainnet.solana.com` | yes | 262 ms |

## Validators & stake

- **677 active** validators, **13 delinquent** (1.88% by count, 0.007% by stake).
- **Total stake:** 440,227,371 SOL ($47.64B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.80% of active stake.
- **Commission:** median 5.0%, mean 12.54%; 239 validators at 0% and 63 at 100%.

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

- **SOL:** $108.22 (-3.18% 24h, +8.14% 7d, +18.90% 30d). Market cap $63.57B, 24h volume $2.82B (4.43% of cap). Price source: `coingecko`.
- **TVL:** $6.12B across 332 protocols - rank #2 of 467 chains, 6.62% of all tracked chain TVL. +3.59% over 7d, -53.8% from its ATH.
- **Stablecoins:** $15.80B circulating on Solana (-4.35% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.88B in 24h, $18.83B over 7d across 124 venues. Volume/TVL turnover 0.470x per day.
- **REV (chain fees):** $15.28M in 24h, $419.87M over 30d. Retained chain revenue $5.47M (35.8% of fees). Annualised fees are 8.77% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,366,743 SOL circulating of 634,375,422 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.72B | -3.2% | +10.6% |
| 2 | Kamino Lend | Lending | $1.37B | -1.7% | +1.1% |
| 3 | Raydium AMM | Dexs | $1.22B | -3.0% | +7.2% |
| 4 | Jupiter Lend | Lending | $1.13B | -1.5% | +2.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.12B | -3.1% | +6.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.12B | -3.0% | +7.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $779.46M | -2.0% | +3.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $559.37M | -2.9% | +6.3% |
| 9 | Marinade Native | Staking Pool | $413.59M | -3.1% | +6.6% |
| 10 | Sentora Curator | Risk Curators | $364.36M | +0.1% | -6.5% |
| 11 | PumpSwap | Dexs | $352.63M | -3.0% | +5.7% |
| 12 | Drift Staked SOL | Liquid Staking | $305.35M | -3.1% | +6.6% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.78B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.5% · Dexs 15.6% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.7%

### Tokenised assets

$885.34M of tokenised real-world assets and equities are locked on Solana - 5.610% of chain TVL.

- OnRe (RWA): $304.14M
- Solstice (Basis Trading): $232.41M
- Huma Finance V2 (RWA): $202.27M
- JupUSD (Basis Trading): $46.71M
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

### Change over 24h (vs run at 2026-09-19T14:55:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,303.74 | 4,161.29 | -3.31% |
| Average non-vote TPS | 1,776.90 | 1,628.34 | -8.36% |
| Average slot time (ms) | 266.80 | 266.50 | -0.11% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 13.00 | 13.00 | +0.00% |
| Solana TVL | 6,245,959,676.00 | 6,119,687,070.00 | -2.02% |
| SOL price | 111.73 | 108.22 | -3.14% |
| Stablecoin supply | 15,876,497,310.00 | 15,803,956,899.00 | -0.46% |
| 24h DEX volume | 3,536,797,881.43 | 2,875,414,862.20 | -18.70% |
| 24h chain fees | 17,457,812.00 | 15,275,214.85 | -12.50% |

### Change over 7d (vs run at 2026-09-13T15:10:52Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,924.00 | 4,161.29 | +6.05% |
| Average non-vote TPS | 1,796.97 | 1,628.34 | -9.38% |
| Average slot time (ms) | 316.40 | 266.50 | -15.77% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 5,826,154,858.00 | 6,119,687,070.00 | +5.04% |
| SOL price | 100.43 | 108.22 | +7.76% |
| Stablecoin supply | 16,525,122,331.00 | 15,803,956,899.00 | -4.36% |
| 24h DEX volume | 1,691,135,695.08 | 2,875,414,862.20 | +70.03% |
| 24h chain fees | 13,515,656.40 | 15,275,214.85 | +13.02% |

### Change over 30d (vs run at 2026-08-21T18:19:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,537.20 | 4,161.29 | -8.29% |
| Average non-vote TPS | 2,672.27 | 1,628.34 | -39.07% |
| Average slot time (ms) | 365.30 | 266.50 | -27.05% |
| Active validators | 685.00 | 677.00 | -1.17% |
| Delinquent validators | 9.00 | 13.00 | +44.44% |
| Solana TVL | 5,439,131,617.00 | 6,119,687,070.00 | +12.51% |
| SOL price | 91.85 | 108.22 | +17.82% |
| Stablecoin supply | 16,516,726,394.00 | 15,803,956,899.00 | -4.32% |
| 24h DEX volume | 2,770,509,439.33 | 2,875,414,862.20 | +3.79% |
| 24h chain fees | 11,078,485.08 | 15,275,214.85 | +37.88% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
