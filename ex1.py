# LIST — ordered, changeable, duplicates allowed
my_list = [1, 2, 3]
my_list[0]                   # access by index
my_list[-1]                  # last item
my_list.append(4)            # add to end
my_list.insert(1, 99)        # insert at index
print(my_list)



class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    

__init__=[input()]
calculate_average=__init__()
import sys   
sys.exit()
