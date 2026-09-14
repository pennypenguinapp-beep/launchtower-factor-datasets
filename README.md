# LaunchTower Factor Datasets

Independent, reproducible factor research on US equities. Every file is generated from public Yahoo Finance data with a fixed, documented methodology — no fitted parameters, no look-ahead.

## Latest screen: 2026-09-14 (131 stocks)

**Top 5:** BAC · PSX · MPC · HPE · AAPL
**Bottom 5:** ORCL · COIN · ISRG · NKE · INTU

📄 [Full report](reports/2026-09-14.md) · [Raw CSV](data/factors_2026-09-14.csv)

## Methodology

Composite score = 0.6 × momentum percentile + 0.4 × quality percentile
- **Momentum** = 0.25 × 1-month return + 0.75 × 6-month return
- **Quality** = 0.5 × (inverse annualized volatility) + 0.5 × (proximity to 52-week high)

Data: `yfinance`, 1-year daily window, auto-adjusted closes.

## Files

| File | Description |
|---|---|
| `data/factors_2026-09-14.csv` | 131 stocks × 12 columns: rank, ticker, last price, 1M/3M/6M returns, annualized vol, drawdown from high, momentum, quality, composite score |
| `reports/2026-09-14.md` | Dated research report with top/bottom tables and sector read |

## Disclaimer

LaunchTower is an independent research desk. Nothing here is investment advice, an offer, or a recommendation. Past performance does not guarantee future results.
