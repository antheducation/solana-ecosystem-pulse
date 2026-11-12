# Solana Ecosystem Pulse

**Generated:** 2026-11-12T14:06:03Z · **Schema:** `1.0.0` · **Collection time:** 43.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $81.25 | -3.91% |
| Market cap | $48.05B | rank #7 |
| Total value locked | $5.05B | -0.23% |
| Stablecoin supply | $14.22B | -0.53% |
| DEX volume (24h) | $1.62B | +20.81% |
| Chain fees / REV (24h) | $10.19M | +21.06% |
| Non-vote TPS (1h avg) | 1,949 | peak 4,031 total |
| Active validators | 661 | 37 delinquent |
| Epoch 1084 | 61.24% complete | 167,441 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,949.1 average over the last 60 minutes; 2,153.0 in the latest sample.
- **Total TPS:** 1,949.1 average, 4,031.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 446,568,325 at absolute slot 468,552,559.
- **Epoch 1084:** slot 264,559 of 432,000 (61.24% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.560% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 3112 ms |
| `solana-rpc.publicnode.com` | yes | 188 ms |
| `api.mainnet.solana.com` | yes | 1602 ms |

## Validators & stake

- **661 active** validators, **37 delinquent** (5.30% by count, 0.158% by stake).
- **Total stake:** 433,416,361 SOL ($35.22B); stake rate 67.99% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.52% and top 33 hold 46.48% of active stake.
- **Commission:** median 5.0%, mean 12.88%; 222 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,789,054 | 3.880% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,119,194 | 3.725% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,026,247 | 3.010% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,116,092 | 2.338% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,681,376 | 2.237% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,180 | 2.214% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,230,504 | 2.133% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,840,792 | 1.812% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,981 | 1.615% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,421 | 1.555% | 5% |

## Economics

- **SOL:** $81.25 (-3.91% 24h, -14.75% 7d, -23.86% 30d). Market cap $48.05B, 24h volume $2.00B (4.17% of cap). Price source: `coingecko`.
- **TVL:** $5.05B across 343 protocols - rank #3 of 423 chains, 6.50% of all tracked chain TVL. -9.32% over 7d, -60.5% from its ATH.
- **Stablecoins:** $14.22B circulating on Solana (-3.34% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.62B in 24h, $10.08B over 7d across 141 venues. Volume/TVL turnover 0.321x per day.
- **REV (chain fees):** $10.19M in 24h, $328.34M over 30d. Retained chain revenue $3.68M (36.1% of fees). Annualised fees are 7.74% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,456,918 SOL circulating of 637,432,757 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -1.2% | -12.4% |
| 2 | Kamino Lend | Lending | $1.15B | -0.5% | -7.4% |
| 3 | Jupiter Lend | Lending | $963.97M | -0.9% | -6.6% |
| 4 | Raydium AMM | Dexs | $946.06M | -0.5% | -11.9% |
| 5 | Binance Staked SOL | Liquid Staking | $900.65M | -0.9% | -13.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $850.71M | -0.8% | -14.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $631.43M | -0.5% | -9.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $423.16M | -1.1% | -12.6% |
| 9 | Sentora Curator | Risk Curators | $363.73M | -2.6% | -2.5% |
| 10 | OnRe | RWA | $309.35M | +0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $278.84M | -3.4% | -18.9% |
| 12 | PumpSwap | Dexs | $271.29M | +0.2% | -17.4% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.24B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.7% · Dexs 14.9% · Derivatives 5.2% · RWA 4.4% · Risk Curators 4.0%

### Tokenised assets

$844.77M of tokenised real-world assets and equities are locked on Solana - 6.381% of chain TVL.

- OnRe (RWA): $309.35M
- Huma (RWA): $225.76M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $43.69M
- Plume Vaults (RWA): $36.97M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-10
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
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

### Change over 24h (vs run at 2026-11-11T13:03:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,606.62 | 1,949.09 | +21.32% |
| Average non-vote TPS | 1,606.62 | 1,949.09 | +21.32% |
| Average slot time (ms) | 214.60 | 215.20 | +0.28% |
| Active validators | 659.00 | 661.00 | +0.30% |
| Delinquent validators | 40.00 | 37.00 | -7.50% |
| Solana TVL | 5,072,108,301.00 | 5,045,244,828.00 | -0.53% |
| SOL price | 83.71 | 81.25 | -2.94% |
| Stablecoin supply | 14,784,717,550.00 | 14,223,898,249.00 | -3.79% |
| 24h DEX volume | 1,342,063,202.34 | 1,617,758,399.95 | +20.54% |
| 24h chain fees | 8,399,659.99 | 10,185,070.88 | +21.26% |

### Change over 7d (vs run at 2026-11-05T13:37:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,603.34 | 1,949.09 | +21.56% |
| Average non-vote TPS | 1,603.34 | 1,949.09 | +21.56% |
| Average slot time (ms) | 213.80 | 215.20 | +0.65% |
| Active validators | 663.00 | 661.00 | -0.30% |
| Delinquent validators | 31.00 | 37.00 | +19.35% |
| Solana TVL | 5,577,510,303.00 | 5,045,244,828.00 | -9.54% |
| SOL price | 95.28 | 81.25 | -14.73% |
| Stablecoin supply | 15,183,394,102.00 | 14,223,898,249.00 | -6.32% |
| 24h DEX volume | 2,385,538,829.94 | 1,617,758,399.95 | -32.18% |
| 24h chain fees | 11,226,354.64 | 10,185,070.88 | -9.28% |

### Change over 30d (vs run at 2026-10-13T22:01:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,063.39 | 1,949.09 | -61.51% |
| Average non-vote TPS | 1,990.01 | 1,949.09 | -2.06% |
| Average slot time (ms) | 217.80 | 215.20 | -1.19% |
| Active validators | 673.00 | 661.00 | -1.78% |
| Delinquent validators | 7.00 | 37.00 | +428.57% |
| Solana TVL | 6,063,416,281.00 | 5,045,244,828.00 | -16.79% |
| SOL price | 107.01 | 81.25 | -24.07% |
| Stablecoin supply | 16,241,793,471.00 | 14,223,898,249.00 | -12.42% |
| 24h DEX volume | 2,231,842,381.02 | 1,617,758,399.95 | -27.51% |
| 24h chain fees | 13,103,539.72 | 10,185,070.88 | -22.27% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 43.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
