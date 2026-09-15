# Solana Ecosystem Pulse

**Generated:** 2026-09-15T10:34:46Z · **Schema:** `1.0.0` · **Collection time:** 18.6s · **Sources OK:** 41/41

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.72 | -1.03% |
| Market cap | $59.11B | rank #7 |
| Total value locked | $5.85B | +0.29% |
| Stablecoin supply | $16.39B | +0.21% |
| DEX volume (24h) | $2.21B | +23.55% |
| Chain fees / REV (24h) | $13.55M | -3.45% |
| Non-vote TPS (1h avg) | 1,652 | peak 4,442 total |
| Active validators | 676 | 13 delinquent |
| Epoch 1035 | 25.09% complete | 323,612 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 83 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 1 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,652.0 average over the last 60 minutes; 1,479.3 in the latest sample.
- **Total TPS:** 3,786.6 average, 4,441.8 peak. Consensus votes account for 56.4% of all transactions.
- **Slot time:** 314.7 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 425,270,292 at absolute slot 447,228,388.
- **Epoch 1035:** slot 108,388 of 432,000 (25.09% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.647% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 274 ms |
| `solana-rpc.publicnode.com` | yes | 161 ms |
| `api.mainnet.solana.com` | yes | 256 ms |

## Validators & stake

- **676 active** validators, **13 delinquent** (1.89% by count, 0.111% by stake).
- **Total stake:** 439,248,639 SOL ($44.24B); stake rate 69.27% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.35% and top 33 hold 45.78% of active stake.
- **Commission:** median 5.0%, mean 12.23%; 243 validators at 0% and 61 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,757,712 | 4.047% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,373,377 | 3.732% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,492,605 | 2.847% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,369,566 | 2.591% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,669,319 | 2.204% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,256,225 | 2.110% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,035,103 | 2.059% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,372,355 | 1.680% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,944,775 | 1.583% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,553,626 | 1.494% | 0% |

## Economics

- **SOL:** $100.72 (-1.03% 24h, -2.80% 7d, +33.83% 30d). Market cap $59.11B, 24h volume $3.24B (5.49% of cap). Price source: `coingecko`.
- **TVL:** $5.85B across 338 protocols - rank #2 of 467 chains, 6.66% of all tracked chain TVL. -1.21% over 7d, -55.8% from its ATH.
- **Stablecoins:** $16.39B circulating on Solana (-1.84% 7d) - $2.80 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $2.21B in 24h, $17.14B over 7d across 123 venues. Volume/TVL turnover 0.378x per day.
- **REV (chain fees):** $13.55M in 24h, $393.96M over 30d. Retained chain revenue $5.26M (38.8% of fees). Annualised fees are 8.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 587,028,093 SOL circulating of 634,111,649 total (92.57%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.56B | +0.5% | -1.5% |
| 2 | Kamino Lend | Lending | $1.35B | -0.3% | +1.2% |
| 3 | Raydium AMM | Dexs | $1.13B | -0.8% | -1.2% |
| 4 | Jupiter Lend | Lending | $1.09B | -0.7% | -0.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.04B | -1.0% | -3.3% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -1.3% | -2.6% |
| 7 | BlackRock BUIDL | RWA | $992.89M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $743.44M | -1.1% | -1.2% |
| 9 | Jupiter Staked SOL | Liquid Staking | $520.08M | -0.8% | -3.1% |
| 10 | Sentora Curator | Risk Curators | $383.23M | -1.4% | -0.9% |
| 11 | Marinade Native | Staking Pool | $383.17M | -0.9% | -6.7% |
| 12 | PumpSwap | Dexs | $323.86M | -2.6% | -5.3% |

The top five protocols hold 38.0% of Solana's tracked TVL. Summed across all 338 protocols the total is $16.22B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.4% · Lending 16.6% · Dexs 14.2% · RWA 11.8% · Derivatives 5.0% · Risk Curators 3.7%

### Tokenised assets

$2.22B of tokenised real-world assets and equities are locked on Solana - 13.707% of chain TVL.

- BlackRock BUIDL (RWA): $992.89M
- OnRe (RWA): $300.45M
- Solstice (Basis Trading): $235.00M
- Huma Finance V2 (RWA): $183.15M
- Ondo Yield Assets (RWA): $180.10M

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

- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-15
- [SIMD-0377: SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-14
- [Increase TxV1 Account Lock Limit to 96](https://github.com/solana-foundation/solana-improvement-documents/pull/596) - updated 2026-09-14
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [ci: bump dessant/lock-threads to v6.0.2 to fix weekly workflow failure](https://github.com/solana-foundation/solana-improvement-documents/pull/637) - updated 2026-09-14
- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11

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

### Change over 24h (vs run at 2026-09-14T11:05:21Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,417.38 | 3,786.60 | +10.80% |
| Average non-vote TPS | 1,285.09 | 1,652.02 | +28.55% |
| Average slot time (ms) | 315.30 | 314.70 | -0.19% |
| Active validators | 676.00 | 676.00 | +0.00% |
| Delinquent validators | 14.00 | 13.00 | -7.14% |
| Solana TVL | 5,891,617,539.00 | 5,851,427,899.00 | -0.68% |
| SOL price | 101.76 | 100.72 | -1.02% |
| Stablecoin supply | 16,352,362,124.00 | 16,388,773,046.00 | +0.22% |
| 24h DEX volume | 1,790,994,711.97 | 2,212,763,996.85 | +23.55% |
| 24h chain fees | 14,255,438.64 | 13,551,769.58 | -4.94% |

### Change over 7d (vs run at 2026-09-08T10:11:04Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,448.21 | 3,786.60 | +9.81% |
| Average non-vote TPS | 1,336.54 | 1,652.02 | +23.60% |
| Average slot time (ms) | 315.40 | 314.70 | -0.22% |
| Active validators | 675.00 | 676.00 | +0.15% |
| Delinquent validators | 13.00 | 13.00 | +0.00% |
| Solana TVL | 5,869,138,160.00 | 5,851,427,899.00 | -0.30% |
| SOL price | 103.55 | 100.72 | -2.73% |
| Stablecoin supply | 16,695,009,953.00 | 16,388,773,046.00 | -1.83% |
| 24h DEX volume | 2,872,025,884.66 | 2,212,763,996.85 | -22.95% |
| 24h chain fees | 15,999,657.21 | 13,551,769.58 | -15.30% |

### Change over 30d (vs run at 2026-08-16T18:10:46Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,797.96 | 3,786.60 | -0.30% |
| Average non-vote TPS | 2,151.97 | 1,652.02 | -23.23% |
| Average slot time (ms) | 415.20 | 314.70 | -24.21% |
| Active validators | 688.00 | 676.00 | -1.74% |
| Delinquent validators | 9.00 | 13.00 | +44.44% |
| Solana TVL | 4,804,122,508.00 | 5,851,427,899.00 | +21.80% |
| SOL price | 75.15 | 100.72 | +34.03% |
| Stablecoin supply | 15,997,960,401.00 | 16,388,773,046.00 | +2.44% |
| 24h DEX volume | 1,169,008,711.04 | 2,212,763,996.85 | +89.29% |
| 24h chain fees | 8,145,711.86 | 13,551,769.58 | +66.37% |

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

This run made 41 HTTP calls (41 succeeded, 0 failed) in 18.6s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
