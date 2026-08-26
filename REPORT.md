# Solana Ecosystem Pulse

**Generated:** 2026-08-26T19:30:01Z · **Schema:** `1.0.0` · **Collection time:** 39.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $96.76 | -1.28% |
| Market cap | $56.50B | rank #7 |
| Total value locked | $5.56B | -3.10% |
| Stablecoin supply | $16.32B | -0.66% |
| DEX volume (24h) | $2.93B | -2.04% |
| Chain fees / REV (24h) | $13.24M | -8.67% |
| Non-vote TPS (1h avg) | 2,616 | peak 4,999 total |
| Active validators | 685 | 10 delinquent |
| Epoch 1022 | 99.99% complete | 25 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 366.20 sits 16.5 sigma below the median of the last 64 runs (415.20, -11.8%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,557,854,195.00 sits 5.6 sigma above the median of the last 64 runs (4,871,641,651.50, +14.1%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 96.76 sits 7.5 sigma above the median of the last 64 runs (76.85, +25.9%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,616.5 average over the last 60 minutes; 2,410.6 in the latest sample.
- **Total TPS:** 4,472.9 average, 4,998.9 peak. Consensus votes account for 41.5% of all transactions.
- **Slot time:** 366.2 ms average (target 400 ms), worst 1-minute bucket 384.6 ms.
- **Block height:** 419,984,400 at absolute slot 441,935,975.
- **Epoch 1022:** slot 431,975 of 432,000 (99.99% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 764 ms |
| `solana-rpc.publicnode.com` | yes | 43 ms |
| `api.mainnet.solana.com` | yes | 267 ms |

## Validators & stake

- **685 active** validators, **10 delinquent** (1.44% by count, 0.059% by stake).
- **Total stake:** 435,118,104 SOL ($42.10B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.29% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.34%; 254 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 | 3.925% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 | 3.688% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 | 2.821% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 | 2.700% | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 | 2.116% | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 | 2.052% | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 | 1.973% | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 | 1.829% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 | 1.679% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 | 1.512% | 0% |

## Economics

- **SOL:** $96.76 (-1.28% 24h, +17.73% 7d, +28.12% 30d). Market cap $56.50B, 24h volume $3.05B (5.39% of cap). Price source: `coingecko`.
- **TVL:** $5.56B across 332 protocols - rank #2 of 465 chains, 6.35% of all tracked chain TVL. +13.53% over 7d, -58.0% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+1.91% 7d) - $2.94 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.93B in 24h, $21.98B over 7d across 119 venues. Volume/TVL turnover 0.528x per day.
- **REV (chain fees):** $13.24M in 24h, $291.25M over 30d. Retained chain revenue $5.82M (44.0% of fees). Annualised fees are 8.55% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,962,722 SOL circulating of 632,858,717 total (92.27%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.47B | -0.4% | +28.3% |
| 2 | Kamino Lend | Lending | $1.18B | -0.7% | +10.2% |
| 3 | Jupiter Lend | Lending | $1.05B | -0.9% | +10.1% |
| 4 | Raydium AMM | Dexs | $1.05B | -2.5% | +22.7% |
| 5 | Binance Staked SOL | Liquid Staking | $992.02M | -1.4% | +27.6% |
| 6 | Jito Liquid Staking | Liquid Staking | $971.59M | -1.4% | +26.2% |
| 7 | BlackRock BUIDL | RWA | $876.47M | +5.8% | +18.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $747.81M | -1.1% | +8.8% |
| 9 | Jupiter Staked SOL | Liquid Staking | $501.20M | -1.3% | +25.6% |
| 10 | xStocks | RWA | $425.86M | -1.3% | +11.7% |
| 11 | Marinade Native | Staking Pool | $384.80M | +0.2% | +80.4% |
| 12 | Sentora | Risk Curators | $363.19M | +0.0% | -0.8% |

The top five protocols hold 36.4% of Solana's tracked TVL. Summed across all 332 protocols the total is $15.79B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.8% · Lending 15.8% · Dexs 13.9% · RWA 13.0% · Derivatives 5.3% · Staking Pool 3.8%

### Tokenised assets

$2.43B of tokenised real-world assets and equities are locked on Solana - 15.415% of chain TVL.

- BlackRock BUIDL (RWA): $876.47M
- xStocks (RWA): $425.86M
- Solstice (Basis Trading): $303.02M
- OnRe (RWA): $277.78M
- Ondo Yield Assets (RWA): $179.26M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **1,037.3 unique fee payers** signed per block (1,568 distinct addresses in the union, 49.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) - Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) - Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) - Mon, 17 Aug 2026 00:00:00 GMT
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) - Thu, 13 Aug 2026 15:03:00 GMT
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) - Thu, 13 Aug 2026 02:06:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) | 2026-08-21 | pre-release |
| [v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) | 2026-08-21 | pre-release |
| [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) | 2026-08-13 | stable |
| [v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) | 2026-08-14 | pre-release |
| [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) | 2026-08-07 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-26
- [SIMD-0612: SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-26
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-26

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

### Change over 24h (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 4,472.91 | -2.03% |
| Average non-vote TPS | 2,708.19 | 2,616.46 | -3.39% |
| Average slot time (ms) | 366.20 | 366.20 | +0.00% |
| Active validators | 685.00 | 685.00 | +0.00% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,634,312,506.00 | 5,557,854,195.00 | -1.36% |
| SOL price | 98.47 | 96.76 | -1.74% |
| Stablecoin supply | 16,426,872,816.00 | 16,315,958,333.00 | -0.68% |
| 24h DEX volume | 2,996,141,158.64 | 2,934,986,439.19 | -2.04% |
| 24h chain fees | 14,491,360.16 | 13,235,652.04 | -8.67% |

### Change over 7d (vs run at 2026-08-19T18:15:30Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,093.61 | 4,472.91 | -12.19% |
| Average non-vote TPS | 3,460.99 | 2,616.46 | -24.40% |
| Average slot time (ms) | 416.70 | 366.20 | -12.12% |
| Active validators | 686.00 | 685.00 | -0.15% |
| Delinquent validators | 9.00 | 10.00 | +11.11% |
| Solana TVL | 5,060,698,995.00 | 5,557,854,195.00 | +9.82% |
| SOL price | 81.32 | 96.76 | +18.99% |
| Stablecoin supply | 16,009,704,067.00 | 16,315,958,333.00 | +1.91% |
| 24h DEX volume | 1,838,194,723.04 | 2,934,986,439.19 | +59.67% |
| 24h chain fees | 8,772,755.23 | 13,235,652.04 | +50.87% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 4,472.91 | +13.68% |
| Average non-vote TPS | 2,312.46 | 2,616.46 | +13.15% |
| Average slot time (ms) | 424.10 | 366.20 | -13.65% |
| Active validators | 692.00 | 685.00 | -1.01% |
| Delinquent validators | 8.00 | 10.00 | +25.00% |
| Solana TVL | 4,740,035,266.00 | 5,557,854,195.00 | +17.25% |
| SOL price | 72.81 | 96.76 | +32.89% |
| Stablecoin supply | 16,197,749,831.00 | 16,315,958,333.00 | +0.73% |
| 24h DEX volume | 1,636,927,091.91 | 2,934,986,439.19 | +79.30% |
| 24h chain fees | 7,777,648.77 | 13,235,652.04 | +70.18% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 39.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
