import csv

total_revenue = 0

order_count = 0

orders = []

above_average_orders = []

with open("ecommerce_sales_analysis.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["unit_price"] = int(row["unit_price"])
        row["total"] = row["quantity"] * row["unit_price"]
        total_revenue = total_revenue + row["total"]
        order_count = order_count + 1
        orders.append(row)
        
def calculate_average_order(total_revenue, order_count):
    average_order = round(total_revenue / order_count, 2)
    return average_order

average_order = calculate_average_order(total_revenue, order_count)

for order in orders:
    if order["total"] > average_order:
        above_average_orders.append(order)

def find_largest_order(orders):
    largest_order = orders[0]

    for order in orders:
        if order["total"] > largest_order["total"]:
            largest_order = order

    return largest_order

largest_order = find_largest_order(orders)

def find_lowest_order(orders):
    lowest_order = orders[0]

    for order in orders:
        if order["total"] < lowest_order["total"]:
            lowest_order = order

    return lowest_order

lowest_order = find_lowest_order(orders)

with open("above_average_orders.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["order_id", "product", "category", "quantity", "unit_price", "customer", "total"])
    writer.writeheader()
    writer.writerows(above_average_orders)
 
print("BUSINESS SUMMARY:")

print("Celkové tržby:", total_revenue, "Kc")

print("Průměrná objednávka:", average_order, "Kc")

print("Počet objednávek nad průměrem:", len(above_average_orders))

print("Objednávky vyšší než průměrná objednávka:")

for order in above_average_orders:
    print("- ", order["order_id"], order["product"], order["total"])

print("Největší objednávka:")

print("- ", largest_order["order_id"], largest_order["product"], largest_order["total"])

print("Nejnižší objednávka:")

print("- ", lowest_order["order_id"], lowest_order["product"], lowest_order["total"])
