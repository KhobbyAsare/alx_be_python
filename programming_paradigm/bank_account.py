"""
Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py,
which interfaces with the class through command line arguments to perform banking operations.
"""

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
