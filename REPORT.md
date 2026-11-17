# Solana Ecosystem Pulse

**Generated:** 2026-11-17T15:00:27Z · **Schema:** `1.0.0` · **Collection time:** 20.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $73.69 | +2.69% |
| Market cap | $43.60B | rank #7 |
| Total value locked | $4.80B | +2.06% |
| Stablecoin supply | $14.33B | -0.06% |
| DEX volume (24h) | $1.48B | +9.42% |
| Chain fees / REV (24h) | $8.33M | +16.23% |
| Non-vote TPS (1h avg) | 1,921 | peak 2,949 total |
| Active validators | 661 | 5 delinquent |
| Epoch 1089 | 29.69% complete | 303,745 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 131 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,920.8 average over the last 60 minutes; 2,155.8 in the latest sample.
- **Total TPS:** 1,920.8 average, 2,948.6 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.3 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 448,591,069 at absolute slot 470,576,255.
- **Epoch 1089:** slot 128,255 of 432,000 (29.69% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.552% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 154 ms |
| `solana-rpc.publicnode.com` | yes | 110 ms |
| `api.mainnet.solana.com` | yes | 158 ms |

## Validators & stake

- **661 active** validators, **5 delinquent** (0.75% by count, 0.013% by stake).
- **Total stake:** 428,796,576 SOL ($31.60B); stake rate 67.24% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.48% of active stake.
- **Commission:** median 5.0%, mean 12.69%; 220 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,834,343 | 3.926% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,442,668 | 3.835% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,432,778 | 2.900% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,144,846 | 2.366% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,802,677 | 2.286% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,625,021 | 2.245% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,745 | 2.150% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,970,891 | 1.859% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,996,288 | 1.632% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,472 | 1.570% | 5% |

## Economics

- **SOL:** $73.69 (+2.69% 24h, -12.53% 7d, -27.79% 30d). Market cap $43.60B, 24h volume $2.95B (6.77% of cap). Price source: `coingecko`.
- **TVL:** $4.80B across 341 protocols - rank #3 of 424 chains, 6.72% of all tracked chain TVL. -5.56% over 7d, -59.6% from its ATH.
- **Stablecoins:** $14.33B circulating on Solana (-0.07% 7d) - $2.98 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.48B in 24h, $10.55B over 7d across 142 venues. Volume/TVL turnover 0.308x per day.
- **REV (chain fees):** $8.33M in 24h, $310.12M over 30d. Retained chain revenue $3.19M (38.3% of fees). Annualised fees are 6.97% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,739,706 SOL circulating of 637,737,956 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.37B | +2.7% | -10.8% |
| 2 | Kamino Lend | Lending | $1.15B | +1.7% | -1.5% |
| 3 | Jupiter Lend | Lending | $976.90M | +3.8% | +7.4% |
| 4 | Raydium AMM | Dexs | $837.26M | +1.4% | -13.9% |
| 5 | Binance Staked SOL | Liquid Staking | $759.83M | +3.3% | -19.2% |
| 6 | Jito Liquid Staking | Liquid Staking | $746.88M | +3.8% | -15.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $587.86M | +3.4% | -9.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $379.29M | +3.3% | -13.9% |
| 9 | Sentora Curator | Risk Curators | $356.71M | -0.4% | -4.8% |
| 10 | Forward Industries SOL | Liquid Staking | $297.40M | +3.7% | +9.2% |
| 11 | OnRe | RWA | $295.48M | -2.3% | -4.5% |
| 12 | CCIP | Bridge | $274.68M | -1.0% | +3.8% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 341 protocols the total is $12.29B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.7% · Lending 18.9% · Dexs 14.7% · Derivatives 5.3% · RWA 4.7% · Risk Curators 4.1%

### Tokenised assets

$831.34M of tokenised real-world assets and equities are locked on Solana - 6.762% of chain TVL.

- OnRe (RWA): $295.48M
- Huma (RWA): $231.52M
- Solstice (Basis Trading): $201.07M
- JupUSD (Basis Trading): $40.18M
- Plume Vaults (RWA): $38.93M

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

- [SIMD-0643: SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-11-17
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-16
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

### Change over 24h (vs run at 2026-11-16T14:07:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,536.76 | 1,920.75 | +24.99% |
| Average non-vote TPS | 1,536.76 | 1,920.75 | +24.99% |
| Average slot time (ms) | 214.90 | 215.30 | +0.19% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 37.00 | 5.00 | -86.49% |
| Solana TVL | 4,696,110,297.00 | 4,802,561,637.00 | +2.27% |
| SOL price | 70.75 | 73.69 | +4.16% |
| Stablecoin supply | 14,341,479,831.00 | 14,334,215,667.00 | -0.05% |
| 24h DEX volume | 1,352,559,060.09 | 1,479,923,822.31 | +9.42% |
| 24h chain fees | 7,199,120.53 | 8,328,280.55 | +15.68% |

### Change over 7d (vs run at 2026-11-10T13:51:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,797.16 | 1,920.75 | +6.88% |
| Average non-vote TPS | 1,797.16 | 1,920.75 | +6.88% |
| Average slot time (ms) | 214.20 | 215.30 | +0.51% |
| Active validators | 657.00 | 661.00 | +0.61% |
| Delinquent validators | 41.00 | 5.00 | -87.80% |
| Solana TVL | 5,023,282,930.00 | 4,802,561,637.00 | -4.39% |
| SOL price | 84.45 | 73.69 | -12.74% |
| Stablecoin supply | 14,832,999,164.00 | 14,334,215,667.00 | -3.36% |
| 24h DEX volume | 1,487,777,537.32 | 1,479,923,822.31 | -0.53% |
| 24h chain fees | 9,381,055.72 | 8,328,280.55 | -11.22% |

### Change over 30d (vs run at 2026-10-18T19:46:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.46 | 1,920.75 | -61.39% |
| Average non-vote TPS | 1,911.38 | 1,920.75 | +0.49% |
| Average slot time (ms) | 217.10 | 215.30 | -0.83% |
| Active validators | 668.00 | 661.00 | -1.05% |
| Delinquent validators | 12.00 | 5.00 | -58.33% |
| Solana TVL | 5,875,275,842.00 | 4,802,561,637.00 | -18.26% |
| SOL price | 100.82 | 73.69 | -26.91% |
| Stablecoin supply | 15,898,071,483.00 | 14,334,215,667.00 | -9.84% |
| 24h DEX volume | 1,252,516,756.55 | 1,479,923,822.31 | +18.16% |
| 24h chain fees | 9,375,340.79 | 8,328,280.55 | -11.17% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
