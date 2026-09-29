# Solana Ecosystem Pulse

**Generated:** 2026-09-29T11:41:32Z · **Schema:** `1.0.0` · **Collection time:** 14.0s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $119.76 | +0.90% |
| Market cap | $70.39B | rank #7 |
| Total value locked | $6.51B | -1.87% |
| Stablecoin supply | $16.66B | -0.37% |
| DEX volume (24h) | $2.64B | +36.79% |
| Chain fees / REV (24h) | $17.40M | +12.81% |
| Non-vote TPS (1h avg) | 1,301 | peak 4,286 total |
| Active validators | 674 | 8 delinquent |
| Epoch 1045 | 44.29% complete | 240,656 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 96 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,301.1 average over the last 60 minutes; 1,504.3 in the latest sample.
- **Total TPS:** 3,822.0 average, 4,286.5 peak. Consensus votes account for 66.0% of all transactions.
- **Slot time:** 266.7 ms average (target 400 ms), worst 1-minute bucket 274.0 ms.
- **Block height:** 429,670,900 at absolute slot 451,631,344.
- **Epoch 1045:** slot 191,344 of 432,000 (44.29% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.626% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 177 ms |
| `solana-rpc.publicnode.com` | yes | 184 ms |
| `api.mainnet.solana.com` | yes | 125 ms |

## Validators & stake

- **674 active** validators, **8 delinquent** (1.17% by count, 0.044% by stake).
- **Total stake:** 441,249,792 SOL ($52.84B); stake rate 69.50% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.46% and top 33 hold 45.53% of active stake.
- **Commission:** median 5.0%, mean 12.53%; 229 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 | 4.041% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 | 3.602% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 | 2.798% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 | 2.562% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 | 2.542% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 | 2.096% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 | 2.091% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 | 1.732% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 | 1.519% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 | 1.478% | 0% |

## Economics

- **SOL:** $119.76 (+0.90% 24h, +2.51% 7d, +13.94% 30d). Market cap $70.39B, 24h volume $3.57B (5.08% of cap). Price source: `coingecko`.
- **TVL:** $6.51B across 331 protocols - rank #2 of 467 chains, 6.82% of all tracked chain TVL. +0.86% over 7d, -50.8% from its ATH.
- **Stablecoins:** $16.66B circulating on Solana (-2.98% 7d) - $2.56 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.64B in 24h, $17.46B over 7d across 126 venues. Volume/TVL turnover 0.405x per day.
- **REV (chain fees):** $17.40M in 24h, $412.00M over 30d. Retained chain revenue $5.86M (33.7% of fees). Annualised fees are 9.02% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,852,455 SOL circulating of 634,918,541 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.95B | +2.0% | +2.9% |
| 2 | Kamino Lend | Lending | $1.40B | -2.7% | -1.2% |
| 3 | Raydium AMM | Dexs | $1.34B | +0.7% | +1.2% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.24B | +1.3% | +0.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.23B | +1.5% | -0.2% |
| 6 | Jupiter Lend | Lending | $1.17B | +0.2% | +0.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $815.36M | +0.6% | -1.2% |
| 8 | Jupiter Staked SOL | Liquid Staking | $618.99M | +1.6% | +0.8% |
| 9 | Marinade Native | Staking Pool | $462.71M | +1.2% | +2.6% |
| 10 | PumpSwap | Dexs | $394.11M | +3.1% | +4.6% |
| 11 | Sentora Curator | Risk Curators | $360.68M | -0.5% | -0.6% |
| 12 | Drift Staked SOL | Liquid Staking | $338.29M | +1.2% | +1.1% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $17.01B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.9% · Dexs 15.9% · Derivatives 5.2% · Staking Pool 4.1% · Risk Curators 3.4%

### Tokenised assets

$832.86M of tokenised real-world assets and equities are locked on Solana - 4.897% of chain TVL.

- OnRe (RWA): $294.77M
- Solstice (Basis Trading): $214.95M
- Huma (RWA): $207.76M
- JupUSD (Basis Trading): $44.06M
- Plume Vaults (RWA): $25.48M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) - Mon, 28 Sep 2026 15:00:00 GMT
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0503: SIMD-0503: Static Sysvars](https://github.com/solana-foundation/solana-improvement-documents/pull/503) - updated 2026-09-29
- [SIMD-0607: Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-28
- [SIMD-0161: Remove mentions of SIMD-0161](https://github.com/solana-foundation/solana-improvement-documents/pull/562) - updated 2026-09-28
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-25
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
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

### Change over 24h (vs run at 2026-09-28T12:10:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,130.98 | 3,822.03 | -7.48% |
| Average non-vote TPS | 1,618.33 | 1,301.12 | -19.60% |
| Average slot time (ms) | 268.00 | 266.70 | -0.49% |
| Active validators | 675.00 | 674.00 | -0.15% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 6,503,643,660.00 | 6,514,543,463.00 | +0.17% |
| SOL price | 119.58 | 119.76 | +0.15% |
| Stablecoin supply | 16,722,135,325.00 | 16,661,562,798.00 | -0.36% |
| 24h DEX volume | 1,926,466,128.71 | 2,635,172,514.25 | +36.79% |
| 24h chain fees | 15,306,075.25 | 17,397,216.35 | +13.66% |

### Change over 7d (vs run at 2026-09-22T10:26:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,915.77 | 3,822.03 | -2.39% |
| Average non-vote TPS | 1,388.79 | 1,301.12 | -6.31% |
| Average slot time (ms) | 265.80 | 266.70 | +0.34% |
| Active validators | 676.00 | 674.00 | -0.30% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 6,425,863,032.00 | 6,514,543,463.00 | +1.38% |
| SOL price | 116.51 | 119.76 | +2.79% |
| Stablecoin supply | 17,171,641,113.00 | 16,661,562,798.00 | -2.97% |
| 24h DEX volume | 3,370,343,441.75 | 2,635,172,514.25 | -21.81% |
| 24h chain fees | 18,053,797.21 | 17,397,216.35 | -3.64% |

### Change over 30d (vs run at 2026-08-30T20:10:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,293.13 | 3,822.03 | -10.97% |
| Average non-vote TPS | 2,167.90 | 1,301.12 | -39.98% |
| Average slot time (ms) | 318.30 | 266.70 | -16.21% |
| Active validators | 680.00 | 674.00 | -0.88% |
| Delinquent validators | 17.00 | 8.00 | -52.94% |
| Solana TVL | 5,956,176,022.00 | 6,514,543,463.00 | +9.37% |
| SOL price | 105.77 | 119.76 | +13.23% |
| Stablecoin supply | 16,297,776,213.00 | 16,661,562,798.00 | +2.23% |
| 24h DEX volume | 1,670,710,752.31 | 2,635,172,514.25 | +57.73% |
| 24h chain fees | 11,213,986.82 | 17,397,216.35 | +55.14% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 13.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
