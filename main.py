print("===== PERSONAL EXPENSE TRACKER =====")
income = float(input("Enter your monthly income: "))
expenses = []
while True:
    category = input("Enter expense category (or 'done' to finish): ")

    if category.lower() == "done":
        break

    amount = float(input("Enter expense amount: "))

    expenses.append({
        "category": category,
        "amount": amount
    })
    total_expense = sum(item["amount"] for item in expenses)
balance = income - total_expense

print("\n===== EXPENSE SUMMARY =====")
print("Monthly Income:", income)
print("Total Expenses:", total_expense)
print("Remaining Balance:", balance)
print("\n===== EXPENSE DETAILS =====")

for item in expenses:
    print(item["category"], ":", item["amount"])


with open("expenses.txt", "w") as file:
    file.write("PERSONAL EXPENSE TRACKER\n")
    file.write(f"Income: {income}\n")

    for item in expenses:
        file.write(f"{item['category']}: {item['amount']}\n")

    file.write(f"Total Expenses: {total_expense}\n")
    file.write(f"Balance: {balance}\n")

with open("expenses.txt", "r") as file:
    saved_data = file.read()

print(saved_data)
category_totals = {}

for item in expenses:
    category = item["category"]
    amount = item["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("\n===== CATEGORY TOTALS =====")

for category, total in category_totals.items():
    print(category, ":", total)
for category, total in category_totals.items():
    print(category, ":", total)
print("\n===== DELETE EXPENSE =====")

if expenses:
    for index, item in enumerate(expenses, start=1):
        print(index, item["category"], ":", item["amount"])

    choice = int(input("Enter expense number to delete: "))

    if 1 <= choice <= len(expenses):
        deleted = expenses.pop(choice - 1)
        print("Deleted:", deleted["category"], deleted["amount"])
    else:
        print("Invalid expense number.")
else:
    print("No expenses to delete.")
    total_expense = sum(item["amount"] for item in expenses)
balance = income - total_expense

with open("expenses.txt", "w") as file:
    file.write("PERSONAL EXPENSE TRACKER\n")
    file.write(f"Income: {income}\n")

    for item in expenses:
        file.write(f"{item['category']}: {item['amount']}\n")

    file.write(f"Total Expenses: {total_expense}\n")
    file.write(f"Balance: {balance}\n")

print("Expense file updated successfully!")
