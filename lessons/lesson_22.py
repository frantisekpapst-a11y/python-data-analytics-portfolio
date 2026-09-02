import sqlite3
import pandas as pd

connection = sqlite3.connect("sales.db")

query = """
SELECT
    order_id,
    product,
    quantity,
    unit_price
FROM orders
WHERE quantity >= 2
"""

df = pd.read_sql(query, connection)

print(df)

query = """
SELECT
    o.order_id,
    o.product,
    o.quantity,
    o.unit_price,
    c.customer_name,
    c.region
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
"""

df = pd.read_sql(query, connection)

print(df)

df["total"] = df["quantity"] * df["unit_price"]

print(df["total"])

region_summary = (
    df.groupby("region")["total"]
    .sum()
    .reset_index()
    .sort_values("total", ascending=False)
)

print(region_summary)

import matplotlib.pyplot as plt

plt.pie(
    region_summary["total"],
    labels=region_summary["region"],
    autopct=lambda pct: (
        f"{pct:.1f}%\n"
        f"{pct / 100 * region_summary['total'].sum() / 1000:.1f}k"
    )
)

plt.title("Revenue by Region")

plt.show()

region = "Praha"

query = """
SELECT
    o.order_id,
    o.product,
    o.quantity,
    o.unit_price,
    c.customer_name,
    c.region
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.region = ?
"""

df_region = pd.read_sql(
    query,
    connection,
    params=(region,)
)

print(df_region)

connection.close()