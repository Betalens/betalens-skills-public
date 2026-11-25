# Performance Analysis

Prefer `Analyst.from_backtest` when a Betalens backtest object is available:

```python
from betalens.analyst import Analyst

analysis = Analyst.from_backtest(engine, benchmark=benchmark, name="Demo")
analysis.report(to_excel="report.xlsx", to_html="report.html")
```

The benchmark may be omitted when relative-performance metrics are not needed. Check the current method signature and optional dependencies before exporting.

Useful tables may include `summary_df()`, `top_holdings_df()`, `contribution_df()`, `trade_pnl_df()`, and `monthly_table()`. Holdings and attribution require the corresponding backtest outputs; missing inputs should be reported rather than inferred.
