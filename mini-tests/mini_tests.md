# Python for Data Analytics — minitesty

# Rychlý přehled Lekcí 6 až 12

```text
Lekce 6
→ Pandas základy

Lekce 7
→ filtrování, loc, iloc

Lekce 8
→ missing values

Lekce 9
→ cleaning a validation

Lekce 10
→ CSV, JSON, SQL, API

Lekce 11
→ groupby(), agg(), GROUP BY, HAVING

Lekce 12
→ merge(), JOIN, validate, suffixes
```

---

# Lekce 6 — Pandas základy

## Test 1 — Načtení a kontrola dat

### Zadání

Načti `ecommerce_sales_analysis.csv` do `df` a zobraz:

- prvních 5 řádků,
- rozměry datasetu,
- názvy sloupců,
- základní informace.

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

```text
head()  → první řádky
shape   → počet řádků a sloupců
columns → názvy sloupců
info()  → struktura a datové typy
```

---

## Test 2 — Nový sloupec a agregace

### Zadání

Vytvoř `total = quantity × unit_price` a vypočítej součet, průměr, maximum a minimum.

### Řešení

```python
df["total"] = df["quantity"] * df["unit_price"]

total_revenue = df["total"].sum()
avg_order = df["total"].mean()
max_order_value = df["total"].max()
min_order_value = df["total"].min()
```

---

## Test 3 — Filtrování

### Zadání

Vyber objednávky nad průměr `total` a spočítej tržby kategorie `Furniture`.

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
```

---

## Test 4 — Řazení

### Zadání

Seřaď dataset podle `total` sestupně.

### Řešení

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)

print(sorted_orders.head())
```

---

## Test 5 — Workflow

### Zadání

Načti CSV, vytvoř `total`, vyber objednávky nad průměrem, seřaď je a exportuj do CSV.

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
    "above_average_orders.csv",
    index=False
)
```

---

# Lekce 7 — Filtrování, `loc`, `iloc`

## Test 1 — AND

### Zadání

Vyber `Furniture` s `total > 15000`.

### Řešení

```python
furniture_high_value = df[
    (df["category"] == "Furniture")
    & (df["total"] > 15000)
]
```

---

## Test 2 — OR a NOT

### Zadání

Vyber:

- `quantity >= 4` nebo `total > 20000`,
- vše mimo `Electronics`.

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

---

## Test 4 — `loc`

### Řešení

```python
high_value_summary = df.loc[
    df["total"] > 10000,
    ["order_id", "product", "category", "total"]
]
```

---

## Test 5 — `iloc`

### Řešení

```python
first_five_selected = df.iloc[
    0:5,
    1:5
]
```

---

# Lekce 8 — Missing values

## Test 1 — Kontrola

```python
print(orders.isna().sum())
```

---

## Test 2 — `dropna()`

```python
orders_clean = orders.dropna(
    subset=["product"]
)
```

---

## Test 3 — `fillna()` textem

```python
orders_filled = orders.copy()

orders_filled["region"] = (
    orders_filled["region"]
    .fillna("Unknown")
)
```

---

## Test 4 — `fillna()` mediánem

```python
orders_filled["unit_price"] = (
    orders_filled["unit_price"]
    .fillna(
        orders_filled["unit_price"].median()
    )
)
```

---

## Test 5 — Cleaning workflow

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

## Test 1 — Missing values

```python
print(df.isna().sum())

df = df.dropna(
    subset=["product"]
)

df["quantity"] = df["quantity"].fillna(1)

clean_df = df
```

---

## Test 2 — Duplicity

```python
print(df[df.duplicated()])
print(df.duplicated().sum())

clean_df = df.drop_duplicates()
```

---

## Test 3 — Datové typy

```python
df["order_id"] = df["order_id"].astype(int)
df["quantity"] = df["quantity"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)

print(df.dtypes)
```

---

## Test 4 — Validace hodnot

```python
invalid_rows = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

---

## Test 5 — Cleaning workflow

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
```

---

# Lekce 10 — Data Sources & Ingestion

## Test 1 — CSV

```python
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

---

## Test 2 — JSON

```python
df = pd.read_json("sales.json")

print(df.head())
df.info()
```

---

## Test 3 — Nested JSON

```python
df = pd.json_normalize(data)
```

---

## Test 4 — SQLite + SQL

```python
import sqlite3
import pandas as pd

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
```

---

## Test 5 — API + raw data

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

---

# Lekce 11 — `groupby()` a `agg()`

## Test 1 — Základní `groupby()`

```python
sales_by_category = (
    df.groupby("category")["total"]
    .sum()
    .reset_index()
)
```

---

## Test 2 — Více agregací

```python
category_summary = (
    df.groupby("category")["total"]
    .agg(["sum", "mean", "max"])
    .reset_index()
)
```

---

## Test 3 — Pojmenované agregace

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

---

## Test 4 — WHERE vs. HAVING

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

---

## Test 5 — Více grouping sloupců

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

# Lekce 12 — `merge()` a JOIN logika

## Test 1 — Základní `merge()`

### Zadání

Spoj `orders` s `customers` podle `customer_id`.

Zachovej všechny objednávky a ověř vztah `many_to_one`.

### Řešení

```python
orders_with_customers = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)
```

---

## Test 2 — Různé názvy klíče

### Zadání

Spoj:

```text
orders.customer_id
customers.id
```

### Řešení

```python
result = orders.merge(
    customers,
    left_on="customer_id",
    right_on="id",
    how="left",
    validate="many_to_one"
)
```

---

## Test 3 — `suffixes`

### Zadání

Obě tabulky obsahují `region`.

Použij suffixy:

```text
_order
_customer
```

### Řešení

```python
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    suffixes=(
        "_order",
        "_customer"
    ),
    validate="many_to_one"
)
```

---

## Test 4 — Kontrola po merge

### Zadání

Zjisti missing values a doplň chybějící `customer_name` a `region` hodnotou `"Unknown"`.

### Řešení

```python
print(
    orders_with_customers
    .isna()
    .sum()
)

orders_with_customers["customer_name"] = (
    orders_with_customers["customer_name"]
    .fillna("Unknown")
)

orders_with_customers["region"] = (
    orders_with_customers["region"]
    .fillna("Unknown")
)
```

---

## Test 5 — Merge tří tabulek

### Zadání

Spoj:

```text
orders
→ customers
→ products
```

### Řešení

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