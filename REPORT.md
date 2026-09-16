# Solana Ecosystem Pulse

**Generated:** 2026-09-16T10:23:13Z · **Schema:** `1.0.0` · **Collection time:** 19.8s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $97.26 | -3.46% |
| Market cap | $57.09B | rank #7 |
| Total value locked | $5.72B | -3.38% |
| Stablecoin supply | $15.97B | -2.57% |
| DEX volume (24h) | $2.52B | -0.30% |
| Chain fees / REV (24h) | $14.23M | +4.78% |
| Non-vote TPS (1h avg) | 1,225 | peak 3,648 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1035 | 87.69% complete | 53,160 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 84 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,225.3 average over the last 60 minutes; 1,211.2 in the latest sample.
- **Total TPS:** 3,356.2 average, 3,648.1 peak. Consensus votes account for 63.5% of all transactions.
- **Slot time:** 316.0 ms average (target 400 ms), worst 1-minute bucket 327.9 ms.
- **Block height:** 425,540,315 at absolute slot 447,498,840.
- **Epoch 1035:** slot 378,840 of 432,000 (87.69% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.647% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 252 ms |
| `solana-rpc.publicnode.com` | yes | 54 ms |
| `api.mainnet.solana.com` | yes | 634 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.045% by stake).
- **Total stake:** 439,248,639 SOL ($42.72B); stake rate 69.27% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.33% and top 33 hold 45.75% of active stake.
- **Commission:** median 5.0%, mean 12.66%; 241 validators at 0% and 64 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,757,712 | 4.045% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,373,377 | 3.729% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,492,605 | 2.845% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,369,566 | 2.590% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,669,319 | 2.202% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,225 | 2.108% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,035,103 | 2.058% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,372,355 | 1.679% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,944,775 | 1.582% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,553,626 | 1.493% | 0% |

## Economics

- **SOL:** $97.26 (-3.46% 24h, -6.02% 7d, +29.20% 30d). Market cap $57.09B, 24h volume $3.90B (6.84% of cap). Price source: `coingecko`.
- **TVL:** $5.72B across 330 protocols - rank #2 of 467 chains, 6.64% of all tracked chain TVL. -3.96% over 7d, -56.8% from its ATH.
- **Stablecoins:** $15.97B circulating on Solana (-4.00% 7d) - $2.79 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.52B in 24h, $17.06B over 7d across 123 venues. Volume/TVL turnover 0.441x per day.
- **REV (chain fees):** $14.23M in 24h, $401.45M over 30d. Retained chain revenue $5.43M (38.1% of fees). Annualised fees are 9.10% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,064,665 SOL circulating of 634,110,724 total (92.58%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.54B | -1.2% | -2.8% |
| 2 | Kamino Lend | Lending | $1.32B | -1.7% | -2.7% |
| 3 | Raydium AMM | Dexs | $1.09B | -3.2% | -4.2% |
| 4 | Jupiter Lend | Lending | $1.08B | -1.2% | -2.5% |
| 5 | Binance Staked SOL | Liquid Staking | $1.00B | -3.9% | -6.9% |
| 6 | Jito Liquid Staking | Liquid Staking | $999.21M | -3.4% | -5.9% |
| 7 | Jupiter Perpetual Exchange | Derivatives | $728.04M | -2.1% | -2.9% |
| 8 | Jupiter Staked SOL | Liquid Staking | $500.66M | -3.7% | -6.6% |
| 9 | Sentora Curator | Risk Curators | $372.68M | -2.8% | -3.2% |
| 10 | Marinade Native | Staking Pool | $368.85M | -3.7% | -8.4% |
| 11 | PumpSwap | Dexs | $314.49M | -2.9% | -6.3% |
| 12 | OnRe | RWA | $300.65M | +0.1% | -1.2% |

The top five protocols hold 41.6% of Solana's tracked TVL. Summed across all 330 protocols the total is $14.51B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 40.6% · Lending 18.3% · Dexs 15.4% · Derivatives 5.5% · Risk Curators 4.1% · Staking Pool 4.0%

### Tokenised assets

$858.89M of tokenised real-world assets and equities are locked on Solana - 5.920% of chain TVL.

- OnRe (RWA): $300.65M
- Solstice (Basis Trading): $234.96M
- Huma Finance V2 (RWA): $193.25M
- JupUSD (Basis Trading): $46.79M
- Plume Vaults (RWA): $28.33M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

## News, releases & upcoming upgrades

### Solana Foundation news

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) - Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) - Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) - Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) - Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) - Thu, 03 Sep 2026 16:26:00 GMT

### Validator client releases (Agave)

| Tag | Published | Channel |
|---|---|---|
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | stable |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0499: SIMD-0499: Deactivate execution of loader-v1 and ABI-v0](https://github.com/solana-foundation/solana-improvement-documents/pull/499) - updated 2026-09-16
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-15
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-15
- [SIMD-0630: SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-15
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11

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

### Change over 24h (vs run at 2026-09-15T10:34:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,786.60 | 3,356.16 | -11.37% |
| Average non-vote TPS | 1,652.02 | 1,225.32 | -25.83% |
| Average slot time (ms) | 314.70 | 316.00 | +0.41% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,851,427,899.00 | 5,716,713,977.00 | -2.30% |
| SOL price | 100.72 | 97.26 | -3.44% |
| Stablecoin supply | 16,388,773,046.00 | 15,965,637,649.00 | -2.58% |
| 24h DEX volume | 2,212,763,996.85 | 2,522,724,403.22 | +14.01% |
| 24h chain fees | 13,551,769.58 | 14,228,744.46 | +5.00% |

### Change over 7d (vs run at 2026-09-09T10:14:14Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,846.21 | 3,356.16 | -12.74% |
| Average non-vote TPS | 1,717.92 | 1,225.32 | -28.67% |
| Average slot time (ms) | 316.20 | 316.00 | -0.06% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 10.00 | 12.00 | +20.00% |
| Solana TVL | 5,987,012,086.00 | 5,716,713,977.00 | -4.51% |
| SOL price | 103.79 | 97.26 | -6.29% |
| Stablecoin supply | 16,629,962,371.00 | 15,965,637,649.00 | -3.99% |
| 24h DEX volume | 2,577,833,806.34 | 2,522,724,403.22 | -2.14% |
| 24h chain fees | 16,439,615.38 | 14,228,744.46 | -13.45% |

### Change over 30d (vs run at 2026-08-17T18:19:42Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,422.32 | 3,356.16 | -24.11% |
| Average non-vote TPS | 2,781.61 | 1,225.32 | -55.95% |
| Average slot time (ms) | 415.70 | 316.00 | -23.98% |
| Active validators | 688.00 | 677.00 | -1.60% |
| Delinquent validators | 7.00 | 12.00 | +71.43% |
| Solana TVL | 4,849,572,817.00 | 5,716,713,977.00 | +17.88% |
| SOL price | 75.94 | 97.26 | +28.07% |
| Stablecoin supply | 16,003,787,085.00 | 15,965,637,649.00 | -0.24% |
| 24h DEX volume | 1,055,467,633.95 | 2,522,724,403.22 | +139.01% |
| 24h chain fees | 6,802,409.48 | 14,228,744.46 | +109.17% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 19.7s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
