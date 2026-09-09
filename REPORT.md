# Solana Ecosystem Pulse

**Generated:** 2026-09-09T20:07:25Z · **Schema:** `1.0.0` · **Collection time:** 14.5s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.19 | -1.01% |
| Market cap | $59.97B | rank #7 |
| Total value locked | $5.95B | +0.34% |
| Stablecoin supply | $16.63B | -0.40% |
| DEX volume (24h) | $2.71B | -0.36% |
| Chain fees / REV (24h) | $16.56M | +5.92% |
| Non-vote TPS (1h avg) | 2,342 | peak 5,149 total |
| Active validators | 675 | 13 delinquent |
| Epoch 1031 | 70.80% complete | 126,161 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 72 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,342.3 average over the last 60 minutes; 2,289.2 in the latest sample.
- **Total TPS:** 4,453.1 average, 5,149.1 peak. Consensus votes account for 47.4% of all transactions.
- **Slot time:** 319.3 ms average (target 400 ms), worst 1-minute bucket 331.5 ms.
- **Block height:** 423,741,361 at absolute slot 445,697,839.
- **Epoch 1031:** slot 305,839 of 432,000 (70.80% complete).
- **Client:** agave `4.2.2`, feature set `565236538`. Inflation 3.657% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 161 ms |
| `solana-rpc.publicnode.com` | yes | 133 ms |
| `api.mainnet.solana.com` | yes | 150 ms |

## Validators & stake

- **675 active** validators, **13 delinquent** (1.89% by count, 0.225% by stake).
- **Total stake:** 438,653,505 SOL ($44.83B); stake rate 69.22% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.30% and top 33 hold 45.77% of active stake.
- **Commission:** median 5.0%, mean 12.82%; 241 validators at 0% and 65 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,436,766 | 3.984% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,345,792 | 3.735% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,527,540 | 2.862% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,388,333 | 2.602% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,566,721 | 2.186% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,286,723 | 2.122% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,027,481 | 2.063% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,322,728 | 1.673% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,860,585 | 1.568% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,604,066 | 1.509% | 0% |

## Economics

- **SOL:** $102.19 (-1.01% 24h, +2.84% 7d, +34.28% 30d). Market cap $59.97B, 24h volume $2.89B (4.81% of cap). Price source: `coingecko`.
- **TVL:** $5.95B across 340 protocols - rank #2 of 466 chains, 6.73% of all tracked chain TVL. +5.03% over 7d, -55.1% from its ATH.
- **Stablecoins:** $16.63B circulating on Solana (+4.91% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.71B in 24h, $16.83B over 7d across 122 venues. Volume/TVL turnover 0.456x per day.
- **REV (chain fees):** $16.56M in 24h, $361.78M over 30d. Retained chain revenue $6.74M (40.7% of fees). Annualised fees are 10.08% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,250,200 SOL circulating of 633,736,427 total (92.51%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.59B | +0.4% | +3.9% |
| 2 | Kamino Lend | Lending | $1.35B | -0.8% | +12.1% |
| 3 | Raydium AMM | Dexs | $1.15B | +0.8% | +6.5% |
| 4 | Jupiter Lend | Lending | $1.10B | +1.8% | +5.6% |
| 5 | Binance Staked SOL | Liquid Staking | $1.08B | -0.7% | +4.1% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.06B | -0.5% | +5.9% |
| 7 | BlackRock BUIDL | RWA | $992.17M | +0.5% | +11.9% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $753.54M | -0.1% | +1.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $536.68M | -0.5% | +4.0% |
| 10 | xStocks | RWA | $440.15M | -0.9% | +1.9% |
| 11 | Marinade Native | Staking Pool | $397.30M | -2.1% | -0.1% |
| 12 | Sentora Curator | Risk Curators | $387.38M | +0.9% | +6.8% |

The top five protocols hold 37.0% of Solana's tracked TVL. Summed across all 340 protocols the total is $16.93B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 36.6% · Lending 16.1% · Dexs 13.9% · RWA 13.9% · Derivatives 4.9% · Staking Pool 3.6%

### Tokenised assets

$2.66B of tokenised real-world assets and equities are locked on Solana - 15.733% of chain TVL.

- BlackRock BUIDL (RWA): $992.17M
- xStocks (RWA): $440.15M
- OnRe (RWA): $305.80M
- Solstice (Basis Trading): $235.70M
- Ondo Yield Assets (RWA): $179.95M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **971.0 unique fee payers** signed per block (1,403 distinct addresses in the union, 51.8% overlap between blocks).

*Proxy metric. Unique fee payers observed in sampled blocks; the overlap figure shows how much address reuse there is between blocks. Not a daily-unique-address count - that needs an indexer.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) - Thu, 03 Sep 2026 15:15:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |
| [v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) | 2026-08-28 | pre-release |
| [v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) | 2026-08-28 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-09-08
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [SIMD-0464: amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

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

### Change over 24h (vs run at 2026-09-08T20:23:57Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,250.75 | 4,453.09 | +4.76% |
| Average non-vote TPS | 2,131.65 | 2,342.31 | +9.88% |
| Average slot time (ms) | 317.30 | 319.30 | +0.63% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 11.00 | 13.00 | +18.18% |
| Solana TVL | 5,936,538,125.00 | 5,948,260,786.00 | +0.20% |
| SOL price | 103.30 | 102.19 | -1.07% |
| Stablecoin supply | 16,696,076,448.00 | 16,629,873,212.00 | -0.40% |
| 24h DEX volume | 2,720,639,104.66 | 2,710,734,376.34 | -0.36% |
| 24h chain fees | 15,653,179.21 | 16,561,493.38 | +5.80% |

### Change over 7d (vs run at 2026-09-02T20:11:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,022.99 | 4,453.09 | +10.69% |
| Average non-vote TPS | 1,883.92 | 2,342.31 | +24.33% |
| Average slot time (ms) | 314.50 | 319.30 | +1.53% |
| Active validators | 677.00 | 675.00 | -0.30% |
| Delinquent validators | 18.00 | 13.00 | -27.78% |
| Solana TVL | 5,665,576,869.00 | 5,948,260,786.00 | +4.99% |
| SOL price | 99.75 | 102.19 | +2.45% |
| Stablecoin supply | 15,850,870,070.00 | 16,629,873,212.00 | +4.91% |
| 24h DEX volume | 2,171,560,050.49 | 2,710,734,376.34 | +24.83% |
| 24h chain fees | 12,646,787.67 | 16,561,493.38 | +30.95% |

### Change over 30d (vs run at 2026-08-10T18:39:26Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,162.64 | 4,453.09 | +6.98% |
| Average non-vote TPS | 2,537.28 | 2,342.31 | -7.68% |
| Average slot time (ms) | 422.40 | 319.30 | -24.41% |
| Active validators | 691.00 | 675.00 | -2.32% |
| Delinquent validators | 7.00 | 13.00 | +85.71% |
| Solana TVL | 4,826,095,598.00 | 5,948,260,786.00 | +23.25% |
| SOL price | 75.80 | 102.19 | +34.82% |
| Stablecoin supply | 16,312,056,347.00 | 16,629,873,212.00 | +1.95% |
| 24h DEX volume | 1,347,434,364.98 | 2,710,734,376.34 | +101.18% |
| 24h chain fees | 9,097,906.09 | 16,561,493.38 | +82.04% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 14.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
