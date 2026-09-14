# Solana Ecosystem Pulse

**Generated:** 2026-09-14T21:06:14Z · **Schema:** `1.0.0` · **Collection time:** 17.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.65 | +2.25% |
| Market cap | $60.79B | rank #7 |
| Total value locked | $5.95B | +0.74% |
| Stablecoin supply | $16.35B | -1.03% |
| DEX volume (24h) | $1.79B | +2.72% |
| Chain fees / REV (24h) | $14.04M | +3.22% |
| Non-vote TPS (1h avg) | 2,156 | peak 5,417 total |
| Active validators | 678 | 12 delinquent |
| Epoch 1034 | 89.53% complete | 45,217 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 82 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,156.0 average over the last 60 minutes; 2,258.0 in the latest sample.
- **Total TPS:** 4,278.0 average, 5,417.2 peak. Consensus votes account for 49.6% of all transactions.
- **Slot time:** 317.9 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 425,117,133 at absolute slot 447,074,783.
- **Epoch 1034:** slot 386,783 of 432,000 (89.53% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.649% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 60 ms |
| `solana-rpc.publicnode.com` | yes | 41 ms |
| `api.mainnet.solana.com` | yes | 77 ms |

## Validators & stake

- **678 active** validators, **12 delinquent** (1.74% by count, 0.054% by stake).
- **Total stake:** 438,740,367 SOL ($45.48B); stake rate 69.20% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.69% of active stake.
- **Commission:** median 5.0%, mean 12.79%; 242 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,568,189 | 4.006% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,361,599 | 3.731% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,501,349 | 2.851% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,372,391 | 2.593% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,619,665 | 2.194% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,712 | 2.110% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,025,175 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,367,885 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,943,003 | 1.583% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,552,506 | 1.494% | 0% |

## Economics

- **SOL:** $103.65 (+2.25% 24h, -0.42% 7d, +37.34% 30d). Market cap $60.79B, 24h volume $3.48B (5.72% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 338 protocols - rank #2 of 467 chains, 6.67% of all tracked chain TVL. -0.92% over 7d, -55.0% from its ATH.
- **Stablecoins:** $16.35B circulating on Solana (-2.31% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.79B in 24h, $18.46B over 7d across 123 venues. Volume/TVL turnover 0.301x per day.
- **REV (chain fees):** $14.04M in 24h, $389.54M over 30d. Retained chain revenue $5.08M (36.2% of fees). Annualised fees are 8.43% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,892,419 SOL circulating of 634,017,165 total (92.57%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | +2.3% | -2.6% |
| 2 | Kamino Lend | Lending | $1.36B | +1.2% | +1.2% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.4% | +0.2% |
| 4 | Jupiter Lend | Lending | $1.11B | +1.2% | -1.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.07B | +2.5% | -2.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | +2.5% | -3.1% |
| 7 | BlackRock BUIDL | RWA | $992.89M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $760.67M | +1.6% | -0.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $534.99M | +2.5% | -2.8% |
| 10 | Marinade Native | Staking Pool | $393.55M | +2.3% | -6.1% |
| 11 | Sentora Curator | Risk Curators | $383.04M | -1.6% | -1.5% |
| 12 | PumpSwap | Dexs | $333.37M | +1.8% | -2.1% |

The top five protocols hold 38.1% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.48B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.5% · Lending 16.6% · Dexs 14.2% · RWA 11.7% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.560% of chain TVL.

- BlackRock BUIDL (RWA): $992.89M
- OnRe (RWA): $299.62M
- Solstice (Basis Trading): $235.02M
- Huma Finance V2 (RWA): $194.13M
- Ondo Yield Assets (RWA): $179.93M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,023.0 unique fee payers** signed per block (1,588 distinct addresses in the union, 48.3% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0377: SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-14
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-14
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-11

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

### Change over 24h (vs run at 2026-09-13T19:56:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,911.91 | 4,277.98 | +9.36% |
| Average non-vote TPS | 1,778.64 | 2,155.99 | +21.22% |
| Average slot time (ms) | 315.70 | 317.90 | +0.70% |
| Active validators | 676.00 | 678.00 | +0.30% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 5,861,539,247.00 | 5,949,162,754.00 | +1.49% |
| SOL price | 100.85 | 103.65 | +2.78% |
| Stablecoin supply | 16,525,835,618.00 | 16,354,375,710.00 | -1.04% |
| 24h DEX volume | 1,691,135,695.08 | 1,790,994,711.97 | +5.90% |
| 24h chain fees | 13,515,656.40 | 14,036,101.64 | +3.85% |

### Change over 7d (vs run at 2026-09-07T20:51:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,930.66 | 4,277.98 | +8.84% |
| Average non-vote TPS | 1,809.47 | 2,155.99 | +19.15% |
| Average slot time (ms) | 316.70 | 317.90 | +0.38% |
| Active validators | 676.00 | 678.00 | +0.30% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,896,988,391.00 | 5,949,162,754.00 | +0.88% |
| SOL price | 104.08 | 103.65 | -0.41% |
| Stablecoin supply | 16,741,090,548.00 | 16,354,375,710.00 | -2.31% |
| 24h DEX volume | 2,904,503,252.44 | 1,790,994,711.97 | -38.34% |
| 24h chain fees | 14,655,299.70 | 14,036,101.64 | -4.23% |

### Change over 30d (vs run at 2026-08-15T18:10:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,866.12 | 4,277.98 | +10.65% |
| Average non-vote TPS | 2,226.46 | 2,155.99 | -3.17% |
| Average slot time (ms) | 416.10 | 317.90 | -23.60% |
| Active validators | 687.00 | 678.00 | -1.31% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 4,817,167,805.00 | 5,949,162,754.00 | +23.50% |
| SOL price | 75.57 | 103.65 | +37.16% |
| Stablecoin supply | 16,008,773,555.00 | 16,354,375,710.00 | +2.16% |
| 24h DEX volume | 1,612,403,611.56 | 1,790,994,711.97 | +11.08% |
| 24h chain fees | 8,047,086.79 | 14,036,101.64 | +74.42% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 17.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
