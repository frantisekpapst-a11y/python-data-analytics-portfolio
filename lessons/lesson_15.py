import pandas as pd

sales = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "region": [
        "Praha", "Praha", "Brno", "Brno",
        "Praha", "Ostrava", "Brno", "Ostrava"
    ],
    "revenue": [
        1200, 1500, 900, 1100,
        1300, 800, 1000, 8500
    ],
    "quantity": [
        2, 3, 1, 2,
        2, 1, 2, 10
    ]
})

print(sales.shape)
sales.info()
print(sales.describe())

top_3 = (
    sales.sort_values(
        by="revenue",
        ascending=False
    )
    .head(3)
)

print(top_3)

print(sales["region"].value_counts())

sales_by_region = (
    sales.groupby(
        "region",
        as_index=False)
    ["revenue"]
    .sum()
)

print(sales_by_region)

region_summary = (
    sales.groupby(
        "region",
        as_index=False
    )
    .agg(
        orders_count=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean")
    )
)

print(region_summary)

q1 = sales["revenue"].quantile(0.25)
q3 = sales["revenue"].quantile(0.75)

print(q1)
print(q3)

iqr = q3 - q1

print(iqr)

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(lower_bound)
print(upper_bound)

outliers = sales[
    (sales["revenue"] < lower_bound)
    | (sales["revenue"] > upper_bound)
]

print(outliers)

sales_no_outlier = sales[
    sales["revenue"] <= upper_bound
]

region_summary_no_outlier = (
    sales_no_outlier.groupby(
        "region",
        as_index=False
    )
    .agg(
        orders_count=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean"),
        )
)

print(region_summary_no_outlier)

correlation = sales[
    ["quantity", "revenue"]
].corr()

print(correlation)

correlation_no_outlier = sales_no_outlier[
    ["quantity", "revenue"]
].corr()

print(correlation_no_outlier)

import matplotlib.pyplot as plt

sales["revenue"].hist(
    bins=5
)

plt.show()

sales.boxplot(
    column="revenue"
)

plt.show()