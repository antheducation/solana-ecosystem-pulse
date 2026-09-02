# Solana Ecosystem Pulse

**Generated:** 2026-09-02T10:03:32Z · **Schema:** `1.0.0` · **Collection time:** 24.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.48 | -3.50% |
| Market cap | $57.66B | rank #7 |
| Total value locked | $5.71B | -4.64% |
| Stablecoin supply | $15.85B | -0.74% |
| DEX volume (24h) | $2.25B | -10.19% |
| Chain fees / REV (24h) | $12.27M | -9.14% |
| Non-vote TPS (1h avg) | 1,015 | peak 3,834 total |
| Active validators | 673 | 22 delinquent |
| Epoch 1027 | 1.19% complete | 426,856 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 65 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 673.00 sits 4.4 sigma below the median of the last 65 runs (686.00, -1.9%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 22.00 sits 4.0 sigma above the median of the last 65 runs (10.00, +120.0%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,014.9 average over the last 60 minutes; 617.2 in the latest sample.
- **Total TPS:** 3,149.2 average, 3,833.8 peak. Consensus votes account for 67.8% of all transactions.
- **Slot time:** 315.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 421,716,601 at absolute slot 443,669,144.
- **Epoch 1027:** slot 5,144 of 432,000 (1.19% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 551 ms |
| `solana-rpc.publicnode.com` | yes | 1053 ms |
| `api.mainnet.solana.com` | yes | 500 ms |

## Validators & stake

- **673 active** validators, **22 delinquent** (3.17% by count, 0.226% by stake).
- **Total stake:** 438,422,357 SOL ($43.18B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.41%; 242 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.966% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,325,737 | 3.732% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,462,274 | 2.849% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,304,498 | 2.584% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,565,273 | 2.187% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,486 | 2.123% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,040,435 | 2.067% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,220,140 | 1.651% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,125,475 | 1.629% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,590,653 | 1.507% | 0% |

## Economics

- **SOL:** $98.48 (-3.50% 24h, +2.43% 7d, +35.50% 30d). Market cap $57.66B, 24h volume $3.29B (5.70% of cap). Price source: `coingecko`.
- **TVL:** $5.71B across 340 protocols - rank #2 of 465 chains, 6.67% of all tracked chain TVL. +1.79% over 7d, -56.9% from its ATH.
- **Stablecoins:** $15.85B circulating on Solana (-1.86% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.25B in 24h, $16.74B over 7d across 120 venues. Volume/TVL turnover 0.394x per day.
- **REV (chain fees):** $12.27M in 24h, $331.58M over 30d. Retained chain revenue $5.53M (45.1% of fees). Annualised fees are 7.77% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,292,459 SOL circulating of 633,361,825 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.51B | -3.0% | +3.0% |
| 2 | Kamino Lend | Lending | $1.23B | -1.2% | +4.4% |
| 3 | Raydium AMM | Dexs | $1.08B | -3.1% | +1.8% |
| 4 | Jupiter Lend | Lending | $1.06B | -1.3% | +1.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | -1.9% | +4.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $998.27M | -2.9% | +3.0% |
| 7 | BlackRock BUIDL | RWA | $887.01M | +0.0% | +1.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $745.97M | -1.5% | -0.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $518.69M | -1.8% | +3.6% |
| 10 | xStocks | RWA | $431.15M | -1.8% | +0.7% |
| 11 | Marinade Native | Staking Pool | $396.90M | -3.6% | +5.0% |
| 12 | Sentora | Risk Curators | $362.17M | +0.2% | -0.3% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.22B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.5% · Lending 15.8% · Dexs 14.0% · RWA 12.8% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.789% of chain TVL.

- BlackRock BUIDL (RWA): $887.01M
- xStocks (RWA): $431.15M
- OnRe (RWA): $288.02M
- Solstice (Basis Trading): $249.86M
- Ondo Yield Assets (RWA): $179.26M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **801.0 unique fee payers** signed per block (1,050 distinct addresses in the union, 56.3% overlap between blocks).

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
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27

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

### Change over 24h (vs run at 2026-09-01T10:37:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,426.48 | 3,149.23 | -8.09% |
| Average non-vote TPS | 1,291.44 | 1,014.87 | -21.42% |
| Average slot time (ms) | 316.80 | 315.10 | -0.54% |
| Active validators | 680.00 | 673.00 | -1.03% |
| Delinquent validators | 14.00 | 22.00 | +57.14% |
| Solana TVL | 5,808,427,098.00 | 5,706,889,294.00 | -1.75% |
| SOL price | 102.48 | 98.48 | -3.90% |
| Stablecoin supply | 16,130,106,220.00 | 15,850,556,625.00 | -1.73% |
| 24h DEX volume | 2,457,757,824.05 | 2,246,687,191.49 | -8.59% |
| 24h chain fees | 13,288,721.08 | 12,266,833.67 | -7.69% |

### Change over 7d (vs run at 2026-08-26T12:23:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,489.57 | 3,149.23 | -9.75% |
| Average non-vote TPS | 1,624.74 | 1,014.87 | -37.54% |
| Average slot time (ms) | 365.20 | 315.10 | -13.72% |
| Active validators | 684.00 | 673.00 | -1.61% |
| Delinquent validators | 11.00 | 22.00 | +100.00% |
| Solana TVL | 5,596,733,884.00 | 5,706,889,294.00 | +1.97% |
| SOL price | 97.02 | 98.48 | +1.50% |
| Stablecoin supply | 16,315,003,426.00 | 15,850,556,625.00 | -2.85% |
| 24h DEX volume | 2,934,986,439.19 | 2,246,687,191.49 | -23.45% |
| 24h chain fees | 13,134,401.04 | 12,266,833.67 | -6.61% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,149.23 | -19.96% |
| Average non-vote TPS | 2,312.46 | 1,014.87 | -56.11% |
| Average slot time (ms) | 424.10 | 315.10 | -25.70% |
| Active validators | 692.00 | 673.00 | -2.75% |
| Delinquent validators | 8.00 | 22.00 | +175.00% |
| Solana TVL | 4,740,035,266.00 | 5,706,889,294.00 | +20.40% |
| SOL price | 72.81 | 98.48 | +35.26% |
| Stablecoin supply | 16,197,749,831.00 | 15,850,556,625.00 | -2.14% |
| 24h DEX volume | 1,636,927,091.91 | 2,246,687,191.49 | +37.25% |
| 24h chain fees | 7,777,648.77 | 12,266,833.67 | +57.72% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 24.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
