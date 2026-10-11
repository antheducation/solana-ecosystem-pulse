# Solana Ecosystem Pulse

**Generated:** 2026-10-11T11:42:05Z · **Schema:** `1.0.0` · **Collection time:** 11.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $109.42 | -0.17% |
| Market cap | $64.46B | rank #7 |
| Total value locked | $6.20B | +0.04% |
| Stablecoin supply | $16.40B | -0.14% |
| DEX volume (24h) | $1.29B | -34.97% |
| Chain fees / REV (24h) | $11.82M | -15.01% |
| Non-vote TPS (1h avg) | 1,446 | peak 4,914 total |
| Active validators | 674 | 6 delinquent |
| Epoch 1054 | 71.87% complete | 121,528 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 103 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 218.30 sits 16.2 sigma below the median of the last 103 runs (268.60, -18.7%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,445.7 average over the last 60 minutes; 1,819.9 in the latest sample.
- **Total TPS:** 4,516.8 average, 4,914.2 peak. Consensus votes account for 68.0% of all transactions.
- **Slot time:** 218.3 ms average (target 400 ms), worst 1-minute bucket 226.4 ms.
- **Block height:** 433,675,608 at absolute slot 455,638,472.
- **Epoch 1054:** slot 310,472 of 432,000 (71.87% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.608% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 221 ms |
| `solana-rpc.publicnode.com` | yes | 103 ms |
| `api.mainnet.solana.com` | yes | 108 ms |

## Validators & stake

- **674 active** validators, **6 delinquent** (0.88% by count, 0.003% by stake).
- **Total stake:** 438,737,964 SOL ($48.01B); stake rate 69.03% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.47% and top 33 hold 45.82% of active stake.
- **Commission:** median 5.0%, mean 13.07%; 231 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,775,444 | 4.052% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,954,957 | 3.637% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,356 | 2.807% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,145,934 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,754,664 | 2.451% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,328,689 | 2.126% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,266 | 2.106% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,603,786 | 1.733% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,810,142 | 1.552% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,421,774 | 1.464% | 0% |

## Economics

- **SOL:** $109.42 (-0.17% 24h, -9.77% 7d, +10.34% 30d). Market cap $64.46B, 24h volume $1.53B (2.37% of cap). Price source: `coingecko`.
- **TVL:** $6.20B across 336 protocols - rank #3 of 468 chains, 6.74% of all tracked chain TVL. -5.02% over 7d, -53.2% from its ATH.
- **Stablecoins:** $16.40B circulating on Solana (-2.83% 7d) - $2.65 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.29B in 24h, $13.93B over 7d across 130 venues. Volume/TVL turnover 0.208x per day.
- **REV (chain fees):** $11.82M in 24h, $475.05M over 30d. Retained chain revenue $4.53M (38.3% of fees). Annualised fees are 6.70% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,051,066 SOL circulating of 635,598,059 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.80B | -0.1% | -8.0% |
| 2 | Kamino Lend | Lending | $1.32B | -0.0% | -4.4% |
| 3 | Raydium AMM | Dexs | $1.24B | -0.3% | -8.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.14B | -0.1% | -8.3% |
| 5 | Jupiter Lend | Lending | $1.13B | -0.1% | -2.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.12B | -0.1% | -8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $768.29M | -0.1% | -5.3% |
| 8 | Jupiter Staked SOL | Liquid Staking | $565.48M | -0.3% | -8.5% |
| 9 | Sentora Curator | Risk Curators | $490.84M | -0.0% | +31.0% |
| 10 | Marinade Native | Staking Pool | $405.77M | +0.1% | -8.8% |
| 11 | PumpSwap | Dexs | $366.73M | -0.1% | -8.3% |
| 12 | Orca DEX | Dexs | $309.88M | +0.1% | -2.9% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.48B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 16.7% · Dexs 15.5% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$883.61M of tokenised real-world assets and equities are locked on Solana - 5.361% of chain TVL.

- OnRe (RWA): $292.36M
- Huma (RWA): $255.43M
- Solstice (Basis Trading): $210.56M
- JupUSD (Basis Trading): $47.33M
- Plume Vaults (RWA): $33.24M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) - Mon, 05 Oct 2026 00:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-11
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-11
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-10
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-10

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

### Change over 24h (vs run at 2026-10-10T11:28:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,325.84 | 4,516.76 | +4.41% |
| Average non-vote TPS | 1,230.91 | 1,445.69 | +17.45% |
| Average slot time (ms) | 217.40 | 218.30 | +0.41% |
| Active validators | 675.00 | 674.00 | -0.15% |
| Delinquent validators | 6.00 | 6.00 | +0.00% |
| Solana TVL | 6,201,943,177.00 | 6,195,850,647.00 | -0.10% |
| SOL price | 109.48 | 109.42 | -0.05% |
| Stablecoin supply | 16,426,938,969.00 | 16,404,382,269.00 | -0.14% |
| 24h DEX volume | 1,978,097,665.91 | 1,286,316,590.57 | -34.97% |
| 24h chain fees | 13,931,064.19 | 11,824,628.92 | -15.12% |

### Change over 7d (vs run at 2026-10-04T11:25:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,957.72 | 4,516.76 | +14.13% |
| Average non-vote TPS | 1,450.73 | 1,445.69 | -0.35% |
| Average slot time (ms) | 266.70 | 218.30 | -18.15% |
| Active validators | 671.00 | 674.00 | +0.45% |
| Delinquent validators | 15.00 | 6.00 | -60.00% |
| Solana TVL | 6,697,034,306.00 | 6,195,850,647.00 | -7.48% |
| SOL price | 121.32 | 109.42 | -9.81% |
| Stablecoin supply | 16,881,455,761.00 | 16,404,382,269.00 | -2.83% |
| 24h DEX volume | 1,553,984,451.11 | 1,286,316,590.57 | -17.22% |
| 24h chain fees | 12,836,094.54 | 11,824,628.92 | -7.88% |

### Change over 30d (vs run at 2026-09-11T20:08:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,273.36 | 4,516.76 | +5.70% |
| Average non-vote TPS | 2,154.29 | 1,445.69 | -32.89% |
| Average slot time (ms) | 317.20 | 218.30 | -31.18% |
| Active validators | 678.00 | 674.00 | -0.59% |
| Delinquent validators | 12.00 | 6.00 | -50.00% |
| Solana TVL | 5,878,734,141.00 | 6,195,850,647.00 | +5.39% |
| SOL price | 102.41 | 109.42 | +6.85% |
| Stablecoin supply | 16,358,198,746.00 | 16,404,382,269.00 | +0.28% |
| 24h DEX volume | 2,921,890,110.01 | 1,286,316,590.57 | -55.98% |
| 24h chain fees | 14,614,973.44 | 11,824,628.92 | -19.09% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
