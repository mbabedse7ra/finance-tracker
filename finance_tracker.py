from datetime import datetime
import csv
import os

class Transaction:
    def __init__(self, type, amount, category, description, date=None):
        if type not in ["income", "expense"]:
            raise ValueError("Type must be 'income' or 'expense'")
        self.type = type
        self.amount = float(amount)
        self.category = str(category)
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.description = description

    def display(self):
        return f"[{self.date}] {self.type} | {self.category} | {abs(self.amount)} | {self.description}"
    
person_1 = Transaction("income", 3200, "salary", "Monthly salary")
person_2 = Transaction("expense", 1200, "bank", "Monthly credit")

def save_transaction(t):
    file_exists = os.path.exists("transactions.csv")
    with open("transactions.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["type", "amount", "category", "date", "description"])  # header
        writer.writerow([t.type, t.amount, t.category, t.date, t.description])

save_transaction(person_1)
save_transaction(person_2)

def load_transaction():
    transactions = []
    try:
        with open("transactions.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                t = Transaction(row[0], row[1], row[2], row[4], date=row[3])
                transactions.append(t)
    except FileNotFoundError:
        pass
    return transactions

def show_transactions(transactions):
    print(f"{'Date':<12} {'Type':<10} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * 60)
    for t in transactions:
        print(f"{t.date:<12} {t.type:<10} {t.category:<15} {t.amount:<10} {t.description}")

show_transactions(load_transaction())

def get_balance(transactions):
    balance = sum([t.amount for t in transactions if t.type == "income"] ) - sum([t.amount for t in transactions if t.type == "expense"] )
    return balance

def get_summary(transactions):
    total_income = sum([t.amount for t in transactions if t.type == "income"] )
    total_expenses = sum([t.amount for t in transactions if t.type == "expense"] )
    balance = total_income - total_expenses
    return f"Total income: {total_income}\n Total expenses: {total_expenses}\n Balance: {balance}"

def get_by_category(transactions):
    categories = {}
    for t in transactions:
        if t.category not in categories:
            categories[t.category] = 0
        categories[t.category] += t.amount

    for category, total in categories.items():
        print(f"{category:<15}: {total}€")
    

transactions = load_transaction()
print(get_summary(transactions))
get_by_category(transactions)