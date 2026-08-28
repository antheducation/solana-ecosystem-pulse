# Solana Ecosystem Pulse

**Generated:** 2026-08-28T17:47:22Z · **Schema:** `1.0.0` · **Collection time:** 18.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.55 | -3.04% |
| Market cap | $61.06B | rank #7 |
| Total value locked | $5.90B | +2.10% |
| Stablecoin supply | $16.38B | +0.52% |
| DEX volume (24h) | $3.70B | +57.34% |
| Chain fees / REV (24h) | $16.30M | +7.19% |
| Non-vote TPS (1h avg) | 3,012 | peak 6,204 total |
| Active validators | 688 | 9 delinquent |
| Epoch 1024 | 6.14% complete | 405,454 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 63 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 321.30 sits 8.9 sigma below the median of the last 63 runs (414.50, -22.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 57.3% in 24h) | DEX volume changed +57.3% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 3,011.7 average over the last 60 minutes; 2,616.2 in the latest sample.
- **Total TPS:** 5,145.5 average, 6,203.8 peak. Consensus votes account for 41.5% of all transactions.
- **Slot time:** 321.3 ms average (target 400 ms), worst 1-minute bucket 333.3 ms.
- **Block height:** 420,442,672 at absolute slot 442,394,546.
- **Epoch 1024:** slot 26,546 of 432,000 (6.14% complete).
- **Client:** agave `4.3.0-beta.2`, feature set `2409014235`. Inflation 3.674% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 161 ms |
| `solana-rpc.publicnode.com` | yes | 195 ms |
| `api.mainnet.solana.com` | yes | 231 ms |

## Validators & stake

- **688 active** validators, **9 delinquent** (1.29% by count, 0.009% by stake).
- **Total stake:** 436,134,289 SOL ($45.60B); stake rate 68.89% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.15% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 12.89%; 250 validators at 0% and 67 at 100%.

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

- **SOL:** $104.55 (-3.04% 24h, +14.15% 7d, +42.84% 30d). Market cap $61.06B, 24h volume $6.24B (10.23% of cap). Price source: `coingecko`.
- **TVL:** $5.90B across 335 protocols - rank #2 of 465 chains, 6.63% of all tracked chain TVL. +10.56% over 7d, -55.5% from its ATH.
- **Stablecoins:** $16.38B circulating on Solana (-0.83% 7d) - $2.78 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.70B in 24h, $22.25B over 7d across 119 venues. Volume/TVL turnover 0.628x per day.
- **REV (chain fees):** $16.30M in 24h, $305.99M over 30d. Retained chain revenue $7.53M (46.2% of fees). Annualised fees are 9.75% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 584,162,438 SOL circulating of 633,079,823 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.63B | -1.6% | +24.1% |
| 2 | Kamino Lend | Lending | $1.24B | -1.7% | +8.8% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.2% | +16.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.10B | -1.3% | +23.7% |
| 5 | Jupiter Lend | Lending | $1.10B | -3.4% | +7.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.07B | -1.9% | +21.4% |
| 7 | BlackRock BUIDL | RWA | $886.54M | +0.0% | +19.7% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $784.94M | -1.3% | +8.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $555.25M | -1.4% | +21.1% |
| 10 | xStocks | RWA | $438.22M | -0.7% | +6.8% |
| 11 | Marinade Native | Staking Pool | $435.89M | -1.5% | +70.1% |
| 12 | Sentora | Risk Curators | $361.61M | -0.7% | -0.9% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 335 protocols the total is $16.92B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.5% · Lending 15.5% · Dexs 14.0% · RWA 12.3% · Derivatives 5.2% · Staking Pool 3.9%

### Tokenised assets

$2.41B of tokenised real-world assets and equities are locked on Solana - 14.237% of chain TVL.

- BlackRock BUIDL (RWA): $886.54M
- xStocks (RWA): $438.22M
- OnRe (RWA): $284.53M
- Solstice (Basis Trading): $249.91M
- Ondo Yield Assets (RWA): $179.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,017.0 unique fee payers** signed per block (1,509 distinct addresses in the union, 50.5% overlap between blocks).

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
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |

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

### Change over 24h (vs run at 2026-08-27T16:57:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,739.80 | 5,145.52 | +8.56% |
| Average non-vote TPS | 2,877.86 | 3,011.73 | +4.65% |
| Average slot time (ms) | 367.20 | 321.30 | -12.50% |
| Active validators | 685.00 | 688.00 | +0.44% |
| Delinquent validators | 12.00 | 9.00 | -25.00% |
| Solana TVL | 5,971,320,873.00 | 5,895,133,114.00 | -1.28% |
| SOL price | 109.05 | 104.55 | -4.13% |
| Stablecoin supply | 16,295,559,951.00 | 16,380,565,155.00 | +0.52% |
| 24h DEX volume | 2,351,677,355.00 | 3,700,129,857.54 | +57.34% |
| 24h chain fees | 15,169,688.78 | 16,302,758.52 | +7.47% |

### Change over 7d (vs run at 2026-08-21T18:19:03Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,537.20 | 5,145.52 | +13.41% |
| Average non-vote TPS | 2,672.27 | 3,011.73 | +12.70% |
| Average slot time (ms) | 365.30 | 321.30 | -12.04% |
| Active validators | 685.00 | 688.00 | +0.44% |
| Delinquent validators | 9.00 | 9.00 | +0.00% |
| Solana TVL | 5,439,131,617.00 | 5,895,133,114.00 | +8.38% |
| SOL price | 91.85 | 104.55 | +13.83% |
| Stablecoin supply | 16,516,726,394.00 | 16,380,565,155.00 | -0.82% |
| 24h DEX volume | 2,770,509,439.33 | 3,700,129,857.54 | +33.55% |
| 24h chain fees | 11,078,485.08 | 16,302,758.52 | +47.16% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 5,145.52 | +30.78% |
| Average non-vote TPS | 2,312.46 | 3,011.73 | +30.24% |
| Average slot time (ms) | 424.10 | 321.30 | -24.24% |
| Active validators | 692.00 | 688.00 | -0.58% |
| Delinquent validators | 8.00 | 9.00 | +12.50% |
| Solana TVL | 4,740,035,266.00 | 5,895,133,114.00 | +24.37% |
| SOL price | 72.81 | 104.55 | +43.59% |
| Stablecoin supply | 16,197,749,831.00 | 16,380,565,155.00 | +1.13% |
| 24h DEX volume | 1,636,927,091.91 | 3,700,129,857.54 | +126.04% |
| 24h chain fees | 7,777,648.77 | 16,302,758.52 | +109.61% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
