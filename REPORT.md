# Solana Ecosystem Pulse

**Generated:** 2026-09-15T15:48:11Z · **Schema:** `1.0.0` · **Collection time:** 20.3s · **Sources OK:** 39/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $99.39 | -2.43% |
| Market cap | $58.32B | rank #7 |
| Total value locked | $5.84B | -0.01% |
| Stablecoin supply | $16.39B | +0.20% |
| DEX volume (24h) | $2.53B | +41.27% |
| Chain fees / REV (24h) | $13.58M | -3.25% |
| Non-vote TPS (1h avg) | 2,261 | peak 5,259 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1035 | 38.87% complete | 264,099 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 84 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (up 41.3% in 24h) | DEX volume changed +41.3% over the last day, past the 40% alert band. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,261.4 average over the last 60 minutes; 1,697.5 in the latest sample.
- **Total TPS:** 4,388.9 average, 5,259.5 peak. Consensus votes account for 48.5% of all transactions.
- **Slot time:** 316.5 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 425,329,729 at absolute slot 447,287,901.
- **Epoch 1035:** slot 167,901 of 432,000 (38.87% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.647% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 233 ms |
| `solana-rpc.publicnode.com` | yes | 136 ms |
| `api.mainnet.solana.com` | yes | 213 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.097% by stake).
- **Total stake:** 439,248,639 SOL ($43.66B); stake rate 69.27% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.34% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.35%; 243 validators at 0% and 62 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,757,712 | 4.047% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,373,377 | 3.731% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,492,605 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,369,566 | 2.591% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,669,319 | 2.203% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,225 | 2.109% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,035,103 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,372,355 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,944,775 | 1.583% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,553,626 | 1.493% | 0% |

## Economics

- **SOL:** $99.39 (-2.43% 24h, -3.78% 7d, +31.94% 30d). Market cap $58.32B, 24h volume $3.50B (5.99% of cap). Price source: `coingecko`.
- **TVL:** $5.84B across 338 protocols - rank #3 of 467 chains, 6.67% of all tracked chain TVL. -1.51% over 7d, -55.9% from its ATH.
- **Stablecoins:** $16.39B circulating on Solana (-1.85% 7d) - $2.81 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.53B in 24h, $18.20B over 7d across 123 venues. Volume/TVL turnover 0.434x per day.
- **REV (chain fees):** $13.58M in 24h, $394.95M over 30d. Retained chain revenue $5.20M (38.3% of fees). Annualised fees are 8.50% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,027,901 SOL circulating of 634,111,457 total (92.57%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.55B | -0.3% | -1.9% |
| 2 | Kamino Lend | Lending | $1.35B | -0.2% | +1.1% |
| 3 | Raydium AMM | Dexs | $1.13B | -0.4% | -1.3% |
| 4 | Jupiter Lend | Lending | $1.09B | -1.6% | -0.7% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | -1.8% | -3.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -1.6% | -3.0% |
| 7 | BlackRock BUIDL | RWA | $992.89M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $741.21M | -1.7% | -1.5% |
| 9 | Jupiter Staked SOL | Liquid Staking | $517.75M | -1.4% | -3.5% |
| 10 | Sentora Curator | Risk Curators | $385.25M | +0.4% | -0.4% |
| 11 | Marinade Native | Staking Pool | $381.47M | -1.4% | -7.1% |
| 12 | PumpSwap | Dexs | $325.62M | -2.7% | -4.8% |

The top five protocols hold 38.0% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.19B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.3% · Lending 16.6% · Dexs 14.2% · RWA 11.9% · Derivatives 5.0% · Risk Curators 3.7%

### Tokenised assets

$2.23B of tokenised real-world assets and equities are locked on Solana - 13.769% of chain TVL.

- BlackRock BUIDL (RWA): $992.89M
- OnRe (RWA): $300.57M
- Solstice (Basis Trading): $235.00M
- Huma Finance V2 (RWA): $187.53M
- Ondo Yield Assets (RWA): $179.87M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT

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

### Change over 24h (vs run at 2026-09-14T17:07:59Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,445.20 | 4,388.88 | -1.27% |
| Average non-vote TPS | 2,314.04 | 2,261.36 | -2.28% |
| Average slot time (ms) | 316.90 | 316.50 | -0.13% |
| Active validators | 680.00 | 677.00 | -0.44% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,897,760,887.00 | 5,835,026,620.00 | -1.06% |
| SOL price | 102.55 | 99.39 | -3.08% |
| Stablecoin supply | 16,352,410,301.00 | 16,387,600,113.00 | +0.22% |
| 24h DEX volume | 1,790,994,711.97 | 2,530,223,236.85 | +41.27% |
| 24h chain fees | 14,036,101.64 | 13,579,959.58 | -3.25% |

### Change over 7d (vs run at 2026-09-08T15:29:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,461.84 | 4,388.88 | -1.64% |
| Average non-vote TPS | 2,356.32 | 2,261.36 | -4.03% |
| Average slot time (ms) | 318.60 | 316.50 | -0.66% |
| Active validators | 675.00 | 677.00 | +0.30% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,858,003,246.00 | 5,835,026,620.00 | -0.39% |
| SOL price | 103.44 | 99.39 | -3.92% |
| Stablecoin supply | 16,694,571,293.00 | 16,387,600,113.00 | -1.84% |
| 24h DEX volume | 2,720,639,104.66 | 2,530,223,236.85 | -7.00% |
| 24h chain fees | 15,653,179.21 | 13,579,959.58 | -13.24% |

### Change over 30d (vs run at 2026-08-16T18:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,797.96 | 4,388.88 | +15.56% |
| Average non-vote TPS | 2,151.97 | 2,261.36 | +5.08% |
| Average slot time (ms) | 415.20 | 316.50 | -23.77% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,804,122,508.00 | 5,835,026,620.00 | +21.46% |
| SOL price | 75.15 | 99.39 | +32.26% |
| Stablecoin supply | 15,997,960,401.00 | 16,387,600,113.00 | +2.44% |
| 24h DEX volume | 1,169,008,711.04 | 2,530,223,236.85 | +116.44% |
| 24h chain fees | 8,145,711.86 | 13,579,959.58 | +66.71% |

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

This run made 41 HTTP calls (39 succeeded, 2 failed) in 20.3s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `github:agave_releases` - HTTP 403 (1 attempts)
- `github:simd_prs` - HTTP 403 (1 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
