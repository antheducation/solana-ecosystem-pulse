# Solana Ecosystem Pulse

**Generated:** 2026-08-26T12:23:42Z · **Schema:** `1.0.0` · **Collection time:** 44.7s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $97.02 | -0.99% |
| Market cap | $56.59B | rank #7 |
| Total value locked | $5.60B | -2.45% |
| Stablecoin supply | $16.32B | -0.67% |
| DEX volume (24h) | $2.93B | -2.04% |
| Chain fees / REV (24h) | $13.13M | -9.36% |
| Non-vote TPS (1h avg) | 1,625 | peak 3,872 total |
| Active validators | 684 | 11 delinquent |
| Epoch 1022 | 83.82% complete | 69,897 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 64 historical runs, sigma = 3.0).

Critical 0 · Serious 3 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 365.20 sits 16.9 sigma below the median of the last 64 runs (415.20, -12.0%). | `zscore` |
| [SERIOUS] | Solana TVL is above its recent norm | Current 5,596,733,884.00 sits 7.8 sigma above the median of the last 64 runs (4,856,279,035.50, +15.2%). | `zscore` |
| [SERIOUS] | SOL price is above its recent norm | Current 97.02 sits 8.4 sigma above the median of the last 64 runs (76.77, +26.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,624.7 average over the last 60 minutes; 1,647.4 in the latest sample.
- **Total TPS:** 3,489.6 average, 3,872.1 peak. Consensus votes account for 53.4% of all transactions.
- **Slot time:** 365.2 ms average (target 400 ms), worst 1-minute bucket 375.0 ms.
- **Block height:** 419,914,612 at absolute slot 441,866,103.
- **Epoch 1022:** slot 362,103 of 432,000 (83.82% complete).
- **Client:** agave `4.2.0`, feature set `565236538`. Inflation 3.679% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 294 ms |
| `solana-rpc.publicnode.com` | yes | 26 ms |
| `api.mainnet.solana.com` | yes | 285 ms |

## Validators & stake

- **684 active** validators, **11 delinquent** (1.58% by count, 0.067% by stake).
- **Total stake:** 435,118,104 SOL ($42.22B); stake rate 68.75% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.87% of active stake.
- **Commission:** median 5.0%, mean 12.19%; 255 validators at 0% and 62 at 100%.

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

- **SOL:** $97.02 (-0.99% 24h, +25.21% 7d, +26.83% 30d). Market cap $56.59B, 24h volume $3.32B (5.87% of cap). Price source: `coingecko`.
- **TVL:** $5.60B across 330 protocols - rank #2 of 465 chains, 6.37% of all tracked chain TVL. +14.29% over 7d, -57.7% from its ATH.
- **Stablecoins:** $16.32B circulating on Solana (+1.90% 7d) - $2.92 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.93B in 24h, $21.98B over 7d across 119 venues. Volume/TVL turnover 0.524x per day.
- **REV (chain fees):** $13.13M in 24h, $291.15M over 30d. Retained chain revenue $5.82M (44.3% of fees). Annualised fees are 8.47% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 583,375,152 SOL circulating of 632,859,013 total (92.18%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.48B | -1.3% | +28.7% |
| 2 | Kamino Lend | Lending | $1.18B | -3.0% | +10.7% |
| 3 | Raydium AMM | Dexs | $1.07B | -3.9% | +24.7% |
| 4 | Jupiter Lend | Lending | $1.05B | -2.9% | +10.3% |
| 5 | Binance Staked SOL | Liquid Staking | $992.67M | -1.9% | +27.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $977.23M | -2.0% | +26.9% |
| 7 | BlackRock BUIDL | RWA | $876.38M | +5.8% | +18.2% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $748.71M | -1.9% | +8.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $501.53M | -2.6% | +25.7% |
| 10 | xStocks | RWA | $428.44M | +1.5% | +12.3% |
| 11 | Marinade Native | Staking Pool | $384.26M | -0.1% | +80.1% |
| 12 | Sentora | Risk Curators | $362.73M | -0.0% | -0.9% |

The top five protocols hold 36.5% of Solana's tracked TVL. Summed across all 330 protocols the total is $15.84B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 35.8% · Lending 15.8% · Dexs 14.0% · RWA 13.0% · Derivatives 5.3% · Staking Pool 3.8%

### Tokenised assets

$2.44B of tokenised real-world assets and equities are locked on Solana - 15.392% of chain TVL.

- BlackRock BUIDL (RWA): $876.38M
- xStocks (RWA): $428.44M
- Solstice (Basis Trading): $303.04M
- OnRe (RWA): $277.68M
- Ondo Yield Assets (RWA): $178.69M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **916.7 unique fee payers** signed per block (1,249 distinct addresses in the union, 54.6% overlap between blocks).

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

- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-26
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-08-26
- [Remove floating point arithmetic from Runtime critical inflation and rent path](https://github.com/solana-foundation/solana-improvement-documents/pull/607) - updated 2026-08-26
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-25
- [SIMD-0599: SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-25
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25

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

### Change over 24h (vs run at 2026-08-25T12:21:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,629.28 | 3,489.57 | -3.85% |
| Average non-vote TPS | 1,760.33 | 1,624.74 | -7.70% |
| Average slot time (ms) | 364.50 | 365.20 | +0.19% |
| Active validators | 685.00 | 684.00 | -0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 5,744,421,267.00 | 5,596,733,884.00 | -2.57% |
| SOL price | 98.21 | 97.02 | -1.21% |
| Stablecoin supply | 16,426,518,373.00 | 16,315,003,426.00 | -0.68% |
| 24h DEX volume | 2,996,141,158.64 | 2,934,986,439.19 | -2.04% |
| 24h chain fees | 14,392,606.16 | 13,134,401.04 | -8.74% |

### Change over 7d (vs run at 2026-08-19T12:19:09Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,485.50 | 3,489.57 | +0.12% |
| Average non-vote TPS | 1,849.57 | 1,624.74 | -12.16% |
| Average slot time (ms) | 414.10 | 365.20 | -11.81% |
| Active validators | 685.00 | 684.00 | -0.15% |
| Delinquent validators | 10.00 | 11.00 | +10.00% |
| Solana TVL | 4,914,919,992.00 | 5,596,733,884.00 | +13.87% |
| SOL price | 77.39 | 97.02 | +25.37% |
| Stablecoin supply | 16,008,130,055.00 | 16,315,003,426.00 | +1.92% |
| 24h DEX volume | 1,838,194,723.04 | 2,934,986,439.19 | +59.67% |
| 24h chain fees | 8,688,793.23 | 13,134,401.04 | +51.16% |

### Change over 30d (vs run at 2026-08-06T19:58:38Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,934.59 | 3,489.57 | -11.31% |
| Average non-vote TPS | 2,312.46 | 1,624.74 | -29.74% |
| Average slot time (ms) | 424.10 | 365.20 | -13.89% |
| Active validators | 692.00 | 684.00 | -1.16% |
| Delinquent validators | 8.00 | 11.00 | +37.50% |
| Solana TVL | 4,740,035,266.00 | 5,596,733,884.00 | +18.07% |
| SOL price | 72.81 | 97.02 | +33.25% |
| Stablecoin supply | 16,197,749,831.00 | 16,315,003,426.00 | +0.72% |
| 24h DEX volume | 1,636,927,091.91 | 2,934,986,439.19 | +79.30% |
| 24h chain fees | 7,777,648.77 | 13,134,401.04 | +68.87% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 44.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
