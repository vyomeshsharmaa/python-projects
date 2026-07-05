#1
profile={"Name":"Vyomesh","Age":18,"City":"Haldwani","Goal":"To become the richest","favourite_lang":"Python"}
print(profile)
print(profile["Goal"])


#2
profile["github_username"]="vyomeshsharmaa"
profile["Age"]=19
print(profile)


#3
student_record = {
    "name": "Vyomesh",
    "subjects": ["Maths", "Science", "English", "Python"],
    "marks": [88, 79, 92, 95]
}
subjects = student_record["subjects"]
marks = student_record["marks"]

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

#4
for key, value in student_record.items():
    print(key, "->", value)