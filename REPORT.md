# Solana Ecosystem Pulse

**Generated:** 2026-09-08T10:11:04Z · **Schema:** `1.0.0` · **Collection time:** 30.0s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $103.55 | -1.20% |
| Market cap | $60.70B | rank #7 |
| Total value locked | $5.87B | -2.07% |
| Stablecoin supply | $16.70B | -0.27% |
| DEX volume (24h) | $2.87B | -1.12% |
| Chain fees / REV (24h) | $16.00M | +9.17% |
| Non-vote TPS (1h avg) | 1,337 | peak 3,727 total |
| Active validators | 675 | 13 delinquent |
| Epoch 1030 | 81.56% complete | 79,665 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 71 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,336.5 average over the last 60 minutes; 1,333.5 in the latest sample.
- **Total TPS:** 3,448.2 average, 3,727.0 peak. Consensus votes account for 61.2% of all transactions.
- **Slot time:** 315.4 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 423,356,367 at absolute slot 445,312,335.
- **Epoch 1030:** slot 352,335 of 432,000 (81.56% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.659% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 732 ms |
| `solana-rpc.publicnode.com` | yes | 120 ms |
| `api.mainnet.solana.com` | yes | 720 ms |

## Validators & stake

- **675 active** validators, **13 delinquent** (1.89% by count, 0.123% by stake).
- **Total stake:** 439,477,988 SOL ($45.51B); stake rate 69.36% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.22% and top 33 hold 45.66% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 243 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,438,541 | 3.973% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,336,964 | 3.722% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,517,399 | 2.852% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,397,824 | 2.597% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,564,412 | 2.179% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,181,909 | 2.092% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,038,443 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,384,461 | 1.682% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,858,929 | 1.563% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,595,421 | 1.503% | 0% |

## Economics

- **SOL:** $103.55 (-1.20% 24h, +1.56% 7d, +35.57% 30d). Market cap $60.70B, 24h volume $2.93B (4.83% of cap). Price source: `coingecko`.
- **TVL:** $5.87B across 340 protocols - rank #2 of 466 chains, 6.69% of all tracked chain TVL. -1.93% over 7d, -55.7% from its ATH.
- **Stablecoins:** $16.70B circulating on Solana (+4.55% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.87B in 24h, $15.45B over 7d across 121 venues. Volume/TVL turnover 0.489x per day.
- **REV (chain fees):** $16.00M in 24h, $352.43M over 30d. Retained chain revenue $6.63M (41.5% of fees). Annualised fees are 9.62% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,165,323 SOL circulating of 633,642,603 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.57B | -1.8% | -0.3% |
| 2 | Kamino Lend | Lending | $1.33B | -0.6% | -5.0% |
| 3 | Raydium AMM | Dexs | $1.13B | -0.9% | +1.2% |
| 4 | Jupiter Lend | Lending | $1.09B | -1.3% | -0.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.07B | -1.5% | +0.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | -1.5% | +1.6% |
| 7 | BlackRock BUIDL | RWA | $977.90M | +0.0% | +10.3% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $748.36M | -1.0% | -1.9% |
| 9 | Jupiter Staked SOL | Liquid Staking | $532.92M | -1.5% | -0.3% |
| 10 | xStocks | RWA | $441.65M | -1.9% | -0.0% |
| 11 | Marinade Native | Staking Pool | $405.83M | -2.2% | -4.2% |
| 12 | Sentora Curator | Risk Curators | $387.08M | -0.0% | +7.3% |

The top five protocols hold 36.8% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.80B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.0% · RWA 14.0% · Dexs 13.9% · Derivatives 4.9% · Staking Pool 3.7%

### Tokenised assets

$2.67B of tokenised real-world assets and equities are locked on Solana - 15.865% of chain TVL.

- BlackRock BUIDL (RWA): $977.90M
- xStocks (RWA): $441.65M
- OnRe (RWA): $302.84M
- Solstice (Basis Trading): $237.90M
- Huma Finance V2 (RWA): $186.50M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **927.0 unique fee payers** signed per block (1,339 distinct addresses in the union, 51.9% overlap between blocks).

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
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-08-31
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-31

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

### Change over 24h (vs run at 2026-09-07T10:52:34Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,317.21 | 3,448.21 | +3.95% |
| Average non-vote TPS | 1,194.13 | 1,336.54 | +11.93% |
| Average slot time (ms) | 316.40 | 315.40 | -0.32% |
| Active validators | 674.00 | 675.00 | +0.15% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,924,761,773.00 | 5,869,138,160.00 | -0.94% |
| SOL price | 105.05 | 103.55 | -1.43% |
| Stablecoin supply | 16,740,615,784.00 | 16,695,009,953.00 | -0.27% |
| 24h DEX volume | 1,960,574,882.81 | 2,872,025,884.66 | +46.49% |
| 24h chain fees | 10,482,001.50 | 15,999,657.21 | +52.64% |

### Change over 7d (vs run at 2026-09-01T10:37:53Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,426.48 | 3,448.21 | +0.63% |
| Average non-vote TPS | 1,291.44 | 1,336.54 | +3.49% |
| Average slot time (ms) | 316.80 | 315.40 | -0.44% |
| Active validators | 680.00 | 675.00 | -0.74% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,808,427,098.00 | 5,869,138,160.00 | +1.05% |
| SOL price | 102.48 | 103.55 | +1.04% |
| Stablecoin supply | 16,130,106,220.00 | 16,695,009,953.00 | +3.50% |
| 24h DEX volume | 2,457,757,824.05 | 2,872,025,884.66 | +16.86% |
| 24h chain fees | 13,288,721.08 | 15,999,657.21 | +20.40% |

### Change over 30d (vs run at 2026-08-09T18:21:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,304.40 | 3,448.21 | -19.89% |
| Average non-vote TPS | 2,694.81 | 1,336.54 | -50.40% |
| Average slot time (ms) | 426.40 | 315.40 | -26.03% |
| Active validators | 691.00 | 675.00 | -2.32% |
| Delinquent validators | 7.00 | 13.00 | +85.71% |
| Solana TVL | 4,857,325,993.00 | 5,869,138,160.00 | +20.83% |
| SOL price | 77.09 | 103.55 | +34.32% |
| Stablecoin supply | 16,258,695,331.00 | 16,695,009,953.00 | +2.68% |
| 24h DEX volume | 1,493,144,029.54 | 2,872,025,884.66 | +92.35% |
| 24h chain fees | 9,274,886.08 | 15,999,657.21 | +72.51% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 29.9s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
