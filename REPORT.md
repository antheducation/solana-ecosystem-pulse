# Solana Ecosystem Pulse

**Generated:** 2026-09-02T15:26:57Z · **Schema:** `1.0.0` · **Collection time:** 13.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.97 | -2.56% |
| Market cap | $57.93B | rank #7 |
| Total value locked | $5.62B | -6.04% |
| Stablecoin supply | $15.85B | -0.74% |
| DEX volume (24h) | $2.17B | -13.19% |
| Chain fees / REV (24h) | $12.64M | -5.97% |
| Non-vote TPS (1h avg) | 1,822 | peak 4,767 total |
| Active validators | 677 | 18 delinquent |
| Epoch 1027 | 15.46% complete | 365,195 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 65 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL moved sharply (down 6.0% in 24h) | Solana TVL changed -6.0% over the last day, past the 6% alert band. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 677.00 sits 3.0 sigma below the median of the last 65 runs (686.00, -1.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,822.1 average over the last 60 minutes; 1,846.2 in the latest sample.
- **Total TPS:** 3,963.5 average, 4,767.0 peak. Consensus votes account for 54.0% of all transactions.
- **Slot time:** 314.8 ms average (target 400 ms), worst 1-minute bucket 322.6 ms.
- **Block height:** 421,778,208 at absolute slot 443,730,805.
- **Epoch 1027:** slot 66,805 of 432,000 (15.46% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 87 ms |
| `solana-rpc.publicnode.com` | yes | 56 ms |
| `api.mainnet.solana.com` | yes | 116 ms |

## Validators & stake

- **677 active** validators, **18 delinquent** (2.59% by count, 0.048% by stake).
- **Total stake:** 438,422,357 SOL ($43.39B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.36%; 244 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.959% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,325,737 | 3.726% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,462,274 | 2.844% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,304,498 | 2.580% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,565,273 | 2.183% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,486 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,040,435 | 2.063% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,220,140 | 1.648% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,125,475 | 1.626% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,590,653 | 1.504% | 0% |

## Economics

- **SOL:** $98.97 (-2.56% 24h, +3.68% 7d, +34.29% 30d). Market cap $57.93B, 24h volume $3.40B (5.87% of cap). Price source: `coingecko`.
- **TVL:** $5.62B across 341 protocols - rank #2 of 465 chains, 6.62% of all tracked chain TVL. +0.29% over 7d, -57.5% from its ATH.
- **Stablecoins:** $15.85B circulating on Solana (-1.87% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.17B in 24h, $16.92B over 7d across 120 venues. Volume/TVL turnover 0.386x per day.
- **REV (chain fees):** $12.64M in 24h, $332.77M over 30d. Retained chain revenue $5.79M (45.8% of fees). Annualised fees are 7.97% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,292,279 SOL circulating of 633,361,645 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.49B | -4.3% | +1.8% |
| 2 | Kamino Lend | Lending | $1.22B | -2.2% | +3.3% |
| 3 | Raydium AMM | Dexs | $1.06B | -4.2% | -0.4% |
| 4 | Jupiter Lend | Lending | $1.05B | -2.2% | -0.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.02B | -3.9% | +2.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $987.07M | -4.2% | +1.9% |
| 7 | BlackRock BUIDL | RWA | $887.01M | +0.0% | +1.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $734.24M | -3.0% | -1.8% |
| 9 | Jupiter Staked SOL | Liquid Staking | $507.04M | -4.2% | +1.3% |
| 10 | xStocks | RWA | $428.94M | -1.2% | +0.2% |
| 11 | Marinade Native | Staking Pool | $391.51M | -3.6% | +3.6% |
| 12 | Sentora | Risk Curators | $362.39M | +0.2% | -0.2% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.03B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.4% · Lending 15.8% · Dexs 13.9% · RWA 12.9% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.960% of chain TVL.

- BlackRock BUIDL (RWA): $887.01M
- xStocks (RWA): $428.94M
- OnRe (RWA): $288.64M
- Solstice (Basis Trading): $249.83M
- Ondo Yield Assets (RWA): $179.82M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **923.0 unique fee payers** signed per block (1,348 distinct addresses in the union, 51.3% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) - Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT

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

### Change over 24h (vs run at 2026-09-01T15:39:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,606.13 | 3,963.51 | -13.95% |
| Average non-vote TPS | 2,498.79 | 1,822.14 | -27.08% |
| Average slot time (ms) | 320.60 | 314.80 | -1.81% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 15.00 | 18.00 | +20.00% |
| Solana TVL | 5,787,343,823.00 | 5,622,784,841.00 | -2.84% |
| SOL price | 102.04 | 98.97 | -3.01% |
| Stablecoin supply | 15,969,865,893.00 | 15,849,987,390.00 | -0.75% |
| 24h DEX volume | 2,501,465,620.05 | 2,171,560,050.49 | -13.19% |
| 24h chain fees | 13,500,453.08 | 12,641,815.67 | -6.36% |

### Change over 7d (vs run at 2026-08-26T12:23:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,489.57 | 3,963.51 | +13.58% |
| Average non-vote TPS | 1,624.74 | 1,822.14 | +12.15% |
| Average slot time (ms) | 365.20 | 314.80 | -13.80% |
| Active validators | 684.00 | 677.00 | -1.02% |
| Delinquent validators | 11.00 | 18.00 | +63.64% |
| Solana TVL | 5,596,733,884.00 | 5,622,784,841.00 | +0.47% |
| SOL price | 97.02 | 98.97 | +2.01% |
| Stablecoin supply | 16,315,003,426.00 | 15,849,987,390.00 | -2.85% |
| 24h DEX volume | 2,934,986,439.19 | 2,171,560,050.49 | -26.01% |
| 24h chain fees | 13,134,401.04 | 12,641,815.67 | -3.75% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,963.51 | +0.74% |
| Average non-vote TPS | 2,312.46 | 1,822.14 | -21.20% |
| Average slot time (ms) | 424.10 | 314.80 | -25.77% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,622,784,841.00 | +18.62% |
| SOL price | 72.81 | 98.97 | +35.93% |
| Stablecoin supply | 16,197,749,831.00 | 15,849,987,390.00 | -2.15% |
| 24h DEX volume | 1,636,927,091.91 | 2,171,560,050.49 | +32.66% |
| 24h chain fees | 7,777,648.77 | 12,641,815.67 | +62.54% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
