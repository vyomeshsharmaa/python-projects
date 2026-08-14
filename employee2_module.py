class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def describe(self):
        return f"{self.name} earns {self.__salary}"




class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        return f"{super().describe()}, manages a team of {self.team_size}"




class Intern(Employee):
    def __init__(self, name, salary, mentor_name):
        super().__init__(name, salary)
        self.mentor_name = mentor_name

    def describe(self):
        return f"{super().describe()}, and is being mentored by {self.mentor_name}"



def total_payroll(staff_list):
    total = 0
    for employee in staff_list:
        total += employee.get_salary()
    return total