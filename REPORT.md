# Solana Ecosystem Pulse

**Generated:** 2026-09-27T10:56:00Z · **Schema:** `1.0.0` · **Collection time:** 17.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $123.93 | +2.83% |
| Market cap | $72.84B | rank #7 |
| Total value locked | $6.69B | +1.31% |
| Stablecoin supply | $16.80B | -0.04% |
| DEX volume (24h) | $2.20B | -15.65% |
| Chain fees / REV (24h) | $18.49M | +18.57% |
| Non-vote TPS (1h avg) | 1,554 | peak 4,507 total |
| Active validators | 676 | 11 delinquent |
| Epoch 1043 | 92.62% complete | 31,864 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 95 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,554.3 average over the last 60 minutes; 1,687.7 in the latest sample.
- **Total TPS:** 4,069.6 average, 4,506.6 peak. Consensus votes account for 61.8% of all transactions.
- **Slot time:** 267.9 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 429,015,839 at absolute slot 450,976,136.
- **Epoch 1043:** slot 400,136 of 432,000 (92.62% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.630% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 214 ms |
| `solana-rpc.publicnode.com` | yes | 182 ms |
| `api.mainnet.solana.com` | yes | 267 ms |

## Validators & stake

- **676 active** validators, **11 delinquent** (1.60% by count, 0.008% by stake).
- **Total stake:** 437,542,654 SOL ($54.22B); stake rate 68.93% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.61% and top 33 hold 45.65% of active stake.
- **Commission:** median 5.0%, mean 12.93%; 229 validators at 0% and 65 at 100%.

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

- **SOL:** $123.93 (+2.83% 24h, +14.48% 7d, +16.99% 30d). Market cap $72.84B, 24h volume $3.54B (4.86% of cap). Price source: `coingecko`.
- **TVL:** $6.69B across 331 protocols - rank #2 of 467 chains, 6.96% of all tracked chain TVL. +8.84% over 7d, -49.2% from its ATH.
- **Stablecoins:** $16.80B circulating on Solana (+6.32% 7d) - $2.51 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.20B in 24h, $19.11B over 7d across 126 venues. Volume/TVL turnover 0.330x per day.
- **REV (chain fees):** $18.49M in 24h, $418.77M over 30d. Retained chain revenue $7.33M (39.6% of fees). Annualised fees are 9.27% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,711,824 SOL circulating of 634,763,027 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $2.02B | +3.5% | +14.4% |
| 2 | Kamino Lend | Lending | $1.48B | +1.3% | +7.2% |
| 3 | Raydium AMM | Dexs | $1.36B | +0.9% | +9.3% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.29B | +3.5% | +12.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.27B | +3.4% | +10.5% |
| 6 | Jupiter Lend | Lending | $1.20B | +2.3% | +7.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $839.78M | +2.3% | +6.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $643.33M | +3.4% | +12.5% |
| 9 | Marinade Native | Staking Pool | $478.75M | +3.2% | +13.2% |
| 10 | PumpSwap | Dexs | $396.72M | -0.6% | +12.2% |
| 11 | Sentora Curator | Risk Curators | $362.86M | +0.1% | -0.5% |
| 12 | Drift Staked SOL | Liquid Staking | $350.05M | +3.3% | +12.1% |

The top five protocols hold 42.5% of Solana's tracked TVL. Summed across all 331 protocols the total is $17.50B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.1% · Dexs 15.7% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.3%

### Tokenised assets

$836.86M of tokenised real-world assets and equities are locked on Solana - 4.783% of chain TVL.

- OnRe (RWA): $296.62M
- Solstice (Basis Trading): $216.12M
- Huma (RWA): $209.72M
- JupUSD (Basis Trading): $44.06M
- Plume Vaults (RWA): $25.46M

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

- [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) - updated 2026-09-27
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-19

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

### Change over 24h (vs run at 2026-09-26T10:24:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,206.43 | 4,069.58 | -3.25% |
| Average non-vote TPS | 1,688.52 | 1,554.32 | -7.95% |
| Average slot time (ms) | 267.50 | 267.90 | +0.15% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 11.00 | 11.00 | +0.00% |
| Solana TVL | 6,590,356,995.00 | 6,686,550,317.00 | +1.46% |
| SOL price | 120.58 | 123.93 | +2.78% |
| Stablecoin supply | 16,990,728,148.00 | 16,804,013,694.00 | -1.10% |
| 24h DEX volume | 2,800,185,915.63 | 2,204,204,155.21 | -21.28% |
| 24h chain fees | 15,487,343.47 | 18,490,489.57 | +19.39% |

### Change over 7d (vs run at 2026-09-20T10:11:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,772.47 | 4,069.58 | +7.88% |
| Average non-vote TPS | 1,239.40 | 1,554.32 | +25.41% |
| Average slot time (ms) | 266.60 | 267.90 | +0.49% |
| Active validators | 678.00 | 676.00 | -0.29% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 6,124,115,707.00 | 6,686,550,317.00 | +9.18% |
| SOL price | 108.07 | 123.93 | +14.68% |
| Stablecoin supply | 15,802,349,869.00 | 16,804,013,694.00 | +6.34% |
| 24h DEX volume | 3,233,490,127.20 | 2,204,204,155.21 | -31.83% |
| 24h chain fees | 15,220,774.85 | 18,490,489.57 | +21.48% |

### Change over 30d (vs run at 2026-08-28T17:47:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,145.52 | 4,069.58 | -20.91% |
| Average non-vote TPS | 3,011.73 | 1,554.32 | -48.39% |
| Average slot time (ms) | 321.30 | 267.90 | -16.62% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 9.00 | 11.00 | +22.22% |
| Solana TVL | 5,895,133,114.00 | 6,686,550,317.00 | +13.42% |
| SOL price | 104.55 | 123.93 | +18.54% |
| Stablecoin supply | 16,380,565,155.00 | 16,804,013,694.00 | +2.59% |
| 24h DEX volume | 3,700,129,857.54 | 2,204,204,155.21 | -40.43% |
| 24h chain fees | 16,302,758.52 | 18,490,489.57 | +13.42% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 17.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
