class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary
      

    def get_salary(self):
        return self.__salary
    
    def describe(self):
        return f"{self.name} earns {self.__salary}"
    
    def annual_bonus(self):
        return self.__salary*0.10
    
class Manager(Employee):
    def __init__(self, name, salary,team_size):
         super().__init__(name, salary)
         self.team_size=team_size

    def describe(self):
        return f"{super().describe()}, manages a team of {self.team_size}"
    
    def annual_bonus(self):
        return super().annual_bonus() * 2
         
    
class Intern(Employee):
     def __init__(self, name, salary, mentor_name):
         super().__init__(name,salary)
         self.mentor_name=mentor_name

     def describe(self):
         return f"{super().describe()}, and is being mentored by {self.mentor_name}"


staff=[
    Employee("Vyomesh",1900000000),
    Intern("Krish",190000,"Vyomesh"),
    Manager("Void",900000,10)
]


for person in staff:
    print(person.describe())
    print("Annual Bonus:", person.annual_bonus())
