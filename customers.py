## Reflection
# 1. I would use .get() when a key might not exist because it lets the program
# return a default value instead of crashing. I would use bracket notation when
# I know the key exists and need its value. My rule of thumb is to use .get()
# for optional information and brackets for information I expect to be there.

# 2. Exercise 8 reminds me of organizing sales numbers in an Excel spreadsheet
# and adding them together based on their region. Python is more useful for
# large datasets because it can process a lot of information quickly and
# automatically update totals without manually doing the calculations.


## Exercise 1
customer = {
    "name": "John Smith",
    "email": "johnsmith@email.com",
    "tier": "Gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


## Exercise 2
customer["phone"] = "401-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


## Exercise 3
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


## Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")
for key in customer:
    print(key)


## Exercise 5
tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print("Tier:", tier)
print("Discount rate:", discount * 100, "%")
print("Final price: $", final_price)


## Exercise 6
dict1 = {"name": "Alice", "tier": "platinum"}
dict2 = {"name": "Bob", "tier": "gold"}
dict3 = {"name": "Sarah", "tier": "silver"}
customers = [dict1, dict2, dict3]
for customer in customers:
    name = customer["name"]
    tier = customer["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{name}: {tier} tier - ${discount_amount:.2f} discount")


## Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left!")


## Exercise 8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
sales_summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")  