chemistry=int(input("Marks in Chemistry:"))
physics=int(input("Marks in Physics:"))
maths=int(input("Marks in Maths:"))
biology=int(input("Marks in Biology:"))
english=int(input("Marks in English:"))

total_marks=chemistry+physics+maths+biology+english

score=(total_marks/500)*100
if score>=90:
   grade =("Distinction")
elif score>=75:
    grade=("First Class")
elif score>=60:
    grade=("Second Class")
elif score>=40:
    grade=("Pass")
else:
    grade=("FAIL")


print("Total Marks You've Obtained:",total_marks,". And the total Percentage you got is",score,"%. Your Grade:",grade)


