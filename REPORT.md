# Solana Ecosystem Pulse

**Generated:** 2026-10-12T02:55:24Z · **Schema:** `1.0.0` · **Collection time:** 12.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $112.07 | +1.95% |
| Market cap | $66.02B | rank #7 |
| Total value locked | $6.25B | +0.41% |
| Stablecoin supply | $16.36B | -0.28% |
| DEX volume (24h) | $1.25B | -3.07% |
| Chain fees / REV (24h) | $11.26M | -5.66% |
| Non-vote TPS (1h avg) | 2,088 | peak 5,865 total |
| Active validators | 673 | 8 delinquent |
| Epoch 1055 | 29.90% complete | 302,825 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 103 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,087.7 average over the last 60 minutes; 2,179.3 in the latest sample.
- **Total TPS:** 5,135.9 average, 5,865.2 peak. Consensus votes account for 59.4% of all transactions.
- **Slot time:** 219.7 ms average (target 400 ms), worst 1-minute bucket 227.3 ms.
- **Block height:** 433,926,281 at absolute slot 455,889,175.
- **Epoch 1055:** slot 129,175 of 432,000 (29.90% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.606% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 54 ms |
| `solana-rpc.publicnode.com` | yes | 115 ms |
| `api.mainnet.solana.com` | yes | 60 ms |

## Validators & stake

- **673 active** validators, **8 delinquent** (1.17% by count, 0.017% by stake).
- **Total stake:** 438,762,140 SOL ($49.17B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 12.79%; 232 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,781,885 | 4.053% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,956,122 | 3.637% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,320,023 | 2.808% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,147,729 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,755,463 | 2.452% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,332,199 | 2.127% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,248,710 | 2.108% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,607,284 | 1.734% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,811,094 | 1.553% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,422,658 | 1.464% | 0% |

## Economics

- **SOL:** $112.07 (+1.95% 24h, -7.48% 7d, +9.88% 30d). Market cap $66.02B, 24h volume $2.03B (3.07% of cap). Price source: `coingecko`.
- **TVL:** $6.25B across 335 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -7.03% over 7d, -52.8% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-3.12% 7d) - $2.62 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.25B in 24h, $12.88B over 7d across 130 venues. Volume/TVL turnover 0.199x per day.
- **REV (chain fees):** $11.26M in 24h, $467.22M over 30d. Retained chain revenue $4.15M (36.9% of fees). Annualised fees are 6.23% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,107,334 SOL circulating of 635,660,118 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.83B | +1.2% | -7.8% |
| 2 | Kamino Lend | Lending | $1.34B | +0.8% | -4.3% |
| 3 | Raydium AMM | Dexs | $1.26B | +1.0% | -7.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.17B | +1.3% | -7.9% |
| 5 | Jupiter Lend | Lending | $1.15B | +0.7% | -6.7% |
| 6 | Binance Staked SOL | Liquid Staking | $1.14B | +1.1% | -8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $778.51M | +0.9% | -5.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $577.54M | +1.5% | -8.1% |
| 9 | Sentora Curator | Risk Curators | $491.81M | +0.2% | +29.4% |
| 10 | Marinade Native | Staking Pool | $412.50M | +1.2% | -8.7% |
| 11 | PumpSwap | Dexs | $370.02M | +0.8% | -9.3% |
| 12 | Orca DEX | Dexs | $310.23M | -0.1% | -3.5% |

The top five protocols hold 40.4% of Solana's tracked TVL. Summed across all 335 protocols the total is $16.68B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 16.6% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$882.46M of tokenised real-world assets and equities are locked on Solana - 5.291% of chain TVL.

- OnRe (RWA): $292.46M
- Huma (RWA): $253.76M
- Solstice (Basis Trading): $210.58M
- JupUSD (Basis Trading): $47.35M
- Plume Vaults (RWA): $33.58M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-11
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-10
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-10

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

### Change over 24h (vs run at 2026-10-11T02:30:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,606.30 | 5,135.89 | +11.50% |
| Average non-vote TPS | 1,517.17 | 2,087.65 | +37.60% |
| Average slot time (ms) | 217.60 | 219.70 | +0.97% |
| Active validators | 674.00 | 673.00 | -0.15% |
| Delinquent validators | 6.00 | 8.00 | +33.33% |
| Solana TVL | 6,218,958,410.00 | 6,254,990,671.00 | +0.58% |
| SOL price | 109.93 | 112.07 | +1.95% |
| Stablecoin supply | 16,409,963,032.00 | 16,359,537,345.00 | -0.31% |
| 24h DEX volume | 1,579,981,826.57 | 1,246,835,645.31 | -21.09% |
| 24h chain fees | 11,975,476.33 | 11,260,863.80 | -5.97% |

### Change over 7d (vs run at 2026-10-05T02:39:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,345.78 | 5,135.89 | +18.18% |
| Average non-vote TPS | 1,847.54 | 2,087.65 | +13.00% |
| Average slot time (ms) | 267.50 | 219.70 | -17.87% |
| Active validators | 671.00 | 673.00 | +0.30% |
| Delinquent validators | 15.00 | 8.00 | -46.67% |
| Solana TVL | 6,743,140,234.00 | 6,254,990,671.00 | -7.24% |
| SOL price | 121.39 | 112.07 | -7.68% |
| Stablecoin supply | 16,885,469,670.00 | 16,359,537,345.00 | -3.11% |
| 24h DEX volume | 1,649,284,605.63 | 1,246,835,645.31 | -24.40% |
| 24h chain fees | 15,446,766.41 | 11,260,863.80 | -27.10% |

### Change over 30d (vs run at 2026-09-11T20:08:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,273.36 | 5,135.89 | +20.18% |
| Average non-vote TPS | 2,154.29 | 2,087.65 | -3.09% |
| Average slot time (ms) | 317.20 | 219.70 | -30.74% |
| Active validators | 678.00 | 673.00 | -0.74% |
| Delinquent validators | 12.00 | 8.00 | -33.33% |
| Solana TVL | 5,878,734,141.00 | 6,254,990,671.00 | +6.40% |
| SOL price | 102.41 | 112.07 | +9.43% |
| Stablecoin supply | 16,358,198,746.00 | 16,359,537,345.00 | +0.01% |
| 24h DEX volume | 2,921,890,110.01 | 1,246,835,645.31 | -57.33% |
| 24h chain fees | 14,614,973.44 | 11,260,863.80 | -22.95% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
