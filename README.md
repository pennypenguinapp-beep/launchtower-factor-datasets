# LaunchTower Factor Datasets

**Independent market-data desk. Real data, reproducible methodology, no hype.**

This repo hosts dated, reproducible factor research from LaunchTower. Every file is generated from public market data (yfinance) with a documented, cross-sectional scoring method — so anyone can re-run the numbers and check our work.

## What's inside

| File | Description |
|------|-------------|
| `data/launchtower_factors_2026-09-11.csv` | Full factor table: 19 large/mega-cap US tech & growth names, momentum + quality z-scores, composite ranking (data as of 2026-09-11 close) |
| `reports/momentum-quality-2026-09-11.md` | The dated research report: methodology, top/bottom 5, and a read of the tape |

## Methodology (2026-09-11 report)

- **Universe:** 19 large/mega-cap US tech & growth names (SQ excluded — delisted/renamed, no data)
- **Data:** 499 trading days (2024-09-16 → 2026-09-11), split/dividend-adjusted closes via `yfinance`
- **Momentum:** equal-weight of 1m / 3m / 6m / 12m return z-scores (252-day windows)
- **Quality:** negative z of 12m realized volatility and 12m max drawdown
- **Composite:** `0.6 × momentum + 0.4 × quality`
- All scores are cross-sectional z-scores within the universe

## Top 5 (2026-09-11)

| # | Ticker | 3m ret | 12m ret | 12m vol | 12m maxDD | Composite |
|---|--------|--------|---------|---------|-----------|-----------|
| 1 | CRM | +48.8% | +3.0% | 47.2% | −43.3% | **0.721** |
| 2 | AMD | +5.7% | +223.5% | 71.7% | −27.8% | **0.650** |
| 3 | MSFT | +27.2% | −0.1% | 32.4% | −34.5% | **0.283** |
| 4 | AAPL | +12.5% | +47.1% | 25.1% | −13.8% | **0.246** |
| 5 | MSTR | +9.0% | −59.9% | 79.7% | −77.1% | **0.157** |

## CSV columns

`rank, ticker, price, ret_1m, ret_3m, ret_6m, ret_12m, vol_12m, maxdd_12m, momentum, quality, composite`

- Returns are simple (adjusted-close) returns over the trailing window
- `vol_12m` = annualized realized volatility over the trailing 12 months
- `maxdd_12m` = maximum drawdown over the trailing 12 months (negative)
- `momentum`, `quality`, `composite` are cross-sectional z-scores / weighted composite

## Reproducing

```python
import yfinance as yf
import pandas as pd

tickers = ["CRM","AMD","MSFT","AAPL","MSTR","ABNB","META","TSM","PLTR","COIN",
           "AMZN","GOOGL","NVDA","NFLX","TSLA","UBER","SHOP","ORCL","AVGO"]
end = "2026-09-11"
start = "2024-09-16"
px = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]

def z(s): return (s - s.mean()) / s.std()

mom = (z(px.pct_change(21)) + z(px.pct_change(63)) + z(px.pct_change(126)) + z(px.pct_change(252))) / 4
vol = px.pct_change().rolling(252).std().iloc[-1] * (252 ** 0.5)
dd  = (px / px.cummax() - 1).iloc[-1]
qual = -(z(vol) + z(dd)) / 2
composite = 0.6 * mom + 0.4 * qual
```

## Disclaimer

LaunchTower is an independent market-data desk. This content is generated from public data for research and educational purposes. **It is not investment advice**, not personalized, and not a recommendation to buy or sell any security. Past factor rankings do not predict future performance. Do your own research.
