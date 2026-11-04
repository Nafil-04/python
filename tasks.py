# ---calculator---

# n1=float(input("Enter First Number: "))
# operator=input("Enter Operator : (+,-,/,*)")
# n2=float(input("Enter Second Number: "))

# if operator == "+":
#     print(n1+n2)
# elif operator == "-":
#     print(n1-n2)
# elif operator == "*":
#     print(n1*n2)
# elif operator == "/":
#     print(n1/n2)
# else:
#     print("Invalid Operator")

# ---personal expense tracker---

import json

expenses = []


def menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Show Total Spent")
    print("5. Exit")


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n---- All Expenses ----")

    if not expenses:
        print("No expenses found!")
        return

    print(f"{'Amount':<12}{'Category':<18}{'Date'}")
    print("-" * 40)

    for expense in expenses:
        print(f"{expense['amount']:<12}{expense['category']:<18}{expense['date']}")


def search_expenses():
    choice = input("Search by category or date? (c/d): ").lower()

    if choice == "c":
        search = input("Enter category: ")

        results = [
            e for e in expenses
            if e["category"].lower() == search.lower()
        ]

    elif choice == "d":
        search = input("Enter date (YYYY-MM-DD): ")

        results = [
            e for e in expenses
            if e["date"] == search
        ]

    else:
        print("Invalid choice!")
        return

    print("\n---- Search Results ----")

    if not results:
        print("No matching expenses found!")
        return

    print(f"{'Amount':<12}{'Category':<18}{'Date'}")
    print("-" * 40)

    for expense in results:
        print(f"{expense['amount']:<12}{expense['category']:<18}{expense['date']}")


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spent: {total}")


def save_expenses():
    with open("expenses.txt", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Data saved to expenses.txt")


def load_expenses():
    global expenses

    try:
        with open("expenses.txt", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        expenses = []
        print("no valid saved data found.starting fresh.")



load_expenses()

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expenses()

    elif choice == "4":
        show_total()

    elif choice == "5":
        save_expenses()
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")