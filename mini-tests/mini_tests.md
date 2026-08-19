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

## Shrnutí lekce 6

V minitestech byly procvičeny následující dovednosti:

```python
pd.read_csv()

df.head()
df.shape
df.columns
df.info()

df["new_column"] = ...

.sum()
.mean()
.min()
.max()

df[podmínka]

.sort_values()

.to_csv()
.to_json()
```

### Hlavní analytický princip

```text
DataFrame
→ kontrola
→ transformace
→ výpočet
→ filtr
→ řazení
→ export
```

### Výsledek minitestů

```text
Test 1: 5 / 5
Test 2: 5 / 5
Test 3: 5 / 5
Test 4: 4,5 / 5
Test 5: 4 / 5

Celkem: 23,5 / 25
```

### Co dále procvičovat

* přesně rozlišovat mezi hodnotou a celým řádkem
* sledovat, nad kterým DataFrame právě provádíme operaci
* používat výstižné názvy proměnných
* věnovat pozornost pořadí jednotlivých kroků analýzy

Další téma:

```text
Lekce 7
→ filtrování s více podmínkami
→ &, |, ~
→ isin()
→ loc a iloc
```
