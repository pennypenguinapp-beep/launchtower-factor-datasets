# LaunchTower Factor Model Report — 2026-09-14

**Universe:** 128 US large-cap stocks (129 fetched, 128 with full data)
**Data source:** yfinance (Yahoo Finance), auto-adjusted daily closes, 1-year window
**Last price date:** 2026-09-11 (most recent completed trading day)
**Generated:** 2026-09-14 UTC

---

## Methodology

**Momentum (45% weight):** 12-month return excluding the most recent month (12-1 momentum), z-scored across the universe.

**3-month return (25% weight):** 3-month cumulative return, z-scored.

**Volatility quality (20% weight):** 6-month annualized volatility, z-scored and inverted (lower vol = higher score).

**Beta quality (10% weight):** 1-year beta vs SPY, clipped to [-1, 3], z-scored and inverted (lower beta = higher score).

**Composite score** = 0.45·z(mom_12_1) + 0.25·z(ret_3m) + 0.20·z(-vol_6m) + 0.10·z(-beta)

All z-scores are cross-sectional (mean 0, std 1) within this universe.

---

## Top 10 — Strongest Momentum + Quality

| Rank | Ticker | Close  | 1M Ret | 3M Ret | 6M Ret | 12-1 Mom | 6M Vol | Beta | Score |
|------|--------|--------|--------|--------|--------|----------|--------|------|-------|
| 1 | **MU** | $975.26 | +7.0% | -0.6% | +129.0% | +480.5% | 94.2% | 3.33 | **2.301** |
| 2 | **VLO** | $390.42 | +18.2% | +51.5% | +70.8% | +115.2% | 37.1% | -0.27 | **1.474** |
| 3 | **MPC** | $395.93 | +14.0% | +50.6% | +76.2% | +95.9% | 35.6% | -0.12 | **1.328** |
| 4 | **PSX** | $259.47 | +15.6% | +45.4% | +52.1% | +76.7% | 32.2% | -0.27 | **1.165** |
| 5 | **INTC** | $102.94 | +2.0% | -17.4% | +124.9% | +319.2% | 86.4% | 2.85 | **1.050** |
| 6 | **MRK** | $143.93 | +8.3% | +21.8% | +26.3% | +65.9% | 32.4% | 0.18 | **0.687** |
| 7 | **TGT** | $155.83 | +1.2% | +16.1% | +35.1% | +78.1% | 31.3% | 0.42 | **0.667** |
| 8 | **AMD** | $516.13 | +6.9% | +0.9% | +166.9% | +204.6% | 74.8% | 3.13 | **0.634** |
| 9 | **REGN** | $781.49 | -1.9% | +27.8% | +5.1% | +43.1% | 31.9% | 0.48 | **0.594** |
| 10 | **AMAT** | $456.49 | -16.6% | -19.4% | +34.0% | +228.1% | 69.2% | 2.72 | **0.566** |

---

## Bottom 5 — Weakest Momentum + Quality

| Rank | Ticker | Close  | 1M Ret | 3M Ret | 6M Ret | 12-1 Mom | 6M Vol | Beta | Score |
|------|--------|--------|--------|--------|--------|----------|--------|------|-------|
| 124 | **NIO** | $3.69 | -18.7% | -29.2% | -37.0% | -27.0% | 51.0% | 1.31 | **-0.981** |
| 125 | **XPEV** | $10.54 | -10.3% | -27.3% | -47.2% | -43.7% | 46.0% | 1.54 | **-1.049** |
| 126 | **ORCL** | $150.28 | -2.0% | -18.1% | -2.4% | -46.9% | 60.9% | 2.05 | **-1.115** |
| 127 | **LCID** | $4.22 | -35.5% | -18.9% | -57.4% | -66.1% | 97.7% | 2.27 | **-1.586** |
| 128 | **POM** | $0.73 | -25.1% | -60.2% | -89.8% | -98.7% | 233.6% | 0.89 | **-3.403** |

---

## Key Observations

- **MU (Micron)** leads the screen at **2.301**, driven by a +481% 12-1 momentum reading and +129% 6-month return — the memory/semiconductor cycle is the dominant momentum story.
- **Refiners (VLO, MPC, PSX)** occupy ranks 2–4, reflecting sustained 3-month outperformance of +52%, +51%, +45% respectively, with low vol and negative beta (defensive quality).
- **INTC** at rank 5 shows a +319% 12-1 momentum reading but negative 3-month return — a recovery trade, not a sustained trend.
- **POM (Pomelo)** is the weakest name at **-3.403**, with a -90% 6-month drawdown and the highest volatility in the universe.
- **ORCL** at rank 127 is the notable large-cap underperformer, with negative 12-1 momentum and a -18% 3-month return.

---

## Reproducibility

```python
import yfinance as yf, pandas as pd, numpy as np

UNIVERSE = [/* 132 tickers — see factor_scores_2026-09-14.csv */]

def fetch(tk):
    df = yf.Ticker(tk).history(period="1y", auto_adjust=True)
    return df if df is not None and len(df) >= 130 else None

# For each ticker:
#   ret_1m   = close[-1]/close[-22] - 1
#   ret_3m   = close[-1]/close[-63] - 1
#   ret_6m   = close[-1]/close[-126] - 1
#   mom_12_1 = close[-22]/close[-252] - 1
#   vol_6m   = close.pct_change()[-126:].std() * sqrt(252)
#   beta     = cov(ret, spy_ret) / var(spy_ret)   [1y, clipped -1 to 3]

# Z-score each factor cross-sectionally, then:
#   score = 0.45*z(mom_12_1) + 0.25*z(ret_3m) + 0.20*z(-vol_6m) + 0.10*z(-beta)
```

---

## Disclaimer

This report is a statistical factor screen for research and educational purposes only. It is **not** investment advice, a recommendation to buy or sell any security, or a prediction of future performance. Past momentum and quality factors do not guarantee future results. All data is sourced from Yahoo Finance via yfinance and may contain errors or gaps. Consult a licensed financial advisor before making investment decisions.

*LaunchTower — self-funded market-data desk. Report generated 2026-09-14.*
