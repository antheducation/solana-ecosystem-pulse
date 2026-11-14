# Solana Ecosystem Pulse

**Generated:** 2026-11-14T21:44:56Z · **Schema:** `1.0.0` · **Collection time:** 22.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.58 | -10.39% |
| Market cap | $41.75B | rank #7 |
| Total value locked | $4.73B | -5.95% |
| Stablecoin supply | $14.23B | -1.04% |
| DEX volume (24h) | $1.56B | +3.80% |
| Chain fees / REV (24h) | $9.23M | +14.31% |
| Non-vote TPS (1h avg) | 2,639 | peak 4,221 total |
| Active validators | 663 | 36 delinquent |
| Epoch 1086 | 76.64% complete | 100,927 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | SOL price moved sharply (down 10.4% in 24h) | SOL price changed -10.4% over the last day, past the 8% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,639.5 average over the last 60 minutes; 1,871.6 in the latest sample.
- **Total TPS:** 2,639.5 average, 4,220.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.8 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 447,498,129 at absolute slot 469,483,073.
- **Epoch 1086:** slot 331,073 of 432,000 (76.64% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.557% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 181 ms |
| `solana-rpc.publicnode.com` | yes | 111 ms |
| `api.mainnet.solana.com` | yes | 153 ms |

## Validators & stake

- **663 active** validators, **36 delinquent** (5.15% by count, 0.092% by stake).
- **Total stake:** 429,651,631 SOL ($30.32B); stake rate 67.39% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.74% and top 33 hold 46.39% of active stake.
- **Commission:** median 5.0%, mean 12.87%; 221 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,955,905 | 3.950% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,374,909 | 3.815% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,611,498 | 2.938% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,140,468 | 2.362% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,736,890 | 2.268% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,439 | 2.230% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,199,377 | 2.143% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,914,792 | 1.844% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,990,062 | 1.628% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,707,745 | 1.563% | 5% |

## Economics

- **SOL:** $70.58 (-10.39% 24h, -20.70% 7d, -33.15% 30d). Market cap $41.75B, 24h volume $4.22B (10.12% of cap). Price source: `coingecko`.
- **TVL:** $4.73B across 343 protocols - rank #3 of 423 chains, 6.57% of all tracked chain TVL. -10.03% over 7d, -60.2% from its ATH.
- **Stablecoins:** $14.23B circulating on Solana (-1.97% 7d) - $3.01 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.56B in 24h, $9.47B over 7d across 141 venues. Volume/TVL turnover 0.330x per day.
- **REV (chain fees):** $9.23M in 24h, $324.93M over 30d. Retained chain revenue $3.38M (36.6% of fees). Annualised fees are 8.07% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,573,669 SOL circulating of 637,554,631 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.34B | -11.0% | -16.1% |
| 2 | Kamino Lend | Lending | $1.14B | -3.3% | -4.1% |
| 3 | Jupiter Lend | Lending | $922.02M | -2.5% | -1.1% |
| 4 | Raydium AMM | Dexs | $843.41M | -7.4% | -17.1% |
| 5 | Binance Staked SOL | Liquid Staking | $752.57M | -13.3% | -23.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $735.69M | -10.0% | -20.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $572.19M | -6.6% | -13.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $368.19M | -10.1% | -20.0% |
| 9 | Sentora Curator | Risk Curators | $358.70M | +0.5% | -4.0% |
| 10 | OnRe | RWA | $307.57M | -0.4% | -0.3% |
| 11 | Forward Industries SOL | Liquid Staking | $290.34M | -10.2% | +2.1% |
| 12 | CCIP | Bridge | $285.97M | -0.4% | +7.8% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.21B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.2% · Lending 18.6% · Dexs 14.8% · Derivatives 5.2% · RWA 4.9% · Risk Curators 4.2%

### Tokenised assets

$860.44M of tokenised real-world assets and equities are locked on Solana - 7.046% of chain TVL.

- OnRe (RWA): $307.57M
- Huma (RWA): $247.05M
- Solstice (Basis Trading): $201.02M
- JupUSD (Basis Trading): $40.84M
- Plume Vaults (RWA): $37.02M

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

### Change over 24h (vs run at 2026-11-13T22:57:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,140.34 | 2,639.46 | +23.32% |
| Average non-vote TPS | 2,140.34 | 2,639.46 | +23.32% |
| Average slot time (ms) | 215.20 | 215.80 | +0.28% |
| Active validators | 661.00 | 663.00 | +0.30% |
| Delinquent validators | 38.00 | 36.00 | -5.26% |
| Solana TVL | 4,958,650,115.00 | 4,728,855,740.00 | -4.63% |
| SOL price | 78.20 | 70.58 | -9.74% |
| Stablecoin supply | 14,376,185,613.00 | 14,226,361,055.00 | -1.04% |
| 24h DEX volume | 1,503,485,412.77 | 1,560,618,093.20 | +3.80% |
| 24h chain fees | 8,074,998.20 | 9,227,351.07 | +14.27% |

### Change over 7d (vs run at 2026-11-07T21:09:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,746.41 | 2,639.46 | +51.14% |
| Average non-vote TPS | 1,746.41 | 2,639.46 | +51.14% |
| Average slot time (ms) | 214.20 | 215.80 | +0.75% |
| Active validators | 663.00 | 663.00 | +0.00% |
| Delinquent validators | 34.00 | 36.00 | +5.88% |
| Solana TVL | 5,227,801,801.00 | 4,728,855,740.00 | -9.54% |
| SOL price | 88.92 | 70.58 | -20.63% |
| Stablecoin supply | 14,838,386,518.00 | 14,226,361,055.00 | -4.12% |
| 24h DEX volume | 1,479,986,839.85 | 1,560,618,093.20 | +5.45% |
| 24h chain fees | 9,301,190.12 | 9,227,351.07 | -0.79% |

### Change over 30d (vs run at 2026-10-15T20:36:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,323.17 | 2,639.46 | -50.42% |
| Average non-vote TPS | 2,236.62 | 2,639.46 | +18.01% |
| Average slot time (ms) | 216.50 | 215.80 | -0.32% |
| Active validators | 672.00 | 663.00 | -1.34% |
| Delinquent validators | 9.00 | 36.00 | +300.00% |
| Solana TVL | 6,044,693,032.00 | 4,728,855,740.00 | -21.77% |
| SOL price | 105.91 | 70.58 | -33.36% |
| Stablecoin supply | 16,055,865,871.00 | 14,226,361,055.00 | -11.39% |
| 24h DEX volume | 2,118,350,659.32 | 1,560,618,093.20 | -26.33% |
| 24h chain fees | 10,654,111.63 | 9,227,351.07 | -13.39% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
