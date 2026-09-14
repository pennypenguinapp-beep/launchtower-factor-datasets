#!/usr/bin/env python3
"""
LaunchTower — Momentum + Quality factor model (reproducible).

Pulls REAL, free, public daily price data from Yahoo Finance (yfinance) for a
68 large-cap US equity universe, computes a transparent momentum + quality
composite score, and writes a dated CSV.

No paid data. No look-ahead bias (every factor uses only trailing data).
Not financial advice.

Usage:
    pip install -r requirements.txt
    python launchtower_model.py
    # -> writes factors_<YYYY-MM-DD>.csv
"""
import warnings
warnings.filterwarnings("ignore")

import datetime as dt
import numpy as np
import pandas as pd
import yfinance as yf

TICKERS = [
    "AAPL","MSFT","NVDA","GOOGL","AMZN","META","AVGO","TSLA","JPM","V",
    "XOM","JNJ","PG","COST","WMT","HD","UNH","LLY","MRK","ABT",
    "CAT","DE","HON","GE","UPS","MA","CSCO","ORCL","CRM","ADBE",
    "INTC","AMD","QCOM","TXN","AMGN","PFE","BMY","ABBV","NKE","MCD",
    "SBUX","DIS","NFLX","PYPL","UBER","ABNB","SHOP","SNOW","PLTR","COIN",
    "MSTR","HOOD","SMCI","ARM","CRWD","DDOG","NET","ZS","PANW","FTNT",
    "ANET","DELL","HPQ","IBM","ACN","T","VZ","TMUS",
]

# Factor weights (sum to 1.0). Inverted factors reward lower risk.
WEIGHTS = {
    "ret_6m": 0.35,          # 6-month momentum
    "ret_3m": 0.20,          # 3-month momentum
    "ann_vol": 0.20,         # annualized volatility (inverted)
    "max_dd_6m": 0.15,       # max drawdown 6M (inverted)
    "skew_6m": 0.10,         # return skewness 6M
}
INVERTED = {"ann_vol", "max_dd_6m"}


def fetch_close(tickers):
    close = yf.download(
        tickers, period="1y", interval="1d",
        auto_adjust=True, progress=False,
    )["Close"].dropna(axis=1, how="any")
    return close


def compute_factors(close):
    rows = []
    for t in close.columns:
        s = close[t]
        if len(s) < 130:
            continue
        r1 = s.iloc[-1] / s.iloc[-21] - 1
        r3 = s.iloc[-1] / s.iloc[-64] - 1
        r6 = s.iloc[-1] / s.iloc[-127] - 1
        r12 = s.iloc[-1] / s.iloc[0] - 1
        rets = s.pct_change().dropna()
        vol = rets.iloc[-126:].std() * np.sqrt(252)
        win = s.iloc[-127:]
        dd = (win / win.cummax() - 1).min()
        skew = rets.iloc[-126:].skew()
        rows.append(dict(
            ticker=t, close=s.iloc[-1],
            ret_1m=r1, ret_3m=r3, ret_6m=r6, ret_12m=r12,
            ann_vol=vol, max_dd_6m=dd, skew_6m=skew,
            data_points=len(s),
            start_date=str(s.index[0].date()),
            end_date=str(s.index[-1].date()),
        ))
    return pd.DataFrame(rows)


def composite_score(df):
    def pct(x, invert=False):
        r = x.rank(pct=True) * 100
        return (100 - r) if invert else r
    score = pd.Series(0.0, index=df.index)
    for f, w in WEIGHTS.items():
        score = score + pct(df[f], invert=f in INVERTED) * w
    return score.round(1)


def main():
    close = fetch_close(TICKERS)
    df = compute_factors(close)
    df["composite_score"] = composite_score(df)
    df = df.sort_values("composite_score", ascending=False).reset_index(drop=True)
    df.insert(0, "rank", df.index + 1)
    out = f"factors_{dt.date.today().isoformat()}.csv"
    df.to_csv(out, index=False)
    print(f"Wrote {out} — {len(df)} tickers, {len(df.columns)} columns")
    print(df[["rank", "ticker", "ret_6m", "ret_12m", "ann_vol", "composite_score"]].head(10).to_string(index=False))
    print("\nBottom 5:")
    print(df[["rank", "ticker", "ret_6m", "ret_12m", "composite_score"]].tail(5).to_string(index=False))


if __name__ == "__main__":
    main()
