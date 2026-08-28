# Solana Ecosystem Pulse

**Generated:** 2026-08-28T01:49:59Z · **Schema:** `1.0.0` · **Collection time:** 15.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $108.38 | +6.68% |
| Market cap | $63.26B | rank #7 |
| Total value locked | $6.01B | +0.03% |
| Stablecoin supply | $16.30B | -0.12% |
| DEX volume (24h) | $3.64B | +54.61% |
| Chain fees / REV (24h) | $14.76M | -2.97% |
| Non-vote TPS (1h avg) | 2,110 | peak 4,646 total |
| Active validators | 688 | 10 delinquent |
| Epoch 1023 | 69.05% complete | 133,685 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.40 sits 14.9 sigma below the median of the last 63 runs (415.10, -11.7%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 108.38 sits 5.3 sigma above the median of the last 63 runs (77.39, +40.0%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 54.6% in 24h) | DEX volume changed +54.6% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,008,382,169.00 sits 4.2 sigma above the median of the last 63 runs (4,914,919,992.00, +22.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,110.4 average over the last 60 minutes; 1,737.7 in the latest sample.
- **Total TPS:** 3,982.3 average, 4,645.8 peak. Consensus votes account for 47.0% of all transactions.
- **Slot time:** 366.4 ms average (target 400 ms), worst 1-minute bucket 387.1 ms.
- **Block height:** 420,282,490 at absolute slot 442,234,315.
- **Epoch 1023:** slot 298,315 of 432,000 (69.05% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.677% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 124 ms |
| `solana-rpc.publicnode.com` | yes | 218 ms |
| `api.mainnet.solana.com` | yes | 126 ms |

## Validators & stake

- **688 active** validators, **10 delinquent** (1.43% by count, 0.062% by stake).
- **Total stake:** 436,884,837 SOL ($47.35B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 13.17%; 248 validators at 0% and 69 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,062,869 | 3.908% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,029,433 | 3.671% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,314,379 | 2.820% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,751,683 | 2.692% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,216,852 | 2.111% | 7% |
| 6 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,051,084 | 2.073% | 0% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,904,595 | 2.039% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,849,682 | 1.798% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,301,740 | 1.672% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,578,261 | 1.507% | 0% |

## Economics

- **SOL:** $108.38 (+6.68% 24h, +22.90% 7d, +47.03% 30d). Market cap $63.26B, 24h volume $7.07B (11.17% of cap). Price source: `coingecko`.
- **TVL:** $6.01B across 335 protocols - rank #2 of 465 chains, 6.73% of all tracked chain TVL. +13.04% over 7d, -54.5% from its ATH.
- **Stablecoins:** $16.30B circulating on Solana (-0.19% 7d) - $2.71 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.64B in 24h, $21.90B over 7d across 119 venues. Volume/TVL turnover 0.605x per day.
- **REV (chain fees):** $14.76M in 24h, $292.97M over 30d. Retained chain revenue $6.54M (44.3% of fees). Annualised fees are 8.51% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 584,062,190 SOL circulating of 632,969,000 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.67B | +9.2% | +27.7% |
| 2 | Kamino Lend | Lending | $1.25B | +3.8% | +9.9% |
| 3 | Raydium AMM | Dexs | $1.18B | +6.7% | +20.0% |
| 4 | Jupiter Lend | Lending | $1.13B | +2.9% | +10.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.13B | +9.1% | +26.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.10B | +8.6% | +24.8% |
| 7 | BlackRock BUIDL | RWA | $886.45M | +0.0% | +19.7% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $795.93M | +3.8% | +9.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $568.32M | +8.5% | +24.0% |
| 10 | Marinade Native | Staking Pool | $446.59M | +11.3% | +74.3% |
| 11 | xStocks | RWA | $441.65M | +2.7% | +7.7% |
| 12 | PumpSwap | Dexs | $370.66M | +12.2% | +25.2% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 335 protocols the total is $17.32B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.7% · Lending 15.4% · Dexs 14.1% · RWA 12.0% · Derivatives 5.1% · Staking Pool 4.0%

### Tokenised assets

$2.46B of tokenised real-world assets and equities are locked on Solana - 14.229% of chain TVL.

- BlackRock BUIDL (RWA): $886.45M
- xStocks (RWA): $441.65M
- Solstice (Basis Trading): $303.00M
- OnRe (RWA): $283.44M
- Ondo Yield Assets (RWA): $179.18M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **945.3 unique fee payers** signed per block (1,361 distinct addresses in the union, 52.0% overlap between blocks).

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
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-27T05:23:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,396.37 | 3,982.31 | +17.25% |
| Average non-vote TPS | 1,521.66 | 2,110.38 | +38.69% |
| Average slot time (ms) | 364.30 | 366.40 | +0.58% |
| Active validators | 686.00 | 688.00 | +0.29% |
| Delinquent validators | 11.00 | 10.00 | -9.09% |
| Solana TVL | 5,770,223,599.00 | 6,008,382,169.00 | +4.13% |
| SOL price | 100.92 | 108.38 | +7.39% |
| Stablecoin supply | 16,290,346,473.00 | 16,295,366,838.00 | +0.03% |
| 24h DEX volume | 2,481,205,722.00 | 3,635,966,596.54 | +46.54% |
| 24h chain fees | 14,682,184.01 | 14,757,082.36 | +0.51% |

### Change over 7d (vs run at 2026-08-21T00:33:25Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,319.13 | 3,982.31 | -7.80% |
| Average non-vote TPS | 2,669.71 | 2,110.38 | -20.95% |
| Average slot time (ms) | 415.80 | 366.40 | -11.88% |
| Active validators | 690.00 | 688.00 | -0.29% |
| Delinquent validators | 6.00 | 10.00 | +66.67% |
| Solana TVL | 5,285,370,682.00 | 6,008,382,169.00 | +13.68% |
| SOL price | 88.31 | 108.38 | +22.73% |
| Stablecoin supply | 16,326,513,472.00 | 16,295,366,838.00 | -0.19% |
| 24h DEX volume | 3,150,837,936.95 | 3,635,966,596.54 | +15.40% |
| 24h chain fees | 13,758,063.85 | 14,757,082.36 | +7.26% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,982.31 | +1.21% |
| Average non-vote TPS | 2,312.46 | 2,110.38 | -8.74% |
| Average slot time (ms) | 424.10 | 366.40 | -13.61% |
| Active validators | 692.00 | 688.00 | -0.58% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 6,008,382,169.00 | +26.76% |
| SOL price | 72.81 | 108.38 | +48.85% |
| Stablecoin supply | 16,197,749,831.00 | 16,295,366,838.00 | +0.60% |
| 24h DEX volume | 1,636,927,091.91 | 3,635,966,596.54 | +122.12% |
| 24h chain fees | 7,777,648.77 | 14,757,082.36 | +89.74% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
