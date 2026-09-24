# Solana Ecosystem Pulse

**Generated:** 2026-09-24T20:51:18Z · **Schema:** `1.0.0` · **Collection time:** 11.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $116.85 | +2.33% |
| Market cap | $68.67B | rank #7 |
| Total value locked | $6.48B | -0.76% |
| Stablecoin supply | $16.43B | -2.69% |
| DEX volume (24h) | $2.55B | -20.10% |
| Chain fees / REV (24h) | $16.12M | -7.77% |
| Non-vote TPS (1h avg) | 2,393 | peak 5,461 total |
| Active validators | 676 | 10 delinquent |
| Epoch 1041 | 99.53% complete | 2,009 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 92 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,393.1 average over the last 60 minutes; 2,209.6 in the latest sample.
- **Total TPS:** 4,906.5 average, 5,460.6 peak. Consensus votes account for 51.2% of all transactions.
- **Slot time:** 267.4 ms average (target 400 ms), worst 1-minute bucket 280.4 ms.
- **Block height:** 428,182,013 at absolute slot 450,141,991.
- **Epoch 1041:** slot 429,991 of 432,000 (99.53% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 97 ms |
| `solana-rpc.publicnode.com` | yes | 39 ms |
| `api.mainnet.solana.com` | yes | 145 ms |

## Validators & stake

- **676 active** validators, **10 delinquent** (1.46% by count, 0.009% by stake).
- **Total stake:** 439,964,137 SOL ($51.41B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.86% of active stake.
- **Commission:** median 5.0%, mean 12.87%; 233 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.056% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.600% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.810% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.561% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.349% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.097% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.082% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.728% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.491% | 0% |

## Economics

- **SOL:** $116.85 (+2.33% 24h, +15.87% 7d, +19.33% 30d). Market cap $68.67B, 24h volume $4.32B (6.29% of cap). Price source: `coingecko`.
- **TVL:** $6.48B across 331 protocols - rank #2 of 467 chains, 6.80% of all tracked chain TVL. +12.16% over 7d, -51.0% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+4.14% 7d) - $2.53 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.55B in 24h, $20.98B over 7d across 125 venues. Volume/TVL turnover 0.394x per day.
- **REV (chain fees):** $16.12M in 24h, $412.76M over 30d. Retained chain revenue $5.84M (36.3% of fees). Annualised fees are 8.57% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,576,811 SOL circulating of 634,607,922 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.89B | +2.5% | +20.4% |
| 2 | Kamino Lend | Lending | $1.42B | +1.4% | +6.7% |
| 3 | Raydium AMM | Dexs | $1.33B | +1.5% | +19.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.21B | +2.1% | +18.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | +2.0% | +17.0% |
| 6 | Jupiter Lend | Lending | $1.18B | +1.3% | +10.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $809.75M | +1.0% | +9.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.30M | +2.5% | +19.6% |
| 9 | Marinade Native | Staking Pool | $451.04M | +2.5% | +19.9% |
| 10 | PumpSwap | Dexs | $384.26M | +2.8% | +19.7% |
| 11 | Sentora Curator | Risk Curators | $362.26M | -0.0% | -2.7% |
| 12 | Drift Staked SOL | Liquid Staking | $330.49M | +2.3% | +18.9% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.76B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.3% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$834.14M of tokenised real-world assets and equities are locked on Solana - 4.978% of chain TVL.

- OnRe (RWA): $299.11M
- Solstice (Basis Trading): $217.00M
- Huma (RWA): $198.36M
- JupUSD (Basis Trading): $44.43M
- Plume Vaults (RWA): $28.26M

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

- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-24
- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-24
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-24
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-23T20:45:40Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,741.96 | 4,906.54 | +3.47% |
| Average non-vote TPS | 2,211.74 | 2,393.07 | +8.20% |
| Average slot time (ms) | 265.30 | 267.40 | +0.79% |
| Active validators | 674.00 | 676.00 | +0.30% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 6,385,088,886.00 | 6,484,914,945.00 | +1.56% |
| SOL price | 114.36 | 116.85 | +2.18% |
| Stablecoin supply | 16,880,373,729.00 | 16,427,048,512.00 | -2.69% |
| 24h DEX volume | 3,195,015,036.76 | 2,552,816,117.41 | -20.10% |
| 24h chain fees | 17,874,880.76 | 16,120,232.81 | -9.82% |

### Change over 7d (vs run at 2026-09-17T20:39:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,673.89 | 4,906.54 | +4.98% |
| Average non-vote TPS | 2,551.83 | 2,393.07 | -6.22% |
| Average slot time (ms) | 318.10 | 267.40 | -15.94% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 5,865,883,806.00 | 6,484,914,945.00 | +10.55% |
| SOL price | 101.14 | 116.85 | +15.53% |
| Stablecoin supply | 15,774,027,557.00 | 16,427,048,512.00 | +4.14% |
| 24h DEX volume | 2,800,249,070.18 | 2,552,816,117.41 | -8.84% |
| 24h chain fees | 14,069,098.05 | 16,120,232.81 | +14.58% |

### Change over 30d (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 4,906.54 | +7.47% |
| Average non-vote TPS | 2,708.19 | 2,393.07 | -11.64% |
| Average slot time (ms) | 366.20 | 267.40 | -26.98% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,634,312,506.00 | 6,484,914,945.00 | +15.10% |
| SOL price | 98.47 | 116.85 | +18.67% |
| Stablecoin supply | 16,426,872,816.00 | 16,427,048,512.00 | +0.00% |
| 24h DEX volume | 2,996,141,158.64 | 2,552,816,117.41 | -14.80% |
| 24h chain fees | 14,491,360.16 | 16,120,232.81 | +11.24% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
