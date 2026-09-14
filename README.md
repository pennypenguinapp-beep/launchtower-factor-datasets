# LaunchTower — Factor Screen & Research Reports

**LaunchTower** is an independent, self-funded market-data desk. We run a
transparent, reproducible momentum + quality factor screen on a universe of
~95 liquid US mega-cap equities, and publish the full factor table, the
research report, and the exact code used to generate it — so anyone can
verify, reproduce, or build on our work.

> **Disclaimer:** This is a research screen built from public market data.
> It is **not** personalized investment advice and is not a recommendation
> to buy or sell any security. Past momentum does not guarantee future
> returns. Run at your own risk.

---

## Get the Full Model Pack

Want the complete, reproducible model — the full 95-ticker factor table,
the dated research report, the exact Python code, and the methodology
documentation — in one place?

**[→ Get the LaunchTower Full Model Pack ($49)](https://buy.stripe.com/test_bJeaEWgLd8o7etq7zr7AK3C)**

What's included:
- The complete 95-ticker factor score dataset (CSV) from the 2026-09-15 screen
- The full dated research report with top/bottom 10 analysis and interpretation
- The self-contained Python script that reproduces the entire screen end-to-end
- Methodology documentation: component definitions, weights, z-scoring, and data sources
- CSV schema reference for every column

One-time purchase. No subscription. No lock-in. Run it, verify it, build on it.

---

## What's in this repository

| Path | Description |
|---|---|
| `launchtower_factor_screen_v2.py` | The complete, self-contained factor screen (v2, 2026-09-15). Runs end-to-end: downloads data, computes factors, prints top/bottom 10, writes a dated CSV. |
| `reports/2026-09-15.md` | Latest research report (dated 2026-09-15, data as of 2026-09-11 close). |
| `data/factor_scores_2026-09-15.csv` | Full 95-ticker factor table from the 2026-09-15 screen. |

---

## Methodology (v2, 2026-09-15)

The composite score is a z-scored blend of four components, computed over a
trailing 12-month (252 trading day) window:

| Component | Weight | Definition |
|---|---|---|
| **Momentum (12-1)** | 50% | Return from `t-252` to `t-22` (skips the last month to avoid short-term reversal) |
| **Quality (Sharpe)** | 30% | Annualized mean daily return / annualized daily vol, trailing 252 days (gross Sharpe, rf = 0) |
| **Low Volatility** | 10% | Inverse z-score of annualized realized vol, trailing 252 days |
| **Low Drawdown** | 10% | Inverse z-score of max drawdown from peak, trailing 252 days |

All components are z-scored across the universe before weighting. A higher
composite score indicates stronger momentum and better risk-adjusted
performance.

**Data source:** Yahoo Finance (via `yfinance`), auto-adjusted (split and
dividend adjusted) daily closes, trailing ~3 years.

**Universe:** 96 liquid US mega-cap names across tech, semis, industrials,
energy, and consumer. Names with fewer than 252 trading days of history are
dropped automatically (OTIV is the known exclusion).

---

## Quick start

```bash
# 1. Install dependencies
pip install yfinance pandas numpy

# 2. Run the screen
python launchtower_factor_screen_v2.py
```

The script will:
1. Download ~3 years of adjusted daily closes for the full universe.
2. Compute the four components per ticker over the trailing 252-day window.
3. Z-score each component cross-sectionally.
4. Build the composite score and rank the universe.
5. Print the top 10 and bottom 10 tickers.
6. Write a dated CSV (`factor_scores_YYYY-MM-DD.csv`) to the current directory.

---

## Latest results (2026-09-15)

**Top 10 — Strongest Momentum + Quality**

| Rank | Ticker | Name | 12M Ret | 12-1 Mom | Sharpe | MaxDD 1Y | Score |
|---|---|---|---|---|---|---|---|
| 1 | MU | Micron | +548.8% | +506.2% | 2.71 | -39.1% | **+2.512** |
| 2 | LITE | Lumentum | +462.2% | +465.5% | 2.27 | -42.8% | **+2.160** |
| 3 | WDC | Western Digital | +365.9% | +373.0% | 2.33 | -41.8% | **+1.837** |
| 4 | STX | Seagate | +325.3% | +349.9% | 2.31 | -31.8% | **+1.698** |
| 5 | INTC | Intel | +318.3% | +310.2% | 2.19 | -41.9% | **+1.526** |
| 6 | AMAT | Applied Materials | +169.8% | +223.6% | 1.97 | -39.6% | **+1.166** |
| 7 | TER | Teradyne | +229.2% | +249.0% | 1.95 | -34.0% | **+1.160** |
| 8 | MRVL | Marvell | +255.3% | +226.7% | 2.00 | -48.4% | **+1.142** |
| 9 | COHR | Coherent | +195.0% | +243.6% | 1.71 | -48.0% | **+1.114** |
| 10 | AMD | AMD | +231.6% | +210.2% | 2.03 | -27.8% | **+0.992** |

**Bottom 10 — Weakest Momentum + Quality**

| Rank | Ticker | Name | 12M Ret | 12-1 Mom | Sharpe | MaxDD 1Y | Score |
|---|---|---|---|---|---|---|---|
| 86 | GRAB | Grab | -44.9% | -34.7% | -1.36 | -53.3% | **-0.667** |
| 87 | INTU | Intuit | -50.8% | -48.8% | -1.21 | -63.4% | **-0.681** |
| 88 | HUBS | HubSpot | -54.6% | -57.7% | -0.72 | -67.4% | **-0.688** |
| 89 | MSTR | MicroStrategy | -59.8% | -70.9% | -0.75 | -77.1% | **-0.734** |
| 90 | NKE | Nike | -48.9% | -44.3% | -1.67 | -49.3% | **-0.803** |
| 91 | RBLX | Roblox | -65.8% | -73.3% | -1.25 | -74.9% | **-0.823** |
| 92 | SMR | NuScale | -75.5% | -72.7% | -0.86 | -85.8% | **-0.831** |
| 93 | TTD | Trade Desk | -68.3% | -70.2% | -1.76 | -75.9% | **-0.883** |
| 94 | TME | Tencent Music | -68.0% | -66.1% | -2.19 | -69.3% | **-0.968** |
| 95 | MNSO | Mens Sana | -63.3% | -51.8% | -2.58 | -63.3% | **-0.990** |

**Interpretation:** The top of the table is dominated by the **memory /
storage / optical complex** — Micron, Lumentum, Western Digital, Seagate,
Intel, Teradyne, Marvell, and Coherent. This is a meaningful rotation from
the prior screen (2026-09-14), where the top was led by semiconductor
*equipment* (AMAT, LRCX, KLAC) and energy (MPC). The new leaders are the
*components* of the AI data-center buildout: HBM memory (MU), optical
transceivers (LITE, COHR), and nearline storage (WDC, STX).

The bottom of the table is led by **consumer software, gaming, and
China-exposed names** that have underperformed over the trailing 12 months.
All 10 carry negative 12-month returns and negative Sharpe ratios.

---

## CSV schema

`data/factor_scores_2026-09-15.csv` contains one row per ticker with the
following columns:

| Column | Description |
|---|---|
| `rank` | Rank by composite score (1 = strongest) |
| `ticker` | Ticker symbol |
| `price` | Last adjusted close (USD) |
| `ret_12m` | 12-month total return (decimal) |
| `mom_12_1` | 12-1 momentum (decimal) |
| `vol_12m` | Annualized realized volatility (decimal) |
| `sharpe` | Annualized gross Sharpe ratio |
| `maxdd_12m` | Maximum drawdown from peak (negative decimal) |
| `momentum_z` | Z-score of `mom_12_1` across the universe |
| `sharpe_z` | Z-score of `sharpe` across the universe |
| `lowvol_z` | Z-score of `-vol_12m` across the universe |
| `lowdd_z` | Z-score of `-maxdd_12m` across the universe |
| `composite` | Final composite score (higher = stronger) |

---

## Reproducibility

The screen is fully deterministic given the same input data. To reproduce
the 2026-09-15 report:

1. Run `python launchtower_factor_screen_v2.py` on or after 2026-09-15.
2. The output CSV will contain the same 95 tickers with the same factor
   values (prices may differ slightly if Yahoo Finance revises history).
3. The top/bottom 10 tables in `reports/2026-09-15.md` are generated from
   the same composite score.

**Note:** Yahoo Finance data is point-in-time and subject to revision.
Minor differences in the last few days of history are normal.

---

## Update cadence

The screen is re-run **monthly** (first trading day of each month). Each
run produces:
- A new dated CSV in `data/`
- A new dated report in `reports/`
- The same code, same weights, same universe — so results are directly
  comparable across months.

---

## License

MIT — see [LICENSE](LICENSE).

## Contact

LaunchTower is an independent research desk. For questions, corrections, or
data requests, open an issue on this repository.
