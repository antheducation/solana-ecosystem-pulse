# Solana Ecosystem Pulse

**Generated:** 2026-09-26T15:13:30Z · **Schema:** `1.0.0` · **Collection time:** 17.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $120.99 | +0.09% |
| Market cap | $71.11B | rank #7 |
| Total value locked | $6.61B | +1.99% |
| Stablecoin supply | $16.99B | -3.94% |
| DEX volume (24h) | $2.61B | +6.61% |
| Chain fees / REV (24h) | $15.60M | -2.38% |
| Non-vote TPS (1h avg) | 2,202 | peak 5,323 total |
| Active validators | 676 | 11 delinquent |
| Epoch 1043 | 31.37% complete | 296,493 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 94 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 3.9% in 24h) | Stablecoin supply changed -3.9% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,201.7 average over the last 60 minutes; 2,121.3 in the latest sample.
- **Total TPS:** 4,705.9 average, 5,322.7 peak. Consensus votes account for 53.2% of all transactions.
- **Slot time:** 268.7 ms average (target 400 ms), worst 1-minute bucket 279.1 ms.
- **Block height:** 428,751,264 at absolute slot 450,711,507.
- **Epoch 1043:** slot 135,507 of 432,000 (31.37% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.630% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 187 ms |
| `solana-rpc.publicnode.com` | yes | 209 ms |
| `api.mainnet.solana.com` | yes | 182 ms |

## Validators & stake

- **676 active** validators, **11 delinquent** (1.60% by count, 0.008% by stake).
- **Total stake:** 437,542,654 SOL ($52.94B); stake rate 68.93% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.61% and top 33 hold 45.65% of active stake.
- **Commission:** median 5.0%, mean 12.59%; 233 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,860,284 | 4.082% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,799,204 | 3.611% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,343,056 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,222,561 | 2.565% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,836,562 | 2.477% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,102 | 2.111% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,182,742 | 2.099% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,606,181 | 1.739% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,093,311 | 1.621% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,506,505 | 1.487% | 0% |

## Economics

- **SOL:** $120.99 (+0.09% 24h, +8.24% 7d, +13.35% 30d). Market cap $71.11B, 24h volume $4.00B (5.62% of cap). Price source: `coingecko`.
- **TVL:** $6.61B across 330 protocols - rank #2 of 467 chains, 6.92% of all tracked chain TVL. +4.89% over 7d, -50.0% from its ATH.
- **Stablecoins:** $16.99B circulating on Solana (+7.05% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.61B in 24h, $19.91B over 7d across 125 venues. Volume/TVL turnover 0.395x per day.
- **REV (chain fees):** $15.60M in 24h, $416.51M over 30d. Retained chain revenue $6.03M (38.7% of fees). Annualised fees are 8.01% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,712,644 SOL circulating of 634,763,848 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.96B | +2.1% | +8.6% |
| 2 | Kamino Lend | Lending | $1.47B | +1.2% | +4.8% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.7% | +6.3% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.25B | +1.4% | +6.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.24B | +1.5% | +5.9% |
| 6 | Jupiter Lend | Lending | $1.18B | +0.7% | +2.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $824.06M | +0.7% | +2.7% |
| 8 | Jupiter Staked SOL | Liquid Staking | $625.77M | +1.4% | +6.2% |
| 9 | Marinade Native | Staking Pool | $466.20M | +1.9% | +7.5% |
| 10 | PumpSwap | Dexs | $400.63M | +2.6% | +9.1% |
| 11 | Sentora Curator | Risk Curators | $362.27M | +0.1% | -0.7% |
| 12 | Drift Staked SOL | Liquid Staking | $340.80M | +1.5% | +6.5% |

The top five protocols hold 42.4% of Solana's tracked TVL. Summed across all 330 protocols the total is $17.18B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.3% · Lending 17.2% · Dexs 15.8% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$836.29M of tokenised real-world assets and equities are locked on Solana - 4.868% of chain TVL.

- OnRe (RWA): $296.59M
- Solstice (Basis Trading): $216.14M
- Huma (RWA): $209.72M
- JupUSD (Basis Trading): $44.05M
- Plume Vaults (RWA): $25.45M

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

- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-26
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-18

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

### Change over 24h (vs run at 2026-09-25T16:01:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,941.47 | 4,705.95 | -4.77% |
| Average non-vote TPS | 2,435.17 | 2,201.74 | -9.59% |
| Average slot time (ms) | 268.30 | 268.70 | +0.15% |
| Active validators | 675.00 | 676.00 | +0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 6,543,782,193.00 | 6,613,775,749.00 | +1.07% |
| SOL price | 119.95 | 120.99 | +0.87% |
| Stablecoin supply | 17,687,227,712.00 | 16,991,097,586.00 | -3.94% |
| 24h DEX volume | 2,450,711,180.43 | 2,612,632,382.63 | +6.61% |
| 24h chain fees | 15,979,712.80 | 15,598,587.47 | -2.39% |

### Change over 7d (vs run at 2026-09-19T14:55:49Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,303.74 | 4,705.95 | +9.35% |
| Average non-vote TPS | 1,776.90 | 2,201.74 | +23.91% |
| Average slot time (ms) | 266.80 | 268.70 | +0.71% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 13.00 | 11.00 | -15.38% |
| Solana TVL | 6,245,959,676.00 | 6,613,775,749.00 | +5.89% |
| SOL price | 111.73 | 120.99 | +8.29% |
| Stablecoin supply | 15,876,497,310.00 | 16,991,097,586.00 | +7.02% |
| 24h DEX volume | 3,536,797,881.43 | 2,612,632,382.63 | -26.13% |
| 24h chain fees | 17,457,812.00 | 15,598,587.47 | -10.65% |

### Change over 30d (vs run at 2026-08-27T16:57:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,739.80 | 4,705.95 | -0.71% |
| Average non-vote TPS | 2,877.86 | 2,201.74 | -23.49% |
| Average slot time (ms) | 367.20 | 268.70 | -26.82% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 5,971,320,873.00 | 6,613,775,749.00 | +10.76% |
| SOL price | 109.05 | 120.99 | +10.95% |
| Stablecoin supply | 16,295,559,951.00 | 16,991,097,586.00 | +4.27% |
| 24h DEX volume | 2,351,677,355.00 | 2,612,632,382.63 | +11.10% |
| 24h chain fees | 15,169,688.78 | 15,598,587.47 | +2.83% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
