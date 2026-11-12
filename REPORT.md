# Solana Ecosystem Pulse

**Generated:** 2026-11-12T04:37:02Z · **Schema:** `1.0.0` · **Collection time:** 19.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $82.85 | -0.33% |
| Market cap | $49.00B | rank #7 |
| Total value locked | $5.06B | +0.08% |
| Stablecoin supply | $14.23B | -0.51% |
| DEX volume (24h) | $1.64B | +22.25% |
| Chain fees / REV (24h) | $9.32M | +10.97% |
| Non-vote TPS (1h avg) | 1,577 | peak 2,273 total |
| Active validators | 661 | 37 delinquent |
| Epoch 1084 | 24.47% complete | 326,309 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,577.1 average over the last 60 minutes; 1,394.6 in the latest sample.
- **Total TPS:** 1,577.1 average, 2,272.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.8 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 446,409,599 at absolute slot 468,393,691.
- **Epoch 1084:** slot 105,691 of 432,000 (24.47% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.560% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 152 ms |
| `solana-rpc.publicnode.com` | yes | 119 ms |
| `api.mainnet.solana.com` | yes | 194 ms |

## Validators & stake

- **661 active** validators, **37 delinquent** (5.30% by count, 0.158% by stake).
- **Total stake:** 433,416,361 SOL ($35.91B); stake rate 67.99% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.52% and top 33 hold 46.48% of active stake.
- **Commission:** median 5.0%, mean 12.73%; 223 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,789,054 | 3.880% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,119,194 | 3.725% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,026,247 | 3.010% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,116,092 | 2.338% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,681,376 | 2.237% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,580,180 | 2.214% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,230,504 | 2.133% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,840,792 | 1.812% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,981 | 1.615% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,730,421 | 1.555% | 5% |

## Economics

- **SOL:** $82.85 (-0.33% 24h, -13.92% 7d, -22.83% 30d). Market cap $49.00B, 24h volume $2.10B (4.29% of cap). Price source: `coingecko`.
- **TVL:** $5.06B across 343 protocols - rank #3 of 423 chains, 6.48% of all tracked chain TVL. -9.12% over 7d, -60.4% from its ATH.
- **Stablecoins:** $14.23B circulating on Solana (-3.31% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.64B in 24h, $9.41B over 7d across 141 venues. Volume/TVL turnover 0.324x per day.
- **REV (chain fees):** $9.32M in 24h, $326.06M over 30d. Retained chain revenue $3.41M (36.6% of fees). Annualised fees are 6.94% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,457,046 SOL circulating of 637,432,884 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -0.2% | -12.0% |
| 2 | Kamino Lend | Lending | $1.16B | +0.3% | -6.8% |
| 3 | Jupiter Lend | Lending | $966.69M | -0.3% | -6.3% |
| 4 | Raydium AMM | Dexs | $947.16M | +0.0% | -11.8% |
| 5 | Binance Staked SOL | Liquid Staking | $906.56M | +0.2% | -13.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $852.52M | -0.3% | -14.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $631.56M | -0.1% | -9.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $424.90M | -0.0% | -12.2% |
| 9 | Sentora Curator | Risk Curators | $373.54M | -0.3% | +0.1% |
| 10 | OnRe | RWA | $309.37M | +0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $288.27M | +0.2% | -16.2% |
| 12 | PumpSwap | Dexs | $272.31M | +0.6% | -17.1% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.31B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.9% · Lending 17.7% · Dexs 14.9% · Derivatives 5.2% · RWA 4.4% · Risk Curators 4.0%

### Tokenised assets

$844.75M of tokenised real-world assets and equities are locked on Solana - 6.346% of chain TVL.

- OnRe (RWA): $309.37M
- Huma (RWA): $225.79M
- Solstice (Basis Trading): $201.11M
- JupUSD (Basis Trading): $43.69M
- Plume Vaults (RWA): $36.90M

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

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-10
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [docs(template): add required status and Advisory category hints](https://github.com/solana-foundation/solana-improvement-documents/pull/725) - updated 2026-11-06

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

### Change over 24h (vs run at 2026-11-11T03:26:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,879.61 | 1,577.09 | -16.09% |
| Average non-vote TPS | 1,879.61 | 1,577.09 | -16.09% |
| Average slot time (ms) | 214.70 | 214.80 | +0.05% |
| Active validators | 658.00 | 661.00 | +0.46% |
| Delinquent validators | 41.00 | 37.00 | -9.76% |
| Solana TVL | 5,057,543,658.00 | 5,056,620,554.00 | -0.02% |
| SOL price | 83.46 | 82.85 | -0.73% |
| Stablecoin supply | 14,784,030,341.00 | 14,227,548,633.00 | -3.76% |
| 24h DEX volume | 1,336,261,741.34 | 1,636,935,274.95 | +22.50% |
| 24h chain fees | 8,164,222.84 | 9,320,608.90 | +14.16% |

### Change over 7d (vs run at 2026-11-05T03:56:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,542.90 | 1,577.09 | +2.22% |
| Average non-vote TPS | 1,542.90 | 1,577.09 | +2.22% |
| Average slot time (ms) | 213.30 | 214.80 | +0.70% |
| Active validators | 662.00 | 661.00 | -0.15% |
| Delinquent validators | 31.00 | 37.00 | +19.35% |
| Solana TVL | 5,556,165,279.00 | 5,056,620,554.00 | -8.99% |
| SOL price | 96.39 | 82.85 | -14.05% |
| Stablecoin supply | 15,184,455,347.00 | 14,227,548,633.00 | -6.30% |
| 24h DEX volume | 2,222,398,076.94 | 1,636,935,274.95 | -26.34% |
| 24h chain fees | 10,960,459.01 | 9,320,608.90 | -14.96% |

### Change over 30d (vs run at 2026-10-12T23:52:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,094.70 | 1,577.09 | -69.04% |
| Average non-vote TPS | 2,039.01 | 1,577.09 | -22.65% |
| Average slot time (ms) | 218.80 | 214.80 | -1.83% |
| Active validators | 672.00 | 661.00 | -1.64% |
| Delinquent validators | 8.00 | 37.00 | +362.50% |
| Solana TVL | 6,087,233,347.00 | 5,056,620,554.00 | -16.93% |
| SOL price | 105.47 | 82.85 | -21.45% |
| Stablecoin supply | 16,359,920,349.00 | 14,227,548,633.00 | -13.03% |
| 24h DEX volume | 1,277,023,682.31 | 1,636,935,274.95 | +28.18% |
| 24h chain fees | 11,301,815.14 | 9,320,608.90 | -17.53% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 19.6s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
