import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)

print(response.headers["Content-Type"])

data = response.json()

print(type(data))

print(data[0])

print(data[0]["name"])

import pandas as pd

df = pd.DataFrame(data)

print(df.loc[0, "name"])

print(df.head())

df = pd.json_normalize(data)

print(df.head())

print(df.loc[0, ["name", "email", "address.city", "company.name"]])

print(df[["name", "email", "address.city", "company.name"]])

df.info()

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print(response.url)

params = {
    "userId": 3
}

response = requests.get(url, params=params)

print(response.url)

print(len(response.json()))

print(response.json())

df_posts = pd.DataFrame(response.json())

print(df_posts)

params = [
    ("userId", 1),
    ("userId", 2)
]

response_1 = requests.get(url, params={"userId": 1})
response_2 = requests.get(url, params={"userId": 2})

df_1 = pd.DataFrame(response_1.json())
df_2 = pd.DataFrame(response_2.json())

df_posts = pd.concat([df_1, df_2], ignore_index=True)

print(df_posts)

headers = {
    "Accept": "application/json"
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

print(response.status_code)
print(response.request.headers)

headers = {
    "X-API-Key": "MOJE_API_KEY"
}

response = requests.get(
    url,
    headers=headers
)

headers = {
    "Authorization": "Bearer MUJ_TOKEN"
}

response = requests.get(
    url,
    headers=headers
)

import requests

url = "https://jsonplaceholder.typicode.com/neexistuje"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Request proběhl úspěšně.")

except requests.exceptions.RequestException as error:
    print("Chyba při komunikaci s API:", error)

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "_page": 1,
    "_limit": 5
}

response_1 = requests.get(url, params=params)

print(response_1.url)
print(len(response_1.json()))

params_2 = {
    "_page": 2,
    "_limit": 5
}

response_2 = requests.get(url, params=params_2)

print(response_2.url)
print(len(response_2.json()))

df_1 = pd.DataFrame(response_1.json())
df_2 = pd.DataFrame(response_2.json())

df_all = pd.concat([df_1, df_2], ignore_index=True)

print(df_all)

all_posts = []

for page in range(1, 3):
    params = {
        "_page": page,
        "_limit": 5
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    all_posts.extend(data)

df_all = pd.DataFrame(all_posts)

print(df_all)

all_posts = []
page = 1

while True:
    params = {
        "_page": page,
        "_limit": 5
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        break

    all_posts.extend(data)

    page += 1

df_all = pd.DataFrame(all_posts)

print(df_all)

print(df_all.shape)
print(df_all.info())

print(df_all.isna().sum())
print(df_all.duplicated().sum())

print(df_all["id"].nunique())
print(df_all["id"].duplicated().sum())

print(df_all["userId"].nunique())

summary_userid = (
    df_all.groupby(
        "userId",
        as_index=False
    )
    .size()
)

print(summary_userid)

summary_userid = (
    df_all.groupby("userId", as_index=False)
    .size()
    .rename(columns={"size": "post_count"})
)

print(summary_userid)

summary_userid = summary_userid.sort_values(
    by="post_count",
    ascending=False
)

print(summary_userid)

print(summary_userid["post_count"].describe())

summary_userid.plot(
    x="userId",
    y="post_count",
    kind="bar",
    legend=False,
    title="Počet příspěvků podle uživatele"
)

import matplotlib.pyplot as plt

plt.xlabel("User ID")
plt.ylabel("Počet příspěvků")
plt.show()

summary_userid.to_csv(
    "api_posts_summary.csv",
    index=False
)