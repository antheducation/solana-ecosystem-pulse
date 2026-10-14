# Solana Ecosystem Pulse

**Generated:** 2026-10-14T02:23:58Z · **Schema:** `1.0.0` · **Collection time:** 11.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $107.46 | +1.28% |
| Market cap | $63.34B | rank #7 |
| Total value locked | $6.05B | +0.22% |
| Stablecoin supply | $16.50B | +1.60% |
| DEX volume (24h) | $2.28B | +2.05% |
| Chain fees / REV (24h) | $11.69M | -10.80% |
| Non-vote TPS (1h avg) | 1,752 | peak 5,104 total |
| Active validators | 672 | 6 delinquent |
| Epoch 1057 | 10.98% complete | 384,580 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 104 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,751.7 average over the last 60 minutes; 1,570.5 in the latest sample.
- **Total TPS:** 4,817.4 average, 5,103.5 peak. Consensus votes account for 63.6% of all transactions.
- **Slot time:** 218.5 ms average (target 400 ms), worst 1-minute bucket 225.6 ms.
- **Block height:** 434,707,748 at absolute slot 456,671,420.
- **Epoch 1057:** slot 47,420 of 432,000 (10.98% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.603% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 152 ms |
| `solana-rpc.publicnode.com` | yes | 270 ms |
| `api.mainnet.solana.com` | yes | 100 ms |

## Validators & stake

- **672 active** validators, **6 delinquent** (0.88% by count, 0.439% by stake).
- **Total stake:** 438,131,312 SOL ($47.08B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.70% and top 33 hold 46.22% of active stake.
- **Commission:** median 5.0%, mean 12.82%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,794,097 | 4.079% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,830,160 | 3.629% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,027 | 2.823% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,142,984 | 2.555% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,763,192 | 2.467% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,407,225 | 2.157% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,434 | 2.118% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,700,931 | 1.765% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,906,931 | 1.583% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,868 | 1.522% | 0% |

## Economics

- **SOL:** $107.46 (+1.28% 24h, -9.74% 7d, +7.38% 30d). Market cap $63.34B, 24h volume $3.08B (4.86% of cap). Price source: `coingecko`.
- **TVL:** $6.05B across 324 protocols - rank #3 of 425 chains, 6.64% of all tracked chain TVL. -8.73% over 7d, -54.5% from its ATH.
- **Stablecoins:** $16.50B circulating on Solana (-2.43% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.28B in 24h, $12.91B over 7d across 133 venues. Volume/TVL turnover 0.377x per day.
- **REV (chain fees):** $11.69M in 24h, $464.86M over 30d. Retained chain revenue $4.17M (35.7% of fees). Annualised fees are 6.74% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,219,400 SOL circulating of 635,783,342 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +2.6% | -8.7% |
| 2 | Kamino Lend | Lending | $1.31B | +1.2% | -6.3% |
| 3 | Raydium AMM | Dexs | $1.21B | +1.1% | -10.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.12B | +3.9% | -10.6% |
| 5 | Jupiter Lend | Lending | $1.10B | +0.9% | -10.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.10B | +3.8% | -11.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $754.76M | +3.1% | -7.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $560.73M | +3.3% | -10.2% |
| 9 | Sentora Curator | Risk Curators | $472.40M | +0.1% | -4.0% |
| 10 | Marinade Native | Staking Pool | $394.66M | +4.0% | -12.2% |
| 11 | PumpSwap | Dexs | $357.63M | +0.9% | -10.7% |
| 12 | Orca DEX | Dexs | $302.56M | +1.0% | -5.6% |

The top five protocols hold 40.6% of Solana's tracked TVL. Summed across all 324 protocols the total is $16.14B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.7% · Dexs 15.4% · Derivatives 5.1% · Risk Curators 4.2% · RWA 3.6%

### Tokenised assets

$861.14M of tokenised real-world assets and equities are locked on Solana - 5.336% of chain TVL.

- OnRe (RWA): $292.57M
- Huma (RWA): $248.52M
- Solstice (Basis Trading): $209.27M
- JupUSD (Basis Trading): $46.62M
- Plume Vaults (RWA): $33.62M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) - Fri, 09 Oct 2026 12:46:00 GMT
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) - Thu, 08 Oct 2026 18:18:00 GMT
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) - Thu, 08 Oct 2026 08:33:00 GMT
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) - Wed, 07 Oct 2026 23:30:00 GMT
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) - Tue, 06 Oct 2026 19:38:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |
| [v4.3.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.1) | 2026-10-13 | pre-release |
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-13
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-13
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11

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

### Change over 24h (vs run at 2026-10-13T04:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,857.67 | 4,817.45 | -0.83% |
| Average non-vote TPS | 1,791.44 | 1,751.73 | -2.22% |
| Average slot time (ms) | 218.00 | 218.50 | +0.23% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,026,822,576.00 | 6,046,086,631.00 | +0.32% |
| SOL price | 107.65 | 107.46 | -0.18% |
| Stablecoin supply | 16,240,493,273.00 | 16,502,656,668.00 | +1.61% |
| 24h DEX volume | 1,866,875,583.02 | 2,277,563,559.38 | +22.00% |
| 24h chain fees | 12,980,703.44 | 11,688,355.74 | -9.96% |

### Change over 7d (vs run at 2026-10-07T02:58:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,983.12 | 4,817.45 | -3.32% |
| Average non-vote TPS | 2,500.28 | 1,751.73 | -29.94% |
| Average slot time (ms) | 270.10 | 218.50 | -19.10% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 8.00 | 6.00 | -25.00% |
| Solana TVL | 6,621,064,757.00 | 6,046,086,631.00 | -8.68% |
| SOL price | 118.29 | 107.46 | -9.16% |
| Stablecoin supply | 16,917,902,048.00 | 16,502,656,668.00 | -2.45% |
| 24h DEX volume | 2,039,240,588.65 | 2,277,563,559.38 | +11.69% |
| 24h chain fees | 16,053,410.31 | 11,688,355.74 | -27.19% |

### Change over 30d (vs run at 2026-09-13T19:56:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,911.91 | 4,817.45 | +23.15% |
| Average non-vote TPS | 1,778.64 | 1,751.73 | -1.51% |
| Average slot time (ms) | 315.70 | 218.50 | -30.79% |
| Active validators | 676.00 | 672.00 | -0.59% |
| Delinquent validators | 14.00 | 6.00 | -57.14% |
| Solana TVL | 5,861,539,247.00 | 6,046,086,631.00 | +3.15% |
| SOL price | 100.85 | 107.46 | +6.55% |
| Stablecoin supply | 16,525,835,618.00 | 16,502,656,668.00 | -0.14% |
| 24h DEX volume | 1,691,135,695.08 | 2,277,563,559.38 | +34.68% |
| 24h chain fees | 13,515,656.40 | 11,688,355.74 | -13.52% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 11.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
