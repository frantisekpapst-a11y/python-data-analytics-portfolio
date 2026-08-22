# Case Study 03 — B2B/B2C Order Data Quality & Profit Analysis

## Přehled

Tato case study se zaměřuje na kontrolu kvality dat, čištění dat, přípravu analytického datasetu a základní business analýzu B2B a B2C objednávek pomocí Pythonu a knihovny `pandas`.

Cílem bylo převést původní dataset na vyčištěnou analytickou verzi a následně vypočítat základní prodejní a ziskové ukazatele (KPI).

---

## Dataset

Zdrojový dataset obsahuje 650 objednávek a zahrnuje informace o:

- datu objednávky,
- ID zákazníka,
- typu zákazníka,
- regionu,
- prodejním kanálu,
- produktu a kategorii,
- množství,
- jednotkové ceně,
- jednotkových nákladech,
- slevě,
- nákladech na dopravu,
- platební metodě,
- stavu objednávky.

Dataset obsahuje také záměrně vložené chybějící hodnoty, které byly využity pro kontrolu kvality dat a jejich čištění.

---

## Kontrola kvality dat

Na začátku analýzy byla provedena:

- kontrola struktury datasetu,
- kontrola názvů sloupců,
- kontrola datových typů,
- kontrola počtu neprázdných hodnot,
- identifikace chybějících hodnot,
- převod `order_date` na datový typ `datetime`,
- posouzení způsobu zpracování chybějících hodnot.

Chybějící hodnoty nebyly řešeny jedním univerzálním způsobem, ale podle významu jednotlivých sloupců.

Použitý přístup:

- chybějící hodnoty v `customer_type`, `region` a `payment_method` byly nahrazeny hodnotou `Unknown`,
- řádky s chybějícím `product` byly odstraněny,
- chybějící `unit_price` a `unit_cost` byly doplněny mediánem,
- chybějící hodnoty v `quantity`, `discount_pct` a `shipping_cost` byly ponechány jako `NaN`, protože jejich nahrazení by mohlo vytvářet nepodložené předpoklady.

---

## Příprava dat

Po vyčištění byly vytvořeny nové analytické sloupce:

```text
gross_sales
discount_amount
net_sales
total_cost
profit
```

Použité výpočty:

```text
gross_sales
= quantity × unit_price

discount_amount
= gross_sales × discount_pct

net_sales
= gross_sales - discount_amount

total_cost
= quantity × unit_cost

profit
= net_sales - total_cost - shipping_cost
```

---

## Business analýza

Analýza zahrnuje:

- celkové hrubé tržby,
- celkové čisté tržby,
- celkový zisk,
- průměrnou hodnotu objednávky po slevě,
- nejvyšší hodnotu objednávky po slevě,
- nejvyšší ztrátu na jedné objednávce,
- počet ztrátových objednávek,
- porovnání čistých tržeb B2B a B2C,
- porovnání zisku B2B a B2C.

---

## Klíčové výsledky

```text
Celkové hrubé tržby:             23 008 983,00 Kč
Celkové čisté tržby:             21 321 384,65 Kč
Celkový zisk:                     5 111 052,60 Kč

Průměrná hodnota objednávky:         34 168,89 Kč
Nejvyšší hodnota objednávky:        198 509,15 Kč
Nejvyšší ztráta na objednávce:      -86 603,00 Kč

Počet ztrátových objednávek:                 14

Čisté tržby B2B:                  10 088 654,65 Kč
Čisté tržby B2C:                  10 641 132,35 Kč

Zisk B2B:                          2 567 467,65 Kč
Zisk B2C:                          2 403 436,30 Kč
```

---

## Business závěry

- Celkové čisté tržby dosáhly přibližně **21,3 mil. Kč**.
- Celkový zisk dosáhl přibližně **5,1 mil. Kč**.
- Čisté tržby B2B a B2C segmentu byly poměrně vyrovnané.
- B2C segment dosáhl mírně vyšších čistých tržeb než B2B.
- B2B segment dosáhl mírně vyššího celkového zisku než B2C.
- Dataset obsahoval **14 ztrátových objednávek**.
- Nejvyšší ztráta na jedné objednávce činila přibližně **86,6 tis. Kč**.
- Při čištění dat bylo nutné volit rozdílný přístup podle významu jednotlivých sloupců a nevytvářet nepodložené náhradní hodnoty.

---

## Použité nástroje a techniky

### Python

- proměnné,
- základní výpočty,
- filtrování,
- podmínky,
- práce s výstupem.

### pandas

- `read_csv()`
- `head()`
- `info()`
- `shape`
- `dtypes`
- `to_datetime()`
- `isna()`
- `fillna()`
- `dropna()`
- `copy()`
- `median()`
- `sum()`
- `mean()`
- `max()`
- `min()`
- boolean filtrování
- `to_csv()`

---

## Soubory projektu

```text
case_study_03.py
→ Python zdrojový kód analýzy

case_study_03_b2b_b2c_orders.csv
→ původní zdrojový dataset

case_study_03_clean_orders.csv
→ vyčištěný a analyticky rozšířený dataset

business_summary.png
→ screenshot výsledného business summary

code.png
→ screenshot Python kódu
```

---

## Analytický postup

```text
Původní dataset
→ kontrola struktury
→ kontrola datových typů
→ kontrola chybějících hodnot
→ vytvoření pracovní kopie
→ čištění dat
→ vytvoření analytických sloupců
→ výpočet KPI
→ porovnání B2B a B2C
→ business summary
→ export vyčištěného datasetu
```

---

## Rozsah projektu

Case study záměrně používá pouze techniky, které byly v dané fázi studia již probrány.

Pokročilejší postupy jako:

- `groupby()`,
- `agg()`,
- `merge()`,
- analýza duplicit,
- pokročilá práce s datumy,
- vizualizace,

nejsou v tomto projektu použity a budou zařazeny v dalších lekcích a case studies.