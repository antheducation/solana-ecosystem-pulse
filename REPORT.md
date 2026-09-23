# Solana Ecosystem Pulse

**Generated:** 2026-09-23T10:22:04Z · **Schema:** `1.0.0` · **Collection time:** 59.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.38 | +0.34% |
| Market cap | $68.98B | rank #7 |
| Total value locked | $6.55B | +1.39% |
| Stablecoin supply | $16.88B | -1.70% |
| DEX volume (24h) | $3.45B | +0.59% |
| Chain fees / REV (24h) | $17.84M | -4.27% |
| Non-vote TPS (1h avg) | 1,543 | peak 4,405 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1040 | 91.38% complete | 37,245 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 91 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 264.90 sits 15.9 sigma below the median of the last 91 runs (316.70, -16.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,548,550,262.00 sits 3.4 sigma above the median of the last 91 runs (5,861,539,247.00, +11.7%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,543.3 average over the last 60 minutes; 1,379.8 in the latest sample.
- **Total TPS:** 4,085.1 average, 4,404.8 peak. Consensus votes account for 62.2% of all transactions.
- **Slot time:** 264.9 ms average (target 400 ms), worst 1-minute bucket 272.7 ms.
- **Block height:** 427,715,034 at absolute slot 449,674,755.
- **Epoch 1040:** slot 394,755 of 432,000 (91.38% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.636% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 59 ms |
| `solana-rpc.publicnode.com` | yes | 58 ms |
| `api.mainnet.solana.com` | yes | 51 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.045% by stake).
- **Total stake:** 439,861,749 SOL ($51.63B); stake rate 69.32% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.83% of active stake.
- **Commission:** median 5.0%, mean 12.58%; 235 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,826,722 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,698 | 3.603% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,354,353 | 2.810% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,265,429 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,210,832 | 2.322% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,211,356 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,144,102 | 2.080% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,458,789 | 1.696% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,089,342 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,555,722 | 1.491% | 0% |

## Economics

- **SOL:** $117.38 (+0.34% 24h, +20.72% 7d, +24.02% 30d). Market cap $68.98B, 24h volume $4.39B (6.37% of cap). Price source: `coingecko`.
- **TVL:** $6.55B across 332 protocols - rank #2 of 467 chains, 6.77% of all tracked chain TVL. +14.39% over 7d, -50.5% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+5.73% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.45B in 24h, $20.08B over 7d across 125 venues. Volume/TVL turnover 0.527x per day.
- **REV (chain fees):** $17.84M in 24h, $432.70M over 30d. Retained chain revenue $6.85M (38.4% of fees). Annualised fees are 9.44% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,506,858 SOL circulating of 634,530,486 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.88B | +1.6% | +22.6% |
| 2 | Kamino Lend | Lending | $1.43B | +0.7% | +7.8% |
| 3 | Raydium AMM | Dexs | $1.34B | +2.1% | +23.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | +0.6% | +22.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.21B | +0.8% | +20.9% |
| 6 | Jupiter Lend | Lending | $1.20B | +0.7% | +10.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $822.68M | +0.7% | +12.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $614.06M | +0.9% | +22.2% |
| 9 | Marinade Native | Staking Pool | $456.04M | +1.4% | +23.2% |
| 10 | PumpSwap | Dexs | $390.56M | +3.3% | +24.5% |
| 11 | Sentora Curator | Risk Curators | $362.94M | -0.1% | -5.3% |
| 12 | Drift Staked SOL | Liquid Staking | $334.68M | +0.8% | +22.4% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.87B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 17.3% · Dexs 15.9% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$826.77M of tokenised real-world assets and equities are locked on Solana - 4.901% of chain TVL.

- OnRe (RWA): $302.74M
- Solstice (Basis Trading): $218.06M
- Huma Finance V2 (RWA): $188.39M
- JupUSD (Basis Trading): $46.61M
- Plume Vaults (RWA): $28.20M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-23
- [SIMD-0649: SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) - updated 2026-09-23
- [SIMD-0558: SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22

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

### Change over 24h (vs run at 2026-09-22T10:26:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,915.77 | 4,085.13 | +4.33% |
| Average non-vote TPS | 1,388.79 | 1,543.26 | +11.12% |
| Average slot time (ms) | 265.80 | 264.90 | -0.34% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 6,425,863,032.00 | 6,548,550,262.00 | +1.91% |
| SOL price | 116.51 | 117.38 | +0.75% |
| Stablecoin supply | 17,171,641,113.00 | 16,880,437,780.00 | -1.70% |
| 24h DEX volume | 3,370,343,441.75 | 3,449,152,862.76 | +2.34% |
| 24h chain fees | 18,053,797.21 | 17,843,164.76 | -1.17% |

### Change over 7d (vs run at 2026-09-16T10:23:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,356.16 | 4,085.13 | +21.72% |
| Average non-vote TPS | 1,225.32 | 1,543.26 | +25.95% |
| Average slot time (ms) | 316.00 | 264.90 | -16.17% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,716,713,977.00 | 6,548,550,262.00 | +14.55% |
| SOL price | 97.26 | 117.38 | +20.69% |
| Stablecoin supply | 15,965,637,649.00 | 16,880,437,780.00 | +5.73% |
| 24h DEX volume | 2,522,724,403.22 | 3,449,152,862.76 | +36.72% |
| 24h chain fees | 14,228,744.46 | 17,843,164.76 | +25.40% |

### Change over 30d (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,085.13 | -10.57% |
| Average non-vote TPS | 2,714.40 | 1,543.26 | -43.15% |
| Average slot time (ms) | 367.20 | 264.90 | -27.86% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,621,355,422.00 | 6,548,550,262.00 | +16.49% |
| SOL price | 96.29 | 117.38 | +21.90% |
| Stablecoin supply | 16,453,918,497.00 | 16,880,437,780.00 | +2.59% |
| 24h DEX volume | 2,938,613,605.25 | 3,449,152,862.76 | +17.37% |
| 24h chain fees | 12,654,048.70 | 17,843,164.76 | +41.01% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 59.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
