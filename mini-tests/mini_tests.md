# Python for Data Analytics — minitesty

# Rychlý přehled Lekcí 6 až 16

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

Lekce 13
→ datetime, dt, strftime(), filtrování podle data

Lekce 14
→ práce s textem, .str, strip(), title(), lower(), upper(), contains(), startswith(), endswith(), replace(), split(), len()

Lekce 15
→ EDA, describe(), value_counts(), groupby(), IQR, outliers, corr(), histogram

Lekce 16
→ SDA, H0, H1, p-value, Pearson, t-test, chi-square, ANOVA, Mann-Whitney U, Shapiro-Wilk
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

---

# Lekce 13 — Datum a čas

## Test 1 — Převod na datetime a `year_month`

### Zadání

Převeď `order_date` z textu na `datetime` a vytvoř `year_month` ve formátu `2026_08`.

### Řešení

```python
orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

orders["year_month"] = (
    orders["order_date"]
    .dt.strftime("%Y_%m")
)
```

---

## Test 2 — Rozdíl mezi daty

### Zadání

Z `order_date` a `delivery_date` vytvoř počet dní dodání.

### Řešení

```python
orders["delivery_days"] = (
    orders["delivery_date"]
    - orders["order_date"]
).dt.days
```

---

## Test 3 — Filtrování mezi daty

### Zadání

Vyber objednávky mezi `2026-08-05` a `2026-08-15` bez zahrnutí hranic.

### Řešení

```python
filtered_orders = orders[
    orders["order_date"].between(
        "2026-08-05",
        "2026-08-15",
        inclusive="neither"
    )
]
```

---

## Test 4 — Den v týdnu

### Zadání

Vytvoř `day_name` s českým názvem dne.

### Řešení

```python
orders["day_name"] = (
    orders["order_date"]
    .dt.day_name(
        locale="cs_CZ"
    )
)
```

---

## Test 5 — Měsíční revenue

### Zadání

Vytvoř `year_month` a spočítej celkové `revenue` za každý měsíc.

Použij DataFrame bez `reset_index()`.

### Řešení

```python
orders["year_month"] = (
    orders["order_date"]
    .dt.strftime("%Y_%m")
)

monthly_sales = (
    orders.groupby(
        "year_month",
        as_index=False
    )["revenue"]
    .sum()
)
```

---

## Test 6 — Kombinovaný úkol

### Zadání

1. vytvoř `delivery_days`,
2. vyber objednávky ze srpna 2026,
3. seřaď je podle `delivery_days` sestupně,
4. zobraz pouze:

```text
order_id
order_date
delivery_days
revenue
```

### Řešení

```python
orders["delivery_days"] = (
    orders["delivery_date"]
    - orders["order_date"]
).dt.days

august_orders = orders[
    orders["order_date"].between(
        "2026-08-01",
        "2026-08-31"
    )
]

august_orders = august_orders.sort_values(
    by="delivery_days",
    ascending=False
)

result = august_orders[
    [
        "order_id",
        "order_date",
        "delivery_days",
        "revenue"
    ]
]

print(result)
```

---

# Lekce 14 — Práce s textem v Pandas

## Test 1 — `strip()` a `title()`

### Zadání

Ve sloupci `customer_name`:

- odstraň mezery na začátku a konci,
- uprav jména do formátu `Jan Novák`.

### Řešení

```python
customers["customer_name"] = (
    customers["customer_name"]
    .str.strip()
    .str.title()
)
```

---

## Test 2 — `lower()`

### Zadání

Převeď celý sloupec `email` na malá písmena.

### Řešení

```python
customers["email"] = (
    customers["email"]
    .str.lower()
)
```

---

## Test 3 — `endswith()`

### Zadání

Vyber pouze zákazníky, jejichž email končí na `gmail.com`.

### Řešení

```python
g_customers = customers[
    customers["email"].str.endswith(
        "gmail.com",
        na=False
    )
]
```

---

## Test 4 — `split()`

### Zadání

Rozděl `email` podle `@` do sloupců:

```text
email_name
email_domain
```

### Řešení

```python
customers[["email_name", "email_domain"]] = (
    customers["email"]
    .str.split(
        "@",
        expand=True
    )
)
```

---

## Test 5 — `len()`

### Zadání

Vytvoř sloupec `email_length` s počtem znaků v emailu.

### Řešení

```python
customers["email_length"] = (
    customers["email"]
    .str.len()
)
```

---


# Lekce 15 — EDA (Exploratory Data Analysis)

## Test 1 — `describe()` a interpretace

### Zadání

Zobraz základní statistický přehled pro `revenue`.

Potom vysvětli, co může naznačit výraznější rozdíl mezi průměrem a mediánem.

### Řešení

```python
print(
    sales["revenue"].describe()
)
```

### Krátce

```text
mean výrazně > median
→ může upozornit na right-skewed distribuci
→ případně na vysoký outlier

mean výrazně < median
→ může upozornit na left-skewed distribuci
```

Rozdíl mezi průměrem a mediánem je varovný signál, ne automatický důkaz outlieru.

---

## Test 2 — Počet objednávek podle regionu

### Zadání

Zjisti počet objednávek v jednotlivých regionech.

### Řešení

```python
orders_summary = (
    sales.groupby(
        "region",
        as_index=False
    )["order_id"]
    .count()
)
```

### Krátce

```text
count()
→ počítá neprázdné hodnoty konkrétního sloupce

size()
→ počítá řádky ve skupině

value_counts()
→ počítá četnost hodnot ve vybraném sloupci
```

Pokud `order_id` obsahuje `NaN`, může `count()` dát jiný výsledek než počet řádků.

Pro počet řádků ve skupině:

```python
orders_summary = (
    sales.groupby(
        "region",
        as_index=False
    )
    .size()
)
```

---

## Test 3 — Agregace podle regionu

### Zadání

Pro každý `region` spočítej:

- počet objednávek,
- celkové `revenue`,
- průměrné `revenue`.

### Řešení

```python
region_summary = (
    sales.groupby(
        "region",
        as_index=False
    )
    .agg(
        orders_count=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean")
    )
)
```

### Krátce

```text
count
→ počet neprázdných order_id

sum
→ celkové revenue

mean
→ průměrné revenue
```

---

## Test 4 — IQR a outliers

### Zadání

Pro `revenue` spočítej:

- `Q1`,
- `Q3`,
- `IQR`,
- dolní hranici,
- horní hranici,

a vyber potenciální outliery.

### Řešení

```python
q1 = sales["revenue"].quantile(0.25)
q3 = sales["revenue"].quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = sales[
    (sales["revenue"] < lower_bound)
    | (sales["revenue"] > upper_bound)
]
```

### Krátce

```text
Q1
→ 25. percentil

Q3
→ 75. percentil

IQR
→ Q3 - Q1

mimo hranice
→ potenciální outlier
→ ne automaticky chyba
```

---

## Test 5 — Korelace

### Zadání

Zjisti korelaci mezi:

```text
quantity
revenue
```

Potom interpretuj hodnotu kolem `0.92`.

### Řešení

```python
correlation = sales[
    ["quantity", "revenue"]
].corr()
```

### Krátce

```text
0.92
→ velmi silná pozitivní lineární korelace
→ proměnné mají tendenci růst společně
```

Důležité:

```text
korelace
≠
kauzalita

silná korelace
≠
přímá úměra
```

Vhodná formulace:

```text
Mezi quantity a revenue existuje
velmi silný pozitivní vztah.
```

---

## Test 6 — Distribuce

### Zadání

Vytvoř histogram `revenue` s pěti intervaly a zobraz ho.

Potom interpretuj situaci:

```text
většina hodnot vlevo
+
dlouhý ocas doprava
```

### Řešení

```python
import matplotlib.pyplot as plt

sales["revenue"].hist(
    bins=5
)

plt.show()
```

### Krátce

```text
většina hodnot vlevo
+
dlouhý ocas doprava

→ right-skewed distribuce
→ často mean > median
```

---

# Lekce 16 — SDA / praktické statistické testy

## Test 1 — Výběr testu: 2 skupiny + číslo

### Zadání

Chceš zjistit:

```text
Liší se průměrné revenue mezi B2B a B2C zákazníky?
```

Jaký test použiješ?

### Řešení

```text
t-test
```

### Krátce

```text
2 skupiny + číselná proměnná
→ t-test
```

---

## Test 2 — Výběr testu: 2 kategorie

### Zadání

Chceš zjistit:

```text
Souvisí region zákazníka s customer_type?
```

Jaký test použiješ?

### Řešení

```text
chi-square
```

### Krátce

```text
2 kategoriální proměnné
→ chi-square
```

---

## Test 3 — Výběr testu: 2 čísla

### Zadání

Chceš zjistit:

```text
Souvisí quantity s revenue?
```

Jaký test použiješ?

### Řešení

```text
Pearson
```

### Krátce

```text
2 číselné proměnné
→ Pearsonova korelace
```

---

## Test 4 — Výběr testu: 3+ skupiny

### Zadání

Chceš zjistit:

```text
Liší se průměrné revenue mezi Prahou, Brnem a Ostravou?
```

Jaký test použiješ?

### Řešení

```text
ANOVA
```

### Krátce

```text
3+ skupiny + číselná proměnná
→ ANOVA
```

---

## Test 5 — Outliery / problematické rozložení

### Zadání

Máš 2 skupiny zákazníků a `revenue` obsahuje výrazné outliery.

Chceš porovnat, jestli se skupiny liší.

Jaký test použiješ?

### Řešení

```text
Mann–Whitney U
```

### Krátce

```text
2 skupiny + outliery / nehezké rozložení
→ Mann–Whitney U
```

---

## Test 6 — Normalita

### Zadání

Chceš zjistit:

```text
Jsou hodnoty revenue přibližně normálně rozložené?
```

Jaký test použiješ?

### Řešení

```text
Shapiro–Wilk
```

### Krátce

```text
kontrola normality
→ Shapiro–Wilk
```

---

## Test 7 — p-value pod 0.05

### Zadání

Výsledek testu je:

```text
p-value = 0.03
```

Co uděláš s H0?

### Řešení

```text
0.03 < 0.05
→ H0 zamítáme
```

### Krátce

```text
p-value < 0.05
→ výsledek je statisticky významný
→ máme důvod zamítnout H0
```

---

## Test 8 — p-value nad 0.05

### Zadání

Výsledek testu je:

```text
p-value = 0.27
```

Co uděláš s H0?

### Řešení

```text
0.27 > 0.05
→ H0 nezamítáme
```

### Důležité

To neznamená:

```text
H0 je pravda
nebo
H1 je nepravda
```

Znamená to jen:

```text
nemáme dost důkazů proti H0
```

---

