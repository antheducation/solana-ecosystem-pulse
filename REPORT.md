# Solana Ecosystem Pulse

**Generated:** 2026-09-01T10:37:53Z · **Schema:** `1.0.0` · **Collection time:** 26.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.48 | -0.42% |
| Market cap | $59.98B | rank #7 |
| Total value locked | $5.81B | +0.36% |
| Stablecoin supply | $16.13B | +0.04% |
| DEX volume (24h) | $2.46B | +27.37% |
| Chain fees / REV (24h) | $13.29M | +7.97% |
| Non-vote TPS (1h avg) | 1,291 | peak 3,828 total |
| Active validators | 680 | 14 delinquent |
| Epoch 1026 | 39.50% complete | 261,376 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 14.00 sits 3.4 sigma above the median of the last 64 runs (9.00, +55.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,291.4 average over the last 60 minutes; 1,526.8 in the latest sample.
- **Total TPS:** 3,426.5 average, 3,827.5 peak. Consensus votes account for 62.3% of all transactions.
- **Slot time:** 316.8 ms average (target 400 ms), worst 1-minute bucket 333.3 ms.
- **Block height:** 421,450,210 at absolute slot 443,402,624.
- **Epoch 1026:** slot 170,624 of 432,000 (39.50% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.669% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 522 ms |
| `solana-rpc.publicnode.com` | yes | 165 ms |
| `api.mainnet.solana.com` | yes | 469 ms |

## Validators & stake

- **680 active** validators, **14 delinquent** (2.02% by count, 0.008% by stake).
- **Total stake:** 438,201,819 SOL ($44.91B); stake rate 69.20% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.17% and top 33 hold 45.59% of active stake.
- **Commission:** median 5.0%, mean 12.16%; 247 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,174,436 | 3.920% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,281,426 | 3.716% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,434,730 | 2.838% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,480,709 | 2.620% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,455,250 | 2.158% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,285,506 | 2.119% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,044,016 | 2.064% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,216,300 | 1.647% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,930,213 | 1.582% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,591,885 | 1.504% | 0% |

## Economics

- **SOL:** $102.48 (-0.42% 24h, +2.74% 7d, +39.77% 30d). Market cap $59.98B, 24h volume $3.02B (5.03% of cap). Price source: `coingecko`.
- **TVL:** $5.81B across 338 protocols - rank #2 of 465 chains, 6.63% of all tracked chain TVL. +1.24% over 7d, -56.1% from its ATH.
- **Stablecoins:** $16.13B circulating on Solana (-1.79% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.46B in 24h, $17.42B over 7d across 120 venues. Volume/TVL turnover 0.423x per day.
- **REV (chain fees):** $13.29M in 24h, $327.00M over 30d. Retained chain revenue $5.45M (41.0% of fees). Annualised fees are 8.09% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,206,930 SOL circulating of 633,267,359 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | -0.5% | +2.3% |
| 2 | Kamino Lend | Lending | $1.25B | -0.1% | +3.0% |
| 3 | Raydium AMM | Dexs | $1.12B | +0.7% | +0.9% |
| 4 | Jupiter Lend | Lending | $1.08B | +0.2% | -1.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -0.7% | +5.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -0.9% | +4.1% |
| 7 | BlackRock BUIDL | RWA | $886.92M | +0.0% | +7.0% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $757.11M | -0.3% | -0.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $527.98M | -0.6% | +3.7% |
| 10 | xStocks | RWA | $439.09M | +1.6% | +4.2% |
| 11 | Marinade Native | Staking Pool | $411.91M | -2.3% | +11.6% |
| 12 | Sentora | Risk Curators | $361.47M | +0.1% | -0.6% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.51B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.8% · Lending 15.8% · Dexs 14.1% · RWA 12.6% · Derivatives 5.1% · Staking Pool 3.8%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.586% of chain TVL.

- BlackRock BUIDL (RWA): $886.92M
- xStocks (RWA): $439.09M
- OnRe (RWA): $287.71M
- Solstice (Basis Trading): $249.86M
- Ondo Yield Assets (RWA): $179.96M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **853.7 unique fee payers** signed per block (1,214 distinct addresses in the union, 52.6% overlap between blocks).

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

- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-31
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-31
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-31
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

### Change over 24h (vs run at 2026-08-31T11:58:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,455.79 | 3,426.48 | -0.85% |
| Average non-vote TPS | 1,317.61 | 1,291.44 | -1.99% |
| Average slot time (ms) | 316.10 | 316.80 | +0.22% |
| Active validators | 678.00 | 680.00 | +0.29% |
| Delinquent validators | 19.00 | 14.00 | -26.32% |
| Solana TVL | 5,818,482,572.00 | 5,808,427,098.00 | -0.17% |
| SOL price | 103.35 | 102.48 | -0.84% |
| Stablecoin supply | 16,121,972,675.00 | 16,130,106,220.00 | +0.05% |
| 24h DEX volume | 1,929,632,644.74 | 2,457,757,824.05 | +27.37% |
| 24h chain fees | 12,193,230.44 | 13,288,721.08 | +8.98% |

### Change over 7d (vs run at 2026-08-25T12:21:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,629.28 | 3,426.48 | -5.59% |
| Average non-vote TPS | 1,760.33 | 1,291.44 | -26.64% |
| Average slot time (ms) | 364.50 | 316.80 | -13.09% |
| Active validators | 685.00 | 680.00 | -0.73% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 5,744,421,267.00 | 5,808,427,098.00 | +1.11% |
| SOL price | 98.21 | 102.48 | +4.35% |
| Stablecoin supply | 16,426,518,373.00 | 16,130,106,220.00 | -1.80% |
| 24h DEX volume | 2,996,141,158.64 | 2,457,757,824.05 | -17.97% |
| 24h chain fees | 14,392,606.16 | 13,288,721.08 | -7.67% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,426.48 | -12.91% |
| Average non-vote TPS | 2,312.46 | 1,291.44 | -44.15% |
| Average slot time (ms) | 424.10 | 316.80 | -25.30% |
| Active validators | 692.00 | 680.00 | -1.73% |
| Delinquent validators | 8.00 | 14.00 | +75.00% |
| Solana TVL | 4,740,035,266.00 | 5,808,427,098.00 | +22.54% |
| SOL price | 72.81 | 102.48 | +40.75% |
| Stablecoin supply | 16,197,749,831.00 | 16,130,106,220.00 | -0.42% |
| 24h DEX volume | 1,636,927,091.91 | 2,457,757,824.05 | +50.14% |
| 24h chain fees | 7,777,648.77 | 13,288,721.08 | +70.86% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 26.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
