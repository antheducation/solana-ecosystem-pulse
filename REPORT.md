# Solana Ecosystem Pulse

**Generated:** 2026-10-19T21:47:20Z · **Schema:** `1.0.0` · **Collection time:** 19.4s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.69 | +2.93% |
| Market cap | $61.71B | rank #7 |
| Total value locked | $5.85B | -1.23% |
| Stablecoin supply | $15.84B | -0.37% |
| DEX volume (24h) | $1.70B | +35.52% |
| Chain fees / REV (24h) | $9.84M | +4.94% |
| Non-vote TPS (1h avg) | 2,163 | peak 6,184 total |
| Active validators | 669 | 10 delinquent |
| Epoch 1062 | 47.10% complete | 228,532 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 111 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,163.3 average over the last 60 minutes; 2,352.1 in the latest sample.
- **Total TPS:** 5,210.7 average, 6,184.5 peak. Consensus votes account for 58.5% of all transactions.
- **Slot time:** 218.4 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 437,022,601 at absolute slot 458,987,468.
- **Epoch 1062:** slot 203,468 of 432,000 (47.10% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.595% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 231 ms |
| `solana-rpc.publicnode.com` | yes | 108 ms |
| `api.mainnet.solana.com` | yes | 229 ms |

## Validators & stake

- **669 active** validators, **10 delinquent** (1.47% by count, 0.000% by stake).
- **Total stake:** 437,880,622 SOL ($45.84B); stake rate 68.84% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.27% and top 33 hold 45.92% of active stake.
- **Commission:** median 5.0%, mean 12.84%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,095,415 | 3.904% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,730,365 | 3.592% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,524,168 | 2.860% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,975,836 | 2.507% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,890 | 2.219% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,481,609 | 2.165% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,107 | 2.113% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,119 | 1.778% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,993,888 | 1.597% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,731,556 | 1.537% | 0% |

## Economics

- **SOL:** $104.69 (+2.93% 24h, -3.41% 7d, -5.73% 30d). Market cap $61.71B, 24h volume $2.75B (4.45% of cap). Price source: `coingecko`.
- **TVL:** $5.85B across 328 protocols - rank #4 of 420 chains, 6.56% of all tracked chain TVL. -6.42% over 7d, -55.3% from its ATH.
- **Stablecoins:** $15.84B circulating on Solana (-2.10% 7d) - $2.71 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.70B in 24h, $14.76B over 7d across 136 venues. Volume/TVL turnover 0.290x per day.
- **REV (chain fees):** $9.84M in 24h, $447.89M over 30d. Retained chain revenue $3.67M (37.3% of fees). Annualised fees are 5.82% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,493,625 SOL circulating of 636,090,173 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.82B | +3.4% | -0.9% |
| 2 | Kamino Lend | Lending | $1.31B | +1.2% | -2.5% |
| 3 | Raydium AMM | Dexs | $1.17B | +2.8% | -6.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.10B | +3.7% | -5.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.10B | +3.2% | -4.2% |
| 6 | Jupiter Lend | Lending | $1.01B | +1.4% | -11.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $735.11M | +1.8% | -5.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $544.62M | +3.4% | -5.3% |
| 9 | Sentora Curator | Risk Curators | $448.78M | -0.5% | -8.8% |
| 10 | Marinade Native | Staking Pool | $378.75M | +2.8% | -8.2% |
| 11 | PumpSwap | Dexs | $347.81M | +1.7% | -6.0% |
| 12 | Orca DEX | Dexs | $298.76M | +1.2% | -4.1% |

The top five protocols hold 41.0% of Solana's tracked TVL. Summed across all 328 protocols the total is $15.81B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.4% · Dexs 15.1% · Derivatives 5.1% · Risk Curators 4.0% · RWA 3.9%

### Tokenised assets

$885.46M of tokenised real-world assets and equities are locked on Solana - 5.599% of chain TVL.

- OnRe (RWA): $293.87M
- Huma (RWA): $274.69M
- Solstice (Basis Trading): $209.27M
- JupUSD (Basis Trading): $43.16M
- Plume Vaults (RWA): $34.81M

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

- [100M CUs Pt2](https://github.com/solana-foundation/solana-improvement-documents/pull/698) - updated 2026-10-19
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-19
- [SIMD-0123: SIMD-0123: Refine inclusion based on Alpenglow, remove `DepositDelegatorRewards`](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-10-19
- [SIMD-0684: SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-17
- [SIMD-0686: SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-16
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-15
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-15

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

### Change over 24h (vs run at 2026-10-18T19:46:35Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,974.46 | 5,210.74 | +4.75% |
| Average non-vote TPS | 1,911.38 | 2,163.29 | +13.18% |
| Average slot time (ms) | 217.10 | 218.40 | +0.60% |
| Active validators | 668.00 | 669.00 | +0.15% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 5,875,275,842.00 | 5,846,232,281.00 | -0.49% |
| SOL price | 100.82 | 104.69 | +3.84% |
| Stablecoin supply | 15,898,071,483.00 | 15,840,000,252.00 | -0.37% |
| 24h DEX volume | 1,252,516,756.55 | 1,697,352,650.38 | +35.52% |
| 24h chain fees | 9,375,340.79 | 9,839,385.63 | +4.95% |

### Change over 7d (vs run at 2026-10-12T23:52:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,094.70 | 5,210.74 | +2.28% |
| Average non-vote TPS | 2,039.01 | 2,163.29 | +6.10% |
| Average slot time (ms) | 218.80 | 218.40 | -0.18% |
| Active validators | 672.00 | 669.00 | -0.45% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 6,087,233,347.00 | 5,846,232,281.00 | -3.96% |
| SOL price | 105.47 | 104.69 | -0.74% |
| Stablecoin supply | 16,359,920,349.00 | 15,840,000,252.00 | -3.18% |
| 24h DEX volume | 1,277,023,682.31 | 1,697,352,650.38 | +32.91% |
| 24h chain fees | 11,301,815.14 | 9,839,385.63 | -12.94% |

### Change over 30d (vs run at 2026-09-19T19:41:16Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,683.68 | 5,210.74 | +11.25% |
| Average non-vote TPS | 2,161.60 | 2,163.29 | +0.08% |
| Average slot time (ms) | 267.00 | 218.40 | -18.20% |
| Active validators | 677.00 | 669.00 | -1.18% |
| Delinquent validators | 13.00 | 10.00 | -23.08% |
| Solana TVL | 6,243,262,565.00 | 5,846,232,281.00 | -6.36% |
| SOL price | 111.27 | 104.69 | -5.91% |
| Stablecoin supply | 15,875,774,561.00 | 15,840,000,252.00 | -0.23% |
| 24h DEX volume | 3,536,797,881.43 | 1,697,352,650.38 | -52.01% |
| 24h chain fees | 17,457,812.00 | 9,839,385.63 | -43.64% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 19.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
