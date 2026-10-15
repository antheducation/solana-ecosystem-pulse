# Solana Ecosystem Pulse

**Generated:** 2026-10-15T02:04:56Z · **Schema:** `1.0.0` · **Collection time:** 14.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.85 | -3.50% |
| Market cap | $61.20B | rank #7 |
| Total value locked | $6.00B | -0.22% |
| Stablecoin supply | $16.06B | -1.61% |
| DEX volume (24h) | $2.25B | -9.87% |
| Chain fees / REV (24h) | $10.65M | -9.59% |
| Non-vote TPS (1h avg) | 2,080 | peak 6,111 total |
| Active validators | 672 | 8 delinquent |
| Epoch 1058 | 2.02% complete | 423,275 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 106 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,079.7 average over the last 60 minutes; 2,172.0 in the latest sample.
- **Total TPS:** 5,158.4 average, 6,111.4 peak. Consensus votes account for 59.7% of all transactions.
- **Slot time:** 216.6 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 435,100,663 at absolute slot 457,064,725.
- **Epoch 1058:** slot 8,725 of 432,000 (2.02% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.602% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 698 ms |
| `solana-rpc.publicnode.com` | yes | 168 ms |
| `api.mainnet.solana.com` | yes | 81 ms |

## Validators & stake

- **672 active** validators, **8 delinquent** (1.18% by count, 0.000% by stake).
- **Total stake:** 437,887,641 SOL ($45.47B); stake rate 68.87% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 12.66%; 231 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,556,681 | 4.009% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,475,284 | 3.534% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,340,406 | 2.818% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,132,168 | 2.542% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,777,829 | 2.461% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,409,309 | 2.149% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,227,345 | 2.107% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,737,484 | 1.767% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,912,081 | 1.579% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,640,641 | 1.517% | 0% |

## Economics

- **SOL:** $103.85 (-3.50% 24h, -10.51% 7d, +1.57% 30d). Market cap $61.20B, 24h volume $3.22B (5.26% of cap). Price source: `coingecko`.
- **TVL:** $6.00B across 323 protocols - rank #3 of 425 chains, 6.69% of all tracked chain TVL. -7.42% over 7d, -55.0% from its ATH.
- **Stablecoins:** $16.06B circulating on Solana (-2.26% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.25B in 24h, $12.95B over 7d across 133 venues. Volume/TVL turnover 0.375x per day.
- **REV (chain fees):** $10.65M in 24h, $462.60M over 30d. Retained chain revenue $4.26M (40.0% of fees). Annualised fees are 6.35% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,269,260 SOL circulating of 635,844,936 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.76B | -2.9% | -8.2% |
| 2 | Kamino Lend | Lending | $1.31B | +0.0% | -3.9% |
| 3 | Raydium AMM | Dexs | $1.18B | -2.4% | -8.9% |
| 4 | Jupiter Lend | Lending | $1.11B | +0.4% | -8.4% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.09B | -4.7% | -10.1% |
| 6 | Binance Staked SOL | Liquid Staking | $1.07B | -2.3% | -10.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $738.12M | -2.2% | -7.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $544.44M | -2.9% | -9.7% |
| 9 | Sentora Curator | Risk Curators | $457.77M | -3.1% | -8.9% |
| 10 | Marinade Native | Staking Pool | $381.78M | -3.0% | -12.0% |
| 11 | PumpSwap | Dexs | $349.55M | -2.3% | -9.8% |
| 12 | Orca DEX | Dexs | $299.99M | -0.8% | -7.0% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 323 protocols the total is $15.84B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.0% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.7%

### Tokenised assets

$866.30M of tokenised real-world assets and equities are locked on Solana - 5.469% of chain TVL.

- OnRe (RWA): $292.84M
- Huma (RWA): $253.53M
- Solstice (Basis Trading): $209.32M
- JupUSD (Basis Trading): $46.08M
- Plume Vaults (RWA): $33.89M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.3.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-14
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-14
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-14
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-14
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-14
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-14
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

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

### Change over 24h (vs run at 2026-10-14T02:23:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,817.45 | 5,158.40 | +7.08% |
| Average non-vote TPS | 1,751.73 | 2,079.66 | +18.72% |
| Average slot time (ms) | 218.50 | 216.60 | -0.87% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 6.00 | 8.00 | +33.33% |
| Solana TVL | 6,046,086,631.00 | 5,995,764,710.00 | -0.83% |
| SOL price | 107.46 | 103.85 | -3.36% |
| Stablecoin supply | 16,502,656,668.00 | 16,056,807,804.00 | -2.70% |
| 24h DEX volume | 2,277,563,559.38 | 2,248,882,317.32 | -1.26% |
| 24h chain fees | 11,688,355.74 | 10,646,585.63 | -8.91% |

### Change over 7d (vs run at 2026-10-08T03:15:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,343.08 | 5,158.40 | +18.77% |
| Average non-vote TPS | 1,847.99 | 2,079.66 | +12.54% |
| Average slot time (ms) | 268.00 | 216.60 | -19.18% |
| Active validators | 671.00 | 672.00 | +0.15% |
| Delinquent validators | 10.00 | 8.00 | -20.00% |
| Solana TVL | 6,467,832,291.00 | 5,995,764,710.00 | -7.30% |
| SOL price | 115.92 | 103.85 | -10.41% |
| Stablecoin supply | 16,610,992,769.00 | 16,056,807,804.00 | -3.34% |
| 24h DEX volume | 2,143,188,354.81 | 2,248,882,317.32 | +4.93% |
| 24h chain fees | 13,755,904.90 | 10,646,585.63 | -22.60% |

### Change over 30d (vs run at 2026-09-14T21:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,277.98 | 5,158.40 | +20.58% |
| Average non-vote TPS | 2,155.99 | 2,079.66 | -3.54% |
| Average slot time (ms) | 317.90 | 216.60 | -31.87% |
| Active validators | 678.00 | 672.00 | -0.88% |
| Delinquent validators | 12.00 | 8.00 | -33.33% |
| Solana TVL | 5,949,162,754.00 | 5,995,764,710.00 | +0.78% |
| SOL price | 103.65 | 103.85 | +0.19% |
| Stablecoin supply | 16,354,375,710.00 | 16,056,807,804.00 | -1.82% |
| 24h DEX volume | 1,790,994,711.97 | 2,248,882,317.32 | +25.57% |
| 24h chain fees | 14,036,101.64 | 10,646,585.63 | -24.15% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
