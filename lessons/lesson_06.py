import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

print(df)

print(df.head())

print(type(df))

print(df["product"])

print(type(df["product"]))

print(df.info())

df.info()

print(df.shape)

print(df.columns)

df["total"] = df["quantity"] * df["unit_price"]

total_revenue = df["total"].sum()

average_order = df["total"].mean()

print("Celkové tržby:", total_revenue)

print("Průměrná objednávka:", average_order)

print(df["total"] > average_order)

above_average_orders = df[df["total"] > average_order]

furniture_orders = df[df["category"] == "Furniture"]

total_revenue_furniture = furniture_orders["total"].sum()

average_order_furniture = furniture_orders["total"].mean()

sorted_orders = df.sort_values(by="total", ascending=False)

above_average_orders.to_csv("above_average_orders_pandas.csv", index=False)

above_average_orders.to_json("above_average_orders.json", orient="records", indent=4)

above_average_orders.to_excel("above_average_orders.xlsx", index=False)