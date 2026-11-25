# Backtesting

`BacktestBase` consumes target weights and market data. Check its current constructor in the target checkout before choosing optional arguments.

```python
from betalens.backtest import BacktestBase

engine = BacktestBase(
    weight=weights,
    symbol="Demo",
    amount=1_000_000,
)
```

Weight rows are rebalance timestamps; columns are security identifiers. Include `cash` when the strategy can hold cash. A target portfolio may be adjusted for trade status, lot sizes, or available capital, so diagnose the executed portfolio with `engine.actual_weight`, `engine.position`, and `engine.rebalance_log`, not only the input weights.

Useful outputs commonly include `nav`, `actual_weight`, `daily_position_value`, `daily_pnl`, and `rebalance_log`. Verify the available attributes and trade-status behavior against the checked-out implementation. A backtest is only as sound as its price, calendar, universe, and data-availability assumptions.
