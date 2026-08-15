import random
import math
import datetime
import os

# random — random.py, ships with Python
dice_roll = random.randint(1, 6)
print("Dice roll:", dice_roll)

names = ["Ramesh", "Sunita", "Aman"]
print("Random pick:", random.choice(names))

# math — common math operations
print("Square root of 81:", math.sqrt(81))
print("Value of pi:", math.pi)

# datetime — dates and times
today = datetime.date.today()
print("Today's date:", today)

# os — talking to the operating system / file paths
print("Current folder:", os.getcwd())
print("Files here:", os.listdir())