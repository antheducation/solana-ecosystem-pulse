# Solana Ecosystem Pulse

**Generated:** 2026-10-20T02:21:18Z · **Schema:** `1.0.0` · **Collection time:** 22.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.78 | -0.32% |
| Market cap | $61.77B | rank #7 |
| Total value locked | $5.87B | -0.15% |
| Stablecoin supply | $15.91B | +0.45% |
| DEX volume (24h) | $1.61B | -5.09% |
| Chain fees / REV (24h) | $11.95M | +21.43% |
| Non-vote TPS (1h avg) | 1,787 | peak 5,835 total |
| Active validators | 668 | 11 delinquent |
| Epoch 1062 | 64.53% complete | 153,229 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 112 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,787.2 average over the last 60 minutes; 1,754.2 in the latest sample.
- **Total TPS:** 4,836.3 average, 5,835.0 peak. Consensus votes account for 63.0% of all transactions.
- **Slot time:** 218.3 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 437,097,887 at absolute slot 459,062,771.
- **Epoch 1062:** slot 278,771 of 432,000 (64.53% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.595% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 137 ms |
| `solana-rpc.publicnode.com` | yes | 165 ms |
| `api.mainnet.solana.com` | yes | 177 ms |

## Validators & stake

- **668 active** validators, **11 delinquent** (1.62% by count, 0.003% by stake).
- **Total stake:** 437,880,622 SOL ($45.88B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 13.16%; 227 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,095,415 | 3.904% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,730,365 | 3.592% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,524,168 | 2.860% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,975,836 | 2.507% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,890 | 2.219% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,481,609 | 2.165% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,107 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,119 | 1.778% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,993,888 | 1.597% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,731,556 | 1.537% | 0% |

## Economics

- **SOL:** $104.78 (-0.32% 24h, -0.43% 7d, -4.83% 30d). Market cap $61.77B, 24h volume $2.55B (4.14% of cap). Price source: `coingecko`.
- **TVL:** $5.87B across 328 protocols - rank #4 of 420 chains, 6.59% of all tracked chain TVL. -2.22% over 7d, -54.7% from its ATH.
- **Stablecoins:** $15.91B circulating on Solana (-0.95% 7d) - $2.71 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.61B in 24h, $13.41B over 7d across 136 venues. Volume/TVL turnover 0.274x per day.
- **REV (chain fees):** $11.95M in 24h, $444.54M over 30d. Retained chain revenue $4.81M (40.2% of fees). Annualised fees are 7.06% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,493,415 SOL circulating of 636,089,964 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | -0.0% | +3.4% |
| 2 | Kamino Lend | Lending | $1.31B | -0.3% | +1.1% |
| 3 | Raydium AMM | Dexs | $1.18B | +3.9% | -2.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | +0.5% | +2.1% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.09B | -0.1% | +0.3% |
| 6 | Jupiter Lend | Lending | $1.02B | -0.7% | -7.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $740.23M | -0.1% | -0.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $546.06M | +0.1% | +1.0% |
| 9 | Sentora Curator | Risk Curators | $448.37M | -0.6% | -5.0% |
| 10 | Marinade Native | Staking Pool | $378.16M | -0.8% | -1.7% |
| 11 | PumpSwap | Dexs | $348.88M | +2.9% | -2.4% |
| 12 | Orca DEX | Dexs | $299.47M | +0.8% | -0.1% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.84B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.4% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$885.54M of tokenised real-world assets and equities are locked on Solana - 5.590% of chain TVL.

- OnRe (RWA): $293.97M
- Huma (RWA): $274.70M
- Solstice (Basis Trading): $209.29M
- JupUSD (Basis Trading): $43.12M
- Plume Vaults (RWA): $34.81M

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

- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-19
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-19
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-19
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-19
- [100M CUs Pt2](https://github.com/solana-foundation/solana-improvement-documents/pull/698) - updated 2026-10-19
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-19
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-19

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

### Change over 24h (vs run at 2026-10-19T02:05:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,870.39 | 4,836.27 | -0.70% |
| Average non-vote TPS | 1,819.00 | 1,787.15 | -1.75% |
| Average slot time (ms) | 217.50 | 218.30 | +0.37% |
| Active validators | 666.00 | 668.00 | +0.30% |
| Delinquent validators | 14.00 | 11.00 | -21.43% |
| Solana TVL | 5,822,373,107.00 | 5,874,392,428.00 | +0.89% |
| SOL price | 104.90 | 104.78 | -0.11% |
| Stablecoin supply | 15,839,425,505.00 | 15,910,715,203.00 | +0.45% |
| 24h DEX volume | 1,565,959,221.38 | 1,610,955,050.83 | +2.87% |
| 24h chain fees | 9,714,592.98 | 11,948,280.30 | +22.99% |

### Change over 7d (vs run at 2026-10-13T04:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,857.67 | 4,836.27 | -0.44% |
| Average non-vote TPS | 1,791.44 | 1,787.15 | -0.24% |
| Average slot time (ms) | 218.00 | 218.30 | +0.14% |
| Active validators | 672.00 | 668.00 | -0.60% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 6,026,822,576.00 | 5,874,392,428.00 | -2.53% |
| SOL price | 107.65 | 104.78 | -2.67% |
| Stablecoin supply | 16,240,493,273.00 | 15,910,715,203.00 | -2.03% |
| 24h DEX volume | 1,866,875,583.02 | 1,610,955,050.83 | -13.71% |
| 24h chain fees | 12,980,703.44 | 11,948,280.30 | -7.95% |

### Change over 30d (vs run at 2026-09-19T19:41:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,683.68 | 4,836.27 | +3.26% |
| Average non-vote TPS | 2,161.60 | 1,787.15 | -17.32% |
| Average slot time (ms) | 267.00 | 218.30 | -18.24% |
| Active validators | 677.00 | 668.00 | -1.33% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 6,243,262,565.00 | 5,874,392,428.00 | -5.91% |
| SOL price | 111.27 | 104.78 | -5.83% |
| Stablecoin supply | 15,875,774,561.00 | 15,910,715,203.00 | +0.22% |
| 24h DEX volume | 3,536,797,881.43 | 1,610,955,050.83 | -54.45% |
| 24h chain fees | 17,457,812.00 | 11,948,280.30 | -31.56% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 22.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
