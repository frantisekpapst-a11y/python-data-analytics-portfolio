# 🐍 Python Data Analytics Portfolio

Portfolio zaměřené na **Python, pandas, datovou přípravu, analytické workflow, vizualizaci, práci s API a integraci s dalšími datovými nástroji**.

Repozitář obsahuje praktické case studies, lekce, mini testy a referenční materiály pokrývající práci s Pythonem od základních konstrukcí až po komplexnější analytické scénáře nad CSV, JSON, Excel, SQL databázemi a veřejnými API.

Hlavní oblasti:

- Python fundamentals,
- práce se soubory a datovými formáty,
- pandas,
- data cleaning a validation,
- groupby, aggregation a merge,
- datetime a textové transformace,
- exploratory data analysis,
- statistické základy,
- NumPy,
- Matplotlib a Plotly,
- SQL + Python,
- Power BI + Python,
- API ingestion,
- příprava BI-ready datasetů,
- business-oriented analytické case studies.

---

# 📂 Struktura repozitáře

```text
python-data-analytics-portfolio/
│
├── case-studies/
│   ├── case-study-01/
│   ├── case-study-02/
│   ├── case-study-03/
│   ├── case-study-04/
│   ├── case-study-05/
│   └── case-study-06/
│
├── cheatsheets/
│   ├── python_data_analytics_cheatsheet.md
│   ├── python_data_analytics_libraries.md
│   └── python_fundamentals_cheatsheet.md
│
├── lessons/
│
├── mini-tests/
│   └── mini_tests.md
│
└── README.md
```

---

# 🎯 Zaměření portfolia

Repozitář demonstruje praktické využití Pythonu v analytickém workflow:

```text
Business Question
→ Data Source
→ Ingestion
→ Validation
→ Cleaning
→ Transformation
→ Analysis
→ Visualization
→ Interpretation
→ Export / Reporting
```

Python zde není používán izolovaně, ale jako nástroj pro:

- načítání dat,
- přípravu analytických datasetů,
- kontrolu kvality,
- transformace,
- výpočty a agregace,
- spojování více zdrojů,
- statistickou analýzu,
- vizualizaci,
- práci s databázemi a API,
- přípravu dat pro další reportingové nástroje.

---

# 📁 Case Studies

Case studies jsou prezentovány **od nejpokročilejšího a nejreprezentativnějšího projektu po jednodušší analytické úlohy**.

Důvodem je portfolio-oriented prezentace, kdy je na prvním místě projekt, který nejlépe reprezentuje aktuální úroveň práce s Pythonem, pandas, SQL integrací, data quality, statistikou a business reportingem. Původní číslování zůstává zachováno a zároveň dokumentuje vývoj jednotlivých témat.

---

## Case Study 06 — SQL, Python & Power BI Acquisition Analytics

Nejkomplexnější projekt v repozitáři propojující databázi, SQL, Python, data quality a Power BI reporting. fileciteturn74file0L1-L1

Hlavní workflow:

```text
SQLite
→ SQL SELECT / JOIN
→ pd.read_sql()
→ cleaning
→ validation
→ outlier analysis
→ business transformations
→ BI-ready datasets
→ Power BI
```

Použité koncepty:

- vytvoření SQLite databáze,
- SQL ingestion,
- `pd.read_sql()`,
- validační kontroly,
- missing values,
- duplicity,
- referenční integrita,
- outlier analysis,
- `groupby()` + `transform()`,
- datetime transformace,
- business flags,
- příprava čistých datasetů,
- návaznost na Power Query, DAX a Power BI. fileciteturn74file2L1-L1

Projekt ukazuje rozdělení rolí mezi jednotlivé technologie:

```text
SQL
→ relační logika a extraction

Python
→ cleaning, validation a preprocessing

Power BI
→ datový model, DAX a reporting
```

➡️ [Otevřít Case Study 06](case-studies/case-study-06/)

---

## Case Study 05 — Customer Support Ticket Analysis

Case study zaměřená na data quality, exploratory analysis a statistické vyhodnocení dat zákaznické podpory.

Použité koncepty:

- JSON ingestion,
- cleaning a standardizace,
- missing values,
- duplicity,
- EDA,
- IQR outlier detection,
- korelace,
- ANOVA,
- `groupby()` / `agg()`,
- Matplotlib,
- business interpretace.

Analýza porovnává zejména dobu řešení ticketů, spokojenost zákazníků, priority, komunikační kanály a oddělení.

Důležitým závěrem projektu je rozlišení mezi:

```text
statistical significance
≠
automatic business significance
```

➡️ [Otevřít Case Study 05](case-studies/case-study-05/)

---

## Case Study 04 — Multi-Table Sales & Customer Analysis

Projekt zaměřený na propojení více datových tabulek a vytvoření finálního analytického datasetu.

Použité koncepty:

- kontrola kvality více datasetů,
- text cleaning,
- missing values,
- duplicity,
- validace klíčů,
- `merge()`,
- `validate="many_to_one"`,
- left join logika,
- business calculations,
- `groupby()` a agregace.

Po propojení `orders`, `customers` a `products` byly vytvořeny metriky:

```text
revenue
cost
profit
```

Projekt zdůrazňuje, že:

```text
vysoké revenue
≠
vysoký profit

vysoký profit
≠
vysoká profit margin
```

➡️ [Otevřít Case Study 04](case-studies/case-study-04/)

---

## Case Study 03 — B2B/B2C Order Data Quality & Profit Analysis

Case study zaměřená na čištění objednávkových dat a základní profitabilitní analýzu v pandas.

Použité koncepty:

- `read_csv()`,
- `info()` a `shape`,
- datové typy,
- `to_datetime()`,
- missing values,
- `fillna()` a `dropna()`,
- pracovní kopie datasetu,
- business calculations,
- boolean filtering,
- KPI,
- export do CSV.

V projektu vznikají analytické metriky:

```text
gross_sales
discount_amount
net_sales
total_cost
profit
```

Součástí analýzy je porovnání B2B a B2C segmentu a identifikace ztrátových objednávek.

➡️ [Otevřít Case Study 03](case-studies/case-study-03/)

---

## Case Study 02 — E-commerce Sales Analysis

Projekt zaměřený na zpracování CSV dat pomocí základního Pythonu bez pandas.

Použité koncepty:

- `csv.DictReader()`,
- `csv.DictWriter()`,
- listy,
- dictionaries,
- `for` cykly,
- podmínky,
- vlastní funkce,
- převod datových typů,
- výpočty,
- filtrování,
- export do CSV.

Workflow:

```text
CSV
→ načtení
→ převod datových typů
→ výpočty
→ filtrování
→ business summary
→ export
```

Projekt ukazuje práci s externím datovým souborem ještě před použitím analytických knihoven.

➡️ [Otevřít Case Study 02](case-studies/case-study-02/)

---

## Case Study 01 — Employee Salary Analysis

První case study zaměřená na propojení základů Pythonu s jednoduchou business analýzou.

Použité koncepty:

- proměnné,
- listy,
- dictionaries,
- `for`,
- `if / else`,
- `append()`,
- `len()`,
- `sum()`,
- `min()` a `max()`,
- filtrování,
- základní agregace,
- business summary.

Analýza pracuje s údaji o zaměstnancích, odděleních a mzdách a převádí základní Python konstrukce do jednoduchého analytického scénáře.

➡️ [Otevřít Case Study 01](case-studies/case-study-01/)

---

# 🧩 Python Data Analytics Skills

Portfolio pokrývá praktickou práci s Pythonem od základních konstrukcí až po analytické workflow nad více datovými zdroji.

Hlavní oblasti:

- Python fundamentals,
- listy, dictionaries, podmínky, cykly a funkce,
- práce se soubory,
- CSV, JSON a Excel,
- pandas DataFrame / Series,
- filtrování a selection,
- missing values a duplicity,
- text cleaning,
- datové typy a datetime,
- `groupby()`, `agg()`, `size()` a `transform()`,
- `merge()` a validační logika,
- EDA a descriptive statistics,
- korelace, outliers a základní statistické testování,
- NumPy,
- Matplotlib,
- Plotly,
- SQL + pandas,
- Power BI + Python,
- API requests, params, headers a pagination,
- validation, export a BI-ready data preparation.

Důraz je kladen na:

```text
Data Source
→ Clean Data
→ Validated Data
→ Analysis
→ Business Interpretation
```

Detailní syntaxe, příklady a poznámky jsou součástí cheatsheetů, lessons a jednotlivých case studies.

---

# 🔄 Python & Other Analytics Tools

Python je v portfoliu používán také v kombinaci s dalšími analytickými technologiemi.

## SQL + Python

Typický přístup:

```text
Database
→ SQL SELECT / JOIN / filtering
→ pandas
→ cleaning / validation / analysis
```

Použité koncepty zahrnují:

- SQLite,
- `sqlite3`,
- `pd.read_sql()`,
- parameterized SQL,
- oddělení relační a analytické logiky.

---

## Power BI + Python

Python je používán zejména pro:

- cleaning,
- preprocessing,
- custom transformations,
- validaci,
- přípravu BI-ready datasetů.

Navazující role:

```text
Power Query
→ lehká datová příprava

Python
→ komplexnější cleaning a preprocessing

DAX
→ dynamické KPI

Power BI
→ reporting a interaktivita
```

---

## API + Python

Portfolio zahrnuje také praktickou práci s veřejnými API.

Použité oblasti:

- `requests.get()`,
- `params=`,
- `headers=`,
- status codes,
- `raise_for_status()`,
- `try / except`,
- `timeout`,
- pagination,
- multi-page loading,
- nested JSON,
- `pd.json_normalize()`,
- API → DataFrame,
- validation,
- datetime filtering,
- visualization,
- export.

Praktické API scénáře zahrnují JSONPlaceholder a Open-Meteo.

---

# 📚 Knowledge Base

## python_data_analytics_cheatsheet.md

Hlavní analytický cheatsheet pokrývající pandas, cleaning, transformace, agregace, merge, datetime, EDA, vizualizaci, SQL integraci, Power BI integraci a API workflow. fileciteturn74file8L1-L1

➡️ [Python Data Analytics Cheatsheet](cheatsheets/python_data_analytics_cheatsheet.md)

---

## python_fundamentals_cheatsheet.md

Reference k základním Python konstrukcím používaným v analytických projektech.

Obsahuje například:

- proměnné,
- datové typy,
- listy,
- dictionaries,
- podmínky,
- cykly,
- funkce,
- práci se soubory,
- základní práci s cestami a textovými daty. fileciteturn74file5L1-L1

➡️ [Python Fundamentals Cheatsheet](cheatsheets/python_fundamentals_cheatsheet.md)

---

## python_data_analytics_libraries.md

Přehled hlavních Python knihoven používaných nebo relevantních pro datovou analytiku.

➡️ [Python Data Analytics Libraries](cheatsheets/python_data_analytics_libraries.md)

---

## lessons

Praktické lekce a zdrojové soubory používané pro jednotlivá témata Python analytiky.

Obsahují například:

- fundamentals,
- data ingestion,
- pandas,
- cleaning,
- groupby,
- merge,
- datetime,
- EDA,
- NumPy,
- Matplotlib,
- Plotly,
- Excel / Power BI / SQL integration,
- API.

➡️ [Python Lessons](lessons/)

---

## mini-tests

Sada krátkých testů zaměřených na kontrolu syntaxe, logiky a praktického použití Pythonu a pandas.

➡️ [Python Mini Tests](mini-tests/mini_tests.md)

---

# 🛠 Technologie a koncepty

```text
Python
pandas
NumPy
Matplotlib
Plotly
SciPy
requests
JSON
CSV
Excel
SQLite
SQL
Power Query
Power BI
DAX
API
Git
GitHub
VS Code
```

---

# 📈 Další rozvoj

Python portfolio je dále rozšiřováno především prostřednictvím komplexnějších praktických projektů a integrace s externími datovými zdroji.

Navazující oblasti zahrnují například:

- další API projekty,
- finanční a tržní data,
- větší relační datasety,
- pokročilejší statistickou analýzu,
- SQL + Python analytické pipeline,
- přípravu dat pro Power BI,
- reusable Python functions,
- robustnější validation a error handling,
- end-to-end analytické case studies.

Automatizace, kompletní cross-tool analytické workflow a širší data tooling jsou vedeny jako samostatné oblasti mimo čistě Python portfolio.


Lekce
→ API
→ requests
→ parametry
→ JSON
→ reálná data
→ kontrola odpovědi
→ převod do DataFrame

Lekce
→ Automatizace
→ opakované načítání dat
→ automatické zpracování
→ exporty a reporty
→ analytický skript od začátku do konce

Lekce
→ Kompletní analytický workflow
→ ingestion
→ raw data
→ cleaning
→ validation
→ transformace
→ analýza
→ vizualizace
→ reporting

Lekce
→ Jupyter Notebook / VS Code workflow
→ buňky, spouštění po částech
→ Markdown buňky
→ tabulky a grafy přímo v notebooku
→ kdy použít .ipynb a kdy .py
→ práce s notebookem ve VS Code
→ Moderní datové platformy
→ Spark / PySpark
→ Databricks
→ Snowflake
→ BigQuery
→ Azure / Fabric
→ dbt
→ Airflow