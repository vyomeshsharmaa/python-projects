import random 
import math
import datetime
import os

import employee2_module


#1 random
dice1= random.randint(1, 6)
print("Dice roll no.1:", dice1)
dice2= random.randint(1, 6)
print("Dice roll no.2:", dice2)

print("Total sum of numbers rolled:", dice1+dice2)

#2
today = datetime.date.today()
print(f"Dice rolled on {today}: {dice1} and {dice2} = {dice1+dice2}")

#3
staff = [
    employee2_module.Employee("Vyomesh", 1900000000),
    employee2_module.Intern("Krish", 190000, "Vyomesh"),
    employee2_module.Manager("Void", 900000, 10),
    employee2_module.Employee("Sunita", 50000)
]

print(f"Employee of the day: {random.choice(staff).describe()}")

for filename in os.listdir():
    if filename.endswith(".py"):
        print(filename)