# Solana Ecosystem Pulse

**Generated:** 2026-10-24T14:57:39Z · **Schema:** `1.0.0` · **Collection time:** 11.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.37 | -4.19% |
| Market cap | $59.18B | rank #7 |
| Total value locked | $5.76B | -2.15% |
| Stablecoin supply | $15.92B | -0.26% |
| DEX volume (24h) | $2.00B | -2.07% |
| Chain fees / REV (24h) | $10.55M | -8.04% |
| Non-vote TPS (1h avg) | 2,206 | peak 4,064 total |
| Active validators | 664 | 14 delinquent |
| Epoch 1066 | 88.08% complete | 51,498 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 121 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,205.53 sits 4.7 sigma below the median of the last 121 runs (4,654.59, -52.6%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,205.5 average over the last 60 minutes; 1,948.5 in the latest sample.
- **Total TPS:** 2,205.5 average, 4,063.7 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.8 ms average (target 400 ms), worst 1-minute bucket 218.2 ms.
- **Block height:** 438,922,907 at absolute slot 460,892,502.
- **Epoch 1066:** slot 380,502 of 432,000 (88.08% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.589% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 112 ms |
| `solana-rpc.publicnode.com` | yes | 32 ms |
| `api.mainnet.solana.com` | yes | 60 ms |

## Validators & stake

- **664 active** validators, **14 delinquent** (2.06% by count, 0.066% by stake).
- **Total stake:** 437,116,782 SOL ($43.87B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.45% and top 33 hold 45.97% of active stake.
- **Commission:** median 5.0%, mean 13.23%; 225 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,096,230 | 3.914% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,022,778 | 3.668% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,572,396 | 2.878% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,882,511 | 2.491% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,724,046 | 2.226% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,478,407 | 2.170% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,213,418 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,782,539 | 1.782% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,037,301 | 1.611% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 7,003,145 | 1.603% | 0% |

## Economics

- **SOL:** $100.37 (-4.19% 24h, -3.40% 7d, -12.61% 30d). Market cap $59.18B, 24h volume $2.23B (3.77% of cap). Price source: `coingecko`.
- **TVL:** $5.76B across 332 protocols - rank #3 of 421 chains, 6.44% of all tracked chain TVL. -3.19% over 7d, -55.6% from its ATH.
- **Stablecoins:** $15.92B circulating on Solana (-0.65% 7d) - $2.76 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.00B in 24h, $13.52B over 7d across 138 venues. Volume/TVL turnover 0.347x per day.
- **REV (chain fees):** $10.55M in 24h, $440.73M over 30d. Retained chain revenue $3.96M (37.5% of fees). Annualised fees are 6.51% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,708,703 SOL circulating of 636,334,804 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -3.1% | -1.7% |
| 2 | Kamino Lend | Lending | $1.26B | -1.8% | -3.5% |
| 3 | Raydium AMM | Dexs | $1.15B | -2.7% | -2.4% |
| 4 | Binance Staked SOL | Liquid Staking | $1.07B | -2.8% | -2.0% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | -3.1% | -3.1% |
| 6 | Jupiter Lend | Lending | $1.02B | +0.1% | -6.7% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $716.22M | -1.8% | -3.0% |
| 8 | Jupiter Staked SOL | Liquid Staking | $531.01M | -2.7% | -2.7% |
| 9 | Sentora Curator | Risk Curators | $397.29M | -2.7% | -12.0% |
| 10 | Marinade Native | Staking Pool | $365.10M | -2.5% | -4.3% |
| 11 | PumpSwap | Dexs | $336.52M | -3.8% | -4.8% |
| 12 | Orca DEX | Dexs | $301.92M | -1.3% | +0.6% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.45B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.7% · Lending 16.5% · Dexs 15.3% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.8%

### Tokenised assets

$859.54M of tokenised real-world assets and equities are locked on Solana - 5.563% of chain TVL.

- OnRe (RWA): $295.39M
- Huma (RWA): $252.76M
- Solstice (Basis Trading): $201.84M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.46M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) - Fri, 16 Oct 2026 08:08:00 GMT
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) - Wed, 14 Oct 2026 15:05:00 GMT
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) - Mon, 12 Oct 2026 04:41:00 GMT
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0) | 2026-10-24 | pre-release |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-24
- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21

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

### Change over 24h (vs run at 2026-10-23T16:00:22Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,333.57 | 2,205.53 | -5.49% |
| Average non-vote TPS | 2,333.57 | 2,205.53 | -5.49% |
| Average slot time (ms) | 211.90 | 212.80 | +0.42% |
| Active validators | 656.00 | 664.00 | +1.22% |
| Delinquent validators | 20.00 | 14.00 | -30.00% |
| Solana TVL | 5,864,633,004.00 | 5,762,600,848.00 | -1.74% |
| SOL price | 104.63 | 100.37 | -4.07% |
| Stablecoin supply | 15,964,212,870.00 | 15,924,711,325.00 | -0.25% |
| 24h DEX volume | 2,039,384,832.23 | 1,997,070,440.37 | -2.07% |
| 24h chain fees | 11,291,169.22 | 10,552,167.09 | -6.54% |

### Change over 7d (vs run at 2026-10-17T14:31:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,884.13 | 2,205.53 | -54.84% |
| Average non-vote TPS | 1,806.58 | 2,205.53 | +22.08% |
| Average slot time (ms) | 216.70 | 212.80 | -1.80% |
| Active validators | 670.00 | 664.00 | -0.90% |
| Delinquent validators | 11.00 | 14.00 | +27.27% |
| Solana TVL | 5,952,090,339.00 | 5,762,600,848.00 | -3.18% |
| SOL price | 104.23 | 100.37 | -3.70% |
| Stablecoin supply | 16,028,651,978.00 | 15,924,711,325.00 | -0.65% |
| 24h DEX volume | 2,168,129,752.12 | 1,997,070,440.37 | -7.89% |
| 24h chain fees | 12,431,928.33 | 10,552,167.09 | -15.12% |

### Change over 30d (vs run at 2026-09-24T20:51:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,906.54 | 2,205.53 | -55.05% |
| Average non-vote TPS | 2,393.07 | 2,205.53 | -7.84% |
| Average slot time (ms) | 267.40 | 212.80 | -20.42% |
| Active validators | 676.00 | 664.00 | -1.78% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 6,484,914,945.00 | 5,762,600,848.00 | -11.14% |
| SOL price | 116.85 | 100.37 | -14.10% |
| Stablecoin supply | 16,427,048,512.00 | 15,924,711,325.00 | -3.06% |
| 24h DEX volume | 2,552,816,117.41 | 1,997,070,440.37 | -21.77% |
| 24h chain fees | 16,120,232.81 | 10,552,167.09 | -34.54% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
