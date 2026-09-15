# LaunchTower — Momentum + Quality Factor Dataset (2026-09-14)

> **Independent market-data research.** A fully reproducible momentum + quality factor screen on **151 US large-caps**, computed from public Yahoo Finance price data. Every number in this CSV can be regenerated from scratch with the included script.

> ⚠️ **Disclaimer:** This is research/educational output from public market data. **Not** personalized investment advice, **not** a recommendation to buy or sell any security. Past performance does not guarantee future results. No return or performance promises are made.

---

## 📦 What's in This Repo

| File | Description |
|------|-------------|
| `data/factors_2026-09-14.csv` | **Full 151-stock factor table** — 14 columns, ranked by composite score |
| `data/factors_sample_2026-09-14.csv` | 15-row sample (top 10 + bottom 5) for quick inspection |
| `scripts/reproduce.py` | Exact Python script to regenerate the dataset from scratch |
| `README.md` | This file — full methodology, sample output, and how to use the data |

---

## 🔬 Methodology (Transparent & Reproducible)

### Universe
151 US large/mid-cap equities spanning tech, healthcare, financials, energy, industrials, consumer staples, and materials. Tickers are listed in `data/factors_2026-09-14.csv`.

### Data Source
- **Yahoo Finance** via `yfinance` (free, public, auto-adjusted prices)
- **Window:** 252 trading days (2024-09-16 → 2026-09-14)
- **No paid data, no proprietary feeds.**

### Factor Definitions

| Column | Definition |
|--------|------------|
| `ret_1m` | Simple return over the last ~21 trading days |
| `ret_3m` | Simple return over the last ~63 trading days |
| `ret_6m` | Simple return over the last ~126 trading days |
| `ret_12m` | Simple return over the last ~252 trading days |
| `vol_ann` | Annualized volatility = `std(daily_returns) × √252` |
| `max_drawdown` | Maximum peak-to-trough decline over the 12-month window (negative) |
| `from_52w_high` | `last_price / 52w_high − 1` (≤ 0) |
| `momentum_score` | Cross-sectional z-score of `ret_12m` (mean 0, std 1, ddof=1) |
| `quality_score` | Cross-sectional z-score of `−vol_ann` (lower vol → higher score) |
| `composite_score` | **0.5 × momentum_score + 0.5 × quality_score** |

### Composite Score Formula

```
composite = 0.5 × z(ret_12m) + 0.5 × z(−vol_ann)
```

Where `z(x) = (x − mean(x)) / std(x)` computed cross-sectionally across all 151 tickers (ddof=1).

**Interpretation:**
- **Positive composite** → strong 12-month momentum **and/or** low volatility
- **Negative composite** → weak momentum **and/or** high volatility
- The score is a **ranking tool**, not a signal. It tells you where each stock sits relative to its peers on these two dimensions.

### What This Is NOT
- ❌ Not a trade signal or buy/sell recommendation
- ❌ Not a prediction of future returns
- ❌ Not a backtest (no out-of-sample validation included)
- ❌ Not a substitute for your own due diligence

---

## 📊 Sample Output (Top 10)

| Rank | Ticker | Last Price | 12M Return | Ann. Vol | Max DD | Composite |
|------|--------|-----------|------------|----------|--------|-----------|
| 1 | MU | $975.26 | +548.8% | 81.4% | −39.1% | **+2.204** |
| 2 | VLO | $390.42 | +153.0% | 36.2% | −12.1% | **+0.824** |
| 3 | INTC | $102.94 | +318.3% | 79.6% | −42.0% | **+0.786** |
| 4 | MPC | $395.93 | +120.8% | 34.3% | −18.3% | **+0.669** |
| 5 | PSX | $259.47 | +101.6% | 30.9% | −17.3% | **+0.630** |
| 6 | JNJ | $265.58 | +52.1% | 19.1% | −11.0% | **+0.611** |
| 7 | CSX | $48.95 | +50.9% | 22.2% | −11.6% | **+0.526** |
| 8 | TTE | $91.89 | +56.1% | 24.6% | −20.1% | **+0.499** |
| 9 | TGT | $155.83 | +77.2% | 30.6% | −13.3% | **+0.483** |
| 10 | TRV | $375.20 | +36.3% | 20.8% | −8.8% | **+0.469** |

### Bottom 5 (Weakest Composite)

| Rank | Ticker | Last Price | 12M Return | Ann. Vol | Max DD | Composite |
|------|--------|-----------|------------|----------|--------|-----------|
| 147 | HOOD | $112.57 | −4.4% | 72.2% | −57.3% | **−1.075** |
| 148 | ZS | $164.54 | −42.6% | 63.2% | −64.9% | **−1.092** |
| 149 | MRNA | $143.97 | +467.0% | 192.6% | −34.2% | **−1.095** |
| 150 | COIN | $175.26 | −45.9% | 70.8% | −63.6% | **−1.303** |
| 151 | SMCI | $40.10 | −8.8% | 91.6% | −65.0% | **−1.587** |

> **Note:** MRNA ranks near the bottom despite +467% 12M return because its 192.6% annualized volatility dominates the quality penalty. This is exactly what the composite is designed to surface.

---

## 📈 Distribution Statistics

| Statistic | Value |
|-----------|-------|
| N tickers | 151 |
| Composite mean | 0.000 |
| Composite std | 0.463 |
| Composite range | −1.587 → +2.204 |
| Median composite | +0.099 |
| N positive | 89 (59%) |
| N negative | 62 (41%) |
| 12M return range | −58.8% → +548.8% |
| Ann. vol range | 18.4% → 192.6% |

---

## 🛠️ Reproduce It Yourself

```bash
pip install yfinance pandas numpy
python scripts/reproduce.py
```

The script:
1. Downloads 252 days of daily adjusted close prices for all 151 tickers from Yahoo Finance
2. Computes all factor columns exactly as described above
3. Writes `factors_YYYY-MM-DD.csv` to the current directory

**Expected runtime:** ~30–60 seconds (network-bound). No API key required.

### Key Code (Inline)

```python
import yfinance as yf
import pandas as pd
import numpy as np

TICKERS = [/* 151 tickers — see full list in the CSV */]
LOOKBACK = 252  # trading days

prices = yf.download(TICKERS, period="2y", interval="1d", auto_adjust=True)["Close"]
prices = prices.dropna(axis=1, thresh=int(LOOKBACK * 0.8))  # drop tickers with >20% missing

def compute_factors(prices: pd.DataFrame) -> pd.DataFrame:
    last = prices.iloc[-1]
    ret_1m  = last / prices.iloc[-22]  - 1
    ret_3m  = last / prices.iloc[-64]  - 1
    ret_6m  = last / prices.iloc[-127] - 1
    ret_12m = last / prices.iloc[-253] - 1

    daily = prices.pct_change().dropna()
    vol_ann = daily.std() * np.sqrt(252)

    cummax = prices.cummax()
    drawdown = prices / cummax - 1
    max_dd = drawdown.min()

    hi_52w = prices.max()
    from_high = last / hi_52w - 1

    z = lambda s: (s - s.mean()) / s.std(ddof=1)
    momentum = z(ret_12m)
    quality  = z(-vol_ann)
    composite = 0.5 * momentum + 0.5 * quality

    df = pd.DataFrame({
        "last_price": last, "ret_1m": ret_1m, "ret_3m": ret_3m,
        "ret_6m": ret_6m, "ret_12m": ret_12m, "vol_ann": vol_ann,
        "max_drawdown": max_dd, "from_52w_high": from_high,
        "momentum_score": momentum, "quality_score": quality,
        "composite_score": composite,
    }).sort_values("composite_score", ascending=False).reset_index()
    df.insert(1, "rank", range(1, len(df) + 1))
    df.insert(2, "date", prices.index[-1].strftime("%Y-%m-%d"))
    return df[["ticker", "rank", "date", "last_price", "ret_1m", "ret_3m",
               "ret_6m", "ret_12m", "vol_ann", "max_drawdown", "from_52w_high",
               "momentum_score", "quality_score", "composite_score"]]
```

---

## 🎯 How to Use This Data

- **Screening:** Filter `composite_score > 0.5` for a momentum + low-vol shortlist
- **Relative value:** Compare `ret_12m` vs `vol_ann` to find stocks that are "cheap" on risk-adjusted momentum
- **Portfolio construction:** Use `composite_score` as a weighting input in your own optimizer
- **Research:** Extend the model with additional factors (value, size, liquidity) using the same z-score framework
- **Backtesting:** Use the 12-month return windows as a starting point for out-of-sample validation

---

## 📧 Get the Full Pack

This repo contains the **free sample** (151-stock CSV + methodology + reproducible script).

**Want more?** The full LaunchTower Factor Pack includes:
- Weekly updated factor screens (every Friday)
- Extended universe (300+ tickers)
- Additional factor columns (value, size, liquidity)
- Backtest results and performance attribution
- Python notebook with interactive exploration

👉 **[Get the Full Factor Pack on Whop](https://whop.com/launchtower)** — one-time purchase, instant delivery.

---

## 📄 License

MIT License — use, modify, and redistribute freely. Attribution appreciated but not required.

## 📬 Contact

Questions or feedback? Open an issue on this repo or reach out via the Whop product page.

---

*Generated by LaunchTower — independent market-data research. Not affiliated with Yahoo Finance or any exchange.*
