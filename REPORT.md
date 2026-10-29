# Solana Ecosystem Pulse

**Generated:** 2026-10-29T17:41:22Z · **Schema:** `1.0.0` · **Collection time:** 17.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.39 | +0.29% |
| Market cap | $59.84B | rank #7 |
| Total value locked | $5.70B | -0.21% |
| Stablecoin supply | $15.69B | -0.59% |
| DEX volume (24h) | $1.73B | +9.50% |
| Chain fees / REV (24h) | $10.35M | -7.89% |
| Non-vote TPS (1h avg) | 2,471 | peak 4,001 total |
| Active validators | 666 | 23 delinquent |
| Epoch 1071 | 68.70% complete | 135,237 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 127 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,470.6 average over the last 60 minutes; 2,910.3 in the latest sample.
- **Total TPS:** 2,470.6 average, 4,001.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.6 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 440,992,115 at absolute slot 462,968,763.
- **Epoch 1071:** slot 296,763 of 432,000 (68.70% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.581% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 99 ms |
| `solana-rpc.publicnode.com` | yes | 149 ms |
| `api.mainnet.solana.com` | yes | 57 ms |

## Validators & stake

- **666 active** validators, **23 delinquent** (3.34% by count, 0.737% by stake).
- **Total stake:** 436,776,187 SOL ($44.28B); stake rate 68.61% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.71% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 13.04%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,028,574 | 3.928% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,665,444 | 3.844% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,878,826 | 2.971% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,762,073 | 2.482% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,705,356 | 2.239% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,646 | 2.183% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,110 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,761,555 | 1.790% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,998,037 | 1.614% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,646,428 | 1.533% | 5% |

## Economics

- **SOL:** $101.39 (+0.29% 24h, -2.15% 7d, -14.11% 30d). Market cap $59.84B, 24h volume $3.16B (5.28% of cap). Price source: `coingecko`.
- **TVL:** $5.70B across 336 protocols - rank #4 of 420 chains, 6.40% of all tracked chain TVL. -4.71% over 7d, -55.8% from its ATH.
- **Stablecoins:** $15.69B circulating on Solana (-2.84% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.73B in 24h, $12.30B over 7d across 139 venues. Volume/TVL turnover 0.304x per day.
- **REV (chain fees):** $10.35M in 24h, $416.82M over 30d. Retained chain revenue $3.86M (37.3% of fees). Annualised fees are 6.31% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,983,697 SOL circulating of 636,639,251 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +1.4% | -3.7% |
| 2 | Kamino Lend | Lending | $1.27B | +0.4% | -5.0% |
| 3 | Raydium AMM | Dexs | $1.13B | -0.7% | -5.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.11B | +1.6% | -1.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.07B | +1.6% | -4.4% |
| 6 | Jupiter Lend | Lending | $997.44M | -1.4% | -5.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $720.97M | +0.8% | -3.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $532.36M | +0.8% | -5.3% |
| 9 | Sentora Curator | Risk Curators | $383.93M | +0.0% | -7.9% |
| 10 | Marinade Native | Staking Pool | $369.69M | +2.1% | -4.0% |
| 11 | PumpSwap | Dexs | $339.86M | +0.4% | -4.3% |
| 12 | OnRe | RWA | $305.23M | +1.3% | +3.5% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 336 protocols the total is $15.53B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.3% · Lending 16.3% · Dexs 15.0% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$862.35M of tokenised real-world assets and equities are locked on Solana - 5.553% of chain TVL.

- OnRe (RWA): $305.23M
- Huma (RWA): $246.05M
- Solstice (Basis Trading): $201.57M
- JupUSD (Basis Trading): $43.10M
- Plume Vaults (RWA): $35.55M

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

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-29
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-29
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-28T17:30:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,016.09 | 2,470.58 | +22.54% |
| Average non-vote TPS | 2,016.09 | 2,470.58 | +22.54% |
| Average slot time (ms) | 212.60 | 214.60 | +0.94% |
| Active validators | 661.00 | 666.00 | +0.76% |
| Delinquent validators | 30.00 | 23.00 | -23.33% |
| Solana TVL | 5,729,261,190.00 | 5,700,318,430.00 | -0.51% |
| SOL price | 100.93 | 101.39 | +0.46% |
| Stablecoin supply | 15,780,943,599.00 | 15,690,765,268.00 | -0.57% |
| 24h DEX volume | 1,582,952,703.63 | 1,733,397,982.06 | +9.50% |
| 24h chain fees | 10,909,790.93 | 10,347,405.24 | -5.15% |

### Change over 7d (vs run at 2026-10-22T16:10:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,291.15 | 2,470.58 | +7.83% |
| Average non-vote TPS | 2,291.14 | 2,470.58 | +7.83% |
| Average slot time (ms) | 211.10 | 214.60 | +1.66% |
| Active validators | 656.00 | 666.00 | +1.52% |
| Delinquent validators | 20.00 | 23.00 | +15.00% |
| Solana TVL | 5,931,668,789.00 | 5,700,318,430.00 | -3.90% |
| SOL price | 104.58 | 101.39 | -3.05% |
| Stablecoin supply | 16,154,815,750.00 | 15,690,765,268.00 | -2.87% |
| 24h DEX volume | 2,270,402,206.37 | 1,733,397,982.06 | -23.65% |
| 24h chain fees | 11,887,074.66 | 10,347,405.24 | -12.95% |

### Change over 30d (vs run at 2026-09-29T21:34:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,737.06 | 2,470.58 | -47.85% |
| Average non-vote TPS | 2,239.20 | 2,470.58 | +10.33% |
| Average slot time (ms) | 268.60 | 214.60 | -20.10% |
| Active validators | 673.00 | 666.00 | -1.04% |
| Delinquent validators | 10.00 | 23.00 | +130.00% |
| Solana TVL | 6,522,003,878.00 | 5,700,318,430.00 | -12.60% |
| SOL price | 118.62 | 101.39 | -14.53% |
| Stablecoin supply | 16,661,913,603.00 | 15,690,765,268.00 | -5.83% |
| 24h DEX volume | 2,662,061,803.25 | 1,733,397,982.06 | -34.89% |
| 24h chain fees | 17,514,749.35 | 10,347,405.24 | -40.92% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 17.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
