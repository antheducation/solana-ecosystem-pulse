# Solana Ecosystem Pulse

**Generated:** 2026-09-25T02:09:36Z · **Schema:** `1.0.0` · **Collection time:** 19.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.12 | +3.42% |
| Market cap | $69.45B | rank #7 |
| Total value locked | $6.49B | +0.54% |
| Stablecoin supply | $17.69B | +7.68% |
| DEX volume (24h) | $2.26B | -11.37% |
| Chain fees / REV (24h) | $15.93M | -1.06% |
| Non-vote TPS (1h avg) | 1,833 | peak 4,920 total |
| Active validators | 675 | 10 delinquent |
| Epoch 1042 | 16.07% complete | 362,557 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 92 historical runs, sigma = 3.0).

Critical 0 · Serious 1 · Warning 2 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 7.7% in 24h) | Stablecoin supply changed +7.7% over the last day, past the 3% alert band. | `threshold` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Stablecoin supply is above its recent norm | Current 17,687,554,466.00 sits 3.7 sigma above the median of the last 92 runs (16,335,961,270.00, +8.3%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 1,832.7 average over the last 60 minutes; 2,063.6 in the latest sample.
- **Total TPS:** 4,337.9 average, 4,919.6 peak. Consensus votes account for 57.8% of all transactions.
- **Slot time:** 268.2 ms average (target 400 ms), worst 1-minute bucket 281.7 ms.
- **Block height:** 428,253,431 at absolute slot 450,213,443.
- **Epoch 1042:** slot 69,443 of 432,000 (16.07% complete).
- **Client:** agave `4.3.0`, feature set `3383571666`. Inflation 3.632% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 263 ms |
| `solana-rpc.publicnode.com` | yes | 179 ms |
| `api.mainnet.solana.com` | yes | 165 ms |

## Validators & stake

- **675 active** validators, **10 delinquent** (1.46% by count, 0.025% by stake).
- **Total stake:** 440,637,196 SOL ($52.05B); stake rate 69.43% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.41% and top 33 hold 45.82% of active stake.
- **Commission:** median 5.0%, mean 12.58%; 235 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,819,007 | 4.045% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,817,079 | 3.590% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,387,904 | 2.812% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,274,982 | 2.559% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,595,499 | 2.405% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,221,893 | 2.093% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,163,088 | 2.080% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,599,959 | 1.725% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,091,911 | 1.610% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,887 | 1.489% | 0% |

## Economics

- **SOL:** $118.12 (+3.42% 24h, +15.37% 7d, +21.76% 30d). Market cap $69.45B, 24h volume $4.35B (6.26% of cap). Price source: `coingecko`.
- **TVL:** $6.49B across 331 protocols - rank #2 of 467 chains, 6.81% of all tracked chain TVL. +10.01% over 7d, -51.0% from its ATH.
- **Stablecoins:** $17.69B circulating on Solana (+12.56% 7d) - $2.73 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.26B in 24h, $19.63B over 7d across 125 venues. Volume/TVL turnover 0.349x per day.
- **REV (chain fees):** $15.93M in 24h, $415.02M over 30d. Retained chain revenue $5.94M (37.3% of fees). Annualised fees are 8.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,648,035 SOL circulating of 634,686,577 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.89B | +2.0% | +17.5% |
| 2 | Kamino Lend | Lending | $1.43B | +1.3% | +7.3% |
| 3 | Raydium AMM | Dexs | $1.32B | +1.2% | +12.1% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.22B | +2.4% | +16.9% |
| 5 | Binance Staked SOL | Liquid Staking | $1.20B | +2.0% | +14.7% |
| 6 | Jupiter Lend | Lending | $1.18B | +0.7% | +9.2% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $813.60M | +1.1% | +8.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $608.63M | +2.0% | +15.6% |
| 9 | Marinade Native | Staking Pool | $451.41M | +2.0% | +16.9% |
| 10 | PumpSwap | Dexs | $381.69M | +2.0% | +16.3% |
| 11 | Sentora Curator | Risk Curators | $362.40M | +0.0% | -1.7% |
| 12 | Drift Staked SOL | Liquid Staking | $331.30M | +2.0% | +16.2% |

The top five protocols hold 42.1% of Solana's tracked TVL. Summed across all 331 protocols the total is $16.78B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 43.0% · Lending 17.3% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$835.18M of tokenised real-world assets and equities are locked on Solana - 4.976% of chain TVL.

- OnRe (RWA): $299.20M
- Solstice (Basis Trading): $217.05M
- Huma (RWA): $199.26M
- JupUSD (Basis Trading): $44.36M
- Plume Vaults (RWA): $28.26M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) - Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) - Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-24
- [SIMD-0646: SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-24
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-23
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-23
- [SIMD-0648: SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0249: SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23

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

### Change over 24h (vs run at 2026-09-24T01:53:02Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,513.62 | 4,337.90 | -3.89% |
| Average non-vote TPS | 1,982.83 | 1,832.73 | -7.57% |
| Average slot time (ms) | 265.70 | 268.20 | +0.94% |
| Active validators | 675.00 | 675.00 | +0.00% |
| Delinquent validators | 12.00 | 10.00 | -16.67% |
| Solana TVL | 6,391,344,724.00 | 6,485,663,210.00 | +1.48% |
| SOL price | 114.66 | 118.12 | +3.02% |
| Stablecoin supply | 16,427,876,539.00 | 17,687,554,466.00 | +7.67% |
| 24h DEX volume | 2,682,816,608.00 | 2,262,604,262.43 | -15.66% |
| 24h chain fees | 17,125,745.95 | 15,931,553.48 | -6.97% |

### Change over 7d (vs run at 2026-09-18T01:50:33Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,099.51 | 4,337.90 | +5.82% |
| Average non-vote TPS | 1,978.66 | 1,832.73 | -7.38% |
| Average slot time (ms) | 316.70 | 268.20 | -15.31% |
| Active validators | 676.00 | 675.00 | -0.15% |
| Delinquent validators | 14.00 | 10.00 | -28.57% |
| Solana TVL | 5,875,684,850.00 | 6,485,663,210.00 | +10.38% |
| SOL price | 102.31 | 118.12 | +15.45% |
| Stablecoin supply | 15,710,182,138.00 | 17,687,554,466.00 | +12.59% |
| 24h DEX volume | 2,555,388,156.29 | 2,262,604,262.43 | -11.46% |
| 24h chain fees | 13,101,763.60 | 15,931,553.48 | +21.60% |

### Change over 30d (vs run at 2026-08-25T18:20:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,565.46 | 4,337.90 | -4.98% |
| Average non-vote TPS | 2,708.19 | 1,832.73 | -32.33% |
| Average slot time (ms) | 366.20 | 268.20 | -26.76% |
| Active validators | 685.00 | 675.00 | -1.46% |
| Delinquent validators | 10.00 | 10.00 | +0.00% |
| Solana TVL | 5,634,312,506.00 | 6,485,663,210.00 | +15.11% |
| SOL price | 98.47 | 118.12 | +19.96% |
| Stablecoin supply | 16,426,872,816.00 | 17,687,554,466.00 | +7.67% |
| 24h DEX volume | 2,996,141,158.64 | 2,262,604,262.43 | -24.48% |
| 24h chain fees | 14,491,360.16 | 15,931,553.48 | +9.94% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 19.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
