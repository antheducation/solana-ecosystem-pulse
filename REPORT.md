# Solana Ecosystem Pulse

**Generated:** 2026-09-15T02:07:43Z · **Schema:** `1.0.0` · **Collection time:** 9.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.31 | +2.30% |
| Market cap | $60.06B | rank #7 |
| Total value locked | $5.93B | +0.11% |
| Stablecoin supply | $16.39B | +0.22% |
| DEX volume (24h) | $2.20B | +22.63% |
| Chain fees / REV (24h) | $14.42M | +2.73% |
| Non-vote TPS (1h avg) | 1,639 | peak 4,140 total |
| Active validators | 679 | 10 delinquent |
| Epoch 1035 | 2.77% complete | 420,021 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 82 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,638.9 average over the last 60 minutes; 1,733.2 in the latest sample.
- **Total TPS:** 3,753.3 average, 4,139.6 peak. Consensus votes account for 56.3% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 324.3 ms.
- **Block height:** 425,174,180 at absolute slot 447,131,979.
- **Epoch 1035:** slot 11,979 of 432,000 (2.77% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.647% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 78 ms |
| `solana-rpc.publicnode.com` | yes | 32 ms |
| `api.mainnet.solana.com` | yes | 122 ms |

## Validators & stake

- **679 active** validators, **10 delinquent** (1.45% by count, 0.074% by stake).
- **Total stake:** 439,248,639 SOL ($44.94B); stake rate 69.27% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.34% and top 33 hold 45.77% of active stake.
- **Commission:** median 5.0%, mean 12.47%; 245 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,757,712 | 4.046% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,373,377 | 3.730% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,492,605 | 2.846% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,369,566 | 2.590% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,669,319 | 2.203% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,225 | 2.109% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,035,103 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,372,355 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,944,775 | 1.582% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,553,626 | 1.493% | 0% |

## Economics

- **SOL:** $102.31 (+2.30% 24h, -1.96% 7d, +35.79% 30d). Market cap $60.06B, 24h volume $3.37B (5.62% of cap). Price source: `coingecko`.
- **TVL:** $5.93B across 338 protocols - rank #2 of 467 chains, 6.69% of all tracked chain TVL. +0.15% over 7d, -55.2% from its ATH.
- **Stablecoins:** $16.39B circulating on Solana (-1.83% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.20B in 24h, $17.12B over 7d across 123 venues. Volume/TVL turnover 0.370x per day.
- **REV (chain fees):** $14.42M in 24h, $384.86M over 30d. Retained chain revenue $5.10M (35.4% of fees). Annualised fees are 8.76% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,028,532 SOL circulating of 634,111,935 total (92.57%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.57B | +2.9% | -0.9% |
| 2 | Kamino Lend | Lending | $1.36B | +1.6% | +1.9% |
| 3 | Raydium AMM | Dexs | $1.15B | +3.4% | +1.2% |
| 4 | Jupiter Lend | Lending | $1.11B | +1.8% | +1.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | +2.7% | -1.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | +2.8% | -0.8% |
| 7 | BlackRock BUIDL | RWA | $992.89M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $753.78M | +1.6% | +0.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $530.24M | +2.9% | -1.2% |
| 10 | Marinade Native | Staking Pool | $390.50M | +2.8% | -4.9% |
| 11 | Sentora Curator | Risk Curators | $383.08M | -1.6% | -1.0% |
| 12 | PumpSwap | Dexs | $332.24M | +0.6% | -2.8% |

The top five protocols hold 38.1% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.41B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.4% · Lending 16.6% · Dexs 14.3% · RWA 11.8% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.24B of tokenised real-world assets and equities are locked on Solana - 13.636% of chain TVL.

- BlackRock BUIDL (RWA): $992.89M
- OnRe (RWA): $299.85M
- Solstice (Basis Trading): $235.03M
- Huma Finance V2 (RWA): $197.20M
- Ondo Yield Assets (RWA): $179.69M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

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

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-15
- [SIMD-0377: SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-14
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-14
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11

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

### Change over 24h (vs run at 2026-09-14T01:59:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,858.00 | 3,753.31 | -2.71% |
| Average non-vote TPS | 1,717.42 | 1,638.93 | -4.57% |
| Average slot time (ms) | 315.80 | 316.10 | +0.09% |
| Active validators | 678.00 | 679.00 | +0.15% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,820,704,370.00 | 5,932,971,504.00 | +1.93% |
| SOL price | 99.80 | 102.31 | +2.52% |
| Stablecoin supply | 16,352,347,705.00 | 16,390,847,094.00 | +0.24% |
| 24h DEX volume | 1,637,064,257.97 | 2,196,247,156.85 | +34.16% |
| 24h chain fees | 14,050,324.45 | 14,419,679.63 | +2.63% |

### Change over 7d (vs run at 2026-09-08T01:42:47Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,552.09 | 3,753.31 | +5.66% |
| Average non-vote TPS | 1,424.81 | 1,638.93 | +15.03% |
| Average slot time (ms) | 316.10 | 316.10 | +0.00% |
| Active validators | 676.00 | 679.00 | +0.44% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,910,151,740.00 | 5,932,971,504.00 | +0.39% |
| SOL price | 104.14 | 102.31 | -1.76% |
| Stablecoin supply | 16,740,790,725.00 | 16,390,847,094.00 | -2.09% |
| 24h DEX volume | 2,872,029,701.66 | 2,196,247,156.85 | -23.53% |
| 24h chain fees | 13,419,392.83 | 14,419,679.63 | +7.45% |

### Change over 30d (vs run at 2026-08-15T18:10:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,866.12 | 3,753.31 | -2.92% |
| Average non-vote TPS | 2,226.46 | 1,638.93 | -26.39% |
| Average slot time (ms) | 416.10 | 316.10 | -24.03% |
| Active validators | 687.00 | 679.00 | -1.16% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 4,817,167,805.00 | 5,932,971,504.00 | +23.16% |
| SOL price | 75.57 | 102.31 | +35.38% |
| Stablecoin supply | 16,008,773,555.00 | 16,390,847,094.00 | +2.39% |
| 24h DEX volume | 1,612,403,611.56 | 2,196,247,156.85 | +36.21% |
| 24h chain fees | 8,047,086.79 | 14,419,679.63 | +79.19% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 9.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
