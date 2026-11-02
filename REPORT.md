# Solana Ecosystem Pulse

**Generated:** 2026-11-02T02:58:48Z · **Schema:** `1.0.0` · **Collection time:** 19.2s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.84 | -0.59% |
| Market cap | $55.97B | rank #7 |
| Total value locked | $5.49B | +1.10% |
| Stablecoin supply | $15.44B | -0.42% |
| DEX volume (24h) | $832.67M | -12.68% |
| Chain fees / REV (24h) | $8.43M | +1.96% |
| Non-vote TPS (1h avg) | 1,599 | peak 2,279 total |
| Active validators | 662 | 34 delinquent |
| Epoch 1074 | 85.14% complete | 64,208 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 34.00 sits 3.5 sigma above the median of the last 129 runs (13.00, +161.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,599.0 average over the last 60 minutes; 1,457.7 in the latest sample.
- **Total TPS:** 1,599.0 average, 2,279.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 442,357,179 at absolute slot 464,335,792.
- **Epoch 1074:** slot 367,792 of 432,000 (85.14% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.576% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 128 ms |
| `solana-rpc.publicnode.com` | yes | 179 ms |
| `api.mainnet.solana.com` | yes | 160 ms |

## Validators & stake

- **662 active** validators, **34 delinquent** (4.89% by count, 1.050% by stake).
- **Total stake:** 433,943,288 SOL ($41.16B); stake rate 68.14% of total supply.
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

- **SOL:** $94.84 (-0.59% 24h, -6.07% 7d, -20.37% 30d). Market cap $55.97B, 24h volume $1.78B (3.17% of cap). Price source: `coingecko`.
- **TVL:** $5.49B across 334 protocols - rank #4 of 420 chains, 6.41% of all tracked chain TVL. -3.99% over 7d, -57.5% from its ATH.
- **Stablecoins:** $15.44B circulating on Solana (-2.56% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $832.67M in 24h, $11.18B over 7d across 140 venues. Volume/TVL turnover 0.152x per day.
- **REV (chain fees):** $8.43M in 24h, $381.16M over 30d. Retained chain revenue $3.14M (37.3% of fees). Annualised fees are 5.50% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,150,166 SOL circulating of 636,821,977 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.67B | -0.7% | -6.1% |
| 2 | Kamino Lend | Lending | $1.23B | -0.1% | -2.9% |
| 3 | Raydium AMM | Dexs | $1.07B | -0.6% | -6.3% |
| 4 | Binance Staked SOL | Liquid Staking | $1.04B | +0.2% | -2.9% |
| 5 | Jupiter Lend | Lending | $1.00B | +8.2% | -0.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $982.87M | -0.6% | -6.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $686.97M | -0.9% | -4.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $476.40M | -2.7% | -10.2% |
| 9 | Sentora Curator | Risk Curators | $376.41M | +0.2% | -2.8% |
| 10 | Marinade Native | Staking Pool | $342.63M | -0.2% | -5.9% |
| 11 | PumpSwap | Dexs | $321.17M | -0.7% | -4.7% |
| 12 | OnRe | RWA | $307.80M | +0.0% | +4.1% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.64B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.0% · Dexs 15.2% · Derivatives 5.1% · RWA 4.1% · Risk Curators 3.7%

### Tokenised assets

$858.78M of tokenised real-world assets and equities are locked on Solana - 5.868% of chain TVL.

- OnRe (RWA): $307.80M
- Huma (RWA): $244.96M
- Solstice (Basis Trading): $201.42M
- JupUSD (Basis Trading): $38.88M
- Plume Vaults (RWA): $35.54M

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

- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-02
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

### Change over 24h (vs run at 2026-11-01T02:51:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,387.39 | 1,598.99 | +15.25% |
| Average non-vote TPS | 1,387.39 | 1,598.99 | +15.25% |
| Average slot time (ms) | 214.00 | 214.30 | +0.14% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 27.00 | 34.00 | +25.93% |
| Solana TVL | 5,440,989,525.00 | 5,488,771,465.00 | +0.88% |
| SOL price | 95.46 | 94.84 | -0.65% |
| Stablecoin supply | 15,513,310,673.00 | 15,444,373,984.00 | -0.44% |
| 24h DEX volume | 1,443,069,906.19 | 832,668,894.19 | -42.30% |
| 24h chain fees | 8,582,329.70 | 8,432,926.72 | -1.74% |

### Change over 7d (vs run at 2026-10-26T02:00:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,938.20 | 1,598.99 | -17.50% |
| Average non-vote TPS | 1,938.20 | 1,598.99 | -17.50% |
| Average slot time (ms) | 212.80 | 214.30 | +0.70% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 25.00 | 34.00 | +36.00% |
| Solana TVL | 5,735,902,141.00 | 5,488,771,465.00 | -4.31% |
| SOL price | 100.91 | 94.84 | -6.02% |
| Stablecoin supply | 15,877,624,594.00 | 15,444,373,984.00 | -2.73% |
| 24h DEX volume | 1,348,643,859.27 | 832,668,894.19 | -38.26% |
| 24h chain fees | 10,086,756.26 | 8,432,926.72 | -16.40% |

### Change over 30d (vs run at 2026-10-02T21:29:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,922.79 | 1,598.99 | -67.52% |
| Average non-vote TPS | 2,432.94 | 1,598.99 | -34.28% |
| Average slot time (ms) | 268.50 | 214.30 | -20.19% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 13.00 | 34.00 | +161.54% |
| Solana TVL | 6,606,723,520.00 | 5,488,771,465.00 | -16.92% |
| SOL price | 117.81 | 94.84 | -19.50% |
| Stablecoin supply | 16,579,831,390.00 | 15,444,373,984.00 | -6.85% |
| 24h DEX volume | 2,488,460,102.88 | 832,668,894.19 | -66.54% |
| 24h chain fees | 17,134,431.63 | 8,432,926.72 | -50.78% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 19.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
