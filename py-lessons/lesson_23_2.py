import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.0755,
    "longitude": 14.4378,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params, timeout=10)

print(response.status_code)
print(response.url)

data = response.json()

print(data.keys())

print(data["hourly"].keys())

import pandas as pd

df_weather = pd.DataFrame(data["hourly"])

df_weather["time"] = pd.to_datetime(df_weather["time"])

today = pd.Timestamp.today().date()

df_today = df_weather[
    df_weather["time"].dt.date == today
]

print(df_today)

print(df_today["temperature_2m"].describe())

print(
    df_today.loc[
        df_today["temperature_2m"].idxmax()
    ]
)

import matplotlib.pyplot as plt

average_temp = df_today["temperature_2m"].mean()

df_today.plot(
    x="time",
    y="temperature_2m",
    kind="line",
    legend=False,
    title="Dnešní hodinová teplota"
)

plt.axhline(
    y=average_temp,
    linestyle="--",
    label=f"Průměr: {average_temp:.1f} °C"
)

plt.xlabel("Čas")
plt.ylabel("Teplota °C")
plt.legend()
plt.show()

params = {
    "latitude": 50.0755,
    "longitude": 14.4378,
    "hourly": [
        "temperature_2m",
        "precipitation",
        "wind_speed_10m"
    ]
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

df_weather = pd.DataFrame(data["hourly"])
df_weather["time"] = pd.to_datetime(df_weather["time"])

today = pd.Timestamp.today().date()

df_today = df_weather[
    df_weather["time"].dt.date == today
]

print(df_today.head())
print(df_today.info())


print(df_today["precipitation"].sum())
print(df_today["wind_speed_10m"].max())

df_today.to_csv("weather_today.csv", index=False)