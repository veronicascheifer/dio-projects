from datetime import datetime

menu = """
[d] Deposit
[w] Withdraw
[e] Statement
[q] Quit

=>
"""

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
MAX_WITHDRAWALS = 3

while True:
    option = input(menu)

    if option == "d":
        amount = float(input("Enter the deposit amount: "))

        if amount > 0:
            balance += amount
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            statement += f"{date} - Deposit: $ {amount:.2f}\n"
        else:
            print("Invalid amount! Please try again.")

    elif option == "w":
        amount = float(input("Enter the withdrawal amount: "))

        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawals = withdrawal_count >= MAX_WITHDRAWALS

        if exceeded_balance:
            print("Insufficient balance.")
        elif exceeded_limit:
            print("The amount exceeds the withdrawal limit.")
        elif exceeded_withdrawals:
            print("You have exceeded the number of withdrawals.")
        elif amount > 0:
            balance -= amount
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            statement += f"{date} - Withdrawal: $ {amount:.2f}\n"
            withdrawal_count += 1
        else:
            print("Invalid amount! Please try again.")

    elif option == "e":
        print("\n=========== Statement ===========")
        if not statement:
            print("No transactions made.")
        else:
            print(statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("=================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select the desired operation again.")