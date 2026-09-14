# LaunchTower Factor Datasets

Reproducible momentum + quality factor models on US large-caps.

## Latest Report: 2026-09-15

**Universe:** 151 US large-caps  
**Top 5:** APD, PBR, AVGO, NVDA, TRV  
**Bottom 5:** SNOW, CME, ETN, META, GILD

## Files

- `factor_scores_2026-09-15.csv` — Full factor scores (2026-09-15)
- `launchtower_factor_report_2026-09-15.md` — Detailed research report

## Methodology

1. **12-Month Momentum:** Return from 252 trading days ago to 21 trading days ago
2. **3-Month Momentum:** Return from 63 trading days ago to 21 trading days ago
3. **Volatility:** 252-day annualized standard deviation
4. **Quality Proxy:** Inverse of volatility
5. **Composite Score:** 50% momentum (z-score) + 50% quality (z-score)

## Reproducibility

```python
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# See full code in the report
```

## Disclaimer

For research and educational purposes only. NOT investment advice. Past performance does not guarantee future results.
