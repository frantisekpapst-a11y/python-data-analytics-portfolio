import sqlite3
import numpy as np
import pandas as pd


connection = sqlite3.connect("case_study_06.db")


# -----------------------------
# SQL query
# -----------------------------

query = """
SELECT
    c.contract_id,
    c.product_id AS contract_product_id,
    c.contract_date,
    c.contract_status,
    c.contract_value,
    c.sales_channel,

    cu.customer_id,
    cu.customer_name,
    cu.customer_type,
    cu.region,
    cu.acquisition_channel,

    p.product_id AS product_id,
    p.product_name,
    p.product_category,
    p.target_segment

FROM contracts c

LEFT JOIN customers cu
    ON c.customer_id = cu.customer_id

LEFT JOIN products p
    ON c.product_id = p.product_id
"""


# ---------------------------------
# Načtení a uložení zdrojových dat
# ---------------------------------

contracts_raw = pd.read_sql(
    query,
    connection
)

contracts_raw.to_json(
    "case_study_06_contracts_raw.json",
    orient="records",
    indent=4,
    date_format="iso"
)
contracts_clean = contracts_raw.copy()


# -----------------------------
# Základní kontrola
# -----------------------------

print(contracts_clean.head())
print(contracts_clean.shape)
print(contracts_clean.index)

contracts_clean.info()

print(contracts_clean.columns)


# -----------------------------
# Datové typy
# -----------------------------

contracts_clean["contract_date"] = pd.to_datetime(
    contracts_clean["contract_date"]
)


# -----------------------------
# Kontrola neplatných produktových vazeb
# -----------------------------

print(
    contracts_clean.loc[
        contracts_clean["product_id"].isna(),
        [
            "contract_id",
            "contract_product_id",
            "customer_id",
            "product_id",
            "product_name",
            "product_category",
            "target_segment"
        ]
    ]
)


# -----------------------------
# Missing values
# -----------------------------

print(contracts_clean.isna().sum())


# -----------------------------
# Duplicity
# -----------------------------

print(contracts_clean.duplicated().sum())


# -----------------------------
# Kontrola kategorií před cleaning
# -----------------------------

print(contracts_clean["contract_status"].value_counts())
print(contracts_clean["sales_channel"].value_counts())
print(contracts_clean["acquisition_channel"].value_counts())


# -----------------------------
# Text cleaning
# -----------------------------

contracts_clean["contract_status"] = (
    contracts_clean["contract_status"]
    .str.strip()
    .str.title()
)

contracts_clean["sales_channel"] = (
    contracts_clean["sales_channel"]
    .str.strip()
    .str.title()
)

contracts_clean["acquisition_channel"] = (
    contracts_clean["acquisition_channel"]
    .str.strip()
    .str.title()
)


# -----------------------------
# Kontrola kategorií po cleaning
# -----------------------------

print(contracts_clean["contract_status"].value_counts())
print(contracts_clean["sales_channel"].value_counts())
print(contracts_clean["acquisition_channel"].value_counts())


# -----------------------------
# Zobrazení duplicit
# -----------------------------

print(
    contracts_clean[
        contracts_clean.duplicated(
            keep=False
        )
    ]
)


# -----------------------------
# Odstranění duplicit
# -----------------------------

contracts_clean = (
    contracts_clean
    .drop_duplicates()
    .reset_index(drop=True)
)

print(contracts_clean.duplicated().sum())
print(contracts_clean.shape)


# -----------------------------
# Contract value
# -----------------------------

print(
    contracts_clean.loc[
        contracts_clean["contract_value"].isna()
    ]
)

print(
    contracts_clean["contract_value"].describe()
)


# -----------------------------
# Neplatné contract_value
# převést na NaN
# -----------------------------

contracts_clean.loc[
    contracts_clean["contract_value"] <= 0,
    "contract_value"
] = np.nan


# -----------------------------
# Missing contract_value
# doplnit mediánem podle produktu
# -----------------------------

contracts_clean["contract_value"] = (
    contracts_clean["contract_value"]
    .fillna(
        contracts_clean.groupby(
            "product_name"
        )["contract_value"].transform(
            "median"
        )
    )
)


# -----------------------------
# Kontrola contract_value
# -----------------------------

print(
    contracts_clean["contract_value"].isna().sum()
)

print(
    contracts_clean[
        contracts_clean["contract_value"] <= 0
    ]
)


# -----------------------------
# Region
# -----------------------------

print(
    contracts_clean.loc[
        contracts_clean["region"].isna()
    ]
)

contracts_clean["region"] = (
    contracts_clean["region"]
    .fillna("Unknown")
)

print(
    contracts_clean["region"].isna().sum()
)


# -----------------------------
# Neplatné produktové vazby
# -----------------------------

print(
    contracts_clean.loc[
        contracts_clean["product_id"].isna()
    ]
)

contracts_clean["product_name"] = (
    contracts_clean["product_name"]
    .fillna("Unknown")
)

contracts_clean["product_category"] = (
    contracts_clean["product_category"]
    .fillna("Unknown")
)

contracts_clean["target_segment"] = (
    contracts_clean["target_segment"]
    .fillna("Unknown")
)


# -----------------------------
# Product ID
# -----------------------------

contracts_clean["product_id"] = (
    contracts_clean["product_id"]
    .astype("Int64")
)


# -----------------------------
# Kontrola kategorií
# -----------------------------

print(contracts_clean["contract_status"].value_counts())
print(contracts_clean["sales_channel"].value_counts())
print(contracts_clean["acquisition_channel"].value_counts())
print(contracts_clean["customer_type"].value_counts())
print(contracts_clean["region"].value_counts())
print(contracts_clean["product_category"].value_counts())
print(contracts_clean["target_segment"].value_counts())


# -----------------------------
# Kontrola klíčů
# -----------------------------

print(
    contracts_clean["contract_id"]
    .duplicated()
    .sum()
)

print(
    contracts_clean["customer_id"]
    .isna()
    .sum()
)

print(
    contracts_clean["contract_product_id"]
    .isna()
    .sum()
)


# -----------------------------
# Validace contract date
# -----------------------------

print(
    contracts_clean["contract_date"].min()
)

print(
    contracts_clean["contract_date"].max()
)

print(
    contracts_clean["contract_date"]
    .isna()
    .sum()
)

invalid_dates = contracts_clean[
    (contracts_clean["contract_date"] < "2025-01-01")
    | (contracts_clean["contract_date"] > "2025-12-31")
]

print(invalid_dates)


# -----------------------------
# Validace po čištění
# -----------------------------

print(contracts_clean.shape)
print(contracts_clean.isna().sum())
print(contracts_clean.duplicated().sum())
print(contracts_clean.dtypes)

print(
    contracts_clean["contract_value"].min()
)

print(
    contracts_clean["contract_value"].max()
)

print(
    contracts_clean[
        contracts_clean["contract_value"] <= 0
    ]
)


# -----------------------------
# Outliers podle produktu
# -----------------------------

q1 = contracts_clean.groupby(
    "product_name"
)["contract_value"].transform(
    lambda x: x.quantile(0.25)
)

q3 = contracts_clean.groupby(
    "product_name"
)["contract_value"].transform(
    lambda x: x.quantile(0.75)
)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = contracts_clean[
    (contracts_clean["contract_value"] < lower_bound)
    | (contracts_clean["contract_value"] > upper_bound)
]

print(
    "Počet outlierů:",
    len(outliers)
)

print(
    outliers[
        [
            "contract_id",
            "product_name",
            "contract_value"
        ]
    ].to_string(
        index=False
    )
)


# -----------------------------
# Business transformace
# -----------------------------

contracts_clean["year_month"] = (
    contracts_clean["contract_date"]
    .dt.to_period("M")
    .dt.to_timestamp()
)

contracts_clean["is_active"] = (
    contracts_clean["contract_status"] == "Active"
)

contracts_clean["is_cancelled"] = (
    contracts_clean["contract_status"] == "Cancelled"
)

contracts_clean["is_pending"] = (
    contracts_clean["contract_status"] == "Pending"
)

print(contracts_clean.head())


# -----------------------------
# Export do JSON
# -----------------------------

contracts_clean.to_json(
    "case_study_06_contracts_clean.json",
    orient="records",
    indent=4,
    date_format="iso"
)


# -----------------------------
# SQL query - cíle
# -----------------------------

targets_query = """
SELECT
    year_month,
    region,
    product_category,
    target_contracts
FROM acquisition_targets
"""


# ----------------------------------------
# Načtení a uložení zdrojových dat - cíle
# ----------------------------------------

targets_raw = pd.read_sql(
    targets_query,
    connection
)

targets_raw.to_json(
    "case_study_06_targets_raw.json",
    orient="records",
    indent=4
)
targets_clean = targets_raw.copy()


# -----------------------------
# Základní kontrola - cíle
# -----------------------------

print(targets_clean.head())
print(targets_clean.shape)
targets_clean.info()

print(targets_clean.isna().sum())
print(targets_clean.duplicated().sum())

print(targets_clean["region"].unique())
print(targets_clean["product_category"].unique())

print(
    targets_clean["target_contracts"].describe()
)


# -----------------------------
# Export do JSON
# -----------------------------

targets_clean.to_json(
    "case_study_06_targets_clean.json",
    orient="records",
    indent=4
)


# -----------------------------
# Uzavření databáze
# -----------------------------

connection.close()