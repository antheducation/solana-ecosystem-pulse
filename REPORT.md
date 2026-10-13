# Solana Ecosystem Pulse

**Generated:** 2026-10-13T13:02:51Z · **Schema:** `1.0.0` · **Collection time:** 13.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $106.57 | -3.26% |
| Market cap | $62.80B | rank #7 |
| Total value locked | $6.07B | -3.13% |
| Stablecoin supply | $16.24B | -0.72% |
| DEX volume (24h) | $2.23B | +74.77% |
| Chain fees / REV (24h) | $12.99M | +14.91% |
| Non-vote TPS (1h avg) | 1,960 | peak 5,554 total |
| Active validators | 673 | 7 delinquent |
| Epoch 1056 | 60.10% complete | 172,380 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 105 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | DEX volume moved sharply (up 74.8% in 24h) | DEX volume changed +74.8% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,960.2 average over the last 60 minutes; 1,891.2 in the latest sample.
- **Total TPS:** 5,012.7 average, 5,554.4 peak. Consensus votes account for 60.9% of all transactions.
- **Slot time:** 219.1 ms average (target 400 ms), worst 1-minute bucket 229.0 ms.
- **Block height:** 434,488,133 at absolute slot 456,451,620.
- **Epoch 1056:** slot 259,620 of 432,000 (60.10% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.605% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 101 ms |
| `solana-rpc.publicnode.com` | yes | 112 ms |
| `api.mainnet.solana.com` | yes | 90 ms |

## Validators & stake

- **673 active** validators, **7 delinquent** (1.03% by count, 0.012% by stake).
- **Total stake:** 438,790,522 SOL ($46.76B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.56% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 13.24%; 228 validators at 0% and 66 at 100%.

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

- **SOL:** $106.57 (-3.26% 24h, -11.47% 7d, +6.93% 30d). Market cap $62.80B, 24h volume $4.23B (6.73% of cap). Price source: `coingecko`.
- **TVL:** $6.07B across 339 protocols - rank #3 of 469 chains, 6.63% of all tracked chain TVL. -8.35% over 7d, -54.4% from its ATH.
- **Stablecoins:** $16.24B circulating on Solana (-4.75% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.23B in 24h, $13.68B over 7d across 131 venues. Volume/TVL turnover 0.368x per day.
- **REV (chain fees):** $12.99M in 24h, $467.36M over 30d. Retained chain revenue $4.49M (34.6% of fees). Annualised fees are 7.55% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,162,665 SOL circulating of 635,721,280 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | -1.7% | -9.6% |
| 2 | Kamino Lend | Lending | $1.31B | -2.0% | -6.8% |
| 3 | Raydium AMM | Dexs | $1.21B | -3.6% | -10.1% |
| 4 | Jupiter Lend | Lending | $1.12B | -2.2% | -8.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.11B | -4.6% | -12.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.10B | -3.9% | -11.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $753.08M | -2.9% | -8.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $551.68M | -3.7% | -11.9% |
| 9 | Sentora Curator | Risk Curators | $471.75M | -4.0% | +3.2% |
| 10 | Marinade Native | Staking Pool | $392.71M | -4.2% | -12.7% |
| 11 | PumpSwap | Dexs | $362.16M | -3.0% | -9.3% |
| 12 | Orca DEX | Dexs | $302.56M | -3.4% | -6.4% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.11B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 16.8% · Dexs 15.4% · Derivatives 5.1% · Risk Curators 4.2% · RWA 3.7%

### Tokenised assets

$878.81M of tokenised real-world assets and equities are locked on Solana - 5.457% of chain TVL.

- OnRe (RWA): $292.56M
- Huma (RWA): $251.68M
- Solstice (Basis Trading): $209.26M
- JupUSD (Basis Trading): $46.69M
- Plume Vaults (RWA): $33.61M

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

- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-13
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-12
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

### Change over 24h (vs run at 2026-10-12T13:42:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,986.47 | 5,012.70 | +0.53% |
| Average non-vote TPS | 1,921.73 | 1,960.24 | +2.00% |
| Average slot time (ms) | 218.40 | 219.10 | +0.32% |
| Active validators | 673.00 | 673.00 | +0.00% |
| Delinquent validators | 8.00 | 7.00 | -12.50% |
| Solana TVL | 6,257,692,157.00 | 6,068,456,089.00 | -3.02% |
| SOL price | 110.09 | 106.57 | -3.20% |
| Stablecoin supply | 16,360,925,699.00 | 16,241,381,985.00 | -0.73% |
| 24h DEX volume | 1,277,019,605.31 | 2,231,841,478.02 | +74.77% |
| 24h chain fees | 11,200,431.37 | 12,987,306.72 | +15.95% |

### Change over 7d (vs run at 2026-10-06T12:19:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,451.96 | 5,012.70 | +12.60% |
| Average non-vote TPS | 1,940.48 | 1,960.24 | +1.02% |
| Average slot time (ms) | 266.50 | 219.10 | -17.79% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 13.00 | 7.00 | -46.15% |
| Solana TVL | 6,784,753,894.00 | 6,068,456,089.00 | -10.56% |
| SOL price | 120.40 | 106.57 | -11.49% |
| Stablecoin supply | 17,051,522,484.00 | 16,241,381,985.00 | -4.75% |
| 24h DEX volume | 2,057,146,062.50 | 2,231,841,478.02 | +8.49% |
| 24h chain fees | 15,987,778.12 | 12,987,306.72 | -18.77% |

### Change over 30d (vs run at 2026-09-13T19:56:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,911.91 | 5,012.70 | +28.14% |
| Average non-vote TPS | 1,778.64 | 1,960.24 | +10.21% |
| Average slot time (ms) | 315.70 | 219.10 | -30.60% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 14.00 | 7.00 | -50.00% |
| Solana TVL | 5,861,539,247.00 | 6,068,456,089.00 | +3.53% |
| SOL price | 100.85 | 106.57 | +5.67% |
| Stablecoin supply | 16,525,835,618.00 | 16,241,381,985.00 | -1.72% |
| 24h DEX volume | 1,691,135,695.08 | 2,231,841,478.02 | +31.97% |
| 24h chain fees | 13,515,656.40 | 12,987,306.72 | -3.91% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
