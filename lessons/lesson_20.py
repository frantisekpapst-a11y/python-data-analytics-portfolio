import pandas as pd

# --------------------------------------------------
# 1. Excel / Power Query vs. Pandas
# --------------------------------------------------

df = pd.DataFrame({

    "region": ["Praha", "Brno", "Praha", "Ostrava", "Brno"],

    "product": ["Laptop", "Desk", "Monitor", "Chair", "Laptop"],

    "quantity": [2, 3, 4, 2, 1],

    "unit_price": [25000, 8000, 6000, 5000, 25000]

})


# nový sloupec total

df["total"] = (
    df["quantity"]
    * df["unit_price"]
)

# tržby podle produktu

revenue_by_product = (
    df.groupby(
        "product",
        as_index=False
    )["total"]
    .sum()
    .sort_values(
        by="total",
        ascending=False
    )
)

print(revenue_by_product)


# --------------------------------------------------
# 2. Merge
# Power Query Merge / SQL JOIN
# --------------------------------------------------

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer_id": ["C001", "C002", "C001", "C003"],
    "revenue": [12000, 8000, 15000, 7000]
})

customers = pd.DataFrame({
    "customer_id": ["C001", "C002", "C003"],
    "customer_name": ["Jan Novák", "Eva Malá", "Petr Dvořák"],
    "region": ["Praha", "Brno", "Ostrava"]
})

result_merge = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print(result_merge)

# --------------------------------------------------
# 3. Append / concat
# Power Query Append / SQL UNION ALL
# --------------------------------------------------

orders_1 = pd.DataFrame({
    "order_id": [1, 2],
    "customer_id": ["C001", "C002"],
    "revenue": [12000, 8000]
})

orders_2 = pd.DataFrame({
    "order_id": [3, 4],
    "customer_id": ["C001", "C003"],
    "revenue": [15000, 7000]
})

result_concat = pd.concat([
        orders_1,
        orders_2],
    ignore_index=True
)

print(result_concat)

# --------------------------------------------------
# 4. Wide / Long Format
# Power Query Append / SQL UNION ALL
# --------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "month": ["2026-01", "2026-02", "2026-03"],
    "B2B": [120, 135, 150],
    "B2C": [90, 95, 110],
    "Partner": [40, 45, 50]
})

df_long = df.melt(
    id_vars="month",
    var_name="segment",
    value_name="revenue"
)

print(df_long)