#1
class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance
    try:
        def deposit(self, amount):
            self.balance += amount
    except TypeError:
        print("Put a Valid Number")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance



# Example usage
account = BankAccount("Alice")

account.deposit(500)
print(account.check_balance())   # 500

account.withdraw(200)
print(account.check_balance())   # 300

account.withdraw(400)            # Insufficient funds
print(account.check_balance())   # 300

    



