# Solana Ecosystem Pulse

**Generated:** 2026-10-02T02:48:58Z · **Schema:** `1.0.0` · **Collection time:** 12.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.74 | +1.53% |
| Market cap | $70.40B | rank #7 |
| Total value locked | $6.57B | +0.90% |
| Stablecoin supply | $16.58B | +1.11% |
| DEX volume (24h) | $2.58B | +0.38% |
| Chain fees / REV (24h) | $17.03M | +6.59% |
| Non-vote TPS (1h avg) | 2,246 | peak 5,744 total |
| Active validators | 671 | 13 delinquent |
| Epoch 1047 | 40.76% complete | 255,919 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 98 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,246.0 average over the last 60 minutes; 3,186.7 in the latest sample.
- **Total TPS:** 4,734.5 average, 5,743.5 peak. Consensus votes account for 52.6% of all transactions.
- **Slot time:** 268.7 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 430,518,866 at absolute slot 452,480,081.
- **Epoch 1047:** slot 176,081 of 432,000 (40.76% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.622% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 146 ms |
| `solana-rpc.publicnode.com` | yes | 40 ms |
| `api.mainnet.solana.com` | yes | 98 ms |

## Validators & stake

- **671 active** validators, **13 delinquent** (1.90% by count, 0.090% by stake).
- **Total stake:** 440,810,473 SOL ($52.78B); stake rate 69.41% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.64% and top 33 hold 45.79% of active stake.
- **Commission:** median 5.0%, mean 12.72%; 228 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,839,408 | 4.051% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,905,145 | 3.611% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,328,203 | 2.799% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,357,265 | 2.579% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,121 | 2.545% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,267,704 | 2.104% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,246,451 | 2.099% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,601,711 | 1.726% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,063,975 | 1.604% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,682,305 | 1.517% | 0% |

## Economics

- **SOL:** $119.74 (+1.53% 24h, +1.96% 7d, +20.87% 30d). Market cap $70.40B, 24h volume $3.45B (4.90% of cap). Price source: `coingecko`.
- **TVL:** $6.57B across 333 protocols - rank #2 of 468 chains, 6.87% of all tracked chain TVL. +1.22% over 7d, -50.4% from its ATH.
- **Stablecoins:** $16.58B circulating on Solana (-5.28% 7d) - $2.52 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.58B in 24h, $15.93B over 7d across 126 venues. Volume/TVL turnover 0.393x per day.
- **REV (chain fees):** $17.03M in 24h, $421.45M over 30d. Retained chain revenue $6.13M (36.0% of fees). Annualised fees are 8.83% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,075,632 SOL circulating of 635,073,293 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.93B | +0.3% | +1.7% |
| 2 | Kamino Lend | Lending | $1.37B | -1.1% | -3.8% |
| 3 | Raydium AMM | Dexs | $1.33B | -0.1% | +0.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | +0.4% | +1.2% |
| 5 | Jupiter Lend | Lending | $1.22B | +0.4% | +3.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.21B | +0.3% | +0.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $810.73M | +0.9% | -0.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.02M | +0.7% | +0.7% |
| 9 | Marinade Native | Staking Pool | $441.84M | -0.6% | -2.1% |
| 10 | PumpSwap | Dexs | $394.63M | +0.5% | +3.4% |
| 11 | Sentora Curator | Risk Curators | $394.21M | -1.1% | +8.8% |
| 12 | Drift Staked SOL | Liquid Staking | $335.18M | +0.7% | +1.2% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 333 protocols the total is $17.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.8% · Dexs 15.7% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.5%

### Tokenised assets

$860.90M of tokenised real-world assets and equities are locked on Solana - 4.978% of chain TVL.

- OnRe (RWA): $291.24M
- Huma (RWA): $226.60M
- Solstice (Basis Trading): $214.43M
- JupUSD (Basis Trading): $45.15M
- Plume Vaults (RWA): $32.29M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-01
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-30
- [SIMD-0677: SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-29
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-29

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

### Change over 24h (vs run at 2026-10-01T02:45:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,555.14 | 4,734.47 | +3.94% |
| Average non-vote TPS | 2,062.19 | 2,246.04 | +8.92% |
| Average slot time (ms) | 268.10 | 268.70 | +0.22% |
| Active validators | 673.00 | 671.00 | -0.30% |
| Delinquent validators | 10.00 | 13.00 | +30.00% |
| Solana TVL | 6,528,079,711.00 | 6,567,493,900.00 | +0.60% |
| SOL price | 117.98 | 119.74 | +1.49% |
| Stablecoin supply | 16,397,665,769.00 | 16,582,597,354.00 | +1.13% |
| 24h DEX volume | 2,544,678,619.73 | 2,579,620,195.88 | +1.37% |
| 24h chain fees | 15,842,342.66 | 17,028,324.19 | +7.49% |

### Change over 7d (vs run at 2026-09-25T02:09:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,337.90 | 4,734.47 | +9.14% |
| Average non-vote TPS | 1,832.73 | 2,246.04 | +22.55% |
| Average slot time (ms) | 268.20 | 268.70 | +0.19% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 10.00 | 13.00 | +30.00% |
| Solana TVL | 6,485,663,210.00 | 6,567,493,900.00 | +1.26% |
| SOL price | 118.12 | 119.74 | +1.37% |
| Stablecoin supply | 17,687,554,466.00 | 16,582,597,354.00 | -6.25% |
| 24h DEX volume | 2,262,604,262.43 | 2,579,620,195.88 | +14.01% |
| 24h chain fees | 15,931,553.48 | 17,028,324.19 | +6.88% |

### Change over 30d (vs run at 2026-09-01T20:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,409.25 | 4,734.47 | +7.38% |
| Average non-vote TPS | 2,288.53 | 2,246.04 | -1.86% |
| Average slot time (ms) | 317.90 | 268.70 | -15.48% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 17.00 | 13.00 | -23.53% |
| Solana TVL | 5,737,476,214.00 | 6,567,493,900.00 | +14.47% |
| SOL price | 99.96 | 119.74 | +19.79% |
| Stablecoin supply | 15,969,999,346.00 | 16,582,597,354.00 | +3.84% |
| 24h DEX volume | 2,501,465,620.05 | 2,579,620,195.88 | +3.12% |
| 24h chain fees | 13,501,461.08 | 17,028,324.19 | +26.12% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
