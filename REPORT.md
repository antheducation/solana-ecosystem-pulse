# Solana Ecosystem Pulse

**Generated:** 2026-11-19T04:46:17Z · **Schema:** `1.0.0` · **Collection time:** 42.2s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $74.66 | -0.16% |
| Market cap | $44.17B | rank #7 |
| Total value locked | $4.73B | -1.94% |
| Stablecoin supply | $13.05B | -6.59% |
| DEX volume (24h) | $1.70B | +12.72% |
| Chain fees / REV (24h) | $9.97M | +22.52% |
| Non-vote TPS (1h avg) | 1,490 | peak 2,039 total |
| Active validators | 660 | 25 delinquent |
| Epoch 1090 | 75.70% complete | 104,977 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 131 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,490; the healthy floor used here is 1,500. | `threshold` |
| [SERIOUS] | Stablecoin supply moved sharply (down 6.6% in 24h) | Stablecoin supply changed -6.6% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,054,954,798.00 sits 3.6 sigma below the median of the last 131 runs (15,997,960,401.00, -18.4%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,489.7 average over the last 60 minutes; 1,655.2 in the latest sample.
- **Total TPS:** 1,489.7 average, 2,039.3 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.5 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 449,221,366 at absolute slot 471,207,023.
- **Epoch 1090:** slot 327,023 of 432,000 (75.70% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.551% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 2445 ms |
| `solana-rpc.publicnode.com` | yes | 56 ms |
| `api.mainnet.solana.com` | yes | 4719 ms |

## Validators & stake

- **660 active** validators, **25 delinquent** (3.65% by count, 0.015% by stake).
- **Total stake:** 426,746,616 SOL ($31.86B); stake rate 66.91% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.98% and top 33 hold 46.77% of active stake.
- **Commission:** median 5.0%, mean 12.76%; 219 validators at 0% and 61 at 100%.

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

- **SOL:** $74.66 (-0.16% 24h, -10.34% 7d, -29.05% 30d). Market cap $44.17B, 24h volume $2.16B (4.89% of cap). Price source: `coingecko`.
- **TVL:** $4.73B across 343 protocols - rank #3 of 425 chains, 6.72% of all tracked chain TVL. -6.60% over 7d, -60.2% from its ATH.
- **Stablecoins:** $13.05B circulating on Solana (-8.23% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.70B in 24h, $10.05B over 7d across 144 venues. Volume/TVL turnover 0.359x per day.
- **REV (chain fees):** $9.97M in 24h, $303.08M over 30d. Retained chain revenue $3.27M (32.8% of fees). Annualised fees are 8.24% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,796,293 SOL circulating of 637,798,604 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.35B | -2.6% | -9.1% |
| 2 | Kamino Lend | Lending | $1.15B | -1.3% | -1.1% |
| 3 | Jupiter Lend | Lending | $954.46M | -1.5% | -1.3% |
| 4 | Raydium AMM | Dexs | $810.51M | -2.1% | -14.4% |
| 5 | Binance Staked SOL | Liquid Staking | $760.76M | -1.0% | -16.4% |
| 6 | Jito Liquid Staking | Liquid Staking | $738.47M | -1.9% | -13.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $588.59M | -1.0% | -7.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $373.96M | -2.6% | -12.6% |
| 9 | Sentora Curator | Risk Curators | $357.73M | +0.1% | -4.2% |
| 10 | OnRe | RWA | $292.92M | -0.1% | -5.3% |
| 11 | Forward Industries SOL | Liquid Staking | $290.24M | -4.1% | +10.0% |
| 12 | CCIP | Bridge | $261.52M | -0.6% | -1.4% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.14B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.8% · Lending 18.9% · Dexs 14.6% · Derivatives 5.3% · RWA 4.6% · Risk Curators 4.1%

### Tokenised assets

$816.49M of tokenised real-world assets and equities are locked on Solana - 6.725% of chain TVL.

- OnRe (RWA): $292.92M
- Huma (RWA): $219.54M
- Solstice (Basis Trading): $201.08M
- JupUSD (Basis Trading): $40.04M
- Plume Vaults (RWA): $39.32M

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

- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-11-19
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-18
- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09

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

### Change over 24h (vs run at 2026-11-18T00:06:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,864.62 | 1,489.70 | -20.11% |
| Average non-vote TPS | 1,864.62 | 1,489.70 | -20.11% |
| Average slot time (ms) | 216.30 | 214.50 | -0.83% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 5.00 | 25.00 | +400.00% |
| Solana TVL | 4,761,137,008.00 | 4,734,424,341.00 | -0.56% |
| SOL price | 74.98 | 74.66 | -0.43% |
| Stablecoin supply | 14,334,785,302.00 | 13,054,954,798.00 | -8.93% |
| 24h DEX volume | 1,479,924,560.31 | 1,701,658,023.31 | +14.98% |
| 24h chain fees | 8,328,289.41 | 9,966,607.56 | +19.67% |

### Change over 7d (vs run at 2026-11-12T04:37:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,577.09 | 1,489.70 | -5.54% |
| Average non-vote TPS | 1,577.09 | 1,489.70 | -5.54% |
| Average slot time (ms) | 214.80 | 214.50 | -0.14% |
| Active validators | 661.00 | 660.00 | -0.15% |
| Delinquent validators | 37.00 | 25.00 | -32.43% |
| Solana TVL | 5,056,620,554.00 | 4,734,424,341.00 | -6.37% |
| SOL price | 82.85 | 74.66 | -9.89% |
| Stablecoin supply | 14,227,548,633.00 | 13,054,954,798.00 | -8.24% |
| 24h DEX volume | 1,636,935,274.95 | 1,701,658,023.31 | +3.95% |
| 24h chain fees | 9,320,608.90 | 9,966,607.56 | +6.93% |

### Change over 30d (vs run at 2026-10-19T21:47:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,210.74 | 1,489.70 | -71.41% |
| Average non-vote TPS | 2,163.29 | 1,489.70 | -31.14% |
| Average slot time (ms) | 218.40 | 214.50 | -1.79% |
| Active validators | 669.00 | 660.00 | -1.35% |
| Delinquent validators | 10.00 | 25.00 | +150.00% |
| Solana TVL | 5,846,232,281.00 | 4,734,424,341.00 | -19.02% |
| SOL price | 104.69 | 74.66 | -28.68% |
| Stablecoin supply | 15,840,000,252.00 | 13,054,954,798.00 | -17.58% |
| 24h DEX volume | 1,697,352,650.38 | 1,701,658,023.31 | +0.25% |
| 24h chain fees | 9,839,385.63 | 9,966,607.56 | +1.29% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 42.1s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
