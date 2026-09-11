# Solana Ecosystem Pulse

**Generated:** 2026-09-11T15:22:39Z · **Schema:** `1.0.0` · **Collection time:** 23.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.12 | +3.31% |
| Market cap | $60.49B | rank #7 |
| Total value locked | $5.83B | -0.47% |
| Stablecoin supply | $16.36B | -1.32% |
| DEX volume (24h) | $2.92B | -2.61% |
| Chain fees / REV (24h) | $14.61M | -6.98% |
| Non-vote TPS (1h avg) | 2,427 | peak 5,252 total |
| Active validators | 674 | 16 delinquent |
| Epoch 1032 | 84.71% complete | 66,059 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 77 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,427.3 average over the last 60 minutes; 2,273.0 in the latest sample.
- **Total TPS:** 4,526.8 average, 5,252.4 peak. Consensus votes account for 46.4% of all transactions.
- **Slot time:** 318.0 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 424,233,091 at absolute slot 446,189,941.
- **Epoch 1032:** slot 365,941 of 432,000 (84.71% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.654% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 236 ms |
| `solana-rpc.publicnode.com` | yes | 273 ms |
| `api.mainnet.solana.com` | yes | 226 ms |

## Validators & stake

- **674 active** validators, **16 delinquent** (2.32% by count, 0.449% by stake).
- **Total stake:** 439,188,213 SOL ($45.29B); stake rate 69.29% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.32% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.85%; 239 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.989% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.734% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.864% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.603% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.189% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,795 | 2.122% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.067% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.574% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.498% | 0% |

## Economics

- **SOL:** $103.12 (+3.31% 24h, +2.31% 7d, +36.77% 30d). Market cap $60.49B, 24h volume $3.99B (6.60% of cap). Price source: `coingecko`.
- **TVL:** $5.83B across 339 protocols - rank #2 of 467 chains, 6.58% of all tracked chain TVL. -1.73% over 7d, -56.0% from its ATH.
- **Stablecoins:** $16.36B circulating on Solana (-1.74% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.92B in 24h, $18.00B over 7d across 122 venues. Volume/TVL turnover 0.501x per day.
- **REV (chain fees):** $14.61M in 24h, $371.97M over 30d. Retained chain revenue $5.78M (39.5% of fees). Annualised fees are 8.82% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,537,340 SOL circulating of 633,829,905 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | +1.2% | -2.0% |
| 2 | Kamino Lend | Lending | $1.34B | +1.8% | +0.7% |
| 3 | Raydium AMM | Dexs | $1.11B | +0.8% | -0.3% |
| 4 | Binance Staked SOL | Liquid Staking | $1.09B | +4.9% | +1.5% |
| 5 | Jupiter Lend | Lending | $1.08B | +1.0% | -1.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | +1.7% | -0.9% |
| 7 | BlackRock BUIDL | RWA | $992.51M | +0.0% | +5.8% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $749.52M | +1.8% | -2.0% |
| 9 | Jupiter Staked SOL | Liquid Staking | $524.59M | +1.2% | -2.4% |
| 10 | Sentora Curator | Risk Curators | $387.89M | -0.2% | +1.1% |
| 11 | Marinade Native | Staking Pool | $386.36M | +0.4% | -7.5% |
| 12 | PumpSwap | Dexs | $323.74M | -1.5% | -5.3% |

The top five protocols hold 38.1% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.22B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.7% · Lending 16.6% · Dexs 14.1% · RWA 11.7% · Derivatives 5.1% · Staking Pool 3.7%

### Tokenised assets

$2.21B of tokenised real-world assets and equities are locked on Solana - 13.635% of chain TVL.

- BlackRock BUIDL (RWA): $992.51M
- OnRe (RWA): $294.72M
- Solstice (Basis Trading): $235.00M
- Ondo Yield Assets (RWA): $179.85M
- Huma Finance V2 (RWA): $170.16M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,026.7 unique fee payers** signed per block (1,631 distinct addresses in the union, 47.0% overlap between blocks).

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
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | pre-release |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

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

### Change over 24h (vs run at 2026-09-10T15:20:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,259.15 | 4,526.83 | +6.28% |
| Average non-vote TPS | 2,140.25 | 2,427.26 | +13.41% |
| Average slot time (ms) | 317.30 | 318.00 | +0.22% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 13.00 | 16.00 | +23.08% |
| Solana TVL | 5,769,788,805.00 | 5,829,321,373.00 | +1.03% |
| SOL price | 99.93 | 103.12 | +3.19% |
| Stablecoin supply | 16,575,633,012.00 | 16,356,744,456.00 | -1.32% |
| 24h DEX volume | 3,000,435,429.63 | 2,921,890,110.01 | -2.62% |
| 24h chain fees | 15,435,517.17 | 14,614,973.44 | -5.32% |

### Change over 7d (vs run at 2026-09-04T15:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,567.87 | 4,526.83 | -0.90% |
| Average non-vote TPS | 2,461.79 | 2,427.26 | -1.40% |
| Average slot time (ms) | 318.10 | 318.00 | -0.03% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 18.00 | 16.00 | -11.11% |
| Solana TVL | 5,892,160,568.00 | 5,829,321,373.00 | -1.07% |
| SOL price | 101.02 | 103.12 | +2.08% |
| Stablecoin supply | 16,643,633,899.00 | 16,356,744,456.00 | -1.72% |
| 24h DEX volume | 2,459,540,363.80 | 2,921,890,110.01 | +18.80% |
| 24h chain fees | 11,819,564.49 | 14,614,973.44 | +23.65% |

### Change over 30d (vs run at 2026-08-12T18:43:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,653.97 | 4,526.83 | -2.73% |
| Average non-vote TPS | 3,053.77 | 2,427.26 | -20.52% |
| Average slot time (ms) | 422.30 | 318.00 | -24.70% |
| Active validators | 685.00 | 674.00 | -1.61% |
| Delinquent validators | 14.00 | 16.00 | +14.29% |
| Solana TVL | 4,816,384,183.00 | 5,829,321,373.00 | +21.03% |
| SOL price | 75.94 | 103.12 | +35.79% |
| Stablecoin supply | 16,295,860,195.00 | 16,356,744,456.00 | +0.37% |
| 24h DEX volume | 1,650,837,789.28 | 2,921,890,110.01 | +76.99% |
| 24h chain fees | 9,976,052.23 | 14,614,973.44 | +46.50% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 22.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
