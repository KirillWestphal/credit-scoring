# Decisions

Decisions that affect results, with reasoning. Format:

```
## YYYY-MM-DD — short title
Decision: ...
Why: ...
Alternatives: ...
```

## 2026-10-12 — Service rows in raw CSV
Decision: Keep the 33 non-loan rows (quarterly totals and a section header) in the raw Parquet copy; drop them in the cleaning step by `TRY_CAST(id AS BIGINT) IS NULL`.
Why: The raw Parquet stays an exact copy of the CSV; all filtering lives in code where it is visible and testable.
Alternatives: Drop them during CSV → Parquet conversion (simpler, but the raw copy would no longer match the source).
