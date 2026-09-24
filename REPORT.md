# Solana Ecosystem Pulse

**Generated:** 2026-09-24T10:37:53Z · **Schema:** `1.0.0` · **Collection time:** 20.7s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $112.79 | -3.81% |
| Market cap | $66.27B | rank #7 |
| Total value locked | $6.36B | -2.19% |
| Stablecoin supply | $16.43B | -2.69% |
| DEX volume (24h) | $2.68B | -16.03% |
| Chain fees / REV (24h) | $16.50M | -7.67% |
| Non-vote TPS (1h avg) | 1,675 | peak 4,796 total |
| Active validators | 676 | 11 delinquent |
| Epoch 1041 | 67.55% complete | 140,195 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 92 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,675.2 average over the last 60 minutes; 1,913.9 in the latest sample.
- **Total TPS:** 4,214.4 average, 4,796.1 peak. Consensus votes account for 60.2% of all transactions.
- **Slot time:** 265.0 ms average (target 400 ms), worst 1-minute bucket 275.2 ms.
- **Block height:** 428,043,925 at absolute slot 450,003,805.
- **Epoch 1041:** slot 291,805 of 432,000 (67.55% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.634% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 245 ms |
| `solana-rpc.publicnode.com` | yes | 113 ms |
| `api.mainnet.solana.com` | yes | 217 ms |

## Validators & stake

- **676 active** validators, **11 delinquent** (1.60% by count, 0.045% by stake).
- **Total stake:** 439,964,137 SOL ($49.62B); stake rate 69.33% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.59%; 234 validators at 0% and 63 at 100%.

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

- **SOL:** $112.79 (-3.81% 24h, +12.62% 7d, +13.08% 30d). Market cap $66.27B, 24h volume $4.74B (7.14% of cap). Price source: `coingecko`.
- **TVL:** $6.36B across 332 protocols - rank #2 of 467 chains, 6.73% of all tracked chain TVL. +10.53% over 7d, -51.7% from its ATH.
- **Stablecoins:** $16.43B circulating on Solana (+4.14% 7d) - $2.58 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.68B in 24h, $19.96B over 7d across 125 venues. Volume/TVL turnover 0.422x per day.
- **REV (chain fees):** $16.50M in 24h, $434.98M over 30d. Retained chain revenue $6.17M (37.4% of fees). Annualised fees are 9.09% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,577,266 SOL circulating of 634,608,378 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.0% | +17.5% |
| 2 | Kamino Lend | Lending | $1.40B | -1.3% | +4.9% |
| 3 | Raydium AMM | Dexs | $1.31B | -2.7% | +17.5% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.18B | -3.0% | +15.4% |
| 5 | Jupiter Lend | Lending | $1.17B | -1.2% | +8.9% |
| 6 | Binance Staked SOL | Liquid Staking | $1.16B | -3.0% | +13.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $805.32M | -1.3% | +9.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $588.96M | -3.0% | +15.8% |
| 9 | Marinade Native | Staking Pool | $436.75M | -3.1% | +16.1% |
| 10 | PumpSwap | Dexs | $376.74M | -3.5% | +17.4% |
| 11 | Sentora Curator | Risk Curators | $362.40M | -0.1% | -2.6% |
| 12 | Drift Staked SOL | Liquid Staking | $320.54M | -3.1% | +15.3% |

The top five protocols hold 42.0% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.6% · Lending 17.4% · Dexs 15.9% · Derivatives 5.3% · Staking Pool 4.0% · Risk Curators 3.5%

### Tokenised assets

$835.76M of tokenised real-world assets and equities are locked on Solana - 5.082% of chain TVL.

- OnRe (RWA): $301.16M
- Solstice (Basis Trading): $218.07M
- Huma (RWA): $196.69M
- JupUSD (Basis Trading): $44.63M
- Plume Vaults (RWA): $28.26M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT

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
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-23
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0249: SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-23T10:22:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,085.13 | 4,214.44 | +3.17% |
| Average non-vote TPS | 1,543.26 | 1,675.25 | +8.55% |
| Average slot time (ms) | 264.90 | 265.00 | +0.04% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 12.00 | 11.00 | -8.33% |
| Solana TVL | 6,548,550,262.00 | 6,355,143,831.00 | -2.95% |
| SOL price | 117.38 | 112.79 | -3.91% |
| Stablecoin supply | 16,880,437,780.00 | 16,426,393,329.00 | -2.69% |
| 24h DEX volume | 3,449,152,862.76 | 2,682,822,618.41 | -22.22% |
| 24h chain fees | 17,843,164.76 | 16,503,822.03 | -7.51% |

### Change over 7d (vs run at 2026-09-17T10:32:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,552.39 | 4,214.44 | +18.64% |
| Average non-vote TPS | 1,435.43 | 1,675.25 | +16.71% |
| Average slot time (ms) | 316.90 | 265.00 | -16.38% |
| Active validators | 674.00 | 676.00 | +0.30% |
| Delinquent validators | 16.00 | 11.00 | -31.25% |
| Solana TVL | 5,840,847,957.00 | 6,355,143,831.00 | +8.81% |
| SOL price | 99.67 | 112.79 | +13.16% |
| Stablecoin supply | 15,772,866,527.00 | 16,426,393,329.00 | +4.14% |
| 24h DEX volume | 2,733,441,991.18 | 2,682,822,618.41 | -1.85% |
| 24h chain fees | 14,202,548.05 | 16,503,822.03 | +16.20% |

### Change over 30d (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 4,214.44 | -7.69% |
| Average non-vote TPS | 2,708.19 | 1,675.25 | -38.14% |
| Average slot time (ms) | 366.20 | 265.00 | -27.64% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,634,312,506.00 | 6,355,143,831.00 | +12.79% |
| SOL price | 98.47 | 112.79 | +14.54% |
| Stablecoin supply | 16,426,872,816.00 | 16,426,393,329.00 | -0.00% |
| 24h DEX volume | 2,996,141,158.64 | 2,682,822,618.41 | -10.46% |
| 24h chain fees | 14,491,360.16 | 16,503,822.03 | +13.89% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 20.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
