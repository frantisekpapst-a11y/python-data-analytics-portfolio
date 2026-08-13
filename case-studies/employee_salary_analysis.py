employees = [
    {"name": "Petr", "department": "Sales", "salary": 50000},
    {"name": "Jana", "department": "IT", "salary": 65000},
    {"name": "Martin", "department": "Sales", "salary": 48000},
    {"name": "Eva", "department": "IT", "salary": 72000},
    {"name": "Lucie", "department": "Finance", "salary": 58000},
    {"name": "David", "department": "Finance", "salary": 61000},
    {"name": "Tomas", "department": "Sales", "salary": 54000},
    {"name": "Anna", "department": "HR", "salary": 47000}
]

print("--- Business Summary ---")

print("")

print("Number of employees:", len(employees))

salaries = []
for employee in employees:
    salaries.append(employee["salary"])
print("Average salary:", round(sum(salaries) / len(salaries), 2), "Kc")

for employee in employees:
    if employee["salary"] == max(salaries):
        print("Highest salary:", employee["name"], employee["salary"], "Kc")

print("Employees above average salary:")
for employee in employees:
    if employee["salary"] > sum(salaries) / len(salaries):
        print(employee["name"], employee["salary"], "Kc")

salaries_above_average = []
for employee in employees:
    if employee["salary"] > sum(salaries) / len(salaries):
        salaries_above_average.append(employee["salary"])
print("Number of employees above average:", len(salaries_above_average))

for employee in employees:
    if employee["salary"] == min(salaries):
        print("Lowest salary:", employee["name"], employee["salary"], "Kc")

salaries_sales = []
for employee in employees:
    if employee["department"] == "Sales":
        salaries_sales.append(employee["salary"])
print("Number of Sales employees:", len(salaries_sales))

print("Average Sales salary:", round(sum(salaries_sales) / len(salaries_sales), 2), "Kc")

salaries_it = []
for employee in employees:
    if employee["department"] == "IT":
        salaries_it.append(employee["salary"])
print("Average IT salary:", round(sum(salaries_it) / len(salaries_it), 2), "Kc")
if sum(salaries_sales) / len(salaries_sales) > sum(salaries_it) / len(salaries_it):
    print("Sales has higher average salary")
else:
    print("IT has higher average salary")

print(
    "Percentage of Sales employees:",
      round(len(salaries_sales) / len(employees) * 100, 1),
      "%"
)

print(
    "Salary IT vs Sales difference:",
    round(sum(salaries_it) / len(salaries_it) - sum(salaries_sales) / len(salaries_sales), 2),
    "Kc"
)

salaries_finance = []

for employee in employees:
    if employee["department"] == "Finance":
        salaries_finance.append(employee["salary"])

salaries_hr = []

for employee in employees:
    if employee["department"] == "HR":
        salaries_hr.append(employee["salary"])

salaries_average = [sum(salaries_sales) / len(salaries_sales), sum(salaries_it) / len(salaries_it), sum(salaries_finance) / len(salaries_finance), sum(salaries_hr) / len(salaries_hr)]

if sum(salaries_it) / len(salaries_it) == max(salaries_average):
    print("Highest average salary department:", "IT", round(max(salaries_average), 2), "Kc")