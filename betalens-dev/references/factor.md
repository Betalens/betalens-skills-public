# Factor Research

Use the function signatures from the checked-out Betalens version. The following names and shapes are useful orientation, not a substitute for current API docs.

```python
from betalens.factor.factor import (
    get_tradable_pool,
    pre_query_characteristic_data,
    single_characteristic,
    get_single_factor_weight,
)

date_ranges, code_ranges = get_tradable_pool(rebalance_dates)
data = pre_query_characteristic_data(
    rebalance_dates,
    metric,
    table_name=table_name,
    date_ranges=date_ranges,
    code_ranges=code_ranges,
)
labeled = single_characteristic(data, metric=metric, quantiles={metric: 10})
weights = get_single_factor_weight(
    labeled, {"factor_key": metric, "mode": "classic-long-short"}
)
weights["cash"] = 0
```

The labeled pool is indexed by rebalance time and security. Confirm the actual table, metric names, timestamp semantics, and availability of point-in-time constituents in the target data source. Do not treat a present-day classification or revised fundamental value as historically available without evidence.

For preprocessing, inspect `betalens.factor.preprocessing` and specify winsorization, standardization, industry, and market-cap inputs explicitly. Confirm the intended classification and effective-time semantics before claiming point-in-time neutrality.
