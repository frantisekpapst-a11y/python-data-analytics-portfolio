# Lekce 6

## Test 1 — Načtení a kontrola dat

### Zadání

Načti soubor:

```text
ecommerce_sales_analysis.csv
```

Proveď následující:

1. importuj knihovnu `pandas`
2. načti CSV soubor do proměnné `df`
3. zobraz prvních 5 řádků
4. zobraz počet řádků a sloupců
5. zobraz názvy všech sloupců
6. zobraz základní informace o datasetu

### Řešení

```python
import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

print(df.head())

print(df.shape)

print(df.columns)

df.info()
```

### Vysvětlení

```python
df.head()
```

zobrazí prvních 5 řádků datasetu.

```python
df.shape
```

vrací dvojici:

```text
(počet řádků, počet sloupců)
```

```python
df.columns
```

vrací názvy sloupců.

```python
df.info()
```

zobrazí informace o struktuře datasetu, počtu neprázdných hodnot a datových typech.

`shape` a `columns` jsou atributy, proto se za nimi nepoužívají závorky.

`info()` je metoda, proto se používají závorky.

Není potřeba psát:

```python
print(df.info())
```

protože `df.info()` svůj výstup zobrazí sama.

---

## Test 2 — Nový sloupec a agregace

### Zadání

Vytvoř nový sloupec:

```text
total
```

jako:

```text
quantity × unit_price
```

Potom vypočítej:

1. celkové tržby
2. průměrnou hodnotu objednávky
3. nejvyšší hodnotu objednávky
4. nejnižší hodnotu objednávky

Výsledky ulož do proměnných a vypiš.

### Řešení

```python
df["total"] = df["quantity"] * df["unit_price"]

total_revenue = df["total"].sum()

avg_order = df["total"].mean()

max_order_value = df["total"].max()

min_order_value = df["total"].min()

print("Celkové tržby:", total_revenue, "Kč")

print("Průměrná objednávka:", avg_order, "Kč")

print("Nejnižší objednávka:", min_order_value, "Kč")

print("Nejvyšší objednávka:", max_order_value, "Kč")
```

### Vysvětlení

Tento zápis:

```python
df["total"] = df["quantity"] * df["unit_price"]
```

provede výpočet po jednotlivých řádcích bez použití `for` cyklu.

Použité agregace:

```python
.sum()
.mean()
.max()
.min()
```

znamenají:

```text
sum()   → součet
mean()  → průměr
max()   → maximum
min()   → minimum
```

Název `max_order_value` je přesnější než například `max_revenue`, protože hledáme nejvyšší hodnotu jedné objednávky, nikoli celkové tržby.

---

## Test 3 — Filtrování dat

### Zadání

1. vypočítej průměrnou hodnotu objednávky
2. vyfiltruj objednávky, jejichž `total` je vyšší než průměr
3. výsledek ulož do `above_average_orders`
4. vyfiltruj objednávky z kategorie `"Furniture"`
5. výsledek ulož do `furniture_orders`
6. vypočítej celkové tržby pouze pro kategorii `Furniture`

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

print(
    "Celkové tržby nábytek:",
    total_revenue_furniture,
    "Kč"
)
```

### Vysvětlení

Samotná podmínka:

```python
df["total"] > average_order
```

vrací hodnoty:

```text
True
False
True
...
```

Jedná se o takzvanou **boolean masku**.

Boolean maska určuje, které řádky budou zachovány.

Použití:

```python
df[df["total"] > average_order]
```

znamená:

```text
vezmi DataFrame df
→ otestuj podmínku
→ ponech pouze řádky s hodnotou True
```

Stejný princip platí pro textový filtr:

```python
df[df["category"] == "Furniture"]
```

Potom můžeme nad filtrovaným DataFrame provádět další agregace:

```python
furniture_orders["total"].sum()
```

---

## Test 4 — Řazení a nejvyšší objednávka

### Zadání

1. seřaď celý dataset podle `total` sestupně
2. výsledek ulož do `sorted_orders`
3. zobraz prvních 5 řádků
4. zjisti, která objednávka má nejvyšší hodnotu `total`

Nepoužívej žádnou novou Pandas funkci.

### Řešení

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)

print(sorted_orders.head())

print(sorted_orders.head(1))
```

### Vysvětlení

```python
ascending=False
```

znamená sestupné řazení:

```text
nejvyšší
→ nejnižší
```

Po seřazení je proto nejvyšší objednávka na prvním místě.

```python
sorted_orders.head(1)
```

zobrazí první řádek výsledku.

Důležitý rozdíl:

```python
sorted_orders["total"].max()
```

vrátí pouze nejvyšší hodnotu `total`.

Například:

```text
75000
```

Ale:

```python
sorted_orders.head(1)
```

vrátí celý řádek objednávky, takže vidíme i produkt, kategorii, množství a další údaje.

### Index vs. pořadí řádku

Po použití:

```python
df.sort_values(...)
```

Pandas řádky přesune, ale jejich původní indexy zachová.

Výsledek může například vypadat:

```text
   product       total
7  Laptop        50000
1  Chair         30000
4  Desk          25000
```

První řádek zde má index `7`.

```python
head(1)
```

znamená:

```text
zobraz první jeden řádek podle aktuálního pořadí
```

Neznamená:

```text
zobraz řádek s indexem 1
```

Pokud bychom chtěli index po seřazení vytvořit znovu:

```python
sorted_orders = sorted_orders.reset_index(drop=True)
```

---

## Test 5 — Kompletní analytický workflow

### Zadání

Vytvoř jeden souvislý skript, který:

1. načte `ecommerce_sales_analysis.csv`
2. vytvoří sloupec `total`
3. vypočítá průměrnou hodnotu objednávky
4. vyfiltruje objednávky nad průměrem
5. vyfiltrované objednávky seřadí podle `total` sestupně
6. uloží výsledek do CSV:

```text
above_average_orders_test.csv
```

bez pandas indexu

7. uloží stejný výsledek do JSON:

```text
above_average_orders_test.json
```

s nastavením:

```python
orient="records"
indent=4
```

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

### Vysvětlení

Správné pořadí operací je:

```text
načtení
→ výpočet
→ agregace
→ filtrování
→ řazení
→ export
```

Důležitý je tento krok:

```python
sorted_orders = above_average_orders.sort_values(
    by="total",
    ascending=False
)
```

Řadíme pouze objednávky, které už prošly filtrem.

Pokud bychom napsali:

```python
sorted_orders = df.sort_values(
    by="total",
    ascending=False
)
```

seřadili bychom celý původní dataset.

Při exportu proto také používáme:

```python
sorted_orders.to_csv(...)
sorted_orders.to_json(...)
```

aby se do souborů uložil skutečný finální výsledek analýzy.

---

# Lekce 7

## Test 1 — Filtrování pomocí AND

### Zadání

Vyber objednávky, které současně splňují obě podmínky:

* `category == "Furniture"`
* `total > 15000`

Výsledek ulož do:

```python
furniture_high_value
```

Použij operátor `&`.

### Řešení

```python
furniture_high_value = df[
    (df["category"] == "Furniture")
    & (df["total"] > 15000)
]
```

### Vysvětlení

V Pandas se při kombinování boolean podmínek nad `Series` používá:

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Na rozdíl od běžného Pythonu zde nepoužíváme:

```text
and
or
not
```

Každá podmínka musí být při použití `&` nebo `|` uzavřena do vlastních závorek:

```python
(df["category"] == "Furniture")
&
(df["total"] > 15000)
```

Samotné podmínky vytvářejí boolean masky:

```text
True
False
True
...
```

Vnější:

```python
df[...]
```

potom tuto masku aplikuje na celý DataFrame.

SQL obdoba:

```sql
WHERE category = 'Furniture'
  AND total > 15000
```

---

## Test 2 — OR a NOT

### Zadání

Vytvoř dva filtry.

První filtr vybere objednávky, které splňují alespoň jednu z podmínek:

* `quantity >= 4`
* `total > 20000`

Výsledek ulož do:

```python
high_quantity_or_value
```

Druhý filtr vybere všechny objednávky, které nejsou z kategorie:

```text
Electronics
```

Výsledek ulož do:

```python
not_electronics
```

U druhého filtru použij operátor `~`.

### Řešení

```python
high_quantity_or_value = df[
    (df["quantity"] >= 4)
    | (df["total"] > 20000)
]

not_electronics = df[
    ~(df["category"] == "Electronics")
]
```

### Vysvětlení

Operátor:

```python
|
```

znamená OR.

Řádek tedy projde filtrem, pokud platí alespoň jedna podmínka.

```text
quantity >= 4
NEBO
total > 20000
```

Operátor:

```python
~
```

neznamená porovnání.

Neguje již vytvořenou boolean podmínku.

Nejprve:

```python
df["category"] == "Electronics"
```

vytvoří například:

```text
True
False
True
...
```

Potom:

```python
~(df["category"] == "Electronics")
```

hodnoty obrátí:

```text
False
True
False
...
```

Pro jednoduché porovnání lze v praxi použít také:

```python
not_electronics = df[
    df["category"] != "Electronics"
]
```

To je v tomto případě čitelnější.

`~` se hodí zejména při negaci složitějších podmínek nebo například `isin()`.

---

## Test 3 — `isin()` a `between()`

### Zadání

Nejprve vyber pouze produkty:

```text
Laptop
Desk
Office Chair
```

Výsledek ulož do:

```python
selected_products
```

Potom z těchto vybraných produktů ponech pouze objednávky, kde je `total` mezi:

```text
15000 až 30000 včetně
```

Výsledek ulož do:

```python
selected_mid_value
```

Použij:

```python
isin()
between()
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

### Vysvětlení

Metoda:

```python
isin()
```

ověřuje, zda se hodnota nachází mezi zadanými hodnotami.

Například:

```python
df["product"].isin([
    "Laptop",
    "Desk",
    "Office Chair"
])
```

je podobné SQL:

```sql
WHERE product IN ('Laptop', 'Desk', 'Office Chair')
```

Metoda:

```python
between(15000, 30000)
```

znamená:

```text
15000 <= total <= 30000
```

Ve výchozím nastavení jsou tedy obě krajní hodnoty zahrnuté.

Důležitý je zde princip práce s novým DataFrame.

Po:

```python
selected_products = df[...]
```

existují dva různé DataFrame:

```text
df
→ původní DataFrame

selected_products
→ nový filtrovaný DataFrame
```

Proto musí druhá boolean maska vzniknout nad stejným DataFrame, který následně filtrujeme:

```python
selected_mid_value = selected_products[
    selected_products["total"].between(15000, 30000)
]
```

Nesprávně by bylo:

```python
selected_mid_value = df[
    selected_products["total"].between(15000, 30000)
]
```

Boolean maska zde vzniká z `selected_products`, ale snažíme se ji aplikovat na `df`.

Jejich indexy se nemusí shodovat a Pandas může vrátit chybu:

```text
Unalignable boolean Series provided as indexer
```

Princip:

```text
df
→ isin()
→ selected_products
→ between()
→ selected_mid_value
```

### Varianty `between()`

```python
inclusive="both"
```

zahrne oba kraje.

```python
inclusive="left"
```

zahrne pouze levý kraj.

```python
inclusive="right"
```

zahrne pouze pravý kraj.

```python
inclusive="neither"
```

nezahrne žádný kraj.

Například:

```python
df["total"].between(
    15000,
    30000,
    inclusive="neither"
)
```

znamená:

```text
15000 < total < 30000
```

---

## Test 4 — Výběr pomocí `loc`

### Zadání

Pomocí `loc` vyber:

* pouze řádky, kde `total > 10000`
* pouze sloupce:

  * `order_id`
  * `product`
  * `category`
  * `total`

Výsledek ulož do:

```python
high_value_summary
```

### Řešení

```python
high_value_summary = df.loc[
    df["total"] > 10000,
    ["order_id", "product", "category", "total"]
]
```

### Vysvětlení

Základní syntaxe `loc` je:

```python
df.loc[řádky, sloupce]
```

První část:

```python
df["total"] > 10000
```

určuje, které **řádky** budou vybrány.

Druhá část:

```python
["order_id", "product", "category", "total"]
```

je `list` názvů sloupců, které chceme zachovat.

Princip:

```text
df.loc[
    podmínka pro řádky,
    seznam sloupců
]
```

SQL analogie:

```sql
SELECT
    order_id,
    product,
    category,
    total
FROM orders
WHERE total > 10000;
```

Pro zapamatování:

```text
loc

řádky   → podobné WHERE
sloupce → podobné SELECT
```

Pokud chceme filtrovat pouze řádky a zachovat všechny sloupce, můžeme použít:

```python
df.loc[df["total"] > 10000]
```

---

## Test 5 — `iloc` a `loc`

### Zadání

Nejprve pomocí `iloc` vyber:

* prvních 5 řádků
* sloupce na pozicích `1`, `2`, `3`, `4`

Výsledek ulož do:

```python
first_five_selected
```

Potom pomocí `loc` vyber z původního DataFrame:

* řádky, kde `category == "Furniture"`
* řádky, kde zároveň `total > 10000`
* pouze sloupce:

  * `product`
  * `quantity`
  * `total`

Výsledek ulož do:

```python
furniture_summary
```

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

### Vysvětlení

`iloc` pracuje s **číselnými pozicemi** řádků a sloupců.

Základní syntaxe:

```python
df.iloc[řádky, sloupce]
```

Například:

```python
df.iloc[0:5, 1:5]
```

znamená:

```text
řádky:
0, 1, 2, 3, 4

sloupce:
1, 2, 3, 4
```

U slicingu platí:

```text
start → zahrnuje se
stop  → nezahrnuje se
```

Proto:

```python
0:5
```

znamená:

```text
0, 1, 2, 3, 4
```

a:

```python
1:5
```

znamená:

```text
1, 2, 3, 4
```

### `loc` vs. `iloc`

```text
loc
→ výběr podle názvů a podmínek

iloc
→ výběr podle číselných pozic
```

Například:

```python
df.loc[
    df["category"] == "Furniture",
    ["product", "total"]
]
```

vybírá podle názvu a podmínky.

Naopak:

```python
df.iloc[
    0:5,
    1:3
]
```

vybírá podle pozic.

### Důležitý princip nového DataFrame

Po:

```python
first_five_selected = df.iloc[
    0:5,
    1:5
]
```

obsahuje `first_five_selected` pouze sloupce na pozicích:

```text
1
2
3
4
```

V našem datasetu:

```text
1 → product
2 → category
3 → quantity
4 → unit_price
```

Sloupec:

```text
total
```

je na pozici `6`, takže v `first_five_selected` není.

Proto by nefungovalo:

```python
first_five_selected["total"]
```

Pandas vrátí:

```text
KeyError: 'total'
```

Pokud bychom chtěli vytvořit nový DataFrame obsahující například pozice:

```text
1, 2, 3, 6
```

můžeme `iloc` předat list konkrétních pozic:

```python
first_five_selected = df.iloc[
    0:5,
    [1, 2, 3, 6]
]
```

Výsledkem budou sloupce:

```text
product
category
quantity
total
```

Potom by bylo možné pokračovat přímo nad tímto novým DataFrame:

```python
furniture_summary = first_five_selected.loc[
    (first_five_selected["category"] == "Furniture")
    & (first_five_selected["total"] > 10000),
    ["product", "quantity", "total"]
]
```

---

