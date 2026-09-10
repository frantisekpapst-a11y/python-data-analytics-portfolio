import pandas as pd

import matplotlib.pyplot as plt

df = pd.DataFrame({
    "month": ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05"],
    "revenue": [120000, 135000, 128000, 150000, 165000]
})

plt.plot(df["month"], df["revenue"])

plt.show()

plt.figure(figsize=(8, 4))

plt.plot(
    df["month"], 
    df["revenue"], 
    marker="o")

plt.title("Měsíční tržby")
plt.xlabel("Měsíc")
plt.ylabel("Tržby")

plt.yticks(
    ticks=[120000, 130000, 140000, 150000, 160000],
    labels=["120k", "130k", "140k", "150k", "160k"]
)

plt.grid(True)

plt.tight_layout()

plt.show()

from matplotlib.ticker import FuncFormatter

plt.figure(figsize=(8, 4))

plt.plot(
    df["month"],
    df["revenue"],
    marker="o"
)

plt.title("Měsíční tržby")
plt.xlabel("Měsíc")
plt.ylabel("Tržby")

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1000:.0f}k")
)

plt.grid(True)
plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 4))

plt.plot(
    df["month"],
    df["revenue"],
    marker="o"
)

plt.title(
    "Měsíční tržby",
    fontweight="bold"
)

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1000:.0f}k"),
    )

plt.grid(True)
plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "region": ["Praha", "Brno", "Plzeň", "Ostrava"],
    "revenue": [520000, 410000, 465000, 350000]
})

plt.figure(figsize=(8, 4))

plt.bar(
    df["region"],
    df["revenue"]
)

plt.title(
    "Tržby podle regionu",
    fontweight="bold"
)

plt.xlabel(
    "Region",
    fontweight="bold"
)

plt.ylabel(
    "Tržby",
    fontweight="bold"
)

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1000:.0f}k")
)

plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 4))

plt.bar(
    df["region"],
    df["revenue"]
)

plt.title(
    "Tržby podle regionu",
    fontweight="bold"
)

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1000:.0f}k")
)

plt.tight_layout()

plt.show()

df = df.sort_values(
    by="revenue",
    ascending=False
)

plt.figure(figsize=(8, 4))

plt.bar(
    df["region"],
    df["revenue"]
)

plt.title(
    "Tržby podle regionu",
    fontweight="bold"
)

plt.gca().yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x / 1000:.0f}k")
)

plt.grid(
    axis="y",
    alpha=0.5
)

plt.gca().set_axisbelow(True)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "ad_spend": [10, 15, 20, 25, 30, 35],
    "revenue": [80, 110, 150, 170, 210, 250]
})

plt.figure(figsize=(8, 4))

plt.scatter(
    df["ad_spend"],
    df["revenue"]
)

plt.title(
    "Vztah nákladů a tržeb",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    alpha=0.5
)

plt.tight_layout()

plt.show()

plt.figure(figsize=(7, 4))

plt.scatter(
    df["ad_spend"],
    df["revenue"],
    s=70
)

plt.title(
    "Vztah nákladů a tržeb",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    alpha=0.3
)

plt.tight_layout()

plt.show()

import numpy as np

trend = np.polyfit(
    df["ad_spend"],
    df["revenue"],
    1
)

trend_line = np.poly1d(trend)

plt.figure(figsize=(7, 4))

plt.scatter(
    df["ad_spend"],
    df["revenue"],
    s=70
)

plt.plot(
    df["ad_spend"],
    trend_line(df["ad_spend"])
)

plt.title(
    "Vztah nákladů a tržeb",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "resolution_hours": [2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 12, 14, 18, 22, 30]
})

plt.figure(figsize=(7, 4))

plt.hist(
    df["resolution_hours"],
    bins=6
)

plt.title(
    "Distribuce doby řešení",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.tight_layout()

plt.show()

plt.figure(figsize=(7, 4))

plt.hist(
    df["resolution_hours"],
    bins=[0, 5, 10, 15, 20, 25, 30, 35],
    rwidth=0.9,
    edgecolor="black"
)

plt.title(
    "Distribuce doby řešení",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.tight_layout()

plt.show()

mean_value = df["resolution_hours"].mean()
median_value = df["resolution_hours"].median()

plt.figure(figsize=(7, 4))

plt.hist(
    df["resolution_hours"],
    bins=[0, 5, 10, 15, 20, 25, 30, 35],
    rwidth=0.9,
    edgecolor="black"
)

plt.axvline(
    mean_value,
    linestyle="--",
    label="Průměr"
)

plt.axvline(
    median_value,
    linestyle=":",
    label="Medián"
)

plt.title(
    "Distribuce doby řešení",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.legend()

plt.tight_layout()

plt.show()

mean_value = df["resolution_hours"].mean()
median_value = df["resolution_hours"].median()

plt.figure(figsize=(7, 4))

plt.hist(
    df["resolution_hours"],
    bins=[0, 5, 10, 15, 20, 25, 30, 35],
    rwidth=0.9,
    edgecolor="black",
    zorder=2
)

plt.axvline(
    mean_value,
    linestyle="--",
    linewidth=2,
    color="red",
    label="Průměr",
    zorder=5
)

plt.axvline(
    median_value,
    linestyle=":",
    linewidth=2,
    color="black",
    label="Medián",
    zorder=5
)

plt.title(
    "Distribuce doby řešení",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.legend()

plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "resolution_hours": [2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 12, 14, 18, 22, 30]
})

plt.figure(figsize=(7, 4))

plt.boxplot(
    df["resolution_hours"],
    tick_labels=["Doba řešení"]
)

plt.title(
    "Rozdělení doby řešení",
    fontweight="bold"
)

plt.xticks(fontweight="bold")
plt.yticks(fontweight="bold")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.gca().set_axisbelow(True)

plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "segment": ["B2B", "B2C", "Partner"],
    "revenue": [520000, 350000, 130000]
})

plt.figure(figsize=(6, 6))

plt.pie(
    df["revenue"],
    labels=df["segment"],
    autopct="%1.1f%%"
)

plt.title(
    "Podíl tržeb podle segmentu",
    fontweight="bold"
)

plt.tight_layout()

plt.show()

def autopct_with_values(values):
    def my_format(pct):
        total = sum(values)
        absolute = int(round(pct / 100 * total))
        return f"{pct:.1f}%\n({absolute:,} Kč)".replace(",", " ")
    return my_format

plt.figure(figsize=(7, 7))

wedges, texts, autotexts = plt.pie(
    df["revenue"],
    labels=df["segment"],
    autopct=autopct_with_values(df["revenue"]),
    explode=[0.03, 0.03, 0.03],
    startangle=90,
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 2
    },
    textprops={
        "fontweight": "bold"
    }
)

plt.title(
    "Podíl tržeb podle segmentu",
    fontweight="bold"
)

for text in texts:
    text.set_fontweight("bold")

for autotext in autotexts:
    autotext.set_fontweight("bold")

plt.tight_layout()

plt.show()

df = pd.DataFrame({
    "month": ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05"],
    "revenue": [120000, 135000, 128000, 150000, 165000]
})

df.plot(
    x="month",
    y="revenue"
)

plt.show()

df.plot(
    x="month",
    y="revenue",
    kind="bar"
)

plt.show()