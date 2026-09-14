# LaunchTower Factor Model Report — 2026-09-16

**Universe:** 151 US large-caps  
**Data Source:** Yahoo Finance (yfinance)  
**Date Range:** 2024-09-16 to 2026-09-15 (252 trading days)  
**Methodology:** Momentum + Quality composite factor model  
**Generated:** 2026-09-16 (live data pull)

---

## Executive Summary

This report presents the results of a reproducible momentum + quality factor screen across 151 US large-cap stocks. The model ranks stocks by a composite score that balances 12-month momentum (50%) against quality, defined as low annualized volatility (50%).

**Key Findings:**
- **MU (Micron)** leads with a composite score of +2.20, driven by exceptional 12-month momentum (+548.8%) despite high volatility (81.4%)
- **VLO (Valero)** and **MPC (Marathon Petroleum)** rank #2 and #4, combining strong momentum with low volatility
- **SMCI (Super Micro Computer)** ranks last (-1.59) with weak momentum and extreme volatility (91.6%)
- **MRNA (Moderna)** is an outlier: massive 12-month momentum (+467.0%) but extreme volatility (192.6%) pushes it to rank #149

---

## Methodology

### Factors Computed

1. **12-Month Momentum:** Return from 252 trading days ago to today
2. **6-Month Momentum:** Return from 126 trading days ago to today
3. **3-Month Momentum:** Return from 63 trading days ago to today
4. **1-Month Momentum:** Return from 21 trading days ago to today
5. **Volatility:** 252-day annualized standard deviation of daily returns
6. **Max Drawdown:** Maximum peak-to-trough decline over the 252-day window
7. **52-Week High Distance:** Current price relative to 252-day high

### Composite Score

**Composite = 50% Momentum (z-score) + 50% Quality (z-score)**

Where:
- **Momentum** = z-score of 12-month return
- **Quality** = negative z-score of annualized volatility (lower vol = higher quality)

**Interpretation:** Higher composite scores indicate stocks with strong momentum and lower volatility (higher quality). Lower scores indicate weak momentum and/or high volatility.

---

## Top 10 Stocks by Composite Score (2026-09-16)

| Rank | Ticker | 12M Return | 6M Return | 3M Return | 1M Return | Volatility | Max DD | From 52W High | Composite |
|------|--------|------------|-----------|-----------|-----------|------------|--------|---------------|-----------|
| 1 | MU | +548.8% | +140.7% | -2.1% | +7.0% | 81.4% | -39.1% | -19.6% | **+2.20** |
| 2 | VLO | +153.0% | +67.0% | +53.3% | +18.2% | 36.2% | -12.1% | 0.0% | **+0.82** |
| 3 | INTC | +318.3% | +127.5% | -12.0% | +2.0% | 79.6% | -41.9% | -27.0% | **+0.79** |
| 4 | MPC | +120.8% | +73.2% | +52.2% | +14.0% | 34.3% | -18.3% | -0.9% | **+0.67** |
| 5 | PSX | +101.6% | +50.9% | +46.5% | +15.6% | 30.9% | -17.3% | -0.5% | **+0.63** |
| 6 | JNJ | +52.1% | +11.0% | +12.0% | +2.3% | 19.1% | -11.0% | -4.6% | **+0.61** |
| 7 | CSX | +50.9% | +25.5% | +3.6% | -2.0% | 22.2% | -11.6% | -7.8% | **+0.53** |
| 8 | TTE | +56.1% | +14.1% | +4.8% | +4.8% | 24.6% | -20.1% | -1.8% | **+0.50** |
| 9 | TGT | +77.2% | +36.9% | +18.4% | +1.2% | 30.6% | -13.3% | -8.3% | **+0.48** |
| 10 | TRV | +36.3% | +25.2% | +23.9% | +1.7% | 20.8% | -8.8% | -5.2% | **+0.47** |

**Key Observations:**
- **MU (Micron)** leads with exceptional 12-month momentum (+548.8%) despite high volatility
- **VLO (Valero)** and **MPC (Marathon Petroleum)** combine strong momentum with low volatility
- **JNJ (Johnson & Johnson)** and **TTE (TotalEnergies)** show balanced momentum and quality
- **TRV (Travelers)** ranks #10 with moderate momentum and low volatility

---

## Bottom 10 Stocks by Composite Score (2026-09-16)

| Rank | Ticker | 12M Return | 6M Return | 3M Return | 1M Return | Volatility | Max DD | From 52W High | Composite |
|------|--------|------------|-----------|-----------|-----------|------------|--------|---------------|-----------|
| 151 | SMCI | -8.8% | +29.8% | +25.4% | +6.6% | 91.6% | -65.0% | -31.7% | **-1.59** |
| 150 | COIN | -45.9% | -9.3% | +9.2% | +17.6% | 70.8% | -63.6% | -54.7% | **-1.30** |
| 149 | MRNA | +467.0% | +169.7% | +190.0% | +126.1% | 192.6% | -34.2% | -17.4% | **-1.10** |
| 148 | ZS | -42.6% | +8.5% | +30.5% | -7.2% | 63.2% | -64.9% | -51.1% | **-1.09** |
| 147 | HOOD | -4.4% | +47.9% | +22.1% | +18.6% | 72.2% | -57.3% | -26.2% | **-1.07** |
| 146 | ORCL | -50.6% | -4.9% | -18.1% | -2.0% | 57.0% | -64.6% | -53.7% | **-0.99** |
| 145 | NOW | -29.4% | +17.3% | +28.6% | +6.1% | 56.9% | -56.8% | -31.1% | **-0.85** |
| 144 | SE | -45.9% | +24.8% | +24.0% | -17.1% | 50.8% | -60.2% | -45.9% | **-0.80** |
| 143 | INTU | -50.8% | -25.5% | +16.6% | -3.9% | 48.7% | -63.4% | -53.7% | **-0.78** |
| 142 | PLTR | +1.7% | +8.9% | +27.6% | -2.2% | 60.9% | -48.2% | -19.3% | **-0.75** |

**Key Observations:**
- **SMCI (Super Micro Computer)** ranks last with weak momentum and extreme volatility (91.6%)
- **COIN (Coinbase)** shows negative 12-month momentum and high volatility
- **MRNA (Moderna)** is an outlier: massive 12-month momentum (+467.0%) but extreme volatility (192.6%)
- **ZS (Zscaler)** and **HOOD (Robinhood)** show weak momentum and high volatility

---

## Factor Distribution

**Momentum (12M):**
- Mean: +32.9%
- Std Dev: 78.8%
- Range: -58.8% (BSX) to +548.8% (MU)

**Volatility:**
- Mean: 38.7%
- Std Dev: 20.0%
- Range: 18.4% (MCD) to 192.6% (MRNA)

**Composite Score:**
- Mean: 0.00 (by construction)
- Std Dev: 0.46
- Range: -1.59 (SMCI) to +2.20 (MU)

---

## Reproducibility

**Code:** See `launchtower_factor_screen_2026-09-16.py` in this repository.

**Dependencies:**
- Python 3.8+
- yfinance >= 0.2.40
- pandas >= 1.5.0
- numpy >= 1.23.0

**To Reproduce:**
```bash
pip install yfinance pandas numpy
python launchtower_factor_screen_2026-09-16.py
```

**Output:**
- `launchtower_signal_2026-09-16.csv` — Full factor table (151 tickers)
- Console output — Top 10 and Bottom 10 rankings

---

## Disclaimer

This report is for research and educational purposes only. It is NOT personalized investment advice and is not a recommendation to buy or sell any security. Past performance is not indicative of future results. All data is sourced from public market data providers and may contain errors or gaps. Run at your own risk.

**LaunchTower** — independent market-data desk.
