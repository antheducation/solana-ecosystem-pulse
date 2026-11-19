# Solana Ecosystem Pulse

**Generated:** 2026-11-19T14:47:51Z · **Schema:** `1.0.0` · **Collection time:** 22.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $75.26 | +2.29% |
| Market cap | $44.54B | rank #7 |
| Total value locked | $4.79B | -0.74% |
| Stablecoin supply | $13.05B | -6.59% |
| DEX volume (24h) | $1.82B | +20.25% |
| Chain fees / REV (24h) | $10.95M | +33.50% |
| Non-vote TPS (1h avg) | 1,968 | peak 3,021 total |
| Active validators | 659 | 26 delinquent |
| Epoch 1091 | 14.52% complete | 369,273 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 132 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (down 6.6% in 24h) | Stablecoin supply changed -6.6% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,054,966,449.00 sits 3.7 sigma below the median of the last 132 runs (15,987,963,445.50, -18.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,967.5 average over the last 60 minutes; 2,587.6 in the latest sample.
- **Total TPS:** 1,967.5 average, 3,020.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.8 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 449,388,996 at absolute slot 471,374,727.
- **Epoch 1091:** slot 62,727 of 432,000 (14.52% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.549% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 210 ms |
| `solana-rpc.publicnode.com` | yes | 112 ms |
| `api.mainnet.solana.com` | yes | 178 ms |

## Validators & stake

- **659 active** validators, **26 delinquent** (3.80% by count, 0.025% by stake).
- **Total stake:** 428,682,730 SOL ($32.26B); stake rate 67.21% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.85% and top 33 hold 46.55% of active stake.
- **Commission:** median 5.0%, mean 12.63%; 219 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,960 | 3.973% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,375,745 | 3.821% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,422,025 | 2.898% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,299,570 | 2.403% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,431 | 2.290% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,573,248 | 2.234% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,578 | 2.153% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,980,784 | 1.862% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,844 | 1.633% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,772,455 | 1.580% | 5% |

## Economics

- **SOL:** $75.26 (+2.29% 24h, -7.49% 7d, -28.37% 30d). Market cap $44.54B, 24h volume $2.12B (4.76% of cap). Price source: `coingecko`.
- **TVL:** $4.79B across 341 protocols - rank #3 of 425 chains, 6.72% of all tracked chain TVL. -5.43% over 7d, -59.7% from its ATH.
- **Stablecoins:** $13.05B circulating on Solana (-8.23% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.82B in 24h, $10.91B over 7d across 144 venues. Volume/TVL turnover 0.379x per day.
- **REV (chain fees):** $10.95M in 24h, $305.44M over 30d. Retained chain revenue $3.69M (33.7% of fees). Annualised fees are 8.98% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,851,590 SOL circulating of 637,859,765 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.38B | -0.3% | -7.6% |
| 2 | Kamino Lend | Lending | $1.16B | +0.5% | -0.2% |
| 3 | Jupiter Lend | Lending | $965.54M | +0.2% | -0.1% |
| 4 | Raydium AMM | Dexs | $822.02M | -0.2% | -13.2% |
| 5 | Binance Staked SOL | Liquid Staking | $774.46M | +1.2% | -14.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $750.43M | -0.3% | -11.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $594.80M | +1.0% | -6.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $383.52M | +1.2% | -10.3% |
| 9 | Sentora Curator | Risk Curators | $357.74M | +0.2% | -4.2% |
| 10 | Forward Industries SOL | Liquid Staking | $294.05M | -1.9% | +11.5% |
| 11 | OnRe | RWA | $291.98M | -0.5% | -5.6% |
| 12 | CCIP | Bridge | $261.59M | -0.5% | -1.4% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 341 protocols the total is $12.28B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.1% · Lending 18.9% · Dexs 14.6% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.0%

### Tokenised assets

$815.70M of tokenised real-world assets and equities are locked on Solana - 6.640% of chain TVL.

- OnRe (RWA): $291.98M
- Huma (RWA): $219.70M
- Solstice (Basis Trading): $201.06M
- JupUSD (Basis Trading): $40.05M
- Plume Vaults (RWA): $39.32M

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

- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-18
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12

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

### Change over 24h (vs run at 2026-11-18T14:41:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,964.18 | 1,967.50 | +0.17% |
| Average non-vote TPS | 1,964.17 | 1,967.50 | +0.17% |
| Average slot time (ms) | 215.80 | 214.80 | -0.46% |
| Active validators | 660.00 | 659.00 | -0.15% |
| Delinquent validators | 25.00 | 26.00 | +4.00% |
| Solana TVL | 4,793,648,732.00 | 4,789,689,320.00 | -0.08% |
| SOL price | 73.81 | 75.26 | +1.96% |
| Stablecoin supply | 13,976,278,030.00 | 13,054,966,449.00 | -6.59% |
| 24h DEX volume | 1,509,645,641.17 | 1,815,395,819.31 | +20.25% |
| 24h chain fees | 8,200,781.62 | 10,954,885.63 | +33.58% |

### Change over 7d (vs run at 2026-11-12T14:06:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,949.09 | 1,967.50 | +0.94% |
| Average non-vote TPS | 1,949.09 | 1,967.50 | +0.94% |
| Average slot time (ms) | 215.20 | 214.80 | -0.19% |
| Active validators | 661.00 | 659.00 | -0.30% |
| Delinquent validators | 37.00 | 26.00 | -29.73% |
| Solana TVL | 5,045,244,828.00 | 4,789,689,320.00 | -5.07% |
| SOL price | 81.25 | 75.26 | -7.37% |
| Stablecoin supply | 14,223,898,249.00 | 13,054,966,449.00 | -8.22% |
| 24h DEX volume | 1,617,758,399.95 | 1,815,395,819.31 | +12.22% |
| 24h chain fees | 10,185,070.88 | 10,954,885.63 | +7.56% |

### Change over 30d (vs run at 2026-10-20T20:57:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,725.49 | 1,967.50 | -65.64% |
| Average non-vote TPS | 2,649.32 | 1,967.50 | -25.74% |
| Average slot time (ms) | 216.10 | 214.80 | -0.60% |
| Active validators | 668.00 | 659.00 | -1.35% |
| Delinquent validators | 11.00 | 26.00 | +136.36% |
| Solana TVL | 5,971,159,147.00 | 4,789,689,320.00 | -19.79% |
| SOL price | 106.50 | 75.26 | -29.33% |
| Stablecoin supply | 15,910,290,288.00 | 13,054,966,449.00 | -17.95% |
| 24h DEX volume | 1,823,579,289.83 | 1,815,395,819.31 | -0.45% |
| 24h chain fees | 11,987,511.75 | 10,954,885.63 | -8.61% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
