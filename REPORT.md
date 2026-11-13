# Solana Ecosystem Pulse

**Generated:** 2026-11-13T22:57:36Z · **Schema:** `1.0.0` · **Collection time:** 22.1s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $78.20 | -3.90% |
| Market cap | $46.28B | rank #7 |
| Total value locked | $4.96B | -2.48% |
| Stablecoin supply | $14.38B | +1.06% |
| DEX volume (24h) | $1.50B | -7.06% |
| Chain fees / REV (24h) | $8.07M | -21.29% |
| Non-vote TPS (1h avg) | 2,140 | peak 3,250 total |
| Active validators | 661 | 38 delinquent |
| Epoch 1085 | 88.35% complete | 50,341 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,140.3 average over the last 60 minutes; 1,943.3 in the latest sample.
- **Total TPS:** 2,140.3 average, 3,249.8 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 215.2 ms average (target 400 ms), worst 1-minute bucket 223.0 ms.
- **Block height:** 447,116,809 at absolute slot 469,101,659.
- **Epoch 1085:** slot 381,659 of 432,000 (88.35% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.559% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 208 ms |
| `solana-rpc.publicnode.com` | yes | 137 ms |
| `api.mainnet.solana.com` | yes | 149 ms |

## Validators & stake

- **661 active** validators, **38 delinquent** (5.44% by count, 0.132% by stake).
- **Total stake:** 432,410,499 SOL ($33.81B); stake rate 67.83% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.58% and top 33 hold 46.41% of active stake.
- **Commission:** median 5.0%, mean 12.73%; 223 validators at 0% and 61 at 100%.

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

- **SOL:** $78.20 (-3.90% 24h, -13.33% 7d, -25.26% 30d). Market cap $46.28B, 24h volume $3.49B (7.53% of cap). Price source: `coingecko`.
- **TVL:** $4.96B across 343 protocols - rank #3 of 423 chains, 6.61% of all tracked chain TVL. -6.64% over 7d, -60.6% from its ATH.
- **Stablecoins:** $14.38B circulating on Solana (-1.41% 7d) - $2.90 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.50B in 24h, $9.39B over 7d across 141 venues. Volume/TVL turnover 0.303x per day.
- **REV (chain fees):** $8.07M in 24h, $327.63M over 30d. Retained chain revenue $3.00M (37.1% of fees). Annualised fees are 6.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,512,465 SOL circulating of 637,493,538 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | +2.4% | -6.3% |
| 2 | Kamino Lend | Lending | $1.17B | -0.9% | -2.2% |
| 3 | Jupiter Lend | Lending | $945.53M | -0.5% | -3.9% |
| 4 | Raydium AMM | Dexs | $910.96M | -2.0% | -9.2% |
| 5 | Binance Staked SOL | Liquid Staking | $851.75M | -3.9% | -12.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $802.45M | -3.4% | -12.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $604.39M | -2.7% | -8.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $401.74M | -3.2% | -11.5% |
| 9 | Forward Industries SOL | Liquid Staking | $317.36M | +23.6% | +12.5% |
| 10 | OnRe | RWA | $308.88M | -0.1% | +0.1% |
| 11 | CCIP | Bridge | $287.00M | +8.8% | +12.3% |
| 12 | PumpSwap | Dexs | $268.42M | -0.5% | -13.2% |

The top five protocols hold 41.5% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.93B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.0% · Lending 18.1% · Dexs 14.9% · Derivatives 5.1% · RWA 4.7% · Bridge 3.8%

### Tokenised assets

$864.36M of tokenised real-world assets and equities are locked on Solana - 6.686% of chain TVL.

- OnRe (RWA): $308.88M
- Huma (RWA): $249.06M
- Solstice (Basis Trading): $201.01M
- JupUSD (Basis Trading): $40.92M
- Plume Vaults (RWA): $37.06M

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

### Change over 24h (vs run at 2026-11-12T22:55:56Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,817.36 | 2,140.34 | +17.77% |
| Average non-vote TPS | 1,817.36 | 2,140.34 | +17.77% |
| Average slot time (ms) | 215.30 | 215.20 | -0.05% |
| Active validators | 660.00 | 661.00 | +0.15% |
| Delinquent validators | 38.00 | 38.00 | +0.00% |
| Solana TVL | 5,021,601,661.00 | 4,958,650,115.00 | -1.25% |
| SOL price | 81.36 | 78.20 | -3.88% |
| Stablecoin supply | 14,223,412,853.00 | 14,376,185,613.00 | +1.07% |
| 24h DEX volume | 1,617,758,399.95 | 1,503,485,412.77 | -7.06% |
| 24h chain fees | 10,185,070.88 | 8,074,998.20 | -20.72% |

### Change over 7d (vs run at 2026-11-06T22:28:12Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,010.28 | 2,140.34 | +6.47% |
| Average non-vote TPS | 2,010.28 | 2,140.34 | +6.47% |
| Average slot time (ms) | 214.70 | 215.20 | +0.23% |
| Active validators | 659.00 | 661.00 | +0.30% |
| Delinquent validators | 37.00 | 38.00 | +2.70% |
| Solana TVL | 5,241,110,141.00 | 4,958,650,115.00 | -5.39% |
| SOL price | 90.17 | 78.20 | -13.27% |
| Stablecoin supply | 15,033,474,849.00 | 14,376,185,613.00 | -4.37% |
| 24h DEX volume | 2,198,364,299.20 | 1,503,485,412.77 | -31.61% |
| 24h chain fees | 9,708,551.35 | 8,074,998.20 | -16.83% |

### Change over 30d (vs run at 2026-10-14T21:02:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,462.84 | 2,140.34 | -60.82% |
| Average non-vote TPS | 2,373.93 | 2,140.34 | -9.84% |
| Average slot time (ms) | 216.90 | 215.20 | -0.78% |
| Active validators | 673.00 | 661.00 | -1.78% |
| Delinquent validators | 5.00 | 38.00 | +660.00% |
| Solana TVL | 5,960,534,531.00 | 4,958,650,115.00 | -16.81% |
| SOL price | 104.03 | 78.20 | -24.83% |
| Stablecoin supply | 16,320,492,053.00 | 14,376,185,613.00 | -11.91% |
| 24h DEX volume | 2,495,170,004.38 | 1,503,485,412.77 | -39.74% |
| 24h chain fees | 11,775,288.16 | 8,074,998.20 | -31.42% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 22.0s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
