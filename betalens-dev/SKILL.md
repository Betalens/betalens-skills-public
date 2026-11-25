---
name: betalens-dev
description: Develop with the Betalens Python research framework, including factor analysis, backtesting, reporting, event studies, and parameter mining.
---

# Betalens Development

Use this skill for work in a Betalens checkout or when answering questions about its Python API. For factor-family implementation from reports or formulas, use `factor-forge` when available.

## Working Rules

- Identify the target repository from the task and verify its root with `git rev-parse --show-toplevel`. Check its current branch and worktree before editing; preserve unrelated user changes.
- Read the target checkout's documentation and source before relying on an API signature. The checkout is authoritative when this skill and the code disagree.
- Keep database assumptions explicit. Research APIs and the tables available in a user's database may have different contracts; do not infer schema compatibility from a successful connection or table creation.
- Keep credentials, private configuration, machine paths, local data, and research outputs outside source files and generated examples. Use the repository's supported external configuration mechanism without printing secret values.
- Prefer focused tests for the behavior changed. Do not run data-intensive research or connect to a live database unless the task calls for it.

## Core API Notes

- Factor grouping uses `single_characteristic`, `double_characteristic`, and `multi_characteristic`.
- `get_tradable_pool` and `pre_query_characteristic_data` prepare the cross-sectional research data. Verify the target data source and metric names before using them.
- A factor weight matrix uses rebalance timestamps as its index and security identifiers as columns. Include a `cash` column when the portfolio may hold cash.
- `BacktestBase` executes target weights against market data. Integer-lot execution can make actual holdings differ from target weights; use `actual_weight` and position outputs when diagnosing results.
- `Analyst.from_backtest(...)` is the preferred entry point for analysis and report export.
- YAML-driven factor workflows and parameter mining are documented in the linked references. Do not revive retired JSON or Streamlit workflows without finding them in the target checkout.

## References

- Read [factor.md](references/factor.md) for data preparation and factor grouping.
- Read [backtest.md](references/backtest.md) for portfolio weights and execution diagnostics.
- Read [analyst.md](references/analyst.md) for result analysis and reports.
- Read [eventstudy.md](references/eventstudy.md) for event-study workflows.
- Read [robust.md](references/robust.md) for incremental factor tests.
- Read [mining.md](references/mining.md) when creating or changing mining configurations.
