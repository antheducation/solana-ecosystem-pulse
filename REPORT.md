# Solana Ecosystem Pulse

**Generated:** 2026-11-11T03:26:56Z · **Schema:** `1.0.0` · **Collection time:** 22.3s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $83.46 | -2.64% |
| Market cap | $49.36B | rank #7 |
| Total value locked | $5.06B | -0.27% |
| Stablecoin supply | $14.78B | -0.34% |
| DEX volume (24h) | $1.34B | -10.18% |
| Chain fees / REV (24h) | $8.16M | -11.03% |
| Non-vote TPS (1h avg) | 1,880 | peak 2,385 total |
| Active validators | 658 | 41 delinquent |
| Epoch 1083 | 26.84% complete | 316,032 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Delinquent validators is above its recent norm | Current 41.00 sits 3.0 sigma above the median of the last 128 runs (14.00, +192.9%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,879.6 average over the last 60 minutes; 1,489.4 in the latest sample.
- **Total TPS:** 1,879.6 average, 2,384.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.7 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 445,988,543 at absolute slot 467,971,968.
- **Epoch 1083:** slot 115,968 of 432,000 (26.84% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.562% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 153 ms |
| `solana-rpc.publicnode.com` | yes | 120 ms |
| `api.mainnet.solana.com` | yes | 198 ms |

## Validators & stake

- **658 active** validators, **41 delinquent** (5.87% by count, 0.230% by stake).
- **Total stake:** 433,423,964 SOL ($36.17B); stake rate 68.00% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.62% and top 33 hold 46.58% of active stake.
- **Commission:** median 5.0%, mean 12.63%; 221 validators at 0% and 60 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,764,485 | 3.877% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,564,685 | 3.831% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,031,625 | 3.014% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,254 | 2.340% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,644,051 | 2.230% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,571,015 | 2.213% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,231,999 | 2.135% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,814,330 | 1.807% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,248 | 1.616% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,729,845 | 1.556% | 5% |

## Economics

- **SOL:** $83.46 (-2.64% 24h, -8.25% 7d, -25.45% 30d). Market cap $49.36B, 24h volume $2.95B (5.97% of cap). Price source: `coingecko`.
- **TVL:** $5.06B across 343 protocols - rank #3 of 423 chains, 6.51% of all tracked chain TVL. -6.62% over 7d, -60.4% from its ATH.
- **Stablecoins:** $14.78B circulating on Solana (-1.58% 7d) - $2.92 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.34B in 24h, $10.16B over 7d across 141 venues. Volume/TVL turnover 0.264x per day.
- **REV (chain fees):** $8.16M in 24h, $330.57M over 30d. Retained chain revenue $2.58M (31.6% of fees). Annualised fees are 6.04% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,408,529 SOL circulating of 637,372,031 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -3.2% | -8.6% |
| 2 | Kamino Lend | Lending | $1.16B | -0.8% | -5.3% |
| 3 | Jupiter Lend | Lending | $964.92M | +6.6% | -4.5% |
| 4 | Raydium AMM | Dexs | $946.94M | -3.4% | -8.5% |
| 5 | Binance Staked SOL | Liquid Staking | $903.05M | -3.8% | -11.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $851.61M | -3.0% | -9.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $631.63M | -2.1% | -6.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $425.37M | -3.3% | -8.7% |
| 9 | Sentora Curator | Risk Curators | $374.36M | -0.0% | +0.2% |
| 10 | OnRe | RWA | $309.28M | -0.0% | +0.6% |
| 11 | Marinade Native | Staking Pool | $287.18M | -5.6% | -13.6% |
| 12 | Orca DEX | Dexs | $270.98M | -2.5% | -3.7% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.30B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.8% · Lending 17.7% · Dexs 15.0% · Derivatives 5.2% · RWA 4.4% · Risk Curators 4.0%

### Tokenised assets

$844.77M of tokenised real-world assets and equities are locked on Solana - 6.350% of chain TVL.

- OnRe (RWA): $309.28M
- Huma (RWA): $225.89M
- Solstice (Basis Trading): $201.10M
- JupUSD (Basis Trading): $43.76M
- Plume Vaults (RWA): $36.89M

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

### Change over 24h (vs run at 2026-11-10T00:55:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,627.58 | 1,879.61 | +15.48% |
| Average non-vote TPS | 1,627.58 | 1,879.61 | +15.48% |
| Average slot time (ms) | 214.40 | 214.70 | +0.14% |
| Active validators | 657.00 | 658.00 | +0.15% |
| Delinquent validators | 41.00 | 41.00 | +0.00% |
| Solana TVL | 5,091,379,326.00 | 5,057,543,658.00 | -0.66% |
| SOL price | 86.31 | 83.46 | -3.30% |
| Stablecoin supply | 15,064,954,013.00 | 14,784,030,341.00 | -1.86% |
| 24h DEX volume | 1,204,191,616.64 | 1,336,261,741.34 | +10.97% |
| 24h chain fees | 8,676,028.36 | 8,164,222.84 | -5.90% |

### Change over 7d (vs run at 2026-11-04T03:36:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,159.62 | 1,879.61 | -12.97% |
| Average non-vote TPS | 2,159.62 | 1,879.61 | -12.97% |
| Average slot time (ms) | 214.00 | 214.70 | +0.33% |
| Active validators | 666.00 | 658.00 | -1.20% |
| Delinquent validators | 27.00 | 41.00 | +51.85% |
| Solana TVL | 5,411,706,032.00 | 5,057,543,658.00 | -6.54% |
| SOL price | 91.05 | 83.46 | -8.34% |
| Stablecoin supply | 14,901,850,212.00 | 14,784,030,341.00 | -0.79% |
| 24h DEX volume | 1,873,448,962.90 | 1,336,261,741.34 | -28.67% |
| 24h chain fees | 11,428,987.75 | 8,164,222.84 | -28.57% |

### Change over 30d (vs run at 2026-10-11T21:08:31Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.95 | 1,879.61 | -62.22% |
| Average non-vote TPS | 1,917.24 | 1,879.61 | -1.96% |
| Average slot time (ms) | 218.90 | 214.70 | -1.92% |
| Active validators | 672.00 | 658.00 | -2.08% |
| Delinquent validators | 9.00 | 41.00 | +355.56% |
| Solana TVL | 6,251,230,542.00 | 5,057,543,658.00 | -19.10% |
| SOL price | 110.93 | 83.46 | -24.76% |
| Stablecoin supply | 16,405,817,670.00 | 14,784,030,341.00 | -9.89% |
| 24h DEX volume | 1,286,316,590.57 | 1,336,261,741.34 | +3.88% |
| 24h chain fees | 11,936,417.92 | 8,164,222.84 | -31.60% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.2s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
