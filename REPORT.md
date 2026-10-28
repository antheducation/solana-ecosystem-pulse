# Solana Ecosystem Pulse

**Generated:** 2026-10-28T11:44:51Z · **Schema:** `1.0.0` · **Collection time:** 12.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.71 | +2.70% |
| Market cap | $60.58B | rank #7 |
| Total value locked | $5.79B | +1.72% |
| Stablecoin supply | $15.78B | +0.11% |
| DEX volume (24h) | $1.58B | -23.57% |
| Chain fees / REV (24h) | $10.91M | -6.55% |
| Non-vote TPS (1h avg) | 1,323 | peak 1,694 total |
| Active validators | 662 | 29 delinquent |
| Epoch 1070 | 51.87% complete | 207,912 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 126 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,323; the healthy floor used here is 1,500. | `threshold` |
| [SERIOUS] | Average TPS is below its recent norm | Current 1,323.46 sits 5.3 sigma below the median of the last 126 runs (4,528.24, -70.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 29.00 sits 4.0 sigma above the median of the last 126 runs (11.00, +163.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,323.5 average over the last 60 minutes; 1,397.5 in the latest sample.
- **Total TPS:** 1,323.5 average, 1,694.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.6 ms average (target 400 ms), worst 1-minute bucket 218.2 ms.
- **Block height:** 440,488,643 at absolute slot 462,464,088.
- **Epoch 1070:** slot 224,088 of 432,000 (51.87% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.583% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 110 ms |
| `solana-rpc.publicnode.com` | yes | 216 ms |
| `api.mainnet.solana.com` | yes | 142 ms |

## Validators & stake

- **662 active** validators, **29 delinquent** (4.20% by count, 0.886% by stake).
- **Total stake:** 437,290,026 SOL ($44.91B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.34% of active stake.
- **Commission:** median 5.0%, mean 12.95%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,006,422 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,661,096 | 3.844% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,791,931 | 2.951% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,815,143 | 2.495% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,548 | 2.242% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,464,443 | 2.184% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,208,877 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,757,994 | 1.790% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,041,146 | 1.625% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,044 | 1.614% | 0% |

## Economics

- **SOL:** $102.71 (+2.70% 24h, -3.58% 7d, -13.36% 30d). Market cap $60.58B, 24h volume $2.07B (3.41% of cap). Price source: `coingecko`.
- **TVL:** $5.79B across 335 protocols - rank #4 of 421 chains, 6.50% of all tracked chain TVL. -3.41% over 7d, -55.4% from its ATH.
- **Stablecoins:** $15.78B circulating on Solana (-1.44% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.58B in 24h, $12.83B over 7d across 138 venues. Volume/TVL turnover 0.273x per day.
- **REV (chain fees):** $10.91M in 24h, $412.35M over 30d. Retained chain revenue $4.08M (37.4% of fees). Annualised fees are 6.57% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.7% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,928,408 SOL circulating of 636,578,201 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | +3.5% | -1.8% |
| 2 | Kamino Lend | Lending | $1.28B | +1.3% | -4.5% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.8% | -4.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | +3.9% | -1.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.07B | +2.9% | -3.2% |
| 6 | Jupiter Lend | Lending | $1.02B | +1.8% | -1.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $723.51M | +2.2% | -3.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $536.82M | +2.8% | -3.8% |
| 9 | Sentora Curator | Risk Curators | $383.80M | -0.0% | -11.3% |
| 10 | Marinade Native | Staking Pool | $367.88M | +1.9% | -4.6% |
| 11 | PumpSwap | Dexs | $345.29M | +4.5% | -2.5% |
| 12 | Orca DEX | Dexs | $303.67M | +1.2% | -0.3% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 335 protocols the total is $15.63B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.4% · Dexs 15.1% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$867.43M of tokenised real-world assets and equities are locked on Solana - 5.549% of chain TVL.

- OnRe (RWA): $301.24M
- Huma (RWA): $254.22M
- Solstice (Basis Trading): $201.62M
- JupUSD (Basis Trading): $42.96M
- Plume Vaults (RWA): $37.18M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup) - Mon, 26 Oct 2026 10:00:00 GMT
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) - Fri, 23 Oct 2026 01:09:00 GMT
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-27
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

### Change over 24h (vs run at 2026-10-27T11:09:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,484.87 | 1,323.46 | -10.87% |
| Average non-vote TPS | 1,484.87 | 1,323.46 | -10.87% |
| Average slot time (ms) | 212.80 | 212.60 | -0.09% |
| Active validators | 665.00 | 662.00 | -0.45% |
| Delinquent validators | 20.00 | 29.00 | +45.00% |
| Solana TVL | 5,681,242,565.00 | 5,789,213,551.00 | +1.90% |
| SOL price | 100.18 | 102.71 | +2.53% |
| Stablecoin supply | 15,762,299,946.00 | 15,780,319,313.00 | +0.11% |
| 24h DEX volume | 2,071,067,618.15 | 1,582,952,703.63 | -23.57% |
| 24h chain fees | 11,666,989.55 | 10,908,125.93 | -6.50% |

### Change over 7d (vs run at 2026-10-21T10:43:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,602.94 | 1,323.46 | -71.25% |
| Average non-vote TPS | 1,524.60 | 1,323.46 | -13.19% |
| Average slot time (ms) | 216.00 | 212.60 | -1.57% |
| Active validators | 668.00 | 662.00 | -0.90% |
| Delinquent validators | 11.00 | 29.00 | +163.64% |
| Solana TVL | 6,001,273,500.00 | 5,789,213,551.00 | -3.53% |
| SOL price | 106.30 | 102.71 | -3.38% |
| Stablecoin supply | 16,008,541,783.00 | 15,780,319,313.00 | -1.43% |
| 24h DEX volume | 2,235,068,600.00 | 1,582,952,703.63 | -29.18% |
| 24h chain fees | 13,200,582.40 | 10,908,125.93 | -17.37% |

### Change over 30d (vs run at 2026-09-28T22:41:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,519.28 | 1,323.46 | -70.72% |
| Average non-vote TPS | 2,010.42 | 1,323.46 | -34.17% |
| Average slot time (ms) | 267.20 | 212.60 | -20.43% |
| Active validators | 674.00 | 662.00 | -1.78% |
| Delinquent validators | 8.00 | 29.00 | +262.50% |
| Solana TVL | 6,552,189,378.00 | 5,789,213,551.00 | -11.64% |
| SOL price | 118.18 | 102.71 | -13.09% |
| Stablecoin supply | 16,723,366,837.00 | 15,780,319,313.00 | -5.64% |
| 24h DEX volume | 1,926,466,128.71 | 1,582,952,703.63 | -17.83% |
| 24h chain fees | 15,421,946.25 | 10,908,125.93 | -29.27% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
