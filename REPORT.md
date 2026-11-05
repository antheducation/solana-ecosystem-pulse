# Solana Ecosystem Pulse

**Generated:** 2026-11-05T03:56:04Z · **Schema:** `1.0.0` · **Collection time:** 19.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.39 | +6.18% |
| Market cap | $56.89B | rank #7 |
| Total value locked | $5.56B | +2.72% |
| Stablecoin supply | $15.18B | +1.88% |
| DEX volume (24h) | $2.22B | +18.14% |
| Chain fees / REV (24h) | $10.96M | -4.38% |
| Non-vote TPS (1h avg) | 1,543 | peak 2,121 total |
| Active validators | 662 | 31 delinquent |
| Epoch 1077 | 68.83% complete | 134,669 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,542.9 average over the last 60 minutes; 1,201.6 in the latest sample.
- **Total TPS:** 1,542.9 average, 2,121.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.3 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 443,581,580 at absolute slot 465,561,331.
- **Epoch 1077:** slot 297,331 of 432,000 (68.83% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.571% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 472 ms |
| `solana-rpc.publicnode.com` | yes | 415 ms |
| `api.mainnet.solana.com` | yes | 401 ms |

## Validators & stake

- **662 active** validators, **31 delinquent** (4.47% by count, 0.457% by stake).
- **Total stake:** 433,017,789 SOL ($41.74B); stake rate 67.98% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.86% and top 33 hold 46.76% of active stake.
- **Commission:** median 5.0%, mean 12.71%; 224 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,036,631 | 3.952% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,689 | 3.877% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,012,272 | 3.019% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,433,406 | 2.421% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,524,736 | 2.210% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,439,186 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,217,930 | 2.139% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,826,697 | 1.816% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,981,457 | 1.620% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,980,105 | 1.619% | 5% |

## Economics

- **SOL:** $96.39 (+6.18% 24h, -3.58% 7d, -19.81% 30d). Market cap $56.89B, 24h volume $3.80B (6.69% of cap). Price source: `coingecko`.
- **TVL:** $5.56B across 337 protocols - rank #3 of 420 chains, 6.51% of all tracked chain TVL. -2.91% over 7d, -57.0% from its ATH.
- **Stablecoins:** $15.18B circulating on Solana (-3.09% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.22B in 24h, $11.20B over 7d across 141 venues. Volume/TVL turnover 0.400x per day.
- **REV (chain fees):** $10.96M in 24h, $364.23M over 30d. Retained chain revenue $3.88M (35.4% of fees). Annualised fees are 7.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,262,091 SOL circulating of 637,005,496 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.69B | +5.0% | -5.9% |
| 2 | Kamino Lend | Lending | $1.25B | +2.3% | -1.8% |
| 3 | Raydium AMM | Dexs | $1.07B | +3.9% | -6.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.05B | +6.1% | -5.3% |
| 5 | Jupiter Lend | Lending | $1.03B | +2.0% | +1.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $994.43M | +5.5% | -6.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $697.38M | +4.2% | -3.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $487.06M | +5.1% | -8.5% |
| 9 | Sentora Curator | Risk Curators | $373.04M | -0.2% | -2.8% |
| 10 | Marinade Native | Staking Pool | $346.14M | +4.9% | -5.7% |
| 11 | PumpSwap | Dexs | $328.51M | +5.4% | -1.9% |
| 12 | OnRe | RWA | $307.62M | +0.0% | +0.7% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 337 protocols the total is $14.75B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.1% · Dexs 15.2% · Derivatives 5.2% · RWA 3.8% · Risk Curators 3.7%

### Tokenised assets

$829.53M of tokenised real-world assets and equities are locked on Solana - 5.622% of chain TVL.

- OnRe (RWA): $307.62M
- Huma (RWA): $211.89M
- Solstice (Basis Trading): $201.42M
- JupUSD (Basis Trading): $42.54M
- Plume Vaults (RWA): $35.98M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-05
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-05
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-04
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-04
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-11-04
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-03

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

### Change over 24h (vs run at 2026-11-04T03:36:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,159.62 | 1,542.90 | -28.56% |
| Average non-vote TPS | 2,159.62 | 1,542.90 | -28.56% |
| Average slot time (ms) | 214.00 | 213.30 | -0.33% |
| Active validators | 666.00 | 662.00 | -0.60% |
| Delinquent validators | 27.00 | 31.00 | +14.81% |
| Solana TVL | 5,411,706,032.00 | 5,556,165,279.00 | +2.67% |
| SOL price | 91.05 | 96.39 | +5.86% |
| Stablecoin supply | 14,901,850,212.00 | 15,184,455,347.00 | +1.90% |
| 24h DEX volume | 1,873,448,962.90 | 2,222,398,076.94 | +18.63% |
| 24h chain fees | 11,428,987.75 | 10,960,459.01 | -4.10% |

### Change over 7d (vs run at 2026-10-29T03:08:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,832.75 | 1,542.90 | -15.82% |
| Average non-vote TPS | 1,832.75 | 1,542.90 | -15.82% |
| Average slot time (ms) | 214.00 | 213.30 | -0.33% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 24.00 | 31.00 | +29.17% |
| Solana TVL | 5,735,222,416.00 | 5,556,165,279.00 | -3.12% |
| SOL price | 99.93 | 96.39 | -3.54% |
| Stablecoin supply | 15,688,097,062.00 | 15,184,455,347.00 | -3.21% |
| 24h DEX volume | 1,624,511,734.06 | 2,222,398,076.94 | +36.80% |
| 24h chain fees | 10,348,131.32 | 10,960,459.01 | +5.92% |

### Change over 30d (vs run at 2026-10-05T23:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,796.58 | 1,542.90 | -67.83% |
| Average non-vote TPS | 2,304.82 | 1,542.90 | -33.06% |
| Average slot time (ms) | 268.60 | 213.30 | -20.59% |
| Active validators | 672.00 | 662.00 | -1.49% |
| Delinquent validators | 13.00 | 31.00 | +138.46% |
| Solana TVL | 6,781,683,220.00 | 5,556,165,279.00 | -18.07% |
| SOL price | 120.74 | 96.39 | -20.17% |
| Stablecoin supply | 16,885,339,627.00 | 15,184,455,347.00 | -10.07% |
| 24h DEX volume | 1,708,158,585.63 | 2,222,398,076.94 | +30.10% |
| 24h chain fees | 16,123,937.37 | 10,960,459.01 | -32.02% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 19.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
