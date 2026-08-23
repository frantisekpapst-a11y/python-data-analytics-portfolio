# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny `pandas`.

---

# 1. Import pandas

```python
import pandas as pd
```

```text
pandas → knihovna pro práci s tabulkovými daty
pd     → běžný alias
```

---

# 2. Načtení dat

```python
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")
df = pd.read_sql("SELECT * FROM orders", connection)
```

Pro Excel může být potřeba:

```text
pip install openpyxl
```

```text
NAČTENÍ                     ULOŽENÍ

pd.read_csv()       ←→      df.to_csv()
pd.read_json()      ←→      df.to_json()
pd.read_excel()     ←→      df.to_excel()
pd.read_sql()       ←→      df.to_sql()
```

---

# 3. DataFrame a Series

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

`df` je pouze běžná konvence.

```python
orders = pd.read_csv("orders.csv")
sales = pd.read_csv("sales.csv")
```

---

# 4. Základní kontrola datasetu

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
df.shape
→ (počet řádků, počet sloupců)
```

Atributy nemají `()`:

```python
df.shape
df.columns
df.index
df.dtypes
```

Metody mají `()`:

```python
df.head()
df.info()
```

---

# 5. Datové typy

```text
str       → text
int64     → celé číslo
float64   → desetinné číslo
bool      → True / False
datetime  → datum a čas
```

Kontrola:

```python
df.dtypes
```

Převod textu na datum:

```python
df["order_date"] = pd.to_datetime(
    df["order_date"]
)
```

---

# 6. Pandas index

Výchozí index:

```text
0
1
2
3
...
```

```text
Pandas index
≠
business ID / primary key
```

Reset indexu:

```python
df = df.reset_index(
    drop=True
)
```

---

# 7. Výběr sloupců

Jeden sloupec:

```python
df["product"]
```

→ `Series`

Více sloupců:

```python
df[
    ["product", "quantity", "total"]
]
```

→ `DataFrame`

---

# 8. Nový sloupec

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

Pokud sloupec neexistuje, pandas ho vytvoří.

---

# 9. Základní agregace

```python
df["total"].sum()
df["total"].mean()
df["total"].min()
df["total"].max()
df["total"].median()
df["product"].mode()
```

```text
sum()       → součet
mean()      → průměr
min()       → minimum
max()       → maximum
median()    → medián
mode()      → modus
```

---

# 10. Boolean maska a filtrování

Samotná podmínka:

```python
df["total"] > 10000
```

vrací:

```text
True
False
True
...
```

Použití:

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

Porovnávací operátory:

```text
==    rovná se
!=    nerovná se
>     větší než
<     menší než
>=    větší nebo rovno
<=    menší nebo rovno
```

---

# 11. Více podmínek

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Každá podmínka má být v závorkách.

```python
df[
    (df["category"] == "Furniture")
    & (df["total"] > 10000)
]
```

```python
df[
    (df["total"] > 20000)
    | (df["quantity"] >= 4)
]
```

```python
df[
    ~(df["category"] == "Furniture")
]
```

---

# 12. `isin()` a `between()`

## `isin()`

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
        "Desk",
        "Monitor"
    ])
]
```

## `between()`

```python
df[
    df["total"].between(
        10000,
        20000
    )
]
```

Výchozí:

```text
10000 <= x <= 20000
```

Možnosti:

```text
inclusive="both"
inclusive="left"
inclusive="right"
inclusive="neither"
```

---

# 13. `loc` a `iloc`

## `loc`

Výběr podle názvů a podmínek:

```python
df.loc[
    df["category"] == "Furniture",
    ["product", "quantity", "total"]
]
```

```text
loc
→ co se jmenuje jak
```

`loc` lze použít i ke změně vybraných hodnot:

```python
df.loc[
    df["quantity"] <= 0,
    "quantity"
] = pd.NA
```

## `iloc`

Výběr podle číselné pozice:

```python
df.iloc[
    0:5,
    1:4
]
```

```text
iloc
→ co je kde
```

Slicing:

```text
[start:stop]

start → zahrnuje se
stop  → nezahrnuje se
```

---

# 14. Řazení

```python
df.sort_values(
    by="total",
    ascending=False
)
```

Například nejvyšší objednávky:

```python
df.sort_values(
    by="total",
    ascending=False
).head()
```

---

# 15. Chybějící hodnoty

```text
NaN
→ hodnota chybí / není známá

0
→ skutečná známá hodnota nula
```

Kontrola:

```python
df.isna()
df.isna().sum()
df.notna()
```

Filtrování neprázdných hodnot:

```python
df[
    df["region"].notna()
]
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

Není nutné každý `NaN` doplnit.

---

# 16. `copy()` — pracovní kopie

```python
orders_clean = orders.copy()
```

```text
orders
→ původní DataFrame

orders_clean
→ samostatná pracovní kopie
```

Při čištění dat je vhodné neměnit původní dataset bez důvodu.

---

# 17. Duplicity

Počet duplicit:

```python
df.duplicated().sum()
```

Zobrazení duplicit:

```python
df[
    df.duplicated()
]
```

Odstranění:

```python
df = df.drop_duplicates()
```

`drop_duplicates()` bez parametrů porovnává celý řádek.

---

# 18. Kontrola kategorií

Unikátní hodnoty:

```python
df["customer_type"].unique()
```

Počet jednotlivých hodnot:

```python
df["customer_type"].value_counts()
```

Včetně `NaN`:

```python
df["customer_type"].value_counts(
    dropna=False
)
```

Praktické použití:

```text
B2B
b2b
B2B 
Business
```

může odhalit nekonzistentní zápis kategorií.

---

# 19. Čištění textových hodnot

Odstranění mezer na začátku a konci:

```python
df["product"] = (
    df["product"]
    .str.strip()
)
```

Velká písmena:

```python
df["customer_type"] = (
    df["customer_type"]
    .str.upper()
)
```

První písmena velká:

```python
df["product"] = (
    df["product"]
    .str.title()
)
```

Nahrazení konkrétní hodnoty:

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

# 20. Kontrola nevalidních hodnot

Příklady business pravidel:

```python
df[
    df["quantity"] <= 0
]
```

```python
df[
    df["unit_price"] <= 0
]
```

```python
df[
    (df["discount_pct"] < 0)
    | (df["discount_pct"] > 1)
]
```

Více pravidel najednou:

```python
invalid_orders = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
    | (df["discount_pct"] < 0)
    | (df["discount_pct"] > 1)
]
```

Pokud správnou hodnotu neznáme, můžeme chybnou hodnotu převést na `NaN`:

```python
df.loc[
    df["quantity"] <= 0,
    "quantity"
] = pd.NA
```

```python
df.loc[
    df["unit_price"] <= 0,
    "unit_price"
] = pd.NA
```

```python
df.loc[
    (df["discount_pct"] < 0)
    | (df["discount_pct"] > 1),
    "discount_pct"
] = pd.NA
```

---

# 21. Outliers a `describe()`

Rychlý statistický přehled:

```python
df["quantity"].describe()
```

Ukazuje:

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

```text
std
→ směrodatná odchylka
→ ukazuje rozptýlení hodnot
```

Kontrola extrémů:

```python
df.sort_values(
    by="quantity",
    ascending=False
).head()
```

Například:

```python
high_quantity_orders = df[
    df["quantity"] > 20
]
```

Důležitý princip:

```text
neobvyklá hodnota
≠
automaticky chyba
```

Například `quantity = 50` může být legitimní velká B2B objednávka.

---

# 22. Validace po čištění

Po cleaningu data znovu zkontrolujeme:

```python
df.shape

df.isna().sum()

df.duplicated().sum()

df["customer_type"].value_counts(
    dropna=False
)

df["quantity"].min()
df["quantity"].max()

df.dtypes
```

Kontrola business pravidel:

```python
df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
    | (df["discount_pct"] < 0)
    | (df["discount_pct"] > 1)
]
```

Pokud je výsledek:

```text
Empty DataFrame
```

žádný řádek už daná validační pravidla neporušuje.

---

# 23. Data Cleaning Workflow

```text
načtení dat
→ základní kontrola
→ kontrola NaN
→ kontrola duplicit
→ kontrola kategorií
→ sjednocení textu
→ kontrola nevalidních hodnot
→ kontrola outliers
→ úprava datových typů
→ validace po čištění
```

Důležitý princip:

```text
znám správnou hodnotu
→ opravím ji

správnou hodnotu neznám
→ NaN / Unknown podle významu

neobvyklá hodnota
→ nejdříve ověřím

nevymýšlím data bez business důvodu
```

---

# 24. Export dat

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

# 25. Rychlý pandas tahák

```python
import pandas as pd

# načtení
df = pd.read_csv("data.csv")

# základní kontrola
df.head()
df.info()
df.shape
df.columns
df.dtypes

# pracovní kopie
df_clean = df.copy()

# NaN
df_clean.isna().sum()
df_clean["region"].fillna("Unknown")
df_clean.dropna(subset=["product"])

# duplicity
df_clean.duplicated().sum()
df_clean.drop_duplicates()

# kategorie
df_clean["region"].unique()
df_clean["region"].value_counts(dropna=False)

# text
df_clean["product"].str.strip()
df_clean["product"].str.title()
df_clean["customer_type"].str.upper()

# nahrazení
df_clean["region"].replace(
    "cz-west",
    "CZ-West"
)

# datum
df_clean["order_date"] = pd.to_datetime(
    df_clean["order_date"]
)

# kontrola čísel
df_clean[
    df_clean["quantity"] <= 0
]

# změna nevalidní hodnoty na NaN
df_clean.loc[
    df_clean["quantity"] <= 0,
    "quantity"
] = pd.NA

# statistický přehled
df_clean["quantity"].describe()

# nový sloupec
df_clean["total"] = (
    df_clean["quantity"]
    * df_clean["unit_price"]
)

# agregace
df_clean["total"].sum()
df_clean["total"].mean()
df_clean["total"].median()
df_clean["total"].min()
df_clean["total"].max()

# filtr
df_clean[
    df_clean["total"] > 10000
]

# více podmínek
df_clean[
    (df_clean["total"] > 10000)
    & (df_clean["category"] == "Furniture")
]

# isin
df_clean[
    df_clean["product"].isin([
        "Laptop",
        "Desk"
    ])
]

# between
df_clean[
    df_clean["total"].between(
        10000,
        20000
    )
]

# loc
df_clean.loc[
    df_clean["total"] > 10000,
    ["product", "total"]
]

# iloc
df_clean.iloc[
    0:5,
    1:4
]

# řazení
df_clean.sort_values(
    by="total",
    ascending=False
)

# export
df_clean.to_csv(
    "clean_data.csv",
    index=False
)
```

---

# 26. Syntax — rychlá pomůcka

```text
()
→ funkce / metoda
→ seskupení podmínek

[]
→ sloupec
→ filtrování
→ list
→ loc / iloc

""
→ text
→ názvy sloupců
→ textové hodnoty
```

Příklad:

```python
df["product"].isin([
    "Laptop",
    "Desk",
    "Monitor"
])
```

---

# 27. SQL vs. pandas

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

# 28. Nejdůležitější principy

```text
DataFrame
→ celá tabulka

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
→ chybějící nebo neznámá hodnota

isna().sum()
→ počet chybějících hodnot

duplicated()
→ kontrola duplicit

unique()
→ unikátní hodnoty

value_counts()
→ četnost hodnot

str.strip()
→ odstranění mezer

replace()
→ nahrazení hodnot

describe()
→ rychlý statistický přehled

pd.to_datetime()
→ převod na datum

copy()
→ samostatná pracovní kopie
```

---

# Typický analytický postup

```text
získání dat
→ načtení
→ kontrola struktury
→ kontrola kvality
→ cleaning
→ validace
→ transformace
→ filtrování
→ výpočty a analýza
→ export
```

---

# Další témata

```text
Data Sources & Ingestion
SQLite
pd.read_sql()
API

groupby()
agg()
GROUP BY / HAVING

merge()
SQL JOIN

datum a čas

práce s textem

EDA a outliers

vizualizace

SQL + Python

automatizace
```