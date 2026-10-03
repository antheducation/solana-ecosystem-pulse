# Solana Ecosystem Pulse

**Generated:** 2026-10-03T15:18:47Z · **Schema:** `1.0.0` · **Collection time:** 12.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.56 | -0.35% |
| Market cap | $70.31B | rank #7 |
| Total value locked | $6.65B | +1.08% |
| Stablecoin supply | $16.95B | +2.21% |
| DEX volume (24h) | $2.76B | +10.92% |
| Chain fees / REV (24h) | $17.40M | +1.56% |
| Non-vote TPS (1h avg) | 1,813 | peak 4,993 total |
| Active validators | 673 | 12 delinquent |
| Epoch 1048 | 54.57% complete | 196,255 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 100 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,813.4 average over the last 60 minutes; 1,887.0 in the latest sample.
- **Total TPS:** 4,322.3 average, 4,993.3 peak. Consensus votes account for 58.0% of all transactions.
- **Slot time:** 267.3 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 431,010,315 at absolute slot 452,971,745.
- **Epoch 1048:** slot 235,745 of 432,000 (54.57% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.620% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 120 ms |
| `solana-rpc.publicnode.com` | yes | 125 ms |
| `api.mainnet.solana.com` | yes | 138 ms |

## Validators & stake

- **673 active** validators, **12 delinquent** (1.75% by count, 0.006% by stake).
- **Total stake:** 442,013,190 SOL ($52.85B); stake rate 69.59% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.53% and top 33 hold 45.61% of active stake.
- **Commission:** median 5.0%, mean 12.98%; 228 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,923,954 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,898,894 | 3.597% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,401 | 2.792% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,304,108 | 2.558% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,133,145 | 2.519% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,247,324 | 2.092% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,244,926 | 2.092% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,605,153 | 1.721% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,060,361 | 1.597% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,684,213 | 1.512% | 0% |

## Economics

- **SOL:** $119.56 (-0.35% 24h, -1.13% 7d, +13.91% 30d). Market cap $70.31B, 24h volume $2.39B (3.39% of cap). Price source: `coingecko`.
- **TVL:** $6.65B across 334 protocols - rank #2 of 468 chains, 6.97% of all tracked chain TVL. +0.20% over 7d, -49.8% from its ATH.
- **Stablecoins:** $16.95B circulating on Solana (+0.83% 7d) - $2.55 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.76B in 24h, $17.10B over 7d across 126 venues. Volume/TVL turnover 0.415x per day.
- **REV (chain fees):** $17.40M in 24h, $429.95M over 30d. Retained chain revenue $6.25M (35.9% of fees). Annualised fees are 9.03% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 588,145,895 SOL circulating of 635,150,469 total (92.60%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.96B | -2.4% | -1.7% |
| 2 | Kamino Lend | Lending | $1.39B | -0.3% | -5.6% |
| 3 | Raydium AMM | Dexs | $1.35B | -1.7% | -1.5% |
| 4 | Jupiter Lend | Lending | $1.30B | +1.0% | +9.5% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.24B | -1.6% | -1.9% |
| 6 | Binance Staked SOL | Liquid Staking | $1.22B | -2.5% | -2.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $811.28M | -2.1% | -2.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $616.77M | -2.5% | -2.7% |
| 9 | Marinade Native | Staking Pool | $444.01M | -2.6% | -5.5% |
| 10 | PumpSwap | Dexs | $396.47M | -2.5% | +0.3% |
| 11 | Sentora Curator | Risk Curators | $381.68M | -3.2% | +5.3% |
| 12 | Drift Staked SOL | Liquid Staking | $337.02M | -1.8% | -2.3% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 334 protocols the total is $17.55B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 17.0% · Dexs 15.5% · Derivatives 5.0% · Staking Pool 3.9% · RWA 3.4%

### Tokenised assets

$896.82M of tokenised real-world assets and equities are locked on Solana - 5.109% of chain TVL.

- OnRe (RWA): $291.54M
- Huma (RWA): $260.15M
- Solstice (Basis Trading): $212.36M
- JupUSD (Basis Trading): $49.17M
- Plume Vaults (RWA): $32.41M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) - Fri, 02 Oct 2026 19:30:00 GMT
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) - Wed, 30 Sep 2026 19:17:00 GMT
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-03
- [SIMD-0401: SIMD-0401: Stake program Pinocchio migration (`p-stake`)](https://github.com/solana-foundation/solana-improvement-documents/pull/401) - updated 2026-10-03
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [Bump linkify-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/682) - updated 2026-10-02
- [Bump uuid and @actions/core](https://github.com/solana-foundation/solana-improvement-documents/pull/681) - updated 2026-10-02
- [Bump js-yaml from 4.1.0 to 4.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/680) - updated 2026-10-02
- [Bump picomatch from 2.3.1 to 2.3.2](https://github.com/solana-foundation/solana-improvement-documents/pull/679) - updated 2026-10-02
- [Bump markdown-it, markdownlint and markdownlint-cli2](https://github.com/solana-foundation/solana-improvement-documents/pull/678) - updated 2026-10-01

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

### Change over 24h (vs run at 2026-10-02T16:55:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,879.88 | 4,322.31 | -11.43% |
| Average non-vote TPS | 2,381.02 | 1,813.38 | -23.84% |
| Average slot time (ms) | 267.80 | 267.30 | -0.19% |
| Active validators | 672.00 | 673.00 | +0.15% |
| Delinquent validators | 12.00 | 12.00 | +0.00% |
| Solana TVL | 6,698,957,933.00 | 6,649,842,310.00 | -0.73% |
| SOL price | 119.98 | 119.56 | -0.35% |
| Stablecoin supply | 16,579,751,140.00 | 16,950,098,411.00 | +2.23% |
| 24h DEX volume | 2,488,460,102.88 | 2,760,296,309.96 | +10.92% |
| 24h chain fees | 17,134,431.63 | 17,402,246.04 | +1.56% |

### Change over 7d (vs run at 2026-09-26T15:13:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,705.95 | 4,322.31 | -8.15% |
| Average non-vote TPS | 2,201.74 | 1,813.38 | -17.64% |
| Average slot time (ms) | 268.70 | 267.30 | -0.52% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 11.00 | 12.00 | +9.09% |
| Solana TVL | 6,613,775,749.00 | 6,649,842,310.00 | +0.55% |
| SOL price | 120.99 | 119.56 | -1.18% |
| Stablecoin supply | 16,991,097,586.00 | 16,950,098,411.00 | -0.24% |
| 24h DEX volume | 2,612,632,382.63 | 2,760,296,309.96 | +5.65% |
| 24h chain fees | 15,598,587.47 | 17,402,246.04 | +11.56% |

### Change over 30d (vs run at 2026-09-03T20:12:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,437.74 | 4,322.31 | -2.60% |
| Average non-vote TPS | 2,316.58 | 1,813.38 | -21.72% |
| Average slot time (ms) | 316.10 | 267.30 | -15.44% |
| Active validators | 676.00 | 673.00 | -0.44% |
| Delinquent validators | 19.00 | 12.00 | -36.84% |
| Solana TVL | 5,969,689,229.00 | 6,649,842,310.00 | +11.39% |
| SOL price | 105.35 | 119.56 | +13.49% |
| Stablecoin supply | 16,102,283,829.00 | 16,950,098,411.00 | +5.27% |
| 24h DEX volume | 2,289,285,889.32 | 2,760,296,309.96 | +20.57% |
| 24h chain fees | 10,535,900.15 | 17,402,246.04 | +65.17% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 12.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
