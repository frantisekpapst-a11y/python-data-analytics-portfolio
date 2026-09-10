import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "month": ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05"],
    "revenue": [120000, 135000, 128000, 150000, 165000]
})

fig = px.line(
    df,
    x="month",
    y="revenue",
    markers=True,
    title="Monthly Revenue"
)

fig.show()

fig = px.line(
    df,
    x="month",
    y="revenue",
    markers=True,
    title="Měsíční tržby"
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)

fig.update_xaxes(
    type="category"
)

fig.update_yaxes(
    tickformat="~s"
)

fig.show()

df = pd.DataFrame({
    "region": ["Praha", "Brno", "Plzeň", "Ostrava"],
    "revenue": [520000, 410000, 465000, 350000]
})

df = df.sort_values(
    by="revenue",
    ascending=False
)

fig = px.bar(
    df,
    x="region",
    y="revenue",
    title="Tržby podle regionu"
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)

fig.update_yaxes(
    tickformat="~s"
)

fig.update_traces(
    texttemplate="%{y:.3s}",
    textposition="outside"
)

fig.show()

df = pd.DataFrame({
    "ad_spend": [10, 15, 20, 25, 30, 35],
    "revenue": [80, 110, 150, 170, 210, 250]
})

fig = px.scatter(
    df,
    x="ad_spend",
    y="revenue",
    title="Vztah nákladů a tržeb"
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)

fig.show()

import numpy as np
import plotly.express as px

trend = np.polyfit(
    df["ad_spend"],
    df["revenue"],
    1
)

trend_line = np.poly1d(trend)

fig = px.scatter(
    df,
    x="ad_spend",
    y="revenue",
    title="Vztah marketingových nákladů a tržeb"
)

fig.add_scatter(
    x=df["ad_spend"],
    y=trend_line(df["ad_spend"]),
    mode="lines",
    name="Trend"
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)

fig.show()

df = pd.DataFrame({
    "segment": ["B2B", "B2C", "Partner"],
    "revenue": [520000, 350000, 130000]
})

fig = px.pie(
    df,
    names="segment",
    values="revenue",
    title="Podíl tržeb podle segmentu"
)

fig.update_traces(
    textposition="inside",
    textinfo="label+percent+value"
)

fig.update_layout(
    title_font=dict(
        size=20
    )
)

fig.show()

df = pd.DataFrame({
    "month": ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05"],
    "B2B": [120, 135, 128, 150, 165],
    "B2C": [90, 95, 110, 108, 120],
    "Partner": [40, 45, 42, 50, 55]
})

df_long = df.melt(
    id_vars="month",
    var_name="segment",
    value_name="revenue"
)

fig = px.line(
    df_long,
    x="month",
    y="revenue",
    color="segment",
    markers=True,
    title="Vývoj tržeb podle segmentu"
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    title_font=dict(
        size=20
    )
)

fig.update_xaxes(
    type="category"
)

fig.show()