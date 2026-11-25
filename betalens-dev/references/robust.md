# Robustness Tests

`betalens.robust` includes tests for whether candidate factors add information beyond existing factors. Consult the current implementation and its source paper before interpreting statistical results.

```python
from betalens.robust import RobustTest

test = RobustTest(fund=returns, factor=factor_panel)
orthogonal_factors, t_values = test.neu()
effective_factors, adjusted_p_values, null_distribution = test.bootstrap_once(
    n_bootstraps=500
)
```

Align observations by date, remove invalid observations according to a documented rule, and report the bootstrap count and significance threshold. Treat these tests as diagnostics; they do not remove selection bias from an undocumented research process.
