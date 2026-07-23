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

    def describe(self):
        return f"{self.name} earns {self.__salary}"


# Teacher INHERITS everything from Employee, using (Employee) in the class line
class Teacher(Employee):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)   # calls Employee's __init__ to set up name/salary
        self.subject = subject           # then adds the extra thing unique to Teacher

    # NEW method — Employee doesn't have this, only Teacher does
    def describe(self):                  # OVERRIDING Employee's describe() with a more specific version
        base = super().describe()        # reuse the parent's version instead of rewriting it
        return f"{base}, teaches {self.subject}"


emp = Employee("Ramesh", 40000)
print(emp.describe())          # Ramesh earns 40000

teacher = Teacher("Sunita", 55000, "Physics")
print(teacher.describe())      # Sunita earns 55000, teaches Physics
print(teacher.get_salary())    # 55000 — inherited method, never rewritten in Teacher
teacher.give_raise(10)         # inherited method works too
print(teacher.get_salary())    # 60500.0  