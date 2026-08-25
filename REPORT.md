# Solana Ecosystem Pulse

**Generated:** 2026-08-25T06:23:22Z · **Schema:** `1.0.0` · **Collection time:** 10.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.78 | +8.05% |
| Market cap | $59.38B | rank #7 |
| Total value locked | $5.79B | +4.16% |
| Stablecoin supply | $16.43B | -0.17% |
| DEX volume (24h) | $2.99B | +1.68% |
| Chain fees / REV (24h) | $14.09M | +11.32% |
| Non-vote TPS (1h avg) | 1,410 | peak 3,826 total |
| Active validators | 685 | 9 delinquent |
| Epoch 1022 | 15.38% complete | 365,580 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 62 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 364.70 sits 17.2 sigma below the median of the last 62 runs (415.75, -12.3%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,791,641,446.00 sits 13.4 sigma above the median of the last 62 runs (4,848,408,872.50, +19.5%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 101.78 sits 17.2 sigma above the median of the last 62 runs (76.23, +33.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (up 8.1% in 24h) | SOL price changed +8.1% over the last day, past the 8% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,410.4 average over the last 60 minutes; 1,186.6 in the latest sample.
- **Total TPS:** 3,277.7 average, 3,825.6 peak. Consensus votes account for 57.0% of all transactions.
- **Slot time:** 364.7 ms average (target 400 ms), worst 1-minute bucket 377.4 ms.
- **Block height:** 419,619,217 at absolute slot 441,570,420.
- **Epoch 1022:** slot 66,420 of 432,000 (15.38% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 100 ms |
| `solana-rpc.publicnode.com` | yes | 54 ms |
| `api.mainnet.solana.com` | yes | 113 ms |

## Validators & stake

- **685 active** validators, **9 delinquent** (1.30% by count, 0.023% by stake).
- **Total stake:** 435,118,104 SOL ($44.29B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 11.91%; 256 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.923% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.686% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.820% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.699% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.115% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.052% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.972% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.828% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.678% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.511% | 0% |

## Economics

- **SOL:** $101.78 (+8.05% 24h, +34.53% 7d, +35.73% 30d). Market cap $59.38B, 24h volume $7.23B (12.18% of cap). Price source: `coingecko`.
- **TVL:** $5.79B across 331 protocols - rank #2 of 465 chains, 6.51% of all tracked chain TVL. +19.42% over 7d, -56.2% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+2.80% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.99B in 24h, $20.49B over 7d across 119 venues. Volume/TVL turnover 0.516x per day.
- **REV (chain fees):** $14.09M in 24h, $282.12M over 30d. Retained chain revenue $5.67M (40.3% of fees). Annualised fees are 8.66% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,376,249 SOL circulating of 632,860,110 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | +8.9% | +34.7% |
| 2 | Kamino Lend | Lending | $1.23B | +4.1% | +16.0% |
| 3 | Raydium AMM | Dexs | $1.11B | +6.6% | +31.2% |
| 4 | Jupiter Lend | Lending | $1.10B | +4.4% | +17.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | +8.2% | +33.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.02B | +7.7% | +33.9% |
| 7 | BlackRock BUIDL | RWA | $828.75M | +6.6% | +11.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $775.95M | +5.0% | +13.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $524.86M | +7.8% | +33.3% |
| 10 | xStocks | RWA | $425.52M | +1.9% | +9.3% |
| 11 | Solstice | Basis Trading | $402.94M | -0.3% | -20.4% |
| 12 | Marinade Native | Staking Pool | $384.56M | +15.2% | +78.6% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.34B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.0% · Lending 15.9% · Dexs 14.0% · RWA 12.3% · Derivatives 5.3% · Staking Pool 3.7%

### Tokenised assets

$2.49B of tokenised real-world assets and equities are locked on Solana - 15.234% of chain TVL.

- BlackRock BUIDL (RWA): $828.75M
- xStocks (RWA): $425.52M
- Solstice (Basis Trading): $402.94M
- OnRe (RWA): $276.22M
- Ondo Yield Assets (RWA): $178.68M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **869.0 unique fee payers** signed per block (1,164 distinct addresses in the union, 55.4% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-24
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-24
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-24
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-24
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [Remove inactive stakes from the stakes cache](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-22
- [SIMD-0504: simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20

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

### Change over 24h (vs run at 2026-08-24T06:32:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,404.07 | 3,277.72 | -3.71% |
| Average non-vote TPS | 1,533.89 | 1,410.38 | -8.05% |
| Average slot time (ms) | 364.50 | 364.70 | +0.05% |
| Active validators | 684.00 | 685.00 | +0.15% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 5,534,492,880.00 | 5,791,641,446.00 | +4.65% |
| SOL price | 94.29 | 101.78 | +7.94% |
| Stablecoin supply | 16,453,046,975.00 | 16,425,378,976.00 | -0.17% |
| 24h DEX volume | 3,119,842,862.16 | 2,987,931,793.43 | -4.23% |
| 24h chain fees | 12,447,100.70 | 14,086,550.72 | +13.17% |

### Change over 7d (vs run at 2026-08-18T06:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,904.51 | 3,277.72 | +12.85% |
| Average non-vote TPS | 1,251.49 | 1,410.38 | +12.70% |
| Average slot time (ms) | 417.00 | 364.70 | -12.54% |
| Active validators | 689.00 | 685.00 | -0.58% |
| Delinquent validators | 6.00 | 9.00 | +50.00% |
| Solana TVL | 4,846,663,986.00 | 5,791,641,446.00 | +19.50% |
| SOL price | 75.81 | 101.78 | +34.26% |
| Stablecoin supply | 15,980,255,447.00 | 16,425,378,976.00 | +2.79% |
| 24h DEX volume | 1,425,243,228.36 | 2,987,931,793.43 | +109.64% |
| 24h chain fees | 10,772,677.30 | 14,086,550.72 | +30.76% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,277.72 | -16.69% |
| Average non-vote TPS | 2,312.46 | 1,410.38 | -39.01% |
| Average slot time (ms) | 424.10 | 364.70 | -14.01% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 4,740,035,266.00 | 5,791,641,446.00 | +22.19% |
| SOL price | 72.81 | 101.78 | +39.79% |
| Stablecoin supply | 16,197,749,831.00 | 16,425,378,976.00 | +1.41% |
| 24h DEX volume | 1,636,927,091.91 | 2,987,931,793.43 | +82.53% |
| 24h chain fees | 7,777,648.77 | 14,086,550.72 | +81.12% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 10.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
