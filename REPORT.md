# Solana Ecosystem Pulse

**Generated:** 2026-11-26T01:13:48Z · **Schema:** `1.0.0` · **Collection time:** 52.8s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.92 | +1.99% |
| Market cap | $42.00B | rank #7 |
| Total value locked | $4.59B | +0.00% |
| Stablecoin supply | $13.34B | -1.35% |
| DEX volume (24h) | $1.48B | +1.45% |
| Chain fees / REV (24h) | $7.16M | +0.43% |
| Non-vote TPS (1h avg) | 1,883 | peak 3,553 total |
| Active validators | 655 | 33 delinquent |
| Epoch 1097 | 12.93% complete | 376,149 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,335,674,953.00 sits 3.0 sigma below the median of the last 136 runs (15,967,932,747.50, -16.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,883.1 average over the last 60 minutes; 1,618.8 in the latest sample.
- **Total TPS:** 1,883.1 average, 3,553.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 451,972,782 at absolute slot 473,959,851.
- **Epoch 1097:** slot 55,851 of 432,000 (12.93% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.540% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 718 ms |
| `solana-rpc.publicnode.com` | yes | 31 ms |
| `api.mainnet.solana.com` | yes | 569 ms |

## Validators & stake

- **655 active** validators, **33 delinquent** (4.80% by count, 0.059% by stake).
- **Total stake:** 423,675,927 SOL ($30.05B); stake rate 66.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 25.00% and top 33 hold 46.65% of active stake.
- **Commission:** median 5.0%, mean 13.04%; 219 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,805,000 | 3.969% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,814,431 | 3.735% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,430,859 | 2.936% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,236,589 | 2.418% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,910,258 | 2.340% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,394 | 2.271% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,281,563 | 2.192% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,032,075 | 1.897% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,305 | 1.646% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,740,287 | 1.592% | 5% |

## Economics

- **SOL:** $70.92 (+1.99% 24h, -3.69% 7d, -29.58% 30d). Market cap $42.00B, 24h volume $3.56B (8.47% of cap). Price source: `coingecko`.
- **TVL:** $4.59B across 345 protocols - rank #3 of 426 chains, 6.70% of all tracked chain TVL. -3.08% over 7d, -61.4% from its ATH.
- **Stablecoins:** $13.34B circulating on Solana (+2.15% 7d) - $2.90 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.48B in 24h, $9.96B over 7d across 145 venues. Volume/TVL turnover 0.322x per day.
- **REV (chain fees):** $7.16M in 24h, $269.41M over 30d. Retained chain revenue $2.57M (35.8% of fees). Annualised fees are 6.23% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,183,360 SOL circulating of 638,224,830 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.24B | -3.4% | -8.6% |
| 2 | Kamino Lend | Lending | $1.11B | +0.7% | -3.5% |
| 3 | Jupiter Lend | Lending | $945.61M | +0.7% | -1.4% |
| 4 | Raydium AMM | Dexs | $787.78M | +2.4% | -2.8% |
| 5 | Binance Staked SOL | Liquid Staking | $723.74M | +0.9% | -4.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $709.95M | +0.6% | -4.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $567.15M | +0.4% | -3.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $370.08M | +1.5% | -1.5% |
| 9 | Sentora Curator | Risk Curators | $356.60M | +0.5% | -0.2% |
| 10 | OnRe | RWA | $289.94M | +0.0% | -1.0% |
| 11 | Forward Industries SOL | Liquid Staking | $276.99M | +1.1% | -4.6% |
| 12 | CCIP | Bridge | $267.83M | +0.2% | +2.4% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 345 protocols the total is $11.60B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.0% · Lending 19.3% · Dexs 14.8% · Derivatives 5.4% · RWA 4.5% · Risk Curators 4.1%

### Tokenised assets

$780.23M of tokenised real-world assets and equities are locked on Solana - 6.724% of chain TVL.

- OnRe (RWA): $289.94M
- Huma (RWA): $226.86M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $38.22M
- Solomon USDv (Basis Trading): $8.76M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | 2026-11-25 | pre-release |
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-11-25
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-25
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-11-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-25T01:41:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,306.02 | 1,883.14 | -18.34% |
| Average non-vote TPS | 2,306.02 | 1,883.14 | -18.34% |
| Average slot time (ms) | 203.00 | 215.20 | +6.01% |
| Active validators | 660.00 | 655.00 | -0.76% |
| Delinquent validators | 27.00 | 33.00 | +22.22% |
| Solana TVL | 4,568,842,954.00 | 4,594,999,475.00 | +0.57% |
| SOL price | 69.29 | 70.92 | +2.35% |
| Stablecoin supply | 13,518,061,358.00 | 13,335,674,953.00 | -1.35% |
| 24h DEX volume | 1,652,785,326.76 | 1,477,920,816.80 | -10.58% |
| 24h chain fees | 7,654,322.42 | 7,164,291.62 | -6.40% |

### Change over 7d (vs run at 2026-11-18T23:39:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,148.25 | 1,883.14 | -12.34% |
| Average non-vote TPS | 2,148.25 | 1,883.14 | -12.34% |
| Average slot time (ms) | 215.30 | 215.20 | -0.05% |
| Active validators | 660.00 | 655.00 | -0.76% |
| Delinquent validators | 25.00 | 33.00 | +32.00% |
| Solana TVL | 4,729,553,664.00 | 4,594,999,475.00 | -2.84% |
| SOL price | 73.41 | 70.92 | -3.39% |
| Stablecoin supply | 13,976,223,818.00 | 13,335,674,953.00 | -4.58% |
| 24h DEX volume | 1,509,645,641.17 | 1,477,920,816.80 | -2.10% |
| 24h chain fees | 8,200,783.62 | 7,164,291.62 | -12.64% |

### Change over 30d (vs run at 2026-10-26T21:59:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,853.07 | 1,883.14 | +1.62% |
| Average non-vote TPS | 1,853.06 | 1,883.14 | +1.62% |
| Average slot time (ms) | 211.90 | 215.20 | +1.56% |
| Active validators | 665.00 | 655.00 | -1.50% |
| Delinquent validators | 20.00 | 33.00 | +65.00% |
| Solana TVL | 5,710,299,220.00 | 4,594,999,475.00 | -19.53% |
| SOL price | 100.45 | 70.92 | -29.40% |
| Stablecoin supply | 15,849,510,602.00 | 13,335,674,953.00 | -15.86% |
| 24h DEX volume | 1,449,231,950.27 | 1,477,920,816.80 | +1.98% |
| 24h chain fees | 9,292,855.03 | 7,164,291.62 | -22.91% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 52.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
