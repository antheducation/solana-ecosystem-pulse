# Solana Ecosystem Pulse

**Generated:** 2026-10-28T21:57:08Z · **Schema:** `1.0.0` · **Collection time:** 19.9s · **Sources OK:** 40/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $102.77 | +1.38% |
| Market cap | $60.58B | rank #7 |
| Total value locked | $5.75B | +1.28% |
| Stablecoin supply | $15.78B | +0.13% |
| DEX volume (24h) | $1.58B | -23.57% |
| Chain fees / REV (24h) | $11.23M | -3.81% |
| Non-vote TPS (1h avg) | 2,156 | peak 3,570 total |
| Active validators | 661 | 30 delinquent |
| Epoch 1070 | 91.75% complete | 35,640 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 126 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 3 · Info 0

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | Average TPS is below its recent norm | Current 2,155.70 sits 3.5 sigma below the median of the last 126 runs (4,496.09, -52.1%). | `zscore` |
| [WARNING] | Delinquent validators is above its recent norm | Current 30.00 sits 4.3 sigma above the median of the last 126 runs (11.00, +172.7%). | `zscore` |

## Network performance

- **Non-vote (user) TPS:** 2,155.7 average over the last 60 minutes; 1,938.7 in the latest sample.
- **Total TPS:** 2,155.7 average, 3,569.5 peak. Consensus votes account for 0.0% of all transactions.
- **Slot time:** 213.6 ms average (target 400 ms), worst 1-minute bucket 216.6 ms.
- **Block height:** 440,660,751 at absolute slot 462,636,360.
- **Epoch 1070:** slot 396,360 of 432,000 (91.75% complete).
- **Client:** agave `4.3.2`, feature set `3383571666`. Inflation 3.583% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 211 ms |
| `solana-rpc.publicnode.com` | yes | 168 ms |
| `api.mainnet.solana.com` | yes | 216 ms |

## Validators & stake

- **661 active** validators, **30 delinquent** (4.34% by count, 0.886% by stake).
- **Total stake:** 437,290,026 SOL ($44.94B); stake rate 68.69% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.79% and top 33 hold 46.34% of active stake.
- **Commission:** median 5.0%, mean 12.97%; 227 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,006,422 | 3.924% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,661,096 | 3.844% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,791,931 | 2.951% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,815,143 | 2.495% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,718,548 | 2.242% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,464,443 | 2.184% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,208,877 | 2.125% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,757,994 | 1.790% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,041,146 | 1.625% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,997,044 | 1.614% | 0% |

## Economics

- **SOL:** $102.77 (+1.38% 24h, -4.85% 7d, -13.48% 30d). Market cap $60.58B, 24h volume $2.63B (4.34% of cap). Price source: `coingecko`.
- **TVL:** $5.75B across 335 protocols - rank #4 of 420 chains, 6.48% of all tracked chain TVL. -3.83% over 7d, -55.5% from its ATH.
- **Stablecoins:** $15.78B circulating on Solana (-1.41% 7d) - $2.75 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.58B in 24h, $12.83B over 7d across 139 venues. Volume/TVL turnover 0.275x per day.
- **REV (chain fees):** $11.23M in 24h, $412.68M over 30d. Retained chain revenue $4.08M (36.3% of fees). Annualised fees are 6.77% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 589,928,202 SOL circulating of 636,577,995 total (92.67%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.81B | +0.9% | -2.7% |
| 2 | Kamino Lend | Lending | $1.27B | +0.3% | -5.0% |
| 3 | Raydium AMM | Dexs | $1.15B | +1.1% | -4.5% |
| 4 | Binance Staked SOL | Liquid Staking | $1.11B | +2.3% | -0.8% |
| 5 | Jito Liquid Staking | Liquid Staking | $1.06B | +1.0% | -4.1% |
| 6 | Jupiter Lend | Lending | $1.02B | +0.9% | -2.1% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $720.85M | +0.7% | -3.6% |
| 8 | Jupiter Staked SOL | Liquid Staking | $535.68M | +1.2% | -4.0% |
| 9 | Sentora Curator | Risk Curators | $383.73M | -0.0% | -11.3% |
| 10 | Marinade Native | Staking Pool | $367.00M | +1.2% | -4.8% |
| 11 | PumpSwap | Dexs | $339.68M | +1.7% | -4.1% |
| 12 | OnRe | RWA | $305.54M | +1.4% | +3.9% |

The top five protocols hold 41.1% of Solana's tracked TVL. Summed across all 335 protocols the total is $15.57B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 44.1% · Lending 16.4% · Dexs 15.1% · Derivatives 5.1% · RWA 3.9% · Risk Curators 3.7%

### Tokenised assets

$872.08M of tokenised real-world assets and equities are locked on Solana - 5.600% of chain TVL.

- OnRe (RWA): $305.54M
- Huma (RWA): $254.06M
- Solstice (Basis Trading): $201.60M
- JupUSD (Basis Trading): $42.99M
- Plume Vaults (RWA): $37.02M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) | 2026-10-28 | pre-release |
| [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) | 2026-10-26 | pre-release |
| [v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) | 2026-10-26 | stable |
| [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) | 2026-10-15 | stable |
| [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) | 2026-10-13 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0676: SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-28
- [SIMD-0550: docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-28
- [SIMD-0706: SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-10-27
- [SIMD-0709: SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [Amend 0529: charge a flat cu first before execution](https://github.com/solana-foundation/solana-improvement-documents/pull/707) - updated 2026-10-27
- [SIMD-0650: SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-27
- [SIMD-0567: SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-10-27

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

### Change over 24h (vs run at 2026-10-27T21:31:32Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,359.98 | 2,155.70 | -8.66% |
| Average non-vote TPS | 2,359.97 | 2,155.70 | -8.66% |
| Average slot time (ms) | 213.80 | 213.60 | -0.09% |
| Active validators | 665.00 | 661.00 | -0.60% |
| Delinquent validators | 20.00 | 30.00 | +50.00% |
| Solana TVL | 5,721,042,380.00 | 5,748,939,504.00 | +0.49% |
| SOL price | 100.85 | 102.77 | +1.90% |
| Stablecoin supply | 15,763,185,048.00 | 15,784,667,411.00 | +0.14% |
| 24h DEX volume | 2,071,067,618.21 | 1,582,952,703.63 | -23.57% |
| 24h chain fees | 11,672,734.12 | 11,229,097.00 | -3.80% |

### Change over 7d (vs run at 2026-10-21T20:57:39Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 2,089.84 | 2,155.70 | +3.15% |
| Average non-vote TPS | 2,089.84 | 2,155.70 | +3.15% |
| Average slot time (ms) | 213.00 | 213.60 | +0.28% |
| Active validators | 668.00 | 661.00 | -1.05% |
| Delinquent validators | 9.00 | 30.00 | +233.33% |
| Solana TVL | 6,055,835,656.00 | 5,748,939,504.00 | -5.07% |
| SOL price | 108.08 | 102.77 | -4.91% |
| Stablecoin supply | 16,012,993,627.00 | 15,784,667,411.00 | -1.43% |
| 24h DEX volume | 2,437,800,216.24 | 1,582,952,703.63 | -35.07% |
| 24h chain fees | 13,174,208.40 | 11,229,097.00 | -14.76% |

### Change over 30d (vs run at 2026-09-28T22:41:17Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,519.28 | 2,155.70 | -52.30% |
| Average non-vote TPS | 2,010.42 | 2,155.70 | +7.23% |
| Average slot time (ms) | 267.20 | 213.60 | -20.06% |
| Active validators | 674.00 | 661.00 | -1.93% |
| Delinquent validators | 8.00 | 30.00 | +275.00% |
| Solana TVL | 6,552,189,378.00 | 5,748,939,504.00 | -12.26% |
| SOL price | 118.18 | 102.77 | -13.04% |
| Stablecoin supply | 16,723,366,837.00 | 15,784,667,411.00 | -5.61% |
| 24h DEX volume | 1,926,466,128.71 | 1,582,952,703.63 | -17.83% |
| 24h chain fees | 15,421,946.25 | 11,229,097.00 | -27.19% |

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

This run made 41 HTTP calls (40 succeeded, 1 failed) in 19.9s of wall time.

<details><summary>Failed calls this run (the report degrades, it does not break)</summary>

- `solana.com:news_rss` - HTTP 429 (3 attempts)

</details>

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
