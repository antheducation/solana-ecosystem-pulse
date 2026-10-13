# Solana Ecosystem Pulse

**Generated:** 2026-10-13T04:10:46Z · **Schema:** `1.0.0` · **Collection time:** 16.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $107.65 | -3.55% |
| Market cap | $63.38B | rank #7 |
| Total value locked | $6.03B | -2.50% |
| Stablecoin supply | $16.24B | -0.73% |
| DEX volume (24h) | $1.87B | +46.19% |
| Chain fees / REV (24h) | $12.98M | +14.85% |
| Non-vote TPS (1h avg) | 1,791 | peak 5,842 total |
| Active validators | 672 | 8 delinquent |
| Epoch 1056 | 26.19% complete | 318,858 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 104 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 46.2% in 24h) | DEX volume changed +46.2% over the last day, past the 40% alert band. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,791.4 average over the last 60 minutes; 1,753.3 in the latest sample.
- **Total TPS:** 4,857.7 average, 5,841.5 peak. Consensus votes account for 63.1% of all transactions.
- **Slot time:** 218.0 ms average (target 400 ms), worst 1-minute bucket 228.1 ms.
- **Block height:** 434,341,811 at absolute slot 456,305,142.
- **Epoch 1056:** slot 113,142 of 432,000 (26.19% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.605% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 137 ms |
| `solana-rpc.publicnode.com` | yes | 237 ms |
| `api.mainnet.solana.com` | yes | 130 ms |

## Validators & stake

- **672 active** validators, **8 delinquent** (1.18% by count, 0.013% by stake).
- **Total stake:** 438,790,522 SOL ($47.24B); stake rate 69.02% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.56% and top 33 hold 45.94% of active stake.
- **Commission:** median 5.0%, mean 12.81%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,789,243 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,958,932 | 3.638% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,305,752 | 2.805% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,149,129 | 2.541% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,758,268 | 2.452% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,401,788 | 2.143% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,237,163 | 2.105% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,681,229 | 1.751% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,812,456 | 1.553% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,148 | 1.513% | 0% |

## Economics

- **SOL:** $107.65 (-3.55% 24h, -10.30% 7d, +5.97% 30d). Market cap $63.38B, 24h volume $3.95B (6.23% of cap). Price source: `coingecko`.
- **TVL:** $6.03B across 339 protocols - rank #3 of 469 chains, 6.61% of all tracked chain TVL. -11.14% over 7d, -54.5% from its ATH.
- **Stablecoins:** $16.24B circulating on Solana (-4.75% 7d) - $2.69 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.87B in 24h, $12.69B over 7d across 131 venues. Volume/TVL turnover 0.310x per day.
- **REV (chain fees):** $12.98M in 24h, $466.91M over 30d. Retained chain revenue $4.48M (34.5% of fees). Annualised fees are 7.48% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,163,051 SOL circulating of 635,721,665 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.79B | -2.8% | -9.8% |
| 2 | Kamino Lend | Lending | $1.30B | -2.8% | -7.0% |
| 3 | Raydium AMM | Dexs | $1.20B | -4.7% | -11.3% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.11B | -4.8% | -11.9% |
| 5 | Jupiter Lend | Lending | $1.11B | -3.5% | -9.3% |
| 6 | Binance Staked SOL | Liquid Staking | $1.09B | -4.7% | -12.0% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $749.99M | -3.9% | -8.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $551.06M | -4.5% | -12.0% |
| 9 | Sentora Curator | Risk Curators | $471.73M | -4.1% | +3.1% |
| 10 | Marinade Native | Staking Pool | $392.30M | -5.1% | -12.8% |
| 11 | PumpSwap | Dexs | $354.40M | -4.2% | -11.3% |
| 12 | Orca DEX | Dexs | $299.62M | -3.9% | -7.3% |

The top five protocols hold 40.5% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.07B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.1% · Lending 16.8% · Dexs 15.3% · Derivatives 5.3% · Risk Curators 4.2% · RWA 3.7%

### Tokenised assets

$879.28M of tokenised real-world assets and equities are locked on Solana - 5.473% of chain TVL.

- OnRe (RWA): $292.58M
- Huma (RWA): $252.03M
- Solstice (Basis Trading): $209.23M
- JupUSD (Basis Trading): $46.70M
- Plume Vaults (RWA): $33.61M

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
| [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) | 2026-10-08 | pre-release |
| [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) | 2026-10-03 | pre-release |
| [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) | 2026-09-28 | pre-release |
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11
- [SIMD-0683: SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11
- [SIMD-0177: SIMD-0177: Program Runtime ABI v2](https://github.com/solana-foundation/solana-improvement-documents/pull/177) - updated 2026-10-10

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

### Change over 24h (vs run at 2026-10-12T02:55:24Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,135.89 | 4,857.67 | -5.42% |
| Average non-vote TPS | 2,087.65 | 1,791.44 | -14.19% |
| Average slot time (ms) | 219.70 | 218.00 | -0.77% |
| Active validators | 673.00 | 672.00 | -0.15% |
| Delinquent validators | 8.00 | 8.00 | +0.00% |
| Solana TVL | 6,254,990,671.00 | 6,026,822,576.00 | -3.65% |
| SOL price | 112.07 | 107.65 | -3.94% |
| Stablecoin supply | 16,359,537,345.00 | 16,240,493,273.00 | -0.73% |
| 24h DEX volume | 1,246,835,645.31 | 1,866,875,583.02 | +49.73% |
| 24h chain fees | 11,260,863.80 | 12,980,703.44 | +15.27% |

### Change over 7d (vs run at 2026-10-06T03:32:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,576.27 | 4,857.67 | +6.15% |
| Average non-vote TPS | 2,076.07 | 1,791.44 | -13.71% |
| Average slot time (ms) | 267.60 | 218.00 | -18.54% |
| Active validators | 672.00 | 672.00 | +0.00% |
| Delinquent validators | 13.00 | 8.00 | -38.46% |
| Solana TVL | 6,796,887,845.00 | 6,026,822,576.00 | -11.33% |
| SOL price | 119.95 | 107.65 | -10.25% |
| Stablecoin supply | 17,051,507,064.00 | 16,240,493,273.00 | -4.76% |
| 24h DEX volume | 1,904,732,429.50 | 1,866,875,583.02 | -1.99% |
| 24h chain fees | 16,107,910.12 | 12,980,703.44 | -19.41% |

### Change over 30d (vs run at 2026-09-12T19:46:08Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,285.77 | 4,857.67 | +13.34% |
| Average non-vote TPS | 2,164.34 | 1,791.44 | -17.23% |
| Average slot time (ms) | 317.70 | 218.00 | -31.38% |
| Active validators | 679.00 | 672.00 | -1.03% |
| Delinquent validators | 11.00 | 8.00 | -27.27% |
| Solana TVL | 5,903,101,578.00 | 6,026,822,576.00 | +2.10% |
| SOL price | 101.32 | 107.65 | +6.25% |
| Stablecoin supply | 16,554,268,556.00 | 16,240,493,273.00 | -1.90% |
| 24h DEX volume | 3,183,599,712.43 | 1,866,875,583.02 | -41.36% |
| 24h chain fees | 17,875,390.26 | 12,980,703.44 | -27.38% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 16.8s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
