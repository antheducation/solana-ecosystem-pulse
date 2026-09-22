# Solana Ecosystem Pulse

**Generated:** 2026-09-22T20:34:24Z · **Schema:** `1.0.0` · **Collection time:** 21.3s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: DEGRADED** - serious anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $118.17 | -0.68% |
| Market cap | $69.43B | rank #7 |
| Total value locked | $6.51B | +4.75% |
| Stablecoin supply | $17.17B | +7.97% |
| DEX volume (24h) | $3.43B | +22.67% |
| Chain fees / REV (24h) | $18.64M | +26.21% |
| Non-vote TPS (1h avg) | 2,379 | peak 5,474 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1040 | 48.08% complete | 224,300 slots left |

## Anomaly detection

Serious anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 90 historical runs, sigma = 3.0).

Critical 0 · Serious 2 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [SERIOUS] | Stablecoin supply moved sharply (up 8.0% in 24h) | Stablecoin supply changed +8.0% over the last day, past the 3% alert band. | `threshold` |
| [SERIOUS] | Average slot time (ms) is below its recent norm | Current 268.00 sits 15.3 sigma below the median of the last 90 runs (316.75, -15.4%). | `zscore` |
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Solana TVL is above its recent norm | Current 6,505,534,933.00 sits 3.5 sigma above the median of the last 90 runs (5,855,155,696.50, +11.1%). | `zscore` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 2,379.3 average over the last 60 minutes; 2,257.1 in the latest sample.
- **Total TPS:** 4,893.5 average, 5,474.3 peak. Consensus votes account for 51.4% of all transactions.
- **Slot time:** 268.0 ms average (target 400 ms), worst 1-minute bucket 277.8 ms.
- **Block height:** 427,528,033 at absolute slot 449,487,700.
- **Epoch 1040:** slot 207,700 of 432,000 (48.08% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.636% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 355 ms |
| `solana-rpc.publicnode.com` | yes | 115 ms |
| `api.mainnet.solana.com` | yes | 347 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.045% by stake).
- **Total stake:** 439,861,749 SOL ($51.98B); stake rate 69.32% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.83% of active stake.
- **Commission:** median 5.0%, mean 12.28%; 238 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,826,722 | 4.055% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,840,698 | 3.603% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,354,353 | 2.810% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,265,429 | 2.562% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,210,832 | 2.322% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,211,356 | 2.095% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,144,102 | 2.080% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,458,789 | 1.696% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,089,342 | 1.612% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,555,722 | 1.491% | 0% |

## Economics

- **SOL:** $118.17 (-0.68% 24h, +20.76% 7d, +24.31% 30d). Market cap $69.43B, 24h volume $4.83B (6.96% of cap). Price source: `coingecko`.
- **TVL:** $6.51B across 332 protocols - rank #2 of 467 chains, 6.73% of all tracked chain TVL. +9.84% over 7d, -50.9% from its ATH.
- **Stablecoins:** $17.17B circulating on Solana (+4.79% 7d) - $2.64 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $3.43B in 24h, $20.73B over 7d across 125 venues. Volume/TVL turnover 0.527x per day.
- **REV (chain fees):** $18.64M in 24h, $428.70M over 30d. Retained chain revenue $7.79M (41.8% of fees). Annualised fees are 9.80% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,507,416 SOL circulating of 634,531,043 total (92.59%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.88B | +0.8% | +19.9% |
| 2 | Kamino Lend | Lending | $1.43B | +0.8% | +5.6% |
| 3 | Raydium AMM | Dexs | $1.33B | +0.6% | +16.6% |
| 4 | Jito Liquid Staking | Liquid Staking | $1.22B | +0.6% | +16.1% |
| 5 | Binance Staked SOL | Liquid Staking | $1.21B | -0.8% | +13.8% |
| 6 | Jupiter Lend | Lending | $1.18B | -1.4% | +6.3% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $820.37M | +0.0% | +8.8% |
| 8 | Jupiter Staked SOL | Liquid Staking | $610.52M | +0.9% | +15.1% |
| 9 | Marinade Native | Staking Pool | $450.96M | +1.2% | +15.5% |
| 10 | PumpSwap | Dexs | $381.84M | +1.8% | +14.9% |
| 11 | Sentora Curator | Risk Curators | $363.05M | +0.1% | -5.2% |
| 12 | Drift Staked SOL | Liquid Staking | $332.77M | +0.7% | +15.3% |

The top five protocols hold 42.2% of Solana's tracked TVL. Summed across all 332 protocols the total is $16.77B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 42.9% · Lending 17.3% · Dexs 15.8% · Derivatives 5.3% · Staking Pool 4.1% · Risk Curators 3.5%

### Tokenised assets

$826.53M of tokenised real-world assets and equities are locked on Solana - 4.928% of chain TVL.

- OnRe (RWA): $302.65M
- Solstice (Basis Trading): $218.08M
- Huma Finance V2 (RWA): $188.67M
- JupUSD (Basis Trading): $46.67M
- Plume Vaults (RWA): $28.20M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) - Sat, 19 Sep 2026 11:28:00 GMT
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) - Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) - Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) - Thu, 10 Sep 2026 20:16:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) | 2026-09-18 | pre-release |
| [v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) | 2026-09-18 | stable |
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0048: Fix supersedes / superseded-by links for SIMD-0048, 0219 and 0458](https://github.com/solana-foundation/solana-improvement-documents/pull/660) - updated 2026-09-22
- [SIMD-0075: SIMD-0075 / SIMD-0152: fix verify pseudocode](https://github.com/solana-foundation/solana-improvement-documents/pull/659) - updated 2026-09-22
- [SIMD-0138: SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - updated 2026-09-22
- [SIMD-0302: Fix rendering in SIMD-0302/0306/0266/0307, rename 0505 file to 0506](https://github.com/solana-foundation/solana-improvement-documents/pull/655) - updated 2026-09-22
- [SIMD-0047: SIMD-0047 / SIMD-0186: fix syscall hash and signature, union of loaded accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/654) - updated 2026-09-22
- [SIMD-0317: SIMD-0317 / SIMD-0313: fix FEC set payload size, gate name and shred layout](https://github.com/solana-foundation/solana-improvement-documents/pull/653) - updated 2026-09-22
- [SIMD-0174: SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-22
- [Sync SIMD statuses and feature keys with mainnet activations (56 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-22

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

### Change over 24h (vs run at 2026-09-21T21:17:54Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,659.01 | 4,893.52 | +5.03% |
| Average non-vote TPS | 2,142.85 | 2,379.33 | +11.04% |
| Average slot time (ms) | 266.70 | 268.00 | +0.49% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 6,474,683,879.00 | 6,505,534,933.00 | +0.48% |
| SOL price | 118.81 | 118.17 | -0.54% |
| Stablecoin supply | 15,907,385,261.00 | 17,173,484,924.00 | +7.96% |
| 24h DEX volume | 2,795,356,104.36 | 3,428,858,820.75 | +22.66% |
| 24h chain fees | 14,463,382.08 | 18,642,402.21 | +28.89% |

### Change over 7d (vs run at 2026-09-15T20:32:11Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,770.98 | 4,893.52 | +2.57% |
| Average non-vote TPS | 2,641.86 | 2,379.33 | -9.94% |
| Average slot time (ms) | 317.40 | 268.00 | -15.56% |
| Active validators | 679.00 | 677.00 | -0.29% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,793,334,701.00 | 6,505,534,933.00 | +12.29% |
| SOL price | 96.94 | 118.17 | +21.90% |
| Stablecoin supply | 16,388,645,734.00 | 17,173,484,924.00 | +4.79% |
| 24h DEX volume | 2,530,223,236.85 | 3,428,858,820.75 | +35.52% |
| 24h chain fees | 13,579,950.58 | 18,642,402.21 | +37.28% |

### Change over 30d (vs run at 2026-08-23T18:11:19Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,174.50 | 4,893.52 | +17.22% |
| Average non-vote TPS | 2,325.35 | 2,379.33 | +2.32% |
| Average slot time (ms) | 365.10 | 268.00 | -26.60% |
| Active validators | 681.00 | 677.00 | -0.59% |
| Delinquent validators | 14.00 | 12.00 | -14.29% |
| Solana TVL | 5,593,098,038.00 | 6,505,534,933.00 | +16.31% |
| SOL price | 94.99 | 118.17 | +24.40% |
| Stablecoin supply | 16,372,086,266.00 | 17,173,484,924.00 | +4.89% |
| 24h DEX volume | 3,732,294,477.70 | 3,428,858,820.75 | -8.13% |
| 24h chain fees | 12,017,709.26 | 18,642,402.21 | +55.12% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 21.3s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
