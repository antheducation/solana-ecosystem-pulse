# Solana Ecosystem Pulse

**Generated:** 2026-09-11T10:06:04Z · **Schema:** `1.0.0` · **Collection time:** 21.6s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.49 | -1.72% |
| Market cap | $58.33B | rank #7 |
| Total value locked | $5.80B | -0.92% |
| Stablecoin supply | $16.36B | -1.32% |
| DEX volume (24h) | $2.95B | -1.73% |
| Chain fees / REV (24h) | $14.82M | -5.70% |
| Non-vote TPS (1h avg) | 1,349 | peak 3,897 total |
| Active validators | 676 | 13 delinquent |
| Epoch 1032 | 70.86% complete | 125,865 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 76 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,349.4 average over the last 60 minutes; 1,469.8 in the latest sample.
- **Total TPS:** 3,482.1 average, 3,897.1 peak. Consensus votes account for 61.2% of all transactions.
- **Slot time:** 315.1 ms average (target 400 ms), worst 1-minute bucket 322.6 ms.
- **Block height:** 424,173,349 at absolute slot 446,130,135.
- **Epoch 1032:** slot 306,135 of 432,000 (70.86% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.654% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 374 ms |
| `solana-rpc.publicnode.com` | yes | 48 ms |
| `api.mainnet.solana.com` | yes | 391 ms |

## Validators & stake

- **676 active** validators, **13 delinquent** (1.89% by count, 0.416% by stake).
- **Total stake:** 439,188,213 SOL ($43.69B); stake rate 69.29% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.31% and top 33 hold 45.80% of active stake.
- **Commission:** median 5.0%, mean 12.82%; 240 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.988% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.733% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.864% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.602% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.188% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,795 | 2.122% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.066% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.679% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.573% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.498% | 0% |

## Economics

- **SOL:** $99.49 (-1.72% 24h, -4.39% 7d, +29.71% 30d). Market cap $58.33B, 24h volume $3.02B (5.18% of cap). Price source: `coingecko`.
- **TVL:** $5.80B across 339 protocols - rank #2 of 467 chains, 6.67% of all tracked chain TVL. -2.17% over 7d, -56.2% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-1.74% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.95B in 24h, $16.62B over 7d across 122 venues. Volume/TVL turnover 0.508x per day.
- **REV (chain fees):** $14.82M in 24h, $370.49M over 30d. Retained chain revenue $5.97M (40.3% of fees). Annualised fees are 9.27% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,537,555 SOL circulating of 633,830,120 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | -1.2% | -3.5% |
| 2 | Kamino Lend | Lending | $1.33B | -0.1% | -0.3% |
| 3 | Raydium AMM | Dexs | $1.12B | -0.7% | -0.1% |
| 4 | Jupiter Lend | Lending | $1.07B | -0.6% | -1.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | -1.3% | -3.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -1.2% | -2.3% |
| 7 | BlackRock BUIDL | RWA | $992.51M | +0.0% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $741.75M | -0.4% | -3.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $516.85M | -1.2% | -3.9% |
| 10 | Sentora Curator | Risk Curators | $388.10M | +0.2% | +1.2% |
| 11 | Marinade Native | Staking Pool | $380.50M | -2.0% | -8.9% |
| 12 | PumpSwap | Dexs | $322.11M | -2.8% | -5.8% |

The top five protocols hold 37.9% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.06B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.3% · Lending 16.6% · Dexs 14.2% · RWA 11.9% · Derivatives 5.1% · Risk Curators 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.864% of chain TVL.

- BlackRock BUIDL (RWA): $992.51M
- OnRe (RWA): $309.48M
- Solstice (Basis Trading): $235.50M
- Ondo Yield Assets (RWA): $180.09M
- Huma Finance V2 (RWA): $169.38M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **880.7 unique fee payers** signed per block (1,221 distinct addresses in the union, 53.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-09-08
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03

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

### Change over 24h (vs run at 2026-09-10T10:08:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,622.08 | 3,482.12 | -3.86% |
| Average non-vote TPS | 1,482.11 | 1,349.41 | -8.95% |
| Average slot time (ms) | 314.50 | 315.10 | +0.19% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 12.00 | 13.00 | +8.33% |
| Solana TVL | 5,847,622,438.00 | 5,802,516,859.00 | -0.77% |
| SOL price | 101.22 | 99.49 | -1.71% |
| Stablecoin supply | 16,576,237,580.00 | 16,356,714,023.00 | -1.32% |
| 24h DEX volume | 2,556,732,104.63 | 2,948,479,741.01 | +15.32% |
| 24h chain fees | 15,572,481.17 | 14,817,128.44 | -4.85% |

### Change over 7d (vs run at 2026-09-04T10:03:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,392.95 | 3,482.12 | +2.63% |
| Average non-vote TPS | 1,264.70 | 1,349.41 | +6.70% |
| Average slot time (ms) | 315.80 | 315.10 | -0.22% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,913,237,547.00 | 5,802,516,859.00 | -1.87% |
| SOL price | 104.06 | 99.49 | -4.39% |
| Stablecoin supply | 16,642,782,149.00 | 16,356,714,023.00 | -1.72% |
| 24h DEX volume | 2,373,588,819.80 | 2,948,479,741.01 | +24.22% |
| 24h chain fees | 10,960,933.49 | 14,817,128.44 | +35.18% |

### Change over 30d (vs run at 2026-08-12T18:43:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,653.97 | 3,482.12 | -25.18% |
| Average non-vote TPS | 3,053.77 | 1,349.41 | -55.81% |
| Average slot time (ms) | 422.30 | 315.10 | -25.38% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 4,816,384,183.00 | 5,802,516,859.00 | +20.47% |
| SOL price | 75.94 | 99.49 | +31.01% |
| Stablecoin supply | 16,295,860,195.00 | 16,356,714,023.00 | +0.37% |
| 24h DEX volume | 1,650,837,789.28 | 2,948,479,741.01 | +78.61% |
| 24h chain fees | 9,976,052.23 | 14,817,128.44 | +48.53% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 21.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
