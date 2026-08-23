import pandas as pd

orders = pd.read_csv("lesson_09_dirty_orders.csv")

print(orders.head(10))

orders.info()

print(orders.shape)

print(orders.isna().sum())

print(orders.duplicated().sum())

print(orders[orders.duplicated()])

print(orders["customer_type"].unique())
print(orders["region"].unique())
print(orders["product"].unique())
print(orders["status"].unique())

print(orders["customer_type"].value_counts(dropna=False))
print(orders["region"].value_counts(dropna=False))
print(orders["product"].value_counts(dropna=False))

orders_clean = orders.copy()

orders_clean["customer_type"] = orders_clean["customer_type"].str.strip()
orders_clean["region"] = orders_clean["region"].str.strip()
orders_clean["product"] = orders_clean["product"].str.strip()

orders_clean["customer_type"] = orders_clean["customer_type"].str.upper()

orders_clean["product"] = orders_clean["product"].str.title()

orders_clean["region"] = orders_clean["region"].replace("cz-west", "CZ-West")

print(orders_clean["customer_type"].value_counts(dropna=False))
print(orders_clean["region"].value_counts(dropna=False))
print(orders_clean["product"].value_counts(dropna=False))

orders_clean["customer_type"] = orders_clean["customer_type"].replace("Business", "B2B")

orders_clean["customer_type"] = orders_clean["customer_type"].replace("BUSINESS", "B2B")

orders_clean["customer_type"] = orders_clean["customer_type"].fillna("Unknown")
orders_clean["region"] = orders_clean["region"].fillna("Unknown")

print(orders_clean["customer_type"].value_counts(dropna=False))
print(orders_clean["region"].value_counts(dropna=False))

print(orders_clean[orders_clean.duplicated()])

orders_clean = orders_clean.drop_duplicates()

print(orders_clean.duplicated().sum())
print(orders_clean.shape)

print(orders_clean[orders_clean["quantity"] <= 0])
print(orders_clean[orders_clean["unit_price"] <= 0])
print(orders_clean[orders_clean["discount_pct"] < 0])
print(orders_clean[orders_clean["discount_pct"] > 1])

print(orders_clean["quantity"].min())
print(orders_clean["quantity"].max())

print(orders_clean["unit_price"].min())
print(orders_clean["unit_price"].max())

print(orders_clean["discount_pct"].min())
print(orders_clean["discount_pct"].max())

invalid_orders = orders_clean[(orders_clean["quantity"] <= 0) | (orders_clean["unit_price"] <= 0) | (orders_clean["discount_pct"] < 0) | (orders_clean["discount_pct"] > 1)]

print(invalid_orders)

print(len(invalid_orders))

orders_clean.loc[orders_clean["quantity"] <= 0, "quantity"] = pd.NA

orders_clean.loc[orders_clean["unit_price"] <= 0, "unit_price"] = pd.NA

orders_clean.loc[(orders_clean["discount_pct"] < 0) | (orders_clean["discount_pct"] > 1), "discount_pct"] = pd.NA

print(orders_clean[["quantity", "unit_price", "discount_pct"]].isna().sum())

print(orders_clean[["quantity", "unit_price", "discount_pct"]])

print(orders_clean)

print(orders_clean["quantity"].describe())

print(orders_clean.sort_values(by="quantity", ascending=False).head())

high_quantity_orders = orders_clean[orders_clean["quantity"] > 20]

print(high_quantity_orders)

print(orders_clean["quantity"].median())
print(orders_clean["quantity"].max())

orders_clean["order_date"] = pd.to_datetime(orders_clean["order_date"])

print("")
print("FINAL VALIDATION")
print("-" * 62)
print(orders_clean.shape)

print(orders_clean.isna().sum())

print(orders_clean.duplicated().sum())

print(orders_clean["customer_type"].value_counts(dropna=False))
print(orders_clean["region"].value_counts(dropna=False))
print(orders_clean["product"].value_counts(dropna=False))

print(orders_clean["quantity"].min())
print(orders_clean["quantity"].max())

print(orders_clean["unit_price"].min())
print(orders_clean["unit_price"].max())

print(orders_clean["discount_pct"].min())
print(orders_clean["discount_pct"].max())

print(orders_clean.dtypes)

print(orders_clean[(orders_clean["quantity"] <= 0) | (orders_clean["unit_price"] <= 0) | (orders_clean["discount_pct"] < 0) | (orders_clean["discount_pct"] > 1)])

orders_clean.to_csv("orders_clean.csv", index=False)
high_quantity_orders.to_csv("high_quantity_orders.csv", index=False)