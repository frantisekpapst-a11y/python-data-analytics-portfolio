# Python Cheatsheet

Praktický tahák z mého studia Pythonu pro datovou analytiku.

---

## 1. Výpis hodnoty — `print()`

```python
print("Ahoj, Pythone!")
print(salary)
```

`print()` vypíše text nebo hodnotu proměnné.

---

## 2. Proměnné

```python
name = "František"
age = 45
salary = 55500.5
is_data_analyst = True
```

Python datový typ rozpozná podle přiřazené hodnoty.

Hodnotu proměnné lze jednoduše změnit:

```python
salary = 55500.5
salary = 40000
```

Od druhého přiřazení má `salary` hodnotu `40000`.

---

## 3. Základní datové typy

| Typ     | Význam            | Příklad          |
| ------- | ----------------- | ---------------- |
| `str`   | text              | `"Data Analyst"` |
| `int`   | celé číslo        | `45`             |
| `float` | desetinné číslo   | `55500.5`        |
| `bool`  | pravda / nepravda | `True`, `False`  |

---

## 4. Kontrola datového typu — `type()`

```python
print(type(salary))
```

Například:

```python
salary = 55500.5
print(type(salary))
```

Výsledek:

```text
<class 'float'>
```

---

## 5. Převod datových typů

Text na celé číslo:

```python
age_text = "45"
age_number = int(age_text)
```

Text na desetinné číslo:

```python
salary_text = "55500.5"
salary_number = float(salary_text)
```

Další základní převody:

```python
str()
int()
float()
bool()
```

Pozor: ne každý text lze převést na číslo.

```python
int("45")        # funguje
int("František") # chyba
```

---

## 6. Výpočty

```python
salary = 55500.5
bonus = 4000

total_salary = salary + bonus
annual_salary = salary * 12
annual_bonus = bonus * 12
annual_income = annual_salary + annual_bonus
```

Základní operátory:

| Operátor | Význam   |
| -------- | -------- |
| `+`      | sčítání  |
| `-`      | odčítání |
| `*`      | násobení |
| `/`      | dělení   |

---

## 7. Zaokrouhlení — `round()`

```python
bonus_percentage = annual_bonus / annual_income * 100
print(round(bonus_percentage, 2))
```

`2` znamená zaokrouhlení maximálně na dvě desetinná místa.

`round()` neznamená, že Python vždy zobrazí dvě desetinná místa.

```python
round(123.4567, 2)  # 123.46
round(46200.0, 2)   # 46200.0
```

---

## 8. Porovnávání

```python
salary > 50000
salary < 50000
salary == 55500.5
salary <= 50000
salary >= 50000
salary != 50000
```

| Operátor | Význam           |
| -------- | ---------------- |
| `>`      | větší než        |
| `<`      | menší než        |
| `>=`     | větší nebo rovno |
| `<=`     | menší nebo rovno |
| `==`     | rovná se         |
| `!=`     | nerovná se       |

Výsledkem porovnání je:

```python
True
False
```

Pozor na rozdíl:

```python
salary = 50000   # přiřazení hodnoty
salary == 50000  # porovnání hodnot
```

---

## 9. Podmínky — `if` / `else`

```python
if salary > 50000:
    print("Salary is above 50000")
else:
    print("Salary is 50000 or less")
```

`if` = pokud je podmínka `True`, proveď následující blok.

`else` = co se má stát, pokud podmínka `True` není.

### Odsazení je součást syntaxe Pythonu

```python
if salary > 50000:
    print("Salary is above 50000")
```

Odsazený řádek patří pod `if`. Standardně se používají 4 mezery.

---

## 10. List — seznam hodnot

List umožňuje uložit více hodnot do jedné proměnné.

```python
salaries = [42000, 55500, 61000, 48000, 72500]
```

Datový typ:

```python
print(type(salaries))
```

Výsledek:

```text
<class 'list'>
```

List může obsahovat čísla, text i různé datové typy.

```python
names = ["Petr", "Jana", "Eva"]
employee = ["Petr", 45000, True]
```

---

## 11. Indexy v listu

Python počítá indexy od `0`.

```python
salaries = [42000, 55500, 61000, 48000, 72500]

print(salaries[0])  # 42000
print(salaries[2])  # 61000
print(salaries[4])  # 72500
```

Lze počítat také od konce:

```python
print(salaries[-1])  # poslední hodnota
print(salaries[-2])  # předposlední hodnota
print(salaries[-3])  # třetí hodnota od konce
```

---

## 12. Slicing — výběr části listu

```python
salaries[1:4]
```

Vybere hodnoty od indexu `1` do indexu `4`, ale index `4` už nezahrne.

```python
salaries[:3]   # od začátku po index 3
salaries[2:]   # od indexu 2 do konce
```

Příklad:

```python
salaries = [42000, 55500, 61000, 48000, 72500]

print(salaries[1:4])
```

Výsledek:

```text
[55500, 61000, 48000]
```

---

## 13. Základní funkce pro list

```python
len(salaries)
min(salaries)
max(salaries)
sum(salaries)
```

| Funkce  | Význam                  |
| ------- | ----------------------- |
| `len()` | počet hodnot            |
| `min()` | nejnižší hodnota        |
| `max()` | nejvyšší hodnota        |
| `sum()` | součet hodnot           |

Výpočet průměru:

```python
average_salary = sum(salaries) / len(salaries)
print(average_salary)
```

Průměr zaokrouhlený na dvě desetinná místa:

```python
average_salary = round(sum(salaries) / len(salaries), 2)
```

---

## 14. Přidání hodnoty — `append()`

```python
salaries.append(50000)
```

`append()` přidá jednu hodnotu na konec listu.

```python
salaries = [42000, 55500]
salaries.append(50000)

print(salaries)
```

Výsledek:

```text
[42000, 55500, 50000]
```

---

## 15. Mazání hodnot — `remove()` a `pop()`

### `remove()`

Odstraní první výskyt konkrétní hodnoty:

```python
salaries.remove(50000)
```

Pokud se hodnota v listu nachází vícekrát, `remove()` odstraní pouze první výskyt.

### `pop()`

Odstraní hodnotu podle indexu:

```python
salaries.pop(2)
```

Tím odstraníme hodnotu na indexu `2`.

Bez indexu odstraní poslední hodnotu:

```python
salaries.pop()
```

---

## 16. Řazení — `sort()` a `sorted()`

### `sort()`

Změní přímo původní list.

Vzestupně:

```python
salaries.sort()
```

Sestupně:

```python
salaries.sort(reverse=True)
```

`reverse=True` znamená, že se zapne opačné pořadí.

```python
reverse=False  # vzestupně
reverse=True   # sestupně
```

### `sorted()`

Vytvoří nový seřazený list a původní ponechá beze změny.

```python
salaries = [42000, 55500, 61000, 48000, 72500]

sorted_salaries = sorted(salaries)

print(salaries)
print(sorted_salaries)
```

---

## 17. Cyklus — `for`

`for` postupně projde jednotlivé hodnoty.

```python
for salary in salaries:
    print(salary)
```

Proměnnou `salary` není nutné předem vytvářet. Python jí při každém průchodu přiřadí aktuální hodnotu z `salaries`.

```python
for salary in salaries:
```

lze číst jako:

> Pro každou hodnotu v `salaries` ji dočasně pojmenuj `salary`.

Název pomocné proměnné si volíme podle významu dat:

```python
for sale in sales:
    print(sale)
```

---

## 18. `for` + `if` — filtrování hodnot

```python
salaries = [42000, 55500, 61000, 48000, 72500]

for salary in salaries:
    if salary > 50000:
        print(salary)
```

Python postupně projde celý list a podmínku vyhodnotí pro každou hodnotu.

---

## 19. Vytvoření nového listu podle podmínky

Nejprve vytvoříme prázdný list:

```python
high_salaries = []
```

Potom do něj ukládáme pouze hodnoty, které splní podmínku:

```python
for salary in salaries:
    if salary > 50000:
        high_salaries.append(salary)
```

Výsledek:

```python
print(high_salaries)
```

```text
[55500, 61000, 72500]
```

Průměr pouze z vyfiltrovaných hodnot:

```python
average_high_salary = sum(high_salaries) / len(high_salaries)
print(average_high_salary)
```

Princip:

**původní data → podmínka → nový list → výpočet**

---

## 20. Transformace hodnot pomocí `for`

Pomocí cyklu můžeme hodnoty nejen filtrovat, ale také přepočítávat.

Například zvýšení všech mezd o 10 %:

```python
increased_salaries = []

for salary in salaries:
    new_salary = round(salary * 1.1, 2)
    increased_salaries.append(new_salary)

print(increased_salaries)
```

Princip:

**vezmi hodnotu → proveď výpočet → ulož nový výsledek**

---

## 21. `range()`

`range()` vytváří posloupnost čísel.

```python
for number in range(5):
    print(number)
```

Výsledek:

```text
0
1
2
3
4
```

Základní varianty:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Příklady:

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 6)      # 2, 3, 4, 5
range(2, 10, 2)  # 2, 4, 6, 8
```

Stejně jako u slicingu je počáteční hodnota zahrnuta, koncová nikoliv.

---

## 22. `enumerate()` — index a hodnota

Pokud potřebujeme při průchodu listem znát zároveň index i hodnotu:

```python
salaries = [42000, 55500, 61000, 48000, 72500]

for index, salary in enumerate(salaries):
    print(index, salary)
```

Výsledek:

```text
0 42000
1 55500
2 61000
3 48000
4 72500
```

`index` obsahuje pozici hodnoty a `salary` samotnou hodnotu.

---

## 23. Praktický analytický vzor

Příklad práce s měsíčními tržbami:

```python
sales = [125000, 98000, 143000, 87000, 156000, 112000]

print(len(sales))
print(min(sales))
print(max(sales))
print(sum(sales))

average_sale = round(sum(sales) / len(sales), 2)
print(average_sale)

high_sales = []

for sale in sales:
    if sale > 120000:
        high_sales.append(sale)

print(high_sales)

average_high_sales = round(sum(high_sales) / len(high_sales), 2)
print(average_high_sales)
```

Tento postup kombinuje několik základních kroků datové analýzy:

**data → základní statistiky → filtrování → nový dataset → další výpočet**

---

## 24. Důležité poznatky

- Python vykonává program postupně shora dolů.
- Proměnná může během programu změnit hodnotu.
- Python automaticky rozpoznává základní datové typy.
- `=` přiřazuje hodnotu.
- `==` porovnává dvě hodnoty.
- `<=` znamená menší nebo rovno.
- `>=` znamená větší nebo rovno.
- Výsledkem porovnání je `True` nebo `False`.
- `list` ukládá více hodnot do jedné proměnné.
- Indexování v Pythonu začíná od `0`.
- Slicing umožňuje vybrat část listu.
- `append()` přidává hodnotu na konec listu.
- `remove()` maže podle hodnoty.
- `pop()` maže podle indexu.
- `sort()` mění původní list.
- `sorted()` vytváří nový seřazený list.
- `for` postupně prochází hodnoty.
- `for` a `if` lze kombinovat pro filtrování dat.
- Pomocí `append()` lze výsledky postupně ukládat do nového listu.
- `range()` vytváří posloupnost čísel.
- `enumerate()` poskytuje při průchodu index i hodnotu.
- Odsazení v Pythonu určuje strukturu programu.
