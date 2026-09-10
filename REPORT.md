# Solana Ecosystem Pulse

**Generated:** 2026-09-10T10:08:50Z · **Schema:** `1.0.0` · **Collection time:** 18.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.22 | -2.45% |
| Market cap | $59.34B | rank #7 |
| Total value locked | $5.85B | -1.87% |
| Stablecoin supply | $16.58B | -0.32% |
| DEX volume (24h) | $2.56B | -5.68% |
| Chain fees / REV (24h) | $15.57M | -5.97% |
| Non-vote TPS (1h avg) | 1,482 | peak 4,174 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1032 | 7.77% complete | 398,426 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 73 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,482.1 average over the last 60 minutes; 1,348.0 in the latest sample.
- **Total TPS:** 3,622.1 average, 4,174.1 peak. Consensus votes account for 59.1% of all transactions.
- **Slot time:** 314.5 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 423,900,951 at absolute slot 445,857,574.
- **Epoch 1032:** slot 33,574 of 432,000 (7.77% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.654% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 289 ms |
| `solana-rpc.publicnode.com` | yes | 210 ms |
| `api.mainnet.solana.com` | yes | 193 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.019% by stake).
- **Total stake:** 439,188,213 SOL ($44.45B); stake rate 69.29% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.22% and top 33 hold 45.62% of active stake.
- **Commission:** median 5.0%, mean 12.52%; 242 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,441,456 | 3.972% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,324,959 | 3.718% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,523,951 | 2.852% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,380,651 | 2.592% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,569,332 | 2.179% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,279,795 | 2.113% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,036,257 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,344,636 | 1.673% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,880,702 | 1.567% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,550,397 | 1.492% | 0% |

## Economics

- **SOL:** $101.22 (-2.45% 24h, +1.08% 7d, +33.57% 30d). Market cap $59.34B, 24h volume $3.24B (5.46% of cap). Price source: `coingecko`.
- **TVL:** $5.85B across 339 protocols - rank #2 of 466 chains, 6.67% of all tracked chain TVL. +2.27% over 7d, -55.9% from its ATH.
- **Stablecoins:** $16.58B circulating on Solana (+2.94% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.56B in 24h, $16.13B over 7d across 122 venues. Volume/TVL turnover 0.437x per day.
- **REV (chain fees):** $15.57M in 24h, $364.96M over 30d. Retained chain revenue $6.95M (44.6% of fees). Annualised fees are 9.58% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,335,764 SOL circulating of 633,831,009 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -3.5% | +1.9% |
| 2 | Kamino Lend | Lending | $1.33B | -2.2% | +8.1% |
| 3 | Raydium AMM | Dexs | $1.13B | -1.5% | +4.7% |
| 4 | Jupiter Lend | Lending | $1.08B | -2.9% | +1.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.05B | -3.6% | +1.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.04B | -3.4% | +3.1% |
| 7 | BlackRock BUIDL | RWA | $992.17M | +0.5% | +11.4% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $744.43M | -2.0% | -0.1% |
| 9 | Jupiter Staked SOL | Liquid Staking | $522.93M | -3.6% | +1.2% |
| 10 | xStocks | RWA | $437.08M | -1.5% | +0.6% |
| 11 | Marinade Native | Staking Pool | $388.11M | -4.8% | -3.1% |
| 12 | Sentora Curator | Risk Curators | $387.22M | +0.3% | +6.5% |

The top five protocols hold 36.9% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.65B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.4% · Lending 16.1% · RWA 14.1% · Dexs 13.9% · Derivatives 4.9% · Staking Pool 3.6%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.961% of chain TVL.

- BlackRock BUIDL (RWA): $992.17M
- xStocks (RWA): $437.08M
- OnRe (RWA): $307.29M
- Solstice (Basis Trading): $235.68M
- Ondo Yield Assets (RWA): $180.14M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **919.0 unique fee payers** signed per block (1,308 distinct addresses in the union, 52.6% overlap between blocks).

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
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 Amendment: Specify use of sol_get_sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-10
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

### Change over 24h (vs run at 2026-09-09T10:14:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,846.21 | 3,622.08 | -5.83% |
| Average non-vote TPS | 1,717.92 | 1,482.11 | -13.73% |
| Average slot time (ms) | 316.20 | 314.50 | -0.54% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,987,012,086.00 | 5,847,622,438.00 | -2.33% |
| SOL price | 103.79 | 101.22 | -2.48% |
| Stablecoin supply | 16,629,962,371.00 | 16,576,237,580.00 | -0.32% |
| 24h DEX volume | 2,577,833,806.34 | 2,556,732,104.63 | -0.82% |
| 24h chain fees | 16,439,615.38 | 15,572,481.17 | -5.27% |

### Change over 7d (vs run at 2026-09-03T10:13:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,500.09 | 3,622.08 | +3.49% |
| Average non-vote TPS | 1,358.56 | 1,482.11 | +9.09% |
| Average slot time (ms) | 314.50 | 314.50 | +0.00% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 18.00 | 12.00 | -33.33% |
| Solana TVL | 5,754,182,822.00 | 5,847,622,438.00 | +1.62% |
| SOL price | 100.09 | 101.22 | +1.13% |
| Stablecoin supply | 16,099,204,296.00 | 16,576,237,580.00 | +2.96% |
| 24h DEX volume | 2,327,024,999.32 | 2,556,732,104.63 | +9.87% |
| 24h chain fees | 11,210,281.15 | 15,572,481.17 | +38.91% |

### Change over 30d (vs run at 2026-08-11T18:43:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,160.34 | 3,622.08 | -12.94% |
| Average non-vote TPS | 2,542.89 | 1,482.11 | -41.72% |
| Average slot time (ms) | 422.60 | 314.50 | -25.58% |
| Active validators | 690.00 | 676.00 | -2.03% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,798,590,463.00 | 5,847,622,438.00 | +21.86% |
| SOL price | 75.13 | 101.22 | +34.73% |
| Stablecoin supply | 16,322,733,028.00 | 16,576,237,580.00 | +1.55% |
| 24h DEX volume | 1,581,973,855.56 | 2,556,732,104.63 | +61.62% |
| 24h chain fees | 10,493,090.03 | 15,572,481.17 | +48.41% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 18.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
