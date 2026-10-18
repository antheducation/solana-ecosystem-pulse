# Solana Ecosystem Pulse

**Generated:** 2026-10-18T01:48:00Z · **Schema:** `1.0.0` · **Collection time:** 11.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.05 | -0.24% |
| Market cap | $61.35B | rank #7 |
| Total value locked | $5.88B | -0.03% |
| Stablecoin supply | $15.90B | -0.84% |
| DEX volume (24h) | $1.51B | -30.14% |
| Chain fees / REV (24h) | $9.32M | -25.52% |
| Non-vote TPS (1h avg) | 1,736 | peak 5,944 total |
| Active validators | 669 | 12 delinquent |
| Epoch 1060 | 78.12% complete | 94,502 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 109 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,736.1 average over the last 60 minutes; 2,068.9 in the latest sample.
- **Total TPS:** 4,812.8 average, 5,944.4 peak. Consensus votes account for 63.9% of all transactions.
- **Slot time:** 216.7 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 436,292,811 at absolute slot 458,257,498.
- **Epoch 1060:** slot 337,498 of 432,000 (78.12% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.598% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 82 ms |
| `solana-rpc.publicnode.com` | yes | 36 ms |
| `api.mainnet.solana.com` | yes | 113 ms |

## Validators & stake

- **669 active** validators, **12 delinquent** (1.76% by count, 0.038% by stake).
- **Total stake:** 438,750,365 SOL ($45.65B); stake rate 68.99% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.42% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,532,933 | 3.998% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,736,568 | 3.588% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,161 | 2.847% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,972,883 | 2.502% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,191,942 | 2.324% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,445,787 | 2.154% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,250,229 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,759,724 | 1.769% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,991,827 | 1.594% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,726,220 | 1.534% | 0% |

## Economics

- **SOL:** $104.05 (-0.24% 24h, -5.26% 7d, +2.70% 30d). Market cap $61.35B, 24h volume $1.80B (2.93% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 326 protocols - rank #3 of 425 chains, 6.66% of all tracked chain TVL. -5.27% over 7d, -55.7% from its ATH.
- **Stablecoins:** $15.90B circulating on Solana (-2.03% 7d) - $2.70 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.51B in 24h, $13.74B over 7d across 136 venues. Volume/TVL turnover 0.257x per day.
- **REV (chain fees):** $9.32M in 24h, $455.20M over 30d. Retained chain revenue $3.58M (38.5% of fees). Annualised fees are 5.54% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,381,908 SOL circulating of 635,966,943 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | -1.2% | -1.2% |
| 2 | Kamino Lend | Lending | $1.28B | -1.9% | -3.3% |
| 3 | Raydium AMM | Dexs | $1.16B | -1.3% | -6.5% |
| 4 | Jupiter Lend | Lending | $1.08B | -0.6% | -5.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.08B | -1.2% | -6.0% |
| 6 | Binance Staked SOL | Liquid Staking | $1.08B | -1.0% | -4.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $732.52M | -0.8% | -5.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $539.63M | -1.1% | -5.1% |
| 9 | Sentora Curator | Risk Curators | $450.74M | -0.1% | -8.2% |
| 10 | Marinade Native | Staking Pool | $377.31M | -1.1% | -7.3% |
| 11 | PumpSwap | Dexs | $343.74M | -2.4% | -6.4% |
| 12 | Orca DEX | Dexs | $297.09M | -0.7% | -4.3% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 326 protocols the total is $15.77B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.7% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.9%

### Tokenised assets

$892.61M of tokenised real-world assets and equities are locked on Solana - 5.662% of chain TVL.

- OnRe (RWA): $293.46M
- Huma (RWA): $280.54M
- Solstice (Basis Trading): $209.32M
- JupUSD (Basis Trading): $43.98M
- Plume Vaults (RWA): $35.51M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-17
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-17
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-16
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-16
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-15
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-15
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-15

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

### Change over 24h (vs run at 2026-10-17T01:49:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,892.76 | 4,812.84 | -1.63% |
| Average non-vote TPS | 1,831.42 | 1,736.06 | -5.21% |
| Average slot time (ms) | 216.30 | 216.70 | +0.18% |
| Active validators | 671.00 | 669.00 | -0.30% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,951,786,169.00 | 5,882,315,364.00 | -1.17% |
| SOL price | 104.30 | 104.05 | -0.24% |
| Stablecoin supply | 16,032,051,625.00 | 15,897,345,176.00 | -0.84% |
| 24h DEX volume | 1,921,217,321.11 | 1,514,642,363.55 | -21.16% |
| 24h chain fees | 12,415,523.82 | 9,315,995.67 | -24.96% |

### Change over 7d (vs run at 2026-10-11T02:30:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,606.30 | 4,812.84 | +4.48% |
| Average non-vote TPS | 1,517.17 | 1,736.06 | +14.43% |
| Average slot time (ms) | 217.60 | 216.70 | -0.41% |
| Active validators | 674.00 | 669.00 | -0.74% |
| Delinquent validators | 6.00 | 12.00 | +100.00% |
| Solana TVL | 6,218,958,410.00 | 5,882,315,364.00 | -5.41% |
| SOL price | 109.93 | 104.05 | -5.35% |
| Stablecoin supply | 16,409,963,032.00 | 15,897,345,176.00 | -3.12% |
| 24h DEX volume | 1,579,981,826.57 | 1,514,642,363.55 | -4.14% |
| 24h chain fees | 11,975,476.33 | 9,315,995.67 | -22.21% |

### Change over 30d (vs run at 2026-09-17T20:39:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,673.89 | 4,812.84 | +2.97% |
| Average non-vote TPS | 2,551.83 | 1,736.06 | -31.97% |
| Average slot time (ms) | 318.10 | 216.70 | -31.88% |
| Active validators | 677.00 | 669.00 | -1.18% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,865,883,806.00 | 5,882,315,364.00 | +0.28% |
| SOL price | 101.14 | 104.05 | +2.88% |
| Stablecoin supply | 15,774,027,557.00 | 15,897,345,176.00 | +0.78% |
| 24h DEX volume | 2,800,249,070.18 | 1,514,642,363.55 | -45.91% |
| 24h chain fees | 14,069,098.05 | 9,315,995.67 | -33.78% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
