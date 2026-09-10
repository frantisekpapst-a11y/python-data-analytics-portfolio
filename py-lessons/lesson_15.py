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

print("""
==========================================
BUSINESS SUMMARY — LEKCE 15
==========================================

1. Praha má 3 objednávky s celkovými tržbami 4000.
   Průměrná hodnota objednávky je cca 1333.

2. Brno má 3 objednávky s celkovými tržbami 3000.
   Průměrná hodnota objednávky je 1000.

3. Ostrava má pouze 2 objednávky, ale celkové tržby 9300.
   Na první pohled tedy vypadá jako nejsilnější region.

4. Výsledek Ostravy je výrazně ovlivněn jednou
   mimořádně vysokou objednávkou s revenue 8500.

5. IQR metoda tuto objednávku označila jako potenciální outlier.

6. Po odstranění outlieru má Ostrava:
   - 1 objednávku;
   - celkové tržby 800;
   - průměrné tržby 800.

    Bez outlieru je tedy Ostrava naopak nejslabší region.

7. EDA ukázala, že jedna extrémní hodnota může výrazně
   změnit business interpretaci výsledků.

8. Mezi množstvím a tržbami existuje velmi silná
   pozitivní korelace.

   I bez outlieru zůstává vztah silný,takže outlier
    vztah zesiluje, ale nevytváří ho sám.

9. Distribuce revenue je right-skewed:
    většina objednávek má nižší hodnotu, zatímco jedna
    vysoká objednávka vytváří dlouhý ocas doprava.

HLAVNÍ BUSINESS ZÁVĚR:

Samotný součet tržeb nestačí k hodnocení výkonu regionu.

Před rozhodnutím je potřeba zkontrolovat:
- počet objednávek;
- průměrnou hodnotu objednávky;
- distribuci;
- outliery;
- zda výsledek není závislý na několika extrémních případech.
""")