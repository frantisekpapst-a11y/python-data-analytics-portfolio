file = open("employees.txt")

content = file.read()

print(content)

file.close()

with open("employees.txt") as file:
    content = file.read()
    print(content)

import os

print(os.getcwd())

with open("employees.txt") as file:
    content = file.read().splitlines()
    print(content)

print(type(content))

print(type(content[0]))

for name in content:
    print(name)

for name in content:
    if len(name) > 4:
        print(name)

count = 0

for name in content:
    if len(name) > 4:
        count = count + 1

print("Employees with long names:", count)

with open("employees.csv") as file:
    content = file.read()

print(content)

print(type(content))

import csv

with open("employees.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("employees.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[1])

with open("employees.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[2] != "salary":
            row[2] = int(row[2])
            print(row[2])

with open("employees.csv") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        row[2] = int(row[2])
        print(row[2])

with open("employees.csv") as file:
    reader = csv.reader(file)

    next(reader)

    salaries = []

    for row in reader:
        row[2] = int(row[2])
        salaries.append(row[2])

def average_salary(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    return(average_salary)

result = average_salary(salaries)

print("Average salary is:", result, "Kc")
     
with open("employees.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open("employees.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], type(row["name"]))
        print(row["salary"], type(row["salary"]))

high_salary_employees = []

with open("employees.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["salary"] = int(row["salary"])

        if row["salary"] > 60000:
            high_salary_employees.append(row)

print(high_salary_employees)

for employee in high_salary_employees:
    print(employee["name"])

for employee in high_salary_employees:
    print(employee["name"], "works in", employee["department"])

with open("high_salary_employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
    file,
    fieldnames=["name", "department", "salary"]
)
    writer.writeheader()

with open("high_salary_employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
    file,
    fieldnames=["name", "department", "salary"]
)
    writer.writeheader()
    writer.writerows(high_salary_employees)

high_salary_employees = []

with open("employees.csv") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        employee["salary"] = int(employee["salary"])

        if employee["salary"] > 60000:
            high_salary_employees.append(employee)

with open("high_salary_employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    writer.writerows(high_salary_employees)

import json

with open("employees.json") as file:
    employees = json.load(file)

print(type(employees))

print(employees)

for employee in employees:
    if employee["salary"] > 60000:
        high_salary_employees.append(employee)
        print(employee["name"], employee["salary"])

with open("high_salary_employees.json", "w") as file:
    json.dump(high_salary_employees, file, indent=4)