class Expense:
    def __init__(self, description, type, amount, date) -> None:
        self.description = description
        self.type = type
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"Expense: {self.description}, {self.type}, Rs.{self.amount}, {self.date}"