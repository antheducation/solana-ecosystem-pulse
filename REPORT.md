# Solana Ecosystem Pulse

**Generated:** 2026-10-02T11:27:59Z · **Schema:** `1.0.0` · **Collection time:** 16.1s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $122.06 | +3.75% |
| Market cap | $71.79B | rank #7 |
| Total value locked | $6.69B | +2.79% |
| Stablecoin supply | $16.58B | +1.09% |
| DEX volume (24h) | $2.49B | -3.17% |
| Chain fees / REV (24h) | $16.96M | +6.16% |
| Non-vote TPS (1h avg) | 1,427 | peak 4,289 total |
| Active validators | 672 | 12 delinquent |
| Epoch 1047 | 67.72% complete | 139,437 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 99 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,426.7 average over the last 60 minutes; 1,250.3 in the latest sample.
- **Total TPS:** 3,940.9 average, 4,288.6 peak. Consensus votes account for 63.8% of all transactions.
- **Slot time:** 266.2 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 430,635,278 at absolute slot 452,596,563.
- **Epoch 1047:** slot 292,563 of 432,000 (67.72% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.622% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 188 ms |
| `solana-rpc.publicnode.com` | yes | 124 ms |
| `api.mainnet.solana.com` | yes | 184 ms |

## Validators & stake

- **672 active** validators, **12 delinquent** (1.75% by count, 0.020% by stake).
- **Total stake:** 440,810,473 SOL ($53.81B); stake rate 69.41% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.62% and top 33 hold 45.76% of active stake.
- **Commission:** median 5.0%, mean 13.00%; 227 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,839,408 | 4.048% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,905,145 | 3.609% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,328,203 | 2.797% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,357,265 | 2.577% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,121 | 2.543% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,267,704 | 2.103% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,246,451 | 2.098% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,601,711 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,063,975 | 1.603% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,682,305 | 1.516% | 0% |

## Economics

- **SOL:** $122.06 (+3.75% 24h, +2.44% 7d, +24.35% 30d). Market cap $71.79B, 24h volume $4.34B (6.05% of cap). Price source: `coingecko`.
- **TVL:** $6.69B across 333 protocols - rank #2 of 468 chains, 6.91% of all tracked chain TVL. +3.19% over 7d, -49.5% from its ATH.
- **Stablecoins:** $16.58B circulating on Solana (-5.30% 7d) - $2.48 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.49B in 24h, $16.95B over 7d across 126 venues. Volume/TVL turnover 0.372x per day.
- **REV (chain fees):** $16.96M in 24h, $421.62M over 30d. Retained chain revenue $6.12M (36.1% of fees). Annualised fees are 8.62% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,075,284 SOL circulating of 635,072,947 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.99B | +4.1% | +5.0% |
| 2 | Kamino Lend | Lending | $1.39B | +0.6% | -2.6% |
| 3 | Raydium AMM | Dexs | $1.37B | +2.7% | +3.2% |
| 4 | Jupiter Lend | Lending | $1.28B | +5.0% | +8.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.27B | +4.1% | +4.5% |
| 6 | Binance Staked SOL | Liquid Staking | $1.25B | +4.0% | +3.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $825.72M | +2.5% | +1.5% |
| 8 | Jupiter Staked SOL | Liquid Staking | $630.48M | +4.0% | +3.6% |
| 9 | Marinade Native | Staking Pool | $454.24M | +2.6% | +0.6% |
| 10 | PumpSwap | Dexs | $407.00M | +4.5% | +6.6% |
| 11 | Sentora Curator | Risk Curators | $394.60M | -0.0% | +8.9% |
| 12 | Drift Staked SOL | Liquid Staking | $344.59M | +4.0% | +4.0% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 333 protocols the total is $17.71B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.2% · Lending 16.9% · Dexs 15.6% · Derivatives 5.1% · Staking Pool 3.9% · Risk Curators 3.4%

### Tokenised assets

$859.38M of tokenised real-world assets and equities are locked on Solana - 4.852% of chain TVL.

- OnRe (RWA): $291.28M
- Huma (RWA): $222.53M
- Solstice (Basis Trading): $212.74M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.36M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [Bump linkify-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/682) - updated 2026-10-02
- [Bump uuid and @actions/core](https://github.com/solana-foundation/solana-improvement-documents/pull/681) - updated 2026-10-02
- [Bump js-yaml from 4.1.0 to 4.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/680) - updated 2026-10-02
- [Bump picomatch from 2.3.1 to 2.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/679) - updated 2026-10-02
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-01
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01

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

### Change over 24h (vs run at 2026-10-01T11:56:13Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,905.71 | 3,940.87 | +0.90% |
| Average non-vote TPS | 1,400.79 | 1,426.72 | +1.85% |
| Average slot time (ms) | 267.10 | 266.20 | -0.34% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 6,520,822,206.00 | 6,693,361,792.00 | +2.65% |
| SOL price | 117.94 | 122.06 | +3.49% |
| Stablecoin supply | 16,398,738,087.00 | 16,579,036,964.00 | +1.10% |
| 24h DEX volume | 2,569,940,125.73 | 2,488,460,102.88 | -3.17% |
| 24h chain fees | 15,876,757.05 | 16,959,932.19 | +6.82% |

### Change over 7d (vs run at 2026-09-25T10:42:05Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,051.78 | 3,940.87 | -2.74% |
| Average non-vote TPS | 1,524.20 | 1,426.72 | -6.40% |
| Average slot time (ms) | 266.40 | 266.20 | -0.08% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 6,468,632,064.00 | 6,693,361,792.00 | +3.47% |
| SOL price | 118.81 | 122.06 | +2.74% |
| Stablecoin supply | 17,688,733,606.00 | 16,579,036,964.00 | -6.27% |
| 24h DEX volume | 2,262,603,148.43 | 2,488,460,102.88 | +9.98% |
| 24h chain fees | 15,981,761.80 | 16,959,932.19 | +6.12% |

### Change over 30d (vs run at 2026-09-02T20:11:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,022.99 | 3,940.87 | -2.04% |
| Average non-vote TPS | 1,883.92 | 1,426.72 | -24.27% |
| Average slot time (ms) | 314.50 | 266.20 | -15.36% |
| Active validators | 677.00 | 672.00 | -0.74% |
| Delinquent validators | 18.00 | 12.00 | -33.33% |
| Solana TVL | 5,665,576,869.00 | 6,693,361,792.00 | +18.14% |
| SOL price | 99.75 | 122.06 | +22.37% |
| Stablecoin supply | 15,850,870,070.00 | 16,579,036,964.00 | +4.59% |
| 24h DEX volume | 2,171,560,050.49 | 2,488,460,102.88 | +14.59% |
| 24h chain fees | 12,646,787.67 | 16,959,932.19 | +34.10% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
