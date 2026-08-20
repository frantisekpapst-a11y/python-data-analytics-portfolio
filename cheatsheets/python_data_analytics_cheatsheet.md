# Python for Data Analytics Cheatsheet

Praktický tahák pro práci s daty v Pythonu pomocí knihovny `pandas`.

---

## Rychlá orientace

### Základní workflow

```text
načtení dat
→ kontrola dat
→ výběr / filtrování
→ výpočty a nové sloupce
→ agregace
→ řazení
→ export výsledků
```

---

## 1. Import pandas

```python
import pandas as pd
```

`pandas` je knihovna pro práci s tabulkovými daty.

`pd` je běžný alias knihovny `pandas`.

---

## 2. Načtení dat

```python
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")
df = pd.read_sql("SELECT * FROM orders", connection)
```

Pro `.xlsx` může být potřeba:

```text
pip install openpyxl
```

U SQL je navíc potřeba připojení k databázi.

---

## 3. DataFrame a Series

```python
print(type(df))
# <class 'pandas.DataFrame'>

print(type(df["product"]))
# <class 'pandas.Series'>
```

```text
DataFrame → celá tabulka
Series    → jeden sloupec
```

Například:

```python
df
```

je `DataFrame`.

```python
df["product"]
```

je `Series`.

### Název DataFrame

`df` není povinný název. Je pouze běžnou konvencí.

Můžeme použít například:

```python
orders = pd.read_csv("orders.csv")
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")
```

Ve větších projektech mohou být konkrétní názvy čitelnější než obecné `df`.

---

## 4. Pandas index

Pandas automaticky vytváří index řádků:

```text
0
1
2
3
...
```

Výchozí index je obvykle typu:

```text
RangeIndex
```

Kontrola:

```python
print(df.index)
```

Název indexu:

```python
print(df.index.name)
```

Výchozí hodnota může být:

```text
None
```

Index lze pojmenovat:

```python
df.index.name = "row_id"
```

### Index není totéž jako ID

```text
Pandas index
≠
business ID / primary key
```

Například při načtení SQL tabulky můžeme mít:

```text
Pandas index → 0, 1, 2, 3
order_id     → 1001, 1002, 1003, 1004
```

`order_id` může být primary key databáze, zatímco pandas index je technická struktura DataFrame.

---

## 5. Kontrola datasetu

```python
df.head()       # prvních 5 řádků
df.head(10)     # prvních 10 řádků
df.info()       # struktura, Non-Null Count, datové typy
df.shape        # (počet řádků, počet sloupců)
df.columns      # názvy sloupců
```

`shape` a `columns` jsou atributy, proto nemají `()`.

### Non-Null Count

```text
10 entries + 10 non-null → žádná hodnota nechybí
10 entries + 9 non-null  → jedna hodnota chybí
```

`df.info()` vypisuje informace samo.

Proto není potřeba:

```python
print(df.info())
```

Stačí:

```python
df.info()
```

---

## 6. Datové typy

```text
str     → text
int     → celé číslo
float   → desetinné číslo
bool    → True / False
```

V pandas se můžeme setkat například s:

```text
int64
float64
str
```

`df.info()` pomáhá rychle odhalit, zda pandas načetl sloupce jako očekávané datové typy.

---

## 7. Výběr sloupce

```python
df["product"]
df["quantity"]
df["unit_price"]
df["total"]
```

Výsledkem výběru jednoho sloupce je `Series`.

Například:

```python
product = df["product"]
```

Proměnná `product` nyní obsahuje `Series`.

---

## 8. Výpočty mezi sloupci

```python
df["quantity"] * df["unit_price"]
```

Pandas provede výpočet po jednotlivých řádcích bez ručního `for` cyklu.

### Nový sloupec

```python
df["total"] = df["quantity"] * df["unit_price"]
```

Pokud `"total"` neexistuje, pandas ho vytvoří.

Mění se DataFrame v paměti, nikoli původní soubor na disku.

---

## 9. Základní agregace

```python
df["total"].sum()       # součet
df["total"].mean()      # aritmetický průměr
df["total"].min()       # minimum
df["total"].max()       # maximum
df["total"].median()    # medián
df["product"].mode()    # modus
```

Například:

```python
total_revenue = df["total"].sum()
average_order = df["total"].mean()
```

Srovnání průměru:

```text
SQL    → AVG()
Excel  → AVERAGE()
pandas → .mean()
```

`.mode()` může vrátit více hodnot, pokud mají stejnou nejvyšší četnost.

---

## 10. Základní filtrování

Samotná podmínka:

```python
df["total"] > average_order
```

vrátí `Series` hodnot:

```text
True
False
True
False
...
```

Této `Series` říkáme **boolean maska**.

### Objednávky nad průměrem

```python
above_average_orders = df[
    df["total"] > average_order
]
```

### Kategorie Furniture

```python
furniture_orders = df[
    df["category"] == "Furniture"
]
```

Výsledkem filtrování je nový `DataFrame`.

### Porovnávací operátory

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

df[df["category"] != "Furniture"]
```

---

## 11. Boolean maska

Samotná podmínka:

```python
df["total"] > 10000
```

nevytvoří filtrovanou tabulku.

Vytvoří pouze masku:

```text
True
False
True
...
```

Teprve:

```python
df[
    df["total"] > 10000
]
```

aplikuje masku na DataFrame.

Princip:

```text
podmínka
→ boolean maska

df[maska]
→ filtrovaný DataFrame
```

Masku lze uložit i samostatně:

```python
mask = df["total"] > 10000

high_value_orders = df[mask]
```

---

## 12. Více podmínek při filtrování

V běžném Pythonu používáme:

```text
and
or
not
```

Při filtrování pandas `Series` používáme:

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

### AND

```python
furniture_high_value = df[
    (df["category"] == "Furniture")
    & (df["total"] > 10000)
]
```

Každá podmínka musí být v závorkách:

```python
(podmínka_1) & (podmínka_2)
```

SQL analogie:

```sql
WHERE category = 'Furniture'
  AND total > 10000
```

### OR

```python
high_value_or_quantity = df[
    (df["total"] > 20000)
    | (df["quantity"] >= 4)
]
```

SQL analogie:

```sql
WHERE total > 20000
   OR quantity >= 4
```

### NOT

```python
not_furniture = df[
    ~(df["category"] == "Furniture")
]
```

Jednodušší varianta:

```python
not_furniture = df[
    df["category"] != "Furniture"
]
```

`~` neguje již vytvořenou boolean podmínku.

### XOR

```python
exclusive_filter = df[
    (df["total"] > 20000)
    ^ (df["quantity"] >= 4)
]
```

XOR vrací `True`, pokud platí právě jedna z podmínek.

```text
A      B      A ^ B

False  False   False
True   False   True
False  True    True
True   True    False
```

---

## 13. `isin()` — více konkrétních hodnot

Pokud chceme filtrovat několik konkrétních hodnot:

```python
selected_products = df[
    df["product"].isin([
        "Laptop",
        "Desk",
        "Monitor"
    ])
]
```

SQL analogie:

```sql
WHERE product IN ('Laptop', 'Desk', 'Monitor')
```

`isin()` znamená:

```text
je hodnota v tomto seznamu?
```

### NOT IN

Pomocí `~`:

```python
other_products = df[
    ~df["product"].isin([
        "Laptop",
        "Desk",
        "Monitor"
    ])
]
```

SQL analogie:

```sql
WHERE product NOT IN ('Laptop', 'Desk', 'Monitor')
```

---

## 14. `between()` — rozsah od–do

```python
mid_value_orders = df[
    df["total"].between(10000, 20000)
]
```

Výchozí chování znamená:

```text
10000 <= total <= 20000
```

SQL analogie:

```sql
WHERE total BETWEEN 10000 AND 20000
```

### Zahrnutí krajních hodnot

```python
df["total"].between(
    10000,
    20000,
    inclusive="both"
)
```

```text
both
→ 10000 <= total <= 20000
```

```python
df["total"].between(
    10000,
    20000,
    inclusive="left"
)
```

```text
left
→ 10000 <= total < 20000
```

```python
df["total"].between(
    10000,
    20000,
    inclusive="right"
)
```

```text
right
→ 10000 < total <= 20000
```

```python
df["total"].between(
    10000,
    20000,
    inclusive="neither"
)
```

```text
neither
→ 10000 < total < 20000
```

---

## 15. Analýza filtrovaných dat

```python
furniture_orders = df[
    df["category"] == "Furniture"
]

total_revenue_furniture = furniture_orders["total"].sum()

average_order_furniture = furniture_orders["total"].mean()
```

Princip:

```text
původní DataFrame
→ filtr
→ nový DataFrame
→ výběr sloupce
→ agregace
```

### Práce s více DataFrame

Po:

```python
selected_products = df[
    df["product"].isin(["Laptop", "Desk"])
]
```

existují dvě různé proměnné:

```text
df
→ původní DataFrame

selected_products
→ nový filtrovaný DataFrame
```

Pokud chceme dál filtrovat `selected_products`, podmínku vytváříme nad stejným DataFrame:

```python
selected_mid_value = selected_products[
    selected_products["total"].between(
        15000,
        30000
    )
]
```

Ne:

```python
df[
    selected_products["total"].between(
        15000,
        30000
    )
]
```

Maska a DataFrame musí odpovídat stejným řádkům / indexům.

---

## 16. `loc` — výběr podle názvů a podmínek

Základní syntaxe:

```python
df.loc[řádky, sloupce]
```

Například:

```python
furniture_summary = df.loc[
    df["category"] == "Furniture",
    ["product", "quantity", "total"]
]
```

První část:

```python
df["category"] == "Furniture"
```

vybírá řádky.

Druhá část:

```python
["product", "quantity", "total"]
```

je `list` názvů sloupců.

Princip:

```text
df.loc[
    řádky,
    sloupce
]
```

SQL analogie:

```text
loc řádky
→ podobné WHERE

loc sloupce
→ podobné SELECT
```

Například:

```python
high_value_summary = df.loc[
    df["total"] > 10000,
    ["order_id", "product", "category", "total"]
]
```

odpovídá přibližně:

```sql
SELECT
    order_id,
    product,
    category,
    total
FROM orders
WHERE total > 10000;
```

### `loc` s více podmínkami

```python
furniture_high_value = df.loc[
    (df["category"] == "Furniture")
    & (df["total"] > 10000),
    ["product", "quantity", "total"]
]
```

### Pouze filtrování řádků

Pokud nechceme omezit sloupce:

```python
df.loc[
    df["category"] == "Furniture"
]
```

---

## 17. `iloc` — výběr podle pozice

`iloc` používá číselné pozice řádků a sloupců.

Základ:

```python
df.iloc[řádky, sloupce]
```

### První řádek

```python
df.iloc[0]
```

### První tři řádky

```python
df.iloc[0:3]
```

Vrátí pozice:

```text
0
1
2
```

### Řádky i sloupce

```python
df.iloc[
    0:4,
    1:4
]
```

znamená:

```text
řádky:
0, 1, 2, 3

sloupce:
1, 2, 3
```

---

## 18. Slicing

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
df.iloc[0:5]
```

vrátí:

```text
0, 1, 2, 3, 4
```

A:

```python
df.iloc[
    0:5,
    1:5
]
```

vybere:

```text
řádky:
0, 1, 2, 3, 4

sloupce:
1, 2, 3, 4
```

Pravidlo:

```text
od start
do stop
ale stop už ne
```

---

## 19. `iloc` — konkrétní pozice

Nemusíme používat pouze souvislý rozsah.

Můžeme předat `list` konkrétních pozic:

```python
selected_columns = df.iloc[
    0:5,
    [1, 2, 3, 6]
]
```

Tím vybereme:

```text
prvních 5 řádků

a sloupce na pozicích:
1
2
3
6
```

Například:

```text
product
category
quantity
total
```

---

## 20. `loc` vs. `iloc`

```text
loc
→ názvy / labels / podmínky

iloc
→ číselné pozice
```

### `loc`

```python
df.loc[
    df["category"] == "Furniture",
    ["product", "total"]
]
```

### `iloc`

```python
df.iloc[
    0:5,
    1:3
]
```

Pro zapamatování:

```text
loc
→ co se jmenuje jak

iloc
→ co je kde
```

---

## 21. Řazení

Vzestupně:

```python
df.sort_values(by="total")

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

```text
ascending=True
→ vzestupně

ascending=False
→ sestupně
```

`True` a `False` musí mít velké první písmeno.

### Uložení výsledku

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)
```

### Nejvyšší objednávka

```python
sorted_orders.head(1)
```

vrátí celý první řádek.

Naopak:

```python
sorted_orders["total"].max()
```

vrátí pouze nejvyšší hodnotu `total`.

---

## 22. Index po filtrování a řazení

Pandas po filtrování nebo řazení zachovává původní indexy.

Například:

```text
   product       total
7  Laptop        50000
1  Chair         30000
4  Desk          25000
```

První zobrazený řádek má index `7`.

```python
sorted_orders.head(1)
```

znamená:

```text
ukaž první řádek podle aktuálního pořadí
```

Ne:

```text
ukaž řádek s indexem 1
```

### Reset indexu

```python
sorted_orders = sorted_orders.reset_index(
    drop=True
)
```

Index se znovu vytvoří od:

```text
0
1
2
3
...
```

`drop=True` zabrání tomu, aby se původní index uložil jako nový sloupec.

---

## 23. Export dat

### CSV

```python
above_average_orders.to_csv(
    "above_average_orders.csv",
    index=False
)
```

`index=False` nezapíše pandas index jako další sloupec.

### JSON

```python
above_average_orders.to_json(
    "above_average_orders.json",
    orient="records",
    indent=4
)
```

`orient="records"` vytvoří strukturu podobnou listu dictionaries.

`indent=4` zlepší čitelnost.

### Excel

```python
above_average_orders.to_excel(
    "above_average_orders.xlsx",
    index=False
)
```

S názvem listu:

```python
above_average_orders.to_excel(
    "above_average_orders.xlsx",
    sheet_name="Above Average Orders",
    index=False
)
```

### SQL

```python
df.to_sql(
    "orders",
    connection
)
```

Pro SQL je potřeba databázové připojení.

---

## 24. Import vs. export

```text
NAČTENÍ                     ULOŽENÍ

pd.read_csv()       ←→      df.to_csv()
pd.read_json()      ←→      df.to_json()
pd.read_excel()     ←→      df.to_excel()
pd.read_sql()       ←→      df.to_sql()
```

Při načítání DataFrame ještě nemáme, proto používáme:

```python
pd.read_...()
```

Při exportu už DataFrame existuje, proto používáme:

```python
df.to_...()
```

---

## 25. Funkce, metody a atributy

### Funkce

```python
print(df)
type(df)
round(value, 2)
```

### Metody

```python
df.head()
df.info()
df["total"].sum()
df["total"].mean()
df.sort_values(...)
df.to_csv(...)
```

Obecně:

```text
objekt.metoda()
```

### Atributy

```python
df.shape
df.columns
```

Rozdíl:

```python
df.info()     # metoda
df.shape      # atribut
df.columns    # atribut
```

---

## 26. Praktický analytický vzor

```python
import pandas as pd

df = pd.read_csv(
    "ecommerce_sales_analysis.csv"
)

df["total"] = (
    df["quantity"]
    * df["unit_price"]
)

average_order = df["total"].mean()

above_average_furniture = df[
    (df["total"] > average_order)
    & (df["category"] == "Furniture")
]

result = above_average_furniture.sort_values(
    by="total",
    ascending=False
)

result.to_csv(
    "above_average_furniture.csv",
    index=False
)
```

Workflow:

```text
načti
→ vytvoř nový sloupec
→ vypočítej metriku
→ filtruj
→ seřaď
→ exportuj
```

---

## 27. Pandas vs. základní Python

### Nový sloupec

Základní Python:

```python
for row in reader:
    row["total"] = (
        row["quantity"]
        * row["unit_price"]
    )
```

Pandas:

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

### Součet

Základní Python:

```python
total_revenue = 0

for order in orders:
    total_revenue = (
        total_revenue
        + order["total"]
    )
```

Pandas:

```python
total_revenue = df["total"].sum()
```

### Průměr

Základní Python:

```python
average_order = (
    total_revenue
    / order_count
)
```

Pandas:

```python
average_order = df["total"].mean()
```

### Filtrování

Základní Python:

```python
above_average_orders = []

for order in orders:
    if order["total"] > average_order:
        above_average_orders.append(order)
```

Pandas:

```python
above_average_orders = df[
    df["total"] > average_order
]
```

### Export CSV

Základní Python:

```python
with open(
    "output.csv",
    "w",
    newline=""
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[...]
    )

    writer.writeheader()
    writer.writerows(data)
```

Pandas:

```python
df.to_csv(
    "output.csv",
    index=False
)
```

---

## 28. Rychlý pandas tahák

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

# výběr sloupce
df["column"]

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
df["column"].mode()

# základní filtrování
df[df["total"] > 10000]

df[
    df["category"] == "Furniture"
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

# NOT IN
df[
    ~df["product"].isin([
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

# konkrétní pozice sloupců
df.iloc[
    0:5,
    [1, 2, 3, 6]
]

# řazení
df.sort_values(
    by="total"
)

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

## Nejdůležitější principy

```text
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

podmínka
→ vytvoř boolean masku

df[podmínka]
→ vyfiltruj řádky

& → AND
| → OR
~ → NOT
^ → XOR

isin()
→ vyber několik konkrétních hodnot

between()
→ vyber hodnoty v rozsahu

df.loc[řádky, sloupce]
→ vybírej podle názvů a podmínek

df.iloc[řádky, sloupce]
→ vybírej podle číselných pozic

[start:stop]
→ start se zahrnuje
→ stop se nezahrnuje

df.sort_values(...)
→ seřaď data

df.to_...()
→ exportuj DataFrame
```

---

## Typický analytický postup

```text
načti data
→ zkontroluj strukturu
→ vytvoř potřebné sloupce
→ vytvoř podmínky
→ vyfiltruj řádky
→ případně omez sloupce
→ vypočítej metriky
→ seřaď výsledky
→ exportuj
```

---

## SQL vs. pandas — rychlé srovnání

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
```

Příklad SQL:

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

## Další témata

Tento cheatsheet obsahuje pouze dosud probranou látku.

Postupně lze doplnit:

```text
chybějící hodnoty
isna()
notna()
dropna()
fillna()

čištění dat
duplicity
změna datových typů
přejmenování sloupců

groupby()
agregace podle kategorií

práce s textem
datum a čas
spojování tabulek
merge()
SQL + pandas
vizualizace
```
