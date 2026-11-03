# Solana Ecosystem Pulse

**Generated:** 2026-11-03T22:38:19Z · **Schema:** `1.0.0` · **Collection time:** 20.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $93.28 | +1.80% |
| Market cap | $55.06B | rank #7 |
| Total value locked | $5.46B | -0.32% |
| Stablecoin supply | $15.37B | -0.42% |
| DEX volume (24h) | $1.85B | +104.57% |
| Chain fees / REV (24h) | $11.21M | +32.69% |
| Non-vote TPS (1h avg) | 2,438 | peak 3,076 total |
| Active validators | 666 | 27 delinquent |
| Epoch 1076 | 54.96% complete | 194,565 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | DEX volume moved sharply (up 104.6% in 24h) | DEX volume changed +104.6% over the last day, past the 40% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,437.8 average over the last 60 minutes; 2,258.5 in the latest sample.
- **Total TPS:** 2,437.8 average, 3,076.0 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.0 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 443,090,051 at absolute slot 465,069,435.
- **Epoch 1076:** slot 237,435 of 432,000 (54.96% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.573% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 286 ms |
| `solana-rpc.publicnode.com` | yes | 103 ms |
| `api.mainnet.solana.com` | yes | 360 ms |

## Validators & stake

- **666 active** validators, **27 delinquent** (3.90% by count, 0.419% by stake).
- **Total stake:** 434,699,177 SOL ($40.55B); stake rate 68.25% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.77% and top 33 hold 46.54% of active stake.
- **Commission:** median 5.0%, mean 12.79%; 225 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,030,641 | 3.934% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,704,340 | 3.859% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,043,664 | 3.013% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,431,126 | 2.410% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,561,007 | 2.209% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,435,905 | 2.180% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,232,746 | 2.133% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,810 | 1.805% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,008,986 | 1.619% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,979,031 | 1.612% | 5% |

## Economics

- **SOL:** $93.28 (+1.80% 24h, -7.90% 7d, -23.01% 30d). Market cap $55.06B, 24h volume $2.02B (3.67% of cap). Price source: `coingecko`.
- **TVL:** $5.46B across 337 protocols - rank #3 of 420 chains, 6.61% of all tracked chain TVL. -3.69% over 7d, -57.7% from its ATH.
- **Stablecoins:** $15.37B circulating on Solana (-2.47% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.85B in 24h, $11.44B over 7d across 141 venues. Volume/TVL turnover 0.339x per day.
- **REV (chain fees):** $11.21M in 24h, $383.67M over 30d. Retained chain revenue $3.71M (33.1% of fees). Annualised fees are 7.43% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,265,839 SOL circulating of 636,944,476 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.65B | +2.5% | -7.0% |
| 2 | Kamino Lend | Lending | $1.23B | +1.7% | -1.7% |
| 3 | Raydium AMM | Dexs | $1.05B | +1.6% | -7.2% |
| 4 | Jupiter Lend | Lending | $1.02B | +3.8% | +0.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.02B | +1.9% | -5.0% |
| 6 | Jito Liquid Staking | Liquid Staking | $961.84M | +2.0% | -8.5% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $679.83M | +1.7% | -4.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $471.88M | +1.8% | -10.6% |
| 9 | Sentora Curator | Risk Curators | $373.80M | +0.2% | -2.7% |
| 10 | Marinade Native | Staking Pool | $335.66M | +2.2% | -7.5% |
| 11 | PumpSwap | Dexs | $321.97M | +3.4% | -2.2% |
| 12 | OnRe | RWA | $307.43M | +0.0% | +3.9% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 337 protocols the total is $14.47B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.2% · Dexs 15.2% · Derivatives 5.1% · RWA 4.0% · Risk Curators 3.7%

### Tokenised assets

$844.74M of tokenised real-world assets and equities are locked on Solana - 5.838% of chain TVL.

- OnRe (RWA): $307.43M
- Huma (RWA): $230.82M
- Solstice (Basis Trading): $201.40M
- JupUSD (Basis Trading): $39.08M
- Plume Vaults (RWA): $35.93M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-03
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-03
- [SIMD-0706: SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-03
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-02
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-11-03T00:07:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,658.77 | 2,437.77 | +46.96% |
| Average non-vote TPS | 1,658.77 | 2,437.77 | +46.96% |
| Average slot time (ms) | 214.20 | 215.00 | +0.37% |
| Active validators | 664.00 | 666.00 | +0.30% |
| Delinquent validators | 29.00 | 27.00 | -6.90% |
| Solana TVL | 5,362,623,249.00 | 5,464,894,047.00 | +1.91% |
| SOL price | 91.88 | 93.28 | +1.52% |
| Stablecoin supply | 15,440,330,579.00 | 15,373,798,720.00 | -0.43% |
| 24h DEX volume | 905,602,298.19 | 1,852,604,853.50 | +104.57% |
| 24h chain fees | 8,394,709.28 | 11,209,317.50 | +33.53% |

### Change over 7d (vs run at 2026-10-27T21:31:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,359.98 | 2,437.77 | +3.30% |
| Average non-vote TPS | 2,359.97 | 2,437.77 | +3.30% |
| Average slot time (ms) | 213.80 | 215.00 | +0.56% |
| Active validators | 665.00 | 666.00 | +0.15% |
| Delinquent validators | 20.00 | 27.00 | +35.00% |
| Solana TVL | 5,721,042,380.00 | 5,464,894,047.00 | -4.48% |
| SOL price | 100.85 | 93.28 | -7.51% |
| Stablecoin supply | 15,763,185,048.00 | 15,373,798,720.00 | -2.47% |
| 24h DEX volume | 2,071,067,618.21 | 1,852,604,853.50 | -10.55% |
| 24h chain fees | 11,672,734.12 | 11,209,317.50 | -3.97% |

### Change over 30d (vs run at 2026-10-04T20:33:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,626.16 | 2,437.77 | -47.30% |
| Average non-vote TPS | 2,127.97 | 2,437.77 | +14.56% |
| Average slot time (ms) | 267.70 | 215.00 | -19.69% |
| Active validators | 671.00 | 666.00 | -0.75% |
| Delinquent validators | 15.00 | 27.00 | +80.00% |
| Solana TVL | 6,715,169,332.00 | 5,464,894,047.00 | -18.62% |
| SOL price | 120.79 | 93.28 | -22.78% |
| Stablecoin supply | 16,881,830,613.00 | 15,373,798,720.00 | -8.93% |
| 24h DEX volume | 1,553,984,451.11 | 1,852,604,853.50 | +19.22% |
| 24h chain fees | 12,930,244.69 | 11,209,317.50 | -13.31% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
