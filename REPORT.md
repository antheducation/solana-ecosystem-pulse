# Solana Ecosystem Pulse

**Generated:** 2026-11-15T22:11:07Z · **Schema:** `1.0.0` · **Collection time:** 27.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $72.09 | +4.25% |
| Market cap | $42.65B | rank #7 |
| Total value locked | $4.71B | -3.57% |
| Stablecoin supply | $14.22B | -0.01% |
| DEX volume (24h) | $1.68B | +7.52% |
| Chain fees / REV (24h) | $7.95M | -13.93% |
| Non-vote TPS (1h avg) | 1,937 | peak 2,827 total |
| Active validators | 662 | 38 delinquent |
| Epoch 1087 | 71.35% complete | 123,748 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,936.8 average over the last 60 minutes; 1,696.3 in the latest sample.
- **Total TPS:** 1,936.8 average, 2,826.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.6 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 447,907,210 at absolute slot 469,892,252.
- **Epoch 1087:** slot 308,252 of 432,000 (71.35% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.556% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 107 ms |
| `solana-rpc.publicnode.com` | yes | 78 ms |
| `api.mainnet.solana.com` | yes | 142 ms |

## Validators & stake

- **662 active** validators, **38 delinquent** (5.43% by count, 0.084% by stake).
- **Total stake:** 429,328,621 SOL ($30.95B); stake rate 67.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.47% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 220 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,927,749 | 3.946% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,404,544 | 3.824% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,614,561 | 2.941% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,141,932 | 2.364% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,754,208 | 2.274% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,640,656 | 2.247% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,204,466 | 2.146% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,943,264 | 1.852% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,232 | 1.630% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,708,648 | 1.564% | 5% |

## Economics

- **SOL:** $72.09 (+4.25% 24h, -15.89% 7d, -30.79% 30d). Market cap $42.65B, 24h volume $4.01B (9.41% of cap). Price source: `coingecko`.
- **TVL:** $4.71B across 343 protocols - rank #3 of 423 chains, 6.56% of all tracked chain TVL. -9.70% over 7d, -60.4% from its ATH.
- **Stablecoins:** $14.22B circulating on Solana (-2.61% 7d) - $3.02 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.68B in 24h, $10.23B over 7d across 142 venues. Volume/TVL turnover 0.357x per day.
- **REV (chain fees):** $7.95M in 24h, $318.94M over 30d. Retained chain revenue $2.75M (34.6% of fees). Annualised fees are 6.80% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,628,975 SOL circulating of 637,615,718 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.35B | +0.3% | -15.1% |
| 2 | Kamino Lend | Lending | $1.13B | -0.8% | -4.7% |
| 3 | Jupiter Lend | Lending | $925.17M | +0.3% | -0.1% |
| 4 | Raydium AMM | Dexs | $832.84M | -1.2% | -16.9% |
| 5 | Binance Staked SOL | Liquid Staking | $752.67M | +0.0% | -22.8% |
| 6 | Jito Liquid Staking | Liquid Staking | $729.00M | +2.8% | -20.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $574.20M | +0.3% | -13.1% |
| 8 | Jupiter Staked SOL | Liquid Staking | $372.07M | +1.1% | -18.3% |
| 9 | Sentora Curator | Risk Curators | $358.30M | -0.1% | -4.2% |
| 10 | OnRe | RWA | $302.24M | -1.7% | -2.1% |
| 11 | Forward Industries SOL | Liquid Staking | $290.38M | +2.3% | +2.9% |
| 12 | CCIP | Bridge | $278.12M | -2.7% | +4.8% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.09B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.6% · Lending 18.7% · Dexs 14.7% · Derivatives 5.2% · RWA 4.9% · Risk Curators 4.0%

### Tokenised assets

$844.15M of tokenised real-world assets and equities are locked on Solana - 6.983% of chain TVL.

- OnRe (RWA): $302.24M
- Huma (RWA): $237.46M
- Solstice (Basis Trading): $201.08M
- JupUSD (Basis Trading): $40.25M
- Plume Vaults (RWA): $36.98M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-12
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07

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

### Change over 24h (vs run at 2026-11-14T21:44:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,639.46 | 1,936.81 | -26.62% |
| Average non-vote TPS | 2,639.46 | 1,936.81 | -26.62% |
| Average slot time (ms) | 215.80 | 214.60 | -0.56% |
| Active validators | 663.00 | 662.00 | -0.15% |
| Delinquent validators | 36.00 | 38.00 | +5.56% |
| Solana TVL | 4,728,855,740.00 | 4,706,449,733.00 | -0.47% |
| SOL price | 70.58 | 72.09 | +2.14% |
| Stablecoin supply | 14,226,361,055.00 | 14,224,861,314.00 | -0.01% |
| 24h DEX volume | 1,560,618,093.20 | 1,677,928,733.70 | +7.52% |
| 24h chain fees | 9,227,351.07 | 7,947,344.14 | -13.87% |

### Change over 7d (vs run at 2026-11-08T21:25:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,720.02 | 1,936.81 | +12.60% |
| Average non-vote TPS | 1,720.02 | 1,936.81 | +12.60% |
| Average slot time (ms) | 214.60 | 214.60 | +0.00% |
| Active validators | 660.00 | 662.00 | +0.30% |
| Delinquent validators | 37.00 | 38.00 | +2.70% |
| Solana TVL | 5,218,639,304.00 | 4,706,449,733.00 | -9.81% |
| SOL price | 89.02 | 72.09 | -19.02% |
| Stablecoin supply | 15,146,574,447.00 | 14,224,861,314.00 | -6.09% |
| 24h DEX volume | 917,438,831.61 | 1,677,928,733.70 | +82.89% |
| 24h chain fees | 8,033,239.47 | 7,947,344.14 | -1.07% |

### Change over 30d (vs run at 2026-10-16T20:09:55Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,572.51 | 1,936.81 | -65.24% |
| Average non-vote TPS | 2,482.29 | 1,936.81 | -21.97% |
| Average slot time (ms) | 216.20 | 214.60 | -0.74% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 9.00 | 38.00 | +322.22% |
| Solana TVL | 5,951,004,332.00 | 4,706,449,733.00 | -20.91% |
| SOL price | 103.59 | 72.09 | -30.41% |
| Stablecoin supply | 16,233,803,204.00 | 14,224,861,314.00 | -12.38% |
| 24h DEX volume | 2,539,283,878.03 | 1,677,928,733.70 | -33.92% |
| 24h chain fees | 12,783,602.89 | 7,947,344.14 | -37.83% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 27.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
