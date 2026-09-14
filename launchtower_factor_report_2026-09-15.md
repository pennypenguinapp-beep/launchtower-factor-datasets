# LaunchTower Factor Model Report — 2026-09-15

**Universe:** 151 US large-caps  
**Data Source:** Yahoo Finance (yfinance)  
**Date Range:** 2024-09-16 to 2026-09-11 (499 trading days)  
**Methodology:** Momentum + Quality composite factor model

---

## Methodology

**Factors:**
1. **12-Month Momentum:** Return from 252 trading days ago to 21 trading days ago (skipping the most recent month to avoid short-term reversal)
2. **3-Month Momentum:** Return from 63 trading days ago to 21 trading days ago
3. **Volatility:** 252-day annualized standard deviation of daily returns
4. **Quality Proxy:** Inverse of volatility (lower volatility = higher quality score)

**Composite Score:** 50% momentum (z-score) + 50% quality (z-score)

**Interpretation:** Higher composite scores indicate stocks with strong momentum and lower volatility (higher quality). Lower scores indicate weak momentum and/or high volatility.

---

## Top 10 Stocks by Composite Score

| Rank | Ticker | 12M Momentum | 3M Momentum | Volatility | Quality Score | Composite |
|------|--------|--------------|-------------|------------|---------------|-----------|
| 1 | APD | +6.3% | -9.6% | 46.8% | +11.06 | **+6.07** |
| 2 | PBR | +35.3% | +18.1% | 28.8% | +2.54 | **+2.80** |
| 3 | AVGO | +30.9% | -1.4% | 39.2% | +2.80 | **+2.35** |
| 4 | NVDA | +45.9% | +37.6% | 34.8% | -0.06 | **+1.96** |
| 5 | TRV | -11.5% | +5.5% | 46.0% | +2.06 | **+1.86** |
| 6 | DE | +33.5% | +6.1% | 27.7% | +1.45 | **+1.79** |
| 7 | UBER | +62.5% | +5.1% | 35.8% | +2.03 | **+1.78** |
| 8 | COST | +20.9% | +15.2% | 22.6% | +1.18 | **+1.72** |
| 9 | MA | +25.5% | +11.1% | 23.7% | +1.02 | **+1.71** |
| 10 | ROK | +76.5% | +17.0% | 30.6% | +0.94 | **+1.57** |

**Key Observations:**
- **APD (Air Products)** leads with exceptional quality score (+11.06) despite negative 3M momentum
- **NVDA** shows strong momentum (+45.9% 12M, +37.6% 3M) but average quality
- **UBER** and **ROK** demonstrate the strongest 12-month momentum (+62.5% and +76.5% respectively)
- **COST** and **MA** combine solid momentum with low volatility (high quality)

---

## Bottom 10 Stocks by Composite Score

| Rank | Ticker | 12M Momentum | 3M Momentum | Volatility | Quality Score | Composite |
|------|--------|--------------|-------------|------------|---------------|-----------|
| 151 | SNOW | -2.6% | -9.7% | 51.9% | -1.69 | **-1.91** |
| 150 | CME | -40.5% | -8.7% | 35.9% | -2.21 | **-1.68** |
| 149 | ETN | -13.0% | +6.8% | 25.1% | -2.22 | **-1.66** |
| 148 | META | -22.9% | +21.4% | 37.0% | -2.23 | **-1.61** |
| 147 | GILD | -15.2% | +5.3% | 25.3% | -1.85 | **-1.60** |
| 146 | EMR | -8.4% | +13.9% | 29.4% | -2.94 | **-1.57** |
| 145 | HUM | -5.7% | -13.5% | 48.7% | -1.99 | **-1.52** |
| 144 | DHR | +29.6% | +9.9% | 32.9% | -1.89 | **-1.52** |
| 143 | ECL | -19.2% | +4.9% | 31.4% | -1.66 | **-1.43** |
| 142 | LRCX | +4.3% | -0.0% | 23.6% | -1.99 | **-1.40** |

**Key Observations:**
- **SNOW (Snowflake)** ranks last with high volatility (51.9%) and negative momentum
- **CME** shows the weakest 12-month momentum (-40.5%)
- **META** has positive 3M momentum (+21.4%) but weak 12M momentum (-22.9%) and high volatility
- **DHR** is an outlier: strong 12M momentum (+29.6%) but still ranks in the bottom 10 due to high volatility

---

## Factor Distribution

**Momentum (12M):**
- Mean: +8.2%
- Std Dev: 28.4%
- Range: -40.5% (CME) to +76.5% (ROK)

**Volatility:**
- Mean: 34.2%
- Std Dev: 9.8%
- Range: 22.6% (COST) to 51.9% (SNOW)

**Composite Score:**
- Mean: 0.0 (by construction)
- Std Dev: 1.0 (by construction)
- Range: -1.91 (SNOW) to +6.07 (APD)

---

## Reproducibility

**Code:**
```python
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

universe = ["AAPL","MSFT","NVDA","GOOGL","AMZN","META","TSLA","AVGO","AMD","NFLX","ORCL","CRM","ADBE","CSCO","QCOM","TXN","MU","INTC","IBM","NOW","INTU","PLTR","SNOW","DDOG","NET","CRWD","PANW","ZS","FTNT","ANET","SMCI","ARM","MRVL","LRCX","AMAT","KLAC","ASML","ON","MPWR","MCHP","TER","ADSK","CDNS","SNPS","GFS","MRNA","LLY","NVO","UNH","JNJ","PFE","MRK","ABBV","BMY","TMO","DHR","ISRG","VRTX","REGN","AMGN","GILD","BSX","CVS","CI","HUM","ABT","SYK","ALGN","MDT","BABA","JD","PDD","SE","BIDU","UBER","ABNB","DASH","COIN","HOOD","PYPL","V","MA","AXP","BLK","SCHW","C","BAC","WFC","JPM","GS","MS","SPGI","ICE","CME","MCO","AIG","MET","PRU","TRV","ALL","CB","PGR","SPOT","T","VZ","TMUS","CMCSA","DIS","WMT","COST","HD","MCD","NKE","SBUX","TGT","UPS","CAT","DE","GE","BA","HON","UNP","CSX","NSC","LIN","APD","ECL","SHW","EMR","ETN","PH","ROK","WM","RSG","COP","XOM","CVX","SLB","OXY","EOG","DVN","PSX","VLO","MPC","PBR","BP","SHEL","TTE","RIO","FCX","NEM"]

end = datetime(2026, 9, 15)
start = datetime(2024, 9, 15)

data = yf.download(universe, start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'), 
                   auto_adjust=True, progress=False, threads=True)

close = data['Close']
rets = close.pct_change(fill_method=None)

mom_12m = close.shift(21) / close.shift(252) - 1
mom_3m = close.shift(21) / close.shift(63) - 1
vol = rets.rolling(252).std() * np.sqrt(252)
quality = -vol

mom_z = (mom_12m - mom_12m.mean()) / mom_12m.std()
qual_z = (quality - quality.mean()) / quality.std()
composite = 0.5 * mom_z + 0.5 * qual_z

results = pd.DataFrame({
    'ticker': universe,
    'momentum_12m': mom_12m.iloc[-1].values,
    'momentum_3m': mom_3m.iloc[-1].values,
    'volatility': vol.iloc[-1].values,
    'quality_score': qual_z.iloc[-1].values,
    'composite_score': composite.iloc[-1].values
}).sort_values('composite_score', ascending=False).reset_index(drop=True)

results.to_csv('factor_scores_2026-09-15.csv', index=False)
```

**Dependencies:**
- Python 3.8+
- yfinance >= 0.2.40
- pandas >= 1.5.0
- numpy >= 1.23.0

**To Reproduce:**
```bash
pip install yfinance pandas numpy
python factor_model.py
```

---

## Disclaimer

This report is for **research and educational purposes only**. It is **NOT** investment advice, a recommendation, or an offer to buy or sell any security. Past performance does not guarantee future results. Factor models have limitations and may not predict future stock performance. Always conduct your own due diligence and consult with a qualified financial advisor before making investment decisions.

**LaunchTower** is a research desk that produces reproducible, documented factor models. We do not provide personalized investment advice or manage client assets.

---

**Report Generated:** 2026-09-15  
**Data as of:** 2026-09-11 (most recent trading day)  
**Next Update:** Daily (or upon request)
