# Solana Ecosystem Pulse

**Generated:** 2026-11-10T00:55:08Z · **Schema:** `1.0.0` · **Collection time:** 21.2s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $86.31 | -1.12% |
| Market cap | $51.02B | rank #7 |
| Total value locked | $5.09B | -2.27% |
| Stablecoin supply | $15.06B | -0.54% |
| DEX volume (24h) | $1.20B | +15.41% |
| Chain fees / REV (24h) | $8.68M | +4.56% |
| Non-vote TPS (1h avg) | 1,628 | peak 2,543 total |
| Active validators | 657 | 41 delinquent |
| Epoch 1082 | 23.67% complete | 329,747 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 41.00 sits 3.0 sigma above the median of the last 130 runs (14.00, +192.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,627.6 average over the last 60 minutes; 1,148.7 in the latest sample.
- **Total TPS:** 1,627.6 average, 2,543.2 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.4 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 445,543,944 at absolute slot 467,526,253.
- **Epoch 1082:** slot 102,253 of 432,000 (23.67% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.563% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 233 ms |
| `solana-rpc.publicnode.com` | yes | 124 ms |
| `api.mainnet.solana.com` | yes | 266 ms |

## Validators & stake

- **657 active** validators, **41 delinquent** (5.87% by count, 0.224% by stake).
- **Total stake:** 434,984,472 SOL ($37.54B); stake rate 68.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 46.50% of active stake.
- **Commission:** median 5.0%, mean 12.65%; 220 validators at 0% and 60 at 100%.

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

- **SOL:** $86.31 (-1.12% 24h, -6.02% 7d, -21.54% 30d). Market cap $51.02B, 24h volume $2.42B (4.74% of cap). Price source: `coingecko`.
- **TVL:** $5.09B across 341 protocols - rank #4 of 422 chains, 6.43% of all tracked chain TVL. -7.29% over 7d, -60.6% from its ATH.
- **Stablecoins:** $15.06B circulating on Solana (-2.43% 7d) - $2.96 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.20B in 24h, $10.41B over 7d across 141 venues. Volume/TVL turnover 0.237x per day.
- **REV (chain fees):** $8.68M in 24h, $328.56M over 30d. Retained chain revenue $2.86M (33.0% of fees). Annualised fees are 6.21% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,149,226 SOL circulating of 637,311,095 total (92.76%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.54B | -0.2% | -5.5% |
| 2 | Kamino Lend | Lending | $1.17B | -0.4% | -5.5% |
| 3 | Raydium AMM | Dexs | $980.45M | -0.5% | -5.1% |
| 4 | Binance Staked SOL | Liquid Staking | $945.49M | -0.3% | -5.6% |
| 5 | Jupiter Lend | Lending | $910.19M | +0.7% | -10.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $882.96M | -0.0% | -6.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $646.94M | +0.1% | -3.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $442.77M | -0.3% | -5.0% |
| 9 | Sentora Curator | Risk Curators | $374.63M | +0.1% | +0.3% |
| 10 | OnRe | RWA | $309.26M | +0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $305.66M | -2.4% | -7.4% |
| 12 | PumpSwap | Dexs | $279.56M | -9.6% | -10.3% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 341 protocols the total is $13.58B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.6% · Lending 17.0% · Dexs 15.0% · Derivatives 5.2% · RWA 4.3% · Risk Curators 4.0%

### Tokenised assets

$844.96M of tokenised real-world assets and equities are locked on Solana - 6.223% of chain TVL.

- OnRe (RWA): $309.26M
- Huma (RWA): $225.05M
- Solstice (Basis Trading): $201.04M
- JupUSD (Basis Trading): $43.84M
- Plume Vaults (RWA): $36.86M

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

### Change over 24h (vs run at 2026-11-09T03:18:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,452.40 | 1,627.58 | +12.06% |
| Average non-vote TPS | 1,452.39 | 1,627.58 | +12.06% |
| Average slot time (ms) | 215.00 | 214.40 | -0.28% |
| Active validators | 662.00 | 657.00 | -0.76% |
| Delinquent validators | 35.00 | 41.00 | +17.14% |
| Solana TVL | 5,134,576,425.00 | 5,091,379,326.00 | -0.84% |
| SOL price | 87.25 | 86.31 | -1.08% |
| Stablecoin supply | 15,064,026,289.00 | 15,064,954,013.00 | +0.01% |
| 24h DEX volume | 997,083,843.30 | 1,204,191,616.64 | +20.77% |
| 24h chain fees | 8,295,890.36 | 8,676,028.36 | +4.58% |

### Change over 7d (vs run at 2026-11-03T00:07:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,658.77 | 1,627.58 | -1.88% |
| Average non-vote TPS | 1,658.77 | 1,627.58 | -1.88% |
| Average slot time (ms) | 214.20 | 214.40 | +0.09% |
| Active validators | 664.00 | 657.00 | -1.05% |
| Delinquent validators | 29.00 | 41.00 | +41.38% |
| Solana TVL | 5,362,623,249.00 | 5,091,379,326.00 | -5.06% |
| SOL price | 91.88 | 86.31 | -6.06% |
| Stablecoin supply | 15,440,330,579.00 | 15,064,954,013.00 | -2.43% |
| 24h DEX volume | 905,602,298.19 | 1,204,191,616.64 | +32.97% |
| 24h chain fees | 8,394,709.28 | 8,676,028.36 | +3.35% |

### Change over 30d (vs run at 2026-10-10T20:47:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,930.72 | 1,627.58 | -66.99% |
| Average non-vote TPS | 1,904.19 | 1,627.58 | -14.53% |
| Average slot time (ms) | 218.10 | 214.40 | -1.70% |
| Active validators | 675.00 | 657.00 | -2.67% |
| Delinquent validators | 5.00 | 41.00 | +720.00% |
| Solana TVL | 6,218,574,826.00 | 5,091,379,326.00 | -18.13% |
| SOL price | 110.30 | 86.31 | -21.75% |
| Stablecoin supply | 16,426,716,932.00 | 15,064,954,013.00 | -8.29% |
| 24h DEX volume | 1,978,097,665.91 | 1,204,191,616.64 | -39.12% |
| 24h chain fees | 13,913,073.58 | 8,676,028.36 | -37.64% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
