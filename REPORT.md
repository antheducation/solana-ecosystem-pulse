# Solana Ecosystem Pulse

**Generated:** 2026-10-13T22:01:16Z · **Schema:** `1.0.0` · **Collection time:** 16.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $107.01 | -0.09% |
| Market cap | $63.05B | rank #7 |
| Total value locked | $6.06B | -3.00% |
| Stablecoin supply | $16.24B | -0.72% |
| DEX volume (24h) | $2.23B | +74.77% |
| Chain fees / REV (24h) | $13.10M | +15.94% |
| Non-vote TPS (1h avg) | 1,990 | peak 5,776 total |
| Active validators | 673 | 7 delinquent |
| Epoch 1056 | 94.23% complete | 24,942 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 105 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | DEX volume moved sharply (up 74.8% in 24h) | DEX volume changed +74.8% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,990.0 average over the last 60 minutes; 2,117.6 in the latest sample.
- **Total TPS:** 5,063.4 average, 5,776.3 peak. Consensus votes account for 60.7% of all transactions.
- **Slot time:** 217.8 ms average (target 400 ms), worst 1-minute bucket 227.3 ms.
- **Block height:** 434,635,414 at absolute slot 456,599,058.
- **Epoch 1056:** slot 407,058 of 432,000 (94.23% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.605% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 191 ms |
| `solana-rpc.publicnode.com` | yes | 235 ms |
| `api.mainnet.solana.com` | yes | 95 ms |

## Validators & stake

- **673 active** validators, **7 delinquent** (1.03% by count, 0.012% by stake).
- **Total stake:** 438,790,522 SOL ($46.95B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.56% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 13.10%; 228 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,789,243 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,958,932 | 3.637% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,305,752 | 2.805% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,149,129 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,758,268 | 2.452% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,401,788 | 2.143% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,163 | 2.105% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,681,229 | 1.751% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,812,456 | 1.553% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,148 | 1.513% | 0% |

## Economics

- **SOL:** $107.01 (-0.09% 24h, -11.57% 7d, +5.76% 30d). Market cap $63.05B, 24h volume $4.00B (6.34% of cap). Price source: `coingecko`.
- **TVL:** $6.06B across 324 protocols - rank #3 of 425 chains, 6.63% of all tracked chain TVL. -10.62% over 7d, -54.4% from its ATH.
- **Stablecoins:** $16.24B circulating on Solana (-4.75% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.23B in 24h, $13.68B over 7d across 133 venues. Volume/TVL turnover 0.368x per day.
- **REV (chain fees):** $13.10M in 24h, $467.50M over 30d. Retained chain revenue $4.49M (34.3% of fees). Annualised fees are 7.59% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,162,211 SOL circulating of 635,720,825 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +0.2% | -8.7% |
| 2 | Kamino Lend | Lending | $1.31B | +0.3% | -6.2% |
| 3 | Raydium AMM | Dexs | $1.21B | -0.2% | -10.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.12B | -0.7% | -10.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.11B | -0.1% | -10.6% |
| 6 | Jupiter Lend | Lending | $1.10B | -2.1% | -10.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $758.59M | +0.1% | -7.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $560.73M | +0.2% | -10.5% |
| 9 | Sentora Curator | Risk Curators | $472.17M | +0.1% | +3.2% |
| 10 | Marinade Native | Staking Pool | $397.83M | -0.1% | -11.6% |
| 11 | PumpSwap | Dexs | $358.53M | -0.5% | -10.2% |
| 12 | Orca DEX | Dexs | $302.56M | -1.1% | -6.4% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 324 protocols the total is $16.19B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.7% · Dexs 15.4% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.6%

### Tokenised assets

$863.62M of tokenised real-world assets and equities are locked on Solana - 5.336% of chain TVL.

- OnRe (RWA): $292.55M
- Huma (RWA): $251.06M
- Solstice (Basis Trading): $209.25M
- JupUSD (Basis Trading): $46.62M
- Plume Vaults (RWA): $33.62M

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

- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-13
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-13
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11

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

### Change over 24h (vs run at 2026-10-12T23:52:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,094.70 | 5,063.39 | -0.61% |
| Average non-vote TPS | 2,039.01 | 1,990.01 | -2.40% |
| Average slot time (ms) | 218.80 | 217.80 | -0.46% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 8.00 | 7.00 | -12.50% |
| Solana TVL | 6,087,233,347.00 | 6,063,416,281.00 | -0.39% |
| SOL price | 105.47 | 107.01 | +1.46% |
| Stablecoin supply | 16,359,920,349.00 | 16,241,793,471.00 | -0.72% |
| 24h DEX volume | 1,277,023,682.31 | 2,231,842,381.02 | +74.77% |
| 24h chain fees | 11,301,815.14 | 13,103,539.72 | +15.94% |

### Change over 7d (vs run at 2026-10-06T21:56:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,237.18 | 5,063.39 | -3.32% |
| Average non-vote TPS | 2,776.85 | 1,990.01 | -28.34% |
| Average slot time (ms) | 270.70 | 217.80 | -19.54% |
| Active validators | 670.00 | 673.00 | +0.45% |
| Delinquent validators | 15.00 | 7.00 | -53.33% |
| Solana TVL | 6,619,880,617.00 | 6,063,416,281.00 | -8.41% |
| SOL price | 120.95 | 107.01 | -11.53% |
| Stablecoin supply | 17,052,133,908.00 | 16,241,793,471.00 | -4.75% |
| 24h DEX volume | 2,057,146,062.50 | 2,231,842,381.02 | +8.49% |
| 24h chain fees | 16,090,422.62 | 13,103,539.72 | -18.56% |

### Change over 30d (vs run at 2026-09-13T19:56:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,911.91 | 5,063.39 | +29.44% |
| Average non-vote TPS | 1,778.64 | 1,990.01 | +11.88% |
| Average slot time (ms) | 315.70 | 217.80 | -31.01% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 14.00 | 7.00 | -50.00% |
| Solana TVL | 5,861,539,247.00 | 6,063,416,281.00 | +3.44% |
| SOL price | 100.85 | 107.01 | +6.11% |
| Stablecoin supply | 16,525,835,618.00 | 16,241,793,471.00 | -1.72% |
| 24h DEX volume | 1,691,135,695.08 | 2,231,842,381.02 | +31.97% |
| 24h chain fees | 13,515,656.40 | 13,103,539.72 | -3.05% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
