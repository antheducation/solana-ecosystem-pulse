# Solana Ecosystem Pulse

**Generated:** 2026-10-22T02:09:19Z · **Schema:** `1.0.0` · **Collection time:** 16.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.97 | -0.40% |
| Market cap | $62.49B | rank #7 |
| Total value locked | $6.03B | +0.03% |
| Stablecoin supply | $16.15B | +0.88% |
| DEX volume (24h) | $2.28B | -6.54% |
| Chain fees / REV (24h) | $11.88M | -9.86% |
| Non-vote TPS (1h avg) | 1,987 | peak 3,274 total |
| Active validators | 668 | 9 delinquent |
| Epoch 1064 | 49.14% complete | 219,695 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 116 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average TPS is below its recent norm | Current 1,987.14 sits 5.6 sigma below the median of the last 116 runs (4,660.05, -57.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,987.1 average over the last 60 minutes; 1,750.3 in the latest sample.
- **Total TPS:** 1,987.1 average, 3,273.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.4 ms average (target 400 ms), worst 1-minute bucket 217.4 ms.
- **Block height:** 437,894,313 at absolute slot 459,860,305.
- **Epoch 1064:** slot 212,305 of 432,000 (49.14% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.592% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 168 ms |
| `solana-rpc.publicnode.com` | yes | 155 ms |
| `api.mainnet.solana.com` | yes | 174 ms |

## Validators & stake

- **668 active** validators, **9 delinquent** (1.33% by count, 0.005% by stake).
- **Total stake:** 438,868,046 SOL ($46.51B); stake rate 68.98% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 13.01%; 228 validators at 0% and 64 at 100%.

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

- **SOL:** $105.97 (-0.40% 24h, +1.91% 7d, -9.84% 30d). Market cap $62.49B, 24h volume $2.58B (4.12% of cap). Price source: `coingecko`.
- **TVL:** $6.03B across 330 protocols - rank #3 of 421 chains, 6.53% of all tracked chain TVL. +1.18% over 7d, -53.5% from its ATH.
- **Stablecoins:** $16.15B circulating on Solana (+0.61% 7d) - $2.68 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.28B in 24h, $13.31B over 7d across 138 venues. Volume/TVL turnover 0.378x per day.
- **REV (chain fees):** $11.88M in 24h, $436.51M over 30d. Retained chain revenue $4.42M (37.3% of fees). Annualised fees are 6.94% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,604,635 SOL circulating of 636,212,665 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.87B | +0.8% | +6.4% |
| 2 | Kamino Lend | Lending | $1.34B | +0.3% | +1.6% |
| 3 | Raydium AMM | Dexs | $1.21B | +0.8% | +4.8% |
| 4 | Binance Staked SOL | Liquid Staking | $1.13B | +0.9% | +4.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.12B | +0.7% | +2.2% |
| 6 | Jupiter Lend | Lending | $1.05B | +0.9% | -6.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $747.17M | -0.1% | +1.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $562.11M | +0.7% | +3.4% |
| 9 | Sentora Curator | Risk Curators | $417.06M | -3.6% | -8.9% |
| 10 | Marinade Native | Staking Pool | $385.30M | -0.1% | +0.9% |
| 11 | PumpSwap | Dexs | $358.14M | +0.5% | +3.2% |
| 12 | Orca DEX | Dexs | $309.85M | +1.8% | +3.9% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 330 protocols the total is $16.17B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.6% · Dexs 15.3% · Derivatives 5.0% · Risk Curators 3.7% · RWA 3.7%

### Tokenised assets

$865.34M of tokenised real-world assets and equities are locked on Solana - 5.352% of chain TVL.

- OnRe (RWA): $294.56M
- Huma (RWA): $258.26M
- Solstice (Basis Trading): $203.28M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.06M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-22
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-21
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-21
- [SIMD-0529: [SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21
- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-10-21
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/702) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-21T02:14:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,925.73 | 1,987.14 | -59.66% |
| Average non-vote TPS | 1,852.43 | 1,987.14 | +7.27% |
| Average slot time (ms) | 216.20 | 212.40 | -1.76% |
| Active validators | 669.00 | 668.00 | -0.15% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 5,993,789,217.00 | 6,031,824,201.00 | +0.63% |
| SOL price | 106.33 | 105.97 | -0.34% |
| Stablecoin supply | 16,013,636,672.00 | 16,153,982,880.00 | +0.88% |
| 24h DEX volume | 2,235,070,439.00 | 2,278,261,933.37 | +1.93% |
| 24h chain fees | 13,196,843.63 | 11,875,251.66 | -10.01% |

### Change over 7d (vs run at 2026-10-15T02:04:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,158.40 | 1,987.14 | -61.48% |
| Average non-vote TPS | 2,079.66 | 1,987.14 | -4.45% |
| Average slot time (ms) | 216.60 | 212.40 | -1.94% |
| Active validators | 672.00 | 668.00 | -0.60% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 5,995,764,710.00 | 6,031,824,201.00 | +0.60% |
| SOL price | 103.85 | 105.97 | +2.04% |
| Stablecoin supply | 16,056,807,804.00 | 16,153,982,880.00 | +0.61% |
| 24h DEX volume | 2,248,882,317.32 | 2,278,261,933.37 | +1.31% |
| 24h chain fees | 10,646,585.63 | 11,875,251.66 | +11.54% |

### Change over 30d (vs run at 2026-09-21T21:17:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.01 | 1,987.14 | -57.35% |
| Average non-vote TPS | 2,142.85 | 1,987.14 | -7.27% |
| Average slot time (ms) | 266.70 | 212.40 | -20.36% |
| Active validators | 676.00 | 668.00 | -1.18% |
| Delinquent validators | 14.00 | 9.00 | -35.71% |
| Solana TVL | 6,474,683,879.00 | 6,031,824,201.00 | -6.84% |
| SOL price | 118.81 | 105.97 | -10.81% |
| Stablecoin supply | 15,907,385,261.00 | 16,153,982,880.00 | +1.55% |
| 24h DEX volume | 2,795,356,104.36 | 2,278,261,933.37 | -18.50% |
| 24h chain fees | 14,463,382.08 | 11,875,251.66 | -17.89% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
