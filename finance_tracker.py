from datetime import datetime

class Transaction:
    def __init__(self, type, amount, category, description):
        if type not in ["income", "expense"]:
            raise ValueError("Type must be 'income' or 'expense'")
        self.type = type
        self.amount = float(amount)
        self.category = str(category)
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.description = description

    def display(self):
        return f"[{self.date}] {self.type} | {self.category} | {abs(self.amount)} | {self.description}"
    
person_1 = Transaction("income", 3200, "salery", "Monthly salery")
print(person_1.display())