# LaunchTower Factor Research Report
**Date:** 2026-09-11 · **Universe:** 60 US large caps · **Model:** Momentum + Quality composite

## Methodology (reproducible)
- **Data:** Yahoo Finance daily closes (auto-adjusted), 252 trading days; fundamentals from Yahoo Ticker.info.
- **Momentum (50%):** 12-month return excluding the most recent month (12-1), z-scored cross-sectionally.
- **Secondary momentum (20%):** 6-month return, z-scored.
- **Quality (30%):** equal-weight z-scores of ROE, profit margins, and inverse debt/equity (median-imputed).
- **Composite score** = 0.5·mom₁₂₋₁ + 0.2·mom₆ + 0.3·quality. Higher = preferred.
- **Risk overlays:** annualized volatility and 12-month max drawdown reported for context (not in score).
- **Reproduce:** `yfinance` download of the 60-ticker universe → the exact formulas above. All inputs are public and dated; re-running on any later date regenerates the report.

## Top 10 (highest composite score)
| Ticker | Sector | 12-1 Mo | 6M | Ann Vol | ROE | Margin | Score |
|---|---|---|---|---|---|---|---|
| MU | Technology | +532% | +112% | 82% | 67% | 56% | +3.51 |
| INTC | Technology | +325% | +125% | 79% | -11% | -20% | +1.81 |
| AMD | Technology | +210% | +174% | 72% | 10% | 16% | +1.70 |
| AMAT | Technology | +216% | +70% | 60% | 41% | 30% | +1.33 |
| KLAC | Technology | +119% | +58% | 60% | 87% | 36% | +0.82 |
| ASML | Technology | +131% | +35% | 46% | 54% | 30% | +0.73 |
| PANW | Technology | +100% | +112% | 45% | 2% | 3% | +0.68 |
| CRWD | Technology | +108% | +87% | 54% | 1% | 1% | +0.58 |
| TSM | Technology | +68% | +25% | 40% | 40% | 50% | +0.40 |
| NVDA | Technology | +27% | +18% | 38% | 117% | 64% | +0.38 |

## Bottom 10 (lowest composite score)
| Ticker | Sector | 12-1 Mo | 6M | Ann Vol | ROE | Margin | Score |
|---|---|---|---|---|---|---|---|
| BSX | Healthcare | -50% | -38% | 38% | 15% | 17% | -0.84 |
| ORCL | Technology | -49% | -14% | 57% | 41% | 26% | -0.75 |
| GILD | Healthcare | +20% | -9% | 27% | -21% | -11% | -0.67 |
| NOW | Technology | -32% | -8% | 57% | 14% | 11% | -0.64 |
| BA | Industrials | +5% | +4% | 34% | 174% | 3% | -0.62 |
| NFLX | Communication Services | -35% | -23% | 36% | 50% | 28% | -0.55 |
| CRM | Technology | -18% | -13% | 47% | 19% | 22% | -0.54 |
| SYK | Healthcare | -11% | -6% | 29% | 17% | 14% | -0.48 |
| TSLA | Consumer Cyclical | -8% | +1% | 47% | 5% | 4% | -0.48 |
| DIS | Communication Services | -9% | -1% | 26% | 8% | 9% | -0.48 |

## Key observations
- The top of the ranking is dominated by **semiconductors / AI infrastructure** (MU, INTC, AMD, AMAT, KLAC, ASML, TSM) — strong 12-1 momentum with acceptable quality.
- **NVDA** ranks mid-table: excellent quality (ROE ~117%, margin ~64%) but 12-1 momentum is now modest (+27%), illustrating the momentum/quality trade-off.
- Bottom decile mixes negative-momentum names (ORCL, BSX, NOW) with low-quality profiles (GILD negative ROE).
- Volatility is elevated across the top decile (59–82% ann.) — position sizing should reflect this.

## Risk & disclaimers
- This is a **research note, not investment advice**. Scores are cross-sectional ranks, not probability estimates.
- Momentum signals can reverse abruptly; quality imputation (median debt/equity) affects a few names.
- No transaction costs, liquidity, or correlation constraints are modeled.
- Data as of 2026-09-11; re-run the pipeline for current values.

*LaunchTower — independent market-data desk. All data © Yahoo Finance, used for research.*
