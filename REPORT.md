# Solana Ecosystem Pulse

**Generated:** 2026-09-02T20:11:54Z · **Schema:** `1.0.0` · **Collection time:** 11.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.75 | -0.19% |
| Market cap | $58.39B | rank #7 |
| Total value locked | $5.67B | -5.27% |
| Stablecoin supply | $15.85B | -0.74% |
| DEX volume (24h) | $2.17B | -13.19% |
| Chain fees / REV (24h) | $12.65M | -5.93% |
| Non-vote TPS (1h avg) | 1,884 | peak 5,099 total |
| Active validators | 677 | 18 delinquent |
| Epoch 1027 | 28.00% complete | 311,020 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 65 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Active validators is below its recent norm | Current 677.00 sits 3.0 sigma below the median of the last 65 runs (686.00, -1.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,883.9 average over the last 60 minutes; 1,676.0 in the latest sample.
- **Total TPS:** 4,023.0 average, 5,099.1 peak. Consensus votes account for 53.2% of all transactions.
- **Slot time:** 314.5 ms average (target 400 ms), worst 1-minute bucket 322.6 ms.
- **Block height:** 421,832,324 at absolute slot 443,784,980.
- **Epoch 1027:** slot 120,980 of 432,000 (28.00% complete).
- **Client:** agave `4.3.0-beta.2`, feature set `2409014235`. Inflation 3.666% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 92 ms |
| `solana-rpc.publicnode.com` | yes | 164 ms |
| `api.mainnet.solana.com` | yes | 92 ms |

## Validators & stake

- **677 active** validators, **18 delinquent** (2.59% by count, 0.069% by stake).
- **Total stake:** 438,422,357 SOL ($43.73B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.26% and top 33 hold 45.71% of active stake.
- **Commission:** median 5.0%, mean 12.35%; 245 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,348,904 | 3.960% | 7% |
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

- **SOL:** $99.75 (-0.19% 24h, +3.08% 7d, +34.86% 30d). Market cap $58.39B, 24h volume $2.95B (5.04% of cap). Price source: `coingecko`.
- **TVL:** $5.67B across 341 protocols - rank #2 of 465 chains, 6.65% of all tracked chain TVL. +1.12% over 7d, -57.2% from its ATH.
- **Stablecoins:** $15.85B circulating on Solana (-1.86% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.17B in 24h, $16.92B over 7d across 120 venues. Volume/TVL turnover 0.383x per day.
- **REV (chain fees):** $12.65M in 24h, $332.77M over 30d. Retained chain revenue $5.79M (45.8% of fees). Annualised fees are 7.91% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,275,362 SOL circulating of 633,361,454 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.51B | -2.3% | +2.7% |
| 2 | Kamino Lend | Lending | $1.22B | -0.1% | +3.8% |
| 3 | Raydium AMM | Dexs | $1.07B | -3.0% | +0.6% |
| 4 | Jupiter Lend | Lending | $1.05B | -1.3% | +0.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.02B | -2.2% | +3.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $995.32M | -1.0% | +2.7% |
| 7 | BlackRock BUIDL | RWA | $887.09M | +0.0% | +1.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $738.21M | -0.7% | -1.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $510.85M | -2.5% | +2.0% |
| 10 | xStocks | RWA | $431.61M | +0.1% | +0.8% |
| 11 | Marinade Native | Staking Pool | $394.49M | -2.3% | +4.4% |
| 12 | Sentora | Risk Curators | $362.62M | +0.1% | -0.1% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.12B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.5% · Lending 15.8% · Dexs 14.0% · RWA 12.9% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.896% of chain TVL.

- BlackRock BUIDL (RWA): $887.09M
- xStocks (RWA): $431.61M
- OnRe (RWA): $288.65M
- Solstice (Basis Trading): $249.83M
- Ondo Yield Assets (RWA): $179.89M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **896.7 unique fee payers** signed per block (1,258 distinct addresses in the union, 53.2% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-01T20:13:48Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,409.25 | 4,022.99 | -8.76% |
| Average non-vote TPS | 2,288.53 | 1,883.92 | -17.68% |
| Average slot time (ms) | 317.90 | 314.50 | -1.07% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 17.00 | 18.00 | +5.88% |
| Solana TVL | 5,737,476,214.00 | 5,665,576,869.00 | -1.25% |
| SOL price | 99.96 | 99.75 | -0.21% |
| Stablecoin supply | 15,969,999,346.00 | 15,850,870,070.00 | -0.75% |
| 24h DEX volume | 2,501,465,620.05 | 2,171,560,050.49 | -13.19% |
| 24h chain fees | 13,501,461.08 | 12,646,787.67 | -6.33% |

### Change over 7d (vs run at 2026-08-26T19:30:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,472.91 | 4,022.99 | -10.06% |
| Average non-vote TPS | 2,616.46 | 1,883.92 | -28.00% |
| Average slot time (ms) | 366.20 | 314.50 | -14.12% |
| Active validators | 685.00 | 677.00 | -1.17% |
| Delinquent validators | 10.00 | 18.00 | +80.00% |
| Solana TVL | 5,557,854,195.00 | 5,665,576,869.00 | +1.94% |
| SOL price | 96.76 | 99.75 | +3.09% |
| Stablecoin supply | 16,315,958,333.00 | 15,850,870,070.00 | -2.85% |
| 24h DEX volume | 2,934,986,439.19 | 2,171,560,050.49 | -26.01% |
| 24h chain fees | 13,235,652.04 | 12,646,787.67 | -4.45% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,022.99 | +2.25% |
| Average non-vote TPS | 2,312.46 | 1,883.92 | -18.53% |
| Average slot time (ms) | 424.10 | 314.50 | -25.84% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 18.00 | +125.00% |
| Solana TVL | 4,740,035,266.00 | 5,665,576,869.00 | +19.53% |
| SOL price | 72.81 | 99.75 | +37.00% |
| Stablecoin supply | 16,197,749,831.00 | 15,850,870,070.00 | -2.14% |
| 24h DEX volume | 1,636,927,091.91 | 2,171,560,050.49 | +32.66% |
| 24h chain fees | 7,777,648.77 | 12,646,787.67 | +62.60% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 11.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
