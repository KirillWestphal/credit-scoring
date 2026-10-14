"""Build docs/columns.md: a readable reference of all dataset columns.

For every column of the Parquet file it shows type, share of missing values,
approximate number of distinct values, min/max and the description from the
Lending Club data dictionary.

Stats are computed over all years: this is a technical overview and says
nothing about the relationship with default.

Run from anywhere:
    .venv/bin/python scripts/build_columns_md.py
"""

from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PARQUET_PATH = ROOT / "data" / "accepted_2007_to_2018Q4.parquet"
DICT_PATH = ROOT / "docs" / "LCDataDictionary.xlsx"
OUT_PATH = ROOT / "docs" / "columns.md"

# Same rule as in decisions.md (2026-10-12): service rows have a non-numeric id
LOANS_ONLY = "TRY_CAST(id AS BIGINT) IS NOT NULL"

# Columns named differently in the data and in the dictionary: data name -> dictionary name
ALIASES = {"verification_status_joint": "verified_status_joint"}


def load_stats(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    """Return one row of summary stats per column (DuckDB SUMMARIZE)."""
    return con.sql(f"SUMMARIZE SELECT * FROM '{PARQUET_PATH}' WHERE {LOANS_ONLY}").df()


def load_descriptions() -> dict[str, str]:
    """Return {column name: description} from the LoanStats sheet of the dictionary."""
    sheet = pd.read_excel(DICT_PATH, sheet_name="LoanStats").dropna(subset=["LoanStatNew"])
    names = sheet["LoanStatNew"].astype(str).str.strip().str.lower()
    descriptions = dict(zip(names, sheet["Description"].astype(str).str.strip()))
    for data_name, dict_name in ALIASES.items():
        descriptions[data_name] = descriptions[dict_name] + f" *(в словаре: `{dict_name}`)*"
    return descriptions


def md_safe(value, max_len: int | None = None) -> str:
    """Make a value safe for a Markdown table cell, optionally truncating it."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    text = str(value).replace("|", "/").replace("\n", " ")
    if max_len and len(text) > max_len:
        text = text[: max_len - 1] + "…"
    return text


def table_row(i: int, stat: pd.Series, description: str | None) -> str:
    """Format one column as a Markdown table row."""
    value_range = "" if stat["null_percentage"] == 100 else (
        f"{md_safe(stat['min'], 25)} … {md_safe(stat['max'], 25)}"
    )
    return (
        f"| {i} | `{stat['column_name']}` | {stat['column_type']} "
        f"| {float(stat['null_percentage']):.1f} | {int(stat['approx_unique']):,} "
        f"| {value_range} | {md_safe(description) if description else '— нет в словаре —'} |"
    )


def build_markdown(n_loans: int, rows: list[str], missing: list[str]) -> str:
    """Assemble the full document: header, table and list of undocumented columns."""
    header = f"""# Справочник колонок

Колонки `data/accepted_2007_to_2018Q4.parquet` в порядке файла, всего: {len(rows)}.

- **Описание** — из `docs/LCDataDictionary.xlsx`, лист `LoanStats`.
- **Статистика** — по всем {n_loans:,} займам (без 33 служебных строк), все годы. Это технический обзор: о связи с дефолтом здесь ничего нет.
- **Пропуски, %** — доля пустых значений. **Разных ≈** — приблизительное число различных значений (DuckDB `approx_unique`, погрешность в несколько процентов: у `id` оно больше числа займов, хотя все id уникальны). **Диапазон** — минимум … максимум; для текста это алфавитный порядок, а не смысловой.

Файл сгенерирован скриптом `scripts/build_columns_md.py` — не править вручную. Как читать: Cmd + Shift + V — предпросмотр, Cmd + F — поиск по именам и описаниям.

| # | Колонка | Тип | Пропуски, % | Разных ≈ | Диапазон | Описание |
|---|---|---|---|---|---|---|
"""
    footer = ""
    if missing:
        footer = (
            "\n## Колонки без описания в словаре\n\n"
            "Имя в данных не совпало с именем в словаре — добавить в `ALIASES` в скрипте:\n\n"
            + "\n".join(f"- `{name}`" for name in missing)
            + "\n"
        )
    return header + "\n".join(rows) + "\n" + footer


def main() -> None:
    con = duckdb.connect()
    con.sql("SET memory_limit = '3GB'")  # laptop has 8 GB RAM

    stats = load_stats(con)
    descriptions = load_descriptions()
    n_loans = con.sql(f"SELECT count(*) FROM '{PARQUET_PATH}' WHERE {LOANS_ONLY}").fetchone()[0]

    rows, missing = [], []
    for i, stat in stats.reset_index(drop=True).iterrows():
        description = descriptions.get(stat["column_name"].lower())
        if description is None:
            missing.append(stat["column_name"])
        rows.append(table_row(i, stat, description))

    OUT_PATH.write_text(build_markdown(n_loans, rows, missing), encoding="utf-8")
    print(f"{OUT_PATH.relative_to(ROOT)}: {len(rows)} columns, {len(missing)} without description")


if __name__ == "__main__":
    main()
