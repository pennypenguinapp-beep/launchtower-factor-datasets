# LaunchTower — Factor Research (2026-09)

**Latest signal: 2026-09-16** (data through 2026-09-15 close)

## What this is

A reproducible, dated factor-score dataset for 151 liquid US large-caps.
Each row is a ticker with:

| Column | Definition |
|---|---|
| `ret_1m` | 1-month return |
| `ret_3m` | 3-month return |
| `ret_6m` | 6-month return |
| `ret_12m` | 12-month return |
| `vol_ann` | Annualized volatility (252-day) |
| `max_drawdown` | Max drawdown over the period |
| `from_52w_high` | Distance from 52-week high |
| `momentum_score` | Momentum z-score |
| `quality_score` | Quality z-score (inverse volatility) |
| `composite_score` | Composite: 50% momentum + 50% quality |

## Latest Rankings (2026-09-16)

**Top 5:**
1. **MU** (Micron) — +2.20 composite
2. **VLO** (Valero) — +0.82 composite
3. **INTC** (Intel) — +0.79 composite
4. **MPC** (Marathon Petroleum) — +0.67 composite
5. **PSX** (Phillips 66) — +0.63 composite

**Bottom 5:**
1. **SMCI** (Super Micro Computer) — -1.59 composite
2. **COIN** (Coinbase) — -1.30 composite
3. **MRNA** (Moderna) — -1.10 composite
4. **ZS** (Zscaler) — -1.09 composite
5. **HOOD** (Robinhood) — -1.07 composite

## How to reproduce

```python
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

universe = ["AAPL","MSFT","NVDA","GOOGL","AMZN","META","TSLA","AVGO","AMD","NFLX","ORCL","CRM","ADBE","CSCO","QCOM","TXN","MU","INTC","IBM","NOW","INTU","PLTR","SNOW","DDOG","NET","CRWD","PANW","ZS","FTNT","ANET","SMCI","ARM","MRVL","LRCX","AMAT","KLAC","ASML","ON","MPWR","MCHP","TER","ADSK","CDNS","SNPS","GFS","MRNA","LLY","NVO","UNH","JNJ","PFE","MRK","ABBV","BMY","TMO","DHR","ISRG","VRTX","REGN","AMGN","GILD","BSX","CVS","CI","HUM","ABT","SYK","ALGN","MDT","BABA","JD","PDD","SE","BIDU","UBER","ABNB","DASH","COIN","HOOD","PYPL","V","MA","AXP","BLK","SCHW","C","BAC","WFC","JPM","GS","MS","SPGI","ICE","CME","MCO","AIG","MET","PRU","TRV","ALL","CB","PGR","SPOT","T","VZ","TMUS","CMCSA","DIS","WMT","COST","HD","MCD","NKE","SBUX","TGT","UPS","CAT","DE","GE","BA","HON","UNP","CSX","NSC","LIN","APD","ECL","SHW","EMR","ETN","PH","ROK","WM","RSG","COP","XOM","CVX","SLB","OXY","EOG","DVN","PSX","VLO","MPC","PBR","BP","SHEL","TTE","RIO","FCX","NEM"]

end = datetime(2026, 9, 16)
start = datetime(2024, 9, 16)

data = yf.download(universe, start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'), 
                   auto_adjust=True, progress=False, threads=True)

close = data['Close']
rets = close.pct_change(fill_method=None)

ret_1m  = close.iloc[-1] / close.iloc[-22] - 1
ret_3m  = close.iloc[-1] / close.iloc[-64] - 1
ret_6m  = close.iloc[-1] / close.iloc[-127] - 1
ret_12m = close.iloc[-1] / close.iloc[-253] - 1

vol_ann = rets.rolling(252).std().iloc[-1] * np.sqrt(252)

def max_dd(s):
    s = s.dropna()
    if len(s) < 2: return 0.0
    rm = s.cummax()
    return float((s/rm - 1).min())

maxdd = close.rolling(252).apply(max_dd, raw=False).iloc[-1]

high_52w = close.rolling(252).max().iloc[-1]
from_high = close.iloc[-1] / high_52w - 1

def z(s):
    m, sd = s.mean(), s.std()
    if pd.isna(sd) or sd == 0: return pd.Series(0.0, index=s.index)
    return (s - m) / sd

mom_z = z(ret_12m)
vol_z = z(vol_ann)

composite = 0.5 * mom_z + 0.5 * (-vol_z)

results = pd.DataFrame({
    'ticker': universe,
    'last_price': close.iloc[-1].values,
    'ret_1m': ret_1m.values,
    'ret_3m': ret_3m.values,
    'ret_6m': ret_6m.values,
    'ret_12m': ret_12m.values,
    'vol_ann': vol_ann.values,
    'max_drawdown': maxdd.values,
    'from_52w_high': from_high.values,
    'momentum_score': mom_z.values,
    'quality_score': (-vol_z).values,
    'composite_score': composite.values
}).dropna().sort_values('composite_score', ascending=False).reset_index(drop=True)

results.insert(0, 'rank', range(1, len(results)+1))
results.insert(1, 'date', '2026-09-16')

results.to_csv('factors_2026-09-16.csv', index=False)
```

## Files

- `data/launchtower_signal_2026-09-16.csv` — latest dated signal (151 tickers)
- `reports/launchtower_factor_report_2026-09-16.md` — full research report (methodology, top/bottom picks)

## Buy the full pack

**LaunchTower Momentum Signal — $29**

Includes: dated factor dataset (CSV), full research report (Markdown),
reproduction script (Python), and this repo.

> **🛒 BUY NOW:** https://whop.com/checkout/ch_lRnmk2lkgdB92fl/
>
> **Store:** https://whop.com/biz_PafLwqOjrf2HRB/

## Disclaimer

This is research data, not investment advice. Past factor performance does not
guarantee future results. Do your own due diligence.

---
*LaunchTower — independent market-data research.*
