# Solana Ecosystem Pulse

**Generated:** 2026-10-12T23:52:37Z · **Schema:** `1.0.0` · **Collection time:** 16.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.47 | -5.22% |
| Market cap | $62.15B | rank #7 |
| Total value locked | $6.09B | -1.95% |
| Stablecoin supply | $16.36B | -0.28% |
| DEX volume (24h) | $1.28B | -0.72% |
| Chain fees / REV (24h) | $11.30M | -5.32% |
| Non-vote TPS (1h avg) | 2,039 | peak 6,027 total |
| Active validators | 672 | 8 delinquent |
| Epoch 1056 | 9.78% complete | 389,765 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 104 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,039.0 average over the last 60 minutes; 1,784.0 in the latest sample.
- **Total TPS:** 5,094.7 average, 6,027.3 peak. Consensus votes account for 60.0% of all transactions.
- **Slot time:** 218.8 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 434,270,978 at absolute slot 456,234,235.
- **Epoch 1056:** slot 42,235 of 432,000 (9.78% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.605% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 147 ms |
| `solana-rpc.publicnode.com` | yes | 104 ms |
| `api.mainnet.solana.com` | yes | 209 ms |

## Validators & stake

- **672 active** validators, **8 delinquent** (1.18% by count, 0.013% by stake).
- **Total stake:** 438,790,522 SOL ($46.28B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.56% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 231 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,789,243 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,958,932 | 3.638% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,305,752 | 2.805% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,149,129 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,758,268 | 2.452% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,401,788 | 2.143% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,163 | 2.105% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,681,229 | 1.751% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,812,456 | 1.553% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,148 | 1.513% | 0% |

## Economics

- **SOL:** $105.47 (-5.22% 24h, -12.84% 7d, +3.74% 30d). Market cap $62.15B, 24h volume $3.06B (4.92% of cap). Price source: `coingecko`.
- **TVL:** $6.09B across 337 protocols - rank #3 of 468 chains, 6.65% of all tracked chain TVL. -8.08% over 7d, -54.0% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-3.12% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.28B in 24h, $13.50B over 7d across 130 venues. Volume/TVL turnover 0.210x per day.
- **REV (chain fees):** $11.30M in 24h, $467.84M over 30d. Retained chain revenue $4.10M (36.3% of fees). Annualised fees are 6.64% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,163,250 SOL circulating of 635,721,864 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | -1.8% | -9.5% |
| 2 | Kamino Lend | Lending | $1.31B | -1.6% | -6.4% |
| 3 | Raydium AMM | Dexs | $1.22B | -3.2% | -9.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.12B | -2.9% | -11.2% |
| 5 | Jupiter Lend | Lending | $1.12B | -2.0% | -9.0% |
| 6 | Binance Staked SOL | Liquid Staking | $1.11B | -2.3% | -10.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $753.55M | -2.7% | -8.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $555.12M | -2.9% | -11.6% |
| 9 | Sentora Curator | Risk Curators | $471.86M | -4.1% | +24.1% |
| 10 | Marinade Native | Staking Pool | $398.33M | -2.7% | -11.8% |
| 11 | PumpSwap | Dexs | $360.37M | -3.5% | -11.7% |
| 12 | Orca DEX | Dexs | $305.92M | -1.4% | -4.8% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 337 protocols the total is $16.21B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 16.7% · Dexs 15.4% · Derivatives 5.2% · Risk Curators 4.1% · RWA 3.7%

### Tokenised assets

$881.97M of tokenised real-world assets and equities are locked on Solana - 5.440% of chain TVL.

- OnRe (RWA): $292.51M
- Huma (RWA): $254.59M
- Solstice (Basis Trading): $209.25M
- JupUSD (Basis Trading): $46.83M
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
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-10

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

### Change over 24h (vs run at 2026-10-11T21:08:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.95 | 5,094.70 | +2.41% |
| Average non-vote TPS | 1,917.24 | 2,039.01 | +6.35% |
| Average slot time (ms) | 218.90 | 218.80 | -0.05% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 9.00 | 8.00 | -11.11% |
| Solana TVL | 6,251,230,542.00 | 6,087,233,347.00 | -2.62% |
| SOL price | 110.93 | 105.47 | -4.92% |
| Stablecoin supply | 16,405,817,670.00 | 16,359,920,349.00 | -0.28% |
| 24h DEX volume | 1,286,316,590.57 | 1,277,023,682.31 | -0.72% |
| 24h chain fees | 11,936,417.92 | 11,301,815.14 | -5.32% |

### Change over 7d (vs run at 2026-10-05T23:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,796.58 | 5,094.70 | +6.22% |
| Average non-vote TPS | 2,304.82 | 2,039.01 | -11.53% |
| Average slot time (ms) | 268.60 | 218.80 | -18.54% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 6,781,683,220.00 | 6,087,233,347.00 | -10.24% |
| SOL price | 120.74 | 105.47 | -12.65% |
| Stablecoin supply | 16,885,339,627.00 | 16,359,920,349.00 | -3.11% |
| 24h DEX volume | 1,708,158,585.63 | 1,277,023,682.31 | -25.24% |
| 24h chain fees | 16,123,937.37 | 11,301,815.14 | -29.91% |

### Change over 30d (vs run at 2026-09-12T19:46:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,285.77 | 5,094.70 | +18.87% |
| Average non-vote TPS | 2,164.34 | 2,039.01 | -5.79% |
| Average slot time (ms) | 317.70 | 218.80 | -31.13% |
| Active validators | 679.00 | 672.00 | -1.03% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,903,101,578.00 | 6,087,233,347.00 | +3.12% |
| SOL price | 101.32 | 105.47 | +4.10% |
| Stablecoin supply | 16,554,268,556.00 | 16,359,920,349.00 | -1.17% |
| 24h DEX volume | 3,183,599,712.43 | 1,277,023,682.31 | -59.89% |
| 24h chain fees | 17,875,390.26 | 11,301,815.14 | -36.77% |

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
