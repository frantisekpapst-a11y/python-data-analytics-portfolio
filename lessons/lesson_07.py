import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

df["total"] = df["quantity"] * df["unit_price"]

average_order = df["total"].mean()

above_average_furniture = df[(df["total"] > average_order) & (df["category"] == "Furniture")]

print(above_average_furniture)

furniture_or_electronics = df[(df["category"] == "Furniture") | (df["category"] == "Electronics")]

print(furniture_or_electronics)

high_value_or_high_quantity = df[(df["total"] > 20000) | (df["quantity"] >= 4)]

print(high_value_or_high_quantity)

not_furniture = df[~(df["category"] == "Furniture")]

print(not_furniture)

selected_products = df[df["product"].isin(["Laptop", "Desk", "Monitor"])]

print(selected_products)

other_products = df[~df["product"].isin(["Laptop", "Desk", "Monitor"])]

print(other_products)

mid_value_orders = df[df["total"].between(10000, 20000)]

print(mid_value_orders)

mid_value_orders_exclusive = df[df["total"].between(10000, 20000, inclusive="neither")]

print(mid_value_orders_exclusive)

furniture_summary = df.loc[(df["category"] == "Furniture"), ["product", "quantity", "total"]]

print(furniture_summary)

furniture_high_values = df.loc[(df["category"] == "Furniture") & (df["total"] > 10000), ["product", "quantity", "total"]]

print(furniture_high_values)

electronics_summary = df.loc[df["category"] == "Electronics", ["product", "total"]]

print(electronics_summary)

first_three_rows = df.iloc[0:3]

print(first_three_rows)

first_four_selected_columns = df.iloc[0:4, 1:4]

print(first_four_selected_columns)