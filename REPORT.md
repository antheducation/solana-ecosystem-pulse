# Solana Ecosystem Pulse

**Generated:** 2026-09-23T02:05:01Z · **Schema:** `1.0.0` · **Collection time:** 18.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.05 | +0.53% |
| Market cap | $69.38B | rank #7 |
| Total value locked | $6.52B | +0.44% |
| Stablecoin supply | $16.88B | -1.70% |
| DEX volume (24h) | $3.45B | +0.58% |
| Chain fees / REV (24h) | $17.58M | -5.67% |
| Non-vote TPS (1h avg) | 1,932 | peak 5,107 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1040 | 65.32% complete | 149,830 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 90 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 265.70 sits 15.6 sigma below the median of the last 90 runs (316.70, -16.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,520,724,463.00 sits 3.4 sigma above the median of the last 90 runs (5,856,923,697.00, +11.3%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,931.9 average over the last 60 minutes; 1,730.6 in the latest sample.
- **Total TPS:** 4,466.7 average, 5,106.9 peak. Consensus votes account for 56.7% of all transactions.
- **Slot time:** 265.7 ms average (target 400 ms), worst 1-minute bucket 272.7 ms.
- **Block height:** 427,602,475 at absolute slot 449,562,170.
- **Epoch 1040:** slot 282,170 of 432,000 (65.32% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.636% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 129 ms |
| `solana-rpc.publicnode.com` | yes | 138 ms |
| `api.mainnet.solana.com` | yes | 227 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.045% by stake).
- **Total stake:** 439,861,749 SOL ($51.93B); stake rate 69.32% of total supply.
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

- **SOL:** $118.05 (+0.53% 24h, +22.42% 7d, +25.69% 30d). Market cap $69.38B, 24h volume $4.53B (6.52% of cap). Price source: `coingecko`.
- **TVL:** $6.52B across 332 protocols - rank #2 of 467 chains, 6.75% of all tracked chain TVL. +13.90% over 7d, -50.7% from its ATH.
- **Stablecoins:** $16.88B circulating on Solana (+5.73% 7d) - $2.59 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.45B in 24h, $20.08B over 7d across 125 venues. Volume/TVL turnover 0.529x per day.
- **REV (chain fees):** $17.58M in 24h, $420.69M over 30d. Retained chain revenue $7.18M (40.9% of fees). Annualised fees are 9.25% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,507,182 SOL circulating of 634,530,810 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.89B | -0.6% | +22.7% |
| 2 | Kamino Lend | Lending | $1.43B | +0.6% | +7.7% |
| 3 | Raydium AMM | Dexs | $1.34B | -0.7% | +22.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.23B | -0.1% | +22.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.21B | -1.5% | +20.7% |
| 6 | Jupiter Lend | Lending | $1.19B | +1.9% | +10.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $822.34M | -0.4% | +12.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $613.10M | -0.1% | +22.1% |
| 9 | Marinade Native | Staking Pool | $452.83M | +0.4% | +22.4% |
| 10 | PumpSwap | Dexs | $385.76M | +2.4% | +22.9% |
| 11 | Sentora Curator | Risk Curators | $362.98M | +0.1% | -5.2% |
| 12 | Drift Staked SOL | Liquid Staking | $334.16M | -0.1% | +22.2% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.83B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.3% · Dexs 15.9% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$826.80M of tokenised real-world assets and equities are locked on Solana - 4.913% of chain TVL.

- OnRe (RWA): $302.73M
- Solstice (Basis Trading): $218.08M
- Huma Finance V2 (RWA): $188.38M
- JupUSD (Basis Trading): $46.67M
- Plume Vaults (RWA): $28.21M

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

- [SIMD-0558: SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22
- [Fix broken markdown, stale references and typos across several SIMDs](https://github.com/solana-foundation/solana-improvement-documents/pull/668) - updated 2026-09-22
- [SIMD-0385: SIMD-0385 / 0388 / 0204: fix inconsistent field and constant names](https://github.com/solana-foundation/solana-improvement-documents/pull/666) - updated 2026-09-22
- [SIMD-0118: Fix dead links in SIMD-0118, 0153, 0183, 0204, 0266, 0553](https://github.com/solana-foundation/solana-improvement-documents/pull/665) - updated 2026-09-22
- [ci: move checkout/setup-node off the deprecated Node 20 runtime, lint on Node 24](https://github.com/solana-foundation/solana-improvement-documents/pull/664) - updated 2026-09-22
- [Linter: match type exactly; template: add status; README: document Advisory](https://github.com/solana-foundation/solana-improvement-documents/pull/663) - updated 2026-09-22
- [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-22
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-22

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

### Change over 24h (vs run at 2026-09-22T02:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,603.17 | 4,466.71 | -2.96% |
| Average non-vote TPS | 2,079.85 | 1,931.92 | -7.11% |
| Average slot time (ms) | 267.00 | 265.70 | -0.49% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 6,481,815,506.00 | 6,520,724,463.00 | +0.60% |
| SOL price | 117.51 | 118.05 | +0.46% |
| Stablecoin supply | 17,171,514,140.00 | 16,881,209,444.00 | -1.69% |
| 24h DEX volume | 3,370,332,429.75 | 3,448,899,396.17 | +2.33% |
| 24h chain fees | 17,586,862.12 | 17,581,633.45 | -0.03% |

### Change over 7d (vs run at 2026-09-16T01:59:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,022.26 | 4,466.71 | -11.06% |
| Average non-vote TPS | 2,919.81 | 1,931.92 | -33.83% |
| Average slot time (ms) | 319.70 | 265.70 | -16.89% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,720,302,510.00 | 6,520,724,463.00 | +13.99% |
| SOL price | 96.37 | 118.05 | +22.50% |
| Stablecoin supply | 15,965,873,344.00 | 16,881,209,444.00 | +5.73% |
| 24h DEX volume | 2,497,627,822.22 | 3,448,899,396.17 | +38.09% |
| 24h chain fees | 13,951,641.96 | 17,581,633.45 | +26.02% |

### Change over 30d (vs run at 2026-08-23T18:11:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,174.50 | 4,466.71 | +7.00% |
| Average non-vote TPS | 2,325.35 | 1,931.92 | -16.92% |
| Average slot time (ms) | 365.10 | 265.70 | -27.23% |
| Active validators | 681.00 | 677.00 | -0.59% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 5,593,098,038.00 | 6,520,724,463.00 | +16.59% |
| SOL price | 94.99 | 118.05 | +24.28% |
| Stablecoin supply | 16,372,086,266.00 | 16,881,209,444.00 | +3.11% |
| 24h DEX volume | 3,732,294,477.70 | 3,448,899,396.17 | -7.59% |
| 24h chain fees | 12,017,709.26 | 17,581,633.45 | +46.30% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
