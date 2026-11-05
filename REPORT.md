# Solana Ecosystem Pulse

**Generated:** 2026-11-05T13:37:02Z · **Schema:** `1.0.0` · **Collection time:** 21.9s · **Sources OK:** 38/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $95.28 | +2.72% |
| Market cap | $56.25B | rank #7 |
| Total value locked | $5.58B | +3.11% |
| Stablecoin supply | $15.18B | +1.87% |
| DEX volume (24h) | $2.39B | +26.82% |
| Chain fees / REV (24h) | $11.23M | -1.61% |
| Non-vote TPS (1h avg) | 1,603 | peak 1,998 total |
| Active validators | 663 | 31 delinquent |
| Epoch 1078 | 6.65% complete | 403,291 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,603.3 average over the last 60 minutes; 1,715.4 in the latest sample.
- **Total TPS:** 1,603.3 average, 1,998.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.8 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 443,744,793 at absolute slot 465,724,709.
- **Epoch 1078:** slot 28,709 of 432,000 (6.65% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.570% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 193 ms |
| `solana-rpc.publicnode.com` | yes | 122 ms |
| `api.mainnet.solana.com` | yes | 163 ms |

## Validators & stake

- **663 active** validators, **31 delinquent** (4.47% by count, 0.134% by stake).
- **Total stake:** 430,872,482 SOL ($41.05B); stake rate 67.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.78% and top 33 hold 46.49% of active stake.
- **Commission:** median 5.0%, mean 12.67%; 226 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,063,613 | 3.966% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,736,546 | 3.890% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,020,024 | 3.026% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,434,901 | 2.425% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,530,733 | 2.215% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,459,109 | 2.198% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,692 | 2.143% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,860,096 | 1.827% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,477 | 1.625% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,293,076 | 1.463% | 0% |

## Economics

- **SOL:** $95.28 (+2.72% 24h, -5.13% 7d, -20.84% 30d). Market cap $56.25B, 24h volume $4.54B (8.07% of cap). Price source: `coingecko`.
- **TVL:** $5.58B across 336 protocols - rank #3 of 420 chains, 6.58% of all tracked chain TVL. -2.54% over 7d, -56.9% from its ATH.
- **Stablecoins:** $15.18B circulating on Solana (-3.10% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.39B in 24h, $12.39B over 7d across 141 venues. Volume/TVL turnover 0.428x per day.
- **REV (chain fees):** $11.23M in 24h, $364.15M over 30d. Retained chain revenue $3.89M (34.7% of fees). Annualised fees are 7.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,317,701 SOL circulating of 637,066,919 total (92.66%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.70B | +3.9% | -5.5% |
| 2 | Kamino Lend | Lending | $1.25B | +1.6% | -1.8% |
| 3 | Raydium AMM | Dexs | $1.08B | +3.1% | -5.6% |
| 4 | Binance Staked SOL | Liquid Staking | $1.05B | +2.5% | -5.2% |
| 5 | Jupiter Lend | Lending | $1.03B | +1.1% | +1.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $998.02M | +4.3% | -6.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $697.98M | +3.1% | -3.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $487.20M | +3.8% | -8.5% |
| 9 | Sentora Curator | Risk Curators | $373.41M | -0.1% | -2.7% |
| 10 | Marinade Native | Staking Pool | $346.20M | +3.9% | -5.7% |
| 11 | PumpSwap | Dexs | $332.42M | +4.5% | -0.7% |
| 12 | OnRe | RWA | $307.65M | +0.1% | +0.7% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $14.79B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.1% · Dexs 15.2% · Derivatives 5.2% · RWA 3.8% · Risk Curators 3.7%

### Tokenised assets

$830.60M of tokenised real-world assets and equities are locked on Solana - 5.615% of chain TVL.

- OnRe (RWA): $307.65M
- Huma (RWA): $212.85M
- Solstice (Basis Trading): $201.44M
- JupUSD (Basis Trading): $42.56M
- Plume Vaults (RWA): $35.98M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

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

### Change over 24h (vs run at 2026-11-04T13:23:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,488.22 | 1,603.34 | +7.74% |
| Average non-vote TPS | 1,488.22 | 1,603.34 | +7.74% |
| Average slot time (ms) | 214.10 | 213.80 | -0.14% |
| Active validators | 662.00 | 663.00 | +0.15% |
| Delinquent validators | 31.00 | 31.00 | +0.00% |
| Solana TVL | 5,464,731,305.00 | 5,577,510,303.00 | +2.06% |
| SOL price | 92.65 | 95.28 | +2.84% |
| Stablecoin supply | 14,903,033,514.00 | 15,183,394,102.00 | +1.88% |
| 24h DEX volume | 1,881,110,224.90 | 2,385,538,829.94 | +26.82% |
| 24h chain fees | 11,334,057.17 | 11,226,354.64 | -0.95% |

### Change over 7d (vs run at 2026-10-29T11:52:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,331.86 | 1,603.34 | +20.38% |
| Average non-vote TPS | 1,331.86 | 1,603.34 | +20.38% |
| Average slot time (ms) | 214.00 | 213.80 | -0.09% |
| Active validators | 666.00 | 663.00 | -0.45% |
| Delinquent validators | 23.00 | 31.00 | +34.78% |
| Solana TVL | 5,646,734,237.00 | 5,577,510,303.00 | -1.23% |
| SOL price | 100.38 | 95.28 | -5.08% |
| Stablecoin supply | 15,688,764,724.00 | 15,183,394,102.00 | -3.22% |
| 24h DEX volume | 1,733,397,982.06 | 2,385,538,829.94 | +37.62% |
| 24h chain fees | 10,346,775.24 | 11,226,354.64 | +8.50% |

### Change over 30d (vs run at 2026-10-06T21:56:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,237.18 | 1,603.34 | -69.39% |
| Average non-vote TPS | 2,776.85 | 1,603.34 | -42.26% |
| Average slot time (ms) | 270.70 | 213.80 | -21.02% |
| Active validators | 670.00 | 663.00 | -1.04% |
| Delinquent validators | 15.00 | 31.00 | +106.67% |
| Solana TVL | 6,619,880,617.00 | 5,577,510,303.00 | -15.75% |
| SOL price | 120.95 | 95.28 | -21.22% |
| Stablecoin supply | 17,052,133,908.00 | 15,183,394,102.00 | -10.96% |
| 24h DEX volume | 2,057,146,062.50 | 2,385,538,829.94 | +15.96% |
| 24h chain fees | 16,090,422.62 | 11,226,354.64 | -30.23% |

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

This run made 41 HTTP calls (38 succeeded, 3 failed) in 21.8s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)
- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
