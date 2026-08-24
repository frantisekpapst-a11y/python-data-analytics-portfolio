# Python Libraries for Data Analytics

Praktický přehled nejčastějších Python knihoven používaných v datové analytice.

---

## pandas

```python
import pandas as pd
```

Použití:

* načítání dat
* DataFrame / Series
* cleaning
* filtrování
* transformace
* agregace
* spojování tabulek
* práce s datumy
* export dat

Typické funkce:

```python
pd.read_csv()
pd.read_json()
pd.read_excel()
pd.read_sql()

df.head()
df.info()
df.groupby()
df.merge()
df.sort_values()
```

**Role v DA:** hlavní knihovna pro práci s tabulkovými daty.

---

## NumPy

```python
import numpy as np
```

Použití:

* numerické výpočty
* pole a matice
* matematické operace
* práce s `NaN`
* základ pro řadu dalších knihoven

Příklady:

```python
np.mean()
np.median()
np.std()
```

**Role v DA:** numerický základ Python datového ekosystému.

---

## Matplotlib

```python
import matplotlib.pyplot as plt
```

Použití:

* grafy
* vizualizace výsledků
* úprava os, popisků a layoutu

Typické grafy:

```text
line chart
bar chart
histogram
scatter plot
```

**Role v DA:** základní knihovna pro statickou vizualizaci dat.

---

## Plotly

```python
import plotly.express as px
```

Použití:

* interaktivní grafy
* explorace dat
* dashboardové vizualizace

**Role v DA:** interaktivní alternativa k Matplotlib.

---

## requests

```python
import requests
```

Použití:

* komunikace s API
* HTTP GET / POST requesty
* získávání externích dat

Příklad:

```python
response = requests.get(url)

data = response.json()
```

**Role v DA:** získávání dat z webových API.

---

# Databáze

## sqlite3

```python
import sqlite3
```

Použití:

* SQLite databáze
* lokální `.db` soubory
* SQL dotazy z Pythonu

Příklad:

```python
connection = sqlite3.connect(
    "database.db"
)
```

V kombinaci s Pandas:

```python
df = pd.read_sql(
    query,
    connection
)
```

**Role v DA:** jednoduchá lokální relační databáze.

---

## pyodbc

```python
import pyodbc
```

Použití:

* připojení přes ODBC
* často MS SQL Server
* lze použít i pro další databáze s ODBC driverem

Typický princip:

```python
connection = pyodbc.connect(
    connection_string
)
```

Potom:

```python
df = pd.read_sql(
    query,
    connection
)
```

**Role v DA:** časté propojení Pythonu s Microsoft SQL Serverem.

---

## oracledb

```python
import oracledb
```

Použití:

* Oracle Database
* SQL dotazy
* připojení k firemním Oracle databázím

Příklad:

```python
connection = oracledb.connect(
    user="username",
    password="password",
    dsn="server/service_name"
)
```

Potom:

```python
df = pd.read_sql(
    query,
    connection
)
```

**Role v DA:** připojení Pythonu k Oracle databázi.

---

## SQLAlchemy

```python
from sqlalchemy import create_engine
```

Použití:

* obecnější databázová vrstva
* práce s více databázovými systémy
* vytváření databázových connection / engine objektů
* dobrá spolupráce s Pandas

Lze použít například s:

```text
SQLite
MS SQL Server
Oracle
PostgreSQL
MySQL
```

Typický princip:

```python
engine = create_engine(
    connection_string
)

df = pd.read_sql(
    query,
    engine
)
```

**Role v DA:** univerzálnější databázová vrstva mezi Pythonem a různými databázemi.

---

# Excel

## openpyxl

Použití:

* čtení a zápis `.xlsx`
* práce s workbooky, listy a buňkami
* pokročilejší automatizace Excelu

Pandas ji může využívat například při:

```python
pd.read_excel()
df.to_excel()
```

**Role v DA:** podpora práce s Excel soubory.

---

# Statistika

## SciPy

```python
from scipy import stats
```

Použití:

* statistické testy
* pravděpodobnost
* distribuce
* korelace
* pokročilejší statistická analýza

Příklad:

```python
stats.ttest_ind()
```

**Role v DA:** statistika nad rámec základního Pandas a NumPy.

---

# Machine Learning

## scikit-learn

```python
from sklearn import ...
```

Použití:

* preprocessing
* regrese
* klasifikace
* clustering
* model evaluation
* machine learning

**Role v DA:** pokročilejší analytika a základní machine learning.

Pro běžného Data Analysta není nutné ji používat v každém projektu.

---

# Databáze — rychlé srovnání

```text
SQLite
→ sqlite3

MS SQL Server
→ pyodbc
→ případně SQLAlchemy

Oracle
→ oracledb
→ případně SQLAlchemy

Více databázových systémů
→ SQLAlchemy
```

Typický princip je stále stejný:

```text
databáze
→ connection / engine
→ SQL query
→ pd.read_sql()
→ DataFrame
```

---

# Doporučené priority pro Data Analyst

```text
1. pandas
2. NumPy
3. SQL + databázové připojení
4. Matplotlib
5. requests
6. openpyxl
7. SciPy
8. Plotly
9. scikit-learn
```

U databází není nutné znát všechny knihovny.

Stačí rozumět principu a podle prostředí použít například:

```text
sqlite3
pyodbc
oracledb
SQLAlchemy
```

---

# Typický analytický workflow

```text
Data Source
↓
requests / databázový driver / pandas
↓
pandas
↓
NumPy / SciPy
↓
Matplotlib / Plotly
↓
výstup / reporting
```

---

# Rychlý přehled

| Knihovna     | Hlavní použití                    |
| ------------ | --------------------------------- |
| pandas       | tabulková data, cleaning, analýza |
| NumPy        | numerické výpočty                 |
| Matplotlib   | statická vizualizace              |
| Plotly       | interaktivní vizualizace          |
| requests     | API                               |
| sqlite3      | SQLite                            |
| pyodbc       | MS SQL Server / ODBC              |
| oracledb     | Oracle                            |
| SQLAlchemy   | obecná databázová vrstva          |
| openpyxl     | Excel                             |
| SciPy        | statistika                        |
| scikit-learn | machine learning                  |
