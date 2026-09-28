# Solana Ecosystem Pulse

**Generated:** 2026-09-28T12:10:14Z · **Schema:** `1.0.0` · **Collection time:** 12.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.58 | -3.70% |
| Market cap | $70.27B | rank #7 |
| Total value locked | $6.50B | -1.83% |
| Stablecoin supply | $16.72B | -0.48% |
| DEX volume (24h) | $1.93B | -10.61% |
| Chain fees / REV (24h) | $15.31M | -14.67% |
| Non-vote TPS (1h avg) | 1,618 | peak 5,258 total |
| Active validators | 675 | 8 delinquent |
| Epoch 1044 | 71.06% complete | 125,011 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,618.3 average over the last 60 minutes; 2,030.4 in the latest sample.
- **Total TPS:** 4,131.0 average, 5,258.1 peak. Consensus votes account for 60.8% of all transactions.
- **Slot time:** 268.0 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 429,354,628 at absolute slot 451,314,989.
- **Epoch 1044:** slot 306,989 of 432,000 (71.06% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.628% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 160 ms |
| `solana-rpc.publicnode.com` | yes | 111 ms |
| `api.mainnet.solana.com` | yes | 111 ms |

## Validators & stake

- **675 active** validators, **8 delinquent** (1.17% by count, 0.019% by stake).
- **Total stake:** 440,549,807 SOL ($52.68B); stake rate 69.40% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.47% and top 33 hold 45.57% of active stake.
- **Commission:** median 5.0%, mean 12.94%; 229 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,867,779 | 4.057% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,792 | 3.596% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,330,570 | 2.799% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,215,732 | 2.546% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,838,730 | 2.461% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,238,854 | 2.098% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,209,776 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,623,407 | 1.731% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,094,526 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,511,334 | 1.478% | 0% |

## Economics

- **SOL:** $119.58 (-3.70% 24h, +2.45% 7d, +15.53% 30d). Market cap $70.27B, 24h volume $3.54B (5.04% of cap). Price source: `coingecko`.
- **TVL:** $6.50B across 331 protocols - rank #2 of 467 chains, 6.90% of all tracked chain TVL. +4.80% over 7d, -50.9% from its ATH.
- **Stablecoins:** $16.72B circulating on Solana (+5.13% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.93B in 24h, $18.32B over 7d across 126 venues. Volume/TVL turnover 0.296x per day.
- **REV (chain fees):** $15.31M in 24h, $404.67M over 30d. Retained chain revenue $5.30M (34.6% of fees). Annualised fees are 7.95% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,782,064 SOL circulating of 634,840,775 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.91B | -5.3% | +6.8% |
| 2 | Kamino Lend | Lending | $1.44B | -2.9% | +5.6% |
| 3 | Raydium AMM | Dexs | $1.33B | -4.3% | +5.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.22B | -5.1% | +6.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.21B | -4.9% | +3.5% |
| 6 | Jupiter Lend | Lending | $1.17B | -2.6% | +4.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $810.36M | -3.4% | +2.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $609.08M | -5.1% | +6.3% |
| 9 | Marinade Native | Staking Pool | $454.09M | -5.0% | +7.1% |
| 10 | PumpSwap | Dexs | $382.13M | -5.7% | +3.8% |
| 11 | Sentora Curator | Risk Curators | $362.41M | -0.1% | -0.5% |
| 12 | Drift Staked SOL | Liquid Staking | $332.09M | -5.1% | +6.1% |

The top five protocols hold 42.3% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.85B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 17.2% · Dexs 15.8% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$835.20M of tokenised real-world assets and equities are locked on Solana - 4.956% of chain TVL.

- OnRe (RWA): $296.37M
- Solstice (Basis Trading): $215.43M
- Huma (RWA): $209.03M
- JupUSD (Basis Trading): $44.05M
- Plume Vaults (RWA): $25.47M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-28
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-09-28
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) - updated 2026-09-27
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-27T10:56:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,069.58 | 4,130.98 | +1.51% |
| Average non-vote TPS | 1,554.32 | 1,618.33 | +4.12% |
| Average slot time (ms) | 267.90 | 268.00 | +0.04% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 6,686,550,317.00 | 6,503,643,660.00 | -2.74% |
| SOL price | 123.93 | 119.58 | -3.51% |
| Stablecoin supply | 16,804,013,694.00 | 16,722,135,325.00 | -0.49% |
| 24h DEX volume | 2,204,204,155.21 | 1,926,466,128.71 | -12.60% |
| 24h chain fees | 18,490,489.57 | 15,306,075.25 | -17.22% |

### Change over 7d (vs run at 2026-09-21T11:15:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,062.42 | 4,130.98 | +1.69% |
| Average non-vote TPS | 1,532.53 | 1,618.33 | +5.60% |
| Average slot time (ms) | 266.50 | 268.00 | +0.56% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 6,384,701,956.00 | 6,503,643,660.00 | +1.86% |
| SOL price | 116.20 | 119.58 | +2.91% |
| Stablecoin supply | 15,905,119,382.00 | 16,722,135,325.00 | +5.14% |
| 24h DEX volume | 2,795,356,104.36 | 1,926,466,128.71 | -31.08% |
| 24h chain fees | 14,383,414.08 | 15,306,075.25 | +6.41% |

### Change over 30d (vs run at 2026-08-29T20:04:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,144.50 | 4,130.98 | -0.33% |
| Average non-vote TPS | 1,989.40 | 1,618.33 | -18.65% |
| Average slot time (ms) | 318.30 | 268.00 | -15.80% |
| Active validators | 689.00 | 675.00 | -2.03% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 5,896,456,733.00 | 6,503,643,660.00 | +10.30% |
| SOL price | 105.39 | 119.58 | +13.46% |
| Stablecoin supply | 16,345,994,847.00 | 16,722,135,325.00 | +2.30% |
| 24h DEX volume | 2,590,586,442.22 | 1,926,466,128.71 | -25.64% |
| 24h chain fees | 15,728,868.43 | 15,306,075.25 | -2.69% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
