from models.user import User
from models.account import Account
from models.transaction import Transaction
from services.user_service import UserService
from services.account_service import AccountService
from services.transaction_service import TransactionService

def main():
    # Initialize services
    user_service = UserService()
    account_service = AccountService()
    transaction_service = TransactionService()

    # Simple user input loop
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/accountant): ")
            user = User(user_id=len(user_service.users) + 1, username=username, password=password, role=role)
            user_service.add_user(user)
            print("User registered successfully!")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_service.authenticate_user(username, password)
            if user:
                print(f"Welcome, {user.username}!")
                while True:
                    print("1. Add Account")
                    print("2. Add Transaction")
                    print("3. View Accounts")
                    print("4. View Transactions")
                    print("5. Logout")
                    choice = input("Enter choice: ")

                    if choice == '1':
                        account_name = input("Enter account name: ")
                        account_type = input("Enter account type (asset/liability/equity/revenue/expense): ")
                        account = Account(account_id=len(account_service.accounts) + 1, name=account_name, account_type=account_type)
                        account_service.add_account(account)
                        print("Account added successfully!")

                    elif choice == '2':
                        account_id = int(input("Enter account ID: "))
                        amount = float(input("Enter amount: "))
                        transaction_type = input("Enter transaction type (credit/debit): ")
                        description = input("Enter description: ")
                        account = account_service.get_account(account_id)
                        if account:
                            transaction = Transaction(transaction_id=len(transaction_service.transactions) + 1, account=account, amount=amount, transaction_type=transaction_type, description=description)
                            transaction_service.add_transaction(transaction)
                            print("Transaction added successfully!")
                        else:
                            print("Invalid account ID")

                    elif choice == '3':
                        print("Accounts:")
                        for account in account_service.accounts:
                            print(account)

                    elif choice == '4':
                        print("Transactions:")
                        for transaction in transaction_service.transactions:
                            print(transaction)

                    elif choice == '5':
                        print("Logged out")
                        break

                    else:
                        print("Invalid choice")

            else:
                print("Invalid username or password")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
