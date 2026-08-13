# Python Cheatsheet

Praktický tahák z mého studia Pythonu pro datovou analytiku.

---

## Rychlá orientace

### Závorky v Pythonu

| Závorky | Typické použití | Příklad |
| --- | --- | --- |
| `( )` | volání funkce nebo metody | `print(name)`, `len(sales)` |
| `[ ]` | list nebo přístup pomocí indexu/klíče | `[1, 2, 3]`, `employee["name"]` |
| `{ }` | vytvoření dictionary | `{"name": "Petr", "salary": 50000}` |

Důležité:

```python
employee = {
    "name": "Petr",
    "salary": 50000
}
```

Dictionary se **vytváří pomocí `{}`**, ale k jeho konkrétní hodnotě přistupujeme pomocí **`[]`**:

```python
employee["name"]
employee["salary"]
```

Metody a funkce používají `()`:

```python
print(employee)
employee.keys()
employee.pop("salary")
```

### Základní principy

- Python vykonává program postupně shora dolů.
- `=` přiřazuje hodnotu.
- `==` porovnává dvě hodnoty.
- `!=` znamená nerovná se.
- `>` a `<` znamenají větší a menší.
- `>=` a `<=` zahrnují také rovnost.
- Výsledkem porovnání je `True` nebo `False`.
- Indexování začíná od `0`.
- `list` ukládá více hodnot v určitém pořadí.
- `dictionary` ukládá dvojice **klíč → hodnota**.
- `for` postupně prochází data.
- `if` rozhoduje, zda se má určitý blok kódu provést.
- `append()` přidává hodnotu na konec listu.
- `remove()` maže z listu podle hodnoty.
- `pop()` může odstranit položku z listu nebo dictionary.
- `sort()` mění původní list.
- `sorted()` vytvoří nový seřazený list.
- `range()` vytváří posloupnost čísel.
- `enumerate()` poskytuje při průchodu index i hodnotu.
- Odsazení určuje strukturu programu.

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

| Typ | Význam | Příklad |
| --- | --- | --- |
| `str` | text | `"Data Analyst"` |
| `int` | celé číslo | `45` |
| `float` | desetinné číslo | `55500.5` |
| `bool` | pravda / nepravda | `True`, `False` |
| `list` | seznam hodnot | `[42000, 50000]` |
| `dict` | klíče a hodnoty | `{"name": "Petr"}` |

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

Hodnotu můžeme převést také přímo a uložit zpět do stejné proměnné:

```python
salary = "55500.5"
salary = float(salary)
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
int("45")         # funguje
int("František")  # chyba
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

| Operátor | Význam |
| --- | --- |
| `+` | sčítání |
| `-` | odčítání |
| `*` | násobení |
| `/` | dělení |

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

| Operátor | Význam |
| --- | --- |
| `>` | větší než |
| `<` | menší než |
| `>=` | větší nebo rovno |
| `<=` | menší nebo rovno |
| `==` | rovná se |
| `!=` | nerovná se |

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
salaries[:3]
salaries[2:]
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

| Funkce | Význam |
| --- | --- |
| `len()` | počet hodnot |
| `min()` | nejnižší hodnota |
| `max()` | nejvyšší hodnota |
| `sum()` | součet hodnot |

Výpočet průměru:

```python
average_salary = sum(salaries) / len(salaries)
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

### `pop()`

Odstraní hodnotu podle indexu:

```python
salaries.pop(2)
```

Bez indexu odstraní poslední hodnotu:

```python
salaries.pop()
```

---

## 16. Řazení — `sort()` a `sorted()`

### `sort()`

Změní přímo původní list.

```python
salaries.sort()
```

Sestupně:

```python
salaries.sort(reverse=True)
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

Proměnnou `salary` není nutné předem vytvářet.

```python
for salary in salaries:
```

lze číst jako:

> Pro každou hodnotu v `salaries` ji dočasně pojmenuj `salary`.

---

## 18. `for` + `if` — filtrování hodnot

```python
for salary in salaries:
    if salary > 50000:
        print(salary)
```

Python postupně projde celý list a podmínku vyhodnotí pro každou hodnotu.

Princip je podobný filtrování pomocí `WHERE` v SQL, i když `if` je obecná podmínka Pythonu.

---

## 19. Vytvoření nového listu podle podmínky

```python
high_salaries = []

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

Princip:

**původní data → podmínka → nový list → výpočet**

---

## 20. Transformace hodnot pomocí `for`

Například zvýšení všech mezd o 10 %:

```python
increased_salaries = []

for salary in salaries:
    new_salary = round(salary * 1.1, 2)
    increased_salaries.append(new_salary)
```

Princip:

**vezmi hodnotu → proveď výpočet → ulož nový výsledek**

---

## 21. `range()`

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

---

## 22. `enumerate()` — index a hodnota

```python
salaries = [42000, 55500, 61000]

for index, salary in enumerate(salaries):
    print(index, salary)
```

Výsledek:

```text
0 42000
1 55500
2 61000
```

`index` obsahuje pozici a `salary` hodnotu.

Pořadí ve `print()` můžeme změnit:

```python
print(salary, index)
```

To změní pouze pořadí výpisu.

---

## 23. Dictionary — slovník

Dictionary ukládá data jako dvojice:

**klíč → hodnota**

```python
employee = {
    "name": "Petr",
    "department": "Sales",
    "salary": 45000,
    "active": True
}
```

Datový typ:

```python
print(type(employee))
```

Výsledek:

```text
<class 'dict'>
```

Na rozdíl od jednoduchého listu mají jednotlivé hodnoty svůj význam popsaný klíčem.

```python
employee["name"]
employee["salary"]
```

---

## 24. Přístup k hodnotám dictionary

```python
print(employee["name"])
print(employee["salary"])
print(employee["department"])
```

Výstup:

```text
Petr
45000
Sales
```

Hranaté závorky zde neznamenají vytvoření listu.

```python
employee["salary"]
```

znamená:

> Z dictionary `employee` vezmi hodnotu pod klíčem `"salary"`.

---

## 25. Změna hodnoty v dictionary

```python
employee["salary"] = 50000
```

Původní hodnota klíče `"salary"` se přepíše.

```python
print(employee)
```

Výsledek obsahuje:

```text
'salary': 50000
```

Samostatné:

```python
salary = 50000
```

by pouze vytvořilo nebo změnilo proměnnou `salary`.

Dictionary `employee` by to nezměnilo.

---

## 26. Přidání nového klíče do dictionary

Pokud klíč ještě neexistuje, Python ho vytvoří:

```python
employee["city"] = "Prague"
```

Dictionary nyní obsahuje také:

```text
'city': 'Prague'
```

Stejná syntaxe tedy může:

- změnit existující hodnotu,
- přidat nový klíč.

---

## 27. Odstranění klíče — `pop()`

```python
employee.pop("city")
```

Odstraní klíč `"city"` společně s jeho hodnotou.

```python
print(employee)
```

---

## 28. Klíče, hodnoty a dvojice — `keys()`, `values()`, `items()`

### Klíče

```python
print(employee.keys())
```

Například:

```text
dict_keys(['name', 'department', 'salary', 'active'])
```

### Hodnoty

```python
print(employee.values())
```

Například:

```text
dict_values(['Petr', 'Sales', 50000, True])
```

### Klíče a hodnoty společně

```python
print(employee.items())
```

Například:

```text
dict_items([('name', 'Petr'), ('department', 'Sales'), ('salary', 50000), ('active', True)])
```

`items()` poskytuje dvojice:

```text
klíč → hodnota
```

---

## 29. Procházení dictionary pomocí `for`

Pomocí `.items()` můžeme současně získat klíč a jeho hodnotu:

```python
for key, value in employee.items():
    print(key, value)
```

Výstup:

```text
name Petr
department Sales
salary 50000
active True
```

Princip:

```text
1. průchod → name + Petr
2. průchod → department + Sales
3. průchod → salary + 50000
4. průchod → active + True
```

---

## 30. List dictionaries

Pro data podobná tabulce můžeme vytvořit list, který obsahuje více dictionaries.

```python
employees = [
    {"name": "Petr", "department": "Sales", "salary": 50000},
    {"name": "Jana", "department": "IT", "salary": 65000},
    {"name": "Martin", "department": "Sales", "salary": 48000},
    {"name": "Eva", "department": "IT", "salary": 72000}
]
```

Zjednodušeně:

- celý `employees` = tabulka,
- jeden dictionary = jeden řádek,
- klíče = názvy sloupců,
- hodnoty = hodnoty v daném řádku.

Přibližná analogie s SQL tabulkou:

| name | department | salary |
| --- | --- | ---: |
| Petr | Sales | 50000 |
| Jana | IT | 65000 |
| Martin | Sales | 48000 |
| Eva | IT | 72000 |

---

## 31. Přístup k dictionary uvnitř listu

Druhý zaměstnanec:

```python
print(employees[1])
```

Výsledek:

```text
{'name': 'Jana', 'department': 'IT', 'salary': 65000}
```

Pouze plat druhého zaměstnance:

```python
print(employees[1]["salary"])
```

Výsledek:

```text
65000
```

Čteme postupně:

```python
employees[1]["salary"]
```

1. `employees[1]` → vezmi druhý dictionary,
2. `["salary"]` → z něj vezmi hodnotu klíče `"salary"`.

---

## 32. Procházení listu dictionaries

```python
for employee in employees:
    print(employee["name"])
```

Výstup:

```text
Petr
Jana
Martin
Eva
```

Při každém průchodu obsahuje `employee` jeden celý dictionary.

---

## 33. Filtrování listu dictionaries

Pouze zaměstnanci z IT:

```python
for employee in employees:
    if employee["department"] == "IT":
        print(employee["name"])
```

Výstup:

```text
Jana
Eva
```

Pouze zaměstnanci s platem nad `50000`:

```python
for employee in employees:
    if employee["salary"] > 50000:
        print(employee["name"], employee["salary"])
```

Výstup:

```text
Jana 65000
Eva 72000
```

---

## 34. Filtrování dictionaries do nového listu

```python
high_paid_employees = []

for employee in employees:
    if employee["salary"] > 50000:
        high_paid_employees.append(employee)
```

Do nového listu se ukládá celý dictionary zaměstnance.

Výsledek můžeme projít dalším cyklem:

```python
for employee in high_paid_employees:
    print(
        employee["name"],
        employee["department"],
        employee["salary"]
    )
```

Výstup:

```text
Jana IT 65000
Eva IT 72000
```

Rozdíl:

```python
high_paid_employees.append(employee)
```

uloží celý dictionary.

```python
high_paid_employees.append(employee["name"])
```

uloží pouze jméno.

---

## 35. Praktický analytický vzor

Při práci s listem dictionaries se často opakuje tento postup:

```python
products = [
    {"name": "Laptop", "category": "Electronics", "price": 23000},
    {"name": "Mouse", "category": "Electronics", "price": 800},
    {"name": "Desk", "category": "Furniture", "price": 12000}
]

expensive_products = []

for product in products:
    if product["price"] > 10000:
        expensive_products.append(product)

for product in expensive_products:
    print(product["name"], product["category"])
```

Výstup:

```text
Laptop Electronics
Desk Furniture
```

Princip:

```text
původní data
↓
for
↓
if
↓
výběr požadovaných záznamů
↓
nový list
↓
další práce s výsledkem
```

To je jeden ze základních vzorů práce s daty v Pythonu.
