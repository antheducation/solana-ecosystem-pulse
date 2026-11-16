# Solana Ecosystem Pulse

**Generated:** 2026-11-16T03:28:04Z · **Schema:** `1.0.0` · **Collection time:** 18.5s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $72.23 | +0.90% |
| Market cap | $42.74B | rank #7 |
| Total value locked | $4.71B | +1.04% |
| Stablecoin supply | $14.34B | +0.81% |
| DEX volume (24h) | $1.54B | -7.99% |
| Chain fees / REV (24h) | $7.30M | -7.09% |
| Non-vote TPS (1h avg) | 1,633 | peak 2,586 total |
| Active validators | 662 | 38 delinquent |
| Epoch 1087 | 91.81% complete | 35,381 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 129 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,633.5 average over the last 60 minutes; 1,226.0 in the latest sample.
- **Total TPS:** 1,633.5 average, 2,586.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 214.3 ms average (target 400 ms), worst 1-minute bucket 221.4 ms.
- **Block height:** 447,995,569 at absolute slot 469,980,619.
- **Epoch 1087:** slot 396,619 of 432,000 (91.81% complete).
- **Client:** agave `4.4.0`, feature set `2681577653`. Inflation 3.556% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 114 ms |
| `solana-rpc.publicnode.com` | yes | 69 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **662 active** validators, **38 delinquent** (5.43% by count, 0.084% by stake).
- **Total stake:** 429,328,621 SOL ($31.01B); stake rate 67.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.47% of active stake.
- **Commission:** median 5.0%, mean 12.74%; 220 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,927,749 | 3.946% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,404,544 | 3.824% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,614,561 | 2.941% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,141,932 | 2.364% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,754,208 | 2.274% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,640,656 | 2.247% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,204,466 | 2.146% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,943,264 | 1.852% | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,991,232 | 1.630% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,708,648 | 1.564% | 5% |

## Economics

- **SOL:** $72.23 (+0.90% 24h, -17.88% 7d, -30.82% 30d). Market cap $42.74B, 24h volume $3.42B (7.99% of cap). Price source: `coingecko`.
- **TVL:** $4.71B across 343 protocols - rank #3 of 423 chains, 6.58% of all tracked chain TVL. -8.16% over 7d, -60.4% from its ATH.
- **Stablecoins:** $14.34B circulating on Solana (-1.26% 7d) - $3.05 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.54B in 24h, $9.88B over 7d across 142 venues. Volume/TVL turnover 0.328x per day.
- **REV (chain fees):** $7.30M in 24h, $311.19M over 30d. Retained chain revenue $2.56M (35.0% of fees). Annualised fees are 6.24% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 591,628,878 SOL circulating of 637,615,621 total (92.79%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.34B | +0.8% | -12.8% |
| 2 | Kamino Lend | Lending | $1.13B | +1.6% | -3.5% |
| 3 | Jupiter Lend | Lending | $922.22M | +3.3% | +1.5% |
| 4 | Raydium AMM | Dexs | $832.00M | +2.8% | -15.6% |
| 5 | Binance Staked SOL | Liquid Staking | $748.41M | +0.5% | -21.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $724.07M | +4.5% | -19.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $572.94M | +0.6% | -11.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $373.01M | +1.8% | -16.3% |
| 9 | Sentora Curator | Risk Curators | $358.15M | +0.2% | -4.3% |
| 10 | OnRe | RWA | $302.32M | -0.4% | -2.3% |
| 11 | Forward Industries SOL | Liquid Staking | $288.17M | +0.9% | +5.1% |
| 12 | CCIP | Bridge | $278.01M | -0.2% | +4.8% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 343 protocols the total is $12.10B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.4% · Lending 18.7% · Dexs 14.8% · Derivatives 5.2% · RWA 4.8% · Risk Curators 4.2%

### Tokenised assets

$844.00M of tokenised real-world assets and equities are locked on Solana - 6.974% of chain TVL.

- OnRe (RWA): $302.32M
- Huma (RWA): $237.25M
- Solstice (Basis Trading): $201.05M
- JupUSD (Basis Trading): $40.26M
- Plume Vaults (RWA): $36.98M

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

- [Entry timestamp](https://github.com/solana-foundation/solana-improvement-documents/pull/732) - updated 2026-11-14
- [SIMD-0723: SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [rewards: Use live block commission collector](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-11-12
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-11-12
- [SIMD-0326: Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-11-09
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

### Change over 24h (vs run at 2026-11-15T03:28:23Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,657.93 | 1,633.48 | -1.47% |
| Average non-vote TPS | 1,657.93 | 1,633.48 | -1.47% |
| Average slot time (ms) | 215.40 | 214.30 | -0.51% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 37.00 | 38.00 | +2.70% |
| Solana TVL | 4,612,450,821.00 | 4,706,399,962.00 | +2.04% |
| SOL price | 71.61 | 72.23 | +0.87% |
| Stablecoin supply | 14,224,431,770.00 | 14,340,765,034.00 | +0.82% |
| 24h DEX volume | 1,614,007,307.70 | 1,543,698,435.09 | -4.36% |
| 24h chain fees | 8,186,168.20 | 7,303,225.20 | -10.79% |

### Change over 7d (vs run at 2026-11-09T03:18:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,452.40 | 1,633.48 | +12.47% |
| Average non-vote TPS | 1,452.39 | 1,633.48 | +12.47% |
| Average slot time (ms) | 215.00 | 214.30 | -0.33% |
| Active validators | 662.00 | 662.00 | +0.00% |
| Delinquent validators | 35.00 | 38.00 | +8.57% |
| Solana TVL | 5,134,576,425.00 | 4,706,399,962.00 | -8.34% |
| SOL price | 87.25 | 72.23 | -17.21% |
| Stablecoin supply | 15,064,026,289.00 | 14,340,765,034.00 | -4.80% |
| 24h DEX volume | 997,083,843.30 | 1,543,698,435.09 | +54.82% |
| 24h chain fees | 8,295,890.36 | 7,303,225.20 | -11.97% |

### Change over 30d (vs run at 2026-10-16T20:09:55Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,572.51 | 1,633.48 | -70.69% |
| Average non-vote TPS | 2,482.29 | 1,633.48 | -34.19% |
| Average slot time (ms) | 216.20 | 214.30 | -0.88% |
| Active validators | 671.00 | 662.00 | -1.34% |
| Delinquent validators | 9.00 | 38.00 | +322.22% |
| Solana TVL | 5,951,004,332.00 | 4,706,399,962.00 | -20.91% |
| SOL price | 103.59 | 72.23 | -30.27% |
| Stablecoin supply | 16,233,803,204.00 | 14,340,765,034.00 | -11.66% |
| 24h DEX volume | 2,539,283,878.03 | 1,543,698,435.09 | -39.21% |
| 24h chain fees | 12,783,602.89 | 7,303,225.20 | -42.87% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 18.4s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
