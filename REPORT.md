# Solana Ecosystem Pulse

**Generated:** 2026-11-05T22:57:47Z · **Schema:** `1.0.0` · **Collection time:** 20.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $89.52 | -6.85% |
| Market cap | $52.84B | rank #7 |
| Total value locked | $5.29B | -2.16% |
| Stablecoin supply | $15.18B | +1.87% |
| DEX volume (24h) | $2.39B | +26.82% |
| Chain fees / REV (24h) | $11.23M | -1.61% |
| Non-vote TPS (1h avg) | 1,837 | peak 3,385 total |
| Active validators | 662 | 32 delinquent |
| Epoch 1078 | 43.06% complete | 245,978 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,837.5 average over the last 60 minutes; 1,513.4 in the latest sample.
- **Total TPS:** 1,837.5 average, 3,385.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.9 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 443,901,843 at absolute slot 465,882,022.
- **Epoch 1078:** slot 186,022 of 432,000 (43.06% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.570% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 217 ms |
| `solana-rpc.publicnode.com` | yes | 121 ms |
| `api.mainnet.solana.com` | yes | 125 ms |

## Validators & stake

- **662 active** validators, **32 delinquent** (4.61% by count, 0.158% by stake).
- **Total stake:** 430,872,482 SOL ($38.57B); stake rate 67.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.78% and top 33 hold 46.50% of active stake.
- **Commission:** median 5.0%, mean 12.69%; 225 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,063,613 | 3.967% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,736,546 | 3.890% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,020,024 | 3.027% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,434,901 | 2.426% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,530,733 | 2.215% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,459,109 | 2.199% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,692 | 2.144% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,860,096 | 1.827% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,477 | 1.625% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,293,076 | 1.463% | 0% |

## Economics

- **SOL:** $89.52 (-6.85% 24h, -8.12% 7d, -26.03% 30d). Market cap $52.84B, 24h volume $4.47B (8.46% of cap). Price source: `coingecko`.
- **TVL:** $5.29B across 340 protocols - rank #3 of 421 chains, 6.53% of all tracked chain TVL. -7.52% over 7d, -59.1% from its ATH.
- **Stablecoins:** $15.18B circulating on Solana (-3.10% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.39B in 24h, $12.39B over 7d across 141 venues. Volume/TVL turnover 0.451x per day.
- **REV (chain fees):** $11.23M in 24h, $364.15M over 30d. Retained chain revenue $3.89M (34.7% of fees). Annualised fees are 7.76% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,287,426 SOL circulating of 637,066,682 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | -5.5% | -12.1% |
| 2 | Kamino Lend | Lending | $1.20B | -3.6% | -5.8% |
| 3 | Raydium AMM | Dexs | $1.00B | -6.3% | -12.7% |
| 4 | Jupiter Lend | Lending | $987.37M | -3.9% | -2.3% |
| 5 | Binance Staked SOL | Liquid Staking | $980.00M | -5.0% | -11.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $927.94M | -5.3% | -12.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $662.82M | -3.9% | -7.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $453.77M | -5.5% | -14.8% |
| 9 | Sentora Curator | Risk Curators | $373.01M | -0.0% | -2.8% |
| 10 | Marinade Native | Staking Pool | $322.42M | -5.5% | -12.1% |
| 11 | OnRe | RWA | $308.44M | +0.3% | +0.9% |
| 12 | PumpSwap | Dexs | $306.53M | -6.4% | -8.5% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $14.01B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.7% · Lending 17.3% · Dexs 15.1% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.9%

### Tokenised assets

$831.80M of tokenised real-world assets and equities are locked on Solana - 5.937% of chain TVL.

- OnRe (RWA): $308.44M
- Huma (RWA): $212.88M
- Solstice (Basis Trading): $201.01M
- JupUSD (Basis Trading): $42.52M
- Plume Vaults (RWA): $36.89M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-05
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-05
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-05
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-11-05
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-05
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-05
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-11-04

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

### Change over 24h (vs run at 2026-11-04T22:56:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,468.89 | 1,837.49 | -25.57% |
| Average non-vote TPS | 2,468.89 | 1,837.49 | -25.57% |
| Average slot time (ms) | 215.10 | 213.90 | -0.56% |
| Active validators | 661.00 | 662.00 | +0.15% |
| Delinquent validators | 32.00 | 32.00 | +0.00% |
| Solana TVL | 5,531,107,333.00 | 5,293,425,753.00 | -4.30% |
| SOL price | 96.03 | 89.52 | -6.78% |
| Stablecoin supply | 14,903,512,986.00 | 15,182,475,286.00 | +1.87% |
| 24h DEX volume | 1,881,110,224.90 | 2,385,538,829.94 | +26.82% |
| 24h chain fees | 11,462,001.17 | 11,227,806.64 | -2.04% |

### Change over 7d (vs run at 2026-10-29T22:06:52Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,732.84 | 1,837.49 | -32.76% |
| Average non-vote TPS | 2,732.84 | 1,837.49 | -32.76% |
| Average slot time (ms) | 214.30 | 213.90 | -0.19% |
| Active validators | 666.00 | 662.00 | -0.60% |
| Delinquent validators | 23.00 | 32.00 | +39.13% |
| Solana TVL | 5,655,014,849.00 | 5,293,425,753.00 | -6.39% |
| SOL price | 97.17 | 89.52 | -7.87% |
| Stablecoin supply | 15,693,912,574.00 | 15,182,475,286.00 | -3.26% |
| 24h DEX volume | 1,733,397,982.06 | 2,385,538,829.94 | +37.62% |
| 24h chain fees | 10,347,418.88 | 11,227,806.64 | +8.51% |

### Change over 30d (vs run at 2026-10-06T21:56:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,237.18 | 1,837.49 | -64.91% |
| Average non-vote TPS | 2,776.85 | 1,837.49 | -33.83% |
| Average slot time (ms) | 270.70 | 213.90 | -20.98% |
| Active validators | 670.00 | 662.00 | -1.19% |
| Delinquent validators | 15.00 | 32.00 | +113.33% |
| Solana TVL | 6,619,880,617.00 | 5,293,425,753.00 | -20.04% |
| SOL price | 120.95 | 89.52 | -25.99% |
| Stablecoin supply | 17,052,133,908.00 | 15,182,475,286.00 | -10.96% |
| 24h DEX volume | 2,057,146,062.50 | 2,385,538,829.94 | +15.96% |
| 24h chain fees | 16,090,422.62 | 11,227,806.64 | -30.22% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
