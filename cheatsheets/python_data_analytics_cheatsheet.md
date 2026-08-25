# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny `pandas`.

---

# 1. Importy

```python
import pandas as pd
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

TXT s tabulkovou strukturou:

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

Nested JSON:

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
df["quantity"] = df["quantity"].astype(int)
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

Po `groupby()` často:

```python
summary = summary.reset_index()
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

# 10. Základní agregace

```python
df["total"].sum()
df["total"].mean()
df["total"].min()
df["total"].max()
df["total"].median()
df["product"].mode()
df["order_id"].count()
```

```text
sum()    → součet
mean()   → průměr
min()    → minimum
max()    → maximum
median() → medián
mode()   → modus
count()  → počet
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

# 18. Duplicity a unikátní hodnoty

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

Počet unikátních hodnot:

```python
df["customer_id"].nunique()
```

```text
unique()  → vypíše unikátní hodnoty
nunique() → spočítá unikátní hodnoty
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

Odstranění mezer:

```python
df["product"] = (
    df["product"].str.strip()
)
```

Velká písmena:

```python
df["customer_type"] = (
    df["customer_type"].str.upper()
)
```

První písmena velká:

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

# 25. `groupby()`

Základ:

```python
sales_by_category = (
    df.groupby("category")["total"]
    .sum()
    .reset_index()
)
```

Vzorec:

```python
df.groupby("A")["B"].sum()
```

```text
A → podle čeho seskupuji
B → co agreguji
```

Více grouping sloupců:

```python
summary = (
    df.groupby(
        ["category", "region"]
    )["total"]
    .sum()
    .reset_index()
)
```

---

# 26. `agg()`

Více agregací nad jedním sloupcem:

```python
summary = (
    df.groupby("category")["total"]
    .agg([
        "sum",
        "mean",
        "max"
    ])
    .reset_index()
)
```

Více sloupců:

```python
summary = (
    df.groupby("category")
    .agg({
        "total": ["sum", "max"],
        "quantity": ["mean"]
    })
    .reset_index()
)
```

Pojmenované agregace:

```python
summary = (
    df.groupby("category")
    .agg(
        total_revenue=("total", "sum"),
        avg_order_value=("total", "mean"),
        max_quantity=("quantity", "max")
    )
    .reset_index()
)
```

Vzorec:

```python
novy_nazev=("zdrojovy_sloupec", "agregace")
```

---

# 27. WHERE vs. HAVING

```text
WHERE
→ filtr řádků před agregací

HAVING
→ filtr skupin po agregaci
```

Pandas:

```python
filtered = df[
    df["quantity"] > 1
]

summary = (
    filtered.groupby("category")["total"]
    .sum()
    .reset_index()
)

high_categories = summary[
    summary["total"] > 30000
]
```

SQL:

```sql
SELECT
    category,
    SUM(total) AS total_sum
FROM orders
WHERE quantity > 1
GROUP BY category
HAVING SUM(total) > 30000;
```

---

# 28. `merge()` — spojování tabulek

Stejný název klíče:

```python
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)
```

Různé názvy klíče:

```python
result = orders.merge(
    customers,
    left_on="customer_id",
    right_on="id",
    how="left",
    validate="many_to_one"
)
```

```text
on=
→ stejný název klíče

left_on= / right_on=
→ rozdílné názvy klíče
```

---

# 29. Typy JOIN / merge

```text
inner
→ pouze shody

left
→ vše z levé tabulky

right
→ vše z pravé tabulky

outer
→ vše z obou tabulek

left_anti
→ řádky vlevo bez shody vpravo
```

Pandas:

```python
how="inner"
how="left"
how="right"
how="outer"
```

```text
LEFT JOIN
→ nejčastější při analytice

RIGHT JOIN
→ lze často přepsat jako obrácený LEFT JOIN
```

---

# 30. Validace vztahu při `merge()`

```text
one_to_one
→ klíč unikátní vlevo i vpravo

one_to_many
→ unikátní vlevo

many_to_one
→ unikátní vpravo

many_to_many
→ klíč se může opakovat na obou stranách
```

Příklad:

```python
validate="many_to_one"
```

Typický vztah:

```text
orders
many
→
customers
one
```

Při špatném vztahu Pandas vyhodí `MergeError`.

Diagnostika:

```python
customers["id"].nunique()

customers["id"].duplicated().sum()
```

Zobrazení duplicitního klíče:

```python
customers[
    customers["id"].duplicated(
        keep=False
    )
]
```

---

# 31. Kontrola po `merge()`

Missing values:

```python
result.isna().sum()
```

Počet řádků:

```python
len(orders)
len(result)
```

U očekávaného `many_to_one` + `left merge` by se počet řádků typicky neměl nečekaně zvýšit.

```text
NaN po merge
→ často znamená chybějící shodu v pravé tabulce
```

---

# 32. `suffixes`

Pokud mají obě tabulky stejně pojmenovaný sloupec:

```python
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    suffixes=(
        "_order",
        "_customer"
    )
)
```

Místo:

```text
region_x
region_y
```

vznikne:

```text
region_order
region_customer
```

---

# 33. Merge více tabulek

```python
orders_customers = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

final_df = orders_customers.merge(
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)
```

```text
groupby()
→ shrnuje řádky

merge()
→ spojuje tabulky
```

---

# 34. `tuple`

Tuple = pevná uspořádaná skupina hodnot.

```python
my_tuple = (
    "_order",
    "_customer"
)
```

Například:

```python
suffixes=(
    "_order",
    "_customer"
)
```

Rozdíl:

```python
my_list = ["A", "B"]

my_tuple = ("A", "B")
```

```text
list
→ []
→ lze měnit

tuple
→ ()
→ po vytvoření se nemění
```

---

# 35. Export

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

# 36. Import ↔ Export

```text
NAČTENÍ                     ULOŽENÍ

pd.read_csv()        ←→     df.to_csv()

pd.read_json()       ←→     df.to_json()

pd.read_excel()      ←→     df.to_excel()

pd.read_sql()        ←→     df.to_sql()
```

---

# 37. SQL vs. Pandas

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

GROUP BY                    groupby()

HAVING                      filtr po agregaci

INNER JOIN                  merge(how="inner")

LEFT JOIN                   merge(how="left")

RIGHT JOIN                  merge(how="right")

FULL OUTER JOIN             merge(how="outer")

ON stejný klíč              on="key"

ON různé klíče              left_on= / right_on=
```

---

# 38. Syntax — rychlá pomůcka

```text
()

→ funkce / metoda
→ seskupení podmínek
→ tuple podle kontextu


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

→ oddělení slov
→ snake_case
```

Příklad:

```python
pd.read_json()
```

```text
pd
→ pandas

.
→ přístup

read_json
→ název funkce

()
→ spuštění funkce
```

---

# 39. Nejdůležitější principy

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

nunique()
→ počet unikátních hodnot

value_counts()
→ četnosti

describe()
→ statistický přehled

groupby()
→ seskupení dat

agg()
→ více agregací

merge()
→ spojení tabulek

validate=
→ kontrola očekávaného vztahu klíčů

tuple
→ pevná uspořádaná skupina hodnot
```

---

# 40. Typický analytický workflow

```text
zdroj dat

→ ingestion

→ raw data

→ kontrola struktury

→ cleaning

→ validation

→ merge / propojení tabulek

→ transformace

→ filtrování

→ groupby / agregace

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
datum a čas

práce s textem pokročileji

EDA a outliers

vizualizace

API pokročileji

SQL + Python workflow

větší datasety

automatizace

portfolio case studies
```