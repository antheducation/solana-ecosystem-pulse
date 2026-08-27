# Solana Ecosystem Pulse

**Generated:** 2026-08-27T16:57:26Z · **Schema:** `1.0.0` · **Collection time:** 22.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $109.05 | +13.74% |
| Market cap | $63.75B | rank #7 |
| Total value locked | $5.97B | +6.51% |
| Stablecoin supply | $16.30B | -0.12% |
| DEX volume (24h) | $2.35B | -19.87% |
| Chain fees / REV (24h) | $15.17M | +14.62% |
| Non-vote TPS (1h avg) | 2,878 | peak 5,252 total |
| Active validators | 685 | 12 delinquent |
| Epoch 1023 | 48.89% complete | 220,776 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 4 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 367.20 sits 16.2 sigma below the median of the last 64 runs (415.20, -11.6%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 109.05 sits 6.9 sigma above the median of the last 64 runs (77.09, +41.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 13.7% in 24h) | SOL price changed +13.7% over the last day, past the 8% alert band. | `threshold` |
| [WARNING] | Solana TVL moved sharply (up 6.5% in 24h) | Solana TVL changed +6.5% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 5,971,320,873.00 sits 4.8 sigma above the median of the last 64 runs (4,897,165,849.00, +21.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,877.9 average over the last 60 minutes; 2,626.1 in the latest sample.
- **Total TPS:** 4,739.8 average, 5,252.1 peak. Consensus votes account for 39.3% of all transactions.
- **Slot time:** 367.2 ms average (target 400 ms), worst 1-minute bucket 384.6 ms.
- **Block height:** 420,195,483 at absolute slot 442,147,224.
- **Epoch 1023:** slot 211,224 of 432,000 (48.89% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.677% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 343 ms |
| `solana-rpc.publicnode.com` | yes | 180 ms |
| `api.mainnet.solana.com` | yes | 322 ms |

## Validators & stake

- **685 active** validators, **12 delinquent** (1.72% by count, 0.962% by stake).
- **Total stake:** 436,884,837 SOL ($47.64B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.51% and top 33 hold 45.89% of active stake.
- **Commission:** median 5.0%, mean 13.08%; 247 validators at 0% and 68 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,062,869 | 3.943% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,029,433 | 3.705% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,314,379 | 2.846% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,751,683 | 2.716% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,852 | 2.130% | 7% |
| 6 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,051,084 | 2.092% | 0% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,904,595 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,849,682 | 1.814% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,301,740 | 1.688% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,578,261 | 1.520% | 0% |

## Economics

- **SOL:** $109.05 (+13.74% 24h, +24.90% 7d, +46.90% 30d). Market cap $63.75B, 24h volume $6.74B (10.58% of cap). Price source: `coingecko`.
- **TVL:** $5.97B across 333 protocols - rank #2 of 465 chains, 6.68% of all tracked chain TVL. +14.26% over 7d, -54.9% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-0.19% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.35B in 24h, $21.32B over 7d across 119 venues. Volume/TVL turnover 0.394x per day.
- **REV (chain fees):** $15.17M in 24h, $297.33M over 30d. Retained chain revenue $6.28M (41.4% of fees). Annualised fees are 8.69% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 584,062,556 SOL circulating of 632,969,372 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.63B | +12.2% | +27.5% |
| 2 | Kamino Lend | Lending | $1.26B | +7.5% | +11.2% |
| 3 | Raydium AMM | Dexs | $1.14B | +8.9% | +22.3% |
| 4 | Jupiter Lend | Lending | $1.13B | +7.6% | +11.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.10B | +11.8% | +27.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.08B | +11.9% | +26.2% |
| 7 | BlackRock BUIDL | RWA | $886.45M | +1.1% | +19.7% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $791.35M | +6.3% | +7.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $557.28M | +12.0% | +25.5% |
| 10 | xStocks | RWA | $439.42M | +3.7% | +8.2% |
| 11 | Marinade Native | Staking Pool | $437.82M | +16.3% | +80.7% |
| 12 | PumpSwap | Dexs | $365.65M | +10.8% | +29.4% |

The top five protocols hold 36.9% of Solana's tracked TVL. Summed across all 333 protocols the total is $16.96B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.9% · Lending 15.8% · Dexs 14.1% · RWA 12.2% · Derivatives 5.2% · Staking Pool 4.0%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 14.498% of chain TVL.

- BlackRock BUIDL (RWA): $886.45M
- xStocks (RWA): $439.42M
- Solstice (Basis Trading): $303.10M
- OnRe (RWA): $278.02M
- Ondo Yield Assets (RWA): $178.52M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,007.7 unique fee payers** signed per block (1,481 distinct addresses in the union, 51.0% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-26
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-26T19:30:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,472.91 | 4,739.80 | +5.97% |
| Average non-vote TPS | 2,616.46 | 2,877.86 | +9.99% |
| Average slot time (ms) | 366.20 | 367.20 | +0.27% |
| Active validators | 685.00 | 685.00 | +0.00% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,557,854,195.00 | 5,971,320,873.00 | +7.44% |
| SOL price | 96.76 | 109.05 | +12.70% |
| Stablecoin supply | 16,315,958,333.00 | 16,295,559,951.00 | -0.13% |
| 24h DEX volume | 2,934,986,439.19 | 2,351,677,355.00 | -19.87% |
| 24h chain fees | 13,235,652.04 | 15,169,688.78 | +14.61% |

### Change over 7d (vs run at 2026-08-20T18:20:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,033.78 | 4,739.80 | -5.84% |
| Average non-vote TPS | 3,388.67 | 2,877.86 | -15.07% |
| Average slot time (ms) | 417.00 | 367.20 | -11.94% |
| Active validators | 690.00 | 685.00 | -0.72% |
| Delinquent validators | 6.00 | 12.00 | +100.00% |
| Solana TVL | 5,300,056,423.00 | 5,971,320,873.00 | +12.67% |
| SOL price | 86.96 | 109.05 | +25.40% |
| Stablecoin supply | 16,325,927,693.00 | 16,295,559,951.00 | -0.19% |
| 24h DEX volume | 3,009,837,694.95 | 2,351,677,355.00 | -21.87% |
| 24h chain fees | 13,676,729.38 | 15,169,688.78 | +10.92% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,739.80 | +20.46% |
| Average non-vote TPS | 2,312.46 | 2,877.86 | +24.45% |
| Average slot time (ms) | 424.10 | 367.20 | -13.42% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 12.00 | +50.00% |
| Solana TVL | 4,740,035,266.00 | 5,971,320,873.00 | +25.98% |
| SOL price | 72.81 | 109.05 | +49.77% |
| Stablecoin supply | 16,197,749,831.00 | 16,295,559,951.00 | +0.60% |
| 24h DEX volume | 1,636,927,091.91 | 2,351,677,355.00 | +43.66% |
| 24h chain fees | 7,777,648.77 | 15,169,688.78 | +95.04% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
