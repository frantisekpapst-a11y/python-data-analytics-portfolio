def welcome():
    print("Welcome to Data Analytics!")

welcome()

welcome()

def welcome(name):
    print("Welcome", name, "to Data Analytics!")

welcome("Petr")
welcome("Jana")

def employee_info(name, department):
    print("Employee:", name, "Department:", department)

employee_info("Petr", "Sales")
employee_info("Jana", "IT")

def salary_info(salary):
    print("Salary after increase:", round(salary*1.1, 2))

salary_info(50000)

def increase_salary(salary):
    new_salary = salary * 1.1
    return new_salary

result = increase_salary(50000)

print(result)

print("Salary with bonus:", round(result + 5000, 2))

def calculate_bonus(salary, bonus):
    final_salary = salary + bonus
    return final_salary

final_salary = calculate_bonus(65000, 7000)

print(final_salary)

def calculate_average(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    return average_salary

salaries = [50000, 65000, 48000, 72000, 58000]

average_salary = calculate_average(salaries)

print("Average salary:", average_salary, "Kc")

salaries = [50000, 65000, 48000, 72000, 58000]

def count_above_average(salaries):
    average_salary = round(sum(salaries) / len(salaries), 2)
    count = 0

    for salary in salaries:
        if salary > average_salary:
            count = count + 1

    return count

employees_above_average = count_above_average(salaries)

print("Employees above average:", employees_above_average)

def salary_level(salary):
    if salary > 50000:
        return "High salary"
    else:
        return "Low salary"

result = salary_level(65000)

print(result)

def salary_level(salary):
    if salary > 80000:
        return "Very high salary"
    elif salary > 60000:
        return "High salary"
    elif salary >= 40000:
        return "Standard salary"
    else:
        return "Low salary"

result = salary_level(45000)

print(result)

result = salary_level(92000)

print(result)

result = salary_level(21000)

print(result)

result = salary_level(60500)
    
print(result)

result = salary_level(40000)

print(result)

result = salary_level(60000)

print(result)

result = salary_level(80000)

print(result)

def calculate_tax(salary, tax_rate=0.15):
    gross_salary = salary + salary * tax_rate
    return gross_salary

result = calculate_tax(51000, 0.21)

print("Gross salary is:", result, "Kc")

def calculate_tax(salary, tax_rate=0.15):
    tax = round(salary * tax_rate, 2)
    return tax

result = calculate_tax(50000)

print(result)

result = calculate_tax(50000, 0.20)

print(result)

def net_salary(salary, tax_rate=0.15):
    tax = round(salary * tax_rate, 2)
    net = salary - tax
    return net

result = net_salary(50000)

print("Net salary:", result, "Kc")

result = net_salary(80000, 0.25)

print("Net salary:", result, "Kc")

def net_salary(salary, tax_rate=0.15):
    tax = calculate_tax(salary, tax_rate)
    net = salary - tax
    return net

result = net_salary(80000, 0.25)

print("Net salary:", result, "Kc")


def highest_salary(salaries):
    highest = max(salaries)
    return highest

highest_salary_result = highest_salary(salaries)

print("Highest salary:", highest_salary_result, "Kc")

def salary_summary(salaries):
    average = calculate_average(salaries)
    highest = highest_salary(salaries)
    print("Average:", average, "Kc", "/", "Highest:", highest, "Kc")

salary_summary(salaries)