# Solana Ecosystem Pulse

**Generated:** 2026-09-11T01:44:12Z · **Schema:** `1.0.0` · **Collection time:** 27.8s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $98.76 | -2.18% |
| Market cap | $57.94B | rank #7 |
| Total value locked | $5.75B | -0.13% |
| Stablecoin supply | $16.36B | -1.31% |
| DEX volume (24h) | $2.95B | -1.76% |
| Chain fees / REV (24h) | $14.68M | -6.59% |
| Non-vote TPS (1h avg) | 1,687 | peak 4,255 total |
| Active validators | 675 | 14 delinquent |
| Epoch 1032 | 48.81% complete | 221,155 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 75 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,687.3 average over the last 60 minutes; 1,693.8 in the latest sample.
- **Total TPS:** 3,820.5 average, 4,254.7 peak. Consensus votes account for 55.8% of all transactions.
- **Slot time:** 315.1 ms average (target 400 ms), worst 1-minute bucket 324.3 ms.
- **Block height:** 424,078,156 at absolute slot 446,034,845.
- **Epoch 1032:** slot 210,845 of 432,000 (48.81% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.654% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 486 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 337 ms |

## Validators & stake

- **675 active** validators, **14 delinquent** (2.03% by count, 0.124% by stake).
- **Total stake:** 439,188,213 SOL ($43.37B); stake rate 69.29% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.24% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 12.55%; 240 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.976% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.722% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.855% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.595% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.182% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,795 | 2.116% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.060% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.674% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.569% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.493% | 0% |

## Economics

- **SOL:** $98.76 (-2.18% 24h, -4.61% 7d, +29.43% 30d). Market cap $57.94B, 24h volume $2.98B (5.15% of cap). Price source: `coingecko`.
- **TVL:** $5.75B across 339 protocols - rank #2 of 467 chains, 6.64% of all tracked chain TVL. -2.93% over 7d, -56.5% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-1.73% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.95B in 24h, $16.61B over 7d across 122 venues. Volume/TVL turnover 0.512x per day.
- **REV (chain fees):** $14.68M in 24h, $367.01M over 30d. Retained chain revenue $6.25M (42.6% of fees). Annualised fees are 9.25% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,537,843 SOL circulating of 633,830,408 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.52B | -1.9% | -4.3% |
| 2 | Kamino Lend | Lending | $1.30B | -2.8% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.11B | -1.0% | -0.4% |
| 4 | Jupiter Lend | Lending | $1.07B | -1.3% | -2.4% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | -2.0% | -4.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.02B | -1.9% | -3.1% |
| 7 | BlackRock BUIDL | RWA | $992.51M | +0.0% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $737.26M | -0.7% | -3.6% |
| 9 | Jupiter Staked SOL | Liquid Staking | $512.58M | -2.0% | -4.7% |
| 10 | Sentora Curator | Risk Curators | $387.91M | +0.3% | +1.1% |
| 11 | Marinade Native | Staking Pool | $380.41M | -1.9% | -8.9% |
| 12 | PumpSwap | Dexs | $325.25M | -2.1% | -4.9% |

The top five protocols hold 37.8% of Solana's tracked TVL. Summed across all 339 protocols the total is $15.97B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.2% · Lending 16.5% · Dexs 14.3% · RWA 12.0% · Derivatives 5.1% · Risk Curators 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.951% of chain TVL.

- BlackRock BUIDL (RWA): $992.51M
- OnRe (RWA): $309.41M
- Solstice (Basis Trading): $235.53M
- Ondo Yield Assets (RWA): $179.95M
- Huma Finance V2 (RWA): $168.42M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,015.3 unique fee payers** signed per block (1,596 distinct addresses in the union, 47.6% overlap between blocks).

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

- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-10
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

### Change over 24h (vs run at 2026-09-10T01:45:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,072.55 | 3,820.46 | -6.19% |
| Average non-vote TPS | 1,943.91 | 1,687.31 | -13.20% |
| Average slot time (ms) | 315.60 | 315.10 | -0.16% |
| Active validators | 675.00 | 675.00 | +0.00% |
| Delinquent validators | 13.00 | 14.00 | +7.69% |
| Solana TVL | 5,785,220,596.00 | 5,753,733,189.00 | -0.54% |
| SOL price | 100.93 | 98.76 | -2.15% |
| Stablecoin supply | 16,629,480,845.00 | 16,358,256,053.00 | -1.63% |
| 24h DEX volume | 2,555,510,166.63 | 2,947,608,342.01 | +15.34% |
| 24h chain fees | 15,507,501.83 | 14,677,343.47 | -5.35% |

### Change over 7d (vs run at 2026-09-04T01:39:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,565.12 | 3,820.46 | +7.16% |
| Average non-vote TPS | 1,443.12 | 1,687.31 | +16.92% |
| Average slot time (ms) | 315.10 | 315.10 | +0.00% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 18.00 | 14.00 | -22.22% |
| Solana TVL | 5,958,193,076.00 | 5,753,733,189.00 | -3.43% |
| SOL price | 103.48 | 98.76 | -4.56% |
| Stablecoin supply | 16,103,149,858.00 | 16,358,256,053.00 | +1.58% |
| 24h DEX volume | 2,372,074,173.80 | 2,947,608,342.01 | +24.26% |
| 24h chain fees | 10,727,529.99 | 14,677,343.47 | +36.82% |

### Change over 30d (vs run at 2026-08-11T18:43:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,160.34 | 3,820.46 | -8.17% |
| Average non-vote TPS | 2,542.89 | 1,687.31 | -33.65% |
| Average slot time (ms) | 422.60 | 315.10 | -25.44% |
| Active validators | 690.00 | 675.00 | -2.17% |
| Delinquent validators | 9.00 | 14.00 | +55.56% |
| Solana TVL | 4,798,590,463.00 | 5,753,733,189.00 | +19.90% |
| SOL price | 75.13 | 98.76 | +31.45% |
| Stablecoin supply | 16,322,733,028.00 | 16,358,256,053.00 | +0.22% |
| 24h DEX volume | 1,581,973,855.56 | 2,947,608,342.01 | +86.32% |
| 24h chain fees | 10,493,090.03 | 14,677,343.47 | +39.88% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 27.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
