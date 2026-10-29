# Solana Ecosystem Pulse

**Generated:** 2026-10-29T22:06:52Z · **Schema:** `1.0.0` · **Collection time:** 29.0s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $97.17 | -5.14% |
| Market cap | $57.34B | rank #7 |
| Total value locked | $5.66B | -1.15% |
| Stablecoin supply | $15.69B | -0.57% |
| DEX volume (24h) | $1.73B | +9.50% |
| Chain fees / REV (24h) | $10.35M | -7.89% |
| Non-vote TPS (1h avg) | 2,733 | peak 4,798 total |
| Active validators | 666 | 23 delinquent |
| Epoch 1071 | 85.92% complete | 60,826 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 127 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,732.8 average over the last 60 minutes; 3,082.1 in the latest sample.
- **Total TPS:** 2,732.8 average, 4,797.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 218.2 ms.
- **Block height:** 441,066,390 at absolute slot 463,043,174.
- **Epoch 1071:** slot 371,174 of 432,000 (85.92% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.581% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 918 ms |
| `solana-rpc.publicnode.com` | yes | 287 ms |
| `api.mainnet.solana.com` | yes | 721 ms |

## Validators & stake

- **666 active** validators, **23 delinquent** (3.34% by count, 0.737% by stake).
- **Total stake:** 436,776,187 SOL ($42.44B); stake rate 68.61% of total supply.
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

- **SOL:** $97.17 (-5.14% 24h, -6.19% 7d, -18.25% 30d). Market cap $57.34B, 24h volume $3.89B (6.79% of cap). Price source: `coingecko`.
- **TVL:** $5.66B across 336 protocols - rank #5 of 420 chains, 6.38% of all tracked chain TVL. -5.61% over 7d, -56.2% from its ATH.
- **Stablecoins:** $15.69B circulating on Solana (-2.82% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.73B in 24h, $12.30B over 7d across 139 venues. Volume/TVL turnover 0.307x per day.
- **REV (chain fees):** $10.35M in 24h, $416.82M over 30d. Retained chain revenue $3.86M (37.3% of fees). Annualised fees are 6.59% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,983,585 SOL circulating of 636,639,139 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.70B | -5.5% | -9.3% |
| 2 | Kamino Lend | Lending | $1.24B | -2.2% | -7.4% |
| 3 | Raydium AMM | Dexs | $1.13B | -1.4% | -5.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.06B | -4.7% | -6.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.02B | -4.3% | -8.9% |
| 6 | Jupiter Lend | Lending | $965.51M | -5.5% | -8.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $706.19M | -2.0% | -5.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $505.80M | -5.6% | -10.0% |
| 9 | Sentora Curator | Risk Curators | $383.58M | -0.0% | -8.0% |
| 10 | Marinade Native | Staking Pool | $351.62M | -4.4% | -8.7% |
| 11 | PumpSwap | Dexs | $340.52M | +0.2% | -4.1% |
| 12 | OnRe | RWA | $305.10M | -0.1% | +3.5% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 336 protocols the total is $15.06B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 16.4% · Dexs 15.5% · Derivatives 5.1% · RWA 4.0% · Risk Curators 3.8%

### Tokenised assets

$862.19M of tokenised real-world assets and equities are locked on Solana - 5.725% of chain TVL.

- OnRe (RWA): $305.10M
- Huma (RWA): $246.31M
- Solstice (Basis Trading): $201.25M
- JupUSD (Basis Trading): $43.11M
- Plume Vaults (RWA): $35.56M

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

### Change over 24h (vs run at 2026-10-28T21:57:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,155.70 | 2,732.84 | +26.77% |
| Average non-vote TPS | 2,155.70 | 2,732.84 | +26.77% |
| Average slot time (ms) | 213.60 | 214.30 | +0.33% |
| Active validators | 661.00 | 666.00 | +0.76% |
| Delinquent validators | 30.00 | 23.00 | -23.33% |
| Solana TVL | 5,748,939,504.00 | 5,655,014,849.00 | -1.63% |
| SOL price | 102.77 | 97.17 | -5.45% |
| Stablecoin supply | 15,784,667,411.00 | 15,693,912,574.00 | -0.57% |
| 24h DEX volume | 1,582,952,703.63 | 1,733,397,982.06 | +9.50% |
| 24h chain fees | 11,229,097.00 | 10,347,418.88 | -7.85% |

### Change over 7d (vs run at 2026-10-22T20:55:10Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,984.31 | 2,732.84 | -8.43% |
| Average non-vote TPS | 2,984.31 | 2,732.84 | -8.43% |
| Average slot time (ms) | 196.40 | 214.30 | +9.11% |
| Active validators | 655.00 | 666.00 | +1.68% |
| Delinquent validators | 21.00 | 23.00 | +9.52% |
| Solana TVL | 5,883,924,131.00 | 5,655,014,849.00 | -3.89% |
| SOL price | 103.14 | 97.17 | -5.79% |
| Stablecoin supply | 16,152,572,344.00 | 15,693,912,574.00 | -2.84% |
| 24h DEX volume | 2,270,402,206.37 | 1,733,397,982.06 | -23.65% |
| 24h chain fees | 11,957,946.66 | 10,347,418.88 | -13.47% |

### Change over 30d (vs run at 2026-09-29T21:34:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,737.06 | 2,732.84 | -42.31% |
| Average non-vote TPS | 2,239.20 | 2,732.84 | +22.05% |
| Average slot time (ms) | 268.60 | 214.30 | -20.22% |
| Active validators | 673.00 | 666.00 | -1.04% |
| Delinquent validators | 10.00 | 23.00 | +130.00% |
| Solana TVL | 6,522,003,878.00 | 5,655,014,849.00 | -13.29% |
| SOL price | 118.62 | 97.17 | -18.08% |
| Stablecoin supply | 16,661,913,603.00 | 15,693,912,574.00 | -5.81% |
| 24h DEX volume | 2,662,061,803.25 | 1,733,397,982.06 | -34.89% |
| 24h chain fees | 17,514,749.35 | 10,347,418.88 | -40.92% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 28.9s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
