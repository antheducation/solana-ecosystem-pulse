# Solana Ecosystem Pulse

**Generated:** 2026-11-02T13:58:36Z · **Schema:** `1.0.0` · **Collection time:** 16.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $94.34 | -0.41% |
| Market cap | $55.68B | rank #7 |
| Total value locked | $5.47B | +0.65% |
| Stablecoin supply | $15.44B | -0.43% |
| DEX volume (24h) | $905.60M | -5.03% |
| Chain fees / REV (24h) | $8.40M | +1.49% |
| Non-vote TPS (1h avg) | 1,736 | peak 2,984 total |
| Active validators | 666 | 28 delinquent |
| Epoch 1075 | 27.92% complete | 311,407 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,735.9 average over the last 60 minutes; 1,601.9 in the latest sample.
- **Total TPS:** 1,735.9 average, 2,983.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.1 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 442,541,740 at absolute slot 464,520,593.
- **Epoch 1075:** slot 120,593 of 432,000 (27.92% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.575% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 108 ms |
| `solana-rpc.publicnode.com` | yes | 47 ms |
| `api.mainnet.solana.com` | yes | 59 ms |

## Validators & stake

- **666 active** validators, **28 delinquent** (4.03% by count, 1.011% by stake).
- **Total stake:** 434,161,055 SOL ($40.96B); stake rate 68.17% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.96% and top 33 hold 46.73% of active stake.
- **Commission:** median 5.0%, mean 12.65%; 226 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,034,354 | 3.964% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,710,199 | 3.888% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,037,180 | 3.034% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,429,501 | 2.427% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,109 | 2.229% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,453,055 | 2.200% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,805 | 2.147% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,803,392 | 1.816% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,891 | 1.629% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,978,080 | 1.624% | 5% |

## Economics

- **SOL:** $94.34 (-0.41% 24h, -7.08% 7d, -21.04% 30d). Market cap $55.68B, 24h volume $2.16B (3.88% of cap). Price source: `coingecko`.
- **TVL:** $5.47B across 334 protocols - rank #4 of 420 chains, 6.41% of all tracked chain TVL. -4.36% over 7d, -57.7% from its ATH.
- **Stablecoins:** $15.44B circulating on Solana (-2.57% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $905.60M in 24h, $11.66B over 7d across 141 venues. Volume/TVL turnover 0.166x per day.
- **REV (chain fees):** $8.40M in 24h, $381.60M over 30d. Retained chain revenue $3.12M (37.2% of fees). Annualised fees are 5.50% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,205,899 SOL circulating of 636,883,534 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.64B | -1.3% | -7.7% |
| 2 | Kamino Lend | Lending | $1.23B | +0.2% | -2.8% |
| 3 | Raydium AMM | Dexs | $1.05B | -1.3% | -7.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.02B | -1.2% | -4.5% |
| 5 | Jupiter Lend | Lending | $1.00B | +8.0% | -0.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $970.87M | -0.8% | -8.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $688.49M | -0.2% | -3.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $477.42M | -0.5% | -10.0% |
| 9 | Sentora Curator | Risk Curators | $377.29M | +0.2% | -2.6% |
| 10 | Marinade Native | Staking Pool | $339.02M | -0.4% | -6.9% |
| 11 | PumpSwap | Dexs | $320.18M | -1.5% | -5.0% |
| 12 | OnRe | RWA | $307.29M | -0.2% | +4.0% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 334 protocols the total is $14.53B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 17.1% · Dexs 15.2% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.8%

### Tokenised assets

$858.54M of tokenised real-world assets and equities are locked on Solana - 5.908% of chain TVL.

- OnRe (RWA): $307.29M
- Huma (RWA): $245.26M
- Solstice (Basis Trading): $201.40M
- JupUSD (Basis Trading): $38.87M
- Plume Vaults (RWA): $35.57M

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
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
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

### Change over 24h (vs run at 2026-11-01T12:10:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,168.26 | 1,735.94 | +48.59% |
| Average non-vote TPS | 1,168.26 | 1,735.94 | +48.59% |
| Average slot time (ms) | 214.10 | 215.10 | +0.47% |
| Active validators | 662.00 | 666.00 | +0.60% |
| Delinquent validators | 34.00 | 28.00 | -17.65% |
| Solana TVL | 5,439,557,393.00 | 5,468,197,763.00 | +0.53% |
| SOL price | 95.29 | 94.34 | -1.00% |
| Stablecoin supply | 15,513,662,767.00 | 15,442,364,185.00 | -0.46% |
| 24h DEX volume | 953,373,035.19 | 905,602,298.19 | -5.01% |
| 24h chain fees | 8,275,921.37 | 8,395,340.05 | +1.44% |

### Change over 7d (vs run at 2026-10-26T11:41:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,478.31 | 1,735.94 | +17.43% |
| Average non-vote TPS | 1,478.31 | 1,735.94 | +17.43% |
| Average slot time (ms) | 211.90 | 215.10 | +1.51% |
| Active validators | 665.00 | 666.00 | +0.15% |
| Delinquent validators | 25.00 | 28.00 | +12.00% |
| Solana TVL | 5,740,388,903.00 | 5,468,197,763.00 | -4.74% |
| SOL price | 101.37 | 94.34 | -6.93% |
| Stablecoin supply | 15,877,222,933.00 | 15,442,364,185.00 | -2.74% |
| 24h DEX volume | 1,449,231,950.27 | 905,602,298.19 | -37.51% |
| 24h chain fees | 9,299,425.03 | 8,395,340.05 | -9.72% |

### Change over 30d (vs run at 2026-10-03T20:17:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,907.58 | 1,735.94 | -64.63% |
| Average non-vote TPS | 2,415.29 | 1,735.94 | -28.13% |
| Average slot time (ms) | 267.60 | 215.10 | -19.62% |
| Active validators | 670.00 | 666.00 | -0.60% |
| Delinquent validators | 15.00 | 28.00 | +86.67% |
| Solana TVL | 6,664,651,516.00 | 5,468,197,763.00 | -17.95% |
| SOL price | 119.93 | 94.34 | -21.34% |
| Stablecoin supply | 16,950,775,065.00 | 15,442,364,185.00 | -8.90% |
| 24h DEX volume | 2,760,296,309.96 | 905,602,298.19 | -67.19% |
| 24h chain fees | 17,402,246.04 | 8,395,340.05 | -51.76% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 16.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
