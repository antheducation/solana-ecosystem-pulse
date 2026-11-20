# Solana Ecosystem Pulse

**Generated:** 2026-11-20T05:26:43Z · **Schema:** `1.0.0` · **Collection time:** 20.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $72.02 | -3.44% |
| Market cap | $42.63B | rank #7 |
| Total value locked | $4.73B | -0.54% |
| Stablecoin supply | $13.45B | +3.05% |
| DEX volume (24h) | $1.85B | +1.76% |
| Chain fees / REV (24h) | $9.57M | -12.12% |
| Non-vote TPS (1h avg) | 1,702 | peak 2,380 total |
| Active validators | 659 | 26 delinquent |
| Epoch 1091 | 71.19% complete | 124,443 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 132 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (up 3.0% in 24h) | Stablecoin supply changed +3.0% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,453,468,145.00 sits 3.2 sigma below the median of the last 132 runs (15,987,963,445.50, -15.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,702.1 average over the last 60 minutes; 1,812.6 in the latest sample.
- **Total TPS:** 1,702.1 average, 2,379.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.0 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 449,633,658 at absolute slot 471,619,557.
- **Epoch 1091:** slot 307,557 of 432,000 (71.19% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.549% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 343 ms |
| `solana-rpc.publicnode.com` | yes | 157 ms |
| `api.mainnet.solana.com` | yes | 192 ms |

## Validators & stake

- **659 active** validators, **26 delinquent** (3.80% by count, 0.025% by stake).
- **Total stake:** 428,682,730 SOL ($30.87B); stake rate 67.21% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.85% and top 33 hold 46.55% of active stake.
- **Commission:** median 5.0%, mean 12.78%; 218 validators at 0% and 61 at 100%.

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

- **SOL:** $72.02 (-3.44% 24h, -8.05% 7d, -31.92% 30d). Market cap $42.63B, 24h volume $2.46B (5.78% of cap). Price source: `coingecko`.
- **TVL:** $4.73B across 342 protocols - rank #3 of 425 chains, 6.81% of all tracked chain TVL. -6.25% over 7d, -60.4% from its ATH.
- **Stablecoins:** $13.45B circulating on Solana (-6.42% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.85B in 24h, $10.39B over 7d across 144 venues. Volume/TVL turnover 0.390x per day.
- **REV (chain fees):** $9.57M in 24h, $298.19M over 30d. Retained chain revenue $3.16M (33.1% of fees). Annualised fees are 8.19% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,851,277 SOL circulating of 637,859,453 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.33B | -3.5% | -8.7% |
| 2 | Kamino Lend | Lending | $1.14B | -1.1% | -3.1% |
| 3 | Jupiter Lend | Lending | $974.14M | +1.1% | +1.4% |
| 4 | Raydium AMM | Dexs | $798.48M | -1.5% | -14.4% |
| 5 | Binance Staked SOL | Liquid Staking | $751.79M | -2.1% | -15.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $724.25M | -3.5% | -13.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $577.68M | -2.6% | -7.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $372.13M | -2.1% | -10.8% |
| 9 | Sentora Curator | Risk Curators | $357.28M | -0.2% | -1.7% |
| 10 | OnRe | RWA | $291.65M | -0.4% | -5.7% |
| 11 | Forward Industries SOL | Liquid Staking | $286.83M | -2.1% | +11.4% |
| 12 | CCIP | Bridge | $272.00M | +4.1% | +3.6% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 342 protocols the total is $12.05B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.5% · Lending 19.2% · Dexs 14.5% · Derivatives 5.3% · RWA 4.7% · Risk Curators 4.1%

### Tokenised assets

$827.66M of tokenised real-world assets and equities are locked on Solana - 6.866% of chain TVL.

- OnRe (RWA): $291.65M
- Huma (RWA): $231.41M
- Solstice (Basis Trading): $201.04M
- Plume Vaults (RWA): $40.05M
- JupUSD (Basis Trading): $40.03M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-19
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-19
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14

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

### Change over 24h (vs run at 2026-11-19T04:46:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,489.70 | 1,702.06 | +14.26% |
| Average non-vote TPS | 1,489.70 | 1,702.06 | +14.26% |
| Average slot time (ms) | 214.50 | 215.00 | +0.23% |
| Active validators | 660.00 | 659.00 | -0.15% |
| Delinquent validators | 25.00 | 26.00 | +4.00% |
| Solana TVL | 4,734,424,341.00 | 4,734,235,007.00 | -0.00% |
| SOL price | 74.66 | 72.02 | -3.54% |
| Stablecoin supply | 13,054,954,798.00 | 13,453,468,145.00 | +3.05% |
| 24h DEX volume | 1,701,658,023.31 | 1,847,338,570.06 | +8.56% |
| 24h chain fees | 9,966,607.56 | 9,565,396.59 | -4.03% |

### Change over 7d (vs run at 2026-11-13T03:50:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,245.44 | 1,702.06 | -24.20% |
| Average non-vote TPS | 2,245.44 | 1,702.06 | -24.20% |
| Average slot time (ms) | 215.80 | 215.00 | -0.37% |
| Active validators | 659.00 | 659.00 | +0.00% |
| Delinquent validators | 40.00 | 26.00 | -35.00% |
| Solana TVL | 5,024,451,399.00 | 4,734,235,007.00 | -5.78% |
| SOL price | 78.76 | 72.02 | -8.56% |
| Stablecoin supply | 14,374,630,148.00 | 13,453,468,145.00 | -6.41% |
| 24h DEX volume | 1,511,008,694.77 | 1,847,338,570.06 | +22.26% |
| 24h chain fees | 8,490,485.20 | 9,565,396.59 | +12.66% |

### Change over 30d (vs run at 2026-10-20T20:57:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,725.49 | 1,702.06 | -70.27% |
| Average non-vote TPS | 2,649.32 | 1,702.06 | -35.75% |
| Average slot time (ms) | 216.10 | 215.00 | -0.51% |
| Active validators | 668.00 | 659.00 | -1.35% |
| Delinquent validators | 11.00 | 26.00 | +136.36% |
| Solana TVL | 5,971,159,147.00 | 4,734,235,007.00 | -20.71% |
| SOL price | 106.50 | 72.02 | -32.38% |
| Stablecoin supply | 15,910,290,288.00 | 13,453,468,145.00 | -15.44% |
| 24h DEX volume | 1,823,579,289.83 | 1,847,338,570.06 | +1.30% |
| 24h chain fees | 11,987,511.75 | 9,565,396.59 | -20.21% |

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
