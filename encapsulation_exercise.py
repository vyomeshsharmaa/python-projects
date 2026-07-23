class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if isinstance(amount, (int, float)):
            if amount > 0:
                self.__salary = amount
            else:
                print("Salary must be greater than 0")
        else:
            print("Salary must be a number")

    def give_raise(self, percent):
        try:
            self.__salary += self.__salary * (percent / 100)
        except TypeError:
            print("Please enter a valid number")


# Test the class
employee = Employee("Alice", 50000)

print(employee.get_salary())    # 50000

employee.give_raise(10)
print(employee.get_salary())    # 55000.0

employee.set_salary(60000)
print(employee.get_salary())    # 60000

employee.set_salary(-1000)      # Salary must be greater than 0

employee.set_salary("ten")      # Salary must be a number

employee.give_raise("ten")      # Please enter a valid number

print(employee.get_salary())    # 60000