salaries = [42000, 55500, 61000, 48000, 72500]
print(salaries)
print(type(salaries))
print(salaries[2])
print(salaries[4])
print(salaries[-3])
print(salaries[1:4])
print(salaries[:3])
print(salaries[2:])
print(len(salaries))
print(min(salaries))
print(max(salaries))
print(sum(salaries))
average_salary = sum(salaries) / len(salaries)
print(average_salary)
salaries.append(50000)
print(salaries)
print(len(salaries))
salaries.remove(50000)
salaries.pop(2)
print(salaries)
salaries.sort()
print(salaries)
salaries.sort(reverse = True)
print(salaries)
salaries.sort(reverse = False)
print(salaries)
salaries = [42000, 55500, 61000, 48000, 72500]
sorted_salaries = sorted(salaries)
print(salaries)
print(sorted_salaries)
for salary in salaries:
    print(salary)
for salary in salaries:
    if salary > 50000:
        print(salary)
high_salaries = []
for salary in salaries:
    if salary > 50000:
        high_salaries.append(salary)
print(high_salaries)
average_high_salary = sum(high_salaries) / len(high_salaries)
print(average_high_salary)
low_salaries = []
for salary in salaries:
    if salary <= 50000:
        low_salaries.append(salary)
print(low_salaries)
average_low_salary = sum(low_salaries) / len(low_salaries)
print(average_low_salary)
increased_salaries = []
for salary in salaries:
    new_salary = round(salary * 1.1, 2)
    increased_salaries.append(new_salary)
print(increased_salaries)
for number in range(5):
    print(number)
for number in range(2, 6):
    print(number)
for number in range(2, 10, 2):
    print(number)
for index, salary in enumerate(salaries):
    print(index, salary)

sales = [125000, 98000, 143000, 87000, 156000, 112000]
print(len(sales))
print(min(sales))
print(max(sales))
print(sum(sales))
average_sale = round(sum(sales) / len(sales), 2)
print(average_sale)
high_sales = []
for sale in sales:
    if sale > 120000:
        high_sales.append(sale)
print(high_sales)
average_high_sales = round(sum(high_sales) / len(high_sales), 2)
print(average_high_sales)