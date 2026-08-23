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

Jedná se o **boolean masku**.

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

vrátí celý první řádek.

Naopak:

```python
sorted_orders["total"].max()
```

vrátí pouze nejvyšší hodnotu `total`.

Pandas po řazení zachovává původní indexy.

Pokud chceme index vytvořit znovu:

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

---

# Lekce 7

## Test 1 — Filtrování pomocí AND

### Zadání

Vyber objednávky, které současně splňují:

- `category == "Furniture"`
- `total > 15000`

Výsledek ulož do:

```python
furniture_high_value
```

### Řešení

```python
furniture_high_value = df[
    (df["category"] == "Furniture")
    & (df["total"] > 15000)
]
```

### Vysvětlení

V pandas používáme při kombinaci boolean podmínek:

```text
& → AND
| → OR
~ → NOT
^ → XOR
```

Každá podmínka má být uzavřena ve vlastních závorkách.

---

## Test 2 — OR a NOT

### Zadání

Vytvoř dva filtry.

První vybere objednávky, kde platí alespoň jedna podmínka:

- `quantity >= 4`
- `total > 20000`

Výsledek:

```python
high_quantity_or_value
```

Druhý vybere objednávky, které nejsou z kategorie:

```text
Electronics
```

Výsledek:

```python
not_electronics
```

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

```text
| → OR
~ → NOT
```

Jednodušší varianta druhého filtru:

```python
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

Výsledek ulož do:

```python
selected_products
```

Potom z nich vyber objednávky, kde je `total` mezi:

```text
15000 až 30000 včetně
```

Výsledek:

```python
selected_mid_value
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

```python
isin()
```

ověřuje, zda je hodnota v zadaném seznamu.

```python
between(15000, 30000)
```

znamená:

```text
15000 <= total <= 30000
```

Druhou masku vytváříme nad `selected_products`, protože právě tento DataFrame dále filtrujeme.

---

## Test 4 — Výběr pomocí `loc`

### Zadání

Pomocí `loc` vyber:

- řádky, kde `total > 10000`
- sloupce:
  - `order_id`
  - `product`
  - `category`
  - `total`

Výsledek:

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

Základ:

```python
df.loc[řádky, sloupce]
```

```text
řádky   → podobné SQL WHERE
sloupce → podobné SQL SELECT
```

---

## Test 5 — `iloc` a `loc`

### Zadání

Pomocí `iloc` vyber:

- prvních 5 řádků
- sloupce na pozicích `1`, `2`, `3`, `4`

Výsledek:

```python
first_five_selected
```

Potom pomocí `loc` vyber z původního DataFrame:

- `category == "Furniture"`
- `total > 10000`
- sloupce:
  - `product`
  - `quantity`
  - `total`

Výsledek:

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

`iloc` pracuje s číselnými pozicemi:

```python
df.iloc[řádky, sloupce]
```

U slicingu:

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

A:

```python
1:5
```

znamená:

```text
1, 2, 3, 4
```

Rozdíl:

```text
loc
→ názvy a podmínky

iloc
→ číselné pozice
```

---

# Lekce 8

## Test 1 — Kontrola chybějících hodnot

### Zadání

U DataFrame:

```python
orders
```

zjisti počet chybějících hodnot v každém sloupci a výsledek vypiš.

### Řešení

```python
print(
    orders.isna().sum()
)
```

### Vysvětlení

```python
orders.isna()
```

vrací:

```text
True  → hodnota chybí
False → hodnota nechybí
```

Následné:

```python
.sum()
```

spočítá počet hodnot `True` v jednotlivých sloupcích.

```text
True  = 1
False = 0
```

Proto:

```python
orders.isna().sum()
```

vrací počet chybějících hodnot v každém sloupci.

---

## Test 2 — Odstranění řádků podle konkrétního sloupce

### Zadání

Vytvoř nový DataFrame:

```python
orders_clean
```

ve kterém odstraníš pouze řádky, kde chybí hodnota ve sloupci:

```text
product
```

Použij:

```python
dropna()
subset
```

### Řešení

```python
orders_clean = orders.dropna(
    subset=["product"]
)
```

### Vysvětlení

Samotné:

```python
orders.dropna()
```

by odstranilo každý řádek obsahující alespoň jednu chybějící hodnotu.

Pomocí:

```python
subset=["product"]
```

říkáme Pandas:

```text
při rozhodování o odstranění řádku
kontroluj pouze sloupec product
```

---

## Test 3 — Doplnění textové hodnoty

### Zadání

1. vytvoř kopii `orders` do:

```python
orders_filled
```

2. ve sloupci:

```text
region
```

nahraď chybějící hodnoty textem:

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

### Vysvětlení

```python
orders.copy()
```

vytvoří samostatnou kopii DataFrame.

Rozdíl:

```python
orders_filled = orders
```

znamená:

```text
dvě proměnné
→ jeden DataFrame
```

Naopak:

```python
orders_filled = orders.copy()
```

znamená:

```text
orders
→ původní DataFrame

orders_filled
→ samostatná kopie
```

Tento zápis:

```python
orders_filled["region"]
```

vybere pouze sloupec `region`.

```python
.fillna("Unknown")
```

v něm nahradí chybějící hodnoty.

Důležité je výsledek přiřadit zpět do stejného sloupce:

```python
orders_filled["region"] = ...
```

Ne:

```python
orders_filled = ...
```

protože tím bychom celý DataFrame přepsali výslednou `Series`.

---

## Test 4 — Doplnění číselné hodnoty mediánem

### Zadání

1. vytvoř kopii `orders` do:

```python
orders_filled
```

2. ve sloupci:

```text
unit_price
```

nahraď chybějící hodnotu mediánem tohoto sloupce.

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

### Alternativní řešení s mezikrokem

```python
orders_filled = orders.copy()

median_price = (
    orders_filled["unit_price"].median()
)

orders_filled["unit_price"] = (
    orders_filled["unit_price"]
    .fillna(median_price)
)
```

### Vysvětlení

Nejprve:

```python
orders_filled["unit_price"].median()
```

spočítá medián sloupce `unit_price`.

Potom:

```python
fillna(...)
```

použije tuto hodnotu jako náhradu za `NaN`.

Princip:

```text
vyber sloupec
→ spočítej medián
→ použij ho ve fillna()
```

Mezikrok:

```python
median_price = ...
```

není nutný, ale může zlepšit čitelnost a pomoci při pochopení logiky.

---

## Test 5 — Kompletní cleaning workflow

### Zadání

Vytvoř nový DataFrame:

```python
orders_clean
```

jako kopii `orders`.

Potom:

1. doplň chybějící `region` hodnotou `"Unknown"`
2. doplň chybějící `unit_price` mediánem
3. odstraň řádky, kde chybí `product`
4. vypiš počet zbývajících chybějících hodnot v každém sloupci

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

### Vysvětlení

Správné pořadí:

```text
původní data
→ vytvoření kopie
→ doplnění textové hodnoty
→ doplnění číselné hodnoty
→ odstranění nežádoucího řádku
→ kontrola výsledku
```

Důležité je pokračovat nad stejným pracovním DataFrame:

```python
orders_clean
```

Správně:

```python
orders_clean = orders_clean.dropna(
    subset=["product"]
)
```

Ne:

```python
orders_clean = orders.dropna(
    subset=["product"]
)
```

Ve druhém případě bychom se vrátili k původním datům a přišli o předchozí změny provedené v `orders_clean`.

---

# Lekce 9

## Test 1 — Chybějící hodnoty

### Zadání

Máš DataFrame:

```python
import pandas as pd

data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "product": ["Laptop", "Monitor", None, "Desk", "Mouse"],
    "quantity": [2, None, 1, 3, None],
    "unit_price": [25000, 7000, 15000, 12000, 800]
}

df = pd.DataFrame(data)
```

Proveď následující:

1. zjisti počet chybějících hodnot v každém sloupci
2. odstraň řádky, kde chybí `product`
3. chybějící hodnoty ve sloupci `quantity` nahraď hodnotou `1`
4. výsledek ulož do:

```python
clean_df
```

### Řešení

```python
print(df.isna().sum())

df = df.dropna(
    subset=["product"]
)

df["quantity"] = (
    df["quantity"]
    .fillna(1)
)

clean_df = df
```

### Vysvětlení

```python
df.isna().sum()
```

zjistí počet chybějících hodnot v jednotlivých sloupcích.

```python
df.dropna(
    subset=["product"]
)
```

odstraní pouze řádky, kde chybí hodnota ve sloupci `product`.

Parametr:

```python
subset=["product"]
```

říká Pandas, že při rozhodování o odstranění řádku má kontrolovat pouze tento sloupec.

```python
df["quantity"].fillna(1)
```

nahradí chybějící hodnoty ve sloupci `quantity` číslem `1`.

Důležitý rozdíl:

```python
1
```

je číslo.

```python
"1"
```

je textový řetězec.

Proto při práci s číselným sloupcem používáme:

```python
.fillna(1)
```

---

## Test 2 — Duplicity

### Zadání

Máš DataFrame:

```python
data = {
    "order_id": [1001, 1002, 1002, 1003, 1004, 1004],
    "product": ["Laptop", "Monitor", "Monitor", "Desk", "Mouse", "Mouse"],
    "quantity": [1, 2, 2, 1, 3, 3]
}

df = pd.DataFrame(data)
```

Proveď následující:

1. zjisti, které řádky jsou duplicitní
2. zjisti počet duplicitních řádků
3. odstraň duplicity
4. výsledek ulož do:

```python
clean_df
```

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

### Vysvětlení

```python
df.duplicated()
```

vrací boolean masku:

```text
False
False
True
False
False
True
```

Hodnota:

```text
True
```

znamená, že daný řádek je duplicitní vůči některému předchozímu řádku.

Použití:

```python
df[df.duplicated()]
```

zobrazí pouze duplicitní řádky.

```python
df.duplicated().sum()
```

spočítá jejich počet.

Platí:

```text
True  = 1
False = 0
```

Duplicity odstraníme pomocí:

```python
df.drop_duplicates()
```

Důležité je výsledek uložit:

```python
clean_df = df.drop_duplicates()
```

Samotné:

```python
df.drop_duplicates()
```

vytvoří nový DataFrame, ale původní `df` automaticky nezmění.

---

## Test 3 — Datové typy

### Zadání

Máš DataFrame:

```python
data = {
    "order_id": ["1001", "1002", "1003"],
    "quantity": ["2", "3", "1"],
    "unit_price": ["25000.5", "7000", "12000"]
}

df = pd.DataFrame(data)
```

Všechny hodnoty jsou načtené jako text.

Převeď:

1. `order_id` na celé číslo
2. `quantity` na celé číslo
3. `unit_price` na desetinné číslo
4. zobraz výsledné datové typy sloupců

### Řešení

```python
df["order_id"] = df["order_id"].astype(int)

df["quantity"] = df["quantity"].astype(int)

df["unit_price"] = df["unit_price"].astype(float)

print(df.dtypes)
```

### Vysvětlení

Metoda:

```python
.astype()
```

slouží ke změně datového typu hodnot v Pandas objektu.

Například:

```python
df["quantity"].astype(int)
```

převede celý sloupec `quantity` na celá čísla.

```python
int
```

znamená celé číslo.

```python
float
```

znamená desetinné číslo.

Proto:

```python
df["unit_price"] = df["unit_price"].astype(float)
```

převede `unit_price` na desetinný číselný typ.

Datové typy zobrazíme pomocí:

```python
df.dtypes
```

> Poznámka: `astype()` nebylo součástí původně procvičené látky Lekce 9. Tento test proto bereme jako doplňkový příklad převodu datových typů, nikoli jako požadovanou znalost z Lekce 9.

---

## Test 4 — Validace hodnot

### Zadání

Máš DataFrame:

```python
data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "product": ["Laptop", "Monitor", "Desk", "Mouse", "Keyboard"],
    "quantity": [2, -1, 3, 0, 5],
    "unit_price": [25000, 7000, -12000, 800, 1500]
}

df = pd.DataFrame(data)
```

Business pravidla říkají:

```text
quantity > 0
unit_price > 0
```

Vytvoř DataFrame:

```python
invalid_rows
```

který bude obsahovat všechny řádky, kde je:

- `quantity` neplatné

nebo

- `unit_price` neplatné

### Řešení

```python
invalid_rows = df[
    (df["quantity"] <= 0)
    | (df["unit_price"] <= 0)
]
```

### Vysvětlení

Business pravidla definují platné hodnoty:

```text
quantity > 0
unit_price > 0
```

Neplatné hodnoty jsou tedy jejich opak:

```text
quantity <= 0
unit_price <= 0
```

Proto použijeme:

```python
df["quantity"] <= 0
```

a:

```python
df["unit_price"] <= 0
```

Chceme najít řádek, kde je neplatná alespoň jedna z těchto hodnot.

Proto používáme:

```python
|
```

což v Pandas znamená:

```text
OR
```

Každá podmínka musí být uzavřena ve vlastních kulatých závorkách:

```python
(df["quantity"] <= 0)
| (df["unit_price"] <= 0)
```

Obecný zápis:

```python
df[
    (podmínka_1)
    | (podmínka_2)
]
```

Pro `AND` bychom použili:

```python
df[
    (podmínka_1)
    & (podmínka_2)
]
```

---

## Test 5 — Kompletní cleaning workflow

### Zadání

Máš DataFrame:

```python
data = {
    "order_id": [1001, 1002, 1002, 1003, 1004, 1005],
    "product": ["Laptop", "Monitor", "Monitor", None, "Desk", "Mouse"],
    "quantity": [2, 1, 1, 3, None, -2],
    "unit_price": [25000, 7000, 7000, 12000, 10000, 800]
}

df = pd.DataFrame(data)
```

Vytvoř čistý dataset.

Postupně:

1. zkontroluj chybějící hodnoty
2. odstraň duplicity
3. odstraň řádky, kde chybí `product`
4. chybějící `quantity` nahraď hodnotou `1`
5. ponech pouze řádky, kde platí:

```python
quantity > 0
```

6. vytvoř nový sloupec:

```python
total
```

jako:

```text
quantity × unit_price
```

7. výsledek ulož do:

```python
clean_df
```

8. nakonec zobraz výsledný DataFrame a jeho základní informace

### Řešení

```python
print(
    df.isna().sum()
)

df = df.drop_duplicates()

df = df.dropna(
    subset=["product"]
)

df["quantity"] = (
    df["quantity"]
    .fillna(1)
)

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

### Vysvětlení

Nejprve zkontrolujeme chybějící hodnoty:

```python
df.isna().sum()
```

Potom odstraníme duplicitní řádky:

```python
df = df.drop_duplicates()
```

Řádky bez produktu odstraníme pomocí:

```python
df = df.dropna(
    subset=["product"]
)
```

Chybějící množství doplníme číslem `1`:

```python
df["quantity"] = (
    df["quantity"]
    .fillna(1)
)
```

Potom aplikujeme business validační pravidlo:

```python
df["quantity"] > 0
```

a ponecháme pouze platné řádky:

```python
df = df[
    df["quantity"] > 0
]
```

Nový sloupec:

```python
total
```

vytvoříme výpočtem po jednotlivých řádcích:

```python
df["total"] = (
    df["quantity"]
    * df["unit_price"]
)
```

Nakonec pracovní DataFrame uložíme jako:

```python
clean_df = df
```

a provedeme závěrečnou kontrolu:

```python
print(clean_df)

clean_df.info()
```

Celý workflow tedy odpovídá:

```text
raw data

→ kontrola missing values

→ odstranění duplicit

→ řešení chybějících hodnot

→ validace business pravidel

→ odstranění neplatných řádků

→ vytvoření odvozeného sloupce

→ kontrola výsledku
```

Tento postup odpovídá běžnému principu:

```text
inspect
→ clean
→ validate
→ transform
→ verify
```

tedy:

```text
zkontrolovat
→ vyčistit
→ validovat
→ transformovat
→ ověřit
```

---
