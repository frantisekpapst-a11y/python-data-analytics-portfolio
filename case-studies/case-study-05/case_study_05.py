import pandas as pd

support_tickets_raw = pd.read_json("data/case_study_support_tickets.json")

print(support_tickets_raw.head())

support_tickets_raw.info()

print(support_tickets_raw.shape)

print(support_tickets_raw[support_tickets_raw.duplicated()])

support_tickets_raw = support_tickets_raw.drop_duplicates()

print(support_tickets_raw.shape)

support_tickets_raw.info()

print(support_tickets_raw["department"].unique())
print(support_tickets_raw["channel"].unique())
print(support_tickets_raw["priority"].unique())
print(support_tickets_raw["issue_type"].unique())
print(support_tickets_raw["agent_name"].unique())
print(support_tickets_raw["customer_segment"].unique())

support_tickets_raw["department"] = (
    support_tickets_raw["department"]
    .str.strip()
    .str.title()
)

support_tickets_raw["channel"] = (
    support_tickets_raw["channel"]
    .str.strip()
    .str.title()
)

support_tickets_raw["priority"] = (
    support_tickets_raw["priority"]
    .str.strip()
    .str.title()
)

support_tickets_raw["issue_type"] = (
    support_tickets_raw["issue_type"]
    .str.strip()
    .str.title()
)

support_tickets_raw["agent_name"] = (
    support_tickets_raw["agent_name"]
    .str.strip()
    .str.title()
)

support_tickets_raw["customer_segment"] = (
    support_tickets_raw["customer_segment"]
    .str.strip()
    .str.title()
)

print(support_tickets_raw["department"].unique())
print(support_tickets_raw["channel"].unique())
print(support_tickets_raw["priority"].unique())
print(support_tickets_raw["issue_type"].unique())
print(support_tickets_raw["agent_name"].unique())
print(support_tickets_raw["customer_segment"].unique())

print(support_tickets_raw.isna().sum())

support_tickets_raw["agent_name"] = (
    support_tickets_raw["agent_name"]
    .fillna("Unknown")
)

support_tickets_raw["satisfaction_score"] = (
    support_tickets_raw["satisfaction_score"]
    .fillna(
        support_tickets_raw["satisfaction_score"].median()
    )
)

print(support_tickets_raw.isna().sum())

support_tickets_clean = support_tickets_raw.copy()

support_tickets_clean.to_json(
    "case_study_support_tickets_clean",
    orient="records",
    indent=4,
    date_format="iso")

print(support_tickets_clean[["resolution_hours", "satisfaction_score"]]
      .agg([
          "min",
          "max",
          "mean",
          "median"
      ])
)

print("Je možný také tento zápis...")
print(
    support_tickets_clean[
        ["resolution_hours", "satisfaction_score"]
    ].describe()
)

q1_res_hours = support_tickets_clean["resolution_hours"].quantile(0.25)
q3_res_hours = support_tickets_clean["resolution_hours"].quantile(0.75)

iqr_res_hours = q3_res_hours - q1_res_hours

lower_bound_res_hours = q1_res_hours - 1.5 * iqr_res_hours
upper_bound_res_hours = q3_res_hours + 1.5 * iqr_res_hours

print(q1_res_hours, q3_res_hours, iqr_res_hours, lower_bound_res_hours, upper_bound_res_hours)

outliers_res_hours = support_tickets_clean[
    (support_tickets_clean["resolution_hours"] < lower_bound_res_hours)
    | (support_tickets_clean["resolution_hours"] > upper_bound_res_hours)
]
print(outliers_res_hours)

q1_stf_score = support_tickets_clean["satisfaction_score"].quantile(0.25)
q3_stf_score = support_tickets_clean["satisfaction_score"].quantile(0.75)

iqr_stf_score = q3_stf_score - q1_stf_score

lower_bound_stf_score = q1_stf_score - 1.5 * iqr_stf_score
upper_bound_stf_score = q3_stf_score + 1.5 * iqr_stf_score

print(q1_stf_score, q3_stf_score, iqr_stf_score, lower_bound_stf_score, upper_bound_stf_score)

outliers_stf_score = support_tickets_clean[
    (support_tickets_clean["satisfaction_score"] < lower_bound_stf_score)
    | (support_tickets_clean["satisfaction_score"] > upper_bound_stf_score)
]
print(outliers_stf_score)

print(support_tickets_clean["department"].value_counts())
print(support_tickets_clean["channel"].value_counts())
print(support_tickets_clean["priority"].value_counts())
print(support_tickets_clean["customer_segment"].value_counts())

print(support_tickets_clean["issue_type"].value_counts())
print(support_tickets_clean["reopened"].value_counts())

support_tickets_clean["created_month"] = (
    support_tickets_clean["created_at"]
    .dt.strftime("%Y-%m")
)

tickets_month = (
    support_tickets_clean.groupby(
        "created_month",
        as_index=False
    )["ticket_id"]
    .count()
)

print(tickets_month)

print(
    support_tickets_clean[
        ["resolution_hours", "satisfaction_score"]
    ].corr()
)

from scipy.stats import pearsonr

r, p_value = pearsonr(
    support_tickets_clean["resolution_hours"],
    support_tickets_clean["satisfaction_score"]
)

print("r:", r)
print("p-value:", p_value)

import matplotlib.pyplot as plt

support_tickets_clean["resolution_hours"].hist(bins="auto")

plt.show()

support_tickets_clean["satisfaction_score"].hist(bins="auto")

plt.show()

priority_summary = (
    support_tickets_clean.groupby(
        "priority",
        as_index=False
    )
    .agg(
        avg_resolution=("resolution_hours", "mean"),
        median_resolution=("resolution_hours", "median"),
        tickets_count=("ticket_id", "count")
    )
)

print(priority_summary)

high = support_tickets_clean.loc[
    support_tickets_clean["priority"] == "High",
    "resolution_hours"
]

medium = support_tickets_clean.loc[
    support_tickets_clean["priority"] == "Medium",
    "resolution_hours"
]

low = support_tickets_clean.loc[
    support_tickets_clean["priority"] == "Low",
    "resolution_hours"
]

from scipy.stats import f_oneway

f_stat, p_value = f_oneway(
    high,
    medium,
    low
)

print("F-statistic:", f_stat)
print("p-value:", p_value)

channel_summary = (
    support_tickets_clean.groupby(
        "channel",
        as_index=False
    )
    .agg(
        avg_resolution=("resolution_hours", "mean"),
        median_resolution=("resolution_hours", "median"),
        tickets_count=("ticket_id", "count")
    )
)

print(channel_summary)

chat = support_tickets_clean.loc[
    support_tickets_clean["channel"] == "Chat",
    "resolution_hours"
]

email = support_tickets_clean.loc[
    support_tickets_clean["channel"] == "Email",
    "resolution_hours"
]

phone = support_tickets_clean.loc[
    support_tickets_clean["channel"] == "Phone",
    "resolution_hours"
]

f_stat, p_value = f_oneway(
    chat,
    email,
    phone
)

print("F-statistic:", f_stat)
print("p-value:", p_value)

department_summary = (
    support_tickets_clean.groupby(
        "department",
        as_index=False
    )
    .agg(
        avg_resolution=("resolution_hours", "mean"),
        median_resolution=("resolution_hours", "median"),
        tickets_count=("ticket_id", "count")
    )
)

print(department_summary)

account = support_tickets_clean.loc[
    support_tickets_clean["department"] == "Account",
    "resolution_hours"
]

billing = support_tickets_clean.loc[
    support_tickets_clean["department"] == "Billing",
    "resolution_hours"
]

technical = support_tickets_clean.loc[
    support_tickets_clean["department"] == "Technical",
    "resolution_hours"
]

from scipy.stats import f_oneway

f_stat, p_value = f_oneway(
    account,
    billing,
    technical
)

print("F-statistic:", f_stat)
print("p-value:", p_value)

print("""
========================================================================================
BUSINESS SUMMARY
========================================================================================

1. Dataset po vyčištění obsahuje 49 unikátních ticketů.

2. Resolution time má right-skewed distribuci.
   Většina ticketů se řeší výrazně rychleji, ale několik delších případů táhne průměr nahoru.

3. Satisfaction score má naopak left-skewed distribuci.
   Většina zákazníků je spokojená, ale několik velmi nízkých hodnocení snižuje průměr.

4. Ticket T041 je výrazný outlier:
   - resolution_hours = 52
   - satisfaction_score = 1.0

   Jde spíše o reálný problematický případ než o chybu v datech, proto nebyl odstraněn.

5. Mezi resolution_hours a satisfaction_score je velmi silná negativní korelace:

   r ≈ -0.97

   Delší doba řešení tedy souvisí s nižší spokojeností zákazníka.

   Korelace je statisticky významná, ale sama o sobě neprokazuje kauzalitu.

6. Priority má významný vztah k resolution time.

   High priority tickety se řeší nejrychleji, Low priority nejpomaleji.

   ANOVA:
   p-value < 0.05

   Rozdíly mezi prioritami jsou tedy statisticky významné.

7. Také komunikační kanál souvisí s délkou řešení.

   Phone vychází jako nejrychlejší, email jako nejpomalejší.

   ANOVA:
   p-value < 0.05

   Rozdíl mezi kanály je statisticky významný.

8. Mezi odděleními jsou viditelné rozdíly, Account je rychlejší a Billing pomaleji.

   ANOVA ale vyšla:

   p-value ≈ 0.075

   Rozdíl mezi odděleními tedy nebyl při hranici 0.05 statisticky potvrzen.

9. Z 49 ticketů byly pouze 4 znovu otevřeny,tedy přibližně 8 %.


HLAVNÍ BUSINESS ZÁVĚR:

Nejvýraznější faktor spojený se spokojeností zákazníka je délka řešení ticketu.

Priorita i komunikační kanál mají významný vztah k rychlosti vyřešení.

Pro další analýzu by dávalo smysl sledovat, zda změna procesu podpory dokáže zkrátit dobu řešení a současně zvýšit spokojenost zákazníků.
""")