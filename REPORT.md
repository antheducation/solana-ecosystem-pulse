# Solana Ecosystem Pulse

**Generated:** 2026-10-14T21:02:19Z · **Schema:** `1.0.0` · **Collection time:** 18.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.03 | -2.84% |
| Market cap | $61.29B | rank #7 |
| Total value locked | $5.96B | -0.78% |
| Stablecoin supply | $16.32B | +1.61% |
| DEX volume (24h) | $2.50B | +11.80% |
| Chain fees / REV (24h) | $11.78M | -10.14% |
| Non-vote TPS (1h avg) | 2,374 | peak 6,093 total |
| Active validators | 673 | 5 delinquent |
| Epoch 1057 | 82.54% complete | 75,446 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 106 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,373.9 average over the last 60 minutes; 2,268.7 in the latest sample.
- **Total TPS:** 5,462.8 average, 6,093.2 peak. Consensus votes account for 56.5% of all transactions.
- **Slot time:** 216.9 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 435,016,722 at absolute slot 456,980,554.
- **Epoch 1057:** slot 356,554 of 432,000 (82.54% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.603% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 184 ms |
| `solana-rpc.publicnode.com` | yes | 463 ms |
| `api.mainnet.solana.com` | yes | 152 ms |

## Validators & stake

- **673 active** validators, **5 delinquent** (0.74% by count, 0.001% by stake).
- **Total stake:** 438,131,312 SOL ($45.58B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 12.95%; 229 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,794,097 | 4.061% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,830,160 | 3.613% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,027 | 2.810% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,142,984 | 2.543% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,763,192 | 2.457% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,407,225 | 2.147% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,434 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,700,931 | 1.758% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,906,931 | 1.576% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,868 | 1.515% | 0% |

## Economics

- **SOL:** $104.03 (-2.84% 24h, -10.43% 7d, +0.05% 30d). Market cap $61.29B, 24h volume $3.19B (5.21% of cap). Price source: `coingecko`.
- **TVL:** $5.96B across 323 protocols - rank #3 of 425 chains, 6.63% of all tracked chain TVL. -10.03% over 7d, -55.1% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (-2.47% 7d) - $2.74 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.50B in 24h, $14.12B over 7d across 133 venues. Volume/TVL turnover 0.419x per day.
- **REV (chain fees):** $11.78M in 24h, $465.43M over 30d. Retained chain revenue $4.26M (36.1% of fees). Annualised fees are 7.01% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,212,441 SOL circulating of 635,782,482 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.76B | -2.9% | -11.3% |
| 2 | Kamino Lend | Lending | $1.32B | +0.4% | -5.7% |
| 3 | Raydium AMM | Dexs | $1.18B | -3.0% | -12.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.09B | -3.3% | -13.1% |
| 5 | Jupiter Lend | Lending | $1.08B | -1.6% | -12.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.07B | -3.4% | -13.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $738.43M | -2.7% | -9.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $544.26M | -2.9% | -12.9% |
| 9 | Sentora Curator | Risk Curators | $456.93M | -3.2% | -7.1% |
| 10 | Marinade Native | Staking Pool | $381.53M | -4.1% | -15.1% |
| 11 | PumpSwap | Dexs | $349.67M | -2.5% | -12.7% |
| 12 | Orca DEX | Dexs | $301.19M | -0.5% | -6.0% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 323 protocols the total is $15.82B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 16.9% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.7%

### Tokenised assets

$866.32M of tokenised real-world assets and equities are locked on Solana - 5.477% of chain TVL.

- OnRe (RWA): $292.85M
- Huma (RWA): $253.52M
- Solstice (Basis Trading): $209.34M
- JupUSD (Basis Trading): $46.08M
- Plume Vaults (RWA): $33.89M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.3.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-14
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-14
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-14
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-14
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-14
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-14
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14

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

### Change over 24h (vs run at 2026-10-13T22:01:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,063.39 | 5,462.84 | +7.89% |
| Average non-vote TPS | 1,990.01 | 2,373.93 | +19.29% |
| Average slot time (ms) | 217.80 | 216.90 | -0.41% |
| Active validators | 673.00 | 673.00 | +0.00% |
| Delinquent validators | 7.00 | 5.00 | -28.57% |
| Solana TVL | 6,063,416,281.00 | 5,960,534,531.00 | -1.70% |
| SOL price | 107.01 | 104.03 | -2.78% |
| Stablecoin supply | 16,241,793,471.00 | 16,320,492,053.00 | +0.48% |
| 24h DEX volume | 2,231,842,381.02 | 2,495,170,004.38 | +11.80% |
| 24h chain fees | 13,103,539.72 | 11,775,288.16 | -10.14% |

### Change over 7d (vs run at 2026-10-07T22:21:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,609.27 | 5,462.84 | +18.52% |
| Average non-vote TPS | 2,129.60 | 2,373.93 | +11.47% |
| Average slot time (ms) | 269.60 | 216.90 | -19.55% |
| Active validators | 671.00 | 673.00 | +0.30% |
| Delinquent validators | 10.00 | 5.00 | -50.00% |
| Solana TVL | 6,453,092,289.00 | 5,960,534,531.00 | -7.63% |
| SOL price | 115.61 | 104.03 | -10.02% |
| Stablecoin supply | 16,914,576,986.00 | 16,320,492,053.00 | -3.51% |
| 24h DEX volume | 2,052,545,605.65 | 2,495,170,004.38 | +21.56% |
| 24h chain fees | 16,052,631.31 | 11,775,288.16 | -26.65% |

### Change over 30d (vs run at 2026-09-14T21:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,277.98 | 5,462.84 | +27.70% |
| Average non-vote TPS | 2,155.99 | 2,373.93 | +10.11% |
| Average slot time (ms) | 317.90 | 216.90 | -31.77% |
| Active validators | 678.00 | 673.00 | -0.74% |
| Delinquent validators | 12.00 | 5.00 | -58.33% |
| Solana TVL | 5,949,162,754.00 | 5,960,534,531.00 | +0.19% |
| SOL price | 103.65 | 104.03 | +0.37% |
| Stablecoin supply | 16,354,375,710.00 | 16,320,492,053.00 | -0.21% |
| 24h DEX volume | 1,790,994,711.97 | 2,495,170,004.38 | +39.32% |
| 24h chain fees | 14,036,101.64 | 11,775,288.16 | -16.11% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
