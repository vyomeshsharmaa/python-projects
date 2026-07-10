list_a=[1,2,3]
list_b=[4,5,6,1]
list_a.extend(list_b)
print(list_a)


# Add a new student
students = [
    {"name": "Vyomesh", "age": 18, "city": "Haldwani", "marks": {"Science": 85, "Math": 90}}
]
students.append({"name": "Sachin", "age": 19, "city": "Delhi", "marks": {"Science": 80, "Math": 85}})
print(students[1]["marks"])


numbers = [1, 2, 3, 4, 5]
squared = []

for numb in numbers:
    squared.append(numb ** 2)

print(squared)   # [1, 4, 9, 16, 25]


numbb=9/2
print(numbb)

numb1=9/0
print(numb1)