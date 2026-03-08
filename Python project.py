class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Deposit amount must be non-negative.")
            return False
        self.balance += amount
        print(f"Deposited Rs{amount}. Current balance: Rs{self.balance}")
        return True

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Withdrawal amount must be non-negative.")
            return False
        if amount > self.balance:
            print("Error: Insufficient balance.")
            return False
        self.balance -= amount
        print(f"Withdrew Rs{amount}. Current balance: Rs{self.balance}")
        return True

    def get_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            print("Error: Account already exists.")
            return False
        if initial_balance < 0:
            print("Error: Initial balance must be non-negative.")
            return False
        self.accounts[account_number] = BankAccount(account_number, initial_balance)
        print("Account created successfully.")
        return True

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Error: Account does not exist.")
            return False
        if amount < 0:
            print("Error: Deposit amount must be non-negative.")
            return False
        return self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Error: Account does not exist.")
            return False
        if amount < 0:
            print("Error: Withdrawal amount must be non-negative.")
            return False
        return self.accounts[account_number].withdraw(amount)

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            print("Error: Account does not exist.")
            return None
        return self.accounts[account_number].get_balance()

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            print("Error: One or both accounts do not exist.")
            return False
        if amount < 0:
            print("Error: Transfer amount must be non-negative.")
            return False
        if amount > self.accounts[from_account].get_balance():
            print("Error: Insufficient balance for transfer.")
            return False
        if not self.withdraw(from_account, amount):
            print("Error: Withdrawal failed for transfer.")
            return False
        if not self.deposit(to_account, amount):
            print("Error: Deposit failed for transfer.")
            self.deposit(from_account, amount) 
            return False
        print(f"Transfer of Rs{amount} from account {from_account} to account {to_account} successful.")
        return True


def print_menu():
    print("Bank Account Management System")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Account Balance")
    print("5. Transfer Money")
    print("6. Exit")


def main():
    bank_system = BankSystem()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            if account_number in bank_system.accounts:
                print("Error: Account already exists.")
                continue
            initial_balance = float(input("Enter initial balance: "))
            bank_system.create_account(account_number, initial_balance)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank_system.deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank_system.withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            balance = bank_system.get_balance(account_number)
            if balance is not None:
                print(f"Account balance: Rs{balance}")
        elif choice == '5':
            from_account = input("Enter sender account number: ")
            to_account = input("Enter receiver account number: ")
            amount = float(input("Enter transfer amount: "))
            bank_system.transfer(from_account, to_account, amount)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
