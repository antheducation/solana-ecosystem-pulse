# Solana Ecosystem Pulse

**Generated:** 2026-09-20T01:58:19Z · **Schema:** `1.0.0` · **Collection time:** 10.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.06 | -3.05% |
| Market cap | $64.66B | rank #7 |
| Total value locked | $6.17B | -0.76% |
| Stablecoin supply | $15.80B | -0.44% |
| DEX volume (24h) | $3.23B | -8.57% |
| Chain fees / REV (24h) | $16.25M | -6.94% |
| Non-vote TPS (1h avg) | 1,602 | peak 4,519 total |
| Active validators | 678 | 12 delinquent |
| Epoch 1038 | 40.19% complete | 258,397 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 87 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 266.40 sits 22.8 sigma below the median of the last 87 runs (317.10, -16.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,601.8 average over the last 60 minutes; 1,272.8 in the latest sample.
- **Total TPS:** 4,136.8 average, 4,519.4 peak. Consensus votes account for 61.3% of all transactions.
- **Slot time:** 266.4 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 426,630,343 at absolute slot 448,589,603.
- **Epoch 1038:** slot 173,603 of 432,000 (40.19% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.640% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 173 ms |
| `solana-rpc.publicnode.com` | yes | 39 ms |
| `api.mainnet.solana.com` | yes | 53 ms |

## Validators & stake

- **678 active** validators, **12 delinquent** (1.74% by count, 0.035% by stake).
- **Total stake:** 440,227,371 SOL ($48.45B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.22%; 243 validators at 0% and 61 at 100%.

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

- **SOL:** $110.06 (-3.05% 24h, +8.20% 7d, +24.80% 30d). Market cap $64.66B, 24h volume $2.84B (4.40% of cap). Price source: `coingecko`.
- **TVL:** $6.17B across 333 protocols - rank #2 of 467 chains, 6.61% of all tracked chain TVL. +4.50% over 7d, -53.4% from its ATH.
- **Stablecoins:** $15.80B circulating on Solana (-4.36% 7d) - $2.56 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.23B in 24h, $17.53B over 7d across 124 venues. Volume/TVL turnover 0.524x per day.
- **REV (chain fees):** $16.25M in 24h, $412.29M over 30d. Retained chain revenue $5.75M (35.4% of fees). Annualised fees are 9.17% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,367,231 SOL circulating of 634,375,909 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.77B | -1.9% | +13.5% |
| 2 | Kamino Lend | Lending | $1.36B | -2.8% | +0.7% |
| 3 | Raydium AMM | Dexs | $1.25B | -1.2% | +9.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.15B | -1.6% | +9.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.15B | -2.3% | +9.8% |
| 6 | Jupiter Lend | Lending | $1.12B | -3.1% | +1.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $792.19M | -1.2% | +5.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $573.33M | -2.3% | +9.0% |
| 9 | Marinade Native | Staking Pool | $424.11M | -1.8% | +9.4% |
| 10 | Sentora Curator | Risk Curators | $364.67M | -0.1% | -6.4% |
| 11 | PumpSwap | Dexs | $359.12M | -2.9% | +7.6% |
| 12 | Drift Staked SOL | Liquid Staking | $313.01M | -2.2% | +9.3% |

The top five protocols hold 41.7% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.3% · Lending 17.2% · Dexs 15.7% · Derivatives 5.4% · Staking Pool 4.1% · Risk Curators 3.6%

### Tokenised assets

$885.00M of tokenised real-world assets and equities are locked on Solana - 5.522% of chain TVL.

- OnRe (RWA): $304.05M
- Solstice (Basis Trading): $232.45M
- Huma Finance V2 (RWA): $201.85M
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

### Change over 24h (vs run at 2026-09-19T01:55:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,416.04 | 4,136.77 | -6.32% |
| Average non-vote TPS | 1,894.43 | 1,601.78 | -15.45% |
| Average slot time (ms) | 267.10 | 266.40 | -0.26% |
| Active validators | 677.00 | 678.00 | +0.15% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 6,396,701,682.00 | 6,172,970,932.00 | -3.50% |
| SOL price | 113.63 | 110.06 | -3.14% |
| Stablecoin supply | 15,876,163,466.00 | 15,802,339,067.00 | -0.47% |
| 24h DEX volume | 3,097,318,491.84 | 3,233,773,154.20 | +4.41% |
| 24h chain fees | 15,267,932.07 | 16,246,928.52 | +6.41% |

### Change over 7d (vs run at 2026-09-13T01:41:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,596.70 | 4,136.77 | +15.02% |
| Average non-vote TPS | 1,468.09 | 1,601.78 | +9.11% |
| Average slot time (ms) | 316.10 | 266.40 | -15.72% |
| Active validators | 677.00 | 678.00 | +0.15% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,902,475,260.00 | 6,172,970,932.00 | +4.58% |
| SOL price | 101.91 | 110.06 | +8.00% |
| Stablecoin supply | 16,527,129,251.00 | 15,802,339,067.00 | -4.39% |
| 24h DEX volume | 2,474,258,713.08 | 3,233,773,154.20 | +30.70% |
| 24h chain fees | 15,265,567.51 | 16,246,928.52 | +6.43% |

### Change over 30d (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 4,136.77 | -17.82% |
| Average non-vote TPS | 3,388.67 | 1,601.78 | -52.73% |
| Average slot time (ms) | 417.00 | 266.40 | -36.12% |
| Active validators | 690.00 | 678.00 | -1.74% |
| Delinquent validators | 6.00 | 12.00 | +100.00% |
| Solana TVL | 5,300,056,423.00 | 6,172,970,932.00 | +16.47% |
| SOL price | 86.96 | 110.06 | +26.56% |
| Stablecoin supply | 16,325,927,693.00 | 15,802,339,067.00 | -3.21% |
| 24h DEX volume | 3,009,837,694.95 | 3,233,773,154.20 | +7.44% |
| 24h chain fees | 13,676,729.38 | 16,246,928.52 | +18.79% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 10.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
