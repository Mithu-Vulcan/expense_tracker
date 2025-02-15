from expense import Expense
from income import Income
from datetime import date
from os import system, name

def main():

    account_file = "Accounts.csv"
    types_of_expenses = ["Tution", "Food", "Fuel"]
    types_of_incomes = ["Amma"]

    def clear():

        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def welcome():
        print("Advanced daily expenses and budget tracker")
        try:
            with open(account_file, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("No past records found...")
            print("Creating new expenses.csv")
            f = open(account_file, "x")
        total_summary()
        input("Press enter to continue....")
        clear()
        summary_and_confirmation()

    def get_user_input():

        while True:
            expense_or_income = input("Expense(1), Income(2) :")
            if int(expense_or_income) == 2:
                print("Select the income type")
                for i, type_of_income in enumerate(types_of_incomes):
                    print(f"    {i+1}: {type_of_income}")
                value_range = f"1 - {len(types_of_incomes)}"
                type_of_income_index = int(input(f"select between{value_range} :")) - 1
                while True:
                    if type_of_income_index in range(len(types_of_incomes)):
                        selected_type = types_of_incomes[type_of_income_index]
                        description = input("Describe :")
                        today = date.today()
                        amount = input("Input the amount :")
                        new_income = Income(type=selected_type,description=description,date=today, amount = amount)
                        return new_income
                    else:
                        print("Invalid Option Try again")
                
                

            elif int(expense_or_income) == 1:
                print("Select the expense type")
                for i, type_of_expense in enumerate(types_of_expenses):
                    print(f"    {i+1}: {type_of_expense}")
                value_range = f"1 - {len(types_of_expenses)}"
                type_of_expense_index = int(input(f"select between{value_range} :")) - 1
                while True:
                    if type_of_expense_index in range(len(types_of_expenses)):
                        selected_type = types_of_expenses[type_of_expense_index]
                        description = input("Describe :")
                        today = date.today()
                        amount = input("Ïnput the amount :")
                        amount = int(f"-{amount}")
                        new_expense = Expense(type=selected_type,description=description,date=today, amount = amount)
                        return new_expense

                    else:
                        print("Invalid Option Try again")
            else:
                print("Invalid option please try again..")

    def summary_and_confirmation():
        summary = str(get_user_input())
        summary_stripped = summary.strip()
        category_and_description,type, amount, date= summary_stripped.split(",")
        clear()
        print("Summary of the event :")
        print(f"    Description: {category_and_description}\n    type: {type}\n    amount: {amount}\n    date: {date}")
        print("")
        print("Press enter to continue... or to cancel the event press ctrl+c...")
        input()
        print(f"writing to the csv file ({account_file})")
        category, description = category_and_description.split(":")
        date = date.strip()
        category = category.strip()
        type = type.strip()
        description = description.strip()
        amount = amount.strip()
        with open(account_file, "a") as f:
            f.write(f"{date},{category},{type},{description},{amount}\n")
            f.close()
        total_summary()

    def total_summary():
        dictionary = {}
        print("Here is a overall summary")
        with open(account_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                line_stripped = line.strip()
                d_date, category, t_type, description, amount = line_stripped.split(",")
                ruppee, amount1 = amount.split(".")
                if t_type in dictionary:
                    old_amount = dictionary[f"{t_type}"]
                    try:
                        new_amount = int(old_amount) + int(amount1)
                    except(TypeError):
                        old_amount = old_amount.pop()
                        new_amount = int(old_amount) + int(amount1)
                    dictionary.update({f"{t_type}": {new_amount}})
                else:
                    dictionary[f"{t_type}"] = int(amount1)

        print("")
        for e in types_of_expenses:
            try:
                total_summary_amount = int(dictionary[f"{e}"])
            except(TypeError):
                total_summary_amount = dictionary[f"{e}"]
                total_summary_amount = int(total_summary_amount.pop())
            print(f"{e}: {total_summary_amount}")
        for i in types_of_incomes:
            try:
                total_summary_amount = int(dictionary[f"{i}"])
            except(TypeError):
                total_summary_amount = dictionary[f"{i}"]
                total_summary_amount = int(total_summary_amount.pop())
            print(f"{i}: {total_summary_amount}")

    welcome()


if __name__ == "__main__":
    main()