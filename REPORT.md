# Solana Ecosystem Pulse

**Generated:** 2026-10-24T09:54:42Z · **Schema:** `1.0.0` · **Collection time:** 14.2s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $101.24 | -2.73% |
| Market cap | $59.70B | rank #7 |
| Total value locked | $5.78B | -1.81% |
| Stablecoin supply | $15.92B | -0.26% |
| DEX volume (24h) | $2.02B | -0.90% |
| Chain fees / REV (24h) | $10.54M | -8.15% |
| Non-vote TPS (1h avg) | 1,467 | peak 1,957 total |
| Active validators | 664 | 14 delinquent |
| Epoch 1066 | 68.25% complete | 137,142 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 120 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Throughput below normal band | Average TPS is 1,467; the healthy floor used here is 1,500. | `threshold` |
| [SERIOUS] | Average TPS is below its recent norm | Current 1,467.49 sits 6.3 sigma below the median of the last 120 runs (4,656.80, -68.5%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,467.5 average over the last 60 minutes; 1,454.5 in the latest sample.
- **Total TPS:** 1,467.5 average, 1,957.4 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 212.6 ms average (target 400 ms), worst 1-minute bucket 219.0 ms.
- **Block height:** 438,837,340 at absolute slot 460,806,858.
- **Epoch 1066:** slot 294,858 of 432,000 (68.25% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.589% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 95 ms |
| `solana-rpc.publicnode.com` | yes | 121 ms |
| `api.mainnet.solana.com` | yes | 88 ms |

## Validators & stake

- **664 active** validators, **14 delinquent** (2.06% by count, 0.066% by stake).
- **Total stake:** 437,116,782 SOL ($44.25B); stake rate 68.69% of total supply.
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

- **SOL:** $101.24 (-2.73% 24h, -3.53% 7d, -11.23% 30d). Market cap $59.70B, 24h volume $2.29B (3.83% of cap). Price source: `coingecko`.
- **TVL:** $5.78B across 332 protocols - rank #3 of 421 chains, 6.45% of all tracked chain TVL. -2.85% over 7d, -55.4% from its ATH.
- **Stablecoins:** $15.92B circulating on Solana (-0.65% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.02B in 24h, $12.48B over 7d across 138 venues. Volume/TVL turnover 0.349x per day.
- **REV (chain fees):** $10.54M in 24h, $440.35M over 30d. Retained chain revenue $3.96M (37.6% of fees). Annualised fees are 6.44% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,708,780 SOL circulating of 636,334,881 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.78B | -2.7% | -1.5% |
| 2 | Kamino Lend | Lending | $1.27B | -1.6% | -3.2% |
| 3 | Raydium AMM | Dexs | $1.15B | -2.3% | -2.0% |
| 4 | Binance Staked SOL | Liquid Staking | $1.08B | -1.8% | -1.2% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | -2.2% | -3.0% |
| 6 | Jupiter Lend | Lending | $1.02B | -0.1% | -6.4% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $717.81M | -1.9% | -2.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $535.45M | -1.9% | -1.9% |
| 9 | Sentora Curator | Risk Curators | $397.23M | -2.7% | -12.0% |
| 10 | Marinade Native | Staking Pool | $365.78M | -2.3% | -4.1% |
| 11 | PumpSwap | Dexs | $340.46M | -2.0% | -3.7% |
| 12 | Orca DEX | Dexs | $303.19M | -1.4% | +1.1% |

The top five protocols hold 40.9% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.50B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.8% · Lending 16.5% · Dexs 15.3% · Derivatives 5.1% · RWA 3.8% · Risk Curators 3.8%

### Tokenised assets

$859.57M of tokenised real-world assets and equities are locked on Solana - 5.545% of chain TVL.

- OnRe (RWA): $295.39M
- Huma (RWA): $252.77M
- Solstice (Basis Trading): $201.88M
- JupUSD (Basis Trading): $42.97M
- Plume Vaults (RWA): $36.44M

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

- [SIMD-0690: SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0670: SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-23
- [SIMD-0701: SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-22
- [SIMD-0675: SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-22
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

### Change over 24h (vs run at 2026-10-23T10:36:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 1,792.56 | 1,467.49 | -18.13% |
| Average non-vote TPS | 1,792.56 | 1,467.49 | -18.13% |
| Average slot time (ms) | 211.50 | 212.60 | +0.52% |
| Active validators | 656.00 | 664.00 | +1.22% |
| Delinquent validators | 20.00 | 14.00 | -30.00% |
| Solana TVL | 5,868,506,816.00 | 5,782,762,976.00 | -1.46% |
| SOL price | 104.11 | 101.24 | -2.76% |
| Stablecoin supply | 15,966,112,276.00 | 15,924,707,128.00 | -0.26% |
| 24h DEX volume | 2,074,632,771.23 | 2,020,963,434.37 | -2.59% |
| 24h chain fees | 11,333,373.27 | 10,536,967.05 | -7.03% |

### Change over 7d (vs run at 2026-10-17T09:48:37Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,356.06 | 1,467.49 | -66.31% |
| Average non-vote TPS | 1,277.52 | 1,467.49 | +14.87% |
| Average slot time (ms) | 217.10 | 212.60 | -2.07% |
| Active validators | 671.00 | 664.00 | -1.04% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 5,965,614,107.00 | 5,782,762,976.00 | -3.07% |
| SOL price | 104.84 | 101.24 | -3.43% |
| Stablecoin supply | 16,028,712,157.00 | 15,924,707,128.00 | -0.65% |
| 24h DEX volume | 2,499,920,867.12 | 2,020,963,434.37 | -19.16% |
| 24h chain fees | 12,237,570.18 | 10,536,967.05 | -13.90% |

### Change over 30d (vs run at 2026-09-24T20:51:18Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,906.54 | 1,467.49 | -70.09% |
| Average non-vote TPS | 2,393.07 | 1,467.49 | -38.68% |
| Average slot time (ms) | 267.40 | 212.60 | -20.49% |
| Active validators | 676.00 | 664.00 | -1.78% |
| Delinquent validators | 10.00 | 14.00 | +40.00% |
| Solana TVL | 6,484,914,945.00 | 5,782,762,976.00 | -10.83% |
| SOL price | 116.85 | 101.24 | -13.36% |
| Stablecoin supply | 16,427,048,512.00 | 15,924,707,128.00 | -3.06% |
| 24h DEX volume | 2,552,816,117.41 | 2,020,963,434.37 | -20.83% |
| 24h chain fees | 16,120,232.81 | 10,536,967.05 | -34.64% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 14.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
