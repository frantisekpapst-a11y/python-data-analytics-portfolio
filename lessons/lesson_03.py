employee = {
    "name": "Petr",
    "department": "Sales",
    "salary": 45000,
    "active": True
}

print(employee)
print(type(employee))

print(employee["name"])
print(employee["salary"])
print(employee["department"])

print(type(employee["salary"]))

employee["salary"] = 50000
print(employee)

employee["city"] = "Prague"
print(employee)

employee.pop("city")
print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(key, value)

employees = [
    {"name": "Petr", "department": "Sales", "salary": 50000},
    {"name": "Jana", "department": "IT", "salary": 65000},
    {"name": "Martin", "department": "Sales", "salary": 48000},
    {"name": "Eva", "department": "IT", "salary": 72000}
]

print(employees)

print(employees[1])

print(employees[1]["salary"])

for employee in employees:
    print(employee["name"])

for employee in employees:
    if employee["department"] == "IT":
        print(employee["name"])

for employee in employees:
    if employee["salary"] > 50000:
        print(employee["name"], employee["salary"])

high_paid_employees = []
for employee in employees:
    if employee["salary"] > 50000:
        high_paid_employees.append(employee)
for employee in high_paid_employees:
    print(employee["name"], employee["department"], employee["salary"])