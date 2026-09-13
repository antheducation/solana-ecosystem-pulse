# Solana Ecosystem Pulse

**Generated:** 2026-09-13T15:10:52Z · **Schema:** `1.0.0` · **Collection time:** 34.2s · **Sources OK:** 35/35

> This file is regenerated end-to-end by `python run.py`. Nothing in it is hand-written; every number below carries its source in [Data sources](#data-sources).

**Network status: WATCH** - minor anomalies detected.

## At a glance

| Metric | Value | 24h |
|---|---:|---:|
| SOL price | $100.43 | -1.49% |
| Market cap | $58.93B | rank #7 |
| Total value locked | $5.83B | -1.25% |
| Stablecoin supply | $16.53B | -0.18% |
| DEX volume (24h) | $1.69B | -46.88% |
| Chain fees / REV (24h) | $13.52M | -24.39% |
| Non-vote TPS (1h avg) | 1,797 | peak 4,395 total |
| Active validators | 677 | 12 delinquent |
| Epoch 1034 | 10.59% complete | 386,258 slots left |

## Anomaly detection

Minor anomalies detected. 17 rules evaluated across two engines (threshold + robust z-score over 81 historical runs, sigma = 3.0).

Critical 0 · Serious 0 · Warning 2 · Info 1

| Severity | Finding | Detail | Engine |
|---|---|---|---|
| [WARNING] | Stake concentration is high | Nakamoto coefficient is 18: that many validators together control over a third of active stake. | `threshold` |
| [WARNING] | DEX volume moved sharply (down 46.9% in 24h) | DEX volume changed -46.9% over the last day, past the 40% alert band. | `threshold` |
| [INFO] | Answering RPC node runs a release candidate | The endpoint that served this run reports agave 4.3.0-rc.0. | `threshold` |

## Network performance

- **Non-vote (user) TPS:** 1,797.0 average over the last 60 minutes; 1,605.7 in the latest sample.
- **Total TPS:** 3,924.0 average, 4,394.9 peak. Consensus votes account for 54.2% of all transactions.
- **Slot time:** 316.4 ms average (target 400 ms), worst 1-minute bucket 326.1 ms.
- **Block height:** 424,776,384 at absolute slot 446,733,742.
- **Epoch 1034:** slot 45,742 of 432,000 (10.59% complete).
- **Client:** agave `4.3.0-rc.0`, feature set `2409014235`. Inflation 3.649% annualised.

**Public RPC endpoint health this run**

| Endpoint | Healthy | Latency |
|---|:--:|---:|
| `api.mainnet-beta.solana.com` | yes | 403 ms |
| `solana-rpc.publicnode.com` | yes | 69 ms |
| `api.mainnet.solana.com` | yes | 400 ms |

## Validators & stake

- **677 active** validators, **12 delinquent** (1.74% by count, 0.408% by stake).
- **Total stake:** 438,740,367 SOL ($44.06B); stake rate 69.20% of total supply.
- **Concentration:** Nakamoto coefficient **18**; top 10 hold 24.39% and top 33 hold 45.85% of active stake.
- **Commission:** median 5.0%, mean 12.51%; 243 validators at 0% and 63 at 100%.

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|--:|---|--:|--:|--:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,568,189 | 4.021% | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,361,599 | 3.745% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,501,349 | 2.861% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,372,391 | 2.603% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,619,665 | 2.202% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,712 | 2.118% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,025,175 | 2.066% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,367,885 | 1.686% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,943,003 | 1.589% | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,552,506 | 1.500% | 0% |

## Economics

- **SOL:** $100.43 (-1.49% 24h, -4.95% 7d, +33.55% 30d). Market cap $58.93B, 24h volume $1.88B (3.20% of cap). Price source: `coingecko`.
- **TVL:** $5.83B across 339 protocols - rank #2 of 467 chains, 6.65% of all tracked chain TVL. -1.57% over 7d, -56.0% from its ATH.
- **Stablecoins:** $16.53B circulating on Solana (-0.96% 7d) - $2.84 of stablecoin per dollar locked in DeFi (stablecoins are not a subset of DeFi TVL, so this ratio can exceed 1).
- **DEX volume:** $1.69B in 24h, $19.13B over 7d across 122 venues. Volume/TVL turnover 0.290x per day.
- **REV (chain fees):** $13.52M in 24h, $383.47M over 30d. Retained chain revenue $5.16M (38.2% of fees). Annualised fees are 8.37% of market cap.
- **Transaction fees:** base fee 5,000 lamports; median priority fee 0.00 micro-lamports/CU across 150 recent slots (0.0% of slots carried one). A modelled 200k-CU transaction costs 0.000005000 SOL (~$0.00).
- **Supply:** 586,731,026 SOL circulating of 634,018,266 total (92.54%).

## Ecosystem

### Top protocols by TVL on Solana

| # | Protocol | Category | TVL | 1d | 7d |
|--:|---|---|--:|--:|--:|
| 1 | Sanctum Validator LSTs | Liquid Staking | $1.53B | -2.0% | -3.3% |
| 2 | Kamino Lend | Lending | $1.34B | -0.7% | +1.0% |
| 3 | Raydium AMM | Dexs | $1.12B | -1.7% | +0.3% |
| 4 | Jupiter Lend | Lending | $1.09B | -1.2% | -1.3% |
| 5 | Binance Staked SOL | Liquid Staking | $1.03B | -2.3% | -3.7% |
| 6 | Jito Liquid Staking | Liquid Staking | $1.03B | -2.0% | -3.0% |
| 7 | BlackRock BUIDL | RWA | $992.60M | +0.0% | +1.5% |
| 8 | Jupiter Perpetual Exchange | Derivatives | $741.23M | -1.5% | -2.0% |
| 9 | Jupiter Staked SOL | Liquid Staking | $515.73M | -2.1% | -3.6% |
| 10 | Sentora Curator | Risk Curators | $389.44M | +0.1% | -0.4% |
| 11 | Marinade Native | Staking Pool | $380.17M | -2.2% | -6.8% |
| 12 | PumpSwap | Dexs | $327.77M | -0.2% | -3.5% |

The top five protocols hold 37.9% of Solana's tracked TVL. Summed across all 339 protocols the total is $16.12B. The per-protocol sum runs higher than the headline chain TVL because DeFiLlama strips double-counted value (liquid-staking tokens redeposited as lending collateral, and similar) from chain totals but reports it in each protocol's own figure. Both numbers are correct; they answer different questions.

**TVL by category:** Liquid Staking 37.1% · Lending 16.7% · Dexs 14.2% · RWA 12.0% · Derivatives 5.0% · Risk Curators 3.8%

### Tokenised assets

$2.24B of tokenised real-world assets and equities are locked on Solana - 13.879% of chain TVL.

- BlackRock BUIDL (RWA): $992.60M
- OnRe (RWA): $299.02M
- Solstice (Basis Trading): $235.01M
- Huma Finance V2 (RWA): $192.40M
- Ondo Yield Assets (RWA): $179.69M

*Tokenised real-world assets and equities on Solana, summed from DeFiLlama categories Basis Trading, RWA, RWA Lending, Tokenized Equities, Treasury Bonds. This is locked value, not traded volume - keyless per-venue equity volume is not published.*

### Address activity (proxy)

Across 3 sampled blocks, an average of **898.0 unique fee payers** signed per block (1,213 distinct addresses in the union, 55.0% overlap between blocks).

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
| [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) | 2026-09-11 | pre-release |
| [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) | 2026-09-10 | pre-release |
| [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) | 2026-09-04 | stable |
| [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) | 2026-09-03 | pre-release |
| [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) | 2026-08-28 | pre-release |

### Open SIMD proposals (live from the SIMD repository)

- [SIMD-0558: SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-12
- [SIMD-0602: SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-09-11
- [SIMD-0610: SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11
- [SIMD-0609: SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-11
- [SIMD-0376: Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0571: SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-09-09
- [SIMD-0582: SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-09
- [SIMD-0579: SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-09-08

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

### Change over 24h (vs run at 2026-09-12T14:30:07Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,491.18 | 3,924.00 | +12.40% |
| Average non-vote TPS | 1,366.96 | 1,796.97 | +31.46% |
| Average slot time (ms) | 317.40 | 316.40 | -0.32% |
| Active validators | 677.00 | 677.00 | +0.00% |
| Delinquent validators | 13.00 | 12.00 | -7.69% |
| Solana TVL | 5,898,998,874.00 | 5,826,154,858.00 | -1.23% |
| SOL price | 101.97 | 100.43 | -1.51% |
| Stablecoin supply | 16,553,783,165.00 | 16,525,122,331.00 | -0.17% |
| 24h DEX volume | 3,183,599,712.43 | 1,691,135,695.08 | -46.88% |
| 24h chain fees | 17,875,390.26 | 13,515,656.40 | -24.39% |

### Change over 7d (vs run at 2026-09-06T14:29:50Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 3,822.09 | 3,924.00 | +2.67% |
| Average non-vote TPS | 1,703.42 | 1,796.97 | +5.49% |
| Average slot time (ms) | 317.20 | 316.40 | -0.25% |
| Active validators | 676.00 | 677.00 | +0.15% |
| Delinquent validators | 17.00 | 12.00 | -29.41% |
| Solana TVL | 5,924,761,773.00 | 5,826,154,858.00 | -1.66% |
| SOL price | 106.04 | 100.43 | -5.29% |
| Stablecoin supply | 16,685,708,351.00 | 16,525,122,331.00 | -0.96% |
| 24h DEX volume | 1,960,574,882.81 | 1,691,135,695.08 | -13.74% |
| 24h chain fees | 10,482,001.50 | 13,515,656.40 | +28.94% |

### Change over 30d (vs run at 2026-08-14T18:37:41Z)

| Metric | Then | Now | Change |
|---|--:|--:|--:|
| Average TPS | 4,201.34 | 3,924.00 | -6.60% |
| Average non-vote TPS | 2,555.64 | 1,796.97 | -29.69% |
| Average slot time (ms) | 415.90 | 316.40 | -23.92% |
| Active validators | 689.00 | 677.00 | -1.74% |
| Delinquent validators | 9.00 | 12.00 | +33.33% |
| Solana TVL | 4,805,244,467.00 | 5,826,154,858.00 | +21.25% |
| SOL price | 75.00 | 100.43 | +33.91% |
| Stablecoin supply | 16,096,537,114.00 | 16,525,122,331.00 | +2.66% |
| 24h DEX volume | 1,942,768,290.75 | 1,691,135,695.08 | -12.95% |
| 24h chain fees | 10,148,326.92 | 13,515,656.40 | +33.18% |

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

This run made 35 HTTP calls (35 succeeded, 0 failed) in 34.1s of wall time.

---

Generated by [solana-ecosystem-pulse](https://github.com/antheducation/solana-ecosystem-pulse) - Python standard library only, zero API keys, zero installed packages.
