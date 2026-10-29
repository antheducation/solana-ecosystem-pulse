# Solana Ecosystem Pulse

**Generated:** 2026-10-29T03:08:46Z · **Schema:** `1.0.0` · **Collection time:** 18.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.93 | -1.51% |
| Market cap | $58.95B | rank #7 |
| Total value locked | $5.74B | +0.22% |
| Stablecoin supply | $15.69B | -0.61% |
| DEX volume (24h) | $1.62B | +2.63% |
| Chain fees / REV (24h) | $10.35M | -7.85% |
| Non-vote TPS (1h avg) | 1,833 | peak 3,590 total |
| Active validators | 665 | 24 delinquent |
| Epoch 1071 | 12.00% complete | 380,175 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 126 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,832.75 sits 3.8 sigma below the median of the last 126 runs (4,464.22, -58.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,832.8 average over the last 60 minutes; 1,326.8 in the latest sample.
- **Total TPS:** 1,832.8 average, 3,590.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.0 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 440,747,410 at absolute slot 462,723,825.
- **Epoch 1071:** slot 51,825 of 432,000 (12.00% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.581% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 176 ms |
| `solana-rpc.publicnode.com` | yes | 351 ms |
| `api.mainnet.solana.com` | yes | 84 ms |

## Validators & stake

- **665 active** validators, **24 delinquent** (3.48% by count, 0.743% by stake).
- **Total stake:** 436,776,187 SOL ($43.65B); stake rate 68.61% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.71% and top 33 hold 46.40% of active stake.
- **Commission:** median 5.0%, mean 12.62%; 229 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,028,574 | 3.928% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,665,444 | 3.844% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,878,826 | 2.971% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,762,073 | 2.482% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,705,356 | 2.239% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,646 | 2.184% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,110 | 2.126% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,761,555 | 1.790% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,998,037 | 1.614% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,646,428 | 1.533% | 5% |

## Economics

- **SOL:** $99.93 (-1.51% 24h, -5.24% 7d, -14.52% 30d). Market cap $58.95B, 24h volume $2.84B (4.82% of cap). Price source: `coingecko`.
- **TVL:** $5.74B across 336 protocols - rank #4 of 420 chains, 6.47% of all tracked chain TVL. -4.33% over 7d, -55.7% from its ATH.
- **Stablecoins:** $15.69B circulating on Solana (-2.86% 7d) - $2.74 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.62B in 24h, $11.49B over 7d across 139 venues. Volume/TVL turnover 0.283x per day.
- **REV (chain fees):** $10.35M in 24h, $410.20M over 30d. Retained chain revenue $3.83M (37.0% of fees). Annualised fees are 6.41% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,983,924 SOL circulating of 636,639,478 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | +0.2% | -4.2% |
| 2 | Kamino Lend | Lending | $1.27B | -0.0% | -5.3% |
| 3 | Raydium AMM | Dexs | $1.15B | +0.2% | -3.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | +1.6% | -1.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.05B | -0.9% | -6.1% |
| 6 | Jupiter Lend | Lending | $1.01B | -0.9% | -4.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $719.18M | -0.1% | -3.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $532.53M | -0.1% | -5.3% |
| 9 | Sentora Curator | Risk Curators | $383.74M | -0.0% | -8.0% |
| 10 | Marinade Native | Staking Pool | $366.96M | +1.1% | -4.8% |
| 11 | PumpSwap | Dexs | $343.95M | +3.0% | -3.2% |
| 12 | OnRe | RWA | $305.62M | +1.4% | +3.7% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 336 protocols the total is $15.50B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.4% · Dexs 15.2% · Derivatives 5.1% · RWA 3.8% · Risk Curators 3.7%

### Tokenised assets

$860.92M of tokenised real-world assets and equities are locked on Solana - 5.553% of chain TVL.

- OnRe (RWA): $305.62M
- Huma (RWA): $244.90M
- Solstice (Basis Trading): $201.53M
- JupUSD (Basis Trading): $42.98M
- Plume Vaults (RWA): $35.03M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | pre-release |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-28
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-28
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-28T02:47:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,716.48 | 1,832.75 | +6.77% |
| Average non-vote TPS | 1,716.48 | 1,832.75 | +6.77% |
| Average slot time (ms) | 213.20 | 214.00 | +0.38% |
| Active validators | 662.00 | 665.00 | +0.45% |
| Delinquent validators | 29.00 | 24.00 | -17.24% |
| Solana TVL | 5,734,907,585.00 | 5,735,222,416.00 | +0.01% |
| SOL price | 101.49 | 99.93 | -1.54% |
| Stablecoin supply | 15,779,317,711.00 | 15,688,097,062.00 | -0.58% |
| 24h DEX volume | 1,848,988,925.55 | 1,624,511,734.06 | -12.14% |
| 24h chain fees | 11,083,243.89 | 10,348,131.32 | -6.63% |

### Change over 7d (vs run at 2026-10-22T02:09:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,987.14 | 1,832.75 | -7.77% |
| Average non-vote TPS | 1,987.14 | 1,832.75 | -7.77% |
| Average slot time (ms) | 212.40 | 214.00 | +0.75% |
| Active validators | 668.00 | 665.00 | -0.45% |
| Delinquent validators | 9.00 | 24.00 | +166.67% |
| Solana TVL | 6,031,824,201.00 | 5,735,222,416.00 | -4.92% |
| SOL price | 105.97 | 99.93 | -5.70% |
| Stablecoin supply | 16,153,982,880.00 | 15,688,097,062.00 | -2.88% |
| 24h DEX volume | 2,278,261,933.37 | 1,624,511,734.06 | -28.70% |
| 24h chain fees | 11,875,251.66 | 10,348,131.32 | -12.86% |

### Change over 30d (vs run at 2026-09-28T22:41:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,519.28 | 1,832.75 | -59.45% |
| Average non-vote TPS | 2,010.42 | 1,832.75 | -8.84% |
| Average slot time (ms) | 267.20 | 214.00 | -19.91% |
| Active validators | 674.00 | 665.00 | -1.34% |
| Delinquent validators | 8.00 | 24.00 | +200.00% |
| Solana TVL | 6,552,189,378.00 | 5,735,222,416.00 | -12.47% |
| SOL price | 118.18 | 99.93 | -15.44% |
| Stablecoin supply | 16,723,366,837.00 | 15,688,097,062.00 | -6.19% |
| 24h DEX volume | 1,926,466,128.71 | 1,624,511,734.06 | -15.67% |
| 24h chain fees | 15,421,946.25 | 10,348,131.32 | -32.90% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
