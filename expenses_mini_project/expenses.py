from datetime import datetime

FILE_NAME = "expenses.txt"

class Expense:
    def __init__(self, date, category, amount, note):
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_line(self):
        return f"{self.date},{self.category},{self.amount},{self.note}\n"


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (Food, Travel, Rent etc.): ")
    amount = float(input("Enter Amount: "))
    note = input("Enter Note: ")

    exp = Expense(date, category, amount, note)

    f = open(FILE_NAME, "a")
    f.write(exp.to_line())
    f.close()

    print("Expense Added Successfully\n")


def view_expenses():
    try:
        f = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("No expenses found\n")
        return

    total = 0
    print("\n--- All Expenses ---")
    for line in f:
        date, category, amount, note = line.strip().split(",")
        amount = float(amount)
        total += amount
        print(f"{date} | {category} | ₹{amount} | {note}")

    f.close()
    print(f"\nTotal Expense: ₹{total}\n")


def category_wise_expense():
    category_search = input("Enter Category to search: ")

    try:
        f = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("No data available\n")
        return

    total = 0
    print(f"\n--- Expenses for {category_search} ---")
    for line in f:
        date, category, amount, note = line.strip().split(",")
        amount = float(amount)
        if category.lower() == category_search.lower():
            total += amount
            print(f"{date} | ₹{amount} | {note}")

    f.close()
    print(f"Total for {category_search}: ₹{total}\n")


def filter_high_expense():
    limit = float(input("Show expenses greater than: "))

    try:
        f = open(FILE_NAME, "r")
    except FileNotFoundError:
        print("No data available\n")
        return

    print("\n--- High Expenses ---")
    for line in f:
        date, category, amount, note = line.strip().split(",")
        amount = float(amount)
        if amount > limit:
            print(f"{date} | {category} | ₹{amount} | {note}")

    f.close()
    print()


def delete_all_expenses():
    confirm = input("Are you sure you want to delete all expenses? (yes/no): ")
    if confirm.lower() == "yes":
        f = open(FILE_NAME, "w")
        f.close()
        print("All expenses deleted\n")
    else:
        print("Operation cancelled\n")


# ================= MAIN MENU =================

while True:
    print("====== Personal Expense Tracker ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Wise Expense")
    print("4. Filter High Expense")
    print("5. Delete All Expenses")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_wise_expense()
    elif choice == "4":
        filter_high_expense()
    elif choice == "5":
        delete_all_expenses()
    elif choice == "6":
        print("Exiting Expense Tracker")
        break
    else:
        print("Invalid Choice\n")
