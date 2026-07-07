#1
raw_input="    vyomesh SHARMA    "
print(raw_input.strip().title())
print(f"Cleaned name: {raw_input.strip().title()}")


#2
data = "Python,Data Science,Machine Learning,AI,Automation"
parts = data.split(",")           # split by comma — gives you the list
print(parts)
print(len(parts))                     # length of the list
rejoined = " | ".join(parts)      # join that list back with " | "
print(rejoined)


#3
mysentence="I will become the greatest and the richest person in the world" 
print(mysentence.count("a"))
print(mysentence.startswith("I"))
print(mysentence.replace("the","the whole"))

#4
name="Vyomesh"
age=18
city="Haldwani"
goal="To become the richest"
print(f"My name is {name}, I am {age} years old, I live in {city} and my goal is {goal}.")





