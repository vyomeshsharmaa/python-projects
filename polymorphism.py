class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def give_raise(self,percent):
        try:
            self.__salary*=self.__salary * (percent/100)
        except TypeError:
            print("Please enter a valid number")

    def describe(self):
        return f"{self.name} earns {self.__salary}"
    

class Teacher(Employee):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary) 
        self.subject = subject  

    def describe(self):
        return f"{super().describe()}, teaches {self.subject}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        return f"{super().describe()}, manages a team of {self.team_size}"
    
#Polymorphism in action : one list, mixed object types, same method call

staff = [
    Employee("Ramesh", 40000),
    Teacher("Sunita", 55000, "Physics"),
    Manager("Aman", 70000, 5)
]

for person in staff:
    print(person.describe()) #same call, different outputs - Python picks the right version automatically

#Output
#Ramesh Earns 40000
#Sunita earns 50000, teaches physics
#Aman earns 70000, manages a team of 5