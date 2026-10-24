# Solana Ecosystem Pulse

**Generated:** 2026-10-24T19:54:17Z · **Schema:** `1.0.0` · **Collection time:** 16.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.01 | -2.45% |
| Market cap | $59.57B | rank #7 |
| Total value locked | $5.72B | -2.92% |
| Stablecoin supply | $15.93B | -0.26% |
| DEX volume (24h) | $2.00B | -2.07% |
| Chain fees / REV (24h) | $10.55M | -8.04% |
| Non-vote TPS (1h avg) | 1,955 | peak 2,445 total |
| Active validators | 665 | 25 delinquent |
| Epoch 1067 | 7.50% complete | 399,584 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 121 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,955.01 sits 5.1 sigma below the median of the last 121 runs (4,653.97, -58.0%). | `zscore` |
| [SERIOUS] | Delinquent validators is above its recent norm | Current 25.00 sits 5.1 sigma above the median of the last 121 runs (10.00, +150.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,955.0 average over the last 60 minutes; 1,705.2 in the latest sample.
- **Total TPS:** 1,955.0 average, 2,444.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.5 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 439,005,690 at absolute slot 460,976,416.
- **Epoch 1067:** slot 32,416 of 432,000 (7.50% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.587% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 212 ms |
| `solana-rpc.publicnode.com` | yes | 165 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **665 active** validators, **25 delinquent** (3.62% by count, 0.049% by stake).
- **Total stake:** 437,191,006 SOL ($44.16B); stake rate 68.70% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 46.04% of active stake.
- **Commission:** median 5.0%, mean 12.91%; 228 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,099,113 | 3.913% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,646,121 | 3.809% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,588,035 | 2.881% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,881,430 | 2.490% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,721,918 | 2.225% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,483,244 | 2.170% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,837 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,036 | 1.782% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,038,249 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,006,653 | 1.603% | 0% |

## Economics

- **SOL:** $101.01 (-2.45% 24h, -2.69% 7d, -13.92% 30d). Market cap $59.57B, 24h volume $2.53B (4.25% of cap). Price source: `coingecko`.
- **TVL:** $5.72B across 332 protocols - rank #4 of 421 chains, 6.45% of all tracked chain TVL. -3.95% over 7d, -55.9% from its ATH.
- **Stablecoins:** $15.93B circulating on Solana (-0.65% 7d) - $2.79 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.00B in 24h, $13.52B over 7d across 138 venues. Volume/TVL turnover 0.349x per day.
- **REV (chain fees):** $10.55M in 24h, $440.73M over 30d. Retained chain revenue $3.96M (37.5% of fees). Annualised fees are 6.47% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,764,454 SOL circulating of 636,396,198 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.76B | -3.6% | -2.9% |
| 2 | Kamino Lend | Lending | $1.26B | -2.6% | -3.9% |
| 3 | Raydium AMM | Dexs | $1.14B | -4.0% | -3.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.05B | -3.5% | -4.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | -4.8% | -4.2% |
| 6 | Jupiter Lend | Lending | $1.01B | -0.0% | -7.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $703.77M | -3.8% | -4.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $521.37M | -4.4% | -4.4% |
| 9 | Sentora Curator | Risk Curators | $396.98M | -0.3% | -12.1% |
| 10 | Marinade Native | Staking Pool | $361.36M | -3.1% | -5.3% |
| 11 | PumpSwap | Dexs | $336.71M | -3.2% | -4.8% |
| 12 | Orca DEX | Dexs | $300.10M | -1.8% | +0.0% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.31B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.6% · Lending 16.6% · Dexs 15.3% · Derivatives 5.0% · RWA 3.9% · Risk Curators 3.8%

### Tokenised assets

$859.54M of tokenised real-world assets and equities are locked on Solana - 5.615% of chain TVL.

- OnRe (RWA): $295.39M
- Huma (RWA): $252.75M
- Solstice (Basis Trading): $201.86M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.46M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0) | 2026-10-24 | pre-release |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-24
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-23T20:43:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,163.30 | 1,955.01 | -9.63% |
| Average non-vote TPS | 2,163.30 | 1,955.01 | -9.63% |
| Average slot time (ms) | 212.20 | 212.50 | +0.14% |
| Active validators | 664.00 | 665.00 | +0.15% |
| Delinquent validators | 14.00 | 25.00 | +78.57% |
| Solana TVL | 5,856,286,188.00 | 5,717,401,347.00 | -2.37% |
| SOL price | 103.58 | 101.01 | -2.48% |
| Stablecoin supply | 15,965,866,149.00 | 15,925,693,948.00 | -0.25% |
| 24h DEX volume | 2,039,384,832.23 | 1,997,070,440.37 | -2.07% |
| 24h chain fees | 11,472,475.22 | 10,552,167.09 | -8.02% |

### Change over 7d (vs run at 2026-10-17T19:45:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,823.29 | 1,955.01 | -59.47% |
| Average non-vote TPS | 1,758.64 | 1,955.01 | +11.17% |
| Average slot time (ms) | 217.70 | 212.50 | -2.39% |
| Active validators | 670.00 | 665.00 | -0.75% |
| Delinquent validators | 11.00 | 25.00 | +127.27% |
| Solana TVL | 5,922,304,891.00 | 5,717,401,347.00 | -3.46% |
| SOL price | 104.07 | 101.01 | -2.94% |
| Stablecoin supply | 16,030,558,263.00 | 15,925,693,948.00 | -0.65% |
| 24h DEX volume | 2,168,129,752.12 | 1,997,070,440.37 | -7.89% |
| 24h chain fees | 12,431,928.33 | 10,552,167.09 | -15.12% |

### Change over 30d (vs run at 2026-09-24T20:51:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,906.54 | 1,955.01 | -60.16% |
| Average non-vote TPS | 2,393.07 | 1,955.01 | -18.31% |
| Average slot time (ms) | 267.40 | 212.50 | -20.53% |
| Active validators | 676.00 | 665.00 | -1.63% |
| Delinquent validators | 10.00 | 25.00 | +150.00% |
| Solana TVL | 6,484,914,945.00 | 5,717,401,347.00 | -11.84% |
| SOL price | 116.85 | 101.01 | -13.56% |
| Stablecoin supply | 16,427,048,512.00 | 15,925,693,948.00 | -3.05% |
| 24h DEX volume | 2,552,816,117.41 | 1,997,070,440.37 | -21.77% |
| 24h chain fees | 16,120,232.81 | 10,552,167.09 | -34.54% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
