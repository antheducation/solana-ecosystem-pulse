# Solana Ecosystem Pulse

**Generated:** 2026-10-14T10:44:19Z · **Schema:** `1.0.0` · **Collection time:** 18.5s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $106.75 | +0.43% |
| Market cap | $62.90B | rank #7 |
| Total value locked | $6.07B | +1.00% |
| Stablecoin supply | $16.50B | +1.59% |
| DEX volume (24h) | $2.31B | +3.50% |
| Chain fees / REV (24h) | $11.69M | -10.78% |
| Non-vote TPS (1h avg) | 1,423 | peak 5,123 total |
| Active validators | 673 | 5 delinquent |
| Epoch 1057 | 42.95% complete | 246,438 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 105 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,423.1 average over the last 60 minutes; 1,195.0 in the latest sample.
- **Total TPS:** 4,517.9 average, 5,122.9 peak. Consensus votes account for 68.5% of all transactions.
- **Slot time:** 216.5 ms average (target 400 ms), worst 1-minute bucket 223.9 ms.
- **Block height:** 434,845,857 at absolute slot 456,809,562.
- **Epoch 1057:** slot 185,562 of 432,000 (42.95% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.603% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 195 ms |
| `solana-rpc.publicnode.com` | yes | 146 ms |
| `api.mainnet.solana.com` | yes | 225 ms |

## Validators & stake

- **673 active** validators, **5 delinquent** (0.74% by count, 0.001% by stake).
- **Total stake:** 438,131,312 SOL ($46.77B); stake rate 68.91% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.59% and top 33 hold 46.02% of active stake.
- **Commission:** median 5.0%, mean 12.80%; 230 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,794,097 | 4.061% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,830,160 | 3.613% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,313,027 | 2.810% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,142,984 | 2.543% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 10,763,192 | 2.457% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,407,225 | 2.147% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,240,434 | 2.109% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,700,931 | 1.758% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,906,931 | 1.576% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,638,868 | 1.515% | 0% |

## Economics

- **SOL:** $106.75 (+0.43% 24h, -9.32% 7d, +4.74% 30d). Market cap $62.90B, 24h volume $2.85B (4.53% of cap). Price source: `coingecko`.
- **TVL:** $6.07B across 324 protocols - rank #3 of 425 chains, 6.62% of all tracked chain TVL. -8.42% over 7d, -54.4% from its ATH.
- **Stablecoins:** $16.50B circulating on Solana (-2.44% 7d) - $2.72 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.31B in 24h, $13.18B over 7d across 133 venues. Volume/TVL turnover 0.381x per day.
- **REV (chain fees):** $11.69M in 24h, $465.02M over 30d. Retained chain revenue $4.17M (35.7% of fees). Annualised fees are 6.78% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,219,025 SOL circulating of 635,782,983 total (92.68%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +0.3% | -8.7% |
| 2 | Kamino Lend | Lending | $1.33B | +1.4% | -4.8% |
| 3 | Raydium AMM | Dexs | $1.21B | -0.0% | -9.9% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.13B | -0.1% | -10.0% |
| 5 | Jupiter Lend | Lending | $1.10B | -2.2% | -10.8% |
| 6 | Binance Staked SOL | Liquid Staking | $1.10B | -1.3% | -11.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $754.77M | -0.3% | -7.4% |
| 8 | Jupiter Staked SOL | Liquid Staking | $557.00M | -0.7% | -10.8% |
| 9 | Sentora Curator | Risk Curators | $467.74M | -0.8% | -4.9% |
| 10 | Marinade Native | Staking Pool | $393.18M | -1.5% | -12.5% |
| 11 | PumpSwap | Dexs | $358.54M | -1.0% | -10.5% |
| 12 | Orca DEX | Dexs | $299.62M | -1.0% | -6.5% |

The top five protocols hold 40.8% of Solana's tracked TVL. Summed across all 324 protocols the total is $16.16B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.4% · Lending 16.8% · Dexs 15.3% · Derivatives 5.1% · Risk Curators 4.1% · RWA 3.6%

### Tokenised assets

$861.18M of tokenised real-world assets and equities are locked on Solana - 5.330% of chain TVL.

- OnRe (RWA): $292.75M
- Huma (RWA): $248.64M
- Solstice (Basis Trading): $209.25M
- JupUSD (Basis Trading): $46.44M
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

- [SIMD-0565: [SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [SIMD-0511: SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-13
- [SIMD-0645: SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-10-13
- [SIMD-0630: SIMD-0630: FLH Slot Time Compensation](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-10-12
- [SIMD-0677: SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-12
- [SIMD-0690: SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0674: SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-11
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-11

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

### Change over 24h (vs run at 2026-10-13T13:02:51Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 5,012.70 | 4,517.95 | -9.87% |
| Average non-vote TPS | 1,960.24 | 1,423.12 | -27.40% |
| Average slot time (ms) | 219.10 | 216.50 | -1.19% |
| Active validators | 673.00 | 673.00 | +0.00% |
| Delinquent validators | 7.00 | 5.00 | -28.57% |
| Solana TVL | 6,068,456,089.00 | 6,066,631,253.00 | -0.03% |
| SOL price | 106.57 | 106.75 | +0.17% |
| Stablecoin supply | 16,241,381,985.00 | 16,500,896,449.00 | +1.60% |
| 24h DEX volume | 2,231,841,478.02 | 2,309,961,007.38 | +3.50% |
| 24h chain fees | 12,987,306.72 | 11,690,508.74 | -9.99% |

### Change over 7d (vs run at 2026-10-07T12:10:29Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,150.69 | 4,517.95 | +8.85% |
| Average non-vote TPS | 1,657.06 | 1,423.12 | -14.12% |
| Average slot time (ms) | 268.60 | 216.50 | -19.40% |
| Active validators | 670.00 | 673.00 | +0.45% |
| Delinquent validators | 11.00 | 5.00 | -54.55% |
| Solana TVL | 6,507,392,132.00 | 6,066,631,253.00 | -6.77% |
| SOL price | 117.28 | 106.75 | -8.98% |
| Stablecoin supply | 16,916,603,331.00 | 16,500,896,449.00 | -2.46% |
| 24h DEX volume | 2,052,545,605.65 | 2,309,961,007.38 | +12.54% |
| 24h chain fees | 16,043,229.31 | 11,690,508.74 | -27.13% |

### Change over 30d (vs run at 2026-09-14T21:06:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,277.98 | 4,517.95 | +5.61% |
| Average non-vote TPS | 2,155.99 | 1,423.12 | -33.99% |
| Average slot time (ms) | 317.90 | 216.50 | -31.90% |
| Active validators | 678.00 | 673.00 | -0.74% |
| Delinquent validators | 12.00 | 5.00 | -58.33% |
| Solana TVL | 5,949,162,754.00 | 6,066,631,253.00 | +1.97% |
| SOL price | 103.65 | 106.75 | +2.99% |
| Stablecoin supply | 16,354,375,710.00 | 16,500,896,449.00 | +0.90% |
| 24h DEX volume | 1,790,994,711.97 | 2,309,961,007.38 | +28.98% |
| 24h chain fees | 14,036,101.64 | 11,690,508.74 | -16.71% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.5s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
