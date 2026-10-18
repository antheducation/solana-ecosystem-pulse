# Solana Ecosystem Pulse

**Generated:** 2026-10-18T19:46:35Z · **Schema:** `1.0.0` · **Collection time:** 15.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.82 | -3.09% |
| Market cap | $59.42B | rank #7 |
| Total value locked | $5.88B | -1.35% |
| Stablecoin supply | $15.90B | -0.83% |
| DEX volume (24h) | $1.25B | -42.23% |
| Chain fees / REV (24h) | $9.38M | -25.18% |
| Non-vote TPS (1h avg) | 1,911 | peak 6,293 total |
| Active validators | 668 | 12 delinquent |
| Epoch 1061 | 47.23% complete | 227,958 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 110 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 42.2% in 24h) | DEX volume changed -42.2% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,911.4 average over the last 60 minutes; 2,813.0 in the latest sample.
- **Total TPS:** 4,974.5 average, 6,292.9 peak. Consensus votes account for 61.6% of all transactions.
- **Slot time:** 217.1 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 436,591,288 at absolute slot 458,556,042.
- **Epoch 1061:** slot 204,042 of 432,000 (47.23% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.597% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 156 ms |
| `solana-rpc.publicnode.com` | yes | 117 ms |
| `api.mainnet.solana.com` | yes | 117 ms |

## Validators & stake

- **668 active** validators, **12 delinquent** (1.76% by count, 0.004% by stake).
- **Total stake:** 437,350,803 SOL ($44.09B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.97% of active stake.
- **Commission:** median 5.0%, mean 12.85%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,091,304 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,762,758 | 3.604% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,730 | 2.864% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,974,352 | 2.509% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,484 | 2.222% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,253 | 2.165% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,251,164 | 2.115% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,774,268 | 1.778% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,992,811 | 1.599% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,730,670 | 1.539% | 0% |

## Economics

- **SOL:** $100.82 (-3.09% 24h, -9.54% 7d, -10.12% 30d). Market cap $59.42B, 24h volume $2.16B (3.64% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 326 protocols - rank #3 of 420 chains, 6.66% of all tracked chain TVL. -5.39% over 7d, -55.8% from its ATH.
- **Stablecoins:** $15.90B circulating on Solana (-2.02% 7d) - $2.71 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.25B in 24h, $14.34B over 7d across 136 venues. Volume/TVL turnover 0.213x per day.
- **REV (chain fees):** $9.38M in 24h, $455.73M over 30d. Retained chain revenue $3.54M (37.8% of fees). Annualised fees are 5.76% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,438,019 SOL circulating of 636,028,784 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -1.1% | -1.9% |
| 2 | Kamino Lend | Lending | $1.31B | +0.1% | -1.6% |
| 3 | Raydium AMM | Dexs | $1.15B | -1.5% | -7.4% |
| 4 | Jupiter Lend | Lending | $1.08B | -0.9% | -5.3% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.07B | -1.0% | -6.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.07B | -1.0% | -5.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $729.24M | -0.7% | -5.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $534.40M | -1.1% | -6.0% |
| 9 | Sentora Curator | Risk Curators | $450.84M | -0.0% | -8.2% |
| 10 | Marinade Native | Staking Pool | $373.60M | -1.1% | -8.2% |
| 11 | PumpSwap | Dexs | $341.87M | -1.9% | -6.9% |
| 12 | Orca DEX | Dexs | $296.17M | -0.5% | -4.6% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 326 protocols the total is $15.70B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 16.9% · Dexs 15.1% · Derivatives 5.1% · Risk Curators 4.1% · RWA 4.0%

### Tokenised assets

$892.78M of tokenised real-world assets and equities are locked on Solana - 5.687% of chain TVL.

- OnRe (RWA): $293.63M
- Huma (RWA): $280.44M
- Solstice (Basis Trading): $209.26M
- JupUSD (Basis Trading): $43.91M
- Plume Vaults (RWA): $35.78M

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

### Change over 24h (vs run at 2026-10-17T19:45:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,823.29 | 4,974.46 | +3.13% |
| Average non-vote TPS | 1,758.64 | 1,911.38 | +8.69% |
| Average slot time (ms) | 217.70 | 217.10 | -0.28% |
| Active validators | 670.00 | 668.00 | -0.30% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 5,922,304,891.00 | 5,875,275,842.00 | -0.79% |
| SOL price | 104.07 | 100.82 | -3.12% |
| Stablecoin supply | 16,030,558,263.00 | 15,898,071,483.00 | -0.83% |
| 24h DEX volume | 2,168,129,752.12 | 1,252,516,756.55 | -42.23% |
| 24h chain fees | 12,431,928.33 | 9,375,340.79 | -24.59% |

### Change over 7d (vs run at 2026-10-11T21:08:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.95 | 4,974.46 | -0.01% |
| Average non-vote TPS | 1,917.24 | 1,911.38 | -0.31% |
| Average slot time (ms) | 218.90 | 217.10 | -0.82% |
| Active validators | 672.00 | 668.00 | -0.60% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 6,251,230,542.00 | 5,875,275,842.00 | -6.01% |
| SOL price | 110.93 | 100.82 | -9.11% |
| Stablecoin supply | 16,405,817,670.00 | 15,898,071,483.00 | -3.09% |
| 24h DEX volume | 1,286,316,590.57 | 1,252,516,756.55 | -2.63% |
| 24h chain fees | 11,936,417.92 | 9,375,340.79 | -21.46% |

### Change over 30d (vs run at 2026-09-18T20:04:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,950.64 | 4,974.46 | +0.48% |
| Average non-vote TPS | 2,440.09 | 1,911.38 | -21.67% |
| Average slot time (ms) | 267.70 | 217.10 | -18.90% |
| Active validators | 676.00 | 668.00 | -1.18% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 6,242,343,437.00 | 5,875,275,842.00 | -5.88% |
| SOL price | 113.98 | 100.82 | -11.55% |
| Stablecoin supply | 15,713,039,562.00 | 15,898,071,483.00 | +1.18% |
| 24h DEX volume | 2,592,123,183.29 | 1,252,516,756.55 | -51.68% |
| 24h chain fees | 14,675,830.10 | 9,375,340.79 | -36.12% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
