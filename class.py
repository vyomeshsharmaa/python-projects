class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def calculate_average(self):
        return sum(self.marks)/len(self.marks)

    def is_passing(self,passing_marks=40):
        return self.calculate_average()>=passing_marks
    

student1=Student("Vyomesh",18,[88,92,79])
student2=Student("Rahul",19,[30,35,38])
print(student1.calculate_average())
print(student2.calculate_average())
print(student1.is_passing())
print(student2.is_passing())
