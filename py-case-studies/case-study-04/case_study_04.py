import pandas as pd

orders = pd.DataFrame({
    "order_id": [
        5001, 5002, 5003, 5004, 5005,
        5006, 5007, 5008, 5009, 5010,
        5011, 5012, 5013, 5014, 5014
    ],
    "customer_id": [
        101, 102, 103, 101, 104,
        105, 106, 107, 108, 109,
        110, 111, 999, 104, 104
    ],
    "product_id": [
        501, 502, 503, 504, 501,
        505, 502, 503, 504, 505,
        501, 502, 503, 504, 504
    ],
    "quantity": [
        1, 2, 1, 3, 1,
        2, 1, 2, 1, 4,
        1, 2, 1, None, None
    ],
    "discount_pct": [
        0, 0.10, 0.05, 0, 0.15,
        0, 0.05, 0, 0.20, 0,
        0.10, 0, 0, 0.05, 0.05
    ]
})

customers = pd.DataFrame({
    "customer_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110, 111
    ],
    "customer_name": [
        "Jan Novák",
        "Petra Malá",
        "Tomáš Dvořák",
        "Eva Černá",
        "Martin Král",
        "Lucie Veselá",
        "Pavel Horák",
        "Anna Němcová",
        "Karel Marek",
        "Jana Procházková",
        "Marek Jelínek"
    ],
    "customer_type": [
        "B2C", "B2B", "B2C", "B2B", "B2C",
        "B2B", "B2C", "B2C", "B2B", "B2C", "B2B"
    ],
    "region": [
        "Praha", "Brno", "Plzeň", "Ostrava", "Praha",
        "Brno", "Plzeň", None, "Praha", "Ostrava", "Brno"
    ]
})

products = pd.DataFrame({
    "product_id": [501, 502, 503, 504, 505],
    "product_name": [
        "Laptop",
        "Monitor",
        "Desk",
        "Mouse",
        "Office Chair"
    ],
    "category": [
        "Electronics",
        "Electronics",
        "Furniture",
        "Accessories",
        "Furniture"
    ],
    "unit_price": [
        25000, 7000, 12000, 800, 9000
    ],
    "unit_cost": [
        19000, 4800, 8500, 350, 6200
    ]
})

orders_raw = orders.copy()
customers_raw = customers.copy()
products_raw = products.copy()

orders_raw.to_csv("orders_raw.csv", index=False)
customers_raw.to_csv("customers_raw.csv", index=False)
products_raw.to_csv("products_raw.csv", index=False)

print(orders.head())
print(customers.head())
print(products.head())

print(orders.shape)
print(customers.shape)
print(products.shape)

print(customers["customer_type"].unique())
print(customers["region"].unique())
print(products["product_name"].unique())
print(products["category"].unique())

customers["customer_type"] = (customers["customer_type"].str.strip().str.upper())
customers["region"] = (customers["region"].str.strip().str.title())
products["product_name"] = (products["product_name"].str.strip().str.title())
products["category"] = (products["category"].str.strip().str.title())
customers["region"] = (customers["region"].replace("", pd.NA))

print(orders.isna().sum())
print(customers.isna().sum())
print(products.isna().sum())

print(orders.duplicated().sum())
print(customers.duplicated().sum())
print(products.duplicated().sum())

print(orders[orders["quantity"].isna()])
print(customers[customers["region"].isna()])
print(orders[orders.duplicated()])

orders = orders.drop_duplicates()
print(orders[orders.duplicated()])

print(orders["quantity"].median())

orders["quantity"] = (orders["quantity"].fillna(orders["quantity"].median()))

print(orders.isna().sum())

print(orders[orders["customer_id"] == 108])

customers["region"] = (customers["region"].fillna("Unknown"))

print(customers.isna().sum())

print(orders.dtypes)
print(customers.dtypes)
print(products.dtypes)

products["unit_price"] = products["unit_price"].astype(float)
products["unit_cost"] = products["unit_cost"].astype(float)

print(orders[(orders["quantity"] <= 0) | (orders["discount_pct"] < 0) | (orders["discount_pct"] > 1)])
print(products[(products["unit_price"] <= 0) | (products["unit_cost"] <= 0) | (products["unit_cost"] > products["unit_price"])])

print(customers["customer_id"].duplicated().sum())
print(products["product_id"].duplicated().sum())

print(orders[~orders["customer_id"].isin(customers["customer_id"])])
print(orders[~orders["product_id"].isin(products["product_id"])])

orders["notes"] = ""
orders.loc[orders["customer_id"] == 999, "notes"] = "Unknown customer"

orders_with_customers = orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
print(len(orders))
print(len(orders_with_customers))
print(orders_with_customers.isna().sum())

print(orders_with_customers[orders_with_customers["customer_name"].isna()])

final_df = orders_with_customers.merge(products, on="product_id", how="left", validate="many_to_one")
print(len(orders_with_customers))
print(len(final_df))
print(final_df.isna().sum())

print(final_df.loc[final_df["customer_name"].isna(), ["order_id", "customer_id", "notes"]])

orders_with_customers.to_csv("orders_with_customers.csv", index=False)
final_df.to_csv("final_df.csv", index=False)

print(final_df.head())

final_df["revenue"] = final_df["quantity"] * final_df["unit_price"] * (1 - final_df["discount_pct"])
final_df["cost"] = final_df["quantity"] * final_df["unit_cost"]
final_df["profit"] = final_df["revenue"] - final_df["cost"]

category_summary = (
    final_df.groupby("category")
    .agg(
        category_total_revenue=("revenue", "sum"),
        category_total_cost=("cost", "sum"),
        category_total_profit=("profit", "sum")
    )
    .reset_index()
)

region_summary = (
    final_df.groupby("region")
    .agg(
        region_total_revenue=("revenue", "sum"),
        region_total_profit=("profit", "sum")
    )
    .reset_index()
)

customer_type_summary = (
    final_df.groupby("customer_type")
    .agg(
        customer_type_total_revenue=("revenue", "sum"),
        customer_type_total_profit=("profit", "sum")
    )
    .reset_index()
)

final_df["customer_name"] = (final_df["customer_name"].fillna("Unknown"))

customer_summary = (
    final_df.groupby("customer_name")
    .agg(
        customer_total_revenue=("revenue", "sum"),
        customer_total_profit=("profit", "sum")
    )
    .reset_index()
)

product_summary = (
    final_df.groupby("product_name")
    .agg(
        product_total_revenue=("revenue", "sum"),
        product_total_profit=("profit", "sum")
    )
    .reset_index()
)

product_summary["profit_margin"] = (product_summary["product_total_profit"] / product_summary["product_total_revenue"])
product_summary["profit_margin"] = (product_summary["profit_margin"] *100).round(1)

category_summary = category_summary.sort_values(by="category_total_revenue", ascending=False)
region_summary = region_summary.sort_values(by="region_total_revenue", ascending=False)
customer_type_summary = customer_type_summary.sort_values(by="customer_type_total_revenue", ascending=False)
customer_summary = customer_summary.sort_values(by="customer_total_revenue", ascending=False)
product_summary = product_summary.sort_values(by="product_total_revenue", ascending=False)

print(category_summary)
print(region_summary)
print(customer_type_summary)
print(customer_summary)
print(product_summary)

print("")
print("=" * 80)
print("BUSINESS SUMMARY")
print("=" * 80)

print("\nCATEGORY SUMMARY")
print("-" * 80)
print(category_summary.to_string(index=False))

print("\nREGION SUMMARY")
print("-" * 80)
print(region_summary.to_string(index=False))

print("\nCUSTOMER TYPE SUMMARY")
print("-" * 80)
print(customer_type_summary.to_string(index=False))

print("\nCUSTOMER SUMMARY")
print("-" * 80)
print(customer_summary.to_string(index=False))

print("\nPRODUCT SUMMARY")
print("-" * 80)
print(product_summary.to_string(index=False))

print("")
print("=" * 80)
print("KEY CONCLUSIONS")
print("=" * 80)

print("1. Kategorie Electronics vygenerovala nejvyšší tržby, zatímco Furniture nejvyšší zisk.")

print("2. Praha byla nejsilnějším regionem podle tržeb i zisku.")

print("3. B2C zákazníci vygenerovali mírně vyšší tržby i zisk než B2B zákazníci.")

print("4. Karel Marek byl nejhodnotnějším zákazníkem podle tržeb i zisku.")

print("5. Laptop vygeneroval nejvyšší tržby ze všech produktů, ale měl nejnižší ziskovou marži.")

print("6. Office Chair vygenerovala nejvyšší absolutní zisk ze všech produktů.")

print("7. Mezi problémy kvality dat patřila jedna duplicitní objednávka, jedna chybějící hodnota quantity, jeden chybějící region a jeden neznámý zákazník.")
