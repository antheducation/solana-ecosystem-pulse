# Solana Ecosystem Pulse

**Generated:** 2026-09-25T16:01:22Z · **Schema:** `1.0.0` · **Collection time:** 19.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.95 | +3.36% |
| Market cap | $70.43B | rank #7 |
| Total value locked | $6.54B | +2.34% |
| Stablecoin supply | $17.69B | +7.68% |
| DEX volume (24h) | $2.45B | -4.00% |
| Chain fees / REV (24h) | $15.98M | -1.37% |
| Non-vote TPS (1h avg) | 2,435 | peak 5,472 total |
| Active validators | 675 | 10 delinquent |
| Epoch 1042 | 59.34% complete | 175,642 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 93 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 7.7% in 24h) | Stablecoin supply changed +7.7% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is above its recent norm | Current 17,687,227,712.00 sits 3.4 sigma above the median of the last 93 runs (16,345,994,847.00, +8.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,435.2 average over the last 60 minutes; 2,672.0 in the latest sample.
- **Total TPS:** 4,941.5 average, 5,471.6 peak. Consensus votes account for 50.7% of all transactions.
- **Slot time:** 268.3 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 428,440,242 at absolute slot 450,400,358.
- **Epoch 1042:** slot 256,358 of 432,000 (59.34% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.632% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 120 ms |
| `solana-rpc.publicnode.com` | yes | 140 ms |
| `api.mainnet.solana.com` | yes | 166 ms |

## Validators & stake

- **675 active** validators, **10 delinquent** (1.46% by count, 0.008% by stake).
- **Total stake:** 440,637,196 SOL ($52.85B); stake rate 69.43% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.91%; 230 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,819,007 | 4.044% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,817,079 | 3.590% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,387,904 | 2.812% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,274,982 | 2.559% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,595,499 | 2.405% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,221,893 | 2.093% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,163,088 | 2.080% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,599,959 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,091,911 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,887 | 1.488% | 0% |

## Economics

- **SOL:** $119.95 (+3.36% 24h, +7.83% 7d, +25.00% 30d). Market cap $70.43B, 24h volume $6.14B (8.72% of cap). Price source: `coingecko`.
- **TVL:** $6.54B across 331 protocols - rank #2 of 467 chains, 6.87% of all tracked chain TVL. +10.97% over 7d, -50.6% from its ATH.
- **Stablecoins:** $17.69B circulating on Solana (+12.56% 7d) - $2.70 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.45B in 24h, $20.84B over 7d across 125 venues. Volume/TVL turnover 0.375x per day.
- **REV (chain fees):** $15.98M in 24h, $415.86M over 30d. Retained chain revenue $5.90M (36.9% of fees). Annualised fees are 8.28% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,647,474 SOL circulating of 634,686,016 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.92B | +3.7% | +19.2% |
| 2 | Kamino Lend | Lending | $1.45B | +2.5% | +8.7% |
| 3 | Raydium AMM | Dexs | $1.35B | +3.1% | +14.0% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.24B | +2.5% | +18.2% |
| 5 | Binance Staked SOL | Liquid Staking | $1.22B | +3.8% | +16.3% |
| 6 | Jupiter Lend | Lending | $1.17B | +0.7% | +8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $818.37M | +1.4% | +9.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $616.95M | +3.8% | +17.2% |
| 9 | Marinade Native | Staking Pool | $457.56M | +3.8% | +18.5% |
| 10 | PumpSwap | Dexs | $390.35M | +5.6% | +18.9% |
| 11 | Sentora Curator | Risk Curators | $361.79M | -0.2% | -1.8% |
| 12 | Drift Staked SOL | Liquid Staking | $335.82M | +3.8% | +17.8% |

The top five protocols hold 42.3% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.96B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.2% · Lending 17.2% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$834.29M of tokenised real-world assets and equities are locked on Solana - 4.920% of chain TVL.

- OnRe (RWA): $298.73M
- Solstice (Basis Trading): $216.97M
- Huma (RWA): $199.09M
- JupUSD (Basis Trading): $44.36M
- Plume Vaults (RWA): $28.17M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-24
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18

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

### Change over 24h (vs run at 2026-09-24T16:00:52Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,047.33 | 4,941.47 | -2.10% |
| Average non-vote TPS | 2,528.87 | 2,435.17 | -3.71% |
| Average slot time (ms) | 266.30 | 268.30 | +0.75% |
| Active validators | 674.00 | 675.00 | +0.15% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 6,401,917,349.00 | 6,543,782,193.00 | +2.22% |
| SOL price | 116.24 | 119.95 | +3.19% |
| Stablecoin supply | 16,428,129,447.00 | 17,687,227,712.00 | +7.66% |
| 24h DEX volume | 2,552,816,117.41 | 2,450,711,180.43 | -4.00% |
| 24h chain fees | 16,480,956.03 | 15,979,712.80 | -3.04% |

### Change over 7d (vs run at 2026-09-18T15:18:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,324.84 | 4,941.47 | -7.20% |
| Average non-vote TPS | 2,803.86 | 2,435.17 | -13.15% |
| Average slot time (ms) | 267.40 | 268.30 | +0.34% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 11.00 | 10.00 | -9.09% |
| Solana TVL | 6,074,970,771.00 | 6,543,782,193.00 | +7.72% |
| SOL price | 110.21 | 119.95 | +8.84% |
| Stablecoin supply | 15,710,184,327.00 | 17,687,227,712.00 | +12.58% |
| 24h DEX volume | 2,592,123,183.29 | 2,450,711,180.43 | -5.46% |
| 24h chain fees | 14,675,830.10 | 15,979,712.80 | +8.88% |

### Change over 30d (vs run at 2026-08-26T19:30:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,472.91 | 4,941.47 | +10.48% |
| Average non-vote TPS | 2,616.46 | 2,435.17 | -6.93% |
| Average slot time (ms) | 366.20 | 268.30 | -26.73% |
| Active validators | 685.00 | 675.00 | -1.46% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,557,854,195.00 | 6,543,782,193.00 | +17.74% |
| SOL price | 96.76 | 119.95 | +23.97% |
| Stablecoin supply | 16,315,958,333.00 | 17,687,227,712.00 | +8.40% |
| 24h DEX volume | 2,934,986,439.19 | 2,450,711,180.43 | -16.50% |
| 24h chain fees | 13,235,652.04 | 15,979,712.80 | +20.73% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 19.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
