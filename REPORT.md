# Solana Ecosystem Pulse

**Generated:** 2026-09-24T01:53:02Z · **Schema:** `1.0.0` · **Collection time:** 12.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $114.66 | -2.86% |
| Market cap | $67.39B | rank #7 |
| Total value locked | $6.39B | -0.61% |
| Stablecoin supply | $16.43B | -2.68% |
| DEX volume (24h) | $2.68B | -16.03% |
| Chain fees / REV (24h) | $17.13M | -4.19% |
| Non-vote TPS (1h avg) | 1,983 | peak 5,161 total |
| Active validators | 675 | 12 delinquent |
| Epoch 1041 | 40.04% complete | 259,014 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 91 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 265.70 sits 7.1 sigma below the median of the last 91 runs (316.50, -16.1%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,982.8 average over the last 60 minutes; 2,002.8 in the latest sample.
- **Total TPS:** 4,513.6 average, 5,161.5 peak. Consensus votes account for 56.1% of all transactions.
- **Slot time:** 265.7 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 427,925,127 at absolute slot 449,884,986.
- **Epoch 1041:** slot 172,986 of 432,000 (40.04% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 96 ms |
| `solana-rpc.publicnode.com` | yes | 74 ms |
| `api.mainnet.solana.com` | yes | 112 ms |

## Validators & stake

- **675 active** validators, **12 delinquent** (1.75% by count, 0.054% by stake).
- **Total stake:** 439,964,137 SOL ($50.45B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.88% of active stake.
- **Commission:** median 5.0%, mean 12.31%; 236 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.058% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.350% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.098% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.083% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.729% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.491% | 0% |

## Economics

- **SOL:** $114.66 (-2.86% 24h, +16.24% 7d, +12.69% 30d). Market cap $67.39B, 24h volume $5.15B (7.65% of cap). Price source: `coingecko`.
- **TVL:** $6.39B across 332 protocols - rank #2 of 467 chains, 6.73% of all tracked chain TVL. +10.54% over 7d, -51.7% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+4.15% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.68B in 24h, $19.96B over 7d across 125 venues. Volume/TVL turnover 0.420x per day.
- **REV (chain fees):** $17.13M in 24h, $423.22M over 30d. Retained chain revenue $6.57M (38.4% of fees). Annualised fees are 9.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,577,611 SOL circulating of 634,608,723 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.8% | +17.7% |
| 2 | Kamino Lend | Lending | $1.41B | -1.4% | +5.4% |
| 3 | Raydium AMM | Dexs | $1.30B | -2.7% | +16.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.19B | -2.8% | +16.8% |
| 5 | Binance Staked SOL | Liquid Staking | $1.18B | -3.0% | +15.0% |
| 6 | Jupiter Lend | Lending | $1.17B | -1.6% | +9.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $804.31M | -2.2% | +9.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $596.92M | -2.6% | +17.3% |
| 9 | Marinade Native | Staking Pool | $442.71M | -2.2% | +17.7% |
| 10 | PumpSwap | Dexs | $372.54M | -3.4% | +16.1% |
| 11 | Sentora Curator | Risk Curators | $362.34M | -0.2% | -2.7% |
| 12 | Drift Staked SOL | Liquid Staking | $324.90M | -2.8% | +16.9% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.51B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 17.4% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.0% · Risk Curators 3.5%

### Tokenised assets

$836.02M of tokenised real-world assets and equities are locked on Solana - 5.064% of chain TVL.

- OnRe (RWA): $301.08M
- Solstice (Basis Trading): $218.07M
- Huma (RWA): $197.05M
- JupUSD (Basis Trading): $45.09M
- Plume Vaults (RWA): $28.21M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-24
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-23
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0249: SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-23T02:05:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,466.71 | 4,513.62 | +1.05% |
| Average non-vote TPS | 1,931.92 | 1,982.83 | +2.64% |
| Average slot time (ms) | 265.70 | 265.70 | +0.00% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 6,520,724,463.00 | 6,391,344,724.00 | -1.98% |
| SOL price | 118.05 | 114.66 | -2.87% |
| Stablecoin supply | 16,881,209,444.00 | 16,427,876,539.00 | -2.69% |
| 24h DEX volume | 3,448,899,396.17 | 2,682,816,608.00 | -22.21% |
| 24h chain fees | 17,581,633.45 | 17,125,745.95 | -2.59% |

### Change over 7d (vs run at 2026-09-17T02:03:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,281.28 | 4,513.62 | +5.43% |
| Average non-vote TPS | 2,153.15 | 1,982.83 | -7.91% |
| Average slot time (ms) | 317.20 | 265.70 | -16.24% |
| Active validators | 679.00 | 675.00 | -0.59% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,738,424,911.00 | 6,391,344,724.00 | +11.38% |
| SOL price | 99.21 | 114.66 | +15.57% |
| Stablecoin supply | 15,774,289,704.00 | 16,427,876,539.00 | +4.14% |
| 24h DEX volume | 2,733,437,291.18 | 2,682,816,608.00 | -1.85% |
| 24h chain fees | 14,036,672.88 | 17,125,745.95 | +22.01% |

### Change over 30d (vs run at 2026-08-24T18:21:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,568.13 | 4,513.62 | -1.19% |
| Average non-vote TPS | 2,714.40 | 1,982.83 | -26.95% |
| Average slot time (ms) | 367.20 | 265.70 | -27.64% |
| Active validators | 685.00 | 675.00 | -1.46% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,621,355,422.00 | 6,391,344,724.00 | +13.70% |
| SOL price | 96.29 | 114.66 | +19.08% |
| Stablecoin supply | 16,453,918,497.00 | 16,427,876,539.00 | -0.16% |
| 24h DEX volume | 2,938,613,605.25 | 2,682,816,608.00 | -8.70% |
| 24h chain fees | 12,654,048.70 | 17,125,745.95 | +35.34% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
