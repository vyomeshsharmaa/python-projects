class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
        except TypeError:
            print("Please enter a valid number")

    def withdraw(self, amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds")
        except TypeError:
            print("Please enter a valid number")

    def check_balance(self):
        return self.balance


# Test the class
account = BankAccount("Alice", 100)

# Valid deposit
account.deposit(50)
print(account.check_balance())  # 150

# Valid withdrawal
account.withdraw(30)
print(account.check_balance())  # 120

# Over-limit withdrawal
account.withdraw(200)           # Insufficient funds

# Invalid deposit (string instead of number)
account.deposit("five")         # Please enter a valid number

# Invalid withdrawal (string instead of number)
account.withdraw("five")        # Please enter a valid number

# Final balance
print(account.check_balance())  # 120