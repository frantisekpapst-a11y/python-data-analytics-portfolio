## Test 1 — Převod datového typu

### Zadání

Máš proměnnou:

```python
salary = "55000"
```

Chceš zvýšit mzdu o `5000`.

Tento zápis nebude fungovat:

```python
new_salary = salary + 5000
```

### Otázky

1. Proč tento zápis nefunguje?
2. Jak upravíš kód tak, aby výsledkem bylo číslo `60000`?

### Řešení

Hodnota `"55000"` je textový datový typ `str`, zatímco `5000` je číslo typu `int`.

Nejprve je nutné text převést na číslo:

```python
salary = int(salary)
new_salary = salary + 5000

print(new_salary)
```

Výsledek:

```text
60000
```

Pokud bychom chtěli pracovat s desetinnými čísly, můžeme použít:

```python
salary = float(salary)
```

---

## Test 2 — Filtrování hodnot do nového listu

### Zadání

Máš seznam mezd:

```python
salaries = [42000, 55000, 61000, 48000, 72500]
```

Vytvoř nový list `high_salaries`, který bude obsahovat pouze mzdy vyšší než `50000`.

### Řešení

```python
high_salaries = []

for salary in salaries:
    if salary > 50000:
        high_salaries.append(salary)

print(high_salaries)
```

Výsledek:

```text
[55000, 61000, 72500]
```

Princip:

```text
původní list
    ↓
for
    ↓
if
    ↓
append()
    ↓
nový list
```

---

## Test 3 — Indexy a slicing

### Zadání

Máš list:

```python
salaries = [42000, 55000, 61000, 48000, 72500]
```

Urči výsledek:

```python
print(salaries[1:4])
print(salaries[-2])
```

### Řešení

První výraz:

```python
salaries[1:4]
```

vybere hodnoty od indexu `1` včetně do indexu `4` bez něj.

Výsledek:

```text
[55000, 61000, 48000]
```

Druhý výraz:

```python
salaries[-2]
```

vrátí druhou hodnotu od konce.

Výsledek:

```text
48000
```

---

## Test 4 — `sorted()` a změna původního listu

### Zadání

Urči výsledný obsah proměnných `salaries` a `sorted_salaries`:

```python
salaries = [55000, 42000, 72000]

sorted_salaries = sorted(salaries)

salaries.append(60000)
```

### Řešení

Po:

```python
sorted_salaries = sorted(salaries)
```

vznikne nový seřazený list:

```python
sorted_salaries = [42000, 55000, 72000]
```

Původní list zůstává:

```python
salaries = [55000, 42000, 72000]
```

Následně:

```python
salaries.append(60000)
```

změní pouze původní `salaries`.

Finální stav:

```python
salaries = [55000, 42000, 72000, 60000]
sorted_salaries = [42000, 55000, 72000]
```

Důležité:

* `sorted()` vytvoří nový list.
* `append()` změní list, na kterém je metoda zavolána.
* `append()` nepřidává hodnotu automaticky na správnou pozici podle velikosti, ale vždy na konec.

---

## Test 5 — `enumerate()`, index a hodnota

### Zadání

Urči přesný výstup:

```python
sales = [100, 200, 300, 400]

for index, sale in enumerate(sales):
    if sale >= 300:
        print(index, sale)
```

### Řešení

`enumerate()` poskytuje při každém průchodu index a hodnotu.

List:

```text
index 0 → 100
index 1 → 200
index 2 → 300
index 3 → 400
```

Podmínku:

```python
sale >= 300
```

splní pouze hodnoty `300` a `400`.

Výstup:

```text
2 300
3 400
```

Pokud bychom změnili pořadí ve `print()`:

```python
print(sale, index)
```

výsledek by byl:

```text
300 2
400 3
```

Pořadí v:

```python
for index, sale in enumerate(sales):
```

určuje, co se uloží do jednotlivých proměnných.

Pořadí v:

```python
print(sale, index)
```

určuje pouze pořadí výpisu.

---

## Test 6 — vytvoření dictionary a přístup k hodnotám

### Zadání

Vytvoř dictionary `product` s následujícími údaji:

```text
name → Laptop
category → Electronics
price → 25000
in_stock → True
```

Potom vypiš pouze název produktu a jeho cenu.

### Řešení

Dictionary vytvoříme pomocí `{}`:

```python
product = {
    "name": "Laptop",
    "category": "Electronics",
    "price": 25000,
    "in_stock": True
}
```

Ke konkrétní hodnotě přistupujeme pomocí názvu dictionary a klíče v `[]`:

```python
print(product["name"], product["price"])
```

Výstup:

```text
Laptop 25000
```

`product` je celý dictionary.

`"name"` a `"price"` jsou jeho klíče:

```python
product["name"]
product["price"]
```

---

## Test 7 — změna a přidání hodnoty v dictionary

### Zadání

Použij dictionary `product` z předchozího testu.

Změň cenu produktu z `25000` na `23000`.

Potom přidej nový klíč:

```text
discount → True
```

Nakonec vypiš celý dictionary.

### Řešení

Existující hodnotu změníme pomocí jejího klíče:

```python
product["price"] = 23000
```

Nový klíč přidáme stejným způsobem:

```python
product["discount"] = True
```

Potom:

```python
print(product)
```

Výsledek:

```text
{'name': 'Laptop', 'category': 'Electronics', 'price': 23000, 'in_stock': True, 'discount': True}
```

Pokud klíč již existuje:

```python
product["price"] = 23000
```

jeho hodnota se změní.

Pokud klíč neexistuje:

```python
product["discount"] = True
```

Python vytvoří nový klíč a přiřadí mu hodnotu.

---

## Test 8 — odstranění položky z dictionary

### Zadání

Z dictionary `product` odstraň klíč:

```text
discount
```

Potom vypiš celý dictionary.

### Řešení

Pro odstranění klíče můžeme použít:

```python
product.pop("discount")
```

Potom:

```python
print(product)
```

Výsledek:

```text
{'name': 'Laptop', 'category': 'Electronics', 'price': 23000, 'in_stock': True}
```

Metoda:

```python
.pop()
```

odstraní z dictionary zadaný klíč společně s jeho hodnotou.

---

## Test 9 — list dictionaries, `for` a filtrování pomocí `if`

### Zadání

Vytvoř list `products`, který obsahuje tři produkty:

```text
Laptop → Electronics → 23000
Mouse → Electronics → 800
Desk → Furniture → 12000
```

Každý produkt bude samostatný dictionary.

Pomocí `for` a `if` vypiš pouze název a cenu produktů, jejichž cena je vyšší než `10000`.

### Řešení

List obsahující dictionaries:

```python
products = [
    {"name": "Laptop", "category": "Electronics", "price": 23000},
    {"name": "Mouse", "category": "Electronics", "price": 800},
    {"name": "Desk", "category": "Furniture", "price": 12000}
]
```

Potom projdeme jednotlivé produkty:

```python
for product in products:
    if product["price"] > 10000:
        print(product["name"], product["price"])
```

Výstup:

```text
Laptop 23000
Desk 12000
```

`for` postupně uloží každý dictionary do proměnné `product`.

Podmínka:

```python
if product["price"] > 10000:
```

zkontroluje hodnotu pod klíčem `"price"`.

Pokud je podmínka `True`, vypíšeme hodnoty pod klíči:

```python
product["name"]
product["price"]
```

---

## Test 10 — filtrování dictionaries do nového listu

### Zadání

Z existujícího listu `products` vytvoř nový prázdný list:

```python
expensive_products = []
```

Do něj ulož celý dictionary každého produktu, jehož cena je vyšší než `10000`.

Potom nový list projdi pomocí dalšího `for` a vypiš pouze název produktu a jeho kategorii.

### Řešení

Nejprve vytvoříme prázdný list:

```python
expensive_products = []
```

Potom projdeme původní data:

```python
for product in products:
    if product["price"] > 10000:
        expensive_products.append(product)
```

Pokud produkt splní podmínku:

```python
product["price"] > 10000
```

uložíme celý jeho dictionary do nového listu:

```python
expensive_products.append(product)
```

Výsledný list potom znovu projdeme:

```python
for product in expensive_products:
    print(product["name"], product["category"])
```

Výstup:

```text
Laptop Electronics
Desk Furniture
```

První `for` tedy provádí výběr:

```text
products
↓
kontrola price
↓
expensive_products
```

Druhý `for` pracuje už pouze s vybranými produkty:

```text
expensive_products
↓
name + category
↓
výpis
```

Důležitý rozdíl je mezi:

```python
expensive_products.append(product)
```

a:

```python
expensive_products.append(product["name"])
```

První varianta uloží **celý dictionary produktu**.

Druhá varianta by uložila pouze **hodnotu klíče `"name"`**.

---


