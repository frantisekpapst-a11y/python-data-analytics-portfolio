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

sales["revenue_per_item"] = (
    sales["revenue"]
    / sales["quantity"]
)

print(
    sales[
        [
            "quantity",
            "revenue",
            "revenue_per_item"
        ]
    ]
)

print(
    sales[
        [
            "quantity",
            "revenue"
        ]
    ].corr()
)

print(
    sales[
        [
            "quantity",
            "revenue_per_item"
        ]
    ].corr()
)

from scipy.stats import pearsonr

r, p_value = pearsonr(
    sales["quantity"],
    sales["revenue"]
)

print("r:", r)
print("p-value:", p_value)

group_a = sales[
    sales["region"] == "Praha"
]["revenue"]

group_b = sales[
    sales["region"] == "Brno"
]["revenue"]

print(group_a)
print(group_b)

from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

print("t-statistic:", t_stat)
print("p-value:", p_value)

customers = pd.DataFrame({
    "region": [
        "Praha", "Praha", "Praha", "Praha",
        "Brno", "Brno", "Brno", "Brno",
        "Ostrava", "Ostrava", "Ostrava", "Ostrava"
    ],
    "customer_type": [
        "B2B", "B2B", "B2C", "B2C",
        "B2B", "B2B", "B2B", "B2C",
        "B2C", "B2C", "B2C", "B2B"
    ]
})

contingency_table = pd.crosstab(
    customers["region"],
    customers["customer_type"]
)

print(contingency_table)

from scipy.stats import chi2_contingency

chi2, p_value, dof, expected = chi2_contingency(
    contingency_table
)

print("chi2:", chi2)
print("p-value:", p_value)
print("dof:", dof)
print("expected:")
print(expected)

praha = sales.loc[
    sales["region"] == "Praha",
    "revenue"
]

brno = sales.loc[
    sales["region"] == "Brno",
    "revenue"
]

ostrava = sales.loc[
    sales["region"] == "Ostrava",
    "revenue"
]

from scipy.stats import f_oneway

f_stat, p_value = f_oneway(
    praha,
    brno,
    ostrava
)

print("F-statistic:", f_stat)
print("p-value:", p_value)

from scipy.stats import mannwhitneyu

u_stat, p_value = mannwhitneyu(
    praha,
    brno,
    alternative="two-sided"
)

print("U-statistic:", u_stat)
print("p-value:", p_value)

from scipy.stats import shapiro

stat, p_value = shapiro(
    praha
)

print("statistic:", stat)
print("p-value:", p_value)

print("""
==========================================
BUSINESS SUMMARY — LEKCE 16
==========================================

1. Korelace mezi quantity a revenue je velmi silná a pozitivní.
   Pearsonův koeficient je přibližně 0.99.

2. Velmi nízká p-value u Pearsonovy korelace ukazuje,
   že tento vztah je statisticky významný.

3. Statisticky významná korelace ale sama o sobě
   neprokazuje kauzalitu.

4. t-test mezi Prahou a Brnem vyšel statisticky významně:
   p-value < 0.05.

   To znamená, že v našem vzorku existuje důkaz
   o rozdílu průměrného revenue mezi těmito dvěma regiony.

5. Mann-Whitney U test pro Prahu a Brno ale vyšel:
   p-value > 0.05.

   To ukazuje, že výsledek není úplně robustní
   a je citlivý na zvolenou metodu a malý počet dat.

6. Chi-square test mezi regionem a customer_type vyšel:
   p-value > 0.05.

   Nemáme tedy dost důkazů, že region a typ zákazníka
   spolu v našem vzorku statisticky významně souvisejí.

7. ANOVA pro Prahu, Brno a Ostravu vyšla:
   p-value > 0.05.

   Nemáme tedy dost důkazů, že se průměrné revenue
   mezi všemi regiony statisticky významně liší.

8. Shapiro-Wilk test pro Prahu neukázal
   statisticky významnou odchylku od normality.

   Vzorek je ale velmi malý, takže tento výsledek
   nelze interpretovat příliš silně.

HLAVNÍ BUSINESS ZÁVĚR:

Statistické testy mohou pomoci ověřit,
zda pozorovaný rozdíl nebo vztah není pouze náhodný.

Samotná p-value ale nestačí.

Při business interpretaci je vždy potřeba zohlednit:
- velikost vzorku
- kvalitu dat
- outliery
- rozložení dat
- velikost samotného rozdílu
- business význam výsledku

Statisticky významný výsledek
nemusí být automaticky businessově důležitý.

A naopak:
businessově důležitý rozdíl
nemusí být při malém vzorku statisticky významný.
""")