# Solana Ecosystem Pulse

**Generated:** 2026-11-10T13:51:54Z · **Schema:** `1.0.0` · **Collection time:** 24.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $84.45 | -2.35% |
| Market cap | $49.93B | rank #7 |
| Total value locked | $5.02B | -1.93% |
| Stablecoin supply | $14.83B | -1.54% |
| DEX volume (24h) | $1.49B | +42.59% |
| Chain fees / REV (24h) | $9.38M | +12.89% |
| Non-vote TPS (1h avg) | 1,797 | peak 4,387 total |
| Active validators | 657 | 41 delinquent |
| Epoch 1082 | 74.07% complete | 112,036 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 42.6% in 24h) | DEX volume changed +42.6% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 41.00 sits 3.0 sigma above the median of the last 129 runs (14.00, +192.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,797.2 average over the last 60 minutes; 1,776.5 in the latest sample.
- **Total TPS:** 1,797.2 average, 4,387.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.2 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 445,761,402 at absolute slot 467,743,964.
- **Epoch 1082:** slot 319,964 of 432,000 (74.07% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.563% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 711 ms |
| `solana-rpc.publicnode.com` | yes | 87 ms |
| `api.mainnet.solana.com` | yes | 545 ms |

## Validators & stake

- **657 active** validators, **41 delinquent** (5.87% by count, 0.224% by stake).
- **Total stake:** 434,984,472 SOL ($36.73B); stake rate 68.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 46.50% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 218 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,898,208 | 3.894% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,746,254 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,034,244 | 3.003% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,280,950 | 2.369% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,598,549 | 2.212% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,851 | 2.201% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,233,159 | 2.127% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,813,316 | 1.800% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,971 | 1.610% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,712,231 | 1.547% | 5% |

## Economics

- **SOL:** $84.45 (-2.35% 24h, -9.17% 7d, -22.82% 30d). Market cap $49.93B, 24h volume $2.34B (4.70% of cap). Price source: `coingecko`.
- **TVL:** $5.02B across 341 protocols - rank #4 of 422 chains, 6.42% of all tracked chain TVL. -7.54% over 7d, -61.2% from its ATH.
- **Stablecoins:** $14.83B circulating on Solana (-4.27% 7d) - $2.95 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.49B in 24h, $11.39B over 7d across 141 venues. Volume/TVL turnover 0.296x per day.
- **REV (chain fees):** $9.38M in 24h, $335.63M over 30d. Retained chain revenue $3.08M (32.8% of fees). Annualised fees are 6.86% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,149,055 SOL circulating of 637,310,925 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.51B | -1.7% | -7.3% |
| 2 | Kamino Lend | Lending | $1.16B | +0.7% | -6.1% |
| 3 | Raydium AMM | Dexs | $960.17M | -1.8% | -7.0% |
| 4 | Binance Staked SOL | Liquid Staking | $920.39M | -1.7% | -8.1% |
| 5 | Jupiter Lend | Lending | $896.77M | -0.9% | -11.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $867.36M | -1.5% | -8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $637.85M | -0.9% | -4.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $432.10M | -1.5% | -7.3% |
| 9 | Sentora Curator | Risk Curators | $374.44M | +0.1% | +0.3% |
| 10 | OnRe | RWA | $309.36M | +0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $298.97M | -1.7% | -9.4% |
| 12 | Orca DEX | Dexs | $277.18M | +0.1% | -3.4% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.39B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.3% · Lending 17.1% · Dexs 14.9% · Derivatives 5.2% · RWA 4.5% · Risk Curators 4.0%

### Tokenised assets

$860.51M of tokenised real-world assets and equities are locked on Solana - 6.429% of chain TVL.

- OnRe (RWA): $309.36M
- Huma (RWA): $240.55M
- Solstice (Basis Trading): $201.00M
- JupUSD (Basis Trading): $43.85M
- Plume Vaults (RWA): $36.87M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-09
- [SIMD-0326: Amend SIMD-0326: define BLS validator ranks](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-09
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06

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

### Change over 24h (vs run at 2026-11-09T14:31:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,665.74 | 1,797.16 | +7.89% |
| Average non-vote TPS | 1,665.74 | 1,797.16 | +7.89% |
| Average slot time (ms) | 214.30 | 214.20 | -0.05% |
| Active validators | 663.00 | 657.00 | -0.90% |
| Delinquent validators | 34.00 | 41.00 | +20.59% |
| Solana TVL | 5,081,946,678.00 | 5,023,282,930.00 | -1.15% |
| SOL price | 86.96 | 84.45 | -2.89% |
| Stablecoin supply | 15,065,947,064.00 | 14,832,999,164.00 | -1.55% |
| 24h DEX volume | 1,043,374,478.30 | 1,487,777,537.32 | +42.59% |
| 24h chain fees | 8,307,454.36 | 9,381,055.72 | +12.92% |

### Change over 7d (vs run at 2026-11-03T13:07:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,522.59 | 1,797.16 | +18.03% |
| Average non-vote TPS | 1,522.59 | 1,797.16 | +18.03% |
| Average slot time (ms) | 213.90 | 214.20 | +0.14% |
| Active validators | 664.00 | 657.00 | -1.05% |
| Delinquent validators | 29.00 | 41.00 | +41.38% |
| Solana TVL | 5,402,051,428.00 | 5,023,282,930.00 | -7.01% |
| SOL price | 92.81 | 84.45 | -9.01% |
| Stablecoin supply | 15,370,716,122.00 | 14,832,999,164.00 | -3.50% |
| 24h DEX volume | 1,830,732,933.50 | 1,487,777,537.32 | -18.73% |
| 24h chain fees | 11,140,650.50 | 9,381,055.72 | -15.79% |

### Change over 30d (vs run at 2026-10-11T21:08:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.95 | 1,797.16 | -63.88% |
| Average non-vote TPS | 1,917.24 | 1,797.16 | -6.26% |
| Average slot time (ms) | 218.90 | 214.20 | -2.15% |
| Active validators | 672.00 | 657.00 | -2.23% |
| Delinquent validators | 9.00 | 41.00 | +355.56% |
| Solana TVL | 6,251,230,542.00 | 5,023,282,930.00 | -19.64% |
| SOL price | 110.93 | 84.45 | -23.87% |
| Stablecoin supply | 16,405,817,670.00 | 14,832,999,164.00 | -9.59% |
| 24h DEX volume | 1,286,316,590.57 | 1,487,777,537.32 | +15.66% |
| 24h chain fees | 11,936,417.92 | 9,381,055.72 | -21.41% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 24.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
