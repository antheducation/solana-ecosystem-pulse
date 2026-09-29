# Solana Ecosystem Pulse

**Generated:** 2026-09-29T17:08:02Z · **Schema:** `1.0.0` · **Collection time:** 17.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.18 | -0.51% |
| Market cap | $69.47B | rank #7 |
| Total value locked | $6.58B | -0.92% |
| Stablecoin supply | $16.66B | -0.36% |
| DEX volume (24h) | $2.66B | +38.18% |
| Chain fees / REV (24h) | $17.51M | +13.56% |
| Non-vote TPS (1h avg) | 2,435 | peak 5,817 total |
| Active validators | 672 | 10 delinquent |
| Epoch 1045 | 61.19% complete | 167,638 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,434.5 average over the last 60 minutes; 2,276.7 in the latest sample.
- **Total TPS:** 4,925.9 average, 5,816.5 peak. Consensus votes account for 50.6% of all transactions.
- **Slot time:** 268.6 ms average (target 400 ms), worst 1-minute bucket 283.0 ms.
- **Block height:** 429,743,862 at absolute slot 451,704,362.
- **Epoch 1045:** slot 264,362 of 432,000 (61.19% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 242 ms |
| `solana-rpc.publicnode.com` | yes | 146 ms |
| `api.mainnet.solana.com` | yes | 165 ms |

## Validators & stake

- **672 active** validators, **10 delinquent** (1.47% by count, 0.054% by stake).
- **Total stake:** 441,249,792 SOL ($52.15B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.54% of active stake.
- **Commission:** median 5.0%, mean 12.85%; 227 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.042% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.798% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.562% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.542% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.096% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.732% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.519% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.478% | 0% |

## Economics

- **SOL:** $118.18 (-0.51% 24h, +0.62% 7d, +10.63% 30d). Market cap $69.47B, 24h volume $3.81B (5.48% of cap). Price source: `coingecko`.
- **TVL:** $6.58B across 331 protocols - rank #2 of 467 chains, 6.91% of all tracked chain TVL. +1.84% over 7d, -50.3% from its ATH.
- **Stablecoins:** $16.66B circulating on Solana (-2.97% 7d) - $2.53 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.66B in 24h, $17.56B over 7d across 127 venues. Volume/TVL turnover 0.405x per day.
- **REV (chain fees):** $17.51M in 24h, $412.12M over 30d. Retained chain revenue $5.87M (33.5% of fees). Annualised fees are 9.20% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,851,607 SOL circulating of 634,918,308 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.96B | +2.0% | +3.5% |
| 2 | Kamino Lend | Lending | $1.41B | -2.2% | -0.6% |
| 3 | Raydium AMM | Dexs | $1.35B | +0.0% | +1.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.25B | +1.9% | +2.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.24B | +1.9% | +0.4% |
| 6 | Jupiter Lend | Lending | $1.22B | +4.1% | +4.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $817.62M | +1.6% | -1.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $610.12M | -0.5% | -0.6% |
| 9 | Marinade Native | Staking Pool | $465.70M | +2.2% | +3.3% |
| 10 | PumpSwap | Dexs | $393.15M | +1.2% | +4.3% |
| 11 | Sentora Curator | Risk Curators | $350.66M | -3.2% | -3.3% |
| 12 | Drift Staked SOL | Liquid Staking | $340.41M | +1.9% | +1.8% |

The top five protocols hold 42.2% of Solana's tracked TVL. Summed across all 331 protocols the total is $17.11B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 17.2% · Dexs 15.8% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.3%

### Tokenised assets

$831.95M of tokenised real-world assets and equities are locked on Solana - 4.863% of chain TVL.

- OnRe (RWA): $293.61M
- Solstice (Basis Trading): $215.02M
- Huma (RWA): $207.54M
- JupUSD (Basis Trading): $44.07M
- Plume Vaults (RWA): $25.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-29
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-09-28
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25

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

### Change over 24h (vs run at 2026-09-28T12:10:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,130.98 | 4,925.90 | +19.24% |
| Average non-vote TPS | 1,618.33 | 2,434.54 | +50.44% |
| Average slot time (ms) | 268.00 | 268.60 | +0.22% |
| Active validators | 675.00 | 672.00 | -0.44% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 6,503,643,660.00 | 6,578,087,634.00 | +1.14% |
| SOL price | 119.58 | 118.18 | -1.17% |
| Stablecoin supply | 16,722,135,325.00 | 16,662,773,223.00 | -0.35% |
| 24h DEX volume | 1,926,466,128.71 | 2,662,061,803.25 | +38.18% |
| 24h chain fees | 15,306,075.25 | 17,514,749.35 | +14.43% |

### Change over 7d (vs run at 2026-09-22T15:50:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,849.16 | 4,925.90 | +1.58% |
| Average non-vote TPS | 2,344.69 | 2,434.54 | +3.83% |
| Average slot time (ms) | 268.40 | 268.60 | +0.07% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 6,467,273,208.00 | 6,578,087,634.00 | +1.71% |
| SOL price | 117.67 | 118.18 | +0.43% |
| Stablecoin supply | 17,171,768,101.00 | 16,662,773,223.00 | -2.96% |
| 24h DEX volume | 3,428,858,820.75 | 2,662,061,803.25 | -22.36% |
| 24h chain fees | 18,642,402.21 | 17,514,749.35 | -6.05% |

### Change over 30d (vs run at 2026-08-30T20:10:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,293.13 | 4,925.90 | +14.74% |
| Average non-vote TPS | 2,167.90 | 2,434.54 | +12.30% |
| Average slot time (ms) | 318.30 | 268.60 | -15.61% |
| Active validators | 680.00 | 672.00 | -1.18% |
| Delinquent validators | 17.00 | 10.00 | -41.18% |
| Solana TVL | 5,956,176,022.00 | 6,578,087,634.00 | +10.44% |
| SOL price | 105.77 | 118.18 | +11.73% |
| Stablecoin supply | 16,297,776,213.00 | 16,662,773,223.00 | +2.24% |
| 24h DEX volume | 1,670,710,752.31 | 2,662,061,803.25 | +59.34% |
| 24h chain fees | 11,213,986.82 | 17,514,749.35 | +56.19% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
