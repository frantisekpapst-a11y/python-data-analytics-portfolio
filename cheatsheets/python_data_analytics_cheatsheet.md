# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny `pandas`. :contentReference[oaicite:0]{index=0}

---

# 1. Importy

```python
import pandas as pd
import sqlite3
import requests
import matplotlib.pyplot as plt
```

```text
pandas     → tabulková data
sqlite3    → SQLite databáze
requests   → API / HTTP požadavky
matplotlib → grafy a vizualizace
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

UTF-8  → dnešní standard
cp1250 → starší Windows encoding pro střední Evropu
```

TXT:

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
{} → objekt
[] → pole / array

"key": value
→ dvojice klíč–hodnota
```

### Nested JSON

```python
df = pd.json_normalize(data)
```

```text
customer
├── name
└── city
```

může vytvořit:

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

---

## SQLite + SQL

```python
connection = sqlite3.connect(
    "database.db"
)
```

```python
query = """
SELECT *
FROM orders
WHERE quantity > 2
"""
```

```python
df = pd.read_sql(
    query,
    connection
)
```

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

---

## API

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

JSON:

```python
data = response.json()
```

DataFrame:

```python
df = pd.DataFrame(data)
```

Nested JSON:

```python
df = pd.json_normalize(data)
```

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
df.index
df.dtypes
```

Metody:

```python
df.head()
df.info()
df.copy()
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

df["price"] = df["price"].astype(float)
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

Po `groupby()`:

```python
summary = (
    df.groupby("category")["total"]
    .sum()
    .reset_index()
)
```

Alternativa:

```python
summary = (
    df.groupby(
        "category",
        as_index=False
    )["total"]
    .sum()
)
```

`as_index=False` ponechá grouping sloupec jako běžný sloupec.

---

# 8. Výběr sloupců

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

```text
vnitřní []
→ list názvů sloupců

vnější []
→ výběr z DataFrame
```

---

# 9. Nový sloupec

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

Pokud sloupec neexistuje, pandas ho vytvoří.

---

# 10. Základní agregace

```python
df["total"].sum()
df["total"].mean()
df["total"].median()
df["total"].min()
df["total"].max()
df["total"].count()
```

Četnosti:

```python
df["category"].value_counts()
```

Nejčastější hodnota:

```python
df["category"].mode()
```

---

# 11. Boolean maska

```python
df["total"] > 10000
```

Vrací:

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

```text
podmínka
→ boolean maska

df[podmínka]
→ ponechá řádky s True
```

---

# 12. Více podmínek

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

AND:

```python
df[
    (df["total"] > 10000)
    & (df["category"] == "Furniture")
]
```

OR:

```python
df[
    (df["category"] == "Furniture")
    | (df["category"] == "Electronics")
]
```

---

# 13. `isin()`

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

```text
SQL IN     → isin()
SQL NOT IN → ~isin()
```

---

# 14. `between()`

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

# 15. `loc`

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

```text
loc
→ názvy / podmínky
```

---

# 16. `iloc`

```python
df.iloc[
    0:5,
    1:4
]
```

```text
iloc
→ číselné pozice

start → zahrnuje se
stop  → nezahrnuje se
```

---

# 17. Řazení

```python
df.sort_values(
    by="total",
    ascending=False
)
```

Výchozí:

```text
ascending=True
```

---

# 18. Missing values

Kontrola:

```python
df.isna()
df.isna().sum()
df.notna()
```

Odstranění:

```python
df = df.dropna(
    subset=["product"]
)
```

Doplnění textu:

```python
df["region"] = (
    df["region"]
    .fillna("Unknown")
)
```

Doplnění mediánem:

```python
df["unit_price"] = (
    df["unit_price"]
    .fillna(
        df["unit_price"].median()
    )
)
```

---

# 19. Duplicity a unikátní hodnoty

Kontrola:

```python
df.duplicated()
df.duplicated().sum()
```

Zobrazení:

```python
df[
    df.duplicated()
]
```

Odstranění:

```python
df = df.drop_duplicates()
```

Unikátní hodnoty:

```python
df["category"].unique()
```

Počet unikátních:

```python
df["customer_id"].nunique()
```

Četnosti:

```python
df["category"].value_counts()
```

---

# 20. Čištění textu

Odstranění mezer:

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

Title Case:

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

Business pravidla:

```python
df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

`Empty DataFrame` → žádný řádek podmínku neporušuje.

---

# 24. Data Cleaning Workflow

```text
raw data
→ kontrola struktury
→ text cleaning
→ NaN
→ duplicity
→ datové typy
→ business validace
→ kontrola klíčů
→ outliers
→ závěrečná kontrola
```

```text
znám správnou hodnotu
→ opravím

správnou hodnotu neznám
→ NaN / Unknown

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

Jednodušší varianta:

```python
sales_by_category = (
    df.groupby(
        "category",
        as_index=False
    )["total"]
    .sum()
)
```

Více grouping sloupců:

```python
summary = (
    df.groupby(
        ["category", "region"],
        as_index=False
    )["total"]
    .sum()
)
```

---

# 26. `agg()`

Více agregací:

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

Pojmenované agregace:

```python
summary = (
    df.groupby(
        "category",
        as_index=False
    )
    .agg(
        total_revenue=("total", "sum"),
        avg_order_value=("total", "mean"),
        max_quantity=("quantity", "max")
    )
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
    filtered.groupby(
        "category",
        as_index=False
    )["total"]
    .sum()
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

Stejný klíč:

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
→ rozdílné názvy
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

```python
how="inner"
how="left"
how="right"
how="outer"
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
→ opakování na obou stranách
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

Diagnostika:

```python
customers["id"].nunique()

customers["id"].duplicated().sum()
```

Duplicitní klíče:

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

```text
NaN po merge
→ často chybějící shoda v pravé tabulce
```

Kontrola referenční integrity:

```python
orders[
    ~orders["customer_id"].isin(
        customers["customer_id"]
    )
]
```

---

# 32. `suffixes`

Pokud mají tabulky stejně pojmenovaný sloupec:

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

# 35. Datum a čas

Převod textu na datetime:

```python
df["order_date"] = pd.to_datetime(
    df["order_date"]
)
```

```text
pd.to_datetime()
→ funkce knihovny pandas
→ převádí hodnoty na datetime
```

Části data:

```python
df["year"] = df["order_date"].dt.year

df["month"] = df["order_date"].dt.month

df["day"] = df["order_date"].dt.day
```

```text
.dt
→ přístup k částem datetime / timedelta
```

---

# 36. `strftime()` — formát data

```python
df["year_month"] = (
    df["order_date"]
    .dt.strftime("%Y_%m")
)
```

```text
%Y → rok
%m → měsíc
%d → den
```

Například:

```text
2026-08-27
→
2026_08
```

`strftime()` vrací text.

---

# 37. Název dne

```python
df["day_name"] = (
    df["order_date"]
    .dt.day_name()
)
```

Česky:

```python
df["day_name"] = (
    df["order_date"]
    .dt.day_name(
        locale="cs_CZ"
    )
)
```

---

# 38. Rozdíl mezi daty

```python
df["delivery_days"] = (
    df["delivery_date"]
    - df["order_date"]
).dt.days
```

```text
datum - datum
→ timedelta

.dt.days
→ počet dní
```

---

# 39. Filtrování podle data

```python
df[
    df["order_date"] >= "2026-08-01"
]
```

Interval:

```python
df[
    df["order_date"].between(
        "2026-08-05",
        "2026-08-15"
    )
]
```

Bez hranic:

```python
df[
    df["order_date"].between(
        "2026-08-05",
        "2026-08-15",
        inclusive="neither"
    )
]
```

---

# 40. Řazení podle data

```python
df = df.sort_values(
    by="order_date"
)
```

Sestupně:

```python
df = df.sort_values(
    by="order_date",
    ascending=False
)
```

---

# 41. Měsíční reporting

```python
df["year_month"] = (
    df["order_date"]
    .dt.strftime("%Y_%m")
)
```

```python
monthly_sales = (
    df.groupby(
        "year_month",
        as_index=False
    )["revenue"]
    .sum()
)
```

Výsledek:

```text
year_month  revenue
2026_07     1500
2026_08     5000
```

---

# 42. Export

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

# 43. Import ↔ Export

```text
NAČTENÍ                      ULOŽENÍ

pd.read_csv()        ←→      df.to_csv()
pd.read_json()       ←→      df.to_json()
pd.read_excel()      ←→      df.to_excel()
pd.read_sql()        ←→      df.to_sql()
```

---

# 44. SQL vs. Pandas

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

# 45. Syntax — rychlá pomůcka

```text
pd.funkce()
→ funkce knihovny pandas

df.metoda()
→ metoda DataFrame / Series

df.vlastnost
→ atribut / vlastnost
```

Příklady:

```python
pd.to_datetime(...)

df.copy()
df.head()

df.shape
df.dtypes
```

Další přehled:

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
→ přístup k metodě / atributu

_
→ snake_case
```

---

# 46. Nejdůležitější principy

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
→ seskupení

agg()
→ agregace

merge()
→ spojení tabulek

validate=
→ kontrola vztahu klíčů

pd.to_datetime()
→ převod na datetime

.dt
→ části data / času

strftime()
→ datetime → text

timedelta
→ rozdíl mezi daty

.str
→ přístup k textovým metodám
```

---

# 47. Typický analytický workflow

```text
zdroj dat

→ ingestion

→ raw data

→ kontrola struktury

→ cleaning

→ validation

→ merge

→ transformace

→ filtrování

→ groupby / agregace

→ analýza

→ export / reporting
```

---

# 48. Práce s textem v Pandas

Textové metody používají `.str`:

```python
df["column"].str.metoda()
```

Základní úpravy:

```python
df["name"].str.strip()
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.title()
```

```text
strip() → odstraní mezery na začátku a konci
lower() → malá písmena
upper() → velká písmena
title() → první písmeno každého slova velké
```

Hledání v textu:

```python
df["email"].str.contains(
    "gmail.com",
    na=False
)

df["email"].str.startswith(
    "jan",
    na=False
)

df["email"].str.endswith(
    "gmail.com",
    na=False
)
```

```text
contains()   → obsahuje
startswith() → začíná
endswith()   → končí
```

SQL analogie:

```text
LIKE '%text%' → .str.contains("text")
LIKE 'text%'  → .str.startswith("text")
LIKE '%text'  → .str.endswith("text")
= 'text'      → == "text"
```

Nahrazení textu:

```python
df["email"] = (
    df["email"]
    .str.replace(
        "@firma.cz",
        "@company.cz",
        regex=False
    )
)
```

Rozdělení textu:

```python
df[["email_name", "email_domain"]] = (
    df["email"]
    .str.split(
        "@",
        expand=True
    )
)
```

```text
expand=True
→ rozdělí výsledek do více sloupců
```

Délka textu:

```python
df["email_length"] = (
    df["email"]
    .str.len()
)
```

```text
.str.len()
→ počet znaků
```

---

# 49. EDA — Exploratory Data Analysis

EDA = rychlé prozkoumání dat před hlubší analýzou.

```text
struktura
→ statistiky
→ kategorie
→ agregace
→ outliers
→ distribuce
→ vztahy mezi proměnnými
→ business interpretace
```

## Základní kontrola

```python
df.shape
df.info()
df.dtypes
df.describe()
```

Kategorie:

```python
df["region"].value_counts()
```

Extrémní hodnoty:

```python
df.sort_values(
    by="revenue",
    ascending=False
).head(3)
```

---

## Mean, median a rozložení

```text
mean
→ průměr
→ citlivý na extrémní hodnoty

median
→ prostřední hodnota
→ odolnější vůči outlierům

mean výrazně > median
→ často right-skewed distribuce

mean výrazně < median
→ často left-skewed distribuce
```

---

## IQR a outliers

Kvartily:

```python
q1 = df["revenue"].quantile(0.25)
q3 = df["revenue"].quantile(0.75)

iqr = q3 - q1
```

```text
Q1  → 25. percentil
Q3  → 75. percentil

IQR = Q3 - Q1
→ šířka prostředních 50 % dat
```

Hranice:

```python
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
```

Outliers:

```python
outliers = df[
    (df["revenue"] < lower_bound)
    | (df["revenue"] > upper_bound)
]
```

```text
hodnota mimo hranice
→ potenciální outlier

outlier
≠
automaticky chyba
```

Pro outliery bývá často praktičtější:

```text
median + IQR
```

Pro celkovou variabilitu:

```text
mean + std
```

---

## Korelace

```python
correlation = df[
    ["quantity", "revenue"]
].corr()
```

```text
korelace blízko 1
→ silný pozitivní lineární vztah

korelace blízko 0
→ slabý lineární vztah

korelace blízko -1
→ silný negativní lineární vztah
```

```text
korelace
≠
kauzalita
```

Outlier může korelaci výrazně zesílit nebo oslabit.

---

## Distribuce

Histogram:

```python
df["revenue"].hist(
    bins=5
)

plt.show()
```

```text
histogram
→ ukazuje tvar distribuce

bins
→ počet intervalů
```

Typické tvary:

```text
symetrická
→ mean ≈ median

right-skewed
→ dlouhý ocas doprava
→ často mean > median

left-skewed
→ dlouhý ocas doleva
→ často mean < median
```

---

## Boxplot

```python
df.boxplot(
    column="revenue"
)

plt.show()
```

```text
spodní hrana boxu → Q1
čára v boxu       → median
horní hrana boxu  → Q3

box
→ prostředních 50 % dat

samostatné body
→ potenciální outliers
```

---

## EDA checklist

```text
1. Struktura
→ shape
→ info()
→ dtypes

2. Statistiky
→ describe()
→ mean / median
→ min / max / std

3. Kategorie
→ value_counts()

4. Agregace
→ groupby()
→ sum / mean / count

5. Outliers
→ Q1 / Q3
→ IQR
→ hranice

6. Distribuce
→ histogram
→ boxplot

7. Vztahy
→ corr()

8. Interpretace
→ co výsledek vytváří
→ co je neobvyklé
→ co je potřeba ověřit
```

---

# 50. Statistické testy — praktické minimum

Statistické testy pomáhají ověřit, zda rozdíl nebo vztah v datech může být skutečný, nebo mohl vzniknout náhodou.

## H0, H1 a p-value

```text
H0
→ nic zvláštního se neděje
→ rozdíl / vztah není statisticky prokázán

H1
→ rozdíl / vztah existuje
```

Praktické pravidlo:

```text
p-value < 0.05
→ zamítáme H0
→ máme statistický důkaz rozdílu / vztahu

p-value >= 0.05
→ H0 nezamítáme
→ nemáme dost důkazů
```

Důležité:

```text
statisticky významné
≠
businessově důležité

korelace
≠
kauzalita
```

---

## Jaký test použít?

```text
2 číselné proměnné
→ Pearson
→ souvisí spolu?

2 skupiny + číslo
→ t-test
→ liší se jejich průměry?

2 kategorie
→ chi-square
→ souvisejí spolu kategorie?

3+ skupin + číslo
→ ANOVA
→ liší se průměry mezi skupinami?

2 skupiny + problematická distribuce / outliers
→ Mann–Whitney U
→ alternativa k t-testu

kontrola normality
→ Shapiro-Wilk
```

---

## Pearsonova korelace

Pandas `.corr()` používá standardně Pearsonovu korelaci:

```python
df[
    ["quantity", "revenue"]
].corr()
```

Korelace + p-value:

```python
from scipy.stats import pearsonr

r, p_value = pearsonr(
    df["quantity"],
    df["revenue"]
)
```

```text
r
→ síla a směr lineárního vztahu

r > 0 → pozitivní vztah
r < 0 → negativní vztah

p-value
→ statistická významnost vztahu
```

---

## t-test — dvě skupiny

Například Praha vs. Brno:

```python
from scipy.stats import ttest_ind

praha = df.loc[
    df["region"] == "Praha",
    "revenue"
]

brno = df.loc[
    df["region"] == "Brno",
    "revenue"
]

t_stat, p_value = ttest_ind(
    praha,
    brno,
    equal_var=False
)
```

```text
otázka
→ liší se průměrné revenue mezi 2 skupinami?
```

---

## Chi-square — dvě kategorie

Například:

```text
region × customer_type
```

```python
from scipy.stats import chi2_contingency

table = pd.crosstab(
    df["region"],
    df["customer_type"]
)

chi2, p_value, dof, expected = (
    chi2_contingency(table)
)
```

```text
otázka
→ souvisejí spolu dvě kategoriální proměnné?
```

---

## ANOVA — více skupin

```python
from scipy.stats import f_oneway

f_stat, p_value = f_oneway(
    praha,
    brno,
    ostrava
)
```

```text
t-test
→ 2 skupiny

ANOVA
→ 3+ skupin

ANOVA řekne:
→ alespoň jedna skupina se liší

neřekne:
→ která konkrétní
```

---

## Mann–Whitney U

```python
from scipy.stats import mannwhitneyu

u_stat, p_value = mannwhitneyu(
    praha,
    brno,
    alternative="two-sided"
)
```

```text
→ alternativa k t-testu
→ pracuje s pořadím hodnot
→ vhodný při outlierech / problematické distribuci
```

---

## Shapiro-Wilk — normalita

```python
from scipy.stats import shapiro

stat, p_value = shapiro(
    praha
)
```

```text
p-value < 0.05
→ data pravděpodobně nejsou normálně rozložená

p-value >= 0.05
→ nemáme důkaz proti normalitě
```

---

## Praktický tahák

```text
Co chci zjistit?

souvisí 2 čísla?
→ Pearson

liší se 2 skupiny?
→ t-test

liší se 3+ skupin?
→ ANOVA

souvisejí 2 kategorie?
→ chi-square

mám 2 skupiny a divná data / outliery?
→ Mann–Whitney

chci zkontrolovat normalitu?
→ Shapiro-Wilk
```

Při interpretaci vždy zkontroluj:

```text
p-value
+
velikost vzorku
+
outliery
+
velikost skutečného rozdílu
+
business význam
```

---

# NumPy — praktické použití v datové analýze

## Import

```python
import numpy as np
```

---

## NumPy array

```python
sales = np.array([1200, 1500, 900, 1800, 2100])
```

Základní informace:

```python
sales.shape
sales.size
sales.ndim
sales.dtype
```

---

## Filtrování

```python
sales[sales > 1500]
```

Princip je podobný jako v Pandas:

```python
df[df["sales"] > 1500]
```

---

## Výpočty nad celým polem

```python
sales * 1.10
```

```python
profit = sales - costs
```

NumPy provádí výpočty nad všemi hodnotami bez nutnosti `for` smyčky.

---

## `np.where()` — jedna podmínka

Praktické hlavně při tvorbě nového sloupce v Pandas:

```python
df["sales_level"] = np.where(
    df["sales"] >= 1500,
    "High",
    "Low"
)
```

Struktura:

```text
np.where(
    podmínka,
    hodnota když True,
    hodnota když False
)
```

```text
1 podmínka
→ np.where()
```

---

## `np.select()` — více podmínek

```python
df["sales_category"] = np.select(
    [
        df["sales"] >= 1800,
        df["sales"] >= 1200
    ],
    [
        "High",
        "Medium"
    ],
    default="Low"
)
```

Struktura:

```text
np.select(
    conditions,
    choices,
    default
)
```

```text
více podmínek
→ np.select()
```

Pořadí podmínek je důležité.

---

## Chybějící hodnoty

NumPy používá:

```python
np.nan
```

Například:

```python
values = np.array([10, 20, np.nan, 40])
```

Funkce ignorující `NaN`:

```python
np.nanmean(values)
np.nanmedian(values)
np.nansum(values)
```

Pozor:

```python
np.mean(values)
```

může vrátit:

```text
nan
```

V Pandas `mean()`, `median()` nebo `sum()` standardně `NaN` ignorují.

---

## Percentily

```python
q1 = np.percentile(sales, 25)
q3 = np.percentile(sales, 75)

iqr = q3 - q1
```

Pandas varianta:

```python
df["sales"].quantile(0.25)
df["sales"].quantile(0.75)
```

---

## 2D array a `axis`

```python
data = np.array([
    [1200, 800],
    [1500, 1000],
    [900, 700]
])
```

Průměr po sloupcích:

```python
np.mean(data, axis=0)
```

Průměr po řádcích:

```python
np.mean(data, axis=1)
```

```text
axis=0
→ výsledek pro jednotlivé sloupce

axis=1
→ výsledek pro jednotlivé řádky
```

---

## Převod Pandas → NumPy

```python
array = df["sales"].to_numpy()
```

NumPy → Pandas:

```python
series = pd.Series(array)
```

---

## Pandas vs. NumPy

```text
Pandas
→ hlavní nástroj pro tabulková business data
→ groupby
→ merge
→ missing values
→ agregace
→ filtry
→ práce se sloupci

NumPy
→ pomocný nástroj pro číselné výpočty
→ arrays
→ np.where()
→ np.select()
→ numerické operace
```

Pro běžnou datovou analytiku:

```text
základ práce
→ Pandas

NumPy použít tam,
kde zkrátí nebo zpřehlední řešení
```

Nejpraktičtější kombinace:

```text
Pandas DataFrame
+
np.where()
+
np.select()
```

---

# Vizualizace — Matplotlib, Pandas plotting a Plotly

## Importy

```python
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import plotly.express as px
import numpy as np
```

```text
Matplotlib
→ statické grafy
→ velká kontrola nad vzhledem

Pandas plotting
→ rychlé grafy přímo z DataFrame
→ používá Matplotlib

Plotly
→ interaktivní grafy
→ hover, zoom, legenda
```

---

## Matplotlib — základní grafy

```python
plt.plot(x, y)
plt.bar(x, y)
plt.scatter(x, y)
plt.hist(values)
plt.boxplot(values)
plt.pie(values)
```

```text
plot()    → line chart
bar()     → sloupcový graf
scatter() → scatter plot
hist()    → histogram
boxplot() → boxplot
pie()     → koláčový graf
```

---

## Základní formátování

```python
plt.figure(figsize=(8, 4))

plt.title(
    "Název grafu",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.tight_layout()
plt.show()
```

```text
figsize
→ velikost grafu

fontweight="bold"
→ tučné písmo

grid()
→ mřížka

alpha
→ průhlednost

tight_layout()
→ upraví rozložení

show()
→ zobrazí graf
```

---

## Formát hodnot na ose

Například:

```text
120000
→ 120k
```

```python
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(
        lambda x, pos: f"{x / 1000:.0f}k"
    )
)
```

---

## Trendová čára

```python
trend = np.polyfit(
    df["ad_spend"],
    df["revenue"],
    1
)

trend_line = np.poly1d(trend)
```

```python
plt.plot(
    df["ad_spend"],
    trend_line(df["ad_spend"])
)
```

```text
np.polyfit(..., 1)
→ lineární trend

np.poly1d()
→ vytvoří použitelnou funkci trendu
```

---

## Histogram

```python
plt.hist(
    df["resolution_hours"],
    bins=[0, 5, 10, 15, 20, 25, 30, 35],
    rwidth=0.9,
    edgecolor="black"
)
```

```text
bins
→ intervaly

rwidth
→ šířka sloupců

edgecolor
→ obrys sloupců
```

Průměr a medián:

```python
plt.axvline(
    mean_value,
    linestyle="--",
    label="Průměr",
    zorder=5
)

plt.axvline(
    median_value,
    linestyle=":",
    label="Medián",
    zorder=5
)

plt.legend()
```

```text
axvline()
→ svislá čára

zorder
→ pořadí vrstev
→ vyšší číslo = více vpředu
```

---

## Koláčový graf

```python
plt.pie(
    df["revenue"],
    labels=df["segment"],
    autopct="%1.1f%%",
    explode=[0.03, 0.03, 0.03]
)

plt.show()
```

```text
labels
→ názvy výsečí

autopct
→ procenta

explode
→ oddělení výsečí
```

---

## Pandas plotting

```python
df.plot(
    x="month",
    y="revenue"
)

plt.show()
```

Sloupcový graf:

```python
df.plot(
    x="month",
    y="revenue",
    kind="bar"
)

plt.show()
```

```text
df.plot()
→ rychlá vizualizace přímo z DataFrame

kind="line"
kind="bar"
kind="scatter"
kind="hist"
```

Pandas plotting používá jako výchozí backend Matplotlib.

---

# Plotly — interaktivní grafy

## Import

```python
import plotly.express as px
```

---

## Line chart

```python
fig = px.line(
    df,
    x="month",
    y="revenue",
    markers=True,
    title="Měsíční tržby"
)

fig.show()
```

```text
fig
→ objekt grafu

fig.show()
→ zobrazí interaktivní graf
```

---

## Základní formátování

```python
fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)
```

Osa X jako kategorie:

```python
fig.update_xaxes(
    type="category"
)
```

Formát tisíců:

```python
fig.update_yaxes(
    tickformat="~s"
)
```

---

## Bar chart

```python
fig = px.bar(
    df,
    x="region",
    y="revenue",
    title="Tržby podle regionu"
)
```

Hodnoty nad sloupci:

```python
fig.update_traces(
    texttemplate="%{y:.3s}",
    textposition="outside"
)
```

```python
fig.show()
```

---

## Scatter plot

```python
fig = px.scatter(
    df,
    x="ad_spend",
    y="revenue",
    title="Vztah marketingových nákladů a tržeb"
)

fig.show()
```

Trend přes NumPy:

```python
trend = np.polyfit(
    df["ad_spend"],
    df["revenue"],
    1
)

trend_line = np.poly1d(trend)
```

```python
fig.add_scatter(
    x=df["ad_spend"],
    y=trend_line(df["ad_spend"]),
    mode="lines",
    name="Trend"
)
```

---

## Pie chart

```python
fig = px.pie(
    df,
    names="segment",
    values="revenue",
    title="Podíl tržeb podle segmentu"
)
```

```python
fig.update_traces(
    textposition="inside",
    textinfo="label+percent+value"
)

fig.show()
```

---

## Více line sérií

Wide DataFrame:

```text
month
B2B
B2C
Partner
```

Převod na long format:

```python
df_long = df.melt(
    id_vars="month",
    var_name="segment",
    value_name="revenue"
)
```

Graf:

```python
fig = px.line(
    df_long,
    x="month",
    y="revenue",
    color="segment",
    markers=True,
    title="Vývoj tržeb podle segmentu"
)

fig.show()
```

```text
melt()
→ wide → long format

color="segment"
→ samostatná série pro každý segment
→ automatická legenda
```

---

## Plotly interaktivita

```text
hover
→ přesné hodnoty

zoom
→ přiblížení

legenda
→ klik = skrýt / zobrazit sérii

dvojklik
→ izolovat jednu sérii
```

---

## Praktické použití

```text
rychlá kontrola dat
→ Pandas plotting

statický graf s větší kontrolou
→ Matplotlib

interaktivní graf
→ Plotly
```