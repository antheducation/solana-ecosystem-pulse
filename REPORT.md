# Solana Ecosystem Pulse

**Generated:** 2026-10-10T20:47:16Z · **Schema:** `1.0.0` · **Collection time:** 16.4s · **Sources OK:** 39/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $110.30 | +1.37% |
| Market cap | $64.95B | rank #7 |
| Total value locked | $6.22B | +0.11% |
| Stablecoin supply | $16.43B | +0.28% |
| DEX volume (24h) | $1.98B | -25.21% |
| Chain fees / REV (24h) | $13.91M | -7.66% |
| Non-vote TPS (1h avg) | 1,904 | peak 5,472 total |
| Active validators | 675 | 5 delinquent |
| Epoch 1054 | 14.88% complete | 367,735 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 102 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 218.10 sits 16.6 sigma below the median of the last 102 runs (268.65, -18.8%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,904.2 average over the last 60 minutes; 1,707.7 in the latest sample.
- **Total TPS:** 4,930.7 average, 5,471.6 peak. Consensus votes account for 61.4% of all transactions.
- **Slot time:** 218.1 ms average (target 400 ms), worst 1-minute bucket 231.7 ms.
- **Block height:** 433,429,435 at absolute slot 455,392,265.
- **Epoch 1054:** slot 64,265 of 432,000 (14.88% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.608% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 163 ms |
| `solana-rpc.publicnode.com` | yes | 164 ms |
| `api.mainnet.solana.com` | yes | 192 ms |

## Validators & stake

- **675 active** validators, **5 delinquent** (0.74% by count, 0.002% by stake).
- **Total stake:** 438,737,964 SOL ($48.39B); stake rate 69.03% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.47% and top 33 hold 45.82% of active stake.
- **Commission:** median 5.0%, mean 12.90%; 233 validators at 0% and 64 at 100%.

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

- **SOL:** $110.30 (+1.37% 24h, -7.90% 7d, +10.66% 30d). Market cap $64.95B, 24h volume $1.56B (2.40% of cap). Price source: `coingecko`.
- **TVL:** $6.22B across 336 protocols - rank #2 of 468 chains, 6.73% of all tracked chain TVL. -6.13% over 7d, -53.0% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (-3.09% 7d) - $2.64 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.98B in 24h, $14.20B over 7d across 130 venues. Volume/TVL turnover 0.318x per day.
- **REV (chain fees):** $13.91M in 24h, $476.68M over 30d. Retained chain revenue $5.12M (36.8% of fees). Annualised fees are 7.82% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,848,389 SOL circulating of 635,598,700 total (92.64%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +1.2% | -7.2% |
| 2 | Kamino Lend | Lending | $1.33B | +0.4% | -4.0% |
| 3 | Raydium AMM | Dexs | $1.24B | +0.9% | -7.7% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.15B | +1.6% | -6.9% |
| 5 | Jupiter Lend | Lending | $1.14B | +0.5% | -5.2% |
| 6 | Binance Staked SOL | Liquid Staking | $1.13B | +1.4% | -7.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $770.81M | +0.4% | -4.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $569.91M | +1.4% | -7.1% |
| 9 | Sentora Curator | Risk Curators | $491.04M | -1.2% | +28.4% |
| 10 | Marinade Native | Staking Pool | $406.85M | +0.3% | -7.8% |
| 11 | PumpSwap | Dexs | $368.01M | +0.8% | -6.8% |
| 12 | Orca DEX | Dexs | $310.28M | +0.6% | -2.0% |

The top five protocols hold 40.3% of Solana's tracked TVL. Summed across all 336 protocols the total is $16.56B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 16.7% · Dexs 15.5% · Derivatives 5.2% · Risk Curators 4.2% · Staking Pool 3.9%

### Tokenised assets

$884.28M of tokenised real-world assets and equities are locked on Solana - 5.341% of chain TVL.

- OnRe (RWA): $292.67M
- Huma (RWA): $255.95M
- Solstice (Basis Trading): $210.55M
- JupUSD (Basis Trading): $47.34M
- Plume Vaults (RWA): $33.13M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) - Tue, 06 Oct 2026 02:00:00 GMT
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) - Mon, 05 Oct 2026 00:00:00 GMT
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT

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

### Change over 24h (vs run at 2026-10-09T21:56:06Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,940.51 | 4,930.72 | -0.20% |
| Average non-vote TPS | 1,872.44 | 1,904.19 | +1.70% |
| Average slot time (ms) | 218.80 | 218.10 | -0.32% |
| Active validators | 674.00 | 675.00 | +0.15% |
| Delinquent validators | 6.00 | 5.00 | -16.67% |
| Solana TVL | 6,170,032,842.00 | 6,218,574,826.00 | +0.79% |
| SOL price | 108.92 | 110.30 | +1.27% |
| Stablecoin supply | 16,379,819,991.00 | 16,426,716,932.00 | +0.29% |
| 24h DEX volume | 2,644,852,886.24 | 1,978,097,665.91 | -25.21% |
| 24h chain fees | 15,072,203.23 | 13,913,073.58 | -7.69% |

### Change over 7d (vs run at 2026-10-03T20:17:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,907.58 | 4,930.72 | +0.47% |
| Average non-vote TPS | 2,415.29 | 1,904.19 | -21.16% |
| Average slot time (ms) | 267.60 | 218.10 | -18.50% |
| Active validators | 670.00 | 675.00 | +0.75% |
| Delinquent validators | 15.00 | 5.00 | -66.67% |
| Solana TVL | 6,664,651,516.00 | 6,218,574,826.00 | -6.69% |
| SOL price | 119.93 | 110.30 | -8.03% |
| Stablecoin supply | 16,950,775,065.00 | 16,426,716,932.00 | -3.09% |
| 24h DEX volume | 2,760,296,309.96 | 1,978,097,665.91 | -28.34% |
| 24h chain fees | 17,402,246.04 | 13,913,073.58 | -20.05% |

### Change over 30d (vs run at 2026-09-10T20:09:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,122.54 | 4,930.72 | +19.60% |
| Average non-vote TPS | 1,990.17 | 1,904.19 | -4.32% |
| Average slot time (ms) | 315.50 | 218.10 | -30.87% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 12.00 | 5.00 | -58.33% |
| Solana TVL | 5,779,330,766.00 | 6,218,574,826.00 | +7.60% |
| SOL price | 99.77 | 110.30 | +10.55% |
| Stablecoin supply | 16,576,239,978.00 | 16,426,716,932.00 | -0.90% |
| 24h DEX volume | 3,000,435,429.63 | 1,978,097,665.91 | -34.07% |
| 24h chain fees | 15,717,207.17 | 13,913,073.58 | -11.48% |

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

This run made 41 HTTP calls (39 succeeded, 2 failed) in 16.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
