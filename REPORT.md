# Solana Ecosystem Pulse

**Generated:** 2026-08-30T02:00:05Z · **Schema:** `1.0.0` · **Collection time:** 23.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $105.15 | +0.97% |
| Market cap | $61.51B | rank #7 |
| Total value locked | $5.91B | +0.41% |
| Stablecoin supply | $16.35B | -0.22% |
| DEX volume (24h) | $1.81B | -30.01% |
| Chain fees / REV (24h) | $11.72M | -25.48% |
| Non-vote TPS (1h avg) | 1,702 | peak 4,484 total |
| Active validators | 686 | 11 delinquent |
| Epoch 1024 | 90.78% complete | 39,829 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 62 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 317.60 sits 5.3 sigma below the median of the last 62 runs (413.35, -23.2%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,702.2 average over the last 60 minutes; 2,042.3 in the latest sample.
- **Total TPS:** 3,858.1 average, 4,483.7 peak. Consensus votes account for 55.9% of all transactions.
- **Slot time:** 317.6 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 420,807,970 at absolute slot 442,760,171.
- **Epoch 1024:** slot 392,171 of 432,000 (90.78% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.674% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 654 ms |
| `solana-rpc.publicnode.com` | yes | 160 ms |
| `api.mainnet.solana.com` | yes | 157 ms |

## Validators & stake

- **686 active** validators, **11 delinquent** (1.58% by count, 0.009% by stake).
- **Total stake:** 436,134,289 SOL ($45.86B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.15% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 13.21%; 247 validators at 0% and 69 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,991,835 | 3.896% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,737 | 3.677% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,393,242 | 2.842% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,460,007 | 2.628% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,292,131 | 2.131% | 7% |
| 6 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,081,213 | 2.082% | 0% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,001,204 | 2.064% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,294,487 | 1.673% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,192,557 | 1.649% | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,585,996 | 1.510% | 0% |

## Economics

- **SOL:** $105.15 (+0.97% 24h, +9.17% 7d, +41.27% 30d). Market cap $61.51B, 24h volume $2.24B (3.64% of cap). Price source: `coingecko`.
- **TVL:** $5.91B across 338 protocols - rank #2 of 465 chains, 6.70% of all tracked chain TVL. +6.33% over 7d, -55.4% from its ATH.
- **Stablecoins:** $16.35B circulating on Solana (-0.48% 7d) - $2.77 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.81B in 24h, $19.03B over 7d across 120 venues. Volume/TVL turnover 0.307x per day.
- **REV (chain fees):** $11.72M in 24h, $312.83M over 30d. Retained chain revenue $5.37M (45.8% of fees). Annualised fees are 6.96% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,036,057 SOL circulating of 633,078,597 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.61B | +1.0% | +14.1% |
| 2 | Kamino Lend | Lending | $1.26B | +0.3% | +6.2% |
| 3 | Raydium AMM | Dexs | $1.14B | +1.3% | +7.5% |
| 4 | Jupiter Lend | Lending | $1.10B | +0.9% | +3.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | +1.3% | +15.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | +1.3% | +9.8% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $773.76M | +0.6% | +5.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $547.30M | +1.5% | +13.1% |
| 10 | xStocks | RWA | $434.42M | +0.4% | +3.4% |
| 11 | Marinade Native | Staking Pool | $430.34M | +1.2% | +36.3% |
| 12 | Sentora | Risk Curators | $361.03M | -0.0% | -1.3% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.84B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.3% · Lending 15.7% · Dexs 14.1% · RWA 12.3% · Derivatives 5.1% · Staking Pool 3.9%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.272% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $434.42M
- OnRe (RWA): $284.73M
- Solstice (Basis Trading): $249.92M
- Ondo Yield Assets (RWA): $179.56M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **670.7 unique fee payers** signed per block (1,175 distinct addresses in the union, 41.6% overlap between blocks).

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
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-29
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-27
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
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

### Change over 24h (vs run at 2026-08-29T01:13:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,960.85 | 3,858.12 | -2.59% |
| Average non-vote TPS | 1,808.22 | 1,702.15 | -5.87% |
| Average slot time (ms) | 317.40 | 317.60 | +0.06% |
| Active validators | 687.00 | 686.00 | -0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,832,657,009.00 | 5,910,477,808.00 | +1.33% |
| SOL price | 103.93 | 105.15 | +1.17% |
| Stablecoin supply | 16,381,381,392.00 | 16,345,475,515.00 | -0.22% |
| 24h DEX volume | 2,613,991,447.22 | 1,813,165,645.31 | -30.64% |
| 24h chain fees | 16,411,287.12 | 11,721,762.05 | -28.57% |

### Change over 7d (vs run at 2026-08-23T00:32:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,801.15 | 3,858.12 | +1.50% |
| Average non-vote TPS | 1,949.33 | 1,702.15 | -12.68% |
| Average slot time (ms) | 368.10 | 317.60 | -13.72% |
| Active validators | 687.00 | 686.00 | -0.15% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 5,520,748,480.00 | 5,910,477,808.00 | +7.06% |
| SOL price | 94.33 | 105.15 | +11.47% |
| Stablecoin supply | 16,423,898,783.00 | 16,345,475,515.00 | -0.48% |
| 24h DEX volume | 3,761,469,856.66 | 1,813,165,645.31 | -51.80% |
| 24h chain fees | 13,746,381.02 | 11,721,762.05 | -14.73% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,858.12 | -1.94% |
| Average non-vote TPS | 2,312.46 | 1,702.15 | -26.39% |
| Average slot time (ms) | 424.10 | 317.60 | -25.11% |
| Active validators | 692.00 | 686.00 | -0.87% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 4,740,035,266.00 | 5,910,477,808.00 | +24.69% |
| SOL price | 72.81 | 105.15 | +44.42% |
| Stablecoin supply | 16,197,749,831.00 | 16,345,475,515.00 | +0.91% |
| 24h DEX volume | 1,636,927,091.91 | 1,813,165,645.31 | +10.77% |
| 24h chain fees | 7,777,648.77 | 11,721,762.05 | +50.71% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 23.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
