import pandas as pd

orders = pd.read_csv("case_study_03_b2b_b2c_orders.csv")

print(orders.head())

print(orders.shape)

print(orders.columns)

orders.info()

print(orders.isna().sum())

orders_clean = orders.copy()

orders_clean["order_date"] = pd.to_datetime(orders_clean["order_date"])

orders_clean["customer_type"] = orders_clean["customer_type"].fillna("Unknown")

orders_clean["region"] = orders_clean["region"].fillna("Unknown")

orders_clean = orders_clean.dropna(subset=["product"])

orders_clean["unit_price"] = orders_clean["unit_price"].fillna(orders_clean["unit_price"].median())

orders_clean["unit_cost"] = orders_clean["unit_cost"].fillna(orders_clean["unit_cost"].median())

orders_clean["payment_method"] = orders_clean["payment_method"].fillna("Unknown")

print(orders_clean.isna().sum())

orders_clean["gross_sales"] = orders_clean["quantity"] * orders_clean["unit_price"]

orders_clean["discount_amount"] = orders_clean["gross_sales"] * orders_clean["discount_pct"]

orders_clean["net_sales"] = orders_clean["gross_sales"] - orders_clean["discount_amount"]

orders_clean["total_cost"] = orders_clean["quantity"] * orders_clean["unit_cost"]

orders_clean["profit"] = orders_clean["net_sales"] - orders_clean["total_cost"] - orders_clean["shipping_cost"]

print(orders_clean[["quantity", "unit_price", "discount_pct", "gross_sales", "discount_amount", "net_sales", "total_cost", "shipping_cost", "profit"]].head(10))

total_gross_sales = orders_clean["gross_sales"].sum()

total_net_sales = orders_clean["net_sales"].sum()

total_profit = orders_clean["profit"].sum()

average_net_sales = orders_clean["net_sales"].mean()

max_net_sales = orders_clean["net_sales"].max()

min_profit = orders_clean["profit"].min()

loss_orders = orders_clean[orders_clean["profit"] < 0]

loss_orders_count = len(loss_orders)

b2b_orders = orders_clean[orders_clean["customer_type"] == "B2B"]

b2c_orders = orders_clean[orders_clean["customer_type"] == "B2C"]

b2b_net_sales = b2b_orders["net_sales"].sum()

b2c_net_sales = b2c_orders["net_sales"].sum()

b2b_profit = b2b_orders["profit"].sum()

b2c_profit = b2c_orders["profit"].sum()

orders_clean.to_csv("case_study_03_clean_orders.csv", index=False)

print("")
print("=" * 60)
print("BUSINESS SUMMARY:")
print("=" * 60)

print("Celkové hrubé tržby:", round(total_gross_sales, 2), "Kč")
print("Celkové čisté tržby:", round(total_net_sales, 2), "Kč")
print("Celkový zisk:", round(total_profit, 2), "Kč")

print("-" * 60)

print("Průměrná hodnota objednávky po slevě:", round(average_net_sales, 2), "Kč")
print("Nejvyšší hodnota objednávky po slevě:", round(max_net_sales, 2), "Kč")
print("Nejvyšší ztráta na objednávce:", round(min_profit, 2), "Kč")
print("Počet ztrátových objednávek:", loss_orders_count)

print("-" * 60)

print("Čisté tržby B2B:", round(b2b_net_sales, 2), "Kč")
print("Čisté tržby B2C:", round(b2c_net_sales, 2), "Kč")
print("Zisk B2B:", round(b2b_profit, 2), "Kč")
print("Zisk B2C:", round(b2c_profit, 2), "Kč")