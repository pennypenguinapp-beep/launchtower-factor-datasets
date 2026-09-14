# LaunchTower Factor Datasets

Independent market-data desk. Dated, reproducible factor research on large/mega-cap US tech & growth names.

## Momentum + Quality Factor Report — 2026-09-11

**Universe:** 19 large/mega-cap US tech & growth names (SQ excluded — delisted/renamed, no data)
**Observations:** 499 trading days (2024-09-16 → 2026-09-11), split/dividend-adjusted closes via `yfinance`.

### Method
- **Momentum** = equal-weight of cross-sectional z-scores of 1m / 3m / 6m / 12m returns.
- **Quality** = negative z-score of 12m realized volatility and 12m max drawdown.
- **Composite** = 0.6 × momentum + 0.4 × quality.
- All z-scores computed cross-sectionally within the universe for the report date.

> Not investment advice. Reproducible: `yfinance` download, 252-day windows, z-scored cross-sectionally.

### Top 5 (highest composite)
| # | Ticker | Price | 3m ret | 12m ret | 12m vol | 12m maxDD | Momentum | Quality | Composite |
|---|--------|-------|--------|---------|---------|-----------|----------|---------|-----------|
| 1 | CRM | 247.72 | +48.8% | +3.0% | 47.2% | −43.3% | 1.090 | 0.167 | **0.721** |
| 2 | AMD | 516.13 | +5.7% | +223.5% | 71.7% | −27.8% | 1.795 | −1.068 | **0.650** |
| 3 | MSFT | 495.63 | +27.2% | −0.1% | 32.4% | −34.5% | 0.212 | 0.390 | **0.283** |
| 4 | AAPL | 332.27 | +12.5% | +47.1% | 25.1% | −13.8% | 0.386 | 0.037 | **0.246** |
| 5 | MSTR | 130.97 | +9.0% | −59.9% | 79.7% | −77.1% | 0.205 | 0.084 | **0.157** |

### Bottom 5 (lowest composite)
| # | Ticker | Price | 3m ret | 12m ret | 12m vol | 12m maxDD | Composite |
|---|--------|-------|--------|---------|---------|-----------|-----------|
| 15 | TSLA | 365.44 | −8.5% | +5.1% | 47.5% | −39.1% | −0.183 |
| 16 | UBER | 71.67 | +3.1% | −23.9% | 35.9% | −34.1% | −0.218 |
| 17 | SHOP | 128.79 | +16.6% | −9.4% | 58.4% | −46.7% | −0.294 |
| 18 | ORCL | 150.28 | −18.1% | −53.7% | 57.2% | −64.6% | −0.396 |
| 19 | AVGO | 361.99 | −6.0% | −1.3% | 46.2% | −28.7% | −0.496 |

### Read of the tape
- **CRM** leads on momentum (strong 3m run) with acceptable quality — cleanest composite.
- **AMD** is a pure momentum story: +223% over 12m but very high vol (72%) and negative quality; the model still ranks it #2 because momentum dominates the 60/40 weighting.
- **AAPL** is the quality anchor: lowest vol (25%) and shallowest drawdown (−14%) in the universe.
- **AVGO/ORCL** are the clear laggards: negative 3m and 12m returns with elevated vol.

### Data notes
- SQ excluded (yfinance: "possibly delisted").
- All prices are split/dividend-adjusted closes.
- Full factor table: [`data/launchtower_factors_2026-09-11.csv`](data/launchtower_factors_2026-09-11.csv).

---
*LaunchTower — independent market-data desk. Generated from public data; not personalized investment advice.*
