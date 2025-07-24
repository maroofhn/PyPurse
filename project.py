import os
from pyfiglet import Figlet

# Defining Storage for the Program
transactions = []

# Adding Income
def add_income(transactions, amount, category):
    transactions.append({"type": "income", "amount": amount, "category": category})
    print(f"Income of ${amount} added under {category}.")

# Adding Expenses
def add_expense(transactions, amount, category):
    transactions.append({"type": "expense", "amount": amount, "category": category})
    print(f"Expense of ${amount} added under {category}.")

# Showing the Summary, formatting display output
def display_summary(transactions):
    total_income = 0
    total_expenses = 0
    for t in transactions:
        if t["type"] == "income":
            total_income += t["amount"]
        elif t["type"] == "expense":
            total_expenses += t["amount"]

    balance = total_income - total_expenses
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

# For filtering transactions by specific category
def filter_by_category(transactions, category):
    filtered_transactions = [t for t in transactions if t["category"].lower() == category.lower()]
    return filtered_transactions

# MAIN USER PANEL
def display_user_panel(transactions):
    total_income = 0
    total_expenses = 0
    for t in transactions:
        if t["type"] == "income":
            total_income += t["amount"]
        elif t["type"] == "expense":
            total_expenses += t["amount"]

    balance = total_income - total_expenses
    print("\n---- User Panel ----")
    print(f"Balance: ${balance:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Total Income: ${total_income:.2f}")
    print("--------------------")

# def center_align_text(text):
#     terminal_width = os.get_terminal_size().columns
#     text_width = len(text)
#     padding = (terminal_width - text_width) // 2
#     return " " * padding + text

def main():
    fig = Figlet(font='slant')
    pypurse_text = fig.renderText('PyPurse')
    print(pypurse_text)

    print("\n" + " " * 10 + "[A] Add Income   [B] Add Expense   [C] View Summary   [D] View Transactions by Category   [E] User Panel   [F] Exit")

    while True:
        option = input("\nChoose an option: ").strip().upper()

        if option == "A":
            amount = float(input("Enter income amount: $"))
            category = input("Enter income category: ")
            add_income(transactions, amount, category)
        elif option == "B":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            add_expense(transactions, amount, category)
        elif option == "C":
            display_summary(transactions)
        elif option == "D":
            category = input("Enter category to filter by: ")
            filtered_transactions = filter_by_category(transactions, category)
            if filtered_transactions:
                for t in filtered_transactions:
                    print(f"{t['type'].capitalize()} - ${t['amount']} - {t['category']}")
            else:
                print("No transactions found for this category.")
        elif option == "E":
            display_user_panel(transactions)
        elif option == "F":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
