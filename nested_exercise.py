#1
classroom=[
    {"name":"Vyomesh","age":18,"city":"Haldwani","marks":{"Science":85,"Math":90}},
    {"name":"Rahul","age":19,"city":"Delhi","marks":{"Science":80,"Math":85}},
    {"name":"Priyashi","age":18,"city":"Mumbai","marks":{"Science":90,"Math":88}},
    {"name":"Arjun","age":20,"city":"Bangalore","marks":{"Science":75,"Math":80}}
    ]

for student in classroom:
    name=student["name"]
    city=student["city"]
    print(f"{name} lives in {city}.")
    marks=student["marks"]
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    average=sum(student["marks"].values())/len(student["marks"])
    print(f"average marks of {student["name"]} is {average}")
    if average>=40:
        print(f"{student["name"]} has passed")
    else:
        print(f"{student["name"]} has failed")


topper = None
high_avg = 0

for student in classroom:
    avg = sum(student["marks"].values()) / len(student["marks"])
    if avg > high_avg:
        high_avg = avg
        topper = student["name"]

print(f"The topper is {topper} with an average of {high_avg}")


classroom.append({"name":"Lakshay","age":18,"city":"Haldwani","marks":{"Science":0,"Math":0}})
print(f"Number of Students After Updating:{len(classroom)}")
