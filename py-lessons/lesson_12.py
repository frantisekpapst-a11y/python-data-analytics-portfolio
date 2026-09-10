import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "customer_id": [1, 2, 3, 1, 4, 5],
    "product": [
        "Laptop",
        "Monitor",
        "Desk",
        "Mouse",
        "Office Chair",
        "Keyboard"
    ],
    "quantity": [1, 2, 1, 3, 2, 1],
    "total": [25000, 14000, 12000, 2400, 18000, 1500]
})

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 6],
    "customer_name": [
        "Jan Novák",
        "Petra Malá",
        "Tomáš Dvořák",
        "Eva Černá",
        "Martin Král"
    ],
    "region": [
        "Praha",
        "Brno",
        "Plzeň",
        "Ostrava",
        "Liberec"
    ]
})

print(orders)
print(customers)

orders_with_customers_left = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print(orders_with_customers_left)

orders_with_customers_inner = orders.merge(
    customers,
    on="customer_id",
    how="inner"
)

print(orders_with_customers_inner)

orders_with_customers_right = orders.merge(
    customers,
    on="customer_id",
    how="right"
)

print(orders_with_customers_right)

orders_with_customers_outer = orders.merge(
    customers,
    on="customer_id",
    how="outer"
)

print(orders_with_customers_outer)

orders = pd.DataFrame({
    "order_id": [2001, 2002, 2003, 2004, 2005],
    "customer_id": [101, 102, 103, 101, 104],
    "product": ["Laptop", "Monitor", "Desk", "Mouse", "Keyboard"],
    "total": [28000, 9000, 15000, 1200, 2200]
})

customers = pd.DataFrame({
    "id": [101, 102, 103, 105],
    "customer_name": [
        "Jan Novák",
        "Petra Malá",
        "Tomáš Dvořák",
        "Eva Černá"
    ],
    "region": [
        "Praha",
        "Brno",
        "Plzeň",
        "Ostrava"
    ]
})

print(orders)
print(customers)

print(customers["id"].nunique())
print(len(customers))

print(orders["customer_id"].duplicated().sum())
print(customers["id"].duplicated().sum())

orders_with_customers_left = orders.merge(
customers,
left_on="customer_id",
right_on="id",
how="left"
)

print(orders_with_customers_left)

    print(orders_with_customers_left.isna().sum())

orders_with_customers_left = orders_with_customers_left.drop(
    columns=["id"]
)

print(orders_with_customers_left)

orders_with_customers_left["customer_name"] = (
    orders_with_customers_left["customer_name"]
    .fillna("Unknown")
)

orders_with_customers_left["region"] = (
    orders_with_customers_left["region"]
    .fillna("Unknown")
)

print(orders_with_customers_left)

print(len(orders))
print(len(orders_with_customers_left))

orders_with_customers = orders.merge(
    customers,
    left_on="customer_id",
    right_on="id",
    how="left",
    validate="many_to_one"
)

print(orders_with_customers)

orders = pd.DataFrame({
    "order_id": [3001, 3002, 3003, 3004],
    "customer_id": [101, 102, 103, 104],
    "region": ["West", "East", "North", "South"],
    "total": [12000, 18000, 9000, 15000]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "customer_name": [
        "Jan Novák",
        "Petra Malá",
        "Tomáš Dvořák",
        "Eva Černá"
    ],
    "region": [
        "Praha",
        "Brno",
        "Plzeň",
        "Ostrava"
    ]
})

print(orders)
print(customers)

result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    suffixes=("_order", "_customer"),
    validate="many_to_one"
)

print(result)

orders = pd.DataFrame({
    "order_id": [4001, 4002, 4003, 4004],
    "customer_id": [101, 102, 103, 101],
    "product_id": [501, 502, 503, 504],
    "quantity": [1, 2, 1, 3]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "customer_name": ["Jan Novák", "Petra Malá", "Tomáš Dvořák"],
    "region": ["Praha", "Brno", "Plzeň"]
})

products = pd.DataFrame({
    "product_id": [501, 502, 503, 504],
    "product_name": ["Laptop", "Monitor", "Desk", "Mouse"],
    "category": ["Electronics", "Electronics", "Furniture", "Accessories"],
    "unit_price": [25000, 7000, 12000, 800]
})

print(orders)
print(customers)
print(products)

orders_customers = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print(orders_customers)

final_df = orders_customers.merge(
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)

print(final_df)