# Solana Ecosystem Pulse

**Generated:** 2026-11-09T14:31:13Z · **Schema:** `1.0.0` · **Collection time:** 22.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $86.96 | -2.36% |
| Market cap | $51.40B | rank #7 |
| Total value locked | $5.08B | -2.46% |
| Stablecoin supply | $15.07B | -0.53% |
| DEX volume (24h) | $1.04B | +13.73% |
| Chain fees / REV (24h) | $8.31M | +3.73% |
| Non-vote TPS (1h avg) | 1,666 | peak 2,849 total |
| Active validators | 663 | 34 delinquent |
| Epoch 1081 | 83.32% complete | 72,062 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,665.7 average over the last 60 minutes; 2,849.4 in the latest sample.
- **Total TPS:** 1,665.7 average, 2,849.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 219.8 ms.
- **Block height:** 445,369,862 at absolute slot 467,351,938.
- **Epoch 1081:** slot 359,938 of 432,000 (83.32% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.565% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 261 ms |
| `solana-rpc.publicnode.com` | yes | 159 ms |
| `api.mainnet.solana.com` | yes | 166 ms |

## Validators & stake

- **663 active** validators, **34 delinquent** (4.88% by count, 0.129% by stake).
- **Total stake:** 433,920,561 SOL ($37.73B); stake rate 68.09% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.66% and top 33 hold 46.51% of active stake.
- **Commission:** median 5.0%, mean 13.01%; 221 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,050,553 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,720,131 | 3.858% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,021,912 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,279,070 | 2.372% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,388 | 2.204% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,550,278 | 2.204% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,876 | 2.128% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,775,137 | 1.794% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,980,319 | 1.611% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,711,284 | 1.549% | 5% |

## Economics

- **SOL:** $86.96 (-2.36% 24h, -7.71% 7d, -20.83% 30d). Market cap $51.40B, 24h volume $2.86B (5.57% of cap). Price source: `coingecko`.
- **TVL:** $5.08B across 341 protocols - rank #3 of 421 chains, 6.46% of all tracked chain TVL. -7.46% over 7d, -60.7% from its ATH.
- **Stablecoins:** $15.07B circulating on Solana (-2.42% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.04B in 24h, $11.76B over 7d across 141 venues. Volume/TVL turnover 0.205x per day.
- **REV (chain fees):** $8.31M in 24h, $339.17M over 30d. Retained chain revenue $2.74M (33.0% of fees). Annualised fees are 5.90% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,093,583 SOL circulating of 637,249,825 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | -3.4% | -8.1% |
| 2 | Kamino Lend | Lending | $1.15B | -2.8% | -6.1% |
| 3 | Raydium AMM | Dexs | $977.50M | -3.0% | -8.5% |
| 4 | Binance Staked SOL | Liquid Staking | $936.53M | -3.9% | -9.1% |
| 5 | Jupiter Lend | Lending | $905.35M | -2.6% | -9.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $880.70M | -3.3% | -10.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $643.87M | -2.4% | -6.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $438.59M | -4.0% | -7.9% |
| 9 | Sentora Curator | Risk Curators | $374.17M | +0.1% | -0.6% |
| 10 | OnRe | RWA | $309.30M | +0.0% | +0.5% |
| 11 | Marinade Native | Staking Pool | $304.05M | -5.3% | -11.3% |
| 12 | PumpSwap | Dexs | $297.96M | -3.4% | -7.2% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.55B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.5% · Lending 16.9% · Dexs 15.1% · Derivatives 5.2% · RWA 4.3% · Risk Curators 4.0%

### Tokenised assets

$844.92M of tokenised real-world assets and equities are locked on Solana - 6.238% of chain TVL.

- OnRe (RWA): $309.30M
- Huma (RWA): $224.95M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $43.84M
- Plume Vaults (RWA): $36.84M

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

- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0326: Amend SIMD-0326: define BLS validator ranks](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-09
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-09
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

### Change over 24h (vs run at 2026-11-08T12:19:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,031.62 | 1,665.74 | +61.47% |
| Average non-vote TPS | 1,031.62 | 1,665.74 | +61.47% |
| Average slot time (ms) | 214.60 | 214.30 | -0.14% |
| Active validators | 663.00 | 663.00 | +0.00% |
| Delinquent validators | 34.00 | 34.00 | +0.00% |
| Solana TVL | 5,212,225,415.00 | 5,081,946,678.00 | -2.50% |
| SOL price | 89.53 | 86.96 | -2.87% |
| Stablecoin supply | 14,933,269,295.00 | 15,065,947,064.00 | +0.89% |
| 24h DEX volume | 917,438,831.61 | 1,043,374,478.30 | +13.73% |
| 24h chain fees | 8,025,862.47 | 8,307,454.36 | +3.51% |

### Change over 7d (vs run at 2026-11-02T13:58:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,735.94 | 1,665.74 | -4.04% |
| Average non-vote TPS | 1,735.94 | 1,665.74 | -4.04% |
| Average slot time (ms) | 215.10 | 214.30 | -0.37% |
| Active validators | 666.00 | 663.00 | -0.45% |
| Delinquent validators | 28.00 | 34.00 | +21.43% |
| Solana TVL | 5,468,197,763.00 | 5,081,946,678.00 | -7.06% |
| SOL price | 94.34 | 86.96 | -7.82% |
| Stablecoin supply | 15,442,364,185.00 | 15,065,947,064.00 | -2.44% |
| 24h DEX volume | 905,602,298.19 | 1,043,374,478.30 | +15.21% |
| 24h chain fees | 8,395,340.05 | 8,307,454.36 | -1.05% |

### Change over 30d (vs run at 2026-10-10T20:47:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,930.72 | 1,665.74 | -66.22% |
| Average non-vote TPS | 1,904.19 | 1,665.74 | -12.52% |
| Average slot time (ms) | 218.10 | 214.30 | -1.74% |
| Active validators | 675.00 | 663.00 | -1.78% |
| Delinquent validators | 5.00 | 34.00 | +580.00% |
| Solana TVL | 6,218,574,826.00 | 5,081,946,678.00 | -18.28% |
| SOL price | 110.30 | 86.96 | -21.16% |
| Stablecoin supply | 16,426,716,932.00 | 15,065,947,064.00 | -8.28% |
| 24h DEX volume | 1,978,097,665.91 | 1,043,374,478.30 | -47.25% |
| 24h chain fees | 13,913,073.58 | 8,307,454.36 | -40.29% |

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
