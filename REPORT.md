# Solana Ecosystem Pulse

**Generated:** 2026-10-30T03:12:26Z · **Schema:** `1.0.0` · **Collection time:** 20.4s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $95.76 | -4.04% |
| Market cap | $56.49B | rank #7 |
| Total value locked | $5.38B | -5.07% |
| Stablecoin supply | $15.44B | -1.53% |
| DEX volume (24h) | $1.92B | +11.02% |
| Chain fees / REV (24h) | $11.36M | +13.37% |
| Non-vote TPS (1h avg) | 1,784 | peak 2,403 total |
| Active validators | 665 | 26 delinquent |
| Epoch 1072 | 5.77% complete | 407,072 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 127 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 17: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 1,784.28 sits 3.5 sigma below the median of the last 127 runs (4,422.32, -59.7%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 26.00 sits 3.1 sigma above the median of the last 127 runs (12.00, +116.7%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,784.3 average over the last 60 minutes; 1,853.5 in the latest sample.
- **Total TPS:** 1,784.3 average, 2,403.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.5 ms average (target 400 ms), worst 1-minute bucket 222.2 ms.
- **Block height:** 441,151,605 at absolute slot 463,128,928.
- **Epoch 1072:** slot 24,928 of 432,000 (5.77% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.579% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 114 ms |
| `solana-rpc.publicnode.com` | yes | 99 ms |
| `api.mainnet.solana.com` | yes | 142 ms |

## Validators & stake

- **665 active** validators, **26 delinquent** (3.76% by count, 1.084% by stake).
- **Total stake:** 435,357,093 SOL ($41.69B); stake rate 68.38% of total supply.
- **Concentration:** Nakamoto coefficient **17**; top 10 hold 24.90% and top 33 hold 46.57% of active stake.
- **Commission:** median 5.0%, mean 12.62%; 229 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,965,456 | 3.940% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,678,000 | 3.873% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,919,680 | 3.000% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,502,229 | 2.439% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,659,910 | 2.243% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,473,552 | 2.200% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,406 | 2.142% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,780,140 | 1.807% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,045,150 | 1.636% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,001,506 | 1.626% | 0% |

## Economics

- **SOL:** $95.76 (-4.04% 24h, -8.37% 7d, -19.97% 30d). Market cap $56.49B, 24h volume $5.20B (9.21% of cap). Price source: `coingecko`.
- **TVL:** $5.38B across 336 protocols - rank #5 of 420 chains, 6.39% of all tracked chain TVL. -8.79% over 7d, -58.5% from its ATH.
- **Stablecoins:** $15.44B circulating on Solana (-3.15% 7d) - $2.87 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.92B in 24h, $11.38B over 7d across 139 venues. Volume/TVL turnover 0.358x per day.
- **REV (chain fees):** $11.36M in 24h, $409.80M over 30d. Retained chain revenue $3.73M (32.8% of fees). Annualised fees are 7.34% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 590,040,107 SOL circulating of 636,700,411 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.67B | -7.5% | -8.0% |
| 2 | Kamino Lend | Lending | $1.19B | -6.0% | -8.6% |
| 3 | Raydium AMM | Dexs | $1.09B | -5.5% | -8.1% |
| 4 | Binance Staked SOL | Liquid Staking | $1.01B | -8.9% | -7.9% |
| 5 | Jito Liquid Staking | Liquid Staking | $981.56M | -6.3% | -8.9% |
| 6 | Jupiter Lend | Lending | $903.30M | -10.3% | -12.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $688.13M | -4.3% | -5.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $489.47M | -8.1% | -9.7% |
| 9 | Sentora Curator | Risk Curators | $380.32M | -0.9% | -9.1% |
| 10 | Marinade Native | Staking Pool | $341.12M | -7.0% | -8.2% |
| 11 | PumpSwap | Dexs | $325.44M | -5.4% | -6.4% |
| 12 | OnRe | RWA | $304.08M | -0.5% | +3.0% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 336 protocols the total is $14.54B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.1% · Dexs 15.4% · Derivatives 5.2% · RWA 4.1% · Risk Curators 3.8%

### Tokenised assets

$859.59M of tokenised real-world assets and equities are locked on Solana - 5.911% of chain TVL.

- OnRe (RWA): $304.08M
- Huma (RWA): $246.02M
- Solstice (Basis Trading): $201.19M
- JupUSD (Basis Trading): $41.99M
- Plume Vaults (RWA): $35.56M

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

- [SIMD-0714: SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [SIMD-0685: SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-29
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-29
- [SIMD-0568: SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-10-29
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-29T03:08:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,832.75 | 1,784.28 | -2.64% |
| Average non-vote TPS | 1,832.75 | 1,784.28 | -2.64% |
| Average slot time (ms) | 214.00 | 213.50 | -0.23% |
| Active validators | 665.00 | 665.00 | +0.00% |
| Delinquent validators | 24.00 | 26.00 | +8.33% |
| Solana TVL | 5,735,222,416.00 | 5,381,303,759.00 | -6.17% |
| SOL price | 99.93 | 95.76 | -4.17% |
| Stablecoin supply | 15,688,097,062.00 | 15,441,453,836.00 | -1.57% |
| 24h DEX volume | 1,624,511,734.06 | 1,924,354,203.70 | +18.46% |
| 24h chain fees | 10,348,131.32 | 11,363,568.43 | +9.81% |

### Change over 7d (vs run at 2026-10-23T02:15:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,827.63 | 1,784.28 | -2.37% |
| Average non-vote TPS | 1,827.62 | 1,784.28 | -2.37% |
| Average slot time (ms) | 211.60 | 213.50 | +0.90% |
| Active validators | 656.00 | 665.00 | +1.37% |
| Delinquent validators | 20.00 | 26.00 | +30.00% |
| Solana TVL | 5,871,527,154.00 | 5,381,303,759.00 | -8.35% |
| SOL price | 104.05 | 95.76 | -7.97% |
| Stablecoin supply | 15,965,967,694.00 | 15,441,453,836.00 | -3.29% |
| 24h DEX volume | 2,117,243,398.23 | 1,924,354,203.70 | -9.11% |
| 24h chain fees | 11,209,587.27 | 11,363,568.43 | +1.37% |

### Change over 30d (vs run at 2026-09-29T21:34:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,737.06 | 1,784.28 | -62.33% |
| Average non-vote TPS | 2,239.20 | 1,784.28 | -20.32% |
| Average slot time (ms) | 268.60 | 213.50 | -20.51% |
| Active validators | 673.00 | 665.00 | -1.19% |
| Delinquent validators | 10.00 | 26.00 | +160.00% |
| Solana TVL | 6,522,003,878.00 | 5,381,303,759.00 | -17.49% |
| SOL price | 118.62 | 95.76 | -19.27% |
| Stablecoin supply | 16,661,913,603.00 | 15,441,453,836.00 | -7.32% |
| 24h DEX volume | 2,662,061,803.25 | 1,924,354,203.70 | -27.71% |
| 24h chain fees | 17,514,749.35 | 11,363,568.43 | -35.12% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 20.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
