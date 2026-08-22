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

Import a export:

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

`df` je pouze konvence.

Můžeme použít například:

```python
orders = pd.read_json("orders.json")
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
```

```text
df.shape
→ (počet řádků, počet sloupců)
```

`shape`, `columns` a `index` jsou atributy:

```python
df.shape
```

ne:

```python
df.shape()
```

`df.info()` ukáže mimo jiné:

```text
počet řádků
názvy sloupců
Non-Null Count
datové typy
```

---

# 5. Datové typy

```text
str       → text
int       → celé číslo
float     → desetinné číslo
bool      → True / False

int64
float64
object
```

`dtype` znamená:

```text
data type
```

Například:

```text
dtype: int64
```

znamená, že hodnoty výsledné `Series` jsou celá čísla.

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

Kontrola:

```python
df.index
```

Index není totéž jako business ID:

```text
Pandas index
≠
order_id / primary key
```

Po filtrování nebo řazení pandas původní index zachovává.

Reset:

```python
df = df.reset_index(drop=True)
```

`drop=True` zabrání vytvoření starého indexu jako nového sloupce.

---

# 7. Výběr sloupce

Jeden sloupec:

```python
df["product"]
```

Výsledek:

```text
Series
```

Více sloupců:

```python
df[
    ["product", "quantity", "total"]
]
```

Výsledek:

```text
DataFrame
```

---

# 8. Nový sloupec a výpočty

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

Pandas provede výpočet po jednotlivých řádcích.

Pokud sloupec `"total"` neexistuje, pandas ho vytvoří.

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

SQL / Excel / pandas:

```text
SQL AVG()        → pandas mean()
SQL SUM()        → pandas sum()
Excel AVERAGE()  → pandas mean()
```

---

# 10. Boolean maska

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

To je **boolean maska**.

Použití masky:

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

---

# 11. Porovnávací operátory

```text
==    rovná se
!=    nerovná se
>     větší než
<     menší než
>=    větší nebo rovno
<=    menší nebo rovno
```

Příklady:

```python
df[df["total"] > 10000]

df[df["quantity"] >= 2]

df[
    df["category"] == "Furniture"
]

df[
    df["category"] != "Furniture"
]
```

---

# 12. Více podmínek

V pandas používáme:

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Každá podmínka má být v závorkách.

## AND

```python
df[
    (df["category"] == "Furniture")
    & (df["total"] > 10000)
]
```

## OR

```python
df[
    (df["total"] > 20000)
    | (df["quantity"] >= 4)
]
```

## NOT

```python
df[
    ~(df["category"] == "Furniture")
]
```

Často jednodušeji:

```python
df[
    df["category"] != "Furniture"
]
```

## XOR

```python
df[
    (df["total"] > 20000)
    ^ (df["quantity"] >= 4)
]
```

XOR je `True`, pokud platí právě jedna podmínka.

---

# 13. `isin()` — více konkrétních hodnot

```python
df[
    df["product"].isin([
        "Laptop",
        "Desk",
        "Monitor"
    ])
]
```

`isin()` očekává jednu kolekci hodnot, typicky `list`.

Správně:

```python
.isin(["Laptop", "Desk", "Monitor"])
```

Ne:

```python
.isin("Laptop", "Desk", "Monitor")
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

SQL:

```text
IN      → isin()
NOT IN  → ~isin()
```

---

# 14. `between()` — rozsah

```python
df[
    df["total"].between(
        10000,
        20000
    )
]
```

Výchozí chování:

```text
10000 <= total <= 20000
```

Možnosti:

```text
inclusive="both"
→ 10000 <= x <= 20000

inclusive="left"
→ 10000 <= x < 20000

inclusive="right"
→ 10000 < x <= 20000

inclusive="neither"
→ 10000 < x < 20000
```

---

# 15. `loc` — názvy a podmínky

Základ:

```python
df.loc[
    řádky,
    sloupce
]
```

Příklad:

```python
df.loc[
    df["category"] == "Furniture",
    ["product", "quantity", "total"]
]
```

Více podmínek:

```python
df.loc[
    (df["category"] == "Furniture")
    & (df["total"] > 10000),
    ["product", "quantity", "total"]
]
```

Zapamatování:

```text
loc
→ co se jmenuje jak
```

SQL analogie:

```text
řádky   → WHERE
sloupce → SELECT
```

---

# 16. `iloc` — číselné pozice

Základ:

```python
df.iloc[
    řádky,
    sloupce
]
```

První řádek:

```python
df.iloc[0]
```

První 3 řádky:

```python
df.iloc[0:3]
```

Řádky i sloupce:

```python
df.iloc[
    0:5,
    1:4
]
```

Vybere:

```text
řádky:
0, 1, 2, 3, 4

sloupce:
1, 2, 3
```

Konkrétní pozice:

```python
df.iloc[
    0:5,
    [1, 2, 3, 6]
]
```

Zapamatování:

```text
iloc
→ co je kde
```

---

# 17. Slicing

Syntaxe:

```text
[start:stop]
```

Platí:

```text
start → zahrnuje se
stop  → nezahrnuje se
```

Například:

```python
df.iloc[0:3]
```

vrátí:

```text
0, 1, 2
```

Prvních 5 řádků:

```python
df.iloc[0:5]
```

---

# 18. Více DataFrame a masky

Například:

```python
selected_products = df[
    df["product"].isin([
        "Laptop",
        "Desk"
    ])
]
```

Pokud chceme dál filtrovat `selected_products`:

```python
selected_mid_value = selected_products[
    selected_products["total"].between(
        15000,
        30000
    )
]
```

Masku vytváříme nad stejným DataFrame, na který ji aplikujeme.

```text
DataFrame
+
boolean maska
→ musí odpovídat stejným řádkům / indexům
```

---

# 19. Řazení

Vzestupně:

```python
df.sort_values(
    by="total",
    ascending=True
)
```

Sestupně:

```python
df.sort_values(
    by="total",
    ascending=False
)
```

Uložení:

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)
```

Nejvyšší celý řádek:

```python
sorted_orders.head(1)
```

Pouze nejvyšší hodnota:

```python
sorted_orders["total"].max()
```

---

# 20. Chybějící hodnoty — `NaN`

Chybějící hodnota se v pandas často zobrazí jako:

```text
NaN
```

Například JSON:

```json
"region": null
```

se může po načtení zobrazit jako:

```text
NaN
```

Důležitý rozdíl:

```text
NaN
→ hodnota chybí / není známá

0
→ známá hodnota je skutečně nula
```

---

# 21. `isna()` — kde hodnoty chybí

```python
df.isna()
```

Vrací:

```text
True  → hodnota chybí
False → hodnota nechybí
```

Počet chybějících hodnot:

```python
df.isna().sum()
```

Proč `sum()`?

```text
True  = 1
False = 0
```

`len()` by zjistil délku struktury, ne počet `True`.

---

# 22. `notna()` — kde hodnoty nechybí

```python
df.notna()
```

```text
True  → hodnota existuje
False → hodnota chybí
```

Praktický filtr:

```python
df[
    df["region"].notna()
]
```

---

# 23. `dropna()` — odstranění chybějících hodnot

Výchozí:

```python
df.dropna()
```

Odstraní řádek, pokud obsahuje alespoň jeden `NaN`.

Stejné jako:

```python
df.dropna(
    how="any"
)
```

Pouze úplně prázdné řádky:

```python
df.dropna(
    how="all"
)
```

```text
how="any"
→ stačí jeden NaN

how="all"
→ všechny hodnoty musí být NaN
```

---

# 24. `subset` — kontrola vybraných sloupců

Pouze podle `region`:

```python
df.dropna(
    subset=["region"]
)
```

Více sloupců:

```python
df.dropna(
    subset=[
        "region",
        "customer_type"
    ]
)
```

S `how`:

```python
df.dropna(
    subset=[
        "region",
        "customer_type"
    ],
    how="any"
)
```

---

# 25. `fillna()` — doplnění hodnot

Text:

```python
df["region"] = (
    df["region"]
    .fillna("Unknown")
)
```

Číslo například mediánem:

```python
df["unit_price"] = (
    df["unit_price"]
    .fillna(
        df["unit_price"].median()
    )
)
```

Není nutné každé `NaN` doplnit.

Například u `quantity` může být lepší ponechat `NaN`, pokud skutečnou hodnotu neznáme.

---

# 26. Agregace a `NaN`

Pandas při běžných agregacích `NaN` standardně ignoruje.

```python
df["quantity"].sum()
df["quantity"].mean()
df["quantity"].median()
```

To ale neznamená, že chybějící hodnoty nemusíme kontrolovat.

---

# 27. `copy()` — kopie DataFrame

```python
orders_clean = orders
```

znamená:

```text
dvě proměnné
→ jeden objekt
```

Bezpečná kopie:

```python
orders_clean = orders.copy()
```

```text
orders
→ původní DataFrame

orders_clean
→ samostatná kopie
```

Při čištění dat je `copy()` praktická.

---

# 28. Cleaning workflow

```python
orders_clean = orders.copy()

orders_clean["region"] = (
    orders_clean["region"]
    .fillna("Unknown")
)

orders_clean["customer_type"] = (
    orders_clean["customer_type"]
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

Důležité:

```text
orders
→ původní data

orders_clean
→ pracovní vyčištěná data
```

Pokud už pracujeme s `orders_clean`, další kroky provádíme nad `orders_clean`.

---

# 29. Export dat

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

`index=False` zabrání exportu pandas indexu jako dalšího sloupce.

---

# 30. Funkce, metody a atributy

## Funkce

```python
print(df)
type(df)
round(value, 2)
```

## Metody

```python
df.head()
df.info()
df.isna()
df.dropna()
df.copy()

df["total"].sum()
df.sort_values(...)
df.to_csv(...)
```

## Atributy

```python
df.shape
df.columns
df.index
```

```text
objekt.metoda()
objekt.atribut
```

---

# 31. Praktický analytický workflow

```python
import pandas as pd

orders = pd.read_json(
    "orders.json"
)

print(
    orders.isna().sum()
)

orders_clean = orders.copy()

orders_clean["region"] = (
    orders_clean["region"]
    .fillna("Unknown")
)

orders_clean = orders_clean.dropna(
    subset=["product"]
)

orders_clean["total"] = (
    orders_clean["quantity"]
    * orders_clean["unit_price"]
)

average_order = (
    orders_clean["total"].mean()
)

result = orders_clean[
    orders_clean["total"]
    > average_order
]

result = result.sort_values(
    by="total",
    ascending=False
)

result.to_csv(
    "result.csv",
    index=False
)
```

```text
načti
→ zkontroluj
→ vyčisti
→ vypočítej
→ filtruj
→ seřaď
→ exportuj
```

---

# 32. Rychlý pandas tahák

```python
import pandas as pd

# načtení
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")

# kontrola
df.head()
df.info()
df.shape
df.columns
df.index

# chybějící hodnoty
df.isna()
df.isna().sum()
df.notna()

# kopie
df_clean = df.copy()

# odstranění NaN
df.dropna()

df.dropna(
    subset=["region"]
)

df.dropna(
    how="all"
)

# doplnění NaN
df["region"] = (
    df["region"]
    .fillna("Unknown")
)

df["unit_price"] = (
    df["unit_price"]
    .fillna(
        df["unit_price"].median()
    )
)

# sloupec
df["column"]

# více sloupců
df[
    ["product", "quantity", "total"]
]

# nový sloupec
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)

# agregace
df["total"].sum()
df["total"].mean()
df["total"].min()
df["total"].max()
df["total"].median()
df["product"].mode()

# filtr
df[
    df["total"] > 10000
]

# AND
df[
    (df["total"] > 10000)
    & (df["category"] == "Furniture")
]

# OR
df[
    (df["total"] > 20000)
    | (df["quantity"] >= 4)
]

# NOT
df[
    ~(df["category"] == "Furniture")
]

# isin
df[
    df["product"].isin([
        "Laptop",
        "Desk",
        "Monitor"
    ])
]

# between
df[
    df["total"].between(
        10000,
        20000
    )
]

# loc
df.loc[
    df["total"] > 10000,
    ["product", "category", "total"]
]

# iloc
df.iloc[
    0:5,
    1:4
]

# řazení
df.sort_values(
    by="total",
    ascending=False
)

# reset indexu
df.reset_index(
    drop=True
)

# export
df.to_csv(
    "output.csv",
    index=False
)

df.to_json(
    "output.json",
    orient="records",
    indent=4
)

df.to_excel(
    "output.xlsx",
    index=False
)
```

---

# 33. Syntax — závorky a uvozovky

```text
()
→ volání funkce / metody
→ seskupení podmínek

[]
→ výběr sloupce
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

Rozpad:

```text
df["product"]
→ sloupec

isin(...)
→ metoda

["Laptop", "Desk", "Monitor"]
→ list textových hodnot
```

---

# 34. SQL vs. pandas

```text
SQL                         pandas

WHERE                       df[podmínka]
AND                         &
OR                          |
NOT                         ~
IN                          isin()
BETWEEN                     between()
SELECT + WHERE              loc

AVG()                       mean()
SUM()                       sum()
MIN()                       min()
MAX()                       max()

ORDER BY                    sort_values()

IS NULL                     isna()
IS NOT NULL                 notna()
```

SQL:

```sql
SELECT
    product,
    quantity,
    total
FROM orders
WHERE category = 'Furniture'
  AND total > 10000;
```

Pandas:

```python
df.loc[
    (df["category"] == "Furniture")
    & (df["total"] > 10000),
    ["product", "quantity", "total"]
]
```

---

# 35. Nejdůležitější principy

```text
DataFrame
→ celá tabulka

Series
→ jeden sloupec

df["column"]
→ výběr sloupce

df[["a", "b"]]
→ výběr více sloupců

df["new"] = ...
→ nový nebo změněný sloupec

podmínka
→ boolean maska

df[podmínka]
→ filtrované řádky

& → AND
| → OR
~ → NOT
^ → XOR

isin()
→ několik konkrétních hodnot

between()
→ rozsah hodnot

loc
→ názvy a podmínky

iloc
→ číselné pozice

[start:stop]
→ start ano, stop ne

NaN
→ chybějící hodnota

isna()
→ kde hodnoty chybí?

isna().sum()
→ kolik hodnot chybí?

dropna()
→ odstranit řádky s NaN

fillna()
→ doplnit NaN

copy()
→ samostatná kopie DataFrame

sort_values()
→ řazení

to_csv()
to_json()
to_excel()
→ export
```

---

# Typický analytický postup

```text
načti data
→ zkontroluj strukturu
→ zkontroluj chybějící hodnoty
→ případně vytvoř pracovní kopii
→ vyčisti data
→ vytvoř nové sloupce
→ filtruj
→ vypočítej metriky
→ seřaď výsledky
→ exportuj
```

---

# Další témata

```text
duplicity
duplicated()
drop_duplicates()

změna datových typů
astype()

přejmenování sloupců
rename()

groupby()
agregace podle kategorií

práce s textem

datum a čas

merge()
spojování tabulek

SQL + pandas

vizualizace
```