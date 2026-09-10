import pandas as pd

orders = pd.read_json("ecommerce_orders_missing_values.json")

print(orders.head())

print(orders.isna().sum())

print(orders.notna())

print(orders.notna().sum())

orders_clean = orders.dropna(subset=["region"])

print(orders.shape)

print(orders_clean.shape)

orders_filled = orders.copy()

orders_filled["region"] = orders_filled["region"].fillna("Unknown")

orders_filled["customer_type"] = orders_filled["customer_type"].fillna("Unknown")

print(orders_filled.isna().sum())

orders_filled["unit_price"] = orders_filled["unit_price"].fillna(orders_filled["unit_price"].median())

print(orders_filled.isna().sum())

print(orders_filled["unit_price"])

orders_clean = orders.copy()

orders_clean["region"] = orders_clean["region"].fillna("Unknown")

orders_clean["customer_type"] = orders_clean["customer_type"].fillna("Unknown")

orders_clean["unit_price"] = orders_clean["unit_price"].fillna(orders_clean["unit_price"].median())

orders_clean = orders_clean.dropna(subset=["product"])

print(orders_clean.isna().sum())