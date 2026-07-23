class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def give_raise(self, percent):
        try:
            self.__salary += self.__salary * (percent / 100)
        except TypeError:
            print("Please enter a valid number")

    def add_amount(self, amount):
        try:
            self.__salary += amount
        except TypeError:
            print("Please enter a valid number")

    def describe(self):
        return f"{self.name} earns {self.__salary}"


class Manager(Employee):
    def __init__(self,name,salary,team_size):    
        super().__init__(name,salary)
        self.team_size = team_size

    def describe(self):
        return f"{super().describe()}, manages a team of {self.team_size}"
    
    def give_bonus(self, amount):
        self.add_amount(amount)
    

manager=Manager("Ramesh", 40000, 5)
print(manager.describe())
print(manager.get_salary())

manager.give_bonus(5000)
print(manager.get_salary())

manager.give_bonus("bonus")

print(manager.get_salary())        