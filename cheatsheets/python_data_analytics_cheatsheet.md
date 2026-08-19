# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny pandas.

------------------------------------------------------------------------

## Rychlá orientace

### Základní workflow

``` text
načtení dat
→ kontrola dat
→ výběr / filtrování
→ výpočty a nové sloupce
→ agregace
→ řazení
→ export výsledků
```

## 1. Import pandas

``` python
import pandas as pd
```

`pandas` je knihovna pro práci s tabulkovými daty. `pd` je běžný alias.

## 2. Načtení dat

``` python
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")
df = pd.read_sql("SELECT * FROM orders", connection)
```

Pro `.xlsx` může být potřeba:

``` text
pip install openpyxl
```

U SQL je navíc potřeba připojení k databázi.

## 3. DataFrame a Series

``` python
print(type(df))
# <class 'pandas.DataFrame'>

print(type(df["product"]))
# <class 'pandas.Series'>
```

``` text
DataFrame → celá tabulka
Series    → jeden sloupec
```

Pandas automaticky vytváří index řádků od `0`. Index není automaticky
totéž jako ID nebo primary key.

## 4. Kontrola datasetu

``` python
df.head()       # prvních 5 řádků
df.head(10)     # prvních 10 řádků
df.info()       # struktura, Non-Null Count, datové typy
df.shape        # (počet řádků, počet sloupců)
df.columns      # názvy sloupců
```

`shape` a `columns` jsou atributy, proto nemají `()`.

### Non-Null Count

``` text
10 entries + 10 non-null → žádná hodnota nechybí
10 entries + 9 non-null  → jedna hodnota chybí
```

## 5. Datové typy

``` text
str     → text
int     → celé číslo
float   → desetinné číslo
bool    → True / False

int64
float64
str
```

`df.info()` pomáhá rychle odhalit, zda pandas načetl sloupce jako
očekávané datové typy.

## 6. Výběr sloupce

``` python
df["product"]
df["quantity"]
df["unit_price"]
df["total"]
```

Výsledkem výběru jednoho sloupce je `Series`.

## 7. Výpočty mezi sloupci

``` python
df["quantity"] * df["unit_price"]
```

Pandas provede výpočet po jednotlivých řádcích bez ručního `for` cyklu.

### Nový sloupec

``` python
df["total"] = df["quantity"] * df["unit_price"]
```

Pokud `"total"` neexistuje, pandas ho vytvoří. Mění se DataFrame v
paměti, nikoli původní soubor na disku.

## 8. Základní agregace

``` python
df["total"].sum()       # součet
df["total"].mean()      # aritmetický průměr
df["total"].min()       # minimum
df["total"].max()       # maximum
df["total"].median()    # medián
df["product"].mode()    # modus
```

Například:

``` python
total_revenue = df["total"].sum()
average_order = df["total"].mean()
```

Srovnání průměru:

``` text
SQL    → AVG()
Excel  → AVERAGE()
pandas → .mean()
```

`.mode()` může vrátit více hodnot, pokud mají stejnou nejvyšší četnost.

## 9. Filtrování

Samotná podmínka:

``` python
df["total"] > average_order
```

vrátí `Series` hodnot `True` / `False`. Ta funguje jako maska.

### Objednávky nad průměrem

``` python
above_average_orders = df[df["total"] > average_order]
```

### Kategorie Furniture

``` python
furniture_orders = df[df["category"] == "Furniture"]
```

Výsledkem filtrování je nový `DataFrame`.

### Operátory

``` text
==    rovná se
!=    nerovná se
>     větší než
<     menší než
>=    větší nebo rovno
<=    menší nebo rovno
```

Příklady:

``` python
df[df["total"] > 10000]
df[df["quantity"] >= 2]
df[df["category"] != "Furniture"]
```

## 10. Analýza filtrovaných dat

``` python
furniture_orders = df[df["category"] == "Furniture"]

total_revenue_furniture = furniture_orders["total"].sum()
average_order_furniture = furniture_orders["total"].mean()
```

Princip:

``` text
původní DataFrame
→ filtr
→ nový DataFrame
→ výběr sloupce
→ agregace
```

## 11. Řazení

Vzestupně:

``` python
df.sort_values(by="total")
df.sort_values(by="total", ascending=True)
```

Sestupně:

``` python
df.sort_values(by="total", ascending=False)
```

``` text
ascending=True  → vzestupně
ascending=False → sestupně
```

`True` a `False` musí mít velké první písmeno.

Uložení výsledku:

``` python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)
```

## 12. Export dat

### CSV

``` python
above_average_orders.to_csv(
    "above_average_orders.csv",
    index=False
)
```

`index=False` nezapíše pandas index jako další sloupec.

### JSON

``` python
above_average_orders.to_json(
    "above_average_orders.json",
    orient="records",
    indent=4
)
```

`orient="records"` vytvoří strukturu podobnou listu dictionaries.
`indent=4` zlepší čitelnost.

### Excel

``` python
above_average_orders.to_excel(
    "above_average_orders.xlsx",
    index=False
)
```

S názvem listu:

``` python
above_average_orders.to_excel(
    "above_average_orders.xlsx",
    sheet_name="Above Average Orders",
    index=False
)
```

### SQL

``` python
df.to_sql("orders", connection)
```

Pro SQL je potřeba databázové připojení.

## 13. Import vs. export

``` text
NAČTENÍ                     ULOŽENÍ

pd.read_csv()       ←→      df.to_csv()
pd.read_json()      ←→      df.to_json()
pd.read_excel()     ←→      df.to_excel()
pd.read_sql()       ←→      df.to_sql()
```

Při načítání DataFrame ještě nemáme, proto používáme `pd.read_...()`.

Při exportu už DataFrame existuje, proto používáme `df.to_...()`.

## 14. Funkce, metody a atributy

### Funkce

``` python
print(df)
type(df)
round(value, 2)
```

### Metody

``` python
df.head()
df.info()
df["total"].sum()
df["total"].mean()
df.sort_values(...)
df.to_csv(...)
```

Obecně:

``` text
objekt.metoda()
```

### Atributy

``` python
df.shape
df.columns
```

Rozdíl:

``` python
df.info()     # metoda
df.shape      # atribut
df.columns    # atribut
```

## 15. Praktický analytický vzor

``` python
import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

df["total"] = df["quantity"] * df["unit_price"]

total_revenue = df["total"].sum()
average_order = df["total"].mean()

above_average_orders = df[
    df["total"] > average_order
]

sorted_orders = df.sort_values(
    by="total",
    ascending=False
)

above_average_orders.to_csv(
    "above_average_orders.csv",
    index=False
)
```

## 16. Pandas vs. základní Python

### Nový sloupec

Základní Python:

``` python
for row in reader:
    row["total"] = row["quantity"] * row["unit_price"]
```

Pandas:

``` python
df["total"] = df["quantity"] * df["unit_price"]
```

### Součet

Základní Python:

``` python
total_revenue = 0

for order in orders:
    total_revenue = total_revenue + order["total"]
```

Pandas:

``` python
total_revenue = df["total"].sum()
```

### Průměr

Základní Python:

``` python
average_order = total_revenue / order_count
```

Pandas:

``` python
average_order = df["total"].mean()
```

### Filtrování

Základní Python:

``` python
above_average_orders = []

for order in orders:
    if order["total"] > average_order:
        above_average_orders.append(order)
```

Pandas:

``` python
above_average_orders = df[
    df["total"] > average_order
]
```

### Export CSV

Základní Python:

``` python
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[...])
    writer.writeheader()
    writer.writerows(data)
```

Pandas:

``` python
df.to_csv("output.csv", index=False)
```

## 17. Rychlý pandas tahák

``` python
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

# výběr sloupce
df["column"]

# nový sloupec
df["total"] = df["quantity"] * df["unit_price"]

# agregace
df["total"].sum()
df["total"].mean()
df["total"].min()
df["total"].max()
df["total"].median()
df["column"].mode()

# filtrování
df[df["total"] > 10000]
df[df["category"] == "Furniture"]

# řazení
df.sort_values(by="total")
df.sort_values(by="total", ascending=False)

# export
df.to_csv("output.csv", index=False)
df.to_json("output.json", orient="records", indent=4)
df.to_excel("output.xlsx", index=False)
```

## Nejdůležitější principy

``` text
DataFrame
→ celá tabulka

Series
→ jeden sloupec

df["column"]
→ vyber sloupec

df["new"] = ...
→ vytvoř nebo změň sloupec

df["column"].mean()
→ proveď výpočet nad sloupcem

df[podmínka]
→ vyfiltruj řádky

df.sort_values(...)
→ seřaď data

df.to_...()
→ exportuj DataFrame
```

Typický analytický postup:

``` text
načti
→ zkontroluj
→ vyfiltruj
→ vypočítej
→ seřaď
→ exportuj
```

## Další témata

Tento cheatsheet obsahuje pouze dosud probrané základy. Postupně lze
doplnit:

``` text
groupby()
více podmínek při filtrování
chybějící hodnoty
čištění dat
práce s textem
datum a čas
spojování tabulek
SQL + pandas
vizualizace
```
