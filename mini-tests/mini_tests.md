# Lekce 6 — Pandas základy

## Test 1 — Načtení a kontrola dat

### Zadání

Načti `ecommerce_sales_analysis.csv` do `df` a zobraz:

* prvních 5 řádků,
* rozměry datasetu,
* názvy sloupců,
* základní informace.

### Řešení

```python
import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

print(df.head())
print(df.shape)
print(df.columns)
df.info()
```

### Krátce

* `head()` → první řádky
* `shape` → počet řádků a sloupců
* `columns` → názvy sloupců
* `info()` → struktura a datové typy

---

## Test 2 — Nový sloupec a agregace

### Zadání

Vytvoř `total = quantity × unit_price` a vypočítej:

* celkové tržby,
* průměrnou hodnotu objednávky,
* maximum,
* minimum.

### Řešení

```python
df["total"] = df["quantity"] * df["unit_price"]

total_revenue = df["total"].sum()
avg_order = df["total"].mean()
max_order_value = df["total"].max()
min_order_value = df["total"].min()

print("Celkové tržby:", total_revenue)
print("Průměrná objednávka:", avg_order)
print("Maximum:", max_order_value)
print("Minimum:", min_order_value)
```

### Krátce

```text
sum()  → součet
mean() → průměr
max()  → maximum
min()  → minimum
```

---

## Test 3 — Filtrování dat

### Zadání

* vypočítej průměr `total`,
* vyber objednávky nad průměrem,
* vyber kategorii `Furniture`,
* spočítej její celkové tržby.

### Řešení

```python
average_order = df["total"].mean()

above_average_orders = df[
    df["total"] > average_order
]

furniture_orders = df[
    df["category"] == "Furniture"
]

total_revenue_furniture = furniture_orders["total"].sum()

print(total_revenue_furniture)
```

### Krátce

Podmínka vytváří **boolean masku**:

```python
df["total"] > average_order
```

Použití masky:

```python
df[df["total"] > average_order]
```

---

## Test 4 — Řazení

### Zadání

Seřaď dataset podle `total` sestupně a zobraz nejvyšší objednávku.

### Řešení

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)

print(sorted_orders.head())
print(sorted_orders.head(1))
```

### Krátce

```python
ascending=False
```

= sestupné řazení.

---

## Test 5 — Kompletní workflow

### Zadání

Načti CSV, vytvoř `total`, vyber objednávky nad průměrem, seřaď je a exportuj do CSV a JSON.

### Řešení

```python
import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

df["total"] = df["quantity"] * df["unit_price"]

average_order = df["total"].mean()

above_average_orders = df[
    df["total"] > average_order
]

sorted_orders = above_average_orders.sort_values(
    by="total",
    ascending=False
)

sorted_orders.to_csv(
    "above_average_orders_test.csv",
    index=False
)

sorted_orders.to_json(
    "above_average_orders_test.json",
    orient="records",
    indent=4
)
```

### Krátce

```text
načtení
→ výpočet
→ agregace
→ filtr
→ řazení
→ export
```

---

# Lekce 7 — Filtrování, loc a iloc

## Test 1 — AND

### Zadání

Vyber objednávky:

* `category == "Furniture"`
* `total > 15000`

### Řešení

```python
furniture_high_value = df[
    (df["category"] == "Furniture")
    & (df["total"] > 15000)
]
```

### Krátce

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Každou podmínku uzavři do závorek.

---

## Test 2 — OR a NOT

### Zadání

Vyber:

1. `quantity >= 4` nebo `total > 20000`
2. vše mimo kategorii `Electronics`

### Řešení

```python
high_quantity_or_value = df[
    (df["quantity"] >= 4)
    | (df["total"] > 20000)
]

not_electronics = df[
    df["category"] != "Electronics"
]
```

---

## Test 3 — `isin()` a `between()`

### Zadání

Vyber produkty `Laptop`, `Desk`, `Office Chair` a poté pouze objednávky s `total` mezi 15000 a 30000 včetně.

### Řešení

```python
selected_products = df[
    df["product"].isin([
        "Laptop",
        "Desk",
        "Office Chair"
    ])
]

selected_mid_value = selected_products[
    selected_products["total"].between(
        15000,
        30000
    )
]
```

### Krátce

* `isin()` → hodnota patří do seznamu
* `between()` → hodnota leží v intervalu

---

## Test 4 — `loc`

### Zadání

Pomocí `loc` vyber řádky s `total > 10000` a sloupce:

* `order_id`
* `product`
* `category`
* `total`

### Řešení

```python
high_value_summary = df.loc[
    df["total"] > 10000,
    ["order_id", "product", "category", "total"]
]
```

### Krátce

```python
df.loc[řádky, sloupce]
```

---

## Test 5 — `iloc` a `loc`

### Zadání

Pomocí `iloc` vyber prvních 5 řádků a sloupce na pozicích 1–4.

Potom pomocí `loc` vyber `Furniture` s `total > 10000`.

### Řešení

```python
first_five_selected = df.iloc[
    0:5,
    1:5
]

furniture_summary = df.loc[
    (df["category"] == "Furniture")
    & (df["total"] > 10000),
    ["product", "quantity", "total"]
]
```

### Krátce

```text
loc  → názvy a podmínky
iloc → číselné pozice
```

---

# Lekce 8 — Missing values

## Test 1 — Kontrola chybějících hodnot

### Zadání

Zjisti počet chybějících hodnot v každém sloupci `orders`.

### Řešení

```python
print(orders.isna().sum())
```

### Krátce

```text
True  = chybí
False = nechybí
```

`sum()` spočítá hodnoty `True`.

---

## Test 2 — `dropna()` a `subset`

### Zadání

Odstraň pouze řádky, kde chybí `product`.

### Řešení

```python
orders_clean = orders.dropna(
    subset=["product"]
)
```

### Krátce

`subset` určuje sloupce, podle kterých se rozhoduje o odstranění řádku.

---

## Test 3 — `fillna()` s textem

### Zadání

Vytvoř kopii `orders` a chybějící `region` nahraď `"Unknown"`.

### Řešení

```python
orders_filled = orders.copy()

orders_filled["region"] = (
    orders_filled["region"]
    .fillna("Unknown")
)
```

### Krátce

```python
orders.copy()
```

vytvoří samostatnou kopii DataFrame.

---

## Test 4 — `fillna()` mediánem

### Zadání

Chybějící `unit_price` nahraď mediánem.

### Řešení

```python
orders_filled = orders.copy()

orders_filled["unit_price"] = (
    orders_filled["unit_price"]
    .fillna(
        orders_filled["unit_price"].median()
    )
)
```

---

## Test 5 — Cleaning workflow

### Zadání

V kopii `orders`:

1. doplň `region` hodnotou `"Unknown"`,
2. doplň `unit_price` mediánem,
3. odstraň řádky bez `product`,
4. zkontroluj missing values.

### Řešení

```python
orders_clean = orders.copy()

orders_clean["region"] = (
    orders_clean["region"]
    .fillna("Unknown")
)

orders_clean["unit_price"] = (
    orders_clean["unit_price"]
    .fillna(
        orders_clean["unit_price"].median()
    )
)

orders_clean = orders_clean.dropna(
    subset=["product"]
)

print(orders_clean.isna().sum())
```

---

# Lekce 9 — Data Cleaning & Validation

## Test 1 — Chybějící hodnoty

### Zadání

```python
data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "product": ["Laptop", "Monitor", None, "Desk", "Mouse"],
    "quantity": [2, None, 1, 3, None],
    "unit_price": [25000, 7000, 15000, 12000, 800]
}

df = pd.DataFrame(data)
```

* zjisti missing values,
* odstraň řádky bez `product`,
* doplň `quantity` hodnotou `1`,
* výsledek ulož do `clean_df`.

### Řešení

```python
print(df.isna().sum())

df = df.dropna(
    subset=["product"]
)

df["quantity"] = df["quantity"].fillna(1)

clean_df = df
```

### Krátce

```text
1   → číslo
"1" → text
```

---

## Test 2 — Duplicity

### Zadání

```python
data = {
    "order_id": [1001, 1002, 1002, 1003, 1004, 1004],
    "product": ["Laptop", "Monitor", "Monitor", "Desk", "Mouse", "Mouse"],
    "quantity": [1, 2, 2, 1, 3, 3]
}

df = pd.DataFrame(data)
```

Zjisti duplicity, jejich počet a odstraň je.

### Řešení

```python
print(df[df.duplicated()])
print(df.duplicated().sum())

clean_df = df.drop_duplicates()
```

---

## Test 3 — Datové typy

### Zadání

Převeď textové hodnoty na vhodné číselné typy.

### Řešení

```python
df["order_id"] = df["order_id"].astype(int)
df["quantity"] = df["quantity"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)

print(df.dtypes)
```

### Krátce

```text
int   → celé číslo
float → desetinné číslo
```

> `astype()` zde bereme jako doplňkový příklad.

---

## Test 4 — Validace hodnot

### Zadání

Business pravidla:

```text
quantity > 0
unit_price > 0
```

Vyber všechny neplatné řádky.

### Řešení

```python
invalid_rows = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

### Krátce

Neplatný je řádek, kde selže alespoň jedno business pravidlo.

---

## Test 5 — Kompletní cleaning workflow

### Zadání

```python
data = {
    "order_id": [1001, 1002, 1002, 1003, 1004, 1005],
    "product": ["Laptop", "Monitor", "Monitor", None, "Desk", "Mouse"],
    "quantity": [2, 1, 1, 3, None, -2],
    "unit_price": [25000, 7000, 7000, 12000, 10000, 800]
}

df = pd.DataFrame(data)
```

Proveď:

1. kontrolu missing values,
2. odstranění duplicit,
3. odstranění řádků bez `product`,
4. doplnění `quantity = 1`,
5. validaci `quantity > 0`,
6. vytvoření `total`,
7. uložení do `clean_df`.

### Řešení

```python
print(df.isna().sum())

df = df.drop_duplicates()

df = df.dropna(
    subset=["product"]
)

df["quantity"] = df["quantity"].fillna(1)

df = df[
    df["quantity"] > 0
]

df["total"] = (
    df["quantity"]
    * df["unit_price"]
)

clean_df = df

print(clean_df)
clean_df.info()
```

### Krátce

```text
inspect
→ clean
→ validate
→ transform
→ verify
```

---

# Lekce 10 — Data Sources & Ingestion

## Test 1 — CSV: separator a encoding

### Zadání

Načti `sales.csv`:

* oddělovač `;`
* encoding `cp1250`

Potom zobraz `head()`, `shape`, `columns` a `info()`.

### Řešení

```python
import pandas as pd

df = pd.read_csv(
    "sales.csv",
    sep=";",
    encoding="cp1250"
)

print(df.head())
print(df.shape)
print(df.columns)
df.info()
```

### Krátce

```text
sep=       → oddělovač sloupců
encoding=  → způsob uložení znaků
```

UTF-8 většinou není nutné zadávat explicitně.

---

## Test 2 — JSON

### Zadání

Načti `sales.json` do `df` a proveď základní kontrolu.

### Řešení

```python
import pandas as pd

df = pd.read_json("sales.json")

print(df.head())
print(df.shape)
print(df.columns)
df.info()
```

### Krátce

```text
{ } → objekt
[ ] → pole / array
```

U jednoduchého JSON často:

```text
1 objekt → 1 řádek
1 klíč   → 1 sloupec
```

---

## Test 3 — Nested JSON

### Zadání

```python
data = [
    {
        "order_id": 1001,
        "product": "Laptop",
        "customer": {
            "name": "Jan Novák",
            "city": "Plzeň"
        }
    },
    {
        "order_id": 1002,
        "product": "Monitor",
        "customer": {
            "name": "Petra Malá",
            "city": "Praha"
        }
    }
]
```

Zplošti vnořený JSON do DataFrame.

### Řešení

```python
import pandas as pd

df = pd.json_normalize(data)
```

### Krátce

Výsledné sloupce mohou být:

```text
customer.name
customer.city
```

`json_normalize()` = flattening / zploštění JSON.

---

## Test 4 — SQLite + SQL

### Zadání

Z databáze:

```text
ecommerce_practice.db
```

načti z tabulky `orders` pouze řádky:

```sql
WHERE quantity > 2
```

### Řešení

```python
import pandas as pd
import sqlite3

connection = sqlite3.connect(
    "ecommerce_practice.db"
)

query = """
SELECT *
FROM orders
WHERE quantity > 2
"""

df = pd.read_sql(
    query,
    connection
)

connection.close()

print(df.head())
```

### Krátce

```text
sqlite3.connect() → připojení k databázi
pd.read_sql()     → SQL výsledek do DataFrame
close()           → zavření spojení
```

Po načtení `df` zůstává v paměti i po uzavření connection.

---

## Test 5 — API + raw data

### Zadání

Použij:

```text
https://jsonplaceholder.typicode.com/posts
```

Proveď:

1. GET request,
2. kontrolu `status_code`,
3. převod JSON odpovědi,
4. vytvoření `df_raw`,
5. vytvoření pracovní kopie `df`,
6. zobrazení prvních 5 řádků.

### Řešení

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.status_code)

data = response.json()

df_raw = pd.DataFrame(data)

df = df_raw.copy()

print(df.head())
```

### Krátce

```text
API
→ requests.get()
→ response
→ response.json()
→ Python data
→ DataFrame
```

```python
df_raw = pd.DataFrame(data)
df = df_raw.copy()
```

`df_raw` = původní načtená data
`df` = pracovní kopie

---

# Lekce 11 — `groupby()`, `agg()` a SQL logika

## Test 1 — Základní `groupby()`

### Zadání

Máš `df` se sloupci:

```text
category
total
```

Proveď:

1. seskupení podle `category`,
2. součet `total`,
3. `reset_index()`,
4. výsledek ulož do `sales_by_category`.

### Řešení

```python
sales_by_category = (
    df.groupby("category")["total"]
    .sum()
    .reset_index()
)
```

### Krátce

```text
groupby("category")
→ podle čeho seskupuji

["total"]
→ co agreguji

.sum()
→ jakou agregaci použiji
```

---

## Test 2 — Více agregací přes `agg()`

### Zadání

Podle `category` spočítej nad `total`:

* `sum`,
* `mean`,
* `max`.

Výsledek ulož do `category_summary`.

### Řešení

```python
category_summary = (
    df.groupby("category")["total"]
    .agg(["sum", "mean", "max"])
    .reset_index()
)
```

### Krátce

```python
.agg(["sum", "mean", "max"])
```

umožní provést více agregací najednou.

---

## Test 3 — Pojmenované agregace

### Zadání

Máš sloupce:

```text
category
total
quantity
```

Podle `category` vytvoř:

* `total_revenue` = součet `total`,
* `avg_order_value` = průměr `total`,
* `max_quantity` = maximum `quantity`.

### Řešení

```python
category_summary = (
    df.groupby("category")
    .agg(
        total_revenue=("total", "sum"),
        avg_order_value=("total", "mean"),
        max_quantity=("quantity", "max")
    )
    .reset_index()
)
```

### Krátce

Obecný vzorec:

```python
novy_nazev=("zdrojovy_sloupec", "agregace")
```

---

## Test 4 — WHERE vs. HAVING logika

### Zadání

Máš sloupce:

```text
category
quantity
total
```

Proveď:

1. ponech řádky s `quantity >= 2`,
2. seskup podle `category`,
3. spočítej součet `total`,
4. použij `reset_index()`,
5. ponech pouze kategorie s `total > 30000`.

Výsledek ulož do `high_value_categories`.

### Řešení

```python
filtered = df[
    df["quantity"] >= 2
]

grouped = (
    filtered.groupby("category")["total"]
    .sum()
    .reset_index()
)

high_value_categories = grouped[
    grouped["total"] > 30000
]
```

### Krátce

```text
filtr před groupby()
→ SQL WHERE

filtr po agregaci
→ SQL HAVING
```

Workflow:

```text
WHERE
→ GROUP BY
→ agregace
→ HAVING
```

---

## Test 5 — `groupby()` podle více sloupců

### Zadání

Máš sloupce:

```text
category
region
total
```

Proveď:

1. seskupení podle `category` a `region`,
2. součet `total`,
3. `reset_index()`,
4. výsledek ulož do `summary`.

### Řešení

```python
summary = (
    df.groupby(["category", "region"])["total"]
    .sum()
    .reset_index()
)
```

### Krátce

```python
df.groupby(["category", "region"])
```

znamená seskupení podle kombinace více sloupců.

---

# SQL vs. Pandas — rychlý přehled

```text
SQL                         pandas

GROUP BY category           groupby("category")

SUM(total)                  ["total"].sum()

AVG(total)                  ["total"].mean()

MAX(total)                  ["total"].max()

GROUP BY category, region   groupby(["category", "region"])

WHERE                       filtr před groupby()

HAVING                      filtr po agregaci
```

---

# Základní syntaxe

```python
df.groupby("A")["B"].sum()
```

```text
A → podle čeho seskupuji
B → co agreguji
sum → agregace
```

Více agregací:

```python
df.groupby("A")["B"].agg(
    ["sum", "mean", "max"]
)
```

Více skupin:

```python
df.groupby(["A", "B"])["C"].sum()
```

Pojmenované agregace:

```python
df.groupby("A").agg(
    metric_name=("B", "sum")
)
```
---

