# Solana Ecosystem Pulse

**Generated:** 2026-10-17T09:48:37Z · **Schema:** `1.0.0` · **Collection time:** 11.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.84 | -1.40% |
| Market cap | $61.79B | rank #7 |
| Total value locked | $5.97B | -0.77% |
| Stablecoin supply | $16.03B | -1.26% |
| DEX volume (24h) | $2.50B | -10.71% |
| Chain fees / REV (24h) | $12.24M | -4.27% |
| Non-vote TPS (1h avg) | 1,278 | peak 4,778 total |
| Active validators | 671 | 10 delinquent |
| Epoch 1060 | 16.76% complete | 359,582 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 108 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,277.5 average over the last 60 minutes; 1,166.0 in the latest sample.
- **Total TPS:** 4,356.1 average, 4,777.6 peak. Consensus votes account for 70.7% of all transactions.
- **Slot time:** 217.1 ms average (target 400 ms), worst 1-minute bucket 226.4 ms.
- **Block height:** 436,027,810 at absolute slot 457,992,418.
- **Epoch 1060:** slot 72,418 of 432,000 (16.76% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.598% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 123 ms |
| `solana-rpc.publicnode.com` | yes | 29 ms |
| `api.mainnet.solana.com` | yes | 54 ms |

## Validators & stake

- **671 active** validators, **10 delinquent** (1.47% by count, 0.012% by stake).
- **Total stake:** 438,750,365 SOL ($46.00B); stake rate 68.99% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 46.01% of active stake.
- **Commission:** median 5.0%, mean 12.68%; 230 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,532,933 | 3.997% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,736,568 | 3.587% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,161 | 2.846% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,972,883 | 2.501% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,191,942 | 2.323% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,445,787 | 2.153% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,250,229 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,759,724 | 1.769% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,991,827 | 1.594% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,726,220 | 1.533% | 0% |

## Economics

- **SOL:** $104.84 (-1.40% 24h, -4.60% 7d, +4.60% 30d). Market cap $61.79B, 24h volume $2.57B (4.15% of cap). Price source: `coingecko`.
- **TVL:** $5.97B across 325 protocols - rank #3 of 425 chains, 6.65% of all tracked chain TVL. -3.58% over 7d, -55.1% from its ATH.
- **Stablecoins:** $16.03B circulating on Solana (-1.35% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.50B in 24h, $13.52B over 7d across 136 venues. Volume/TVL turnover 0.419x per day.
- **REV (chain fees):** $12.24M in 24h, $459.98M over 30d. Retained chain revenue $4.93M (40.3% of fees). Annualised fees are 7.23% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,385,131 SOL circulating of 635,967,667 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | +0.8% | +1.3% |
| 2 | Kamino Lend | Lending | $1.31B | -1.0% | -1.0% |
| 3 | Raydium AMM | Dexs | $1.18B | -0.6% | -4.8% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.10B | -1.3% | -3.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.10B | -0.4% | -2.2% |
| 6 | Jupiter Lend | Lending | $1.10B | +0.5% | -3.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $741.81M | -0.9% | -3.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $547.87M | -1.5% | -3.0% |
| 9 | Sentora Curator | Risk Curators | $451.28M | -1.4% | -9.2% |
| 10 | Marinade Native | Staking Pool | $383.77M | -1.5% | -5.0% |
| 11 | PumpSwap | Dexs | $348.41M | -2.4% | -4.3% |
| 12 | Orca DEX | Dexs | $300.04M | -0.8% | -3.1% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 325 protocols the total is $15.98B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 16.8% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$892.79M of tokenised real-world assets and equities are locked on Solana - 5.586% of chain TVL.

- OnRe (RWA): $293.39M
- Huma (RWA): $280.87M
- Solstice (Basis Trading): $209.27M
- JupUSD (Basis Trading): $43.98M
- Plume Vaults (RWA): $35.50M

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

### Change over 24h (vs run at 2026-10-16T10:14:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,584.52 | 4,356.06 | -4.98% |
| Average non-vote TPS | 1,477.61 | 1,277.52 | -13.54% |
| Average slot time (ms) | 215.10 | 217.10 | +0.93% |
| Active validators | 671.00 | 671.00 | +0.00% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 6,025,134,675.00 | 5,965,614,107.00 | -0.99% |
| SOL price | 105.70 | 104.84 | -0.81% |
| Stablecoin supply | 16,234,677,076.00 | 16,028,712,157.00 | -1.27% |
| 24h DEX volume | 2,421,172,051.03 | 2,499,920,867.12 | +3.25% |
| 24h chain fees | 12,667,804.48 | 12,237,570.18 | -3.40% |

### Change over 7d (vs run at 2026-10-10T11:28:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,325.84 | 4,356.06 | +0.70% |
| Average non-vote TPS | 1,230.91 | 1,277.52 | +3.79% |
| Average slot time (ms) | 217.40 | 217.10 | -0.14% |
| Active validators | 675.00 | 671.00 | -0.59% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 6,201,943,177.00 | 5,965,614,107.00 | -3.81% |
| SOL price | 109.48 | 104.84 | -4.24% |
| Stablecoin supply | 16,426,938,969.00 | 16,028,712,157.00 | -2.42% |
| 24h DEX volume | 1,978,097,665.91 | 2,499,920,867.12 | +26.38% |
| 24h chain fees | 13,931,064.19 | 12,237,570.18 | -12.16% |

### Change over 30d (vs run at 2026-09-17T20:39:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,673.89 | 4,356.06 | -6.80% |
| Average non-vote TPS | 2,551.83 | 1,277.52 | -49.94% |
| Average slot time (ms) | 318.10 | 217.10 | -31.75% |
| Active validators | 677.00 | 671.00 | -0.89% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 5,865,883,806.00 | 5,965,614,107.00 | +1.70% |
| SOL price | 101.14 | 104.84 | +3.66% |
| Stablecoin supply | 15,774,027,557.00 | 16,028,712,157.00 | +1.61% |
| 24h DEX volume | 2,800,249,070.18 | 2,499,920,867.12 | -10.73% |
| 24h chain fees | 14,069,098.05 | 12,237,570.18 | -13.02% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
