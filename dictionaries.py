#dictionaries.py -- key-value pairs

#Creating a dictionary
person={"name":"Vyomesh","age":18,"city":"Haldwani"}
print(person)


#Accessing values by keys
print(person["name"])
print(person["age"])

#Changing a value
person["age"]=19
print(person)


#Adding a new key-value pair
person["country"]="India"
print(person)


#Removing a key-value pair
del person["city"]
print(person)


#Checking if a key exists
print("name" in person)
print("phone" in person)


#Looping-keys only
for key in person:
    print(key)


#Looping-keys and values together
for key, value in person.items():
    print(key,":", value)


#A more complex dictionary 
student={"name":"Vyomesh",
         "marks" : [88,92,79,95,84],
         "is_passed":True}
print(student["marks"])
print(student["marks"][0])


total=sum(student["marks"])
print("Total Marks:",total)
