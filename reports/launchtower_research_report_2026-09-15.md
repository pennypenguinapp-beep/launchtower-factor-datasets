# LaunchTower Research Report — Momentum + Quality Factor Screen
**Date:** 2026-09-15 (data as of 2026-09-11 close, latest available)
**Universe:** 95 liquid US mega-cap equities (tech, semis, industrials, energy, consumer)
**Method:** 12-1 month momentum (50%) + 1-year Sharpe (30%) + low-volatility (10%) + low-drawdown (10%)
**Data source:** Yahoo Finance (yfinance), auto-adjusted daily closes, trailing 2 years

---

## Executive Summary

The composite score ranks each name on a z-scored blend of momentum and risk-adjusted quality.
The top of the table is now dominated by the **memory / storage / optical complex** — Micron,
Lumentum, Western Digital, Seagate, Intel, Teradyne, Marvell, and Coherent all rank in the top 10.
This is a meaningful rotation from the prior screen (2026-09-14), where the top was led by
semiconductor *equipment* (AMAT, LRCX, KLAC) and energy (MPC). The new leaders are the
*components* of the AI data-center buildout: HBM memory (MU), optical transceivers (LITE, COHR),
and nearline storage (WDC, STX).

The bottom of the table is led by **consumer software, gaming, and China-exposed names** that
have underperformed over the trailing 12 months: Mens Sana, Tencent Music, Trade Desk, NuScale,
Roblox, Nike, MicroStrategy, HubSpot, Intuit, and Grab all carry negative 12-month momentum and
negative Sharpe ratios.

> **This is a research screen, not a recommendation.** Past momentum does not guarantee future
> returns. All data is point-in-time and subject to revision.

---

## What Changed Since the 2026-09-14 Screen

| Ticker | Prior rank | New rank | Direction |
|---|---|---|---|
| MU | 1 | 1 | — (still #1) |
| LITE | — | 2 | **new entrant** |
| WDC | — | 3 | **new entrant** |
| STX | — | 4 | **new entrant** |
| INTC | 2 | 5 | ↓ |
| AMAT | 3 | 6 | ↓ |
| TER | — | 7 | **new entrant** |
| MRVL | — | 8 | **new entrant** |
| COHR | — | 9 | **new entrant** |
| AMD | 4 | 10 | ↓ |
| LRCX | 5 | 11 | ↓ (out of top 10) |
| MPC | 6 | 12 | ↓ (out of top 10) |
| ASML | 7 | — | out of top 10 |
| CAT | 8 | — | out of top 10 |
| KLAC | 9 | — | out of top 10 |
| FDX | 10 | — | out of top 10 |

**Interpretation:** The screen has rotated from *equipment* to *components*. The AI capex
cycle is now showing up in the P&Ls of memory, optical, and storage makers — the names that
actually ship the HBM, transceivers, and nearline drives that data centers consume. Equipment
makers (AMAT, LRCX, KLAC) remain in the top half but have lost their top-10 positions.

---

## Methodology

| Component | Weight | Definition |
|---|---|---|
| Momentum (12-1) | 50% | Return from t-252 to t-22 (skip last month to avoid short-term reversal) |
| Quality (Sharpe) | 30% | Annualized mean daily return / annualized daily vol, trailing 252 days |
| Low Volatility | 10% | Inverse z-score of annualized realized vol, trailing 252 days |
| Low Drawdown | 10% | Inverse z-score of max drawdown from peak, trailing 252 days |

All components are z-scored across the 95-name universe before weighting. A higher composite
score indicates stronger momentum and better risk-adjusted performance.

**Data notes:**
- Prices are auto-adjusted (dividends and splits adjusted) daily closes from Yahoo Finance.
- Sharpe ratio assumes a risk-free rate of 0 (gross Sharpe).
- Universe excludes names with fewer than 252 trading days of history.
- 1 ticker (OTIV) was dropped for lack of data; 95 of 96 requested tickers returned usable history.

---

## Top 10 — Strongest Momentum + Quality

| Rank | Ticker | Name | Price | 12M Ret | 12-1 Mom | Sharpe | MaxDD 1Y | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | MU | Micron | $975.26 | +548.8% | +506.2% | 2.71 | -39.1% | **+2.512** |
| 2 | LITE | Lumentum | $927.03 | +462.2% | +465.5% | 2.27 | -42.8% | **+2.160** |
| 3 | WDC | Western Digital | $447.18 | +365.9% | +373.0% | 2.33 | -41.8% | **+1.837** |
| 4 | STX | Seagate | $830.17 | +325.3% | +349.9% | 2.31 | -31.8% | **+1.698** |
| 5 | INTC | Intel | $102.94 | +318.3% | +310.2% | 2.19 | -41.9% | **+1.526** |
| 6 | AMAT | Applied Materials | $456.49 | +169.8% | +223.6% | 1.97 | -39.6% | **+1.166** |
| 7 | TER | Teradyne | $379.72 | +229.2% | +249.0% | 1.95 | -34.0% | **+1.160** |
| 8 | MRVL | Marvell | $236.10 | +255.3% | +226.7% | 2.00 | -48.4% | **+1.142** |
| 9 | COHR | Coherent | $305.37 | +195.0% | +243.6% | 1.71 | -48.0% | **+1.114** |
| 10 | AMD | AMD | $516.13 | +231.6% | +210.2% | 2.03 | -27.8% | **+0.992** |

**Observation:** 8 of the top 10 are semiconductor or semi-adjacent names. The memory cycle
(Micron, Intel) and the optical/storage cycle (Lumentum, Coherent, Western Digital, Seagate)
are the primary drivers. Micron's +549% 12-month return is the single largest contributor to
its #1 score. Lumentum's +462% run is the second-largest, driven by 800G/1.6T optical
transceiver demand for AI clusters.

---

## Bottom 10 — Weakest Momentum + Quality

| Rank | Ticker | Name | Price | 12M Ret | 12-1 Mom | Sharpe | MaxDD 1Y | Score |
|---|---|---|---|---|---|---|---|---|
| 86 | GRAB | Grab | $3.05 | -44.9% | -34.7% | -1.36 | -53.3% | **-0.667** |
| 87 | INTU | Intuit | $321.57 | -50.8% | -48.8% | -1.21 | -63.4% | **-0.681** |
| 88 | HUBS | HubSpot | $225.33 | -54.6% | -57.7% | -0.72 | -67.4% | **-0.688** |
| 89 | MSTR | MicroStrategy | $130.97 | -59.8% | -70.9% | -0.75 | -77.1% | **-0.734** |
| 90 | NKE | Nike | $36.80 | -48.9% | -44.3% | -1.67 | -49.3% | **-0.803** |
| 91 | RBLX | Roblox | $45.50 | -65.8% | -73.3% | -1.25 | -74.9% | **-0.823** |
| 92 | SMR | NuScale | $8.61 | -75.5% | -72.7% | -0.86 | -85.8% | **-0.831** |
| 93 | TTD | Trade Desk | $14.34 | -68.3% | -70.2% | -1.76 | -75.9% | **-0.883** |
| 94 | TME | Tencent Music | $7.98 | -68.0% | -66.1% | -2.19 | -69.3% | **-0.968** |
| 95 | MNSO | Mens Sana | $9.07 | -63.3% | -51.8% | -2.58 | -63.3% | **-0.990** |

**Observation:** The bottom of the table is a mix of consumer software (HubSpot, Intuit,
Trade Desk), gaming (Roblox), China-exposed names (Tencent Music, Grab), and high-beta
crypto-adjacent (MicroStrategy). All 10 carry negative 12-month returns and negative Sharpe
ratios — the weakest risk-adjusted profiles in the universe.

---

## Reproducibility

To reproduce this report:

```python
import yfinance as yf
import pandas as pd
import numpy as np

# 1. Fetch 2y daily closes for the 95-ticker universe
# 2. Compute:
#    - 12-1 momentum: close[-22] / close[-252] - 1
#    - Annualized vol: std(daily_returns, 252d) * sqrt(252)
#    - Sharpe: mean(daily_returns, 252d) * 252 / annualized_vol
#    - Max drawdown: min(close / cummax(close) - 1) over 252d
# 3. Z-score each component across the universe
# 4. Composite = 0.50*z_mom + 0.30*z_sharpe + 0.10*z_lowvol + 0.10*z_lowdd
# 5. Sort descending
```

**Raw data:** `factor_scores_2026-09-15.csv` (this repository)
**Report generated:** 2026-09-15
**Next scheduled update:** monthly (first trading day)

---

*LaunchTower is a self-funded research desk. This report is for informational purposes only
and does not constitute investment advice, a solicitation, or a recommendation to buy or sell
any security. All data is sourced from Yahoo Finance and is provided as-is without warranty.*
