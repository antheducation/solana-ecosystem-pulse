# Solana Ecosystem Pulse

**Generated:** 2026-09-03T01:45:20Z · **Schema:** `1.0.0` · **Collection time:** 18.1s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.36 | +1.25% |
| Market cap | $58.73B | rank #7 |
| Total value locked | $5.69B | +0.44% |
| Stablecoin supply | $15.85B | -0.73% |
| DEX volume (24h) | $2.33B | +7.20% |
| Chain fees / REV (24h) | $12.13M | -4.11% |
| Non-vote TPS (1h avg) | 1,512 | peak 4,230 total |
| Active validators | 677 | 18 delinquent |
| Epoch 1027 | 42.72% complete | 247,450 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 65 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 677.00 sits 3.0 sigma below the median of the last 65 runs (686.00, -1.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,511.6 average over the last 60 minutes; 1,269.2 in the latest sample.
- **Total TPS:** 3,661.0 average, 4,229.7 peak. Consensus votes account for 58.7% of all transactions.
- **Slot time:** 313.5 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 421,895,803 at absolute slot 443,848,550.
- **Epoch 1027:** slot 184,550 of 432,000 (42.72% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 299 ms |
| `solana-rpc.publicnode.com` | yes | 144 ms |
| `api.mainnet.solana.com` | yes | 199 ms |

## Validators & stake

- **677 active** validators, **18 delinquent** (2.59% by count, 0.046% by stake).
- **Total stake:** 438,422,357 SOL ($44.00B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.25% and top 33 hold 45.70% of active stake.
- **Commission:** median 5.0%, mean 12.35%; 245 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.959% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,325,737 | 3.725% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,462,274 | 2.844% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,304,498 | 2.580% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,565,273 | 2.183% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,486 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,040,435 | 2.063% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,220,140 | 1.648% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,125,475 | 1.626% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,590,653 | 1.504% | 0% |

## Economics

- **SOL:** $100.36 (+1.25% 24h, -0.38% 7d, +37.47% 30d). Market cap $58.73B, 24h volume $2.95B (5.02% of cap). Price source: `coingecko`.
- **TVL:** $5.69B across 341 protocols - rank #2 of 465 chains, 6.70% of all tracked chain TVL. -1.38% over 7d, -57.0% from its ATH.
- **Stablecoins:** $15.85B circulating on Solana (-1.86% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.33B in 24h, $16.71B over 7d across 120 venues. Volume/TVL turnover 0.409x per day.
- **REV (chain fees):** $12.13M in 24h, $327.13M over 30d. Retained chain revenue $5.52M (45.5% of fees). Annualised fees are 7.54% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,275,223 SOL circulating of 633,361,254 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.52B | -0.4% | -0.8% |
| 2 | Kamino Lend | Lending | $1.23B | +2.1% | +2.0% |
| 3 | Raydium AMM | Dexs | $1.08B | +0.0% | -2.3% |
| 4 | Jupiter Lend | Lending | $1.07B | +2.5% | -2.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | +0.1% | +0.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.01B | +0.3% | -0.7% |
| 7 | BlackRock BUIDL | RWA | $890.69M | +0.4% | +0.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $743.07M | +0.0% | -3.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $516.62M | +0.1% | -1.4% |
| 10 | xStocks | RWA | $434.54M | +0.5% | +1.0% |
| 11 | Marinade Native | Staking Pool | $398.89M | +0.2% | -0.6% |
| 12 | Sentora | Risk Curators | $363.45M | +0.2% | +0.1% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.24B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 15.8% · Dexs 13.9% · RWA 12.8% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.832% of chain TVL.

- BlackRock BUIDL (RWA): $890.69M
- xStocks (RWA): $434.54M
- OnRe (RWA): $288.74M
- Solstice (Basis Trading): $249.83M
- Ondo Yield Assets (RWA): $179.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **875.0 unique fee payers** signed per block (1,203 distinct addresses in the union, 54.2% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-02T01:39:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,115.59 | 3,660.97 | -11.05% |
| Average non-vote TPS | 1,979.08 | 1,511.60 | -23.62% |
| Average slot time (ms) | 316.20 | 313.50 | -0.85% |
| Active validators | 678.00 | 677.00 | -0.15% |
| Delinquent validators | 16.00 | 18.00 | +12.50% |
| Solana TVL | 5,658,999,019.00 | 5,694,231,301.00 | +0.62% |
| SOL price | 99.33 | 100.36 | +1.04% |
| Stablecoin supply | 15,968,502,758.00 | 15,851,692,526.00 | -0.73% |
| 24h DEX volume | 2,358,272,391.49 | 2,328,007,156.32 | -1.28% |
| 24h chain fees | 14,355,983.93 | 12,127,495.07 | -15.52% |

### Change over 7d (vs run at 2026-08-27T05:23:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,396.37 | 3,660.97 | +7.79% |
| Average non-vote TPS | 1,521.66 | 1,511.60 | -0.66% |
| Average slot time (ms) | 364.30 | 313.50 | -13.94% |
| Active validators | 686.00 | 677.00 | -1.31% |
| Delinquent validators | 11.00 | 18.00 | +63.64% |
| Solana TVL | 5,770,223,599.00 | 5,694,231,301.00 | -1.32% |
| SOL price | 100.92 | 100.36 | -0.55% |
| Stablecoin supply | 16,290,346,473.00 | 15,851,692,526.00 | -2.69% |
| 24h DEX volume | 2,481,205,722.00 | 2,328,007,156.32 | -6.17% |
| 24h chain fees | 14,682,184.01 | 12,127,495.07 | -17.40% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,660.97 | -6.95% |
| Average non-vote TPS | 2,312.46 | 1,511.60 | -34.63% |
| Average slot time (ms) | 424.10 | 313.50 | -26.08% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,694,231,301.00 | +20.13% |
| SOL price | 72.81 | 100.36 | +37.84% |
| Stablecoin supply | 16,197,749,831.00 | 15,851,692,526.00 | -2.14% |
| 24h DEX volume | 1,636,927,091.91 | 2,328,007,156.32 | +42.22% |
| 24h chain fees | 7,777,648.77 | 12,127,495.07 | +55.93% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
