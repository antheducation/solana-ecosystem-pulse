# Solana Ecosystem Pulse

**Generated:** 2026-08-25T00:31:55Z · **Schema:** `1.0.0` · **Collection time:** 19.6s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.62 | +5.45% |
| Market cap | $58.11B | rank #7 |
| Total value locked | $5.65B | +1.31% |
| Stablecoin supply | $16.45B | +0.50% |
| DEX volume (24h) | $3.00B | +2.25% |
| Chain fees / REV (24h) | $12.73M | +0.63% |
| Non-vote TPS (1h avg) | 2,344 | peak 4,933 total |
| Active validators | 686 | 8 delinquent |
| Epoch 1022 | 2.03% complete | 423,212 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 62 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.70 sits 16.6 sigma below the median of the last 62 runs (415.80, -11.8%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,650,096,546.00 sits 11.9 sigma above the median of the last 62 runs (4,848,408,872.50, +16.5%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 99.62 sits 16.5 sigma above the median of the last 62 runs (76.23, +30.7%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,343.7 average over the last 60 minutes; 2,851.8 in the latest sample.
- **Total TPS:** 4,191.7 average, 4,932.6 peak. Consensus votes account for 44.1% of all transactions.
- **Slot time:** 366.7 ms average (target 400 ms), worst 1-minute bucket 379.7 ms.
- **Block height:** 419,561,627 at absolute slot 441,512,788.
- **Epoch 1022:** slot 8,788 of 432,000 (2.03% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 212 ms |
| `solana-rpc.publicnode.com` | yes | 149 ms |
| `api.mainnet.solana.com` | yes | 152 ms |

## Validators & stake

- **686 active** validators, **8 delinquent** (1.15% by count, 0.017% by stake).
- **Total stake:** 435,118,104 SOL ($43.35B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 11.89%; 257 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.923% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.686% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.820% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.699% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.115% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.051% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.972% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.828% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.678% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.511% | 0% |

## Economics

- **SOL:** $99.62 (+5.45% 24h, +31.20% 7d, +33.77% 30d). Market cap $58.11B, 24h volume $6.17B (10.61% of cap). Price source: `coingecko`.
- **TVL:** $5.65B across 330 protocols - rank #2 of 465 chains, 6.44% of all tracked chain TVL. +17.86% over 7d, -57.5% from its ATH.
- **Stablecoins:** $16.45B circulating on Solana (+2.81% 7d) - $2.91 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.00B in 24h, $18.78B over 7d across 119 venues. Volume/TVL turnover 0.532x per day.
- **REV (chain fees):** $12.73M in 24h, $271.90M over 30d. Retained chain revenue $5.03M (39.5% of fees). Annualised fees are 8.00% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,376,742 SOL circulating of 632,860,329 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.47B | +3.1% | +31.7% |
| 2 | Kamino Lend | Lending | $1.20B | +1.0% | +16.3% |
| 3 | Jupiter Lend | Lending | $1.07B | +0.7% | +16.3% |
| 4 | Raydium AMM | Dexs | $1.05B | +0.3% | +26.0% |
| 5 | Binance Staked SOL | Liquid Staking | $990.30M | +2.8% | +30.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $976.49M | +2.2% | +31.0% |
| 7 | BlackRock BUIDL | RWA | $828.75M | +6.6% | +11.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $755.83M | +1.3% | +12.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $503.66M | +2.3% | +30.2% |
| 10 | xStocks | RWA | $422.00M | +0.2% | +10.1% |
| 11 | Solstice | Basis Trading | $402.94M | -0.3% | -20.4% |
| 12 | Sentora | Risk Curators | $363.63M | -0.6% | -1.0% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.87B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.6% · Lending 16.1% · Dexs 13.9% · RWA 12.6% · Derivatives 5.3% · Staking Pool 3.6%

### Tokenised assets

$2.49B of tokenised real-world assets and equities are locked on Solana - 15.654% of chain TVL.

- BlackRock BUIDL (RWA): $828.75M
- xStocks (RWA): $422.00M
- Solstice (Basis Trading): $402.94M
- OnRe (RWA): $276.11M
- Ondo Yield Assets (RWA): $178.58M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,051.3 unique fee payers** signed per block (1,584 distinct addresses in the union, 49.8% overlap between blocks).

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

### Change over 24h (vs run at 2026-08-24T00:32:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,028.12 | 4,191.70 | +4.06% |
| Average non-vote TPS | 2,170.90 | 2,343.72 | +7.96% |
| Average slot time (ms) | 365.40 | 366.70 | +0.36% |
| Active validators | 684.00 | 686.00 | +0.29% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,590,677,164.00 | 5,650,096,546.00 | +1.06% |
| SOL price | 94.47 | 99.62 | +5.45% |
| Stablecoin supply | 16,372,851,569.00 | 16,454,057,808.00 | +0.50% |
| 24h DEX volume | 3,407,472,979.70 | 3,004,603,140.25 | -11.82% |
| 24h chain fees | 11,680,746.95 | 12,733,845.33 | +9.02% |

### Change over 7d (vs run at 2026-08-18T00:30:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,442.13 | 4,191.70 | +21.78% |
| Average non-vote TPS | 1,788.32 | 2,343.72 | +31.06% |
| Average slot time (ms) | 414.30 | 366.70 | -11.49% |
| Active validators | 689.00 | 686.00 | -0.44% |
| Delinquent validators | 6.00 | 8.00 | +33.33% |
| Solana TVL | 4,848,739,935.00 | 5,650,096,546.00 | +16.53% |
| SOL price | 75.95 | 99.62 | +31.17% |
| Stablecoin supply | 16,003,691,443.00 | 16,454,057,808.00 | +2.81% |
| 24h DEX volume | 1,055,467,633.95 | 3,004,603,140.25 | +184.67% |
| 24h chain fees | 6,906,881.24 | 12,733,845.33 | +84.36% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,191.70 | +6.53% |
| Average non-vote TPS | 2,312.46 | 2,343.72 | +1.35% |
| Average slot time (ms) | 424.10 | 366.70 | -13.53% |
| Active validators | 692.00 | 686.00 | -0.87% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 4,740,035,266.00 | 5,650,096,546.00 | +19.20% |
| SOL price | 72.81 | 99.62 | +36.82% |
| Stablecoin supply | 16,197,749,831.00 | 16,454,057,808.00 | +1.58% |
| 24h DEX volume | 1,636,927,091.91 | 3,004,603,140.25 | +83.55% |
| 24h chain fees | 7,777,648.77 | 12,733,845.33 | +63.72% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 19.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
