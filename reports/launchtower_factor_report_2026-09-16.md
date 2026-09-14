# LaunchTower Factor Model Report — 2026-09-16

**Universe:** 196 US large/mid-cap stocks (206 candidates; 10 excluded — no data or delisted: BRK.B, EXAS, K, SQ, MMC, EGT, UPF, and 3 with gaps)
**Data:** Yahoo Finance daily closes, 1-year window, auto-adjusted. Last bar: 2026-09-11.
**Model:** Composite score = 0.6 × momentum percentile + 0.4 × quality percentile
- Momentum = 0.25 × 1-month return + 0.75 × 6-month return
- Quality = 0.5 × (inverse annualized volatility) + 0.5 × (proximity to 52-week high)

This is a research screen, not investment advice. No position sizing, no risk model, no return promises.

## Top 10 (highest composite score)

| Rank | Ticker | Last | 1M | 3M | 6M | Ann. Vol | From High | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | MET | 97.14 | +0.5% | +11.6% | +43.2% | 22.6% | -2.8% | 0.909 |
| 2 | BAC | 62.69 | -2.8% | +14.2% | +34.4% | 19.3% | -2.8% | 0.888 |
| 3 | PSX | 259.47 | +15.6% | +46.5% | +50.9% | 32.2% | -0.5% | 0.865 |
| 4 | PRU | 119.24 | -1.7% | +13.2% | +32.4% | 21.7% | -3.6% | 0.865 |
| 5 | JPM | 356.23 | -2.5% | +14.1% | +27.1% | 20.8% | -2.5% | 0.852 |
| 6 | AAPL | 332.27 | +9.9% | +12.5% | +30.1% | 27.8% | -2.2% | 0.844 |
| 7 | ELV | 418.72 | +5.4% | +5.4% | +46.7% | 32.8% | -1.5% | 0.842 |
| 8 | MPC | 395.93 | +14.0% | +52.2% | +73.2% | 35.6% | -0.9% | 0.840 |
| 9 | MS | 214.38 | -1.5% | +1.4% | +40.4% | 27.6% | -5.7% | 0.828 |
| 10 | VLO | 390.42 | +18.2% | +53.3% | +67.0% | 37.1% | +0.0% | 0.827 |

## Bottom 5 (lowest composite score)

| Rank | Ticker | Last | 6M | From High | Score |
|---|---|---|---|---|---|
| 196 | RARE | 14.30 | -34.1% | -60.9% | 0.019 |
| 195 | TTD | 14.34 | -45.9% | -73.5% | 0.024 |
| 194 | TME | 7.98 | -40.1% | -68.9% | 0.046 |
| 193 | LULU | 98.97 | -37.4% | -54.2% | 0.054 |
| 192 | BSX | 42.98 | -37.3% | -59.1% | 0.065 |

## What the screen is saying

1. **Financials own the top of the board.** MET (#1), BAC (#2), PRU (#4), JPM (#5), and MS (#9) all combine 6-month momentum of +27% to +43% with the lowest volatility in the universe (~19–22% annualized). The quality leg of the model is doing heavy lifting here — these are the stocks that are both moving and stable.
2. **Energy refiners are still the momentum story.** PSX (#3), MPC (#8), and VLO (#10) carry 6-month returns of +51% to +73%, all within 1% of their 52-week highs. The refiner squeeze that started in mid-2026 is still the clearest sector signal in the dataset.
3. **AAPL cracks the top 6 for the first time in this series.** At #6 with +30% 6-month momentum and only 28% annualized volatility, the quality leg is what gets it in — the momentum leg alone would put it mid-pack.
4. **The laggard list is a different story than the leaders.** RARE, TTD, TME, LULU, and BSX are all 35–75% below their 52-week highs with negative 6-month momentum. TTD at the bottom is notable: a former quality compounder now scoring in the bottom decile on both legs.
5. **Breadth check:** 10 stocks at 52-week highs, 39 stocks more than 30% below theirs. 125 of 196 stocks have positive 6-month returns. The market is bifurcated — a narrow group of financials and refiners carrying the index while a broad set of former favorites de-rate.

## Reproducibility

- Data source: `yfinance` (Yahoo Finance), `period="1y"`, `interval="1d"`, `auto_adjust=True`
- Universe: 206 fixed tickers (see `factors_2026-09-16.csv` for the 196 that returned full data)
- Scoring: pure percentile ranks, no look-ahead, no fitted parameters
- Full dataset: `factors_2026-09-16.csv` (196 rows × 14 columns)

---
*LaunchTower is an independent research desk. This report is for informational purposes only and is not investment advice, an offer, or a recommendation to buy or sell any security. Past performance does not guarantee future results. Do your own research.*
