import sqlite3
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# -----------------------------
# Nastavení
# -----------------------------

random.seed(42)
np.random.seed(42)

DB_NAME = "case_study_06.db"

N_CUSTOMERS = 350
N_CONTRACTS = 750


# -----------------------------
# Připojení k databázi
# -----------------------------

connection = sqlite3.connect(DB_NAME)

print("Database created:", DB_NAME)


# -----------------------------
# Products
# -----------------------------

products = pd.DataFrame({
    "product_id": range(1, 11),
    "product_name": [
        "Current Account",
        "Savings Account",
        "Credit Card",
        "Consumer Loan",
        "Mortgage",
        "Investment Fund",
        "Pension Product",
        "Life Insurance",
        "Travel Insurance",
        "Business Account"
    ],
    "product_category": [
        "Accounts",
        "Accounts",
        "Cards",
        "Loans",
        "Loans",
        "Investments",
        "Investments",
        "Insurance",
        "Insurance",
        "Accounts"
    ],
    "target_segment": [
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Retail",
        "Business"
    ]
})

products.to_sql(
    "products",
    connection,
    if_exists="replace",
    index=False
)

print("Products created:", len(products))


# -----------------------------
# Customers
# -----------------------------

first_names = [
    "Jan", "Petr", "Martin", "Tomáš", "David",
    "Eva", "Jana", "Lucie", "Petra", "Martina"
]

last_names = [
    "Novák", "Svoboda", "Dvořák", "Černý", "Procházka",
    "Kučera", "Veselý", "Horák", "Němec", "Pokorný"
]

regions = [
    "Praha",
    "Střední Čechy",
    "Jižní Čechy",
    "Plzeň",
    "Ústí nad Labem",
    "Liberec",
    "Hradec Králové",
    "Pardubice",
    "Vysočina",
    "Brno",
    "Olomouc",
    "Ostrava"
]

channels = [
    "Branch",
    "Online",
    "Partner",
    "Call Center"
]

customer_types = [
    "Retail",
    "Business"
]

customers = pd.DataFrame({
    "customer_id": range(1001, 1001 + N_CUSTOMERS),

    "customer_name": [
        f"{random.choice(first_names)} {random.choice(last_names)}"
        for _ in range(N_CUSTOMERS)
    ],

    "customer_type": random.choices(
        customer_types,
        weights=[0.85, 0.15],
        k=N_CUSTOMERS
    ),

    "region": random.choices(
        regions,
        weights=[
            0.18, 0.10, 0.06, 0.06,
            0.06, 0.05, 0.06, 0.05,
            0.05, 0.14, 0.07, 0.12
        ],
        k=N_CUSTOMERS
    ),

    "acquisition_channel": random.choices(
        channels,
        weights=[0.40, 0.30, 0.15, 0.15],
        k=N_CUSTOMERS
    )
})


# -----------------------------
# Záměrné problémy v customers
# -----------------------------

customers.loc[
    random.sample(range(N_CUSTOMERS), 5),
    "region"
] = None

customers.loc[
    random.sample(range(N_CUSTOMERS), 4),
    "acquisition_channel"
] = "online"

customers.loc[
    random.sample(range(N_CUSTOMERS), 3),
    "acquisition_channel"
] = " Branch "

customers.loc[
    random.sample(range(N_CUSTOMERS), 3),
    "customer_name"
] = (
    customers["customer_name"]
    + " "
)


customers.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)

print("Customers created:", len(customers))


# -----------------------------
# Contracts
# -----------------------------

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

date_range_days = (end_date - start_date).days

contract_statuses = [
    "Active",
    "Cancelled",
    "Pending"
]

sales_channels = [
    "Branch",
    "Online",
    "Partner",
    "Call Center"
]

contracts = pd.DataFrame({
    "contract_id": range(5001, 5001 + N_CONTRACTS),

    "customer_id": random.choices(
        customers["customer_id"].tolist(),
        k=N_CONTRACTS
    ),

    "product_id": random.choices(
        products["product_id"].tolist(),
        weights=[
            0.16, 0.14, 0.12, 0.10, 0.06,
            0.08, 0.08, 0.09, 0.08, 0.09
        ],
        k=N_CONTRACTS
    ),

    "contract_date": [
        start_date + timedelta(
            days=random.randint(0, date_range_days)
        )
        for _ in range(N_CONTRACTS)
    ],

    "contract_status": random.choices(
        contract_statuses,
        weights=[0.86, 0.09, 0.05],
        k=N_CONTRACTS
    ),

    "sales_channel": random.choices(
        sales_channels,
        weights=[0.38, 0.32, 0.15, 0.15],
        k=N_CONTRACTS
    )
})


# -----------------------------
# Realističtější hodnota smlouvy
# podle produktu
# -----------------------------

product_value_ranges = {
    1: (0, 5000),          # Current Account
    2: (1000, 20000),      # Savings Account
    3: (1000, 10000),      # Credit Card
    4: (20000, 500000),    # Consumer Loan
    5: (1000000, 8000000), # Mortgage
    6: (10000, 500000),    # Investment Fund
    7: (5000, 100000),     # Pension Product
    8: (2000, 80000),      # Life Insurance
    9: (500, 15000),       # Travel Insurance
    10: (0, 50000)         # Business Account
}


def generate_contract_value(product_id):

    if product_id not in product_value_ranges:
        return np.nan

    min_value, max_value = product_value_ranges[
        product_id
    ]

    return random.randint(
        min_value,
        max_value
    )


contracts["contract_value"] = (
    contracts["product_id"]
    .apply(generate_contract_value)
)


# -----------------------------
# Záměrné problémy v contracts
# -----------------------------

contracts.loc[
    random.sample(range(N_CONTRACTS), 6),
    "contract_value"
] = np.nan

contracts.loc[
    random.sample(range(N_CONTRACTS), 4),
    "contract_status"
] = "active"

contracts.loc[
    random.sample(range(N_CONTRACTS), 3),
    "sales_channel"
] = " Online "

contracts.loc[
    random.sample(range(N_CONTRACTS), 2),
    "product_id"
] = 999

contracts.loc[
    random.sample(range(N_CONTRACTS), 2),
    "contract_value"
] = -5000


# -----------------------------
# Záměrné duplicity
# -----------------------------

duplicate_rows = contracts.sample(
    n=5,
    random_state=42
)

contracts = pd.concat(
    [
        contracts,
        duplicate_rows
    ],
    ignore_index=True
)


contracts.to_sql(
    "contracts",
    connection,
    if_exists="replace",
    index=False
)

print("Contracts created:", len(contracts))


# -----------------------------
# Acquisition targets
# -----------------------------

months = pd.date_range(
    start="2025-01-01",
    end="2025-12-01",
    freq="MS"
)

product_categories = products[
    "product_category"
].unique()

target_rows = []

for month in months:
    for region in regions:
        for category in product_categories:

            target_contracts = random.randint(
                2,
                12
            )

            target_rows.append({
                "year_month": month.strftime("%Y-%m"),
                "region": region,
                "product_category": category,
                "target_contracts": target_contracts
            })

acquisition_targets = pd.DataFrame(
    target_rows
)

acquisition_targets.to_sql(
    "acquisition_targets",
    connection,
    if_exists="replace",
    index=False
)

print(
    "Acquisition targets created:",
    len(acquisition_targets)
)


# -----------------------------
# Zavření databáze
# -----------------------------

connection.close()

print("Database connection closed.")