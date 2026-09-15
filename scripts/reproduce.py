#!/usr/bin/env python3
"""
LaunchTower — Momentum + Quality Factor Screen
Reproduces factors_2026-09-14.csv from public Yahoo Finance data.

Usage:
    pip install yfinance pandas numpy
    python reproduce.py

Output:
    factors_YYYY-MM-DD.csv  (151 rows × 14 columns)

Methodology:
    composite = 0.5 × z(ret_12m) + 0.5 × z(−vol_ann)
    where z() is cross-sectional z-score (ddof=1)

NOT investment advice. Research/educational only.
"""

import sys
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

try:
    import yfinance as yf
except ImportError:
    sys.exit("Missing dependency. Run: pip install yfinance")

# ── Universe: 151 US large/mid-caps ──────────────────────────────────────────
TICKERS = [
    # Tech / Semis
    "AAPL","MSFT","NVDA","GOOGL","AMZN","META","AVGO","TSLA","AMD","INTC",
    "QCOM","MU","TXN","MRVL","MCHP","ASML","KLAC","CDNS","SNPS","ADSK",
    "NOW","CRM","ADBE","ORCL","CSCO","ACN","INTU","TEAM","SNOW","NET",
    "SHOP","PYPL","SQ","COIN","HOOD","PLTR","CRWD","DDOG","OKTA","ZS",
    "APP","RBLX","RIVN","LCID","NIO","XPEV","BYDDY","PDD","BABA","JD",
    # Healthcare
    "LLY","UNH","JNJ","MRK","ABBV","PFE","BMY","AMGN","GILD","REGN",
    "NVO","TMO","DHR","ISRG","ABT","BSX","CVS","CI","HUM","ELV",
    "MRNA","ALGN","MNDY","EXC","ENPH","FSLR","SEDG","NEM","FCX","RIO",
    # Financials
    "JPM","BAC","WFC","C","GS","MS","BLK","SCHW","AXP","BRK-B",
    "V","MA","CME","ICE","MCO","AIG","MET","PRU","TRV","ALL",
    # Energy
    "XOM","CVX","COP","OXY","EOG","SLB","MPC","VLO","PSX","WMB",
    "KMI","ET","OKE","WEC","LNG","BP","SHEL","PBR","RIG","VAL",
    # Industrials / Materials
    "CAT","DE","GE","HON","MMM","UPS","FDX","UNP","CSX","NSC",
    "RTX","LMT","BA","NOC","GD","LHX","ROK","PH","EMR","ITW",
    "LIN","APD","SHW","ECL","DOW","PPG","ALB","NEM","CLF","SCCO",
    # Consumer
    "COST","WMT","PG","KO","PEP","MCD","NKE","SBUX","TGT","LOW",
    "HD","ORLY","TJX","LULU","GM","F","PHM","LEN","NVR","DHI",
    "STZ","SJM","KHC","MDLZ","CL","HRL","WELL","RST","CMG","YUM",
]

LOOKBACK = 252  # trading days


def compute_factors(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute all factor columns from a price DataFrame (rows=dates, cols=tickers)."""
    last = prices.iloc[-1]

    # Simple returns over fixed lookback windows
    ret_1m  = last / prices.iloc[-22]  - 1
    ret_3m  = last / prices.iloc[-64]  - 1
    ret_6m  = last / prices.iloc[-127] - 1
    ret_12m = last / prices.iloc[-253] - 1

    # Annualized volatility
    daily = prices.pct_change().dropna()
    vol_ann = daily.std() * np.sqrt(252)

    # Max drawdown over full window
    cummax = prices.cummax()
    drawdown = prices / cummax - 1
    max_dd = drawdown.min()

    # Distance from 52-week high
    hi_52w = prices.max()
    from_high = last / hi_52w - 1

    # Cross-sectional z-scores (ddof=1)
    z = lambda s: (s - s.mean()) / s.std(ddof=1)
    momentum  = z(ret_12m)
    quality   = z(-vol_ann)
    composite = 0.5 * momentum + 0.5 * quality

    df = pd.DataFrame({
        "ticker":          prices.columns,
        "last_price":      last.values,
        "ret_1m":          ret_1m.values,
        "ret_3m":          ret_3m.values,
        "ret_6m":          ret_6m.values,
        "ret_12m":         ret_12m.values,
        "vol_ann":         vol_ann.values,
        "max_drawdown":    max_dd.values,
        "from_52w_high":   from_high.values,
        "momentum_score":  momentum.values,
        "quality_score":   quality.values,
        "composite_score": composite.values,
    }).sort_values("composite_score", ascending=False).reset_index(drop=True)

    df.insert(1, "rank", range(1, len(df) + 1))
    df.insert(2, "date", prices.index[-1].strftime("%Y-%m-%d"))

    cols = ["ticker","rank","date","last_price","ret_1m","ret_3m","ret_6m",
            "ret_12m","vol_ann","max_drawdown","from_52w_high",
            "momentum_score","quality_score","composite_score"]
    return df[cols]


def main():
    print(f"Downloading {len(TICKERS)} tickers from Yahoo Finance…")
    prices = yf.download(
        TICKERS,
        period="2y",
        interval="1d",
        auto_adjust=True,
        progress=False,
    )["Close"]

    # Drop tickers with >20% missing data
    valid = prices.dropna(axis=1, thresh=int(LOOKBACK * 0.8))
    dropped = set(prices.columns) - set(valid.columns)
    if dropped:
        print(f"  Dropped {len(dropped)} tickers (insufficient data): {sorted(dropped)}")
    print(f"  Keeping {valid.shape[1]} tickers × {valid.shape[0]} days")

    df = compute_factors(valid)
    out = f"factors_{df['date'].iloc[0]}.csv"
    df.to_csv(out, index=False)
    print(f"\n✓ Wrote {out}  ({len(df)} rows × {len(df.columns)} cols)")
    print(f"\nTop 5:")
    print(df.head(5)[["ticker","last_price","ret_12m","vol_ann","composite_score"]].to_string(index=False))
    print(f"\nBottom 5:")
    print(df.tail(5)[["ticker","last_price","ret_12m","vol_ann","composite_score"]].to_string(index=False))


if __name__ == "__main__":
    main()
