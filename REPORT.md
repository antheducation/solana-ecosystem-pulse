# Solana Ecosystem Pulse

**Generated:** 2026-10-29T11:52:26Z · **Schema:** `1.0.0` · **Collection time:** 21.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.38 | -2.32% |
| Market cap | $59.21B | rank #7 |
| Total value locked | $5.65B | -1.30% |
| Stablecoin supply | $15.69B | -0.60% |
| DEX volume (24h) | $1.73B | +9.50% |
| Chain fees / REV (24h) | $10.35M | -7.86% |
| Non-vote TPS (1h avg) | 1,332 | peak 1,825 total |
| Active validators | 666 | 23 delinquent |
| Epoch 1071 | 46.05% complete | 233,044 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 127 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,332; the healthy floor used here is 1,500. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,331.86 sits 4.4 sigma below the median of the last 127 runs (4,455.53, -70.1%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,331.9 average over the last 60 minutes; 1,423.4 in the latest sample.
- **Total TPS:** 1,331.9 average, 1,824.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.0 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 440,894,419 at absolute slot 462,870,956.
- **Epoch 1071:** slot 198,956 of 432,000 (46.05% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.581% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 178 ms |
| `solana-rpc.publicnode.com` | yes | 123 ms |
| `api.mainnet.solana.com` | yes | 390 ms |

## Validators & stake

- **666 active** validators, **23 delinquent** (3.34% by count, 0.737% by stake).
- **Total stake:** 436,776,187 SOL ($43.84B); stake rate 68.61% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.71% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 230 validators at 0% and 63 at 100%.

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

- **SOL:** $100.38 (-2.32% 24h, -3.90% 7d, -15.93% 30d). Market cap $59.21B, 24h volume $2.80B (4.73% of cap). Price source: `coingecko`.
- **TVL:** $5.65B across 336 protocols - rank #4 of 420 chains, 6.42% of all tracked chain TVL. -5.75% over 7d, -56.3% from its ATH.
- **Stablecoins:** $15.69B circulating on Solana (-2.86% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.73B in 24h, $12.30B over 7d across 139 venues. Volume/TVL turnover 0.307x per day.
- **REV (chain fees):** $10.35M in 24h, $416.82M over 30d. Retained chain revenue $3.85M (37.3% of fees). Annualised fees are 6.38% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,983,817 SOL circulating of 636,639,371 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.77B | -2.7% | -5.8% |
| 2 | Kamino Lend | Lending | $1.26B | -1.5% | -6.1% |
| 3 | Raydium AMM | Dexs | $1.12B | -2.4% | -5.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.08B | -1.9% | -3.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.05B | -2.6% | -6.4% |
| 6 | Jupiter Lend | Lending | $992.56M | -3.3% | -5.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $708.36M | -2.2% | -5.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $521.70M | -3.0% | -7.2% |
| 9 | Sentora Curator | Risk Curators | $383.74M | -0.0% | -8.0% |
| 10 | Marinade Native | Staking Pool | $360.48M | -2.3% | -6.4% |
| 11 | PumpSwap | Dexs | $337.18M | -2.4% | -5.1% |
| 12 | OnRe | RWA | $305.43M | +1.4% | +3.6% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 336 protocols the total is $15.30B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.4% · Dexs 15.1% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$861.98M of tokenised real-world assets and equities are locked on Solana - 5.633% of chain TVL.

- OnRe (RWA): $305.43M
- Huma (RWA): $246.05M
- Solstice (Basis Trading): $201.54M
- JupUSD (Basis Trading): $43.09M
- Plume Vaults (RWA): $35.03M

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

- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-29
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-28
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

### Change over 24h (vs run at 2026-10-28T11:44:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,323.46 | 1,331.86 | +0.63% |
| Average non-vote TPS | 1,323.46 | 1,331.86 | +0.63% |
| Average slot time (ms) | 212.60 | 214.00 | +0.66% |
| Active validators | 662.00 | 666.00 | +0.60% |
| Delinquent validators | 29.00 | 23.00 | -20.69% |
| Solana TVL | 5,789,213,551.00 | 5,646,734,237.00 | -2.46% |
| SOL price | 102.71 | 100.38 | -2.27% |
| Stablecoin supply | 15,780,319,313.00 | 15,688,764,724.00 | -0.58% |
| 24h DEX volume | 1,582,952,703.63 | 1,733,397,982.06 | +9.50% |
| 24h chain fees | 10,908,125.93 | 10,346,775.24 | -5.15% |

### Change over 7d (vs run at 2026-10-22T10:44:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,731.38 | 1,331.86 | -23.08% |
| Average non-vote TPS | 1,731.38 | 1,331.86 | -23.08% |
| Average slot time (ms) | 211.10 | 214.00 | +1.37% |
| Active validators | 668.00 | 666.00 | -0.30% |
| Delinquent validators | 9.00 | 23.00 | +155.56% |
| Solana TVL | 5,896,494,807.00 | 5,646,734,237.00 | -4.24% |
| SOL price | 104.58 | 100.38 | -4.02% |
| Stablecoin supply | 16,155,037,927.00 | 15,688,764,724.00 | -2.89% |
| 24h DEX volume | 2,257,983,009.37 | 1,733,397,982.06 | -23.23% |
| 24h chain fees | 11,864,192.66 | 10,346,775.24 | -12.79% |

### Change over 30d (vs run at 2026-09-29T21:34:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,737.06 | 1,331.86 | -71.88% |
| Average non-vote TPS | 2,239.20 | 1,331.86 | -40.52% |
| Average slot time (ms) | 268.60 | 214.00 | -20.33% |
| Active validators | 673.00 | 666.00 | -1.04% |
| Delinquent validators | 10.00 | 23.00 | +130.00% |
| Solana TVL | 6,522,003,878.00 | 5,646,734,237.00 | -13.42% |
| SOL price | 118.62 | 100.38 | -15.38% |
| Stablecoin supply | 16,661,913,603.00 | 15,688,764,724.00 | -5.84% |
| 24h DEX volume | 2,662,061,803.25 | 1,733,397,982.06 | -34.89% |
| 24h chain fees | 17,514,749.35 | 10,346,775.24 | -40.93% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 21.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
