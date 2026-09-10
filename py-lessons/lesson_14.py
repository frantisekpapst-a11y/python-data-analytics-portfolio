import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "customer_name": [
        "  jan novák ",
        "PETRA MALÁ",
        " tomáš DVOŘÁK",
        "Eva Černá  "
    ],
    "email": [
        "jan@gmail.com",
        "petra@firma.cz",
        "tomas@gmail.com",
        "eva@firma.cz"
    ]
})

customers["customer_name"] = (
    customers["customer_name"]
    .str.strip()
    .str.title()
)

print(customers["customer_name"])

customers["email_lower"] = (
    customers["email"]
    .str.lower()
)

customers["name_upper"] = (
    customers["customer_name"]
    .str.upper()
)

print(customers)

gmail_customers = customers[
    customers["email"].str.contains("@gmail.com", na=False)
]

print(gmail_customers)

customers["email"] = (
    customers["email"]
    .str.replace(
        "@firma.cz",
        "@company.cz",
        regex=False
    )
)

print(customers)

customers[["email_name", "email_domain"]] = (
    customers["email"]
    .str.split("@", expand=True)
)

print(customers)

customers["email_length"] = (
    customers["email"]
    .str.len()
)
print(customers)

g_customers = customers[
    customers["email"].str.contains("@gmail.com")
]

print(g_customers[["customer_name", "email"]])

g_customers = customers[
    customers["email"].str.endswith("@gmail.com")
]

print(g_customers[["customer_name", "email"]])