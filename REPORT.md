# Solana Ecosystem Pulse

**Generated:** 2026-09-07T16:44:32Z · **Schema:** `1.0.0` · **Collection time:** 15.4s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.80 | -2.29% |
| Market cap | $60.83B | rank #7 |
| Total value locked | $5.93B | +0.46% |
| Stablecoin supply | $16.74B | +0.33% |
| DEX volume (24h) | $2.90B | +55.76% |
| Chain fees / REV (24h) | $14.66M | +44.97% |
| Non-vote TPS (1h avg) | 2,000 | peak 4,780 total |
| Active validators | 675 | 13 delinquent |
| Epoch 1030 | 35.59% complete | 278,231 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 70 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 55.8% in 24h) | DEX volume changed +55.8% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Chain fees moved sharply (up 45.0% in 24h) | Chain fees changed +45.0% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,999.7 average over the last 60 minutes; 1,587.5 in the latest sample.
- **Total TPS:** 4,118.9 average, 4,780.3 peak. Consensus votes account for 51.5% of all transactions.
- **Slot time:** 316.7 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 423,157,991 at absolute slot 445,113,769.
- **Epoch 1030:** slot 153,769 of 432,000 (35.59% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.659% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 119 ms |
| `solana-rpc.publicnode.com` | yes | 117 ms |
| `api.mainnet.solana.com` | yes | 93 ms |

## Validators & stake

- **675 active** validators, **13 delinquent** (1.89% by count, 0.041% by stake).
- **Total stake:** 439,477,988 SOL ($45.62B); stake rate 69.36% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.20% and top 33 hold 45.63% of active stake.
- **Commission:** median 5.0%, mean 12.51%; 245 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,438,541 | 3.970% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,336,964 | 3.719% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,517,399 | 2.849% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,397,824 | 2.595% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,564,412 | 2.177% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,181,909 | 2.090% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,038,443 | 2.057% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,384,461 | 1.681% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,858,929 | 1.561% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,595,421 | 1.501% | 0% |

## Economics

- **SOL:** $103.80 (-2.29% 24h, +0.97% 7d, +36.00% 30d). Market cap $60.83B, 24h volume $3.35B (5.51% of cap). Price source: `coingecko`.
- **TVL:** $5.93B across 338 protocols - rank #2 of 466 chains, 6.73% of all tracked chain TVL. +2.52% over 7d, -55.2% from its ATH.
- **Stablecoins:** $16.74B circulating on Solana (+4.86% 7d) - $2.82 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.90B in 24h, $16.07B over 7d across 121 venues. Volume/TVL turnover 0.489x per day.
- **REV (chain fees):** $14.66M in 24h, $348.01M over 30d. Retained chain revenue $6.04M (41.2% of fees). Annualised fees are 8.79% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,165,945 SOL circulating of 633,643,225 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.60B | -1.1% | +2.3% |
| 2 | Kamino Lend | Lending | $1.33B | -0.9% | +7.5% |
| 3 | Raydium AMM | Dexs | $1.15B | -0.8% | +4.8% |
| 4 | Jupiter Lend | Lending | $1.09B | -2.5% | +1.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.09B | -1.2% | +3.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.07B | -1.9% | +4.0% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +0.0% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $756.00M | -1.3% | -0.3% |
| 9 | Jupiter Staked SOL | Liquid Staking | $541.02M | -0.8% | +2.9% |
| 10 | xStocks | RWA | $447.07M | -0.7% | +3.9% |
| 11 | Marinade Native | Staking Pool | $414.47M | -0.3% | -1.2% |
| 12 | Sentora Curator | Risk Curators | $386.73M | -0.6% | +7.2% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.98B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.8% · Lending 15.9% · Dexs 14.0% · RWA 13.9% · Derivatives 4.9% · Staking Pool 3.8%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.736% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $447.07M
- OnRe (RWA): $302.40M
- Solstice (Basis Trading): $237.88M
- Huma Finance V2 (RWA): $185.01M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **924.3 unique fee payers** signed per block (1,305 distinct addresses in the union, 52.9% overlap between blocks).

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

### Change over 24h (vs run at 2026-09-06T14:29:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,822.09 | 4,118.86 | +7.76% |
| Average non-vote TPS | 1,703.42 | 1,999.68 | +17.39% |
| Average slot time (ms) | 317.20 | 316.70 | -0.16% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 17.00 | 13.00 | -23.53% |
| Solana TVL | 5,924,761,773.00 | 5,933,702,675.00 | +0.15% |
| SOL price | 106.04 | 103.80 | -2.11% |
| Stablecoin supply | 16,685,708,351.00 | 16,740,769,575.00 | +0.33% |
| 24h DEX volume | 1,960,574,882.81 | 2,904,503,252.44 | +48.15% |
| 24h chain fees | 10,482,001.50 | 14,655,299.70 | +39.81% |

### Change over 7d (vs run at 2026-08-31T18:43:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,328.53 | 4,118.86 | -4.84% |
| Average non-vote TPS | 2,195.90 | 1,999.68 | -8.94% |
| Average slot time (ms) | 317.20 | 316.70 | -0.16% |
| Active validators | 681.00 | 675.00 | -0.88% |
| Delinquent validators | 16.00 | 13.00 | -18.75% |
| Solana TVL | 5,791,254,029.00 | 5,933,702,675.00 | +2.46% |
| SOL price | 104.61 | 103.80 | -0.77% |
| Stablecoin supply | 16,123,089,134.00 | 16,740,769,575.00 | +3.83% |
| 24h DEX volume | 1,929,632,644.74 | 2,904,503,252.44 | +50.52% |
| 24h chain fees | 12,307,328.44 | 14,655,299.70 | +19.08% |

### Change over 30d (vs run at 2026-08-08T18:19:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,014.93 | 4,118.86 | +2.59% |
| Average non-vote TPS | 2,401.41 | 1,999.68 | -16.73% |
| Average slot time (ms) | 424.90 | 316.70 | -25.46% |
| Active validators | 691.00 | 675.00 | -2.32% |
| Delinquent validators | 9.00 | 13.00 | +44.44% |
| Solana TVL | 4,824,990,783.00 | 5,933,702,675.00 | +22.98% |
| SOL price | 76.22 | 103.80 | +36.18% |
| Stablecoin supply | 16,242,440,945.00 | 16,740,769,575.00 | +3.07% |
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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 15.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
