# Solana Ecosystem Pulse

**Generated:** 2026-11-15T03:28:23Z · **Schema:** `1.0.0` · **Collection time:** 23.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.61 | -5.17% |
| Market cap | $42.36B | rank #7 |
| Total value locked | $4.61B | -3.68% |
| Stablecoin supply | $14.22B | -0.01% |
| DEX volume (24h) | $1.61B | +3.42% |
| Chain fees / REV (24h) | $8.19M | -10.49% |
| Non-vote TPS (1h avg) | 1,658 | peak 2,620 total |
| Active validators | 662 | 37 delinquent |
| Epoch 1086 | 98.79% complete | 5,248 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,657.9 average over the last 60 minutes; 1,289.5 in the latest sample.
- **Total TPS:** 1,657.9 average, 2,619.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.4 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 447,593,784 at absolute slot 469,578,752.
- **Epoch 1086:** slot 426,752 of 432,000 (98.79% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.557% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 114 ms |
| `solana-rpc.publicnode.com` | yes | 135 ms |
| `api.mainnet.solana.com` | yes | 148 ms |

## Validators & stake

- **662 active** validators, **37 delinquent** (5.29% by count, 0.092% by stake).
- **Total stake:** 429,651,631 SOL ($30.77B); stake rate 67.39% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.74% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 221 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,955,905 | 3.950% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,374,909 | 3.815% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,611,498 | 2.938% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,140,468 | 2.362% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,736,890 | 2.268% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,439 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,199,377 | 2.143% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,914,792 | 1.844% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,990,062 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,707,745 | 1.563% | 5% |

## Economics

- **SOL:** $71.61 (-5.17% 24h, -19.54% 7d, -31.93% 30d). Market cap $42.36B, 24h volume $4.94B (11.67% of cap). Price source: `coingecko`.
- **TVL:** $4.61B across 343 protocols - rank #3 of 423 chains, 6.59% of all tracked chain TVL. -11.52% over 7d, -61.2% from its ATH.
- **Stablecoins:** $14.22B circulating on Solana (-2.61% 7d) - $3.08 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.61B in 24h, $9.39B over 7d across 141 venues. Volume/TVL turnover 0.350x per day.
- **REV (chain fees):** $8.19M in 24h, $317.62M over 30d. Retained chain revenue $2.74M (33.4% of fees). Annualised fees are 7.05% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,573,556 SOL circulating of 637,554,518 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.33B | -6.0% | -16.1% |
| 2 | Kamino Lend | Lending | $1.11B | -3.5% | -6.0% |
| 3 | Jupiter Lend | Lending | $892.81M | -5.4% | -3.6% |
| 4 | Raydium AMM | Dexs | $809.35M | -7.9% | -19.3% |
| 5 | Binance Staked SOL | Liquid Staking | $722.78M | -8.5% | -25.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $692.94M | -9.6% | -24.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $569.53M | -3.5% | -13.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $366.59M | -5.0% | -19.5% |
| 9 | Sentora Curator | Risk Curators | $357.43M | +0.0% | -4.4% |
| 10 | OnRe | RWA | $304.31M | -1.5% | -1.4% |
| 11 | Forward Industries SOL | Liquid Staking | $285.71M | -6.3% | +1.2% |
| 12 | CCIP | Bridge | $278.49M | -3.0% | +5.0% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 343 protocols the total is $11.86B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.2% · Lending 18.6% · Dexs 14.8% · Derivatives 5.3% · RWA 5.0% · Risk Curators 4.1%

### Tokenised assets

$847.60M of tokenised real-world assets and equities are locked on Solana - 7.145% of chain TVL.

- OnRe (RWA): $304.31M
- Huma (RWA): $238.78M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $40.37M
- Plume Vaults (RWA): $37.00M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-12
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07

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

### Change over 24h (vs run at 2026-11-14T03:48:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,775.45 | 1,657.93 | -6.62% |
| Average non-vote TPS | 1,775.45 | 1,657.93 | -6.62% |
| Average slot time (ms) | 214.90 | 215.40 | +0.23% |
| Active validators | 663.00 | 662.00 | -0.15% |
| Delinquent validators | 36.00 | 37.00 | +2.78% |
| Solana TVL | 4,895,736,754.00 | 4,612,450,821.00 | -5.79% |
| SOL price | 75.18 | 71.61 | -4.75% |
| Stablecoin supply | 14,224,740,618.00 | 14,224,431,770.00 | -0.00% |
| 24h DEX volume | 1,453,256,848.20 | 1,614,007,307.70 | +11.06% |
| 24h chain fees | 9,338,440.34 | 8,186,168.20 | -12.34% |

### Change over 7d (vs run at 2026-11-08T02:57:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,493.63 | 1,657.93 | +11.00% |
| Average non-vote TPS | 1,493.63 | 1,657.93 | +11.00% |
| Average slot time (ms) | 214.30 | 215.40 | +0.51% |
| Active validators | 664.00 | 662.00 | -0.30% |
| Delinquent validators | 33.00 | 37.00 | +12.12% |
| Solana TVL | 5,215,961,212.00 | 4,612,450,821.00 | -11.57% |
| SOL price | 88.84 | 71.61 | -19.39% |
| Stablecoin supply | 14,932,755,317.00 | 14,224,431,770.00 | -4.74% |
| 24h DEX volume | 1,298,696,797.61 | 1,614,007,307.70 | +24.28% |
| 24h chain fees | 7,982,653.69 | 8,186,168.20 | +2.55% |

### Change over 30d (vs run at 2026-10-15T20:36:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,323.17 | 1,657.93 | -68.85% |
| Average non-vote TPS | 2,236.62 | 1,657.93 | -25.87% |
| Average slot time (ms) | 216.50 | 215.40 | -0.51% |
| Active validators | 672.00 | 662.00 | -1.49% |
| Delinquent validators | 9.00 | 37.00 | +311.11% |
| Solana TVL | 6,044,693,032.00 | 4,612,450,821.00 | -23.69% |
| SOL price | 105.91 | 71.61 | -32.39% |
| Stablecoin supply | 16,055,865,871.00 | 14,224,431,770.00 | -11.41% |
| 24h DEX volume | 2,118,350,659.32 | 1,614,007,307.70 | -23.81% |
| 24h chain fees | 10,654,111.63 | 8,186,168.20 | -23.16% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
