import pandas as pd

df = pd.read_csv("ecommerce_sales_analysis.csv")

print(df.head())
print(df.shape)
print(df.columns)
df.info()

df_semicolon = pd.read_csv("sales.csv", sep=";")

df_pipe = pd.read_csv("sales.csv", sep="|")

df_utf8 = pd.read_csv("sales.csv")

df_utf8_explicit = pd.read_csv("sales.csv", encoding="utf-8")

df_cp1250 = pd.read_csv("sales.csv", encoding="cp1250")

df_czech = pd.read_csv("sales.csv", sep=";", encoding="cp1250")


import pandas as pd

df = pd.read_json("ecommerce_sales_analysis.json")

print(df.head())
print(df.shape)
print(df.columns)
df.info()

import pandas as pd

data = [
    {
        "order_id": 1001,
        "product": "Laptop",
        "customer": {
            "name": "Jan Novák",
            "city": "Plzeň"
        }
    },
    {
        "order_id": 1002,
        "product": "Monitor",
        "customer": {
            "name": "Petra Malá",
            "city": "Praha"
        }
    }
]

df_nested = pd.json_normalize(data)

print(df_nested)


import sqlite3

import pandas as pd

connection = sqlite3.connect("ecommerce_practice.db")

query = """
SELECT *
FROM orders
"""

df = pd.read_sql(query, connection)

connection.close()

print(df)
print(df.head())
print(df.shape)
print(df.columns)
df.info()


import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
df.info()