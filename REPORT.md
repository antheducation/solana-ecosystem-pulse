# Solana Ecosystem Pulse

**Generated:** 2026-11-17T01:12:04Z · **Schema:** `1.0.0` · **Collection time:** 22.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $71.58 | -0.07% |
| Market cap | $42.36B | rank #7 |
| Total value locked | $4.75B | -0.00% |
| Stablecoin supply | $14.33B | -0.05% |
| DEX volume (24h) | $1.38B | +2.15% |
| Chain fees / REV (24h) | $7.25M | +2.12% |
| Non-vote TPS (1h avg) | 1,790 | peak 2,601 total |
| Active validators | 662 | 37 delinquent |
| Epoch 1088 | 76.12% complete | 103,147 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 130 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,790.2 average over the last 60 minutes; 2,334.8 in the latest sample.
- **Total TPS:** 1,790.2 average, 2,601.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.5 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 448,359,702 at absolute slot 470,344,853.
- **Epoch 1088:** slot 328,853 of 432,000 (76.12% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.554% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 206 ms |
| `solana-rpc.publicnode.com` | yes | 139 ms |
| `api.mainnet.solana.com` | yes | 208 ms |

## Validators & stake

- **662 active** validators, **37 delinquent** (5.29% by count, 0.035% by stake).
- **Total stake:** 429,145,034 SOL ($30.72B); stake rate 67.30% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.49% of active stake.
- **Commission:** median 5.0%, mean 12.78%; 220 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,936,855 | 3.948% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,432,361 | 3.830% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,687 | 2.911% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,142,842 | 2.364% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,787,748 | 2.282% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,620,150 | 2.242% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,212,350 | 2.147% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,959,108 | 1.855% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,992,227 | 1.630% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,709,566 | 1.564% | 5% |

## Economics

- **SOL:** $71.58 (-0.07% 24h, -17.18% 7d, -30.74% 30d). Market cap $42.36B, 24h volume $2.59B (6.12% of cap). Price source: `coingecko`.
- **TVL:** $4.75B across 341 protocols - rank #3 of 423 chains, 6.64% of all tracked chain TVL. -6.57% over 7d, -60.1% from its ATH.
- **Stablecoins:** $14.33B circulating on Solana (-0.06% 7d) - $3.02 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.38B in 24h, $9.58B over 7d across 142 venues. Volume/TVL turnover 0.291x per day.
- **REV (chain fees):** $7.25M in 24h, $303.34M over 30d. Retained chain revenue $2.46M (34.0% of fees). Annualised fees are 6.25% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,684,223 SOL circulating of 637,676,709 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.34B | -1.6% | -12.7% |
| 2 | Kamino Lend | Lending | $1.14B | +0.3% | -2.7% |
| 3 | Jupiter Lend | Lending | $955.47M | +3.2% | +5.1% |
| 4 | Raydium AMM | Dexs | $831.17M | -0.5% | -14.5% |
| 5 | Binance Staked SOL | Liquid Staking | $737.33M | -2.5% | -21.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $726.26M | -0.9% | -17.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $581.55M | +0.6% | -10.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $369.98M | -0.8% | -16.1% |
| 9 | Sentora Curator | Risk Curators | $358.63M | +0.1% | -4.3% |
| 10 | OnRe | RWA | $295.87M | -2.1% | -4.4% |
| 11 | Forward Industries SOL | Liquid Staking | $289.67M | -0.5% | +6.3% |
| 12 | CCIP | Bridge | $276.29M | -0.7% | +4.4% |

The top five protocols hold 41.3% of Solana's tracked TVL. Summed across all 341 protocols the total is $12.11B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.3% · Lending 19.0% · Dexs 14.8% · Derivatives 5.3% · RWA 4.8% · Risk Curators 4.2%

### Tokenised assets

$835.86M of tokenised real-world assets and equities are locked on Solana - 6.902% of chain TVL.

- OnRe (RWA): $295.87M
- Huma (RWA): $236.73M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $40.22M
- Plume Vaults (RWA): $38.11M

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

### Change over 24h (vs run at 2026-11-16T03:28:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,633.48 | 1,790.21 | +9.59% |
| Average non-vote TPS | 1,633.48 | 1,790.21 | +9.59% |
| Average slot time (ms) | 214.30 | 214.50 | +0.09% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 38.00 | 37.00 | -2.63% |
| Solana TVL | 4,706,399,962.00 | 4,749,281,028.00 | +0.91% |
| SOL price | 72.23 | 71.58 | -0.90% |
| Stablecoin supply | 14,340,765,034.00 | 14,334,893,337.00 | -0.04% |
| 24h DEX volume | 1,543,698,435.09 | 1,381,573,830.86 | -10.50% |
| 24h chain fees | 7,303,225.20 | 7,253,029.76 | -0.69% |

### Change over 7d (vs run at 2026-11-10T00:55:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,627.58 | 1,790.21 | +9.99% |
| Average non-vote TPS | 1,627.58 | 1,790.21 | +9.99% |
| Average slot time (ms) | 214.40 | 214.50 | +0.05% |
| Active validators | 657.00 | 662.00 | +0.76% |
| Delinquent validators | 41.00 | 37.00 | -9.76% |
| Solana TVL | 5,091,379,326.00 | 4,749,281,028.00 | -6.72% |
| SOL price | 86.31 | 71.58 | -17.07% |
| Stablecoin supply | 15,064,954,013.00 | 14,334,893,337.00 | -4.85% |
| 24h DEX volume | 1,204,191,616.64 | 1,381,573,830.86 | +14.73% |
| 24h chain fees | 8,676,028.36 | 7,253,029.76 | -16.40% |

### Change over 30d (vs run at 2026-10-17T19:45:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,823.29 | 1,790.21 | -62.88% |
| Average non-vote TPS | 1,758.64 | 1,790.21 | +1.80% |
| Average slot time (ms) | 217.70 | 214.50 | -1.47% |
| Active validators | 670.00 | 662.00 | -1.19% |
| Delinquent validators | 11.00 | 37.00 | +236.36% |
| Solana TVL | 5,922,304,891.00 | 4,749,281,028.00 | -19.81% |
| SOL price | 104.07 | 71.58 | -31.22% |
| Stablecoin supply | 16,030,558,263.00 | 14,334,893,337.00 | -10.58% |
| 24h DEX volume | 2,168,129,752.12 | 1,381,573,830.86 | -36.28% |
| 24h chain fees | 12,431,928.33 | 7,253,029.76 | -41.66% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.8s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
