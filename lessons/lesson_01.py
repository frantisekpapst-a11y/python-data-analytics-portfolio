print("Ahoj, Pythone!")
print("Začínám s datovou analytikou v Pythonu")
name = "František"
job = "Data Analyst"
yrs_experience = 1
print(name)
print(job)
print(yrs_experience)
age = 45
salary = 55500.50
is_data_analyst = True
print(type(age))
print(type(salary))
print(type(is_data_analyst))
print(type(name))
age_text="45"
print(type(age_text))
age_number=int(age_text)
print(type(age_number))
salary = 55500.5
bonus = 4000
total_salary = salary + bonus
print(total_salary)
print(type(total_salary))
annual_salary = salary * 12
annual_bonus = bonus * 12
annual_income = annual_salary + annual_bonus
print(annual_salary)
print(annual_bonus)
print(annual_income)
bonus_percentage = annual_bonus / annual_income * 100
print(round(bonus_percentage, 2))
print(salary > 50000)
print(salary < 50000)
print(salary == 55500.5)
if salary > 50000:
    print("Saůary is above 50 000")
else:
    print("Salary is 50 000 or less")
salary = 40000
if salary > 50000:
    print("Saůary is above 50 000")
else:
    print("Salary is 50 000 or less")
