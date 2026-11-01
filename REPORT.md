# Solana Ecosystem Pulse

**Generated:** 2026-11-01T12:10:11Z · **Schema:** `1.0.0` · **Collection time:** 20.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $95.29 | -0.54% |
| Market cap | $56.23B | rank #7 |
| Total value locked | $5.44B | -0.73% |
| Stablecoin supply | $15.51B | +0.12% |
| DEX volume (24h) | $953.37M | -54.97% |
| Chain fees / REV (24h) | $8.28M | -26.33% |
| Non-vote TPS (1h avg) | 1,168 | peak 1,542 total |
| Active validators | 662 | 34 delinquent |
| Epoch 1074 | 27.55% complete | 312,981 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,168; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 55.0% in 24h) | DEX volume changed -55.0% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,168.26 sits 3.2 sigma below the median of the last 130 runs (4,275.67, -72.7%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 34.00 sits 4.9 sigma above the median of the last 130 runs (12.00, +183.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,168.3 average over the last 60 minutes; 1,003.7 in the latest sample.
- **Total TPS:** 1,168.3 average, 1,541.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.1 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 442,108,526 at absolute slot 464,087,019.
- **Epoch 1074:** slot 119,019 of 432,000 (27.55% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.576% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 282 ms |
| `solana-rpc.publicnode.com` | yes | 171 ms |
| `api.mainnet.solana.com` | yes | 148 ms |

## Validators & stake

- **662 active** validators, **34 delinquent** (4.89% by count, 1.050% by stake).
- **Total stake:** 433,943,288 SOL ($41.35B); stake rate 68.14% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.95% and top 33 hold 46.66% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 225 validators at 0% and 63 at 100%.

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

- **SOL:** $95.29 (-0.54% 24h, -5.87% 7d, -21.80% 30d). Market cap $56.23B, 24h volume $1.18B (2.10% of cap). Price source: `coingecko`.
- **TVL:** $5.44B across 334 protocols - rank #4 of 420 chains, 6.37% of all tracked chain TVL. -6.07% over 7d, -57.9% from its ATH.
- **Stablecoins:** $15.51B circulating on Solana (-2.49% 7d) - $2.85 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $953.37M in 24h, $12.20B over 7d across 139 venues. Volume/TVL turnover 0.175x per day.
- **REV (chain fees):** $8.28M in 24h, $393.65M over 30d. Retained chain revenue $2.75M (33.3% of fees). Annualised fees are 5.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,150,451 SOL circulating of 636,822,241 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.67B | -0.5% | -6.7% |
| 2 | Kamino Lend | Lending | $1.23B | -0.1% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.07B | -0.5% | -7.7% |
| 4 | Binance Staked SOL | Liquid Staking | $1.03B | -0.3% | -4.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $984.06M | -0.5% | -7.7% |
| 6 | Jupiter Lend | Lending | $929.01M | +0.0% | -9.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $692.29M | -0.2% | -4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $483.73M | -1.0% | -9.7% |
| 9 | Sentora Curator | Risk Curators | $376.42M | +0.2% | -5.2% |
| 10 | Marinade Native | Staking Pool | $342.39M | -0.1% | -6.9% |
| 11 | PumpSwap | Dexs | $324.94M | -0.3% | -5.1% |
| 12 | OnRe | RWA | $307.76M | +0.0% | +4.2% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.60B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 16.6% · Dexs 15.2% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.7%

### Tokenised assets

$858.79M of tokenised real-world assets and equities are locked on Solana - 5.883% of chain TVL.

- OnRe (RWA): $307.76M
- Huma (RWA): $245.22M
- Solstice (Basis Trading): $201.54M
- JupUSD (Basis Trading): $38.89M
- Plume Vaults (RWA): $35.12M

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

- [SIMD-0529: rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-31
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

### Change over 24h (vs run at 2026-10-31T11:19:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 991.93 | 1,168.26 | +17.78% |
| Average non-vote TPS | 991.93 | 1,168.26 | +17.78% |
| Average slot time (ms) | 213.70 | 214.10 | +0.19% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 27.00 | 34.00 | +25.93% |
| Solana TVL | 5,443,490,761.00 | 5,439,557,393.00 | -0.07% |
| SOL price | 95.67 | 95.29 | -0.40% |
| Stablecoin supply | 15,491,130,492.00 | 15,513,662,767.00 | +0.15% |
| 24h DEX volume | 2,117,396,479.19 | 953,373,035.19 | -54.97% |
| 24h chain fees | 11,223,116.43 | 8,275,921.37 | -26.26% |

### Change over 7d (vs run at 2026-10-25T10:16:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,206.01 | 1,168.26 | -3.13% |
| Average non-vote TPS | 1,206.01 | 1,168.26 | -3.13% |
| Average slot time (ms) | 212.20 | 214.10 | +0.90% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 25.00 | 34.00 | +36.00% |
| Solana TVL | 5,778,836,045.00 | 5,439,557,393.00 | -5.87% |
| SOL price | 100.82 | 95.29 | -5.49% |
| Stablecoin supply | 15,930,791,568.00 | 15,513,662,767.00 | -2.62% |
| 24h DEX volume | 1,732,393,737.80 | 953,373,035.19 | -44.97% |
| 24h chain fees | 9,945,781.91 | 8,275,921.37 | -16.79% |

### Change over 30d (vs run at 2026-10-02T21:29:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,922.79 | 1,168.26 | -76.27% |
| Average non-vote TPS | 2,432.94 | 1,168.26 | -51.98% |
| Average slot time (ms) | 268.50 | 214.10 | -20.26% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 13.00 | 34.00 | +161.54% |
| Solana TVL | 6,606,723,520.00 | 5,439,557,393.00 | -17.67% |
| SOL price | 117.81 | 95.29 | -19.12% |
| Stablecoin supply | 16,579,831,390.00 | 15,513,662,767.00 | -6.43% |
| 24h DEX volume | 2,488,460,102.88 | 953,373,035.19 | -61.69% |
| 24h chain fees | 17,134,431.63 | 8,275,921.37 | -51.70% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.9s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
