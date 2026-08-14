# Python Cheatsheet

Praktický tahák z mého studia Pythonu pro datovou analytiku.

---

## Rychlá orientace

### Závorky v Pythonu

| Závorky | Typické použití | Příklad |
| --- | --- | --- |
| `( )` | volání funkce nebo metody | `print(name)`, `len(sales)`, `calculate_average(salaries)` |
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
calculate_average(salaries)
```

### Funkce — rychlá orientace

Tři důležité věci:

```text
()       → zavolej / spusť funkci
return   → vrať výsledek z funkce
print()  → zobraz hodnotu v terminálu
```

Příklad:

```python
def highest_salary(salaries):
    highest = max(salaries)
    return highest

print(highest_salary(salaries))
```

Průběh:

```text
highest_salary(salaries)
↓
funkce se spustí
↓
max(salaries)
↓
return highest
↓
výsledek se vrátí do print()
↓
print() ho zobrazí
```

Samotné vytvoření funkce ji nespustí:

```python
def welcome():
    print("Welcome!")
```

Funkci je nutné zavolat:

```python
welcome()
```

### Kdy použít `print()` a kdy `return`

`print()` použijeme, pokud chceme hodnotu pouze zobrazit:

```python
def welcome():
    print("Welcome!")
```

`return` použijeme, pokud chceme výsledek dostat z funkce ven a dále s ním pracovat:

```python
def calculate_average(salaries):
    average = sum(salaries) / len(salaries)
    return average

result = calculate_average(salaries)
```

Důležité:

> `return` funkci nespouští. Funkci spouštíme jejím zavoláním pomocí `()`.

### Dvojtečka `:`

Dvojtečka se používá tam, kde začíná nový odsazený blok kódu:

```python
def calculate_average(salaries):
    ...

if salary > 50000:
    ...

elif salary > 40000:
    ...

else:
    ...

for salary in salaries:
    ...
```

Pomůcka:

> Pokud po řádku následuje odsazený blok kódu, často bude na konci řádku `:`.

### Desetinná čísla

Python používá pro desetinná čísla **tečku**, ne čárku:

```python
0.15
1.1
50000.50
```

Ne:

```text
0,15
1,1
```

Čárka má v Pythonu jiný význam, například odděluje argumenty:

```python
round(value, 2)
```

---

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
- `elif` přidává další podmínku mezi `if` a `else`.
- `append()` přidává hodnotu na konec listu.
- `remove()` maže z listu podle hodnoty.
- `pop()` může odstranit položku z listu nebo dictionary.
- `sort()` mění původní list.
- `sorted()` vytvoří nový seřazený list.
- `range()` vytváří posloupnost čísel.
- `enumerate()` poskytuje při průchodu index i hodnotu.
- `def` vytváří vlastní funkci.
- Funkce se spouští jejím zavoláním pomocí `()`.
- Parametr je proměnná, kterou funkce používá pro přijatou hodnotu.
- `return` vrací výsledek z funkce.
- `print()` pouze zobrazuje hodnotu.
- Funkce může volat jinou funkci.
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

---

## 36. Vlastní funkce — `def`

Funkce umožňuje pojmenovat určitý blok kódu a později ho opakovaně spouštět.

Funkci vytvoříme pomocí `def`:

```python
def welcome():
    print("Welcome to Data Analytics!")
```

Samotné vytvoření funkce ji ještě nespustí.

Funkci zavoláme:

```python
welcome()
```

Výstup:

```text
Welcome to Data Analytics!
```

Pokud ji zavoláme dvakrát:

```python
welcome()
welcome()
```

provede se dvakrát.

Důležitý rozdíl:

```python
def welcome():
```

= vytvoření / definice funkce.

```python
welcome()
```

= zavolání / spuštění funkce.

---

## 37. Parametry funkcí

Funkce může při zavolání dostat hodnotu.

```python
def welcome(name):
    print("Welcome", name, "to Data Analytics!")
```

Volání:

```python
welcome("Petr")
welcome("Jana")
```

Výstup:

```text
Welcome Petr to Data Analytics!
Welcome Jana to Data Analytics!
```

`name` je **parametr funkce**.

Při:

```python
welcome("Petr")
```

si můžeme průběh zjednodušeně představit:

```text
name = "Petr"
```

### Parametr vs. argument

V:

```python
def welcome(name):
```

je `name` parametr.

V:

```python
welcome("Petr")
```

je `"Petr"` argument předaný funkci.

Zjednodušeně:

> Parametr je proměnná funkce, do které při jejím zavolání předáváme hodnotu.

---

## 38. Více parametrů

Funkce může přijímat více hodnot:

```python
def employee_info(name, department):
    print("Employee:", name, "Department:", department)
```

Volání:

```python
employee_info("Petr", "Sales")
employee_info("Jana", "IT")
```

Výstup:

```text
Employee: Petr Department: Sales
Employee: Jana Department: IT
```

Při:

```python
employee_info("Petr", "Sales")
```

Python přiřadí:

```text
name       → "Petr"
department → "Sales"
```

Pořadí argumentů je proto důležité.

---

## 39. Funkce může provádět výpočty

Parametr lze použít stejně jako běžnou proměnnou:

```python
def salary_info(salary):
    print("Salary after increase:", round(salary * 1.1, 2))
```

Volání:

```python
salary_info(50000)
```

Výstup:

```text
Salary after increase: 55000.0
```

---

## 40. `return` — vrácení výsledku

Pokud chceme výsledek funkce dále používat, použijeme `return`.

```python
def increase_salary(salary):
    new_salary = salary * 1.1
    return new_salary
```

Volání:

```python
result = increase_salary(50000)
```

Funkce vypočítá:

```text
new_salary = 55000
```

a:

```python
return new_salary
```

vrátí tuto hodnotu ven.

Výsledek se uloží:

```text
result = 55000
```

Potom s ním můžeme dále pracovat:

```python
print("Salary with bonus:", round(result + 5000, 2))
```

---

## 41. `print()` vs. `return`

Tohle je důležitý rozdíl.

### `print()`

```python
def show_salary(salary):
    print(salary)
```

`print()` hodnotu pouze **zobrazí v terminálu**.

### `return`

```python
def get_salary(salary):
    return salary
```

`return` hodnotu **vrátí z funkce ven**.

Můžeme ji potom uložit:

```python
result = get_salary(50000)
```

a dále použít:

```python
bonus_salary = result + 5000
```

Zjednodušeně:

```text
print()  → ukaž výsledek člověku
return   → pošli výsledek zpět programu
```

Důležité:

```text
()       → spusť funkci
return   → vrať výsledek
print()  → zobraz výsledek
```

---

## 42. Funkce pro analytický výpočet

Například funkce pro výpočet průměru:

```python
def calculate_average(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    return average_salary
```

Data:

```python
salaries = [50000, 65000, 48000, 72000, 58000]
```

Volání:

```python
average_salary = calculate_average(salaries)
```

Výpis:

```python
print("Average salary:", average_salary, "Kc")
```

Výsledek:

```text
Average salary: 58600.0 Kc
```

Princip:

```text
list
↓
předání do funkce
↓
výpočet
↓
return
↓
uložení výsledku
↓
další použití
```

---

## 43. Počítadlo — `count`

Pokud nechceme ukládat konkrétní hodnoty, ale pouze zjistit jejich počet, můžeme použít číselné počítadlo:

```python
count = 0
```

Například:

```python
def count_above_average(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    count = 0

    for salary in salaries:
        if salary > average_salary:
            count = count + 1

    return count
```

Volání:

```python
employees_above_average = count_above_average(salaries)
```

Výpis:

```python
print("Employees above average:", employees_above_average)
```

Rozdíl:

```python
count = []
```

vytváří prázdný list.

```python
count = 0
```

vytváří číselné počítadlo.

### Zvýšení počítadla

```python
count = count + 1
```

lze zkráceně napsat:

```python
count += 1
```

Obě varianty znamenají totéž.

---

## 44. `return` a odsazení

Umístění `return` je důležité.

Správně:

```python
def count_above_average(salaries):
    count = 0

    for salary in salaries:
        if salary > 50000:
            count = count + 1

    return count
```

`return` je mimo `for`, takže Python nejprve projde celý list.

Pokud by byl `return` uvnitř cyklu, funkce by mohla skončit příliš brzy.

`return` ukončuje běh funkce a vrací výsledek.

---

## 45. `if` / `elif` / `else`

Pokud potřebujeme více než dvě možnosti, můžeme použít `elif`.

```python
def salary_level(salary):
    if salary >= 80000:
        return "Very high salary"
    elif salary >= 60000:
        return "High salary"
    elif salary >= 40000:
        return "Standard salary"
    else:
        return "Low salary"
```

`elif` znamená:

> jinak pokud

Strukturu můžeme číst:

```text
if    → pokud platí první podmínka
elif  → jinak pokud platí další podmínka
elif  → jinak pokud platí další podmínka
else  → jinak všechny ostatní případy
```

Můžeme použít více `elif`.

---

## 46. Pořadí podmínek

Python vyhodnocuje `if / elif / else` **shora dolů**.

Jakmile najde první podmínku, která je `True`, provede její blok a ostatní větve přeskočí.

Například:

```python
salary = 65000
```

a:

```python
if salary >= 80000:
    ...
elif salary >= 60000:
    ...
elif salary >= 40000:
    ...
```

Python vyhodnotí:

```text
65000 >= 80000 → False
65000 >= 60000 → True
```

a další `elif` už neřeší.

Proto je při vytváření kategorií důležité správné pořadí podmínek.

---

## 47. Hraniční hodnoty — `>` vs. `>=`

Rozdíl:

```python
salary > 80000
```

znamená více než `80000`.

Hodnota přesně `80000` podmínku nesplní.

```python
salary >= 80000
```

znamená `80000` nebo více.

Například pokud chceme:

```text
80000 a více → Very high salary
60000 a více → High salary
40000 a více → Standard salary
pod 40000    → Low salary
```

použijeme:

```python
if salary >= 80000:
    return "Very high salary"
elif salary >= 60000:
    return "High salary"
elif salary >= 40000:
    return "Standard salary"
else:
    return "Low salary"
```

Hraniční hodnoty je vhodné při testování programu kontrolovat:

```text
39999
40000
60000
80000
```

---

## 48. Výchozí hodnota parametru

Parametr může mít výchozí hodnotu:

```python
def calculate_tax(salary, tax_rate=0.15):
    tax = round(salary * tax_rate, 2)
    return tax
```

Pokud druhý argument nezadáme:

```python
calculate_tax(50000)
```

Python použije:

```text
tax_rate = 0.15
```

Výsledek:

```text
7500.0
```

Pokud zadáme jinou hodnotu:

```python
calculate_tax(50000, 0.20)
```

hodnota `0.20` přepíše výchozích `0.15`.

Výsledek:

```text
10000.0
```

---

## 49. Scope — kde proměnná existuje

Parametry a proměnné vytvořené uvnitř funkce jsou běžně dostupné uvnitř této funkce.

```python
def calculate_tax(salary, tax_rate=0.15):
    tax = salary * tax_rate
    return tax
```

Uvnitř funkce známe:

```text
salary
tax_rate
tax
```

Pokud ale mimo funkci napíšeme:

```python
print(tax_rate)
```

Python nemusí tuto proměnnou znát, protože `tax_rate` je parametr funkce.

Zjednodušeně:

```text
uvnitř funkce
┌─────────────────────┐
│ salary              │
│ tax_rate            │
│ tax                 │
└─────────────────────┘

mimo funkci
→ tyto lokální proměnné nejsou automaticky dostupné
```

Pokud chceme hodnotu dostat ven, použijeme `return`.

---

## 50. Funkce může volat jinou funkci

Jedna funkce může použít výsledek jiné funkce.

Nejprve máme:

```python
def calculate_tax(salary, tax_rate=0.15):
    tax = round(salary * tax_rate, 2)
    return tax
```

Potom:

```python
def net_salary(salary, tax_rate=0.15):
    tax = calculate_tax(salary, tax_rate)
    net = salary - tax
    return net
```

Volání:

```python
result = net_salary(80000, 0.25)
```

Průběh:

```text
net_salary(80000, 0.25)
↓
calculate_tax(80000, 0.25)
↓
return 20000
↓
tax = 20000
↓
net = 80000 - 20000
↓
return 60000
```

Výsledek:

```text
60000
```

Výhodou je, že nemusíme stejný výpočet daně psát znovu.

---

## 51. Funkce pracující s listem

Funkci můžeme předat celý list:

```python
salaries = [50000, 65000, 48000, 72000, 58000]
```

Například:

```python
def highest_salary(salaries):
    highest = max(salaries)
    return highest
```

Volání:

```python
highest_salary_result = highest_salary(salaries)
```

Výpis:

```python
print("Highest salary:", highest_salary_result, "Kc")
```

Výsledek:

```text
Highest salary: 72000 Kc
```

Výsledek funkce můžeme použít také přímo v `print()`:

```python
print("Highest salary:", highest_salary(salaries), "Kc")
```

Není vždy nutné vytvářet pomocnou proměnnou.

---

## 52. Zbytečné volání funkce

Pokud funkce něco vrací:

```python
def highest_salary(salaries):
    highest = max(salaries)
    return highest
```

a napíšeme pouze:

```python
highest_salary(salaries)
```

funkce se spustí a vrátí výsledek, ale v běžném skriptu s výsledkem nic dalšího neuděláme.

Praktičtější je například:

```python
result = highest_salary(salaries)
```

nebo:

```python
print(highest_salary(salaries))
```

---

## 53. Funkce skládající více výpočtů

Můžeme vytvořit funkci, která používá několik již existujících funkcí:

```python
def calculate_average(salaries):
    average = round(sum(salaries) / len(salaries), 2)
    return average


def highest_salary(salaries):
    highest = max(salaries)
    return highest


def salary_summary(salaries):
    average = calculate_average(salaries)
    highest = highest_salary(salaries)

    print("Average:", average, "Kc", "/", "Highest:", highest, "Kc")
```

Aby se `salary_summary()` skutečně provedla, musíme ji zavolat:

```python
salary_summary(salaries)
```

Průběh:

```text
salary_summary(salaries)
↓
calculate_average(salaries)
↓
return 58600.0
↓
average = 58600.0
↓
highest_salary(salaries)
↓
return 72000
↓
highest = 72000
↓
print(...)
```

Výstup:

```text
Average: 58600.0 Kc / Highest: 72000 Kc
```

---

## 54. `return` mezi více funkcemi

Pokud jedna funkce zavolá jinou funkci, `return` vrátí výsledek na místo, odkud byla funkce zavolána.

Například:

```python
average = calculate_average(salaries)
```

Funkce:

```python
def calculate_average(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    return average_salary
```

vrátí výsledek zpět:

```text
calculate_average(salaries)
↓
return 58600.0
↓
average = 58600.0
```

Stejný princip:

```python
highest = highest_salary(salaries)
```

vede k:

```text
highest = 72000
```

Důležité:

> `return` vrací výsledek tomu, kdo funkci zavolal.

---

## 55. Vrácení více hodnot

Funkce může vrátit také více hodnot:

```python
def salary_summary(salaries):
    average = calculate_average(salaries)
    highest = highest_salary(salaries)

    return average, highest
```

Výsledky můžeme uložit do dvou proměnných:

```python
average, highest = salary_summary(salaries)
```

Potom můžeme s oběma hodnotami dále pracovat:

```python
difference = highest - average

print("Difference:", difference, "Kc")
```

Rozdíl oproti `print()`:

```python
def salary_summary(salaries):
    print(...)
```

výsledky pouze zobrazí.

Pokud použijeme:

```python
return average, highest
```

můžeme výsledky získat z funkce ven a dále je používat.

---

## 56. Praktický vzor funkce

Jednoduchou analytickou funkci můžeme číst jako:

```text
vstup
↓
parametry
↓
výpočet
↓
případné podmínky / cykly
↓
return
↓
další práce s výsledkem
```

Například:

```python
def calculate_average(salaries):
    average = round(sum(salaries) / len(salaries), 2)
    return average

result = calculate_average(salaries)

print(result)
```

---

## 57. Nejčastější chyby u funkcí

### Chybějící dvojtečka

Špatně:

```python
def calculate_average(salaries)
```

Správně:

```python
def calculate_average(salaries):
```

---

### Funkce je vytvořená, ale není zavolaná

```python
def welcome():
    print("Welcome!")
```

Tento kód samotný nic nevypíše.

Musíme přidat:

```python
welcome()
```

---

### `print()` místo `return`

```python
def calculate_average(salaries):
    print(sum(salaries) / len(salaries))
```

Výsledek se zobrazí, ale funkce ho nevrací pro další práci.

Pokud ho chceme dále používat:

```python
def calculate_average(salaries):
    average = sum(salaries) / len(salaries)
    return average
```

---

### Použití lokální proměnné mimo funkci

```python
def calculate_tax(salary, tax_rate=0.15):
    tax = salary * tax_rate
    return tax

print(tax_rate)
```

`tax_rate` existuje jako parametr uvnitř funkce, ale mimo ni není automaticky dostupný.

---

### Desetinná čárka místo tečky

Špatně:

```python
salary * 1,1
```

Správně:

```python
salary * 1.1
```

---

## 58. Shrnutí funkcí

### Vytvoření funkce

```python
def function_name():
    ...
```

### Zavolání funkce

```python
function_name()
```

### Parametr

```python
def function_name(value):
    ...
```

### Argument

```python
function_name(50000)
```

### Více parametrů

```python
def employee_info(name, department):
    ...
```

### Výchozí parametr

```python
def calculate_tax(salary, tax_rate=0.15):
    ...
```

### Vrácení výsledku

```python
return result
```

### Uložení vráceného výsledku

```python
result = function_name(value)
```

### Přímé použití výsledku

```python
print(function_name(value))
```

### Funkce volající jinou funkci

```python
def net_salary(salary, tax_rate=0.15):
    tax = calculate_tax(salary, tax_rate)
    return salary - tax
```

### Více podmínek

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

Nejdůležitější princip:

```text
def      → vytvořím funkci
()       → zavolám funkci
parametr → funkce přijme hodnotu
return   → funkce vrátí výsledek
print()  → výsledek zobrazím
```
