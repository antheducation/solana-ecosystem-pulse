# Solana Ecosystem Pulse

**Generated:** 2026-10-30T17:20:22Z · **Schema:** `1.0.0` · **Collection time:** 23.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.83 | -6.65% |
| Market cap | $55.96B | rank #7 |
| Total value locked | $5.34B | -6.67% |
| Stablecoin supply | $15.45B | -1.46% |
| DEX volume (24h) | $2.30B | +32.42% |
| Chain fees / REV (24h) | $12.33M | +16.95% |
| Non-vote TPS (1h avg) | 2,113 | peak 3,156 total |
| Active validators | 667 | 24 delinquent |
| Epoch 1072 | 60.91% complete | 168,869 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL moved sharply (down 6.7% in 24h) | Solana TVL changed -6.7% over the last day, past the 6% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,113.3 average over the last 60 minutes; 2,115.1 in the latest sample.
- **Total TPS:** 2,113.3 average, 3,155.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 441,389,443 at absolute slot 463,367,131.
- **Epoch 1072:** slot 263,131 of 432,000 (60.91% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.579% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 227 ms |
| `solana-rpc.publicnode.com` | yes | 196 ms |
| `api.mainnet.solana.com` | yes | 146 ms |

## Validators & stake

- **667 active** validators, **24 delinquent** (3.47% by count, 0.623% by stake).
- **Total stake:** 435,357,093 SOL ($41.28B); stake rate 68.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.36% of active stake.
- **Commission:** median 5.0%, mean 13.03%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,965,456 | 3.921% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,678,000 | 3.855% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,919,680 | 2.986% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,502,229 | 2.427% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,659,910 | 2.233% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,473,552 | 2.190% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,406 | 2.132% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,780,140 | 1.798% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,045,150 | 1.628% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,506 | 1.618% | 0% |

## Economics

- **SOL:** $94.83 (-6.65% 24h, -9.29% 7d, -21.16% 30d). Market cap $55.96B, 24h volume $5.88B (10.51% of cap). Price source: `coingecko`.
- **TVL:** $5.34B across 335 protocols - rank #5 of 420 chains, 6.38% of all tracked chain TVL. -9.08% over 7d, -58.7% from its ATH.
- **Stablecoins:** $15.45B circulating on Solana (-3.09% 7d) - $2.89 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.30B in 24h, $12.55B over 7d across 139 venues. Volume/TVL turnover 0.430x per day.
- **REV (chain fees):** $12.33M in 24h, $411.80M over 30d. Retained chain revenue $3.87M (31.4% of fees). Annualised fees are 8.04% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,039,793 SOL circulating of 636,700,188 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.68B | -7.2% | -7.3% |
| 2 | Kamino Lend | Lending | $1.18B | -6.6% | -9.7% |
| 3 | Raydium AMM | Dexs | $1.08B | -4.6% | -8.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.02B | -7.7% | -6.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $989.06M | -7.3% | -8.2% |
| 6 | Jupiter Lend | Lending | $896.56M | -10.1% | -13.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $689.08M | -4.4% | -5.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $487.07M | -8.9% | -10.1% |
| 9 | Sentora Curator | Risk Curators | $376.79M | -1.9% | -9.9% |
| 10 | Marinade Native | Staking Pool | $342.64M | -7.3% | -7.8% |
| 11 | PumpSwap | Dexs | $324.75M | -4.5% | -6.6% |
| 12 | OnRe | RWA | $304.25M | -0.4% | +3.1% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 335 protocols the total is $14.53B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 16.0% · Dexs 15.3% · Derivatives 5.2% · RWA 4.2% · Risk Curators 3.8%

### Tokenised assets

$873.00M of tokenised real-world assets and equities are locked on Solana - 6.010% of chain TVL.

- OnRe (RWA): $304.25M
- Huma (RWA): $262.56M
- Solstice (Basis Trading): $201.30M
- JupUSD (Basis Trading): $38.86M
- Plume Vaults (RWA): $35.34M

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

- [SIMD-0529: rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-30
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

### Change over 24h (vs run at 2026-10-29T17:41:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,470.58 | 2,113.28 | -14.46% |
| Average non-vote TPS | 2,470.58 | 2,113.28 | -14.46% |
| Average slot time (ms) | 214.60 | 214.30 | -0.14% |
| Active validators | 666.00 | 667.00 | +0.15% |
| Delinquent validators | 23.00 | 24.00 | +4.35% |
| Solana TVL | 5,700,318,430.00 | 5,343,971,727.00 | -6.25% |
| SOL price | 101.39 | 94.83 | -6.47% |
| Stablecoin supply | 15,690,765,268.00 | 15,451,804,518.00 | -1.52% |
| 24h DEX volume | 1,733,397,982.06 | 2,295,364,281.70 | +32.42% |
| 24h chain fees | 10,347,405.24 | 12,329,690.27 | +19.16% |

### Change over 7d (vs run at 2026-10-23T16:00:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,333.57 | 2,113.28 | -9.44% |
| Average non-vote TPS | 2,333.57 | 2,113.28 | -9.44% |
| Average slot time (ms) | 211.90 | 214.30 | +1.13% |
| Active validators | 656.00 | 667.00 | +1.68% |
| Delinquent validators | 20.00 | 24.00 | +20.00% |
| Solana TVL | 5,864,633,004.00 | 5,343,971,727.00 | -8.88% |
| SOL price | 104.63 | 94.83 | -9.37% |
| Stablecoin supply | 15,964,212,870.00 | 15,451,804,518.00 | -3.21% |
| 24h DEX volume | 2,039,384,832.23 | 2,295,364,281.70 | +12.55% |
| 24h chain fees | 11,291,169.22 | 12,329,690.27 | +9.20% |

### Change over 30d (vs run at 2026-09-30T21:35:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,839.95 | 2,113.28 | -56.34% |
| Average non-vote TPS | 2,344.25 | 2,113.28 | -9.85% |
| Average slot time (ms) | 268.00 | 214.30 | -20.04% |
| Active validators | 672.00 | 667.00 | -0.74% |
| Delinquent validators | 11.00 | 24.00 | +118.18% |
| Solana TVL | 6,529,687,399.00 | 5,343,971,727.00 | -18.16% |
| SOL price | 117.96 | 94.83 | -19.61% |
| Stablecoin supply | 16,483,355,698.00 | 15,451,804,518.00 | -6.26% |
| 24h DEX volume | 2,534,187,471.84 | 2,295,364,281.70 | -9.42% |
| 24h chain fees | 14,686,283.17 | 12,329,690.27 | -16.05% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 23.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
