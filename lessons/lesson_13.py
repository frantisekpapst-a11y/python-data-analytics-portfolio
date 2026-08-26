import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "order_date": [
        "2026-08-01",
        "2026-08-05",
        "2026-08-12",
        "2026-08-20"
    ],
    "revenue": [1200, 800, 1500, 600]
})

print(orders.dtypes)

orders["order_date"] = pd.to_datetime(orders["order_date"])

print(orders.dtypes)

orders["year"] = orders["order_date"].dt.year
orders["month"] = orders["order_date"].dt.month

print(orders.head())

print(orders.dtypes)

orders["day"] = orders["order_date"].dt.day

print(orders.head())

print(orders.dtypes)

orders["year_month"] = orders["order_date"].dt.strftime("%Y_%m")

print(orders.head())

print(orders.dtypes)

print(orders[["order_date", "year_month"]])

monthly_sales = orders.groupby("year_month")["revenue"].sum().reset_index()

print(monthly_sales)

new_orders = pd.DataFrame({
    "order_id": [5, 6],
    "order_date": ["2026-07-05", "2026-08-20"],
    "revenue": [1500, 900]
})

orders = pd.concat([orders, new_orders], ignore_index=True)

orders["order_date"] = pd.to_datetime(orders["order_date"])

orders["year"] = orders["order_date"].dt.year
orders["month"] = orders["order_date"].dt.month
orders["day"] = orders["order_date"].dt.day
orders["year_month"] = orders["order_date"].dt.strftime("%Y_%m")

print(orders)

monthly_sales = orders.groupby("year_month")["revenue"].sum().reset_index()

print(monthly_sales)

monthly_sales = (orders.groupby("year_month", as_index=False)["revenue"].sum())

print(monthly_sales)

august_orders = orders[orders["order_date"] >= "2026-08-01"]

print(august_orders)

orders["order_date"] = orders["order_date"].dt.strftime("%Y.%m.%d")
print(orders)

orders["order_date"] = pd.to_datetime(orders["order_date"])
print(orders)

orders["delivery_date"] = pd.to_datetime([
    "2026-08-03",
    "2026-08-08",
    "2026-08-15",
    "2026-08-25",
    "2026-07-09",
    "2026-08-23"
])

orders["delivery_days"] = (orders["delivery_date"] - orders["order_date"]).dt.days

print(orders)

orders["day_name"] = orders["order_date"].dt.day_name()

print(orders)

orders["day_name"] = orders["order_date"].dt.day_name(locale="cs_CZ")

print(orders)

filtered_orders = orders[(orders["order_date"] >= "2026-08-05") & (orders["order_date"] <= "2026-08-15")]

print(orders)

filtered_orders = orders[orders["order_date"].between("2026-08-05", "2026-08-15")]

print(orders)

orders = orders.sort_values(by="order_date")

print(orders)

orders = orders.sort_values(by="order_date", ascending=False)

print(orders)