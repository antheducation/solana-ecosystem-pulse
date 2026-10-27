# Solana Ecosystem Pulse

**Generated:** 2026-10-27T21:31:32Z · **Schema:** `1.0.0` · **Collection time:** 16.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.85 | +0.44% |
| Market cap | $59.49B | rank #7 |
| Total value locked | $5.72B | -0.18% |
| Stablecoin supply | $15.76B | -0.55% |
| DEX volume (24h) | $2.07B | +42.91% |
| Chain fees / REV (24h) | $11.67M | +25.60% |
| Non-vote TPS (1h avg) | 2,360 | peak 4,390 total |
| Active validators | 665 | 20 delinquent |
| Epoch 1069 | 96.20% complete | 16,433 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 125 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 42.9% in 24h) | DEX volume changed +42.9% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,359.98 sits 3.6 sigma below the median of the last 125 runs (4,565.46, -48.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,360.0 average over the last 60 minutes; 1,974.5 in the latest sample.
- **Total TPS:** 2,360.0 average, 4,389.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.8 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 440,249,111 at absolute slot 462,223,567.
- **Epoch 1069:** slot 415,567 of 432,000 (96.20% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.584% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 256 ms |
| `solana-rpc.publicnode.com` | yes | 169 ms |
| `api.mainnet.solana.com` | yes | 207 ms |

## Validators & stake

- **665 active** validators, **20 delinquent** (2.92% by count, 0.085% by stake).
- **Total stake:** 436,873,593 SOL ($44.06B); stake rate 68.63% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.60% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 12.98%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,059,304 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,636,453 | 3.811% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,660,117 | 2.900% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,812,577 | 2.477% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,716,980 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,494,053 | 2.175% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,206,552 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,754,189 | 1.776% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,040,177 | 1.613% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,375 | 1.603% | 0% |

## Economics

- **SOL:** $100.85 (+0.44% 24h, -5.44% 7d, -17.80% 30d). Market cap $59.49B, 24h volume $2.01B (3.39% of cap). Price source: `coingecko`.
- **TVL:** $5.72B across 335 protocols - rank #4 of 421 chains, 6.44% of all tracked chain TVL. -2.62% over 7d, -55.9% from its ATH.
- **Stablecoins:** $15.76B circulating on Solana (-0.91% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.07B in 24h, $13.69B over 7d across 138 venues. Volume/TVL turnover 0.362x per day.
- **REV (chain fees):** $11.67M in 24h, $418.38M over 30d. Retained chain revenue $4.59M (39.3% of fees). Annualised fees are 7.16% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,874,393 SOL circulating of 636,517,468 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | +1.4% | -1.4% |
| 2 | Kamino Lend | Lending | $1.26B | +0.1% | -3.2% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.2% | -3.9% |
| 4 | Binance Staked SOL | Liquid Staking | $1.08B | +2.3% | -1.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.05B | +0.8% | -3.9% |
| 6 | Jupiter Lend | Lending | $1.01B | +1.0% | -0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $716.70M | +0.8% | -2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $529.32M | +0.9% | -3.1% |
| 9 | Sentora Curator | Risk Curators | $383.86M | -0.0% | -14.4% |
| 10 | Marinade Native | Staking Pool | $362.46M | +0.1% | -4.2% |
| 11 | PumpSwap | Dexs | $334.05M | -0.6% | -4.2% |
| 12 | Orca DEX | Dexs | $301.46M | +0.1% | +1.0% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 335 protocols the total is $15.42B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.5% · Dexs 15.1% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$866.49M of tokenised real-world assets and equities are locked on Solana - 5.618% of chain TVL.

- OnRe (RWA): $301.20M
- Huma (RWA): $253.40M
- Solstice (Basis Trading): $201.55M
- JupUSD (Basis Trading): $42.98M
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

- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-27
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-27
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-27
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-27
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

### Change over 24h (vs run at 2026-10-26T21:59:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,853.07 | 2,359.98 | +27.36% |
| Average non-vote TPS | 1,853.06 | 2,359.97 | +27.36% |
| Average slot time (ms) | 211.90 | 213.80 | +0.90% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 20.00 | 20.00 | +0.00% |
| Solana TVL | 5,710,299,220.00 | 5,721,042,380.00 | +0.19% |
| SOL price | 100.45 | 100.85 | +0.40% |
| Stablecoin supply | 15,849,510,602.00 | 15,763,185,048.00 | -0.54% |
| 24h DEX volume | 1,449,231,950.27 | 2,071,067,618.21 | +42.91% |
| 24h chain fees | 9,292,855.03 | 11,672,734.12 | +25.61% |

### Change over 7d (vs run at 2026-10-20T20:57:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,725.49 | 2,359.98 | -58.78% |
| Average non-vote TPS | 2,649.32 | 2,359.97 | -10.92% |
| Average slot time (ms) | 216.10 | 213.80 | -1.06% |
| Active validators | 668.00 | 665.00 | -0.45% |
| Delinquent validators | 11.00 | 20.00 | +81.82% |
| Solana TVL | 5,971,159,147.00 | 5,721,042,380.00 | -4.19% |
| SOL price | 106.50 | 100.85 | -5.31% |
| Stablecoin supply | 15,910,290,288.00 | 15,763,185,048.00 | -0.92% |
| 24h DEX volume | 1,823,579,289.83 | 2,071,067,618.21 | +13.57% |
| 24h chain fees | 11,987,511.75 | 11,672,734.12 | -2.63% |

### Change over 30d (vs run at 2026-09-27T20:31:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.15 | 2,359.98 | -49.35% |
| Average non-vote TPS | 2,150.72 | 2,359.97 | +9.73% |
| Average slot time (ms) | 268.10 | 213.80 | -20.25% |
| Active validators | 675.00 | 665.00 | -1.48% |
| Delinquent validators | 8.00 | 20.00 | +150.00% |
| Solana TVL | 6,696,462,246.00 | 5,721,042,380.00 | -14.57% |
| SOL price | 122.76 | 100.85 | -17.85% |
| Stablecoin supply | 16,803,216,984.00 | 15,763,185,048.00 | -6.19% |
| 24h DEX volume | 2,155,234,120.21 | 2,071,067,618.21 | -3.91% |
| 24h chain fees | 17,938,389.57 | 11,672,734.12 | -34.93% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
