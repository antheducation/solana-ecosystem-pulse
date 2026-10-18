# Solana Ecosystem Pulse

**Generated:** 2026-10-18T14:59:03Z · **Schema:** `1.0.0` · **Collection time:** 16.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.92 | -2.23% |
| Market cap | $60.08B | rank #7 |
| Total value locked | $5.94B | -0.28% |
| Stablecoin supply | $15.90B | -0.84% |
| DEX volume (24h) | $1.25B | -42.23% |
| Chain fees / REV (24h) | $9.38M | -25.18% |
| Non-vote TPS (1h avg) | 1,988 | peak 5,979 total |
| Active validators | 669 | 11 delinquent |
| Epoch 1061 | 28.83% complete | 307,441 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 110 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 42.2% in 24h) | DEX volume changed -42.2% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,988.3 average over the last 60 minutes; 1,353.4 in the latest sample.
- **Total TPS:** 5,065.9 average, 5,979.2 peak. Consensus votes account for 60.8% of all transactions.
- **Slot time:** 216.0 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 436,511,805 at absolute slot 458,476,559.
- **Epoch 1061:** slot 124,559 of 432,000 (28.83% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.597% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 188 ms |
| `solana-rpc.publicnode.com` | yes | 149 ms |
| `api.mainnet.solana.com` | yes | 147 ms |

## Validators & stake

- **669 active** validators, **11 delinquent** (1.62% by count, 0.004% by stake).
- **Total stake:** 437,350,803 SOL ($44.57B); stake rate 68.76% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.97% of active stake.
- **Commission:** median 5.0%, mean 12.70%; 231 validators at 0% and 62 at 100%.

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

- **SOL:** $101.92 (-2.23% 24h, -6.80% 7d, -6.01% 30d). Market cap $60.08B, 24h volume $2.10B (3.50% of cap). Price source: `coingecko`.
- **TVL:** $5.94B across 326 protocols - rank #3 of 424 chains, 6.68% of all tracked chain TVL. -4.36% over 7d, -55.3% from its ATH.
- **Stablecoins:** $15.90B circulating on Solana (-2.04% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.25B in 24h, $14.34B over 7d across 136 venues. Volume/TVL turnover 0.211x per day.
- **REV (chain fees):** $9.38M in 24h, $455.73M over 30d. Retained chain revenue $3.54M (37.8% of fees). Annualised fees are 5.70% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,438,250 SOL circulating of 636,029,015 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -1.3% | -1.5% |
| 2 | Kamino Lend | Lending | $1.32B | +0.8% | -0.8% |
| 3 | Raydium AMM | Dexs | $1.17B | -0.3% | -5.8% |
| 4 | Jupiter Lend | Lending | $1.09B | +0.2% | -4.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.09B | -0.1% | -5.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.09B | +0.2% | -3.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $732.79M | -0.7% | -4.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $542.86M | -0.2% | -4.5% |
| 9 | Sentora Curator | Risk Curators | $450.91M | -0.1% | -8.1% |
| 10 | Marinade Native | Staking Pool | $375.42M | -1.4% | -7.8% |
| 11 | PumpSwap | Dexs | $347.45M | -0.5% | -5.4% |
| 12 | Orca DEX | Dexs | $298.25M | -0.3% | -3.9% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 326 protocols the total is $15.86B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 16.9% · Dexs 15.2% · Derivatives 5.0% · Risk Curators 4.1% · RWA 3.9%

### Tokenised assets

$892.77M of tokenised real-world assets and equities are locked on Solana - 5.631% of chain TVL.

- OnRe (RWA): $293.59M
- Huma (RWA): $280.44M
- Solstice (Basis Trading): $209.29M
- JupUSD (Basis Trading): $43.90M
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

### Change over 24h (vs run at 2026-10-17T14:31:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,884.13 | 5,065.94 | +3.72% |
| Average non-vote TPS | 1,806.58 | 1,988.30 | +10.06% |
| Average slot time (ms) | 216.70 | 216.00 | -0.32% |
| Active validators | 670.00 | 669.00 | -0.15% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 5,952,090,339.00 | 5,938,643,989.00 | -0.23% |
| SOL price | 104.23 | 101.92 | -2.22% |
| Stablecoin supply | 16,028,651,978.00 | 15,896,205,330.00 | -0.83% |
| 24h DEX volume | 2,168,129,752.12 | 1,252,516,756.55 | -42.23% |
| 24h chain fees | 12,431,928.33 | 9,375,340.79 | -24.59% |

### Change over 7d (vs run at 2026-10-11T16:52:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,142.69 | 5,065.94 | -1.49% |
| Average non-vote TPS | 2,086.39 | 1,988.30 | -4.70% |
| Average slot time (ms) | 219.10 | 216.00 | -1.41% |
| Active validators | 672.00 | 669.00 | -0.45% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 6,198,096,411.00 | 5,938,643,989.00 | -4.19% |
| SOL price | 112.23 | 101.92 | -9.19% |
| Stablecoin supply | 16,404,664,615.00 | 15,896,205,330.00 | -3.10% |
| 24h DEX volume | 1,286,316,590.57 | 1,252,516,756.55 | -2.63% |
| 24h chain fees | 11,936,417.92 | 9,375,340.79 | -21.46% |

### Change over 30d (vs run at 2026-09-18T20:04:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,950.64 | 5,065.94 | +2.33% |
| Average non-vote TPS | 2,440.09 | 1,988.30 | -18.52% |
| Average slot time (ms) | 267.70 | 216.00 | -19.31% |
| Active validators | 676.00 | 669.00 | -1.04% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 6,242,343,437.00 | 5,938,643,989.00 | -4.87% |
| SOL price | 113.98 | 101.92 | -10.58% |
| Stablecoin supply | 15,713,039,562.00 | 15,896,205,330.00 | +1.17% |
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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
