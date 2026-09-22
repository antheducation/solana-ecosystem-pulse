# Solana Ecosystem Pulse

**Generated:** 2026-09-22T15:50:27Z · **Schema:** `1.0.0` · **Collection time:** 17.0s · **Sources OK:** 39/39

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $117.67 | -0.50% |
| Market cap | $69.12B | rank #7 |
| Total value locked | $6.47B | +4.21% |
| Stablecoin supply | $17.17B | +7.96% |
| DEX volume (24h) | $3.43B | +22.67% |
| Chain fees / REV (24h) | $18.64M | +26.21% |
| Non-vote TPS (1h avg) | 2,345 | peak 5,245 total |
| Active validators | 676 | 13 delinquent |
| Epoch 1040 | 33.38% complete | 287,804 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 90 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 8.0% in 24h) | Stablecoin supply changed +8.0% over the last day, past the 3% alert band. | `threshold` |
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 268.40 sits 16.7 sigma below the median of the last 90 runs (316.75, -15.3%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,467,273,208.00 sits 3.5 sigma above the median of the last 90 runs (5,855,155,696.50, +10.5%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,344.7 average over the last 60 minutes; 2,368.0 in the latest sample.
- **Total TPS:** 4,849.2 average, 5,244.5 peak. Consensus votes account for 51.6% of all transactions.
- **Slot time:** 268.4 ms average (target 400 ms), worst 1-minute bucket 281.7 ms.
- **Block height:** 427,464,558 at absolute slot 449,424,196.
- **Epoch 1040:** slot 144,196 of 432,000 (33.38% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.636% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 299 ms |
| `solana-rpc.publicnode.com` | yes | 173 ms |
| `api.mainnet.solana.com` | yes | 151 ms |

## Validators & stake

- **676 active** validators, **13 delinquent** (1.89% by count, 0.124% by stake).
- **Total stake:** 439,861,749 SOL ($51.76B); stake rate 69.32% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.40%; 239 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,826,722 | 4.058% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,698 | 3.606% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,354,353 | 2.812% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,265,429 | 2.564% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,210,832 | 2.324% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,211,356 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,144,102 | 2.081% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,458,789 | 1.698% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,089,342 | 1.614% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,555,722 | 1.492% | 0% |

## Economics

- **SOL:** $117.67 (-0.50% 24h, +19.05% 7d, +23.83% 30d). Market cap $69.12B, 24h volume $5.08B (7.35% of cap). Price source: `coingecko`.
- **TVL:** $6.47B across 332 protocols - rank #2 of 467 chains, 6.72% of all tracked chain TVL. +9.27% over 7d, -51.1% from its ATH.
- **Stablecoins:** $17.17B circulating on Solana (+4.78% 7d) - $2.66 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.43B in 24h, $20.73B over 7d across 125 venues. Volume/TVL turnover 0.530x per day.
- **REV (chain fees):** $18.64M in 24h, $428.70M over 30d. Retained chain revenue $7.79M (41.8% of fees). Annualised fees are 9.85% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,507,634 SOL circulating of 634,531,262 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.87B | -1.2% | +19.0% |
| 2 | Kamino Lend | Lending | $1.42B | -0.4% | +4.6% |
| 3 | Raydium AMM | Dexs | $1.33B | +0.5% | +16.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.21B | -1.3% | +15.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | -2.4% | +12.9% |
| 6 | Jupiter Lend | Lending | $1.18B | -1.6% | +6.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $815.01M | -1.9% | +8.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $605.75M | -0.8% | +14.2% |
| 9 | Marinade Native | Staking Pool | $447.40M | +0.3% | +14.6% |
| 10 | PumpSwap | Dexs | $379.67M | +1.2% | +14.3% |
| 11 | Sentora Curator | Risk Curators | $363.54M | +0.2% | -5.1% |
| 12 | Drift Staked SOL | Liquid Staking | $330.17M | -1.0% | +14.4% |

The top five protocols hold 42.2% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.65B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 17.3% · Dexs 15.9% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$816.38M of tokenised real-world assets and equities are locked on Solana - 4.903% of chain TVL.

- OnRe (RWA): $302.62M
- Solstice (Basis Trading): $218.99M
- Huma Finance V2 (RWA): $177.65M
- JupUSD (Basis Trading): $46.66M
- Plume Vaults (RWA): $28.21M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 1 sampled blocks, an average of **812.0 unique fee payers** signed per block (812 distinct addresses in the union, 0.0% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

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

- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-22
- [SIMD-0558: SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-21
- [SIMD-0558: amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-21
- [SIMD-0649: SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) - updated 2026-09-21
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-21
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19

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

### Change over 24h (vs run at 2026-09-21T17:17:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,276.56 | 4,849.16 | -8.10% |
| Average non-vote TPS | 2,768.69 | 2,344.69 | -15.31% |
| Average slot time (ms) | 268.50 | 268.40 | -0.04% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 6,485,485,561.00 | 6,467,273,208.00 | -0.28% |
| SOL price | 117.62 | 117.67 | +0.04% |
| Stablecoin supply | 15,907,718,208.00 | 17,171,768,101.00 | +7.95% |
| 24h DEX volume | 2,795,356,104.36 | 3,428,858,820.75 | +22.66% |
| 24h chain fees | 14,463,382.08 | 18,642,402.21 | +28.89% |

### Change over 7d (vs run at 2026-09-15T15:48:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,388.88 | 4,849.16 | +10.49% |
| Average non-vote TPS | 2,261.36 | 2,344.69 | +3.68% |
| Average slot time (ms) | 316.50 | 268.40 | -15.20% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 5,835,026,620.00 | 6,467,273,208.00 | +10.84% |
| SOL price | 99.39 | 117.67 | +18.39% |
| Stablecoin supply | 16,387,600,113.00 | 17,171,768,101.00 | +4.79% |
| 24h DEX volume | 2,530,223,236.85 | 3,428,858,820.75 | +35.52% |
| 24h chain fees | 13,579,959.58 | 18,642,402.21 | +37.28% |

### Change over 30d (vs run at 2026-08-23T18:11:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,174.50 | 4,849.16 | +16.16% |
| Average non-vote TPS | 2,325.35 | 2,344.69 | +0.83% |
| Average slot time (ms) | 365.10 | 268.40 | -26.49% |
| Active validators | 681.00 | 676.00 | -0.73% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,593,098,038.00 | 6,467,273,208.00 | +15.63% |
| SOL price | 94.99 | 117.67 | +23.88% |
| Stablecoin supply | 16,372,086,266.00 | 17,171,768,101.00 | +4.88% |
| 24h DEX volume | 3,732,294,477.70 | 3,428,858,820.75 | -8.13% |
| 24h chain fees | 12,017,709.26 | 18,642,402.21 | +55.12% |

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

This run made 39 HTTP calls (39 succeeded, 0 failed) in 16.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
