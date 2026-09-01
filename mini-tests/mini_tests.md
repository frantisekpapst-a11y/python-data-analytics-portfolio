# Python for Data Analytics — minitesty

# Rychlý přehled Lekcí 6 až 20

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

Lekce 17

→ NumPy pro datovou analytiku, np.where(), np.select(), np.nan, array, dtype, axis, propojení NumPy a Pandas

Lekce 18

→ Matplotlib, Pandas plotting, line, bar, scatter, histogram, boxplot, pie, základní formátování grafů

Lekce 19

→ Plotly, interaktivní line, bar, scatter a pie chart, hover, legenda, více sérií, melt() a long formát

Lekce 20

→ Excel / Power Query vs. Pandas, Python in Excel, merge(), pd.concat(), Merge / Append, wide vs. long format, melt(), pivot(), xl()

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

---

## Test 2 — Nový sloupec a agregace

### Zadání

Vytvoř:

```text
total = quantity × unit_price
```

Potom vypočítej:

- součet,
- průměr,
- maximum,
- minimum.

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

Vyber řádky, kde:

```text
category = "Furniture"

a zároveň

total > 15000
```

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

```text
quantity >= 4

nebo

total > 20000
```

Potom vytvoř druhý výběr obsahující vše mimo kategorii `Electronics`.

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

Vyber produkty:

```text
Laptop
Desk
Office Chair
```

Potom z tohoto výběru ponech pouze řádky, kde:

```text
total je mezi 15000 a 30000
```

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

### Zadání

Pomocí `loc` vyber řádky s:

```text
total > 10000
```

a zobraz pouze sloupce:

```text
order_id
product
category
total
```

### Řešení

```python
high_value_summary = df.loc[
    df["total"] > 10000,
    ["order_id", "product", "category", "total"]
]
```

---

## Test 5 — `iloc`

### Zadání

Pomocí `iloc` vyber:

- prvních 5 řádků,
- sloupce na pozicích 1 až 4.

### Řešení

```python
first_five_selected = df.iloc[
    0:5,
    1:5
]
```

---

# Lekce 8 — Missing values

## Test 1 — Kontrola missing values

### Zadání

Zjisti počet chybějících hodnot v jednotlivých sloupcích DataFrame `orders`.

### Řešení

```python
print(
    orders.isna().sum()
)
```

---

## Test 2 — `dropna()`

### Zadání

Odstraň řádky, ve kterých chybí hodnota ve sloupci `product`.

### Řešení

```python
orders_clean = orders.dropna(
    subset=["product"]
)
```

---

## Test 3 — `fillna()` textem

### Zadání

Vytvoř kopii `orders` a chybějící hodnoty ve sloupci `region` nahraď textem:

```text
Unknown
```

### Řešení

```python
orders_filled = orders.copy()

orders_filled["region"] = (
    orders_filled["region"]
    .fillna("Unknown")
)
```

---

## Test 4 — `fillna()` mediánem

### Zadání

Chybějící hodnoty ve sloupci `unit_price` doplň mediánem tohoto sloupce.

### Řešení

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

### Zadání

Vytvoř kopii `orders` a proveď:

1. doplnění `region` hodnotou `"Unknown"`,
2. doplnění `unit_price` mediánem,
3. odstranění řádků bez `product`,
4. závěrečnou kontrolu missing values.

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

print(
    orders_clean.isna().sum()
)
```

---

# Lekce 9 — Data Cleaning & Validation

## Test 1 — Missing values

### Zadání

Zjisti missing values.

Potom:

- odstraň řádky bez `product`,
- doplň chybějící `quantity` hodnotou `1`,
- výsledek ulož do `clean_df`.

### Řešení

```python
print(
    df.isna().sum()
)

df = df.dropna(
    subset=["product"]
)

df["quantity"] = df["quantity"].fillna(1)

clean_df = df
```

---

## Test 2 — Duplicity

### Zadání

Zjisti:

- které řádky jsou duplicitní,
- kolik duplicit dataset obsahuje.

Potom duplicity odstraň.

### Řešení

```python
print(
    df[df.duplicated()]
)

print(
    df.duplicated().sum()
)

clean_df = df.drop_duplicates()
```

---

## Test 3 — Datové typy

### Zadání

Převeď:

```text
order_id
→ int

quantity
→ int

unit_price
→ float
```

Potom zobraz datové typy.

### Řešení

```python
df["order_id"] = df["order_id"].astype(int)
df["quantity"] = df["quantity"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)

print(df.dtypes)
```

---

## Test 4 — Validace hodnot

### Zadání

Najdi řádky, kde:

```text
quantity <= 0

nebo

unit_price <= 0
```

### Řešení

```python
invalid_rows = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

---

## Test 5 — Cleaning workflow

### Zadání

Proveď základní cleaning workflow:

1. kontrola missing values,
2. odstranění duplicit,
3. odstranění řádků bez `product`,
4. doplnění `quantity`,
5. odstranění neplatného `quantity`,
6. vytvoření `total`,
7. uložení výsledku do `clean_df`.

### Řešení

```python
print(
    df.isna().sum()
)

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

### Zadání

Načti `sales.csv`.

Použij:

```text
oddělovač ;
encoding cp1250
```

Potom proveď základní kontrolu dat.

### Řešení

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

### Zadání

Načti soubor:

```text
sales.json
```

Potom zobraz první řádky a informace o DataFrame.

### Řešení

```python
df = pd.read_json(
    "sales.json"
)

print(df.head())

df.info()
```

---

## Test 3 — Nested JSON

### Zadání

Máš nested JSON uložený v proměnné `data`.

Převeď ho na plochý DataFrame.

### Řešení

```python
df = pd.json_normalize(data)
```

---

## Test 4 — SQLite + SQL

### Zadání

Připoj se k databázi:

```text
ecommerce_practice.db
```

Pomocí SQL načti z tabulky `orders` pouze řádky, kde:

```text
quantity > 2
```

Výsledek načti do DataFrame a připojení uzavři.

### Řešení

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

### Zadání

Načti data z API:

```text
https://jsonplaceholder.typicode.com/posts
```

Potom:

1. zobraz status code,
2. převeď odpověď na JSON,
3. vytvoř `df_raw`,
4. vytvoř pracovní kopii `df`,
5. zobraz první řádky.

### Řešení

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(
    response.status_code
)

data = response.json()

df_raw = pd.DataFrame(data)

df = df_raw.copy()

print(
    df.head()
)
```

---

# Lekce 11 — `groupby()` a `agg()`

## Test 1 — Základní `groupby()`

### Zadání

Spočítej celkové `total` pro každou kategorii.

Výsledek vrať jako běžný DataFrame.

### Řešení

```python
sales_by_category = (
    df.groupby("category")["total"]
    .sum()
    .reset_index()
)
```

---

## Test 2 — Více agregací

### Zadání

Pro každou kategorii spočítej z `total`:

```text
sum
mean
max
```

### Řešení

```python
category_summary = (
    df.groupby("category")["total"]
    .agg([
        "sum",
        "mean",
        "max"
    ])
    .reset_index()
)
```

---

## Test 3 — Pojmenované agregace

### Zadání

Pro každou kategorii vytvoř:

```text
total_revenue
→ součet total

avg_order_value
→ průměr total

max_quantity
→ maximum quantity
```

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

---

## Test 4 — WHERE vs. HAVING

### Zadání

Nejdříve vyber pouze řádky, kde:

```text
quantity >= 2
```

Potom:

1. seskup podle `category`,
2. spočítej `total`,
3. ponech pouze kategorie s `total > 30000`.

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

---

## Test 5 — Více grouping sloupců

### Zadání

Spočítej celkové `total` podle kombinace:

```text
category
region
```

### Řešení

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

Zachovej všechny objednávky.

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

Zjisti missing values a doplň chybějící `customer_name` a `region` hodnotou:

```text
Unknown
```

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

Použij `left` merge a validaci `many_to_one`.

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

Převeď `order_date` z textu na `datetime` a vytvoř `year_month` ve formátu:

```text
2026_08
```

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

Vyber objednávky mezi:

```text
2026-08-05

a

2026-08-15
```

bez zahrnutí hranic.

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

Vyber pouze zákazníky, jejichž email končí na:

```text
gmail.com
```

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

Potom interpretuj situaci:

```text
mean výrazně > median
```

a:

```text
mean výrazně < median
```

### Řešení

```python
print(
    sales["revenue"].describe()
)
```

```text
mean výrazně > median

→ může upozornit na right-skewed distribuci
→ případně na vysoký outlier

mean výrazně < median

→ může upozornit na left-skewed distribuci
```

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

Alternativa pro počet řádků:

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

---

## Test 5 — Korelace

### Zadání

Zjisti korelaci mezi:

```text
quantity

revenue
```

Potom interpretuj hodnotu kolem:

```text
0.92
```

### Řešení

```python
correlation = sales[
    ["quantity", "revenue"]
].corr()
```

```text
0.92

→ velmi silná pozitivní lineární korelace

→ proměnné mají tendenci růst společně

→ neznamená automaticky kauzalitu
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

---

## Test 5 — Outliery / problematické rozložení

### Zadání

Máš dvě skupiny zákazníků a `revenue` obsahuje výrazné outliery.

Chceš porovnat, jestli se skupiny liší.

Jaký test použiješ?

### Řešení

```text
Mann–Whitney U
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

→ výsledek je statisticky významný
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

→ nemáme dost důkazů proti H0
```

---

# Lekce 17 — NumPy pro datovou analytiku

## Test 1 — `np.where()` v Pandas workflow

### Zadání

Máš DataFrame:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "sales": [1200, 1800, 950, 2200, 1500]
})
```

Vytvoř nový sloupec `sales_level`.

Pravidla:

```text
sales >= 1500

→ "High"

jinak

→ "Low"
```

Použij `np.where()`.

### Řešení

```python
df["sales_level"] = np.where(
    df["sales"] >= 1500,
    "High",
    "Low"
)
```

---

## Test 2 — `np.where()` podle profitu

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "profit": [200, 450, 700, 350, 900]
})
```

Vytvoř nový sloupec `profit_level`.

Pravidla:

```text
profit >= 500

→ "Good"

jinak

→ "Low"
```

Použij `np.where()`.

### Řešení

```python
df["profit_level"] = np.where(
    df["profit"] >= 500,
    "Good",
    "Low"
)
```

---

## Test 3 — `np.select()` pro více kategorií

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "sales": [900, 1300, 1700, 2200]
})
```

Vytvoř nový sloupec `sales_category`.

Pravidla:

```text
sales >= 1800

→ "High"

sales >= 1200

→ "Medium"

jinak

→ "Low"
```

Použij `np.select()`.

### Řešení

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

---

## Test 4 — Výběr mezi `np.where()` a `np.select()`

### Zadání

Chceš vytvořit nový sloupec podle pravidla:

```text
revenue >= 10000

→ "High"

jinak

→ "Low"
```

Co je vhodnější?

### Řešení

```text
np.where()
```

---

## Test 5 — Výběr nástroje v běžné datové analýze

### Zadání

Máš tabulková business data obsahující:

```text
customer_id

region

sales

profit

date
```

Chceš provádět:

```text
groupby

merge

missing values

filtry

agregace
```

Použiješ jako hlavní nástroj Pandas nebo NumPy?

### Řešení

```text
Pandas
```

---

## Test 6 — Kdy použít NumPy uvnitř Pandas

### Zadání

Chceš v Pandas DataFrame vytvořit nový kategoriální sloupec podle několika podmínek.

Co může být praktičtější než několik po sobě jdoucích `loc` podmínek?

### Řešení

```text
np.select()
```

---

# Lekce 18 — Matplotlib a Pandas plotting

## Test 1 — Bar chart v Matplotlib

### Zadání

Máš DataFrame:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "region": ["Praha", "Brno", "Plzeň", "Ostrava"],
    "revenue": [520000, 410000, 465000, 350000]
})
```

Seřaď data podle `revenue` sestupně.

Vytvoř bar chart:

```text
region

→ osa X

revenue

→ osa Y
```

Přidej tučný nadpis:

```text
Tržby podle regionu
```

### Řešení

```python
df = df.sort_values(
    by="revenue",
    ascending=False
)

plt.bar(
    df["region"],
    df["revenue"]
)

plt.title(
    "Tržby podle regionu",
    fontweight="bold"
)

plt.show()
```

---

## Test 2 — Line chart v Matplotlib

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "month": [
        "2026-01",
        "2026-02",
        "2026-03",
        "2026-04"
    ],
    "revenue": [
        120000,
        135000,
        128000,
        150000
    ]
})
```

Vytvoř line chart s body.

Použij:

```text
month

→ osa X

revenue

→ osa Y
```

### Řešení

```python
plt.plot(
    df["month"],
    df["revenue"],
    marker="o"
)

plt.title(
    "Měsíční tržby"
)

plt.show()
```

---

## Test 3 — Scatter plot a trendová čára

### Zadání

Máš DataFrame:

```python
import numpy as np

df = pd.DataFrame({
    "ad_spend": [10, 15, 20, 25, 30, 35],
    "revenue": [80, 110, 150, 170, 210, 250]
})
```

Vytvoř scatter plot.

Potom vytvoř lineární trend pomocí:

```text
np.polyfit()

np.poly1d()
```

a trendovou čáru přidej do grafu.

### Řešení

```python
plt.scatter(
    df["ad_spend"],
    df["revenue"]
)

trend = np.polyfit(
    df["ad_spend"],
    df["revenue"],
    1
)

trend_line = np.poly1d(trend)

plt.plot(
    df["ad_spend"],
    trend_line(df["ad_spend"])
)

plt.show()
```

---

## Test 4 — Histogram

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "resolution_hours": [
        2, 3, 4, 5, 6, 7, 8, 8,
        9, 10, 12, 14, 18, 22, 30
    ]
})
```

Vytvoř histogram.

Použij intervaly:

```text
0–5

5–10

10–15

15–20

20–25

25–30

30–35
```

### Řešení

```python
plt.hist(
    df["resolution_hours"],
    bins=[
        0,
        5,
        10,
        15,
        20,
        25,
        30,
        35
    ]
)

plt.show()
```

---

## Test 5 — Pandas plotting

### Zadání

Máš DataFrame obsahující:

```text
month

revenue
```

Vytvoř rychlý line chart přímo pomocí Pandas.

### Řešení

```python
df.plot(
    x="month",
    y="revenue"
)

plt.show()
```

---

# Lekce 19 — Plotly

## Test 1 — Line chart

### Zadání

Máš DataFrame:

```python
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "month": [
        "2026-01",
        "2026-02",
        "2026-03",
        "2026-04"
    ],
    "revenue": [
        120000,
        135000,
        128000,
        150000
    ]
})
```

Vytvoř interaktivní line chart.

Použij:

```text
month

→ osa X

revenue

→ osa Y
```

Zobraz body a přidej nadpis:

```text
Měsíční tržby
```

### Řešení

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

---

## Test 2 — Bar chart

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "segment": [
        "B2B",
        "B2C",
        "Partner"
    ],
    "revenue": [
        520000,
        350000,
        130000
    ]
})
```

Vytvoř interaktivní bar chart.

Použij:

```text
segment

→ osa X

revenue

→ osa Y
```

Přidej nadpis:

```text
Tržby podle segmentu
```

### Řešení

```python
fig = px.bar(
    df,
    x="segment",
    y="revenue",
    title="Tržby podle segmentu"
)

fig.show()
```

---

## Test 3 — Scatter plot

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "ad_spend": [10, 15, 20, 25, 30, 35],
    "revenue": [80, 110, 150, 170, 210, 250]
})
```

Vytvoř interaktivní scatter plot.

Použij:

```text
ad_spend

→ osa X

revenue

→ osa Y
```

### Řešení

```python
fig = px.scatter(
    df,
    x="ad_spend",
    y="revenue",
    title="Vztah marketingových nákladů a tržeb"
)

fig.show()
```

---

## Test 4 — Pie chart

### Zadání

Máš DataFrame:

```python
df = pd.DataFrame({
    "segment": [
        "B2B",
        "B2C",
        "Partner"
    ],
    "revenue": [
        520000,
        350000,
        130000
    ]
})
```

Vytvoř interaktivní pie chart.

Použij:

```text
segment

→ názvy výsečí

revenue

→ hodnoty
```

Přidej nadpis:

```text
Podíl tržeb podle segmentu
```

### Řešení

```python
fig = px.pie(
    df,
    names="segment",
    values="revenue",
    title="Podíl tržeb podle segmentu"
)

fig.show()
```

---

## Test 5 — Více line sérií

### Zadání

Máš DataFrame ve wide formátu:

```python
df = pd.DataFrame({
    "month": [
        "2026-01",
        "2026-02",
        "2026-03"
    ],
    "B2B": [
        120,
        135,
        150
    ],
    "B2C": [
        90,
        95,
        110
    ],
    "Partner": [
        40,
        45,
        50
    ]
})
```

Převeď data pomocí `melt()` do long formátu.

Výsledné sloupce:

```text
month

segment

revenue
```

Potom vytvoř Plotly line chart.

Použij:

```text
month

→ osa X

revenue

→ osa Y

segment

→ jednotlivé série
```

Zobraz body.

### Řešení

```python
df_long = df.melt(
    id_vars="month",
    var_name="segment",
    value_name="revenue"
)

fig = px.line(
    df_long,
    x="month",
    y="revenue",
    color="segment",
    markers=True
)

fig.show()
```

# Lekce 20 — Excel / Power Query vs. Pandas

## Test 1 — Výběr vhodného nástroje

### Zadání

Máš malý dataset v Excelu.

Potřebuješ jednorázově:

```text
vytvořit nový sloupec total

→ quantity * unit_price

spočítat tržby podle produktu

seřadit výsledek sestupně
```

Co je v tomto případě nejpraktičtější?

```text
A) Excel

B) Power Query

C) Pandas
```

### Řešení

```text
A) Excel
```

```text
malý dataset
+
jednoduchý výpočet
+
jednorázová analýza

→ Excel
```

---

## Test 2 — Opakovaný workflow

### Zadání

Každý měsíc dostaneš nový export se stejnou strukturou.

Potřebuješ pokaždé:

```text
načíst data

změnit datové typy

odstranit nepotřebné sloupce

spojit data s druhou tabulkou

aktualizovat výsledek
```

Co je vhodnější?

```text
A) ruční Excel

B) Power Query

C) ruční kopírování dat
```

### Řešení

```text
B) Power Query
```

Power Query umožňuje transformační kroky nastavit jednou a potom použít:

```text
Data

→ Aktualizovat vše
```

---

## Test 3 — `merge()` vs. `concat()`

### Zadání

Máš dvě tabulky:

```text
orders

order_id
customer_id
revenue
```

a:

```text
customers

customer_id
customer_name
region
```

Chceš k objednávkám doplnit:

```text
customer_name

region
```

Co použiješ v Pandas?

```text
A) pd.concat()

B) merge()
```

### Řešení

```text
B) merge()
```

```python
result = orders.merge(
    customers,
    on="customer_id",
    how="left"
)
```

---

## Test 4 — `pd.concat()`

### Zadání

Máš dvě tabulky se stejnou strukturou:

```text
orders_january

order_id
customer_id
revenue
```

a:

```text
orders_february

order_id
customer_id
revenue
```

Chceš únorová data přidat pod lednová.

Co použiješ?

### Řešení

```python
result = pd.concat(
    [
        orders_january,
        orders_february
    ],
    ignore_index=True
)
```

---

## Test 5 — `ignore_index=True`

### Zadání

Máš dva DataFrame:

```python
orders_1 = pd.DataFrame({
    "order_id": [1, 2],
    "revenue": [12000, 8000]
})

orders_2 = pd.DataFrame({
    "order_id": [3, 4],
    "revenue": [15000, 7000]
})
```

Spojíš je:

```python
result = pd.concat(
    [
        orders_1,
        orders_2
    ],
    ignore_index=True
)
```

Co udělá:

```python
ignore_index=True
```

### Řešení

```text
vytvoří nový souvislý index
```

Výsledek:

```text
0
1
2
3
```

Bez `ignore_index=True` by se mohly zachovat původní indexy:

```text
0
1
0
1
```

---

## Test 6 — `loc` vs. `iloc`

### Zadání

Jaký je rozdíl mezi:

```python
df.loc[0]
```

a:

```python
df.iloc[0]
```

### Řešení

```text
loc

→ pracuje podle labelu / hodnoty indexu

iloc

→ pracuje podle číselné pozice
```

```python
df.loc[0]
```

→ řádek s indexem `0`

```python
df.iloc[0]
```

→ první řádek v pořadí

---

## Test 7 — Wide format

### Zadání

Máš tabulku:

```text
month     B2B   B2C   Partner

2026-01   120    90      40
2026-02   135    95      45
```

Je to:

```text
A) wide format

B) long format
```

### Řešení

```text
A) wide format
```

Kategorie:

```text
B2B
B2C
Partner
```

jsou uložené jako samostatné sloupce.

---

## Test 8 — Wide → Long pomocí `melt()`

### Zadání

Máš:

```python
df = pd.DataFrame({
    "month": [
        "2026-01",
        "2026-02"
    ],
    "B2B": [
        120,
        135
    ],
    "B2C": [
        90,
        95
    ],
    "Partner": [
        40,
        45
    ]
})
```

Převeď DataFrame do long formátu:

```text
month
segment
revenue
```

### Řešení

```python
df_long = df.melt(
    id_vars="month",
    var_name="segment",
    value_name="revenue"
)
```

---

## Test 9 — Long → Wide pomocí `pivot()`

### Zadání

Máš DataFrame ve formátu:

```text
month     segment   revenue

2026-01   B2B       120
2026-01   B2C        90
2026-01   Partner    40
2026-02   B2B       135
2026-02   B2C        95
2026-02   Partner    45
```

Převeď ho zpět do wide formátu.

### Řešení

```python
df_wide = df_long.pivot(
    index="month",
    columns="segment",
    values="revenue"
).reset_index()
```

---

## Test 10 — Power Query: Wide → Long

### Zadání

Jaká Power Query operace odpovídá Pandas:

```python
df.melt(...)
```

### Řešení

```text
Převést sloupce na řádky

→ Unpivot
```

---

## Test 11 — Power Query: Long → Wide

### Zadání

Jaká Power Query operace odpovídá Pandas:

```python
df.pivot(...)
```

### Řešení

```text
Kontingenční sloupec

→ Pivot
```

---

## Test 12 — Power Query Merge

### Zadání

Máš:

```text
orders

customer_id
revenue
```

a:

```text
customers

customer_id
customer_name
region
```

Chceš zachovat všechny řádky z `orders` a doplnit odpovídající data z `customers`.

Jaký typ spojení použiješ v Power Query?

### Řešení

```text
Sloučit dotazy

→ Levé vnější
```

Pandas ekvivalent:

```python
orders.merge(
    customers,
    on="customer_id",
    how="left"
)
```

---

## Test 13 — Power Query Append

### Zadání

Máš:

```text
orders_1

order_id
customer_id
revenue
```

a:

```text
orders_2

order_id
customer_id
revenue
```

Chceš druhou tabulku přidat pod první.

Jakou operaci použiješ v Power Query?

### Řešení

```text
Připojit dotazy

→ Append
```

Pandas ekvivalent:

```python
pd.concat(
    [
        orders_1,
        orders_2
    ],
    ignore_index=True
)
```

---

## Test 14 — Python in Excel

### Zadání

Načti do Pythonu oblast:

```text
A1:D10
```

První řádek obsahuje názvy sloupců.

### Řešení

```python
df = xl(
    "A1:D10",
    headers=True
)
```

---

## Test 15 — Python in Excel a Pandas

### Zadání

Máš v Excelu data:

```text
region
product
quantity
unit_price
```

Načti je pomocí `xl()`.

Potom:

1. převeď `quantity` a `unit_price` na `int`,
2. vytvoř `total`,
3. spočítej tržby podle produktu,
4. seřaď je sestupně.

### Řešení

```python
df = xl(
    "A1:D6",
    headers=True
)

df["quantity"] = df["quantity"].astype(int)

df["unit_price"] = df["unit_price"].astype(int)

df["total"] = (
    df["quantity"]
    * df["unit_price"]
)

revenue_by_product = (
    df.groupby(
        "product",
        as_index=False
    )["total"]
    .sum()
    .sort_values(
        by="total",
        ascending=False
    )
)

revenue_by_product
```

---

## Test 16 — Python in Excel výstup

### Zadání

Python in Excel vrátí `DataFrame`.

Jak výsledek zobrazíš přímo v buňkách Excelu?

### Řešení

```text
Výstup Pythonu

→ Excelová hodnota
```

