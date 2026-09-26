# Solana Ecosystem Pulse

**Generated:** 2026-09-26T02:15:13Z · **Schema:** `1.0.0` · **Collection time:** 15.9s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $122.14 | +3.35% |
| Market cap | $71.77B | rank #7 |
| Total value locked | $6.64B | +1.02% |
| Stablecoin supply | $16.99B | -3.94% |
| DEX volume (24h) | $2.80B | +14.26% |
| Chain fees / REV (24h) | $14.94M | -6.50% |
| Non-vote TPS (1h avg) | 2,690 | peak 5,523 total |
| Active validators | 675 | 10 delinquent |
| Epoch 1042 | 91.11% complete | 38,397 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 93 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply moved sharply (down 3.9% in 24h) | Stablecoin supply changed -3.9% over the last day, past the 3% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,689.7 average over the last 60 minutes; 2,538.6 in the latest sample.
- **Total TPS:** 5,172.9 average, 5,522.9 peak. Consensus votes account for 48.0% of all transactions.
- **Slot time:** 270.5 ms average (target 400 ms), worst 1-minute bucket 289.9 ms.
- **Block height:** 428,577,427 at absolute slot 450,537,603.
- **Epoch 1042:** slot 393,603 of 432,000 (91.11% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.632% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 184 ms |
| `solana-rpc.publicnode.com` | yes | 136 ms |
| `api.mainnet.solana.com` | yes | 146 ms |

## Validators & stake

- **675 active** validators, **10 delinquent** (1.46% by count, 0.008% by stake).
- **Total stake:** 440,637,196 SOL ($53.82B); stake rate 69.43% of total supply.
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

- **SOL:** $122.14 (+3.35% 24h, +7.72% 7d, +20.37% 30d). Market cap $71.77B, 24h volume $6.40B (8.91% of cap). Price source: `coingecko`.
- **TVL:** $6.64B across 330 protocols - rank #2 of 467 chains, 6.94% of all tracked chain TVL. +5.31% over 7d, -49.8% from its ATH.
- **Stablecoins:** $16.99B circulating on Solana (+7.05% 7d) - $2.56 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.80B in 24h, $18.90B over 7d across 125 venues. Volume/TVL turnover 0.422x per day.
- **REV (chain fees):** $14.94M in 24h, $415.20M over 30d. Retained chain revenue $6.01M (40.2% of fees). Annualised fees are 7.60% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,641,802 SOL circulating of 634,685,559 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +5.0% | +10.0% |
| 2 | Kamino Lend | Lending | $1.47B | +3.0% | +5.0% |
| 3 | Raydium AMM | Dexs | $1.36B | +3.0% | +6.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.27B | +3.8% | +8.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.25B | +4.2% | +7.2% |
| 6 | Jupiter Lend | Lending | $1.19B | +0.5% | +2.8% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $831.28M | +2.1% | +3.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $633.68M | +4.1% | +7.6% |
| 9 | Marinade Native | Staking Pool | $469.79M | +4.1% | +8.3% |
| 10 | PumpSwap | Dexs | $398.48M | +4.4% | +8.5% |
| 11 | Sentora Curator | Risk Curators | $362.35M | -0.0% | -0.7% |
| 12 | Drift Staked SOL | Liquid Staking | $344.95M | +4.1% | +7.8% |

The top five protocols hold 42.4% of Solana's tracked TVL. Summed across all 330 protocols the total is $17.31B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.5% · Lending 17.1% · Dexs 15.8% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$836.75M of tokenised real-world assets and equities are locked on Solana - 4.835% of chain TVL.

- OnRe (RWA): $296.56M
- Solstice (Basis Trading): $216.14M
- Huma (RWA): $209.91M
- JupUSD (Basis Trading): $44.36M
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

- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-25
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

### Change over 24h (vs run at 2026-09-25T02:09:36Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,337.90 | 5,172.85 | +19.25% |
| Average non-vote TPS | 1,832.73 | 2,689.69 | +46.76% |
| Average slot time (ms) | 268.20 | 270.50 | +0.86% |
| Active validators | 675.00 | 675.00 | +0.00% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 6,485,663,210.00 | 6,640,595,779.00 | +2.39% |
| SOL price | 118.12 | 122.14 | +3.40% |
| Stablecoin supply | 17,687,554,466.00 | 16,991,284,619.00 | -3.94% |
| 24h DEX volume | 2,262,604,262.43 | 2,800,186,102.63 | +23.76% |
| 24h chain fees | 15,931,553.48 | 14,941,402.71 | -6.22% |

### Change over 7d (vs run at 2026-09-19T01:55:43Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,416.04 | 5,172.85 | +17.14% |
| Average non-vote TPS | 1,894.43 | 2,689.69 | +41.98% |
| Average slot time (ms) | 267.10 | 270.50 | +1.27% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 11.00 | 10.00 | -9.09% |
| Solana TVL | 6,396,701,682.00 | 6,640,595,779.00 | +3.81% |
| SOL price | 113.63 | 122.14 | +7.49% |
| Stablecoin supply | 15,876,163,466.00 | 16,991,284,619.00 | +7.02% |
| 24h DEX volume | 3,097,318,491.84 | 2,800,186,102.63 | -9.59% |
| 24h chain fees | 15,267,932.07 | 14,941,402.71 | -2.14% |

### Change over 30d (vs run at 2026-08-26T19:30:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,472.91 | 5,172.85 | +15.65% |
| Average non-vote TPS | 2,616.46 | 2,689.69 | +2.80% |
| Average slot time (ms) | 366.20 | 270.50 | -26.13% |
| Active validators | 685.00 | 675.00 | -1.46% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,557,854,195.00 | 6,640,595,779.00 | +19.48% |
| SOL price | 96.76 | 122.14 | +26.23% |
| Stablecoin supply | 16,315,958,333.00 | 16,991,284,619.00 | +4.14% |
| 24h DEX volume | 2,934,986,439.19 | 2,800,186,102.63 | -4.59% |
| 24h chain fees | 13,235,652.04 | 14,941,402.71 | +12.89% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 15.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
