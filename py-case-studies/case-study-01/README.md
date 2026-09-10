# Case Study 01 - Employee Salary Analysis

Malá Python case study zaměřená na základní analýzu mezd zaměstnanců.

Cílem projektu je procvičit základy Pythonu na jednoduchém datasetu s businessovým kontextem a odpovědět na několik praktických otázek týkajících se zaměstnanců, mezd a jednotlivých oddělení.

---

## Cíl analýzy

Analýza odpovídá na následující otázky:

- Kolik zaměstnanců obsahuje dataset?
- Jaká je průměrná mzda?
- Kdo má nejvyšší mzdu?
- Kdo má nejnižší mzdu?
- Kteří zaměstnanci mají mzdu vyšší než celkový průměr?
- Kolik zaměstnanců má mzdu vyšší než průměr?
- Kolik zaměstnanců pracuje v oddělení Sales?
- Jaká je průměrná mzda v Sales?
- Jaká je průměrná mzda v IT?
- Které z oddělení Sales a IT má vyšší průměrnou mzdu?
- Jaké procento všech zaměstnanců pracuje v Sales?
- Jaký je rozdíl mezi průměrnou mzdou v IT a Sales?
- Které oddělení má nejvyšší průměrnou mzdu?

---

## Dataset

Dataset obsahuje 8 zaměstnanců a tři základní údaje:

- `name` — jméno zaměstnance
- `department` — oddělení
- `salary` — mzda

V datasetu jsou zastoupena oddělení:

- Sales
- IT
- Finance
- HR

Data jsou vytvořena přímo v Pythonu jako list obsahující dictionaries.

---

## Hlavní výsledky

Analýza ukázala:

- Počet zaměstnanců: **8**
- Průměrná mzda: **56 875 Kč**
- Nejvyšší mzda: **Eva — 72 000 Kč**
- Nejnižší mzda: **Anna — 47 000 Kč**
- Počet zaměstnanců s nadprůměrnou mzdou: **4**
- Počet zaměstnanců v Sales: **3**
- Podíl zaměstnanců v Sales: **37,5 %**
- Průměrná mzda v Sales: **50 666,67 Kč**
- Průměrná mzda v IT: **68 500 Kč**
- IT má vyšší průměrnou mzdu než Sales.
- Rozdíl mezi průměrnou mzdou v IT a Sales: **17 833,33 Kč**
- Oddělení s nejvyšší průměrnou mzdou: **IT**

---

## Použité Python koncepty

V projektu jsou použity základní principy Pythonu:

- proměnné
- listy
- dictionaries
- `for` cykly
- podmínky `if` / `else`
- `append()`
- `len()`
- `sum()`
- `min()`
- `max()`
- `round()`
- filtrování dat pomocí podmínek

---

## Ukázka výstupu

```text
--- Business Summary ---

Number of employees: 8
Average salary: 56875.0 Kc
Highest salary: Eva 72000 Kc
Employees above average salary:
Jana 65000 Kc
Eva 72000 Kc
Lucie 58000 Kc
David 61000 Kc
Number of employees above average: 4
Lowest salary: Anna 47000 Kc
Number of Sales employees: 3
Average Sales salary: 50666.67 Kc
Average IT salary: 68500.0 Kc
IT has higher average salary
Percentage of Sales employees: 37.5 %
Salary IT vs Sales difference: 17833.33 Kc
Highest average salary department: IT 68500.0 Kc
```

---

## Zdrojový kód

Celá analýza je vytvořena v Pythonu bez použití externích analytických knihoven. Výpočty jsou provedeny pomocí základních Python konstrukcí, jako jsou listy, dictionaries, cykly, podmínky a vestavěné funkce.

➡️ [Zobrazit Python kód](./employee_salary_analysis.py)

---

## Co jsem si na projektu procvičil

Na této case study jsem si procvičil přechod od jednotlivých základů Pythonu k jednoduché analytické úloze nad jedním datasetem.

Projekt kombinuje několik kroků:

**data → filtrování → výpočty → porovnávání → businessové shrnutí**

Důležitou součástí bylo také propojení jednotlivých údajů. Například při hledání nejvyšší mzdy nestačí zjistit pouze maximální hodnotu, ale je potřeba ji následně spojit s konkrétním zaměstnancem.

Stejný princip se uplatnil při porovnávání jednotlivých oddělení.
