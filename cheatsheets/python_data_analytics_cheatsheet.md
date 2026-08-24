# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny `pandas`.

---

# 1. Importy

```python
import pandas as pd
```

Další používané knihovny:

```python
import sqlite3
import requests
```

```text
pandas   → tabulková data
sqlite3  → SQLite databáze
requests → API / HTTP požadavky
```

---

# 2. Data Sources & Ingestion

## CSV

```python
df = pd.read_csv("data.csv")
```

Vlastní oddělovač:

```python
df = pd.read_csv(
    "data.csv",
    sep=";"
)
```

Encoding:

```python
df = pd.read_csv(
    "data.csv",
    encoding="cp1250"
)
```

Kombinace:

```python
df = pd.read_csv(
    "data.csv",
    sep=";",
    encoding="cp1250"
)
```

```text
sep=      → oddělovač sloupců
encoding= → způsob uložení znaků

UTF-8     → dnešní standard
cp1250    → starší Windows encoding pro střední Evropu
```

UTF-8 většinou není nutné zadávat explicitně.

TXT s tabulkovou strukturou lze načíst stejně:

```python
df = pd.read_csv(
    "data.txt",
    sep="\t"
)
```

---

## JSON

```python
df = pd.read_json("data.json")
```

```text
{ } → objekt
[ ] → pole / array

"key": value
→ dvojice klíč–hodnota
```

U jednoduchého JSON často:

```text
1 objekt → 1 záznam / řádek
1 klíč   → 1 sloupec
```

### Nested JSON

Pro zploštění vnořené struktury:

```python
df = pd.json_normalize(data)
```

Například:

```text
customer
├── name
└── city
```

se může změnit na:

```text
customer.name
customer.city
```

`json_normalize()` = flattening / zploštění.

---

## Excel

```python
df = pd.read_excel("data.xlsx")
```

Může být potřeba:

```text
pip install openpyxl
```

---

## XML

```python
df = pd.read_xml("data.xml")
```

XML používá tagy:

```xml
<product>Laptop</product>
```

---

## SQLite + SQL

```python
connection = sqlite3.connect(
    "database.db"
)
```

SQL dotaz:

```python
query = """
SELECT *
FROM orders
WHERE quantity > 2
"""
```

Načtení do DataFrame:

```python
df = pd.read_sql(
    query,
    connection
)
```

Ukončení spojení:

```python
connection.close()
```

```text
SQLite databáze
→ connection
→ SQL query
→ pd.read_sql()
→ DataFrame
```

Po načtení zůstává `df` v Pythonu i po `connection.close()`.

---

## API

GET request:

```python
response = requests.get(url)
```

Kontrola:

```python
response.status_code
```

```text
200 → OK
```

JSON odpověď:

```python
data = response.json()
```

Převod na DataFrame:

```python
df = pd.DataFrame(data)
```

U nested JSON:

```python
df = pd.json_normalize(data)
```

Workflow:

```text
API
→ requests.get()
→ response
→ response.json()
→ Python data
→ DataFrame
```

---

# 3. Raw data

Původní data je vhodné zachovat:

```python
df_raw = pd.read_csv("data.csv")

df = df_raw.copy()
```

```text
df_raw → původní načtená data
df     → pracovní kopie
```

Workflow:

```text
zdroj
→ ingestion
→ raw data
→ cleaning
→ validation
→ analysis
```

---

# 4. DataFrame a Series

```python
type(df)
# pandas.DataFrame

type(df["product"])
# pandas.Series
```

```text
DataFrame → celá tabulka
Series    → jeden sloupec
```

---

# 5. Základní kontrola datasetu

```python
df.head()
df.head(10)

df.info()

df.shape
df.columns
df.index
df.dtypes
```

```text
shape   → (počet řádků, počet sloupců)
columns → názvy sloupců
dtypes  → datové typy
```

Atributy:

```python
df.shape
df.columns
df.dtypes
```

Metody:

```python
df.head()
df.info()
```

---

# 6. Datové typy

```text
str      → text
int64    → celé číslo
float64  → desetinné číslo
bool     → True / False
datetime → datum a čas
```

Kontrola:

```python
df.dtypes
```

Převod:

```python
df["quantity"] = (
    df["quantity"].astype(int)
)
```

Datum:

```python
df["order_date"] = pd.to_datetime(
    df["order_date"]
)
```

---

# 7. Pandas index

```text
Pandas index
≠
business ID / primary key
```

Reset:

```python
df = df.reset_index(
    drop=True
)
```

---

# 8. Výběr sloupců

Jeden sloupec → `Series`:

```python
df["product"]
```

Více sloupců → `DataFrame`:

```python
df[
    ["product", "quantity", "total"]
]
```

---

# 9. Nový sloupec

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

---

# 10. Agregace

```python
df["total"].sum()
df["total"].mean()
df["total"].min()
df["total"].max()
df["total"].median()
df["product"].mode()
```

```text
sum()    → součet
mean()   → průměr
min()    → minimum
max()    → maximum
median() → medián
mode()   → modus
```

---

# 11. Boolean maska a filtrování

```python
df["total"] > 10000
```

vrací `True / False`.

Filtr:

```python
df[
    df["total"] > 10000
]
```

Masku lze uložit:

```python
mask = df["total"] > 10000

high_value_orders = df[mask]
```

Operátory:

```text
==  rovná se
!=  nerovná se
>   větší než
<   menší než
>=  větší nebo rovno
<=  menší nebo rovno
```

---

# 12. Více podmínek

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Každá podmínka do závorky:

```python
df[
    (df["category"] == "Furniture")
    & (df["total"] > 10000)
]
```

---

# 13. `isin()` a `between()`

```python
df[
    df["product"].isin([
        "Laptop",
        "Desk",
        "Monitor"
    ])
]
```

NOT IN:

```python
df[
    ~df["product"].isin([
        "Laptop",
        "Desk"
    ])
]
```

Interval:

```python
df[
    df["total"].between(
        10000,
        20000
    )
]
```

```text
inclusive="both"
inclusive="left"
inclusive="right"
inclusive="neither"
```

---

# 14. `loc` a `iloc`

## `loc`

Názvy a podmínky:

```python
df.loc[
    df["total"] > 10000,
    ["product", "total"]
]
```

Změna hodnot:

```python
df.loc[
    df["quantity"] <= 0,
    "quantity"
] = pd.NA
```

## `iloc`

Číselné pozice:

```python
df.iloc[
    0:5,
    1:4
]
```

```text
start → zahrnuje se
stop  → nezahrnuje se
```

---

# 15. Řazení

```python
df.sort_values(
    by="total",
    ascending=False
)
```

---

# 16. Chybějící hodnoty

```text
NaN → hodnota chybí
0   → známá hodnota nula
```

Kontrola:

```python
df.isna().sum()
df.notna()
```

Odstranění:

```python
df.dropna()

df.dropna(
    subset=["product"]
)
```

Doplnění:

```python
df["region"] = (
    df["region"]
    .fillna("Unknown")
)
```

Medián:

```python
df["unit_price"] = (
    df["unit_price"]
    .fillna(
        df["unit_price"].median()
    )
)
```

---

# 17. `copy()`

```python
df_clean = df.copy()
```

Vytvoří samostatnou pracovní kopii.

---

# 18. Duplicity

```python
df.duplicated().sum()
```

```python
df[
    df.duplicated()
]
```

```python
df = df.drop_duplicates()
```

---

# 19. Kategorie

```python
df["customer_type"].unique()
```

```python
df["customer_type"].value_counts()
```

Včetně `NaN`:

```python
df["customer_type"].value_counts(
    dropna=False
)
```

---

# 20. Čištění textu

```python
df["product"] = (
    df["product"].str.strip()
)
```

```python
df["customer_type"] = (
    df["customer_type"].str.upper()
)
```

```python
df["product"] = (
    df["product"].str.title()
)
```

Nahrazení:

```python
df["region"] = (
    df["region"]
    .replace(
        "cz-west",
        "CZ-West"
    )
)
```

---

# 21. Validace hodnot

```python
invalid_orders = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

Další příklad:

```python
df[
    (df["discount_pct"] < 0)
    | (df["discount_pct"] > 1)
]
```

Neznámou chybnou hodnotu lze změnit na `NaN`:

```python
df.loc[
    df["quantity"] <= 0,
    "quantity"
] = pd.NA
```

---

# 22. `describe()` a outliers

```python
df["quantity"].describe()
```

```text
count
mean
std
min
25%
50%
75%
max
```

Kontrola extrémů:

```python
df.sort_values(
    by="quantity",
    ascending=False
).head()
```

```text
neobvyklá hodnota
≠
automaticky chyba
```

---

# 23. Validace po čištění

```python
df.shape
df.isna().sum()
df.duplicated().sum()
df.dtypes

df["quantity"].min()
df["quantity"].max()
```

Kontrola business pravidel:

```python
df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

`Empty DataFrame` znamená, že žádný řádek daná pravidla neporušuje.

---

# 24. Data Cleaning Workflow

```text
raw data
→ kontrola struktury
→ NaN
→ duplicity
→ kategorie
→ text
→ validace
→ outliers
→ datové typy
→ závěrečná kontrola
```

Princip:

```text
znám správnou hodnotu
→ opravím

správnou hodnotu neznám
→ NaN / Unknown podle významu

neobvyklá hodnota
→ nejdříve ověřím

data si nevymýšlím
```

---

# 25. Export

CSV:

```python
df.to_csv(
    "output.csv",
    index=False
)
```

JSON:

```python
df.to_json(
    "output.json",
    orient="records",
    indent=4
)
```

Excel:

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

SQL:

```python
df.to_sql(
    "orders",
    connection
)
```

---

# 26. Import ↔ Export

```text
NAČTENÍ                     ULOŽENÍ

pd.read_csv()       ←→      df.to_csv()
pd.read_json()      ←→      df.to_json()
pd.read_excel()     ←→      df.to_excel()
pd.read_sql()       ←→      df.to_sql()
```

---

# 27. SQL vs. Pandas

```text
SQL                         pandas

WHERE                       df[podmínka]
AND                         &
OR                          |
NOT                         ~
IN                          isin()
BETWEEN                     between()

AVG()                       mean()
SUM()                       sum()
MIN()                       min()
MAX()                       max()

ORDER BY                    sort_values()

IS NULL                     isna()
IS NOT NULL                 notna()
```

---

# 28. Syntax — rychlá pomůcka

```text
()
→ funkce / metoda
→ seskupení podmínek

[]
→ sloupec
→ filtr
→ list
→ loc / iloc

{}
→ dictionary / JSON objekt

""
→ text

.
→ přístup k metodě / funkci / atributu

_
→ oddělení slov v názvu
→ snake_case
```

Například:

```python
pd.read_json()
```

```text
pd            → pandas
.             → přístup
read_json     → název funkce
()            → spuštění funkce
```

---

# 29. Nejdůležitější principy

```text
DataFrame
→ tabulka

Series
→ jeden sloupec

df["column"]
→ jeden sloupec

df[["a", "b"]]
→ více sloupců

podmínka
→ boolean maska

df[podmínka]
→ filtrované řádky

loc
→ názvy / podmínky

iloc
→ číselné pozice

NaN
→ chybějící hodnota

copy()
→ pracovní kopie

duplicated()
→ duplicity

unique()
→ unikátní hodnoty

value_counts()
→ četnosti

describe()
→ statistický přehled
```

---

# 30. Typický analytický workflow

```text
zdroj dat
→ ingestion
→ raw data
→ kontrola
→ cleaning
→ validation
→ transformace
→ analýza
→ export / reporting
```

Zdrojem může být například:

```text
CSV
JSON
Excel
XML
SQLite / SQL
API
```

---

# Další témata

```text
groupby()
agg()
SQL GROUP BY / HAVING

merge()
SQL JOIN

datum a čas

práce s textem

EDA a outliers

vizualizace

SQL + Python

automatizace
```
