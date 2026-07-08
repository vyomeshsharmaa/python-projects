#nested_data.py - real world data structures


#A list of dictionaries
students=[
    {"name":"Vyomesh","age":18,"marks":[88,92,79,95]},
    {"name":"Rahul","age":19,"marks":[75,81,90,88]},
    {"name":"Priya","age":17,"marks":[95,88,92,91]}
]


#Accessing specific values
print(students[0]["name"])  # Accessing the name of the first student
print(students[1]["marks"])  # Accessing the marks of the second student
print(students[2]["marks"][0])  # Accessing the first mark of the third student


#Looping and calculating averages
for student in students:
    name=student["name"]
    marks=student["marks"]
    average=sum(marks)/len(marks)
    print(f"{name}'s average marks: {average}")


#finding the topper
topper=None
highest_avg=0

for student in students:
    avg=sum(student["marks"])/len(student["marks"])
    if avg>highest_avg:
        highest_avg=avg
        topper=student["name"]

print(f"The topper is {topper} with an average of {highest_avg}.")

# Adding a new student
students.append({"name": "Arjun", "age": 20, "marks": [70, 85, 88, 91]})
print(f"Total students: {len(students)}")

# Adding a new mark to first student
students[0]["marks"].append(100)
print(f"Vyomesh's updated marks: {students[0]['marks']}")

