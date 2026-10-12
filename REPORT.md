# Solana Ecosystem Pulse

**Generated:** 2026-10-12T13:42:19Z · **Schema:** `1.0.0` · **Collection time:** 25.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.09 | +0.59% |
| Market cap | $64.82B | rank #7 |
| Total value locked | $6.26B | +0.50% |
| Stablecoin supply | $16.36B | -0.28% |
| DEX volume (24h) | $1.28B | -0.72% |
| Chain fees / REV (24h) | $11.20M | -6.17% |
| Non-vote TPS (1h avg) | 1,922 | peak 6,091 total |
| Active validators | 673 | 8 delinquent |
| Epoch 1055 | 71.09% complete | 124,910 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 104 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,921.7 average over the last 60 minutes; 2,171.6 in the latest sample.
- **Total TPS:** 4,986.5 average, 6,091.2 peak. Consensus votes account for 61.5% of all transactions.
- **Slot time:** 218.4 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 434,104,079 at absolute slot 456,067,090.
- **Epoch 1055:** slot 307,090 of 432,000 (71.09% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.606% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 289 ms |
| `solana-rpc.publicnode.com` | yes | 201 ms |
| `api.mainnet.solana.com` | yes | 195 ms |

## Validators & stake

- **673 active** validators, **8 delinquent** (1.17% by count, 0.018% by stake).
- **Total stake:** 438,762,140 SOL ($48.30B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.84% of active stake.
- **Commission:** median 5.0%, mean 13.08%; 231 validators at 0% and 65 at 100%.

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

- **SOL:** $110.09 (+0.59% 24h, -8.52% 7d, +7.90% 30d). Market cap $64.82B, 24h volume $2.72B (4.20% of cap). Price source: `coingecko`.
- **TVL:** $6.26B across 337 protocols - rank #3 of 468 chains, 6.76% of all tracked chain TVL. -7.18% over 7d, -52.9% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-3.11% 7d) - $2.61 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.28B in 24h, $13.50B over 7d across 130 venues. Volume/TVL turnover 0.204x per day.
- **REV (chain fees):** $11.20M in 24h, $467.74M over 30d. Retained chain revenue $4.10M (36.6% of fees). Annualised fees are 6.31% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,106,857 SOL circulating of 635,659,640 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | +0.9% | -8.3% |
| 2 | Kamino Lend | Lending | $1.33B | +0.6% | -4.7% |
| 3 | Raydium AMM | Dexs | $1.26B | +1.6% | -6.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.16B | +1.4% | -8.4% |
| 5 | Jupiter Lend | Lending | $1.14B | +0.4% | -7.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.14B | +1.4% | -8.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $775.53M | +0.7% | -5.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $572.80M | +1.3% | -8.8% |
| 9 | Sentora Curator | Risk Curators | $491.41M | -0.1% | +29.3% |
| 10 | Marinade Native | Staking Pool | $410.04M | +1.0% | -9.2% |
| 11 | PumpSwap | Dexs | $373.56M | +1.9% | -8.4% |
| 12 | Orca DEX | Dexs | $313.05M | +1.0% | -2.6% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.57B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 16.6% · Dexs 15.6% · Derivatives 5.2% · Risk Curators 4.2% · RWA 3.6%

### Tokenised assets

$882.82M of tokenised real-world assets and equities are locked on Solana - 5.327% of chain TVL.

- OnRe (RWA): $292.51M
- Huma (RWA): $254.25M
- Solstice (Basis Trading): $210.45M
- JupUSD (Basis Trading): $47.34M
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

- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
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

### Change over 24h (vs run at 2026-10-11T11:42:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,516.76 | 4,986.47 | +10.40% |
| Average non-vote TPS | 1,445.69 | 1,921.73 | +32.93% |
| Average slot time (ms) | 218.30 | 218.40 | +0.05% |
| Active validators | 674.00 | 673.00 | -0.15% |
| Delinquent validators | 6.00 | 8.00 | +33.33% |
| Solana TVL | 6,195,850,647.00 | 6,257,692,157.00 | +1.00% |
| SOL price | 109.42 | 110.09 | +0.61% |
| Stablecoin supply | 16,404,382,269.00 | 16,360,925,699.00 | -0.26% |
| 24h DEX volume | 1,286,316,590.57 | 1,277,019,605.31 | -0.72% |
| 24h chain fees | 11,824,628.92 | 11,200,431.37 | -5.28% |

### Change over 7d (vs run at 2026-10-05T12:50:28Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,875.14 | 4,986.47 | +28.68% |
| Average non-vote TPS | 1,378.28 | 1,921.73 | +39.43% |
| Average slot time (ms) | 267.70 | 218.40 | -18.42% |
| Active validators | 671.00 | 673.00 | +0.30% |
| Delinquent validators | 15.00 | 8.00 | -46.67% |
| Solana TVL | 6,721,988,816.00 | 6,257,692,157.00 | -6.91% |
| SOL price | 120.44 | 110.09 | -8.59% |
| Stablecoin supply | 16,884,585,049.00 | 16,360,925,699.00 | -3.10% |
| 24h DEX volume | 1,708,158,585.63 | 1,277,019,605.31 | -25.24% |
| 24h chain fees | 16,126,162.37 | 11,200,431.37 | -30.54% |

### Change over 30d (vs run at 2026-09-12T19:46:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,285.77 | 4,986.47 | +16.35% |
| Average non-vote TPS | 2,164.34 | 1,921.73 | -11.21% |
| Average slot time (ms) | 317.70 | 218.40 | -31.26% |
| Active validators | 679.00 | 673.00 | -0.88% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,903,101,578.00 | 6,257,692,157.00 | +6.01% |
| SOL price | 101.32 | 110.09 | +8.66% |
| Stablecoin supply | 16,554,268,556.00 | 16,360,925,699.00 | -1.17% |
| 24h DEX volume | 3,183,599,712.43 | 1,277,019,605.31 | -59.89% |
| 24h chain fees | 17,875,390.26 | 11,200,431.37 | -37.34% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 25.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
