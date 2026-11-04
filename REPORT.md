# Solana Ecosystem Pulse

**Generated:** 2026-11-04T22:56:58Z · **Schema:** `1.0.0` · **Collection time:** 20.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.03 | +2.78% |
| Market cap | $56.68B | rank #7 |
| Total value locked | $5.53B | +2.00% |
| Stablecoin supply | $14.90B | -3.07% |
| DEX volume (24h) | $1.88B | +1.54% |
| Chain fees / REV (24h) | $11.46M | +2.24% |
| Non-vote TPS (1h avg) | 2,469 | peak 4,290 total |
| Active validators | 661 | 32 delinquent |
| Epoch 1077 | 49.40% complete | 218,595 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 3.1% in 24h) | Stablecoin supply changed -3.1% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,468.9 average over the last 60 minutes; 2,145.5 in the latest sample.
- **Total TPS:** 2,468.9 average, 4,290.2 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 443,497,794 at absolute slot 465,477,405.
- **Epoch 1077:** slot 213,405 of 432,000 (49.40% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.571% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 105 ms |
| `solana-rpc.publicnode.com` | yes | 61 ms |
| `api.mainnet.solana.com` | yes | 82 ms |

## Validators & stake

- **661 active** validators, **32 delinquent** (4.62% by count, 0.473% by stake).
- **Total stake:** 433,017,789 SOL ($41.58B); stake rate 67.98% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.87% and top 33 hold 46.76% of active stake.
- **Commission:** median 5.0%, mean 12.57%; 224 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,036,631 | 3.953% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,689 | 3.877% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,012,272 | 3.019% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,433,406 | 2.421% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,524,736 | 2.210% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,439,186 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,217,930 | 2.139% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,826,697 | 1.816% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,981,457 | 1.620% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,980,105 | 1.620% | 5% |

## Economics

- **SOL:** $96.03 (+2.78% 24h, -6.44% 7d, -20.50% 30d). Market cap $56.68B, 24h volume $3.97B (7.00% of cap). Price source: `coingecko`.
- **TVL:** $5.53B across 337 protocols - rank #3 of 420 chains, 6.51% of all tracked chain TVL. -3.26% over 7d, -57.2% from its ATH.
- **Stablecoins:** $14.90B circulating on Solana (-5.58% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.88B in 24h, $11.74B over 7d across 141 venues. Volume/TVL turnover 0.340x per day.
- **REV (chain fees):** $11.46M in 24h, $372.08M over 30d. Retained chain revenue $4.30M (37.5% of fees). Annualised fees are 7.38% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,262,174 SOL circulating of 637,005,579 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.67B | +1.5% | -6.5% |
| 2 | Kamino Lend | Lending | $1.24B | +1.1% | -2.0% |
| 3 | Raydium AMM | Dexs | $1.07B | +1.4% | -6.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.03B | +1.1% | -5.3% |
| 5 | Jupiter Lend | Lending | $1.03B | +0.7% | +3.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $980.06M | +1.4% | -6.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $689.87M | +1.5% | -3.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $479.60M | +1.6% | -9.5% |
| 9 | Sentora Curator | Risk Curators | $373.07M | -0.2% | -2.8% |
| 10 | Marinade Native | Staking Pool | $340.83M | +1.2% | -6.1% |
| 11 | PumpSwap | Dexs | $327.47M | +1.7% | -5.2% |
| 12 | OnRe | RWA | $307.55M | +0.0% | +2.1% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 337 protocols the total is $14.63B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.2% · Dexs 15.2% · Derivatives 5.2% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$830.44M of tokenised real-world assets and equities are locked on Solana - 5.677% of chain TVL.

- OnRe (RWA): $307.55M
- Huma (RWA): $215.80M
- Solstice (Basis Trading): $201.43M
- JupUSD (Basis Trading): $39.48M
- Plume Vaults (RWA): $35.97M

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

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-04
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-04
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-04
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-11-04
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
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

### Change over 24h (vs run at 2026-11-03T22:38:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,437.77 | 2,468.89 | +1.28% |
| Average non-vote TPS | 2,437.77 | 2,468.89 | +1.28% |
| Average slot time (ms) | 215.00 | 215.10 | +0.05% |
| Active validators | 666.00 | 661.00 | -0.75% |
| Delinquent validators | 27.00 | 32.00 | +18.52% |
| Solana TVL | 5,464,894,047.00 | 5,531,107,333.00 | +1.21% |
| SOL price | 93.28 | 96.03 | +2.95% |
| Stablecoin supply | 15,373,798,720.00 | 14,903,512,986.00 | -3.06% |
| 24h DEX volume | 1,852,604,853.50 | 1,881,110,224.90 | +1.54% |
| 24h chain fees | 11,209,317.50 | 11,462,001.17 | +2.25% |

### Change over 7d (vs run at 2026-10-28T21:57:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,155.70 | 2,468.89 | +14.53% |
| Average non-vote TPS | 2,155.70 | 2,468.89 | +14.53% |
| Average slot time (ms) | 213.60 | 215.10 | +0.70% |
| Active validators | 661.00 | 661.00 | +0.00% |
| Delinquent validators | 30.00 | 32.00 | +6.67% |
| Solana TVL | 5,748,939,504.00 | 5,531,107,333.00 | -3.79% |
| SOL price | 102.77 | 96.03 | -6.56% |
| Stablecoin supply | 15,784,667,411.00 | 14,903,512,986.00 | -5.58% |
| 24h DEX volume | 1,582,952,703.63 | 1,881,110,224.90 | +18.84% |
| 24h chain fees | 11,229,097.00 | 11,462,001.17 | +2.07% |

### Change over 30d (vs run at 2026-10-05T23:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,796.58 | 2,468.89 | -48.53% |
| Average non-vote TPS | 2,304.82 | 2,468.89 | +7.12% |
| Average slot time (ms) | 268.60 | 215.10 | -19.92% |
| Active validators | 672.00 | 661.00 | -1.64% |
| Delinquent validators | 13.00 | 32.00 | +146.15% |
| Solana TVL | 6,781,683,220.00 | 5,531,107,333.00 | -18.44% |
| SOL price | 120.74 | 96.03 | -20.47% |
| Stablecoin supply | 16,885,339,627.00 | 14,903,512,986.00 | -11.74% |
| 24h DEX volume | 1,708,158,585.63 | 1,881,110,224.90 | +10.13% |
| 24h chain fees | 16,123,937.37 | 11,462,001.17 | -28.91% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
