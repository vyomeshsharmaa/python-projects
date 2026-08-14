class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def describe(self):
        return f"{self.name} earns {self.__salary}"


def greet_employee(emp):
    return f"Welcome, {emp.name}!"