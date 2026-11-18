# Solana Ecosystem Pulse

**Generated:** 2026-11-18T23:39:14Z · **Schema:** `1.0.0` · **Collection time:** 20.7s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $73.41 | -2.18% |
| Market cap | $43.45B | rank #7 |
| Total value locked | $4.73B | -0.14% |
| Stablecoin supply | $13.98B | -2.50% |
| DEX volume (24h) | $1.51B | +2.01% |
| Chain fees / REV (24h) | $8.20M | -1.59% |
| Non-vote TPS (1h avg) | 2,148 | peak 2,795 total |
| Active validators | 660 | 25 delinquent |
| Epoch 1090 | 55.86% complete | 190,691 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 131 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,148.2 average over the last 60 minutes; 2,233.8 in the latest sample.
- **Total TPS:** 2,148.2 average, 2,795.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.3 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 449,135,664 at absolute slot 471,121,309.
- **Epoch 1090:** slot 241,309 of 432,000 (55.86% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.551% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 198 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 127 ms |

## Validators & stake

- **660 active** validators, **25 delinquent** (3.65% by count, 0.015% by stake).
- **Total stake:** 426,746,616 SOL ($31.33B); stake rate 66.91% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.98% and top 33 hold 46.77% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 219 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,030,759 | 3.991% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,476,078 | 3.861% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,423,470 | 2.912% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,297,722 | 2.413% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,430 | 2.300% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,562 | 2.244% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,715 | 2.162% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,973,220 | 1.869% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,720 | 1.640% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,771,472 | 1.587% | 5% |

## Economics

- **SOL:** $73.41 (-2.18% 24h, -11.93% 7d, -30.15% 30d). Market cap $43.45B, 24h volume $2.14B (4.92% of cap). Price source: `coingecko`.
- **TVL:** $4.73B across 341 protocols - rank #3 of 425 chains, 6.75% of all tracked chain TVL. -6.51% over 7d, -60.2% from its ATH.
- **Stablecoins:** $13.98B circulating on Solana (-2.27% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.51B in 24h, $10.72B over 7d across 144 venues. Volume/TVL turnover 0.319x per day.
- **REV (chain fees):** $8.20M in 24h, $307.69M over 30d. Retained chain revenue $2.97M (36.3% of fees). Annualised fees are 6.89% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,794,657 SOL circulating of 637,798,693 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.35B | -2.8% | -8.3% |
| 2 | Kamino Lend | Lending | $1.15B | -0.5% | -1.3% |
| 3 | Jupiter Lend | Lending | $953.29M | -2.6% | -1.2% |
| 4 | Raydium AMM | Dexs | $807.60M | +0.6% | -14.7% |
| 5 | Binance Staked SOL | Liquid Staking | $752.04M | -1.0% | -16.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $737.86M | -1.2% | -13.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $584.69M | -0.5% | -7.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $372.01M | -2.2% | -12.2% |
| 9 | Sentora Curator | Risk Curators | $357.09M | +0.1% | -4.7% |
| 10 | Forward Industries SOL | Liquid Staking | $294.23M | -1.4% | +11.9% |
| 11 | OnRe | RWA | $292.94M | -0.1% | -5.3% |
| 12 | CCIP | Bridge | $262.65M | -0.2% | -1.0% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 341 protocols the total is $12.09B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.9% · Lending 19.0% · Dexs 14.7% · Derivatives 5.3% · RWA 4.6% · Risk Curators 3.9%

### Tokenised assets

$816.22M of tokenised real-world assets and equities are locked on Solana - 6.750% of chain TVL.

- OnRe (RWA): $292.94M
- Huma (RWA): $219.59M
- Solstice (Basis Trading): $201.08M
- JupUSD (Basis Trading): $40.03M
- Plume Vaults (RWA): $39.31M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-18
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
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

### Change over 24h (vs run at 2026-11-18T00:06:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,864.62 | 2,148.25 | +15.21% |
| Average non-vote TPS | 1,864.62 | 2,148.25 | +15.21% |
| Average slot time (ms) | 216.30 | 215.30 | -0.46% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 5.00 | 25.00 | +400.00% |
| Solana TVL | 4,761,137,008.00 | 4,729,553,664.00 | -0.66% |
| SOL price | 74.98 | 73.41 | -2.09% |
| Stablecoin supply | 14,334,785,302.00 | 13,976,223,818.00 | -2.50% |
| 24h DEX volume | 1,479,924,560.31 | 1,509,645,641.17 | +2.01% |
| 24h chain fees | 8,328,289.41 | 8,200,783.62 | -1.53% |

### Change over 7d (vs run at 2026-11-11T23:46:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,538.44 | 2,148.25 | -15.37% |
| Average non-vote TPS | 2,538.44 | 2,148.25 | -15.37% |
| Average slot time (ms) | 215.30 | 215.30 | +0.00% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 37.00 | 25.00 | -32.43% |
| Solana TVL | 5,112,344,922.00 | 4,729,553,664.00 | -7.49% |
| SOL price | 82.86 | 73.41 | -11.40% |
| Stablecoin supply | 14,299,520,719.00 | 13,976,223,818.00 | -2.26% |
| 24h DEX volume | 1,342,063,202.34 | 1,509,645,641.17 | +12.49% |
| 24h chain fees | 8,413,550.31 | 8,200,783.62 | -2.53% |

### Change over 30d (vs run at 2026-10-19T21:47:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,210.74 | 2,148.25 | -58.77% |
| Average non-vote TPS | 2,163.29 | 2,148.25 | -0.70% |
| Average slot time (ms) | 218.40 | 215.30 | -1.42% |
| Active validators | 669.00 | 660.00 | -1.35% |
| Delinquent validators | 10.00 | 25.00 | +150.00% |
| Solana TVL | 5,846,232,281.00 | 4,729,553,664.00 | -19.10% |
| SOL price | 104.69 | 73.41 | -29.88% |
| Stablecoin supply | 15,840,000,252.00 | 13,976,223,818.00 | -11.77% |
| 24h DEX volume | 1,697,352,650.38 | 1,509,645,641.17 | -11.06% |
| 24h chain fees | 9,839,385.63 | 8,200,783.62 | -16.65% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
