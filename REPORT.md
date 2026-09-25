# Solana Ecosystem Pulse

**Generated:** 2026-09-25T10:42:05Z · **Schema:** `1.0.0` · **Collection time:** 23.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.81 | +4.95% |
| Market cap | $69.83B | rank #7 |
| Total value locked | $6.47B | +1.30% |
| Stablecoin supply | $17.69B | +7.69% |
| DEX volume (24h) | $2.26B | -11.37% |
| Chain fees / REV (24h) | $15.98M | -0.75% |
| Non-vote TPS (1h avg) | 1,524 | peak 4,342 total |
| Active validators | 676 | 9 delinquent |
| Epoch 1042 | 42.79% complete | 247,146 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 93 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 7.7% in 24h) | Stablecoin supply changed +7.7% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is above its recent norm | Current 17,688,733,606.00 sits 3.5 sigma above the median of the last 93 runs (16,345,994,847.00, +8.2%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,524.2 average over the last 60 minutes; 1,573.2 in the latest sample.
- **Total TPS:** 4,051.8 average, 4,342.3 peak. Consensus votes account for 62.4% of all transactions.
- **Slot time:** 266.4 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 428,368,758 at absolute slot 450,328,854.
- **Epoch 1042:** slot 184,854 of 432,000 (42.79% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.632% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 128 ms |
| `solana-rpc.publicnode.com` | yes | 152 ms |
| `api.mainnet.solana.com` | yes | 116 ms |

## Validators & stake

- **676 active** validators, **9 delinquent** (1.31% by count, 0.005% by stake).
- **Total stake:** 440,637,196 SOL ($52.35B); stake rate 69.43% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.40% and top 33 hold 45.81% of active stake.
- **Commission:** median 5.0%, mean 12.57%; 235 validators at 0% and 63 at 100%.

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

- **SOL:** $118.81 (+4.95% 24h, +11.73% 7d, +23.57% 30d). Market cap $69.83B, 24h volume $4.49B (6.43% of cap). Price source: `coingecko`.
- **TVL:** $6.47B across 331 protocols - rank #2 of 467 chains, 6.80% of all tracked chain TVL. +9.83% over 7d, -51.1% from its ATH.
- **Stablecoins:** $17.69B circulating on Solana (+12.57% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.26B in 24h, $19.63B over 7d across 125 venues. Volume/TVL turnover 0.350x per day.
- **REV (chain fees):** $15.98M in 24h, $415.28M over 30d. Retained chain revenue $5.90M (36.9% of fees). Annualised fees are 8.35% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,647,708 SOL circulating of 634,686,250 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.90B | +3.3% | +17.6% |
| 2 | Kamino Lend | Lending | $1.43B | +2.1% | +7.5% |
| 3 | Raydium AMM | Dexs | $1.32B | +2.0% | +11.6% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.22B | +3.3% | +16.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | +3.4% | +14.8% |
| 6 | Jupiter Lend | Lending | $1.17B | +0.8% | +8.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $814.14M | +2.2% | +9.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.96M | +3.4% | +15.7% |
| 9 | Marinade Native | Staking Pool | $451.64M | +3.4% | +17.0% |
| 10 | PumpSwap | Dexs | $386.52M | +2.6% | +17.7% |
| 11 | Sentora Curator | Risk Curators | $361.94M | -0.1% | -1.8% |
| 12 | Drift Staked SOL | Liquid Staking | $331.48M | +3.4% | +16.3% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.78B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.2% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$835.20M of tokenised real-world assets and equities are locked on Solana - 4.978% of chain TVL.

- OnRe (RWA): $299.23M
- Solstice (Basis Trading): $216.98M
- Huma (RWA): $199.37M
- JupUSD (Basis Trading): $44.36M
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
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-24
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

### Change over 24h (vs run at 2026-09-24T10:37:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,214.44 | 4,051.78 | -3.86% |
| Average non-vote TPS | 1,675.25 | 1,524.20 | -9.02% |
| Average slot time (ms) | 265.00 | 266.40 | +0.53% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 6,355,143,831.00 | 6,468,632,064.00 | +1.79% |
| SOL price | 112.79 | 118.81 | +5.34% |
| Stablecoin supply | 16,426,393,329.00 | 17,688,733,606.00 | +7.68% |
| 24h DEX volume | 2,682,822,618.41 | 2,262,603,148.43 | -15.66% |
| 24h chain fees | 16,503,822.03 | 15,981,761.80 | -3.16% |

### Change over 7d (vs run at 2026-09-18T10:08:58Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,071.90 | 4,051.78 | -0.49% |
| Average non-vote TPS | 1,539.85 | 1,524.20 | -1.02% |
| Average slot time (ms) | 265.90 | 266.40 | +0.19% |
| Active validators | 677.00 | 676.00 | -0.15% |
| Delinquent validators | 11.00 | 9.00 | -18.18% |
| Solana TVL | 6,020,571,779.00 | 6,468,632,064.00 | +7.44% |
| SOL price | 106.42 | 118.81 | +11.64% |
| Stablecoin supply | 15,709,402,844.00 | 17,688,733,606.00 | +12.60% |
| 24h DEX volume | 2,553,904,323.29 | 2,262,603,148.43 | -11.41% |
| 24h chain fees | 13,898,915.10 | 15,981,761.80 | +14.99% |

### Change over 30d (vs run at 2026-08-26T19:30:01Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,472.91 | 4,051.78 | -9.42% |
| Average non-vote TPS | 2,616.46 | 1,524.20 | -41.75% |
| Average slot time (ms) | 366.20 | 266.40 | -27.25% |
| Active validators | 685.00 | 676.00 | -1.31% |
| Delinquent validators | 10.00 | 9.00 | -10.00% |
| Solana TVL | 5,557,854,195.00 | 6,468,632,064.00 | +16.39% |
| SOL price | 96.76 | 118.81 | +22.79% |
| Stablecoin supply | 16,315,958,333.00 | 17,688,733,606.00 | +8.41% |
| 24h DEX volume | 2,934,986,439.19 | 2,262,603,148.43 | -22.91% |
| 24h chain fees | 13,235,652.04 | 15,981,761.80 | +20.75% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 23.0s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
