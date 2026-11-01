# Solana Ecosystem Pulse

**Generated:** 2026-11-01T21:25:27Z · **Schema:** `1.0.0` · **Collection time:** 23.8s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.18 | -1.56% |
| Market cap | $55.58B | rank #7 |
| Total value locked | $5.39B | -1.57% |
| Stablecoin supply | $15.51B | +0.09% |
| DEX volume (24h) | $953.59M | -54.96% |
| Chain fees / REV (24h) | $8.27M | -26.39% |
| Non-vote TPS (1h avg) | 2,058 | peak 4,579 total |
| Active validators | 662 | 34 delinquent |
| Epoch 1074 | 63.53% complete | 157,567 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 55.0% in 24h) | DEX volume changed -55.0% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 34.00 sits 4.1 sigma above the median of the last 130 runs (12.50, +172.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,058.0 average over the last 60 minutes; 1,701.8 in the latest sample.
- **Total TPS:** 2,058.0 average, 4,578.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.5 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 442,263,883 at absolute slot 464,242,433.
- **Epoch 1074:** slot 274,433 of 432,000 (63.53% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.576% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 251 ms |
| `solana-rpc.publicnode.com` | yes | 182 ms |
| `api.mainnet.solana.com` | yes | 250 ms |

## Validators & stake

- **662 active** validators, **34 delinquent** (4.89% by count, 1.050% by stake).
- **Total stake:** 433,943,288 SOL ($40.87B); stake rate 68.14% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.95% and top 33 hold 46.66% of active stake.
- **Commission:** median 5.0%, mean 13.12%; 223 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,029,196 | 3.966% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,695,127 | 3.888% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,943,199 | 3.014% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,426,987 | 2.428% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,583,157 | 2.232% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,451,197 | 2.201% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,225,053 | 2.148% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,791,639 | 1.815% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,293 | 1.631% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,977,108 | 1.625% | 5% |

## Economics

- **SOL:** $94.18 (-1.56% 24h, -7.26% 7d, -20.02% 30d). Market cap $55.58B, 24h volume $1.45B (2.61% of cap). Price source: `coingecko`.
- **TVL:** $5.39B across 334 protocols - rank #4 of 420 chains, 6.34% of all tracked chain TVL. -6.86% over 7d, -58.3% from its ATH.
- **Stablecoins:** $15.51B circulating on Solana (-2.52% 7d) - $2.88 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $953.59M in 24h, $12.20B over 7d across 139 venues. Volume/TVL turnover 0.177x per day.
- **REV (chain fees):** $8.27M in 24h, $393.66M over 30d. Retained chain revenue $2.75M (33.2% of fees). Annualised fees are 5.43% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,150,285 SOL circulating of 636,822,075 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.64B | -2.1% | -8.2% |
| 2 | Kamino Lend | Lending | $1.22B | -0.7% | -3.3% |
| 3 | Raydium AMM | Dexs | $1.07B | -1.2% | -8.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.02B | -1.4% | -5.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $968.26M | -2.0% | -9.2% |
| 6 | Jupiter Lend | Lending | $924.38M | -0.6% | -10.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $686.06M | -1.1% | -5.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $476.65M | -2.7% | -11.0% |
| 9 | Sentora Curator | Risk Curators | $376.26M | +0.1% | -5.2% |
| 10 | Marinade Native | Staking Pool | $337.66M | -1.8% | -8.2% |
| 11 | PumpSwap | Dexs | $316.30M | -2.3% | -7.6% |
| 12 | OnRe | RWA | $307.66M | -0.0% | +4.1% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 16.6% · Dexs 15.2% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$859.00M of tokenised real-world assets and equities are locked on Solana - 5.946% of chain TVL.

- OnRe (RWA): $307.66M
- Huma (RWA): $245.39M
- Solstice (Basis Trading): $201.40M
- JupUSD (Basis Trading): $38.87M
- Plume Vaults (RWA): $35.53M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0529: rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-30
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-31T20:43:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,655.68 | 2,058.00 | +24.30% |
| Average non-vote TPS | 1,655.68 | 2,058.00 | +24.30% |
| Average slot time (ms) | 214.00 | 214.50 | +0.23% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 27.00 | 34.00 | +25.93% |
| Solana TVL | 5,449,917,859.00 | 5,392,125,548.00 | -1.06% |
| SOL price | 95.56 | 94.18 | -1.44% |
| Stablecoin supply | 15,493,312,766.00 | 15,508,525,506.00 | +0.10% |
| 24h DEX volume | 2,117,396,479.19 | 953,585,251.19 | -54.96% |
| 24h chain fees | 11,233,221.43 | 8,270,455.08 | -26.38% |

### Change over 7d (vs run at 2026-10-25T20:04:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,732.39 | 2,058.00 | +18.80% |
| Average non-vote TPS | 1,732.38 | 2,058.00 | +18.80% |
| Average slot time (ms) | 212.20 | 214.50 | +1.08% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 25.00 | 34.00 | +36.00% |
| Solana TVL | 5,770,053,619.00 | 5,392,125,548.00 | -6.55% |
| SOL price | 101.63 | 94.18 | -7.33% |
| Stablecoin supply | 15,930,366,369.00 | 15,508,525,506.00 | -2.65% |
| 24h DEX volume | 1,423,041,369.80 | 953,585,251.19 | -32.99% |
| 24h chain fees | 10,045,733.76 | 8,270,455.08 | -17.67% |

### Change over 30d (vs run at 2026-10-02T21:29:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,922.79 | 2,058.00 | -58.19% |
| Average non-vote TPS | 2,432.94 | 2,058.00 | -15.41% |
| Average slot time (ms) | 268.50 | 214.50 | -20.11% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 13.00 | 34.00 | +161.54% |
| Solana TVL | 6,606,723,520.00 | 5,392,125,548.00 | -18.38% |
| SOL price | 117.81 | 94.18 | -20.06% |
| Stablecoin supply | 16,579,831,390.00 | 15,508,525,506.00 | -6.46% |
| 24h DEX volume | 2,488,460,102.88 | 953,585,251.19 | -61.68% |
| 24h chain fees | 17,134,431.63 | 8,270,455.08 | -51.73% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.7s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
