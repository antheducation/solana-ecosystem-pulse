# Solana Ecosystem Pulse

**Generated:** 2026-09-07T20:51:35Z · **Schema:** `1.0.0` · **Collection time:** 28.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.08 | -1.63% |
| Market cap | $60.98B | rank #7 |
| Total value locked | $5.90B | -0.16% |
| Stablecoin supply | $16.74B | +0.33% |
| DEX volume (24h) | $2.90B | +55.76% |
| Chain fees / REV (24h) | $14.66M | +44.97% |
| Non-vote TPS (1h avg) | 1,809 | peak 4,694 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1030 | 46.43% complete | 231,425 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 70 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 55.8% in 24h) | DEX volume changed +55.8% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 45.0% in 24h) | Chain fees changed +45.0% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,809.5 average over the last 60 minutes; 1,322.8 in the latest sample.
- **Total TPS:** 3,930.7 average, 4,694.1 peak. Consensus votes account for 54.0% of all transactions.
- **Slot time:** 316.7 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 423,204,751 at absolute slot 445,160,575.
- **Epoch 1030:** slot 200,575 of 432,000 (46.43% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.659% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 648 ms |
| `solana-rpc.publicnode.com` | yes | 104 ms |
| `api.mainnet.solana.com` | yes | 120 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.011% by stake).
- **Total stake:** 439,477,988 SOL ($45.74B); stake rate 69.36% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.19% and top 33 hold 45.61% of active stake.
- **Commission:** median 5.0%, mean 12.50%; 245 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,438,541 | 3.968% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,336,964 | 3.718% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,517,399 | 2.849% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,397,824 | 2.594% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,564,412 | 2.177% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,181,909 | 2.090% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,038,443 | 2.057% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,384,461 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,858,929 | 1.561% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,595,421 | 1.501% | 0% |

## Economics

- **SOL:** $104.08 (-1.63% 24h, +0.45% 7d, +36.76% 30d). Market cap $60.98B, 24h volume $3.28B (5.38% of cap). Price source: `coingecko`.
- **TVL:** $5.90B across 338 protocols - rank #2 of 466 chains, 6.69% of all tracked chain TVL. +1.90% over 7d, -55.5% from its ATH.
- **Stablecoins:** $16.74B circulating on Solana (+4.86% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.90B in 24h, $16.07B over 7d across 121 venues. Volume/TVL turnover 0.493x per day.
- **REV (chain fees):** $14.66M in 24h, $348.01M over 30d. Retained chain revenue $6.04M (41.2% of fees). Annualised fees are 8.77% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,165,786 SOL circulating of 633,643,065 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | -1.7% | +1.8% |
| 2 | Kamino Lend | Lending | $1.33B | -0.9% | +7.4% |
| 3 | Raydium AMM | Dexs | $1.14B | -1.8% | +3.8% |
| 4 | Jupiter Lend | Lending | $1.09B | -2.5% | +1.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | -1.4% | +2.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | -2.4% | +3.5% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +0.0% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $753.08M | -1.1% | -0.7% |
| 9 | Jupiter Staked SOL | Liquid Staking | $537.98M | -1.7% | +2.3% |
| 10 | xStocks | RWA | $447.32M | -0.9% | +4.0% |
| 11 | Marinade Native | Staking Pool | $412.11M | -1.0% | -1.8% |
| 12 | Sentora Curator | Risk Curators | $386.63M | -0.5% | +7.1% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.91B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.7% · Lending 15.9% · RWA 14.0% · Dexs 13.9% · Derivatives 4.9% · Staking Pool 3.8%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.810% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $447.32M
- OnRe (RWA): $302.47M
- Solstice (Basis Trading): $237.92M
- Huma Finance V2 (RWA): $186.42M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **984.0 unique fee payers** signed per block (1,478 distinct addresses in the union, 49.9% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | pre-release |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31

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

### Change over 24h (vs run at 2026-09-06T19:40:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,849.55 | 3,930.66 | +2.11% |
| Average non-vote TPS | 1,725.26 | 1,809.47 | +4.88% |
| Average slot time (ms) | 316.50 | 316.70 | +0.06% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 17.00 | 12.00 | -29.41% |
| Solana TVL | 5,924,761,773.00 | 5,896,988,391.00 | -0.47% |
| SOL price | 105.62 | 104.08 | -1.46% |
| Stablecoin supply | 16,686,094,754.00 | 16,741,090,548.00 | +0.33% |
| 24h DEX volume | 1,960,574,882.81 | 2,904,503,252.44 | +48.15% |
| 24h chain fees | 10,482,001.50 | 14,655,299.70 | +39.81% |

### Change over 7d (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 3,930.66 | -9.19% |
| Average non-vote TPS | 2,195.90 | 1,809.47 | -17.60% |
| Average slot time (ms) | 317.20 | 316.70 | -0.16% |
| Active validators | 681.00 | 676.00 | -0.73% |
| Delinquent validators | 16.00 | 12.00 | -25.00% |
| Solana TVL | 5,791,254,029.00 | 5,896,988,391.00 | +1.83% |
| SOL price | 104.61 | 104.08 | -0.51% |
| Stablecoin supply | 16,123,089,134.00 | 16,741,090,548.00 | +3.83% |
| 24h DEX volume | 1,929,632,644.74 | 2,904,503,252.44 | +50.52% |
| 24h chain fees | 12,307,328.44 | 14,655,299.70 | +19.08% |

### Change over 30d (vs run at 2026-08-08T18:19:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,014.93 | 3,930.66 | -2.10% |
| Average non-vote TPS | 2,401.41 | 1,809.47 | -24.65% |
| Average slot time (ms) | 424.90 | 316.70 | -25.46% |
| Active validators | 691.00 | 676.00 | -2.17% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,824,990,783.00 | 5,896,988,391.00 | +22.22% |
| SOL price | 76.22 | 104.08 | +36.55% |
| Stablecoin supply | 16,242,440,945.00 | 16,741,090,548.00 | +3.07% |
| 24h DEX volume | 1,362,524,618.02 | 2,904,503,252.44 | +113.17% |
| 24h chain fees | 8,154,900.02 | 14,655,299.70 | +79.71% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 28.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
