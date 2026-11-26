# Solana Ecosystem Pulse

**Generated:** 2026-11-26T15:54:33Z · **Schema:** `1.0.0` · **Collection time:** 22.6s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $70.91 | +5.10% |
| Market cap | $41.99B | rank #7 |
| Total value locked | $4.62B | +1.44% |
| Stablecoin supply | $13.34B | -1.36% |
| DEX volume (24h) | $1.51B | +3.72% |
| Chain fees / REV (24h) | $7.48M | +3.87% |
| Non-vote TPS (1h avg) | 1,997 | peak 3,364 total |
| Active validators | 657 | 31 delinquent |
| Epoch 1097 | 69.83% complete | 130,331 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 136 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is below its recent norm | Current 13,335,197,886.00 sits 3.0 sigma below the median of the last 136 runs (15,967,932,747.50, -16.5%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,996.6 average over the last 60 minutes; 1,904.4 in the latest sample.
- **Total TPS:** 1,996.6 average, 3,364.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 216.0 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 452,218,519 at absolute slot 474,205,669.
- **Epoch 1097:** slot 301,669 of 432,000 (69.83% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.540% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 334 ms |
| `solana-rpc.publicnode.com` | yes | 142 ms |
| `api.mainnet.solana.com` | yes | 195 ms |

## Validators & stake

- **657 active** validators, **31 delinquent** (4.51% by count, 0.032% by stake).
- **Total stake:** 423,675,927 SOL ($30.04B); stake rate 66.38% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.99% and top 33 hold 46.63% of active stake.
- **Commission:** median 5.0%, mean 13.24%; 218 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,805,000 | 3.968% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,814,431 | 3.734% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,430,859 | 2.935% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,236,589 | 2.417% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,910,258 | 2.340% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,394 | 2.270% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,281,563 | 2.191% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,032,075 | 1.896% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,971,305 | 1.646% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,740,287 | 1.591% | 5% |

## Economics

- **SOL:** $70.91 (+5.10% 24h, -5.28% 7d, -29.51% 30d). Market cap $41.99B, 24h volume $2.56B (6.10% of cap). Price source: `coingecko`.
- **TVL:** $4.62B across 345 protocols - rank #3 of 426 chains, 6.70% of all tracked chain TVL. -2.66% over 7d, -61.2% from its ATH.
- **Stablecoins:** $13.34B circulating on Solana (+2.14% 7d) - $2.89 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.51B in 24h, $10.88B over 7d across 146 venues. Volume/TVL turnover 0.327x per day.
- **REV (chain fees):** $7.48M in 24h, $275.33M over 30d. Retained chain revenue $2.79M (37.3% of fees). Annualised fees are 6.50% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 592,183,156 SOL circulating of 638,224,627 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.26B | +7.0% | -7.3% |
| 2 | Kamino Lend | Lending | $1.12B | +3.1% | -2.7% |
| 3 | Jupiter Lend | Lending | $947.18M | +3.4% | -1.2% |
| 4 | Raydium AMM | Dexs | $786.35M | +5.8% | -3.0% |
| 5 | Binance Staked SOL | Liquid Staking | $734.02M | +7.1% | -3.5% |
| 6 | Jito Liquid Staking | Liquid Staking | $717.63M | +6.3% | -3.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $571.71M | +4.5% | -2.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $374.42M | +6.7% | -0.3% |
| 9 | Sentora Curator | Risk Curators | $356.30M | +0.3% | -0.2% |
| 10 | OnRe | RWA | $290.01M | +0.0% | -1.0% |
| 11 | Forward Industries SOL | Liquid Staking | $280.33M | +6.5% | -3.5% |
| 12 | CCIP | Bridge | $267.91M | +0.1% | +2.5% |

The top five protocols hold 41.4% of Solana's tracked TVL. Summed across all 345 protocols the total is $11.72B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.2% · Lending 19.2% · Dexs 14.7% · Derivatives 5.4% · RWA 4.5% · Risk Curators 4.2%

### Tokenised assets

$780.98M of tokenised real-world assets and equities are locked on Solana - 6.664% of chain TVL.

- OnRe (RWA): $290.01M
- Huma (RWA): $226.65M
- Solstice (Basis Trading): $201.10M
- JupUSD (Basis Trading): $38.23M
- Solomon USDv (Basis Trading): $8.76M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) | 2026-11-25 | pre-release |
| [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) | 2026-11-19 | pre-release |
| [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) | 2026-11-06 | pre-release |
| [v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) | 2026-11-05 | stable |
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-26
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-26
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-11-25
- [template: encourage authors to drill into details](https://github.com/solana-foundation/solana-improvement-documents/pull/737) - updated 2026-11-25
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-11-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-11-25
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-24

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

### Change over 24h (vs run at 2026-11-25T16:18:44Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,791.23 | 1,996.59 | -28.47% |
| Average non-vote TPS | 2,791.23 | 1,996.59 | -28.47% |
| Average slot time (ms) | 214.80 | 216.00 | +0.56% |
| Active validators | 659.00 | 657.00 | -0.30% |
| Delinquent validators | 28.00 | 31.00 | +10.71% |
| Solana TVL | 4,442,324,165.00 | 4,618,435,898.00 | +3.96% |
| SOL price | 67.77 | 70.91 | +4.63% |
| Stablecoin supply | 13,517,716,588.00 | 13,335,197,886.00 | -1.35% |
| 24h DEX volume | 1,456,787,101.44 | 1,511,024,370.80 | +3.72% |
| 24h chain fees | 7,153,686.50 | 7,477,459.91 | +4.53% |

### Change over 7d (vs run at 2026-11-19T14:47:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,967.50 | 1,996.59 | +1.48% |
| Average non-vote TPS | 1,967.50 | 1,996.59 | +1.48% |
| Average slot time (ms) | 214.80 | 216.00 | +0.56% |
| Active validators | 659.00 | 657.00 | -0.30% |
| Delinquent validators | 26.00 | 31.00 | +19.23% |
| Solana TVL | 4,789,689,320.00 | 4,618,435,898.00 | -3.58% |
| SOL price | 75.26 | 70.91 | -5.78% |
| Stablecoin supply | 13,054,966,449.00 | 13,335,197,886.00 | +2.15% |
| 24h DEX volume | 1,815,395,819.31 | 1,511,024,370.80 | -16.77% |
| 24h chain fees | 10,954,885.63 | 7,477,459.91 | -31.74% |

### Change over 30d (vs run at 2026-10-27T21:31:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,359.98 | 1,996.59 | -15.40% |
| Average non-vote TPS | 2,359.97 | 1,996.59 | -15.40% |
| Average slot time (ms) | 213.80 | 216.00 | +1.03% |
| Active validators | 665.00 | 657.00 | -1.20% |
| Delinquent validators | 20.00 | 31.00 | +55.00% |
| Solana TVL | 5,721,042,380.00 | 4,618,435,898.00 | -19.27% |
| SOL price | 100.85 | 70.91 | -29.69% |
| Stablecoin supply | 15,763,185,048.00 | 13,335,197,886.00 | -15.40% |
| 24h DEX volume | 2,071,067,618.21 | 1,511,024,370.80 | -27.04% |
| 24h chain fees | 11,672,734.12 | 7,477,459.91 | -35.94% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.5s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
