df.groupby("podle_čeho")["co_počitám"].agregace()

df.groupby("category")["total"].sum()

df.groupby("category")["total"].sum().reset_index()

df.groupby("customer_id")["order_id"].count()

sales_by_category = df.groupby("category")["total"].sum()

average_by_category = df.groupby("category")["total"].mean()

orders_by_customer = df.groupby("customer_id")["order_id"].count()

summary = (
    df.groupby("category")["total"]
    .agg(["sum", "mean", "min", "max"])
    .reset_index()
)

df["total"].describe()

df.describe()

category_summary = (
    df.groupby("category")
    .agg({
        "total": ["sum", "mean"],
        "quantity": ["sum", "max"]
    })
    .reset_index()
)

filtered_orders = df[df["quantity"] >= 2]

category_summary = filtered_orders.groupby("category")["total"].mean().reset_index()

high_value_categories = category_summary[category_summary["total"] > 15000]

filtered_orders = df[df["quantity"] > 2]

category_summary = (
    filtered_orders.groupby("category")["total"]
    .agg(["sum", "mean"])
    .reset_index()
    )

high_categories = category_summary[category_summary["sum"] > 30000]

category_summary = (
    df.groupby("category")
    .agg(
        total_revenue=("total", "sum"),
        avg_order_value=("total", "mean"),
        max_order_value=("total", "max"),
        total_quantity=("quantity", "sum")
    )
    .reset_index()
)

category_summary = (
    df.groupby("category")
    .agg(
        total_revenue=("total", "sum"),
        avg_order_value=("total", "mean"),
        max_quantity=("quantity", "max")
    )
    .reset_index()
)

summary = (
    df.groupby(["category", "region"])["total"]
    .sum()
    .reset_index()
)

summary = df.groupby(["category", "region"])["total"].sum().reset_index()