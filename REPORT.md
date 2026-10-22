# Solana Ecosystem Pulse

**Generated:** 2026-10-22T10:44:53Z · **Schema:** `1.0.0` · **Collection time:** 18.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.58 | -1.77% |
| Market cap | $61.66B | rank #7 |
| Total value locked | $5.90B | -1.62% |
| Stablecoin supply | $16.16B | +0.88% |
| DEX volume (24h) | $2.26B | -7.38% |
| Chain fees / REV (24h) | $11.86M | -9.94% |
| Non-vote TPS (1h avg) | 1,731 | peak 2,430 total |
| Active validators | 668 | 9 delinquent |
| Epoch 1064 | 82.88% complete | 73,950 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 116 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,731.38 sits 6.1 sigma below the median of the last 116 runs (4,660.05, -62.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,731.4 average over the last 60 minutes; 2,260.5 in the latest sample.
- **Total TPS:** 1,731.4 average, 2,429.9 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 211.1 ms average (target 400 ms), worst 1-minute bucket 215.8 ms.
- **Block height:** 438,039,871 at absolute slot 460,006,050.
- **Epoch 1064:** slot 358,050 of 432,000 (82.88% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.592% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 252 ms |
| `solana-rpc.publicnode.com` | yes | 106 ms |
| `api.mainnet.solana.com` | yes | 151 ms |

## Validators & stake

- **668 active** validators, **9 delinquent** (1.33% by count, 0.005% by stake).
- **Total stake:** 438,868,046 SOL ($45.90B); stake rate 68.98% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 13.16%; 227 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,130,984 | 3.904% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,955,653 | 3.636% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,545,894 | 2.859% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,933,491 | 2.491% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,728,193 | 2.217% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,480,474 | 2.160% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,296 | 2.108% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,808,122 | 1.779% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,035,085 | 1.603% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,557 | 1.595% | 0% |

## Economics

- **SOL:** $104.58 (-1.77% 24h, +1.49% 7d, -10.93% 30d). Market cap $61.66B, 24h volume $2.85B (4.62% of cap). Price source: `coingecko`.
- **TVL:** $5.90B across 330 protocols - rank #3 of 421 chains, 6.51% of all tracked chain TVL. -1.10% over 7d, -54.5% from its ATH.
- **Stablecoins:** $16.16B circulating on Solana (+0.62% 7d) - $2.74 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.26B in 24h, $13.55B over 7d across 138 venues. Volume/TVL turnover 0.383x per day.
- **REV (chain fees):** $11.86M in 24h, $436.65M over 30d. Retained chain revenue $4.42M (37.3% of fees). Annualised fees are 7.02% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,604,494 SOL circulating of 636,212,524 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | -2.5% | +3.4% |
| 2 | Kamino Lend | Lending | $1.32B | -1.6% | +0.2% |
| 3 | Raydium AMM | Dexs | $1.17B | -2.0% | +1.3% |
| 4 | Binance Staked SOL | Liquid Staking | $1.09B | -2.0% | +1.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.08B | -2.8% | -1.0% |
| 6 | Jupiter Lend | Lending | $1.03B | -1.3% | -8.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $726.87M | -3.2% | -1.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $543.85M | -3.2% | +0.0% |
| 9 | Sentora Curator | Risk Curators | $417.37M | -3.5% | -8.8% |
| 10 | Marinade Native | Staking Pool | $372.65M | -2.9% | -2.4% |
| 11 | PumpSwap | Dexs | $348.96M | -1.8% | +0.6% |
| 12 | Orca DEX | Dexs | $306.34M | +0.3% | +2.7% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.78B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.7% · Dexs 15.2% · Derivatives 5.0% · Risk Curators 3.8% · RWA 3.8%

### Tokenised assets

$865.58M of tokenised real-world assets and equities are locked on Solana - 5.486% of chain TVL.

- OnRe (RWA): $295.04M
- Huma (RWA): $258.30M
- Solstice (Basis Trading): $203.24M
- JupUSD (Basis Trading): $42.96M
- Plume Vaults (RWA): $35.92M

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

- [SIMD-0690: SIMD-0690: Hash validation in Core BPF migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-22
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-22
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21
- [SIMD-0529: [SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-21T10:43:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,602.94 | 1,731.38 | -62.39% |
| Average non-vote TPS | 1,524.60 | 1,731.38 | +13.56% |
| Average slot time (ms) | 216.00 | 211.10 | -2.27% |
| Active validators | 668.00 | 668.00 | +0.00% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 6,001,273,500.00 | 5,896,494,807.00 | -1.75% |
| SOL price | 106.30 | 104.58 | -1.62% |
| Stablecoin supply | 16,008,541,783.00 | 16,155,037,927.00 | +0.92% |
| 24h DEX volume | 2,235,068,600.00 | 2,257,983,009.37 | +1.03% |
| 24h chain fees | 13,200,582.40 | 11,864,192.66 | -10.12% |

### Change over 7d (vs run at 2026-10-15T10:27:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,660.95 | 1,731.38 | -62.85% |
| Average non-vote TPS | 1,557.56 | 1,731.38 | +11.16% |
| Average slot time (ms) | 215.60 | 211.10 | -2.09% |
| Active validators | 672.00 | 668.00 | -0.60% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 5,931,649,344.00 | 5,896,494,807.00 | -0.59% |
| SOL price | 101.81 | 104.58 | +2.72% |
| Stablecoin supply | 16,055,751,684.00 | 16,155,037,927.00 | +0.62% |
| 24h DEX volume | 2,250,924,739.32 | 2,257,983,009.37 | +0.31% |
| 24h chain fees | 10,628,281.63 | 11,864,192.66 | +11.63% |

### Change over 30d (vs run at 2026-09-22T20:34:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,893.52 | 1,731.38 | -64.62% |
| Average non-vote TPS | 2,379.33 | 1,731.38 | -27.23% |
| Average slot time (ms) | 268.00 | 211.10 | -21.23% |
| Active validators | 677.00 | 668.00 | -1.33% |
| Delinquent validators | 12.00 | 9.00 | -25.00% |
| Solana TVL | 6,505,534,933.00 | 5,896,494,807.00 | -9.36% |
| SOL price | 118.17 | 104.58 | -11.50% |
| Stablecoin supply | 17,173,484,924.00 | 16,155,037,927.00 | -5.93% |
| 24h DEX volume | 3,428,858,820.75 | 2,257,983,009.37 | -34.15% |
| 24h chain fees | 18,642,402.21 | 11,864,192.66 | -36.36% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
