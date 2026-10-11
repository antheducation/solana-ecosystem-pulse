# Solana Ecosystem Pulse

**Generated:** 2026-10-11T21:08:31Z · **Schema:** `1.0.0` · **Collection time:** 14.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.93 | +0.52% |
| Market cap | $65.34B | rank #7 |
| Total value locked | $6.25B | +0.95% |
| Stablecoin supply | $16.41B | -0.13% |
| DEX volume (24h) | $1.29B | -34.97% |
| Chain fees / REV (24h) | $11.94M | -14.21% |
| Non-vote TPS (1h avg) | 1,917 | peak 5,694 total |
| Active validators | 672 | 9 delinquent |
| Epoch 1055 | 7.85% complete | 398,106 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 103 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 218.90 sits 10.2 sigma below the median of the last 103 runs (268.60, -18.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,917.2 average over the last 60 minutes; 1,906.5 in the latest sample.
- **Total TPS:** 4,974.9 average, 5,693.6 peak. Consensus votes account for 61.5% of all transactions.
- **Slot time:** 218.9 ms average (target 400 ms), worst 1-minute bucket 227.3 ms.
- **Block height:** 433,831,020 at absolute slot 455,793,894.
- **Epoch 1055:** slot 33,894 of 432,000 (7.85% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.606% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 148 ms |
| `solana-rpc.publicnode.com` | yes | 79 ms |
| `api.mainnet.solana.com` | yes | 174 ms |

## Validators & stake

- **672 active** validators, **9 delinquent** (1.32% by count, 0.024% by stake).
- **Total stake:** 438,762,140 SOL ($48.67B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.48% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 12.80%; 232 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,781,885 | 4.054% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,956,122 | 3.638% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,320,023 | 2.809% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,147,729 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,755,463 | 2.452% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,332,199 | 2.127% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,248,710 | 2.108% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,607,284 | 1.734% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,811,094 | 1.553% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,422,658 | 1.464% | 0% |

## Economics

- **SOL:** $110.93 (+0.52% 24h, -8.53% 7d, +8.24% 30d). Market cap $65.34B, 24h volume $1.83B (2.80% of cap). Price source: `coingecko`.
- **TVL:** $6.25B across 336 protocols - rank #2 of 468 chains, 6.74% of all tracked chain TVL. -5.46% over 7d, -52.8% from its ATH.
- **Stablecoins:** $16.41B circulating on Solana (-2.82% 7d) - $2.62 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.29B in 24h, $13.93B over 7d across 130 venues. Volume/TVL turnover 0.206x per day.
- **REV (chain fees):** $11.94M in 24h, $475.16M over 30d. Retained chain revenue $4.53M (38.0% of fees). Annualised fees are 6.67% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,107,598 SOL circulating of 635,660,382 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.83B | +0.7% | -6.6% |
| 2 | Kamino Lend | Lending | $1.33B | +0.4% | -3.7% |
| 3 | Raydium AMM | Dexs | $1.26B | +1.0% | -7.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.16B | +1.1% | -6.6% |
| 5 | Jupiter Lend | Lending | $1.15B | +0.5% | -1.6% |
| 6 | Binance Staked SOL | Liquid Staking | $1.15B | +1.0% | -6.6% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $777.98M | +0.7% | -4.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $574.80M | +0.7% | -7.0% |
| 9 | Sentora Curator | Risk Curators | $492.03M | +0.2% | +31.3% |
| 10 | Marinade Native | Staking Pool | $412.29M | +0.9% | -7.3% |
| 11 | PumpSwap | Dexs | $374.18M | +1.7% | -6.5% |
| 12 | Orca DEX | Dexs | $311.91M | +0.5% | -2.3% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.69B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 16.6% · Dexs 15.5% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$883.95M of tokenised real-world assets and equities are locked on Solana - 5.295% of chain TVL.

- OnRe (RWA): $292.37M
- Huma (RWA): $255.40M
- Solstice (Basis Trading): $210.55M
- JupUSD (Basis Trading): $47.34M
- Plume Vaults (RWA): $33.58M

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

### Change over 24h (vs run at 2026-10-10T20:47:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,930.72 | 4,974.95 | +0.90% |
| Average non-vote TPS | 1,904.19 | 1,917.24 | +0.69% |
| Average slot time (ms) | 218.10 | 218.90 | +0.37% |
| Active validators | 675.00 | 672.00 | -0.44% |
| Delinquent validators | 5.00 | 9.00 | +80.00% |
| Solana TVL | 6,218,574,826.00 | 6,251,230,542.00 | +0.53% |
| SOL price | 110.30 | 110.93 | +0.57% |
| Stablecoin supply | 16,426,716,932.00 | 16,405,817,670.00 | -0.13% |
| 24h DEX volume | 1,978,097,665.91 | 1,286,316,590.57 | -34.97% |
| 24h chain fees | 13,913,073.58 | 11,936,417.92 | -14.21% |

### Change over 7d (vs run at 2026-10-04T20:33:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,626.16 | 4,974.95 | +7.54% |
| Average non-vote TPS | 2,127.97 | 1,917.24 | -9.90% |
| Average slot time (ms) | 267.70 | 218.90 | -18.23% |
| Active validators | 671.00 | 672.00 | +0.15% |
| Delinquent validators | 15.00 | 9.00 | -40.00% |
| Solana TVL | 6,715,169,332.00 | 6,251,230,542.00 | -6.91% |
| SOL price | 120.79 | 110.93 | -8.16% |
| Stablecoin supply | 16,881,830,613.00 | 16,405,817,670.00 | -2.82% |
| 24h DEX volume | 1,553,984,451.11 | 1,286,316,590.57 | -17.22% |
| 24h chain fees | 12,930,244.69 | 11,936,417.92 | -7.69% |

### Change over 30d (vs run at 2026-09-11T20:08:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,273.36 | 4,974.95 | +16.42% |
| Average non-vote TPS | 2,154.29 | 1,917.24 | -11.00% |
| Average slot time (ms) | 317.20 | 218.90 | -30.99% |
| Active validators | 678.00 | 672.00 | -0.88% |
| Delinquent validators | 12.00 | 9.00 | -25.00% |
| Solana TVL | 5,878,734,141.00 | 6,251,230,542.00 | +6.34% |
| SOL price | 102.41 | 110.93 | +8.32% |
| Stablecoin supply | 16,358,198,746.00 | 16,405,817,670.00 | +0.29% |
| 24h DEX volume | 2,921,890,110.01 | 1,286,316,590.57 | -55.98% |
| 24h chain fees | 14,614,973.44 | 11,936,417.92 | -18.33% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
