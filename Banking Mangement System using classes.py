class Account:
    def __init__(self, account_holder, account_number, balance=0):
        """Initializes a new account with the given details."""
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposits a specified amount to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient balance exists."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def check_balance(self):
        """Displays the current balance of the account."""
        print(f"Account balance: {self.balance}")

    def __str__(self):
        """Returns a string representation of the account."""
        return f"Account holder: {self.account_holder}, Account number: {self.account_number}, Balance: {self.balance}"


class BankingSystem:
    def __init__(self):
        """Initializes the banking system with an empty list of accounts."""
        self.accounts = {}

    def create_account(self, account_holder, account_number, initial_balance=0):
        """Creates a new account with the given details."""
        if account_number in self.accounts:
            print(f"Account with account number {account_number} already exists.")
        else:
            new_account = Account(account_holder, account_number, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder}.")

    def get_account(self, account_number):
        """Fetches an account by account number."""
        return self.accounts.get(account_number)

    def deposit_to_account(self, account_number, amount):
        """Deposits money into a specific account."""
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account with number {account_number} does not exist.")

    def withdraw_from_account(self, account_number, amount):
        """Withdraws money from a specific account."""
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account with number {account_number} does not exist.")

    def check_account_balance(self, account_number):
        """Checks the balance of a specific account."""
        account = self.get_account(account_number)
        if account:
            account.check_balance()
        else:
            print(f"Account with number {account_number} does not exist.")

    def display_all_accounts(self):
        """Displays all accounts in the system."""
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts available.")


# Example Usage
if __name__ == "__main__":
    bank_system = BankingSystem()

    # Creating accounts
    bank_system.create_account("Alice", "1001", 500)
    bank_system.create_account("Bob", "1002", 1000)

    # Checking balance
    bank_system.check_account_balance("1001")

    # Depositing money
    bank_system.deposit_to_account("1001", 200)

    # Withdrawing money
    bank_system.withdraw_from_account("1002", 500)

    # Checking balance again after transactions
    bank_system.check_account_balance("1001")
    bank_system.check_account_balance("1002")

    # Displaying all accounts
    bank_system.display_all_accounts()
