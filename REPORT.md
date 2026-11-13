# Solana Ecosystem Pulse

**Generated:** 2026-11-13T03:50:10Z · **Schema:** `1.0.0` · **Collection time:** 19.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $78.76 | -5.32% |
| Market cap | $46.59B | rank #7 |
| Total value locked | $5.02B | -0.74% |
| Stablecoin supply | $14.37B | +1.05% |
| DEX volume (24h) | $1.51B | -6.60% |
| Chain fees / REV (24h) | $8.49M | -16.53% |
| Non-vote TPS (1h avg) | 2,245 | peak 3,140 total |
| Active validators | 659 | 40 delinquent |
| Epoch 1085 | 14.36% complete | 369,979 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 128 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,245.4 average over the last 60 minutes; 1,969.5 in the latest sample.
- **Total TPS:** 2,245.4 average, 3,140.1 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.8 ms average (target 400 ms), worst 1-minute bucket 220.6 ms.
- **Block height:** 446,797,492 at absolute slot 468,782,021.
- **Epoch 1085:** slot 62,021 of 432,000 (14.36% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.559% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 193 ms |
| `solana-rpc.publicnode.com` | yes | 63 ms |
| `api.mainnet.solana.com` | yes | 119 ms |

## Validators & stake

- **659 active** validators, **40 delinquent** (5.72% by count, 0.132% by stake).
- **Total stake:** 432,410,499 SOL ($34.06B); stake rate 67.83% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.58% and top 33 hold 46.41% of active stake.
- **Commission:** median 5.0%, mean 12.46%; 223 validators at 0% and 59 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,815,755 | 3.894% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,140,175 | 3.738% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,976,229 | 3.005% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,117,722 | 2.343% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,699,456 | 2.246% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,578,398 | 2.218% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,076 | 2.140% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,863,387 | 1.821% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,989,060 | 1.618% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,712,617 | 1.554% | 5% |

## Economics

- **SOL:** $78.76 (-5.32% 24h, -12.71% 7d, -26.86% 30d). Market cap $46.59B, 24h volume $2.38B (5.12% of cap). Price source: `coingecko`.
- **TVL:** $5.02B across 343 protocols - rank #3 of 423 chains, 6.56% of all tracked chain TVL. -5.00% over 7d, -60.0% from its ATH.
- **Stablecoins:** $14.37B circulating on Solana (-1.42% 7d) - $2.86 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.51B in 24h, $8.72B over 7d across 141 venues. Volume/TVL turnover 0.301x per day.
- **REV (chain fees):** $8.49M in 24h, $325.37M over 30d. Retained chain revenue $3.12M (36.7% of fees). Annualised fees are 6.65% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,511,160 SOL circulating of 637,493,881 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.44B | -2.8% | -8.8% |
| 2 | Kamino Lend | Lending | $1.18B | +1.6% | -1.5% |
| 3 | Jupiter Lend | Lending | $958.73M | -0.8% | -2.6% |
| 4 | Raydium AMM | Dexs | $933.02M | -1.5% | -7.0% |
| 5 | Binance Staked SOL | Liquid Staking | $878.66M | -3.1% | -9.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $826.76M | -2.7% | -10.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $618.50M | -2.0% | -6.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $413.37M | -2.6% | -8.9% |
| 9 | Sentora Curator | Risk Curators | $363.54M | -2.7% | -2.7% |
| 10 | OnRe | RWA | $309.36M | -0.0% | +0.3% |
| 11 | Marinade Native | Staking Pool | $272.98M | -5.3% | -15.8% |
| 12 | Orca DEX | Dexs | $268.88M | +0.7% | -5.1% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 343 protocols the total is $13.07B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 41.4% · Lending 18.1% · Dexs 15.0% · Derivatives 5.2% · RWA 4.5% · Risk Curators 4.0%

### Tokenised assets

$840.67M of tokenised real-world assets and equities are locked on Solana - 6.430% of chain TVL.

- OnRe (RWA): $309.36M
- Huma (RWA): $225.21M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $41.13M
- Plume Vaults (RWA): $37.05M

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

- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-12
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-12
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-11-09
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09

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

### Change over 24h (vs run at 2026-11-12T04:37:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,577.09 | 2,245.44 | +42.38% |
| Average non-vote TPS | 1,577.09 | 2,245.44 | +42.38% |
| Average slot time (ms) | 214.80 | 215.80 | +0.47% |
| Active validators | 661.00 | 659.00 | -0.30% |
| Delinquent validators | 37.00 | 40.00 | +8.11% |
| Solana TVL | 5,056,620,554.00 | 5,024,451,399.00 | -0.64% |
| SOL price | 82.85 | 78.76 | -4.94% |
| Stablecoin supply | 14,227,548,633.00 | 14,374,630,148.00 | +1.03% |
| 24h DEX volume | 1,636,935,274.95 | 1,511,008,694.77 | -7.69% |
| 24h chain fees | 9,320,608.90 | 8,490,485.20 | -8.91% |

### Change over 7d (vs run at 2026-11-06T03:54:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,607.08 | 2,245.44 | +39.72% |
| Average non-vote TPS | 1,607.08 | 2,245.44 | +39.72% |
| Average slot time (ms) | 214.00 | 215.80 | +0.84% |
| Active validators | 663.00 | 659.00 | -0.60% |
| Delinquent validators | 31.00 | 40.00 | +29.03% |
| Solana TVL | 5,291,216,002.00 | 5,024,451,399.00 | -5.04% |
| SOL price | 89.73 | 78.76 | -12.23% |
| Stablecoin supply | 15,032,733,630.00 | 14,374,630,148.00 | -4.38% |
| 24h DEX volume | 2,182,575,633.20 | 1,511,008,694.77 | -30.77% |
| 24h chain fees | 9,790,369.15 | 8,490,485.20 | -13.28% |

### Change over 30d (vs run at 2026-10-13T22:01:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,063.39 | 2,245.44 | -55.65% |
| Average non-vote TPS | 1,990.01 | 2,245.44 | +12.84% |
| Average slot time (ms) | 217.80 | 215.80 | -0.92% |
| Active validators | 673.00 | 659.00 | -2.08% |
| Delinquent validators | 7.00 | 40.00 | +471.43% |
| Solana TVL | 6,063,416,281.00 | 5,024,451,399.00 | -17.13% |
| SOL price | 107.01 | 78.76 | -26.40% |
| Stablecoin supply | 16,241,793,471.00 | 14,374,630,148.00 | -11.50% |
| 24h DEX volume | 2,231,842,381.02 | 1,511,008,694.77 | -32.30% |
| 24h chain fees | 13,103,539.72 | 8,490,485.20 | -35.20% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 19.8s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
