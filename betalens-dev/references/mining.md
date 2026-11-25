# Parameter Mining

Read the current mining guide and validate configuration keys against the checked-out Betalens version before running a search. The public API commonly begins with:

```python
from betalens.factor.mining import run_mining

result = run_mining("parameter_space.yaml", "performance.yaml")
```

Keep the search space, evaluation windows, selection filters, runtime controls, cache, and output settings explicit. A configuration field that sounds familiar may not be supported; do not invent `pruner` or early-stopping options without confirming them in source.

Separate fast candidate exploration from slower confirmation where the implementation supports distinct execution modes. Report requested and effective worker counts, memory limits, seeds, windows, filters, and the final selection rule. Validate YAML structure without connecting to a database before starting a costly run.
