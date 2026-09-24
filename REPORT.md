# Solana Ecosystem Pulse

**Generated:** 2026-09-24T16:00:52Z · **Schema:** `1.0.0` · **Collection time:** 13.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $116.24 | +2.05% |
| Market cap | $68.27B | rank #7 |
| Total value locked | $6.40B | -2.17% |
| Stablecoin supply | $16.43B | -2.68% |
| DEX volume (24h) | $2.55B | -20.10% |
| Chain fees / REV (24h) | $16.48M | -7.79% |
| Non-vote TPS (1h avg) | 2,529 | peak 5,550 total |
| Active validators | 674 | 12 delinquent |
| Epoch 1041 | 84.43% complete | 67,261 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 92 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,528.9 average over the last 60 minutes; 2,016.8 in the latest sample.
- **Total TPS:** 5,047.3 average, 5,550.0 peak. Consensus votes account for 49.9% of all transactions.
- **Slot time:** 266.3 ms average (target 400 ms), worst 1-minute bucket 276.5 ms.
- **Block height:** 428,116,830 at absolute slot 450,076,739.
- **Epoch 1041:** slot 364,739 of 432,000 (84.43% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 253 ms |
| `solana-rpc.publicnode.com` | yes | 118 ms |
| `api.mainnet.solana.com` | yes | 106 ms |

## Validators & stake

- **674 active** validators, **12 delinquent** (1.75% by count, 0.045% by stake).
- **Total stake:** 439,964,137 SOL ($51.14B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.61%; 233 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,843,203 | 4.057% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,838,937 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,360,465 | 2.811% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,264,812 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,335,638 | 2.350% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,226,124 | 2.098% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,158,950 | 2.083% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,600,816 | 1.728% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,090,585 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,340 | 1.491% | 0% |

## Economics

- **SOL:** $116.24 (+2.05% 24h, +14.87% 7d, +18.21% 30d). Market cap $68.27B, 24h volume $4.21B (6.17% of cap). Price source: `coingecko`.
- **TVL:** $6.40B across 331 protocols - rank #2 of 467 chains, 6.76% of all tracked chain TVL. +10.56% over 7d, -51.7% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+4.15% 7d) - $2.57 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.55B in 24h, $20.98B over 7d across 125 venues. Volume/TVL turnover 0.399x per day.
- **REV (chain fees):** $16.48M in 24h, $435.82M over 30d. Retained chain revenue $6.15M (37.3% of fees). Annualised fees are 8.81% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,577,032 SOL circulating of 634,608,143 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | +1.1% | +17.8% |
| 2 | Kamino Lend | Lending | $1.41B | +1.1% | +5.7% |
| 3 | Raydium AMM | Dexs | $1.31B | -0.3% | +17.4% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.21B | +1.1% | +18.0% |
| 5 | Binance Staked SOL | Liquid Staking | $1.18B | -1.7% | +15.0% |
| 6 | Jupiter Lend | Lending | $1.16B | -0.6% | +8.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $806.96M | +1.2% | +9.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $594.64M | -0.3% | +16.9% |
| 9 | Marinade Native | Staking Pool | $440.92M | -1.8% | +17.2% |
| 10 | PumpSwap | Dexs | $369.52M | -3.4% | +15.2% |
| 11 | Sentora Curator | Risk Curators | $362.49M | +0.1% | -2.6% |
| 12 | Drift Staked SOL | Liquid Staking | $323.63M | +1.0% | +16.4% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.52B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.8% · Lending 17.3% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.0% · Risk Curators 3.5%

### Tokenised assets

$835.77M of tokenised real-world assets and equities are locked on Solana - 5.058% of chain TVL.

- OnRe (RWA): $301.14M
- Solstice (Basis Trading): $218.07M
- Huma (RWA): $196.74M
- JupUSD (Basis Trading): $44.56M
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

- [SIMD-0215: SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-24
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-24
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-23
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

### Change over 24h (vs run at 2026-09-23T15:39:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,849.84 | 5,047.33 | +4.07% |
| Average non-vote TPS | 2,345.00 | 2,528.87 | +7.84% |
| Average slot time (ms) | 267.40 | 266.30 | -0.41% |
| Active validators | 674.00 | 674.00 | +0.00% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 6,436,874,885.00 | 6,401,917,349.00 | -0.54% |
| SOL price | 114.88 | 116.24 | +1.18% |
| Stablecoin supply | 16,879,859,425.00 | 16,428,129,447.00 | -2.68% |
| 24h DEX volume | 3,195,015,036.76 | 2,552,816,117.41 | -20.10% |
| 24h chain fees | 17,874,880.76 | 16,480,956.03 | -7.80% |

### Change over 7d (vs run at 2026-09-17T15:46:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,671.71 | 5,047.33 | +8.04% |
| Average non-vote TPS | 2,543.87 | 2,528.87 | -0.59% |
| Average slot time (ms) | 316.80 | 266.30 | -15.94% |
| Active validators | 678.00 | 674.00 | -0.59% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 5,852,308,147.00 | 6,401,917,349.00 | +9.39% |
| SOL price | 101.10 | 116.24 | +14.98% |
| Stablecoin supply | 15,773,094,526.00 | 16,428,129,447.00 | +4.15% |
| 24h DEX volume | 2,800,249,070.18 | 2,552,816,117.41 | -8.84% |
| 24h chain fees | 14,068,828.05 | 16,480,956.03 | +17.15% |

### Change over 30d (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 5,047.33 | +10.55% |
| Average non-vote TPS | 2,708.19 | 2,528.87 | -6.62% |
| Average slot time (ms) | 366.20 | 266.30 | -27.28% |
| Active validators | 685.00 | 674.00 | -1.61% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,634,312,506.00 | 6,401,917,349.00 | +13.62% |
| SOL price | 98.47 | 116.24 | +18.05% |
| Stablecoin supply | 16,426,872,816.00 | 16,428,129,447.00 | +0.01% |
| 24h DEX volume | 2,996,141,158.64 | 2,552,816,117.41 | -14.80% |
| 24h chain fees | 14,491,360.16 | 16,480,956.03 | +13.73% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.4s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
