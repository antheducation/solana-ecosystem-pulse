# Solana Ecosystem Pulse

**Generated:** 2026-10-14T16:03:37Z · **Schema:** `1.0.0` · **Collection time:** 16.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.88 | -3.46% |
| Market cap | $61.21B | rank #7 |
| Total value locked | $5.96B | -0.53% |
| Stablecoin supply | $16.32B | +1.61% |
| DEX volume (24h) | $2.50B | +11.80% |
| Chain fees / REV (24h) | $11.65M | -11.10% |
| Non-vote TPS (1h avg) | 2,394 | peak 6,957 total |
| Active validators | 672 | 6 delinquent |
| Epoch 1057 | 63.40% complete | 158,100 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 106 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,393.7 average over the last 60 minutes; 2,425.0 in the latest sample.
- **Total TPS:** 5,476.8 average, 6,956.6 peak. Consensus votes account for 56.3% of all transactions.
- **Slot time:** 217.1 ms average (target 400 ms), worst 1-minute bucket 226.4 ms.
- **Block height:** 434,934,135 at absolute slot 456,897,900.
- **Epoch 1057:** slot 273,900 of 432,000 (63.40% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.603% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 167 ms |
| `solana-rpc.publicnode.com` | yes | 522 ms |
| `api.mainnet.solana.com` | yes | 110 ms |

## Validators & stake

- **672 active** validators, **6 delinquent** (0.88% by count, 0.018% by stake).
- **Total stake:** 438,131,312 SOL ($45.51B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,794,097 | 4.062% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,830,160 | 3.614% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,027 | 2.811% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,142,984 | 2.544% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,763,192 | 2.457% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,407,225 | 2.148% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,434 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,700,931 | 1.758% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,906,931 | 1.577% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,868 | 1.516% | 0% |

## Economics

- **SOL:** $103.88 (-3.46% 24h, -11.00% 7d, +1.89% 30d). Market cap $61.21B, 24h volume $3.15B (5.14% of cap). Price source: `coingecko`.
- **TVL:** $5.96B across 324 protocols - rank #3 of 425 chains, 6.62% of all tracked chain TVL. -9.81% over 7d, -55.0% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (-2.47% 7d) - $2.74 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.50B in 24h, $14.12B over 7d across 133 venues. Volume/TVL turnover 0.419x per day.
- **REV (chain fees):** $11.65M in 24h, $465.27M over 30d. Retained chain revenue $4.13M (35.5% of fees). Annualised fees are 6.95% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,212,687 SOL circulating of 635,782,728 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.75B | -1.7% | -11.5% |
| 2 | Kamino Lend | Lending | $1.31B | -0.0% | -6.4% |
| 3 | Raydium AMM | Dexs | $1.18B | -2.9% | -12.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.09B | -2.5% | -13.3% |
| 5 | Jupiter Lend | Lending | $1.08B | -2.6% | -12.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.07B | -1.5% | -13.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $748.23M | -0.5% | -8.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $542.91M | -1.8% | -13.1% |
| 9 | Sentora Curator | Risk Curators | $466.99M | -1.0% | -5.1% |
| 10 | Marinade Native | Staking Pool | $381.02M | -2.6% | -15.2% |
| 11 | PumpSwap | Dexs | $359.68M | +1.9% | -10.2% |
| 12 | Orca DEX | Dexs | $301.19M | -0.5% | -6.0% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 324 protocols the total is $15.83B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 16.8% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.2% · RWA 3.7%

### Tokenised assets

$855.93M of tokenised real-world assets and equities are locked on Solana - 5.407% of chain TVL.

- OnRe (RWA): $292.85M
- Huma (RWA): $243.07M
- Solstice (Basis Trading): $209.33M
- JupUSD (Basis Trading): $46.19M
- Plume Vaults (RWA): $33.83M

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

- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-13
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-13
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11

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

### Change over 24h (vs run at 2026-10-13T13:02:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,012.70 | 5,476.80 | +9.26% |
| Average non-vote TPS | 1,960.24 | 2,393.65 | +22.11% |
| Average slot time (ms) | 219.10 | 217.10 | -0.91% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 7.00 | 6.00 | -14.29% |
| Solana TVL | 6,068,456,089.00 | 5,957,694,019.00 | -1.83% |
| SOL price | 106.57 | 103.88 | -2.52% |
| Stablecoin supply | 16,241,381,985.00 | 16,320,610,416.00 | +0.49% |
| 24h DEX volume | 2,231,841,478.02 | 2,495,170,004.38 | +11.80% |
| 24h chain fees | 12,987,306.72 | 11,649,593.74 | -10.30% |

### Change over 7d (vs run at 2026-10-07T12:10:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,150.69 | 5,476.80 | +31.95% |
| Average non-vote TPS | 1,657.06 | 2,393.65 | +44.45% |
| Average slot time (ms) | 268.60 | 217.10 | -19.17% |
| Active validators | 670.00 | 672.00 | +0.30% |
| Delinquent validators | 11.00 | 6.00 | -45.45% |
| Solana TVL | 6,507,392,132.00 | 5,957,694,019.00 | -8.45% |
| SOL price | 117.28 | 103.88 | -11.43% |
| Stablecoin supply | 16,916,603,331.00 | 16,320,610,416.00 | -3.52% |
| 24h DEX volume | 2,052,545,605.65 | 2,495,170,004.38 | +21.56% |
| 24h chain fees | 16,043,229.31 | 11,649,593.74 | -27.39% |

### Change over 30d (vs run at 2026-09-14T21:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,277.98 | 5,476.80 | +28.02% |
| Average non-vote TPS | 2,155.99 | 2,393.65 | +11.02% |
| Average slot time (ms) | 317.90 | 217.10 | -31.71% |
| Active validators | 678.00 | 672.00 | -0.88% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 5,949,162,754.00 | 5,957,694,019.00 | +0.14% |
| SOL price | 103.65 | 103.88 | +0.22% |
| Stablecoin supply | 16,354,375,710.00 | 16,320,610,416.00 | -0.21% |
| 24h DEX volume | 1,790,994,711.97 | 2,495,170,004.38 | +39.32% |
| 24h chain fees | 14,036,101.64 | 11,649,593.74 | -17.00% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
