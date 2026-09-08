# Solana Ecosystem Pulse

**Generated:** 2026-09-08T01:42:47Z · **Schema:** `1.0.0` · **Collection time:** 33.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $104.14 | -1.05% |
| Market cap | $61.04B | rank #7 |
| Total value locked | $5.91B | -0.52% |
| Stablecoin supply | $16.74B | +0.33% |
| DEX volume (24h) | $2.87B | -1.12% |
| Chain fees / REV (24h) | $13.42M | -8.43% |
| Non-vote TPS (1h avg) | 1,425 | peak 3,922 total |
| Active validators | 676 | 12 delinquent |
| Epoch 1030 | 59.23% complete | 176,140 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 70 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,424.8 average over the last 60 minutes; 1,495.2 in the latest sample.
- **Total TPS:** 3,552.1 average, 3,921.8 peak. Consensus votes account for 59.9% of all transactions.
- **Slot time:** 316.1 ms average (target 400 ms), worst 1-minute bucket 329.7 ms.
- **Block height:** 423,260,020 at absolute slot 445,215,860.
- **Epoch 1030:** slot 255,860 of 432,000 (59.23% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.659% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 593 ms |
| `solana-rpc.publicnode.com` | yes | 59 ms |
| `api.mainnet.solana.com` | yes | 575 ms |

## Validators & stake

- **676 active** validators, **12 delinquent** (1.74% by count, 0.011% by stake).
- **Total stake:** 439,477,988 SOL ($45.77B); stake rate 69.36% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.19% and top 33 hold 45.61% of active stake.
- **Commission:** median 5.0%, mean 12.80%; 243 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,438,541 | 3.968% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,336,964 | 3.718% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,517,399 | 2.849% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,397,824 | 2.594% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,564,412 | 2.177% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,181,909 | 2.090% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,038,443 | 2.057% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,384,461 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,858,929 | 1.561% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,595,421 | 1.501% | 0% |

## Economics

- **SOL:** $104.14 (-1.05% 24h, +0.96% 7d, +37.11% 30d). Market cap $61.04B, 24h volume $3.09B (5.06% of cap). Price source: `coingecko`.
- **TVL:** $5.91B across 339 protocols - rank #2 of 466 chains, 6.71% of all tracked chain TVL. -1.24% over 7d, -55.4% from its ATH.
- **Stablecoins:** $16.74B circulating on Solana (+4.86% 7d) - $2.83 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.87B in 24h, $15.45B over 7d across 121 venues. Volume/TVL turnover 0.486x per day.
- **REV (chain fees):** $13.42M in 24h, $343.81M over 30d. Retained chain revenue $5.93M (44.2% of fees). Annualised fees are 8.02% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.7% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,165,611 SOL circulating of 633,642,890 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.58B | -2.4% | +0.6% |
| 2 | Kamino Lend | Lending | $1.33B | -1.1% | -4.7% |
| 3 | Raydium AMM | Dexs | $1.14B | -0.9% | +2.3% |
| 4 | Jupiter Lend | Lending | $1.09B | -2.4% | +0.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | -2.5% | +0.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | -2.4% | +2.3% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +0.0% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $752.63M | -1.7% | -1.4% |
| 9 | Jupiter Staked SOL | Liquid Staking | $536.50M | -2.6% | +0.4% |
| 10 | xStocks | RWA | $445.93M | -1.7% | +0.9% |
| 11 | Marinade Native | Staking Pool | $410.80M | -1.9% | -3.0% |
| 12 | Sentora Curator | Risk Curators | $386.92M | -0.5% | +7.2% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.90B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.0% · RWA 14.0% · Dexs 13.9% · Derivatives 4.9% · Staking Pool 3.8%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.813% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $445.93M
- OnRe (RWA): $302.69M
- Solstice (Basis Trading): $237.93M
- Huma Finance V2 (RWA): $186.50M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **868.7 unique fee payers** signed per block (1,183 distinct addresses in the union, 54.6% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) - Wed, 02 Sep 2026 09:00:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | pre-release |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0558: SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0608: SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31

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

### Change over 24h (vs run at 2026-09-07T01:32:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,929.51 | 3,552.09 | -9.60% |
| Average non-vote TPS | 1,812.58 | 1,424.81 | -21.39% |
| Average slot time (ms) | 317.50 | 316.10 | -0.44% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 17.00 | 12.00 | -29.41% |
| Solana TVL | 5,924,761,773.00 | 5,910,151,740.00 | -0.25% |
| SOL price | 105.52 | 104.14 | -1.31% |
| Stablecoin supply | 16,686,042,305.00 | 16,740,790,725.00 | +0.33% |
| 24h DEX volume | 1,960,574,882.81 | 2,872,029,701.66 | +46.49% |
| 24h chain fees | 10,482,001.50 | 13,419,392.83 | +28.02% |

### Change over 7d (vs run at 2026-09-01T02:18:15Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,129.22 | 3,552.09 | -13.98% |
| Average non-vote TPS | 2,000.29 | 1,424.81 | -28.77% |
| Average slot time (ms) | 318.50 | 316.10 | -0.75% |
| Active validators | 680.00 | 676.00 | -0.59% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 5,962,784,320.00 | 5,910,151,740.00 | -0.88% |
| SOL price | 103.02 | 104.14 | +1.09% |
| Stablecoin supply | 16,123,159,936.00 | 16,740,790,725.00 | +3.83% |
| 24h DEX volume | 2,457,773,259.05 | 2,872,029,701.66 | +16.85% |
| 24h chain fees | 13,276,210.28 | 13,419,392.83 | +1.08% |

### Change over 30d (vs run at 2026-08-08T18:19:20Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,014.93 | 3,552.09 | -11.53% |
| Average non-vote TPS | 2,401.41 | 1,424.81 | -40.67% |
| Average slot time (ms) | 424.90 | 316.10 | -25.61% |
| Active validators | 691.00 | 676.00 | -2.17% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,824,990,783.00 | 5,910,151,740.00 | +22.49% |
| SOL price | 76.22 | 104.14 | +36.63% |
| Stablecoin supply | 16,242,440,945.00 | 16,740,790,725.00 | +3.07% |
| 24h DEX volume | 1,362,524,618.02 | 2,872,029,701.66 | +110.79% |
| 24h chain fees | 8,154,900.02 | 13,419,392.83 | +64.56% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 32.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
