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

| Typ | Význam | Příklad |
|---|---|---|
| `str` | text | `"Data Analyst"` |
| `int` | celé číslo | `45` |
| `float` | desetinné číslo | `55500.5` |
| `bool` | pravda / nepravda | `True`, `False` |

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
int("45")       # funguje
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

| Operátor | Význam |
|---|---|
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

`2` znamená zaokrouhlení na dvě desetinná místa.

---

## 8. Porovnávání

```python
salary > 50000
salary < 50000
salary == 55500.5
```

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

## 10. Důležité poznatky

- Python vykonává program postupně shora dolů.
- Proměnná může během programu změnit hodnotu.
- Python automaticky rozpoznává základní datové typy.
- `=` přiřazuje hodnotu.
- `==` porovnává dvě hodnoty.
- `type()` zjistí datový typ.
- `int()` a `float()` mohou převádět hodnoty na číselné typy.
- Výsledkem porovnání je `True` nebo `False`.
- Odsazení v Pythonu určuje strukturu programu.

---

## Lekce 1 — hotovo ✅

Základy: proměnné, datové typy, převody, výpočty, porovnávání a `if / else`.
