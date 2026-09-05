# Solana Ecosystem Pulse

**Generated:** 2026-09-05T14:05:30Z · **Schema:** `1.0.0` · **Collection time:** 12.3s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.80 | +1.15% |
| Market cap | $60.18B | rank #7 |
| Total value locked | $5.88B | -0.72% |
| Stablecoin supply | $16.61B | -0.22% |
| DEX volume (24h) | $1.88B | -23.50% |
| Chain fees / REV (24h) | $10.44M | -11.71% |
| Non-vote TPS (1h avg) | 1,122 | peak 3,542 total |
| Active validators | 677 | 16 delinquent |
| Epoch 1029 | 2.27% complete | 422,192 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 68 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,121.8 average over the last 60 minutes; 1,191.7 in the latest sample.
- **Total TPS:** 3,250.2 average, 3,541.7 peak. Consensus votes account for 65.5% of all transactions.
- **Slot time:** 315.9 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 422,582,263 at absolute slot 444,537,808.
- **Epoch 1029:** slot 9,808 of 432,000 (2.27% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.661% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 113 ms |
| `solana-rpc.publicnode.com` | yes | 166 ms |
| `api.mainnet.solana.com` | yes | 516 ms |

## Validators & stake

- **677 active** validators, **16 delinquent** (2.31% by count, 0.083% by stake).
- **Total stake:** 439,248,820 SOL ($45.15B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.28% and top 33 hold 45.73% of active stake.
- **Commission:** median 5.0%, mean 12.48%; 246 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,421,941 | 3.970% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,321,581 | 3.719% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,507,097 | 2.850% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,374,756 | 2.592% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,561,892 | 2.179% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,268,042 | 2.112% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,037,668 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,352,604 | 1.675% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,128,761 | 1.624% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,594,606 | 1.503% | 0% |

## Economics

- **SOL:** $102.80 (+1.15% 24h, -0.98% 7d, +40.48% 30d). Market cap $60.18B, 24h volume $2.30B (3.82% of cap). Price source: `coingecko`.
- **TVL:** $5.88B across 341 protocols - rank #2 of 466 chains, 6.71% of all tracked chain TVL. +0.12% over 7d, -55.6% from its ATH.
- **Stablecoins:** $16.61B circulating on Solana (+2.60% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.88B in 24h, $14.90B over 7d across 121 venues. Volume/TVL turnover 0.320x per day.
- **REV (chain fees):** $10.44M in 24h, $340.46M over 30d. Retained chain revenue $4.76M (45.7% of fees). Annualised fees are 6.33% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 585,445,999 SOL circulating of 633,549,777 total (92.41%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | -1.6% | -1.7% |
| 2 | Kamino Lend | Lending | $1.32B | -0.3% | +5.4% |
| 3 | Raydium AMM | Dexs | $1.11B | -0.9% | -0.8% |
| 4 | Jupiter Lend | Lending | $1.10B | -0.1% | +0.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.06B | -1.7% | -0.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.05B | -0.9% | -0.0% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +4.3% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $752.49M | -1.8% | -2.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $529.46M | -1.6% | -2.2% |
| 10 | xStocks | RWA | $448.01M | -2.2% | +3.6% |
| 11 | Marinade Native | Staking Pool | $403.87M | -4.0% | -5.0% |
| 12 | Sentora Curator | Risk Curators | $388.43M | +1.8% | +7.6% |

The top five protocols hold 36.7% of Solana's tracked TVL. Summed across all 341 protocols the total is $16.77B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.5% · Lending 16.0% · RWA 14.1% · Dexs 13.8% · Derivatives 5.0% · Staking Pool 3.7%

### Tokenised assets

$2.68B of tokenised real-world assets and equities are locked on Solana - 15.957% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $448.01M
- OnRe (RWA): $298.88M
- Solstice (Basis Trading): $237.91M
- Huma Finance V2 (RWA): $191.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **895.0 unique fee payers** signed per block (1,219 distinct addresses in the union, 54.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) - Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) - Fri, 28 Aug 2026 16:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | pre-release |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 - Current Leader Sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-03
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

### Change over 24h (vs run at 2026-09-04T15:16:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,567.87 | 3,250.15 | -28.85% |
| Average non-vote TPS | 2,461.79 | 1,121.83 | -54.43% |
| Average slot time (ms) | 318.10 | 315.90 | -0.69% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 18.00 | 16.00 | -11.11% |
| Solana TVL | 5,892,160,568.00 | 5,876,842,098.00 | -0.26% |
| SOL price | 101.02 | 102.80 | +1.76% |
| Stablecoin supply | 16,643,633,899.00 | 16,608,776,913.00 | -0.21% |
| 24h DEX volume | 2,459,540,363.80 | 1,881,639,252.00 | -23.50% |
| 24h chain fees | 11,819,564.49 | 10,436,292.55 | -11.70% |

### Change over 7d (vs run at 2026-08-29T15:50:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,871.73 | 3,250.15 | -16.05% |
| Average non-vote TPS | 1,708.06 | 1,121.83 | -34.32% |
| Average slot time (ms) | 316.80 | 315.90 | -0.28% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 9.00 | 16.00 | +77.78% |
| Solana TVL | 5,847,982,989.00 | 5,876,842,098.00 | +0.49% |
| SOL price | 105.04 | 102.80 | -2.13% |
| Stablecoin supply | 16,344,955,563.00 | 16,608,776,913.00 | +1.61% |
| 24h DEX volume | 2,590,586,442.22 | 1,881,639,252.00 | -27.37% |
| 24h chain fees | 15,728,971.43 | 10,436,292.55 | -33.65% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,250.15 | -17.40% |
| Average non-vote TPS | 2,312.46 | 1,121.83 | -51.49% |
| Average slot time (ms) | 424.10 | 315.90 | -25.51% |
| Active validators | 692.00 | 677.00 | -2.17% |
| Delinquent validators | 8.00 | 16.00 | +100.00% |
| Solana TVL | 4,740,035,266.00 | 5,876,842,098.00 | +23.98% |
| SOL price | 72.81 | 102.80 | +41.19% |
| Stablecoin supply | 16,197,749,831.00 | 16,608,776,913.00 | +2.54% |
| 24h DEX volume | 1,636,927,091.91 | 1,881,639,252.00 | +14.95% |
| 24h chain fees | 7,777,648.77 | 10,436,292.55 | +34.18% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 12.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
