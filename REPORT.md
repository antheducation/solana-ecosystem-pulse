# Solana Ecosystem Pulse

**Generated:** 2026-10-17T14:31:42Z · **Schema:** `1.0.0` · **Collection time:** 12.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.23 | -1.83% |
| Market cap | $61.44B | rank #7 |
| Total value locked | $5.95B | -1.21% |
| Stablecoin supply | $16.03B | -1.26% |
| DEX volume (24h) | $2.17B | -22.56% |
| Chain fees / REV (24h) | $12.43M | -2.76% |
| Non-vote TPS (1h avg) | 1,807 | peak 5,493 total |
| Active validators | 670 | 11 delinquent |
| Epoch 1060 | 34.88% complete | 281,309 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 109 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,806.6 average over the last 60 minutes; 2,118.8 in the latest sample.
- **Total TPS:** 4,884.1 average, 5,492.7 peak. Consensus votes account for 63.0% of all transactions.
- **Slot time:** 216.7 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 436,106,071 at absolute slot 458,070,691.
- **Epoch 1060:** slot 150,691 of 432,000 (34.88% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.598% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 183 ms |
| `solana-rpc.publicnode.com` | yes | 75 ms |
| `api.mainnet.solana.com` | yes | 112 ms |

## Validators & stake

- **670 active** validators, **11 delinquent** (1.62% by count, 0.012% by stake).
- **Total stake:** 438,750,365 SOL ($45.73B); stake rate 68.99% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 46.01% of active stake.
- **Commission:** median 5.0%, mean 12.69%; 230 validators at 0% and 62 at 100%.

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

- **SOL:** $104.23 (-1.83% 24h, -5.11% 7d, +3.59% 30d). Market cap $61.44B, 24h volume $2.16B (3.51% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 324 protocols - rank #3 of 425 chains, 6.64% of all tracked chain TVL. -4.01% over 7d, -55.3% from its ATH.
- **Stablecoins:** $16.03B circulating on Solana (-1.35% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.17B in 24h, $14.38B over 7d across 136 venues. Volume/TVL turnover 0.364x per day.
- **REV (chain fees):** $12.43M in 24h, $460.44M over 30d. Retained chain revenue $4.98M (40.1% of fees). Annualised fees are 7.39% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,384,928 SOL circulating of 635,967,464 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +1.0% | +0.5% |
| 2 | Kamino Lend | Lending | $1.31B | -0.7% | -1.3% |
| 3 | Raydium AMM | Dexs | $1.18B | -2.1% | -5.3% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.09B | -1.3% | -4.3% |
| 5 | Jupiter Lend | Lending | $1.09B | -0.0% | -4.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.09B | -0.0% | -3.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $738.23M | -1.1% | -4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $543.90M | -1.3% | -3.7% |
| 9 | Sentora Curator | Risk Curators | $451.15M | -0.1% | -9.2% |
| 10 | Marinade Native | Staking Pool | $380.67M | -1.3% | -5.8% |
| 11 | PumpSwap | Dexs | $349.35M | -1.9% | -4.0% |
| 12 | Orca DEX | Dexs | $299.09M | -0.5% | -3.4% |

The top five protocols hold 40.7% of Solana's tracked TVL. Summed across all 324 protocols the total is $15.89B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.8% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$892.21M of tokenised real-world assets and equities are locked on Solana - 5.614% of chain TVL.

- OnRe (RWA): $293.40M
- Huma (RWA): $280.38M
- Solstice (Basis Trading): $209.24M
- JupUSD (Basis Trading): $44.00M
- Plume Vaults (RWA): $35.49M

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

### Change over 24h (vs run at 2026-10-16T15:39:44Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,269.25 | 4,884.13 | -7.31% |
| Average non-vote TPS | 2,179.57 | 1,806.58 | -17.11% |
| Average slot time (ms) | 216.60 | 216.70 | +0.05% |
| Active validators | 672.00 | 670.00 | -0.30% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 6,025,302,280.00 | 5,952,090,339.00 | -1.22% |
| SOL price | 104.63 | 104.23 | -0.38% |
| Stablecoin supply | 16,234,288,263.00 | 16,028,651,978.00 | -1.27% |
| 24h DEX volume | 2,539,283,878.03 | 2,168,129,752.12 | -14.62% |
| 24h chain fees | 12,783,602.89 | 12,431,928.33 | -2.75% |

### Change over 7d (vs run at 2026-10-10T16:28:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,118.99 | 4,884.13 | -4.59% |
| Average non-vote TPS | 2,059.12 | 1,806.58 | -12.26% |
| Average slot time (ms) | 219.80 | 216.70 | -1.41% |
| Active validators | 675.00 | 670.00 | -0.74% |
| Delinquent validators | 6.00 | 11.00 | +83.33% |
| Solana TVL | 6,217,510,321.00 | 5,952,090,339.00 | -4.27% |
| SOL price | 110.18 | 104.23 | -5.40% |
| Stablecoin supply | 16,427,119,543.00 | 16,028,651,978.00 | -2.43% |
| 24h DEX volume | 1,978,097,665.91 | 2,168,129,752.12 | +9.61% |
| 24h chain fees | 13,913,073.19 | 12,431,928.33 | -10.65% |

### Change over 30d (vs run at 2026-09-17T20:39:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,673.89 | 4,884.13 | +4.50% |
| Average non-vote TPS | 2,551.83 | 1,806.58 | -29.20% |
| Average slot time (ms) | 318.10 | 216.70 | -31.88% |
| Active validators | 677.00 | 670.00 | -1.03% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 5,865,883,806.00 | 5,952,090,339.00 | +1.47% |
| SOL price | 101.14 | 104.23 | +3.06% |
| Stablecoin supply | 15,774,027,557.00 | 16,028,651,978.00 | +1.61% |
| 24h DEX volume | 2,800,249,070.18 | 2,168,129,752.12 | -22.57% |
| 24h chain fees | 14,069,098.05 | 12,431,928.33 | -11.64% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
