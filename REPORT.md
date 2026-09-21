# Solana Ecosystem Pulse

**Generated:** 2026-09-21T17:17:15Z · **Schema:** `1.0.0` · **Collection time:** 14.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.62 | +7.08% |
| Market cap | $69.07B | rank #7 |
| Total value locked | $6.49B | +5.01% |
| Stablecoin supply | $15.91B | +0.65% |
| DEX volume (24h) | $2.80B | -2.81% |
| Chain fees / REV (24h) | $14.46M | -5.41% |
| Non-vote TPS (1h avg) | 2,769 | peak 5,805 total |
| Active validators | 676 | 14 delinquent |
| Epoch 1039 | 62.96% complete | 160,011 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 89 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 3 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 268.50 sits 19.2 sigma below the median of the last 89 runs (316.80, -15.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,485,485,561.00 sits 3.8 sigma above the median of the last 89 runs (5,852,308,147.00, +10.8%). | `zscore` |
| [WARNING] | SOL price is above its recent norm | Current 117.62 sits 3.4 sigma above the median of the last 89 runs (101.32, +16.1%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,768.7 average over the last 60 minutes; 2,761.1 in the latest sample.
- **Total TPS:** 5,276.6 average, 5,805.3 peak. Consensus votes account for 47.5% of all transactions.
- **Slot time:** 268.5 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 427,160,600 at absolute slot 449,119,989.
- **Epoch 1039:** slot 271,989 of 432,000 (62.96% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.638% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 187 ms |
| `solana-rpc.publicnode.com` | yes | 136 ms |
| `api.mainnet.solana.com` | yes | 93 ms |

## Validators & stake

- **676 active** validators, **14 delinquent** (2.03% by count, 0.045% by stake).
- **Total stake:** 439,905,519 SOL ($51.74B); stake rate 69.34% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.79% of active stake.
- **Commission:** median 5.0%, mean 12.54%; 239 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,856,583 | 4.061% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,828,384 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,518,302 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,252,588 | 2.559% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,788,818 | 2.226% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,354 | 2.104% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,106,985 | 2.071% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,443,840 | 1.693% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,088,079 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,572,007 | 1.495% | 0% |

## Economics

- **SOL:** $117.62 (+7.08% 24h, +14.68% 7d, +24.71% 30d). Market cap $69.07B, 24h volume $6.39B (9.25% of cap). Price source: `coingecko`.
- **TVL:** $6.49B across 333 protocols - rank #2 of 467 chains, 6.75% of all tracked chain TVL. +11.13% over 7d, -51.0% from its ATH.
- **Stablecoins:** $15.91B circulating on Solana (-2.73% 7d) - $2.45 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.80B in 24h, $19.83B over 7d across 125 venues. Volume/TVL turnover 0.431x per day.
- **REV (chain fees):** $14.46M in 24h, $420.98M over 30d. Retained chain revenue $5.35M (37.0% of fees). Annualised fees are 7.64% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,437,162 SOL circulating of 634,453,266 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.88B | +8.3% | +23.4% |
| 2 | Kamino Lend | Lending | $1.43B | +3.7% | +6.6% |
| 3 | Raydium AMM | Dexs | $1.32B | +7.4% | +16.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.23B | +8.7% | +18.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.22B | +8.2% | +19.5% |
| 6 | Jupiter Lend | Lending | $1.20B | +6.2% | +10.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $824.92M | +5.4% | +11.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $610.57M | +7.4% | +18.5% |
| 9 | Marinade Native | Staking Pool | $445.48M | +7.2% | +17.3% |
| 10 | PumpSwap | Dexs | $375.29M | +6.9% | +14.7% |
| 11 | Sentora Curator | Risk Curators | $362.81M | -0.4% | -6.8% |
| 12 | Drift Staked SOL | Liquid Staking | $333.07M | +8.6% | +18.7% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.81B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.3% · Dexs 15.6% · Derivatives 5.3% · Staking Pool 4.0% · RWA 3.5%

### Tokenised assets

$877.51M of tokenised real-world assets and equities are locked on Solana - 5.221% of chain TVL.

- OnRe (RWA): $306.26M
- Solstice (Basis Trading): $222.42M
- Huma Finance V2 (RWA): $204.19M
- JupUSD (Basis Trading): $46.66M
- Plume Vaults (RWA): $28.13M

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

- [SIMD-0649: SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) - updated 2026-09-21
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-21
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-21
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18

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

### Change over 24h (vs run at 2026-09-20T14:59:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,161.29 | 5,276.56 | +26.80% |
| Average non-vote TPS | 1,628.34 | 2,768.69 | +70.03% |
| Average slot time (ms) | 266.50 | 268.50 | +0.75% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 13.00 | 14.00 | +7.69% |
| Solana TVL | 6,119,687,070.00 | 6,485,485,561.00 | +5.98% |
| SOL price | 108.22 | 117.62 | +8.69% |
| Stablecoin supply | 15,803,956,899.00 | 15,907,718,208.00 | +0.66% |
| 24h DEX volume | 2,875,414,862.20 | 2,795,356,104.36 | -2.78% |
| 24h chain fees | 15,275,214.85 | 14,463,382.08 | -5.31% |

### Change over 7d (vs run at 2026-09-14T17:07:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,445.20 | 5,276.56 | +18.70% |
| Average non-vote TPS | 2,314.04 | 2,768.69 | +19.65% |
| Average slot time (ms) | 316.90 | 268.50 | -15.27% |
| Active validators | 680.00 | 676.00 | -0.59% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 5,897,760,887.00 | 6,485,485,561.00 | +9.97% |
| SOL price | 102.55 | 117.62 | +14.70% |
| Stablecoin supply | 16,352,410,301.00 | 15,907,718,208.00 | -2.72% |
| 24h DEX volume | 1,790,994,711.97 | 2,795,356,104.36 | +56.08% |
| 24h chain fees | 14,036,101.64 | 14,463,382.08 | +3.04% |

### Change over 30d (vs run at 2026-08-22T18:12:00Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,909.94 | 5,276.56 | +34.95% |
| Average non-vote TPS | 2,049.79 | 2,768.69 | +35.07% |
| Average slot time (ms) | 366.90 | 268.50 | -26.82% |
| Active validators | 687.00 | 676.00 | -1.60% |
| Delinquent validators | 8.00 | 14.00 | +75.00% |
| Solana TVL | 5,514,383,081.00 | 6,485,485,561.00 | +17.61% |
| SOL price | 94.15 | 117.62 | +24.93% |
| Stablecoin supply | 16,420,708,533.00 | 15,907,718,208.00 | -3.12% |
| 24h DEX volume | 3,600,948,276.22 | 2,795,356,104.36 | -22.37% |
| 24h chain fees | 13,332,529.88 | 14,463,382.08 | +8.48% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
