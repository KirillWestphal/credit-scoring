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

## 2026-10-14 — Loans that do not meet the credit policy
Decision: Keep the 2,438 36-month loans with status "Does not meet the credit policy. Status: ..." (issued 2007–2010). Map their outcome like regular statuses (Charged Off → 1, Fully Paid → 0) and add a flag `meets_policy` to test later whether it matters.
Why: These are real loans with known outcomes, issued under an older, looser policy. Dropping them would remove 58% of 2007 loans (352 of 603) and shrink the earliest history.
Alternatives: Drop them to train only on loans under the current policy (closer to the 2017+ stream, but less history).

## 2026-10-15 — Three-model comparison: history length vs bureau features
Decision: Train three models and test all on the same period, Jul–Dec 2013:
A (Jan 2007 – Jun 2013, base features), A′ (Oct 2012 – Jun 2013, base features),
B (Oct 2012 – Jun 2013, base + bureau features).
Why: Bureau columns appear in three waves (Mar–Sep 2012) and are complete only from Oct 2012.
A vs A′ isolates the effect of history length; A′ vs B isolates the effect of bureau features.
Alternatives: Single split 2007–2012 / 2013 as in the original plan (bureau features missing
for 80% of training loans); two models only (effects of history and features confounded).
