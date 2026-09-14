# LaunchTower — Factor Model Datasets

**Independent market-data research desk.** Dated, reproducible momentum + quality factor screens on US large/mid-cap stocks. Every number is pulled from a public source (Yahoo Finance), computed with a fixed, documented model, and published with the date it was generated.

## Latest signal — 2026-09-14

- **Universe:** 64 US large/mid-cap stocks
- **Last bar:** 2026-09-11 (Yahoo Finance daily closes, auto-adjusted)
- **Top of the board:** DELL, VLO, MPC, CRM, MU, PSX, HPE
- **Bottom of the board:** AVGO, FSLR, ISRG, WMT, BA
- **Breadth:** 7 stocks at 52-week highs · 11 stocks more than 30% below theirs

**Full dataset:** [`factors_2026-09-14.csv`](factors_2026-09-14.csv) · **Report:** [`report_2026-09-14.md`](report_2026-09-14.md)

## What's in this repo

| File | What it is |
|---|---|
| `factors_2026-09-14.csv` | Full 64-stock factor screen — rank, last price, 1M/3M/6M/12M returns, annualized volatility, max drawdown, distance from 52-week high, momentum/quality/composite scores |
| `report_2026-09-14.md` | Dated research report with top-10 / bottom-5 tables, sector read, and breadth analysis |
| `README.md` | This file — methodology and reproducibility |

## Methodology (fixed, no fitted parameters)

- **Composite** = 0.6 × momentum percentile + 0.4 × quality percentile
- **Momentum** = 0.25 × 1-month return + 0.75 × 6-month return
- **Quality** = 0.5 × (inverse annualized volatility) + 0.5 × (proximity to 52-week high)
- **Data:** Yahoo Finance, 1-year daily window, `auto_adjust=True`
- **Scoring:** pure percentile ranks — no look-ahead, no fitted parameters, reproducible in under 5 minutes

## Reproduce it

```python
import yfinance as yf, pandas as pd, numpy as np
# pull 1y of daily closes for the universe, compute the returns/vol/drawdown above,
# rank by percentile, and combine. The full script is in the research pack.
```

## Get the full pack

The free preview above is the latest signal. The **LaunchTower Factor Model Pack** adds the complete dated dataset, the full report, and the reproducible script.

👉 **Buy the pack:** [whop.com/biz_PafLwqOjrf2HRB](https://whop.com/biz_PafLwqOjrf2HRB)

---
*LaunchTower is an independent research desk. This is research, not investment advice. No position sizing, no risk model, no return promises. Past performance does not guarantee future results. Do your own research.*
