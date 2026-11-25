---
name: factor-forge
description: Build YAML-configured Betalens factor workflows from a research report or a family of related formulas.
---

# Factor Forge

Use this skill when the user wants to reproduce a factor family, turn a formula into a Betalens factor, or add parameterized factors to a compatible research repository. Aim for a reusable family implementation rather than generating unrelated one-off scripts.

## Workflow

1. Read the supplied report or prompt and extract the formula, economic hypothesis, direction, inputs, frequency, universe, preprocessing, rebalance schedule, and evaluation period. Keep claims from the source separate from assumptions.
2. Check the target repository's current factor examples, YAML schema, templates, and tests. Do not assume a local directory layout or reuse stale APIs from an earlier checkout.
3. Confirm data fields and metric names against the target data contract. Ask or inspect available metadata when a field cannot be mapped confidently; never invent a metric.
4. Group related formulas only when they share meaningful inputs, output shape, and pipeline. Reuse an existing class template where it fits; otherwise add only the shared operators and defaults that belong to the class.
5. Create a complete YAML configuration and a side-effect-free factor module for each runnable factor, following the repository's current contract.
6. Validate configuration and imports, then run focused tests. Execute database queries, backtests, or parameter searches only when the user requested that work and the required data source is available.

## Betalens Conventions

For the current YAML-based FactorPipeline contract, verify these requirements in the checked-out version:

- Keep factor metadata, `factor_spec`, weights, and run settings in the complete YAML configuration.
- Make compute function arguments match declared input keys and return the documented wide panel shape.
- Keep imports free of backtests, database queries, and file writes.
- Expose the repository-required spec/build/run entry points and delegate execution to its shared runner.
- Keep defaults in configuration rather than hidden in generated script logic.
- Store outputs under an explicit runtime/output directory outside versioned source unless the repository says otherwise.
- Do not generate retired JSON or Streamlit layouts unless the target repository explicitly still supports them.

When adding mining, read [the mining reference](../betalens-dev/references/mining.md) if both skills are installed, then verify hook names and YAML keys against the current implementation. Keep candidate budgets, windows, filters, seeds, and runtime constraints explicit.

## Research Integrity

- Preserve the report's formula and cite its source in factor metadata where permitted.
- State the factor direction and define whether returns are absolute or benchmark-relative.
- Avoid look-ahead: distinguish event date from data availability and use point-in-time universe/classification data where available.
- Do not include private reports, proprietary formulas, credentials, local paths, customer data, or unpublished factor results in generated examples or public artifacts.
- Do not claim a factor has been validated from a successful import or a single backtest; report the actual checks and limitations.

For PDF or DOCX report triage, the optional `scripts/read_report.py` helper extracts candidate paragraphs. It does not OCR scanned pages or determine whether a formula is valid.

## Delivery

Report the formula family, assumptions, changed configuration/script paths, validation performed, and any data or API limitations. Summarize backtest metrics only when a backtest was actually run.
