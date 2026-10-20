# Solana Ecosystem Pulse

**Generated:** 2026-10-20T20:57:03Z · **Schema:** `1.0.0` · **Collection time:** 20.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $106.50 | +2.06% |
| Market cap | $62.78B | rank #7 |
| Total value locked | $5.97B | +1.54% |
| Stablecoin supply | $15.91B | +0.45% |
| DEX volume (24h) | $1.82B | +7.44% |
| Chain fees / REV (24h) | $11.99M | +21.81% |
| Non-vote TPS (1h avg) | 2,649 | peak 6,330 total |
| Active validators | 668 | 11 delinquent |
| Epoch 1063 | 35.79% complete | 277,404 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 113 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,649.3 average over the last 60 minutes; 2,587.3 in the latest sample.
- **Total TPS:** 5,725.5 average, 6,330.3 peak. Consensus votes account for 53.7% of all transactions.
- **Slot time:** 216.1 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 437,405,605 at absolute slot 459,370,596.
- **Epoch 1063:** slot 154,596 of 432,000 (35.79% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.594% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 121 ms |
| `solana-rpc.publicnode.com` | yes | 76 ms |
| `api.mainnet.solana.com` | yes | 52 ms |

## Validators & stake

- **668 active** validators, **11 delinquent** (1.62% by count, 0.002% by stake).
- **Total stake:** 438,577,211 SOL ($46.71B); stake rate 68.94% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.96% of active stake.
- **Commission:** median 5.0%, mean 12.86%; 229 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,103,015 | 3.900% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,937,532 | 3.634% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,537,315 | 2.859% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,930,434 | 2.492% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,707 | 2.216% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,482,037 | 2.162% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,253,756 | 2.110% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,792,210 | 1.777% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,034,138 | 1.604% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,000,331 | 1.596% | 0% |

## Economics

- **SOL:** $106.50 (+2.06% 24h, -0.91% 7d, -3.58% 30d). Market cap $62.78B, 24h volume $2.60B (4.14% of cap). Price source: `coingecko`.
- **TVL:** $5.97B across 329 protocols - rank #3 of 420 chains, 6.64% of all tracked chain TVL. -0.65% over 7d, -54.0% from its ATH.
- **Stablecoins:** $15.91B circulating on Solana (-0.95% 7d) - $2.66 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.82B in 24h, $14.36B over 7d across 136 venues. Volume/TVL turnover 0.305x per day.
- **REV (chain fees):** $11.99M in 24h, $445.12M over 30d. Retained chain revenue $4.83M (40.3% of fees). Annualised fees are 6.97% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,549,370 SOL circulating of 636,151,671 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.85B | +2.5% | +5.4% |
| 2 | Kamino Lend | Lending | $1.33B | +2.5% | +3.3% |
| 3 | Raydium AMM | Dexs | $1.20B | +2.4% | -1.2% |
| 4 | Binance Staked SOL | Liquid Staking | $1.11B | +2.2% | +3.7% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.11B | +1.9% | +1.8% |
| 6 | Jupiter Lend | Lending | $1.04B | +2.5% | -5.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $744.97M | +1.3% | +0.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $556.28M | +2.1% | +2.9% |
| 9 | Sentora Curator | Risk Curators | $432.89M | -3.5% | -8.3% |
| 10 | Marinade Native | Staking Pool | $384.63M | +2.2% | -0.1% |
| 11 | PumpSwap | Dexs | $354.83M | +2.0% | -0.8% |
| 12 | Orca DEX | Dexs | $301.92M | +1.1% | +0.8% |

The top five protocols hold 41.2% of Solana's tracked TVL. Summed across all 329 protocols the total is $16.02B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.0% · Lending 16.6% · Dexs 15.2% · Derivatives 5.1% · Risk Curators 3.9% · RWA 3.7%

### Tokenised assets

$864.61M of tokenised real-world assets and equities are locked on Solana - 5.396% of chain TVL.

- OnRe (RWA): $294.00M
- Huma (RWA): $253.78M
- Solstice (Basis Trading): $209.33M
- JupUSD (Basis Trading): $42.95M
- Plume Vaults (RWA): $34.96M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-20
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-20
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-20
- [rewards: Use live commission collectors](https://github.com/solana-foundation/solana-improvement-documents/pull/700) - updated 2026-10-20
- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-20
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-20
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-20

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

### Change over 24h (vs run at 2026-10-19T21:47:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,210.74 | 5,725.49 | +9.88% |
| Average non-vote TPS | 2,163.29 | 2,649.32 | +22.47% |
| Average slot time (ms) | 218.40 | 216.10 | -1.05% |
| Active validators | 669.00 | 668.00 | -0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,846,232,281.00 | 5,971,159,147.00 | +2.14% |
| SOL price | 104.69 | 106.50 | +1.73% |
| Stablecoin supply | 15,840,000,252.00 | 15,910,290,288.00 | +0.44% |
| 24h DEX volume | 1,697,352,650.38 | 1,823,579,289.83 | +7.44% |
| 24h chain fees | 9,839,385.63 | 11,987,511.75 | +21.83% |

### Change over 7d (vs run at 2026-10-13T22:01:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,063.39 | 5,725.49 | +13.08% |
| Average non-vote TPS | 1,990.01 | 2,649.32 | +33.13% |
| Average slot time (ms) | 217.80 | 216.10 | -0.78% |
| Active validators | 673.00 | 668.00 | -0.74% |
| Delinquent validators | 7.00 | 11.00 | +57.14% |
| Solana TVL | 6,063,416,281.00 | 5,971,159,147.00 | -1.52% |
| SOL price | 107.01 | 106.50 | -0.48% |
| Stablecoin supply | 16,241,793,471.00 | 15,910,290,288.00 | -2.04% |
| 24h DEX volume | 2,231,842,381.02 | 1,823,579,289.83 | -18.29% |
| 24h chain fees | 13,103,539.72 | 11,987,511.75 | -8.52% |

### Change over 30d (vs run at 2026-09-20T19:53:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,829.85 | 5,725.49 | +18.54% |
| Average non-vote TPS | 2,325.58 | 2,649.32 | +13.92% |
| Average slot time (ms) | 268.40 | 216.10 | -19.49% |
| Active validators | 675.00 | 668.00 | -1.04% |
| Delinquent validators | 15.00 | 11.00 | -26.67% |
| Solana TVL | 6,171,179,901.00 | 5,971,159,147.00 | -3.24% |
| SOL price | 110.52 | 106.50 | -3.64% |
| Stablecoin supply | 15,806,405,937.00 | 15,910,290,288.00 | +0.66% |
| 24h DEX volume | 2,876,208,374.20 | 1,823,579,289.83 | -36.60% |
| 24h chain fees | 15,275,214.85 | 11,987,511.75 | -21.52% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 20.2s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
