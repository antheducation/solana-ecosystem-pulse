# Solana Ecosystem Pulse

**Generated:** 2026-11-18T14:41:12Z · **Schema:** `1.0.0` · **Collection time:** 20.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $73.81 | -0.29% |
| Market cap | $43.68B | rank #7 |
| Total value locked | $4.79B | +1.22% |
| Stablecoin supply | $13.98B | -2.50% |
| DEX volume (24h) | $1.51B | +2.01% |
| Chain fees / REV (24h) | $8.20M | -1.59% |
| Non-vote TPS (1h avg) | 1,964 | peak 3,170 total |
| Active validators | 660 | 25 delinquent |
| Epoch 1090 | 21.24% complete | 340,243 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 131 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,964.2 average over the last 60 minutes; 2,418.7 in the latest sample.
- **Total TPS:** 1,964.2 average, 3,170.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.8 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 448,986,349 at absolute slot 470,971,757.
- **Epoch 1090:** slot 91,757 of 432,000 (21.24% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.551% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 177 ms |
| `solana-rpc.publicnode.com` | yes | 92 ms |
| `api.mainnet.solana.com` | yes | 87 ms |

## Validators & stake

- **660 active** validators, **25 delinquent** (3.65% by count, 0.015% by stake).
- **Total stake:** 426,746,616 SOL ($31.50B); stake rate 66.91% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.98% and top 33 hold 46.77% of active stake.
- **Commission:** median 5.0%, mean 12.61%; 220 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,030,759 | 3.991% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,476,078 | 3.861% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,423,470 | 2.912% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,297,722 | 2.413% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,815,430 | 2.300% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,562 | 2.244% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,715 | 2.162% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,973,220 | 1.869% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,720 | 1.640% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,771,472 | 1.587% | 5% |

## Economics

- **SOL:** $73.81 (-0.29% 24h, -12.64% 7d, -29.18% 30d). Market cap $43.68B, 24h volume $2.57B (5.88% of cap). Price source: `coingecko`.
- **TVL:** $4.79B across 341 protocols - rank #3 of 425 chains, 6.77% of all tracked chain TVL. -5.23% over 7d, -59.7% from its ATH.
- **Stablecoins:** $13.98B circulating on Solana (-2.27% 7d) - $2.92 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.51B in 24h, $10.72B over 7d across 144 venues. Volume/TVL turnover 0.315x per day.
- **REV (chain fees):** $8.20M in 24h, $307.39M over 30d. Retained chain revenue $2.97M (36.3% of fees). Annualised fees are 6.85% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,794,864 SOL circulating of 637,798,901 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.38B | +0.8% | -6.3% |
| 2 | Kamino Lend | Lending | $1.15B | +0.1% | -0.5% |
| 3 | Jupiter Lend | Lending | $971.74M | -0.5% | +0.7% |
| 4 | Raydium AMM | Dexs | $824.07M | -1.6% | -13.0% |
| 5 | Binance Staked SOL | Liquid Staking | $768.83M | +1.4% | -14.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $752.67M | +0.8% | -11.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $591.55M | +0.2% | -6.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $381.41M | +0.6% | -9.9% |
| 9 | Sentora Curator | Risk Curators | $357.35M | +0.1% | -4.6% |
| 10 | Forward Industries SOL | Liquid Staking | $299.54M | +0.7% | +13.9% |
| 11 | OnRe | RWA | $293.51M | -0.7% | -5.1% |
| 12 | CCIP | Bridge | $262.77M | -4.3% | -1.0% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 341 protocols the total is $12.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.0% · Lending 18.9% · Dexs 14.6% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.0%

### Tokenised assets

$817.11M of tokenised real-world assets and equities are locked on Solana - 6.647% of chain TVL.

- OnRe (RWA): $293.51M
- Huma (RWA): $219.57M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $40.04M
- Plume Vaults (RWA): $39.30M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-17
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
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

### Change over 24h (vs run at 2026-11-17T15:00:27Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,920.75 | 1,964.18 | +2.26% |
| Average non-vote TPS | 1,920.75 | 1,964.17 | +2.26% |
| Average slot time (ms) | 215.30 | 215.80 | +0.23% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 5.00 | 25.00 | +400.00% |
| Solana TVL | 4,802,561,637.00 | 4,793,648,732.00 | -0.19% |
| SOL price | 73.69 | 73.81 | +0.16% |
| Stablecoin supply | 14,334,215,667.00 | 13,976,278,030.00 | -2.50% |
| 24h DEX volume | 1,479,923,822.31 | 1,509,645,641.17 | +2.01% |
| 24h chain fees | 8,328,280.55 | 8,200,781.62 | -1.53% |

### Change over 7d (vs run at 2026-11-11T13:03:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,606.62 | 1,964.18 | +22.26% |
| Average non-vote TPS | 1,606.62 | 1,964.17 | +22.25% |
| Average slot time (ms) | 214.60 | 215.80 | +0.56% |
| Active validators | 659.00 | 660.00 | +0.15% |
| Delinquent validators | 40.00 | 25.00 | -37.50% |
| Solana TVL | 5,072,108,301.00 | 4,793,648,732.00 | -5.49% |
| SOL price | 83.71 | 73.81 | -11.83% |
| Stablecoin supply | 14,784,717,550.00 | 13,976,278,030.00 | -5.47% |
| 24h DEX volume | 1,342,063,202.34 | 1,509,645,641.17 | +12.49% |
| 24h chain fees | 8,399,659.99 | 8,200,781.62 | -2.37% |

### Change over 30d (vs run at 2026-10-19T21:47:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,210.74 | 1,964.18 | -62.31% |
| Average non-vote TPS | 2,163.29 | 1,964.17 | -9.20% |
| Average slot time (ms) | 218.40 | 215.80 | -1.19% |
| Active validators | 669.00 | 660.00 | -1.35% |
| Delinquent validators | 10.00 | 25.00 | +150.00% |
| Solana TVL | 5,846,232,281.00 | 4,793,648,732.00 | -18.00% |
| SOL price | 104.69 | 73.81 | -29.50% |
| Stablecoin supply | 15,840,000,252.00 | 13,976,278,030.00 | -11.77% |
| 24h DEX volume | 1,697,352,650.38 | 1,509,645,641.17 | -11.06% |
| 24h chain fees | 9,839,385.63 | 8,200,781.62 | -16.65% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
