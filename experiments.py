list_a=[1,2,3]
list_b=[4,5,6,1]
list_a.extend(list_b)
print(list_a)


#Add a new student
student=[{"name":"Vyomesh","age":18,"city":"Haldwani","marks":{"Science":85,"Math":90}}]
student.append({"name":"Sachin","age":19,"city":"Delhi","marks":{"Science":80,"Math":85}})
print(student[1]["marks"])
