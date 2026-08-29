# Solana Ecosystem Pulse

**Generated:** 2026-08-29T01:13:54Z · **Schema:** `1.0.0` · **Collection time:** 22.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.93 | -4.75% |
| Market cap | $60.72B | rank #7 |
| Total value locked | $5.83B | -0.00% |
| Stablecoin supply | $16.38B | +0.53% |
| DEX volume (24h) | $2.61B | -29.35% |
| Chain fees / REV (24h) | $16.41M | +0.67% |
| Non-vote TPS (1h avg) | 1,808 | peak 4,984 total |
| Active validators | 687 | 10 delinquent |
| Epoch 1024 | 25.66% complete | 321,142 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 62 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 317.40 sits 8.2 sigma below the median of the last 62 runs (414.35, -23.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,808.2 average over the last 60 minutes; 1,770.2 in the latest sample.
- **Total TPS:** 3,960.8 average, 4,984.3 peak. Consensus votes account for 54.3% of all transactions.
- **Slot time:** 317.4 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 420,526,812 at absolute slot 442,478,858.
- **Epoch 1024:** slot 110,858 of 432,000 (25.66% complete).
- **Client:** agave `4.2.1`, feature set `565236538`. Inflation 3.674% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 259 ms |
| `solana-rpc.publicnode.com` | yes | 128 ms |
| `api.mainnet.solana.com` | yes | 237 ms |

## Validators & stake

- **687 active** validators, **10 delinquent** (1.43% by count, 0.009% by stake).
- **Total stake:** 436,134,289 SOL ($45.33B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.15% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 13.04%; 249 validators at 0% and 68 at 100%.

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

- **SOL:** $103.93 (-4.75% 24h, +10.74% 7d, +41.97% 30d). Market cap $60.72B, 24h volume $5.73B (9.44% of cap). Price source: `coingecko`.
- **TVL:** $5.83B across 336 protocols - rank #2 of 465 chains, 6.66% of all tracked chain TVL. +5.06% over 7d, -55.9% from its ATH.
- **Stablecoins:** $16.38B circulating on Solana (-0.82% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.61B in 24h, $20.95B over 7d across 119 venues. Volume/TVL turnover 0.448x per day.
- **REV (chain fees):** $16.41M in 24h, $299.44M over 30d. Retained chain revenue $7.61M (46.4% of fees). Annualised fees are 9.86% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 584,161,966 SOL circulating of 633,079,506 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | -5.1% | +13.2% |
| 2 | Kamino Lend | Lending | $1.23B | -2.3% | +3.6% |
| 3 | Raydium AMM | Dexs | $1.12B | -4.9% | +7.1% |
| 4 | Jupiter Lend | Lending | $1.09B | -2.9% | +4.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.07B | -4.8% | +13.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | -4.9% | +11.1% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +14.1% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $768.34M | -3.5% | +2.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $540.48M | -4.9% | +10.5% |
| 10 | xStocks | RWA | $432.09M | -2.2% | +1.4% |
| 11 | Marinade Native | Staking Pool | $425.22M | -4.8% | +43.8% |
| 12 | Sentora | Risk Curators | $361.02M | -0.1% | -1.3% |

The top five protocols hold 36.6% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.67B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.2% · Lending 15.6% · Dexs 14.1% · RWA 12.4% · Derivatives 5.2% · Staking Pool 3.9%

### Tokenised assets

$2.40B of tokenised real-world assets and equities are locked on Solana - 14.405% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $432.09M
- OnRe (RWA): $284.53M
- Solstice (Basis Trading): $249.89M
- Ondo Yield Assets (RWA): $179.94M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **894.0 unique fee payers** signed per block (1,259 distinct addresses in the union, 53.1% overlap between blocks).

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

- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-08-28
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

### Change over 24h (vs run at 2026-08-28T01:49:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,982.31 | 3,960.85 | -0.54% |
| Average non-vote TPS | 2,110.38 | 1,808.22 | -14.32% |
| Average slot time (ms) | 366.40 | 317.40 | -13.37% |
| Active validators | 688.00 | 687.00 | -0.15% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 6,008,382,169.00 | 5,832,657,009.00 | -2.92% |
| SOL price | 108.38 | 103.93 | -4.11% |
| Stablecoin supply | 16,295,366,838.00 | 16,381,381,392.00 | +0.53% |
| 24h DEX volume | 3,635,966,596.54 | 2,613,991,447.22 | -28.11% |
| 24h chain fees | 14,757,082.36 | 16,411,287.12 | +11.21% |

### Change over 7d (vs run at 2026-08-22T00:30:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,306.07 | 3,960.85 | -8.02% |
| Average non-vote TPS | 2,452.33 | 1,808.22 | -26.27% |
| Average slot time (ms) | 365.30 | 317.40 | -13.11% |
| Active validators | 682.00 | 687.00 | +0.73% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,519,461,055.00 | 5,832,657,009.00 | +5.67% |
| SOL price | 94.02 | 103.93 | +10.54% |
| Stablecoin supply | 16,517,448,442.00 | 16,381,381,392.00 | -0.82% |
| 24h DEX volume | 2,961,868,880.89 | 2,613,991,447.22 | -11.75% |
| 24h chain fees | 10,823,009.54 | 16,411,287.12 | +51.63% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,960.85 | +0.67% |
| Average non-vote TPS | 2,312.46 | 1,808.22 | -21.81% |
| Average slot time (ms) | 424.10 | 317.40 | -25.16% |
| Active validators | 692.00 | 687.00 | -0.72% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 5,832,657,009.00 | +23.05% |
| SOL price | 72.81 | 103.93 | +42.74% |
| Stablecoin supply | 16,197,749,831.00 | 16,381,381,392.00 | +1.13% |
| 24h DEX volume | 1,636,927,091.91 | 2,613,991,447.22 | +59.69% |
| 24h chain fees | 7,777,648.77 | 16,411,287.12 | +111.01% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
