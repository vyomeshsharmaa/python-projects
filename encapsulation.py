class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name          # public — fine to expose, low risk
        self.__balance = balance              # private — name-mangled, protected from direct outside access

    # GETTER — controlled read access
    def get_balance(self):
        return self.__balance

    # SETTER — controlled write access, with validation baked in
    def set_balance(self, amount):
        if not isinstance(amount, (int, float)):
            print("Balance must be a number")
            return
        if amount < 0:
            print("Balance cannot be negative")
            return
        self.__balance = amount

    def deposit(self, amount):
        try:
            self.__balance += amount
        except TypeError:
            print("Please enter a valid number")

    def withdraw(self, amount):
        try:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds")
        except TypeError:
            print("Please enter a valid number")


account = BankAccount("Alice", 100)

print(account.get_balance())          # 100 — controlled read, works fine

account.set_balance(500)              # valid — passes validation
print(account.get_balance())          # 500

account.set_balance(-50)              # "Balance cannot be negative" — blocked by setter
print(account.get_balance())          # 500, unchanged

# print(account.__balance)            # this line would CRASH with AttributeError
                                       # because Python mangled it to _BankAccount__balance

print(account._BankAccount__balance)  # 500 — technically still reachable if you know the
                                      # mangled name, proving __ is a deterrent, not a lock