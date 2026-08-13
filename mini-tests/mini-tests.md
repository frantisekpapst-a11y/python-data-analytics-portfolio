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
