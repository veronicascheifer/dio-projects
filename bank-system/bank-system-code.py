from datetime import datetime
import textwrap

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
MAX_WITHDRAWALS = 3
users = []
accounts = []

def menu():
    menu = """
    [d] Deposit
    [w] Withdraw
    [e] Statement
    [na] New Account
    [la] List Accounts
    [nu] New User
    [q] Quit

    =>
    """
    return input(textwrap.dedent(menu))

def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        statement += f"{date} - Deposit: $ {value:.2f}\n"
    else:
        print("Invalid amount! Please try again.")
    
    return balance, statement

def withdraw(*, balance, value, statement, limit, withdrawal_count, limit_withdrawals):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = withdrawal_count >= limit_withdrawals

    if exceeded_balance:
        print("Insufficient balance.")
    elif exceeded_limit:
        print("The amount exceeds the withdrawal limit.")
    elif exceeded_withdrawals:
        print("You have exceeded the number of withdrawals.")
    elif value > 0:
        balance -= value
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        statement += f"{date} - Withdrawal: $ {value:.2f}\n"
        withdrawal_count += 1
    else:
        print("Invalid amount! Please try again.")
    
    return balance, statement, withdrawal_count

def show_statement(balance, /, *, statement):
    print("\n=========== Statement ===========")
    if not statement:
        print("No transactions made.")
    else:
        print(statement)
    print(f"\nBalance: $ {balance:.2f}")
    print("=================================")

def create_user(users):
    cpf = input("Enter CPF (only numbers): ")
    user = filter_user(cpf, users)
    
    if user:
        print("User already registered.")
        return
    
    name = input("Enter full name: ")
    birth_date = input("Enter birth date (dd-mm-yyyy): ")
    address = input("Enter address (street, number - neighborhood - city/state: ")

    users.append({"cpf": cpf, "name": name, "birth_date": birth_date, "address": address})
    print("User created successfully!")

def filter_user(cpf, users):
    for user in users:
        if user["cpf"] == cpf:
            return user
    return None

def list_accounts(accounts):
    for account in accounts:
        print(f"Account: {account['account_number']}, User: {account['user']['name']}")

def create_account(users, accounts):
    cpf = input("Enter user's CPF: ")
    user = filter_user(cpf, users)

    if user:
        account_number = len(accounts) + 1
        accounts.append({"agency": "0001", "account_number": account_number, "user": user})
        print(f"Account {account_number} created successfully for {user['name']}!")
    else:
        print("User not found. Please create a user first.")

def main():
    global balance, statement, withdrawal_count

    while True:
        option = menu()

        if option == "d":
            value = float(input("Enter the deposit amount: "))
            balance, statement = deposit(balance, value, statement)

        elif option == "w":
            value = float(input("Enter the withdrawal amount: "))
            balance, statement, withdrawal_count = withdraw(
                balance=balance, 
                value=value, 
                statement=statement, 
                limit=limit, 
                withdrawal_count=withdrawal_count, 
                limit_withdrawals=MAX_WITHDRAWALS
            )

        elif option == "e":
            show_statement(balance, statement=statement)

        elif option == "nu":
            create_user(users)

        elif option == "na":
            create_account(users, accounts)

        elif option == "la":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

main()
