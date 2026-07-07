#string_methods.py - manipulating text


name="vyomesh sharma"

#Case methods
print(name.upper())
print(name.title())
print(name.capitalize())


#Whitesccape 
messy="   hello world   "
print(messy.strip())


#Search
sentence="I am learning Python for Data Science"
print(sentence.find("Python"))
print(sentence.count("a"))
print(sentence.startswith("I"))
print(sentence.endswith("Science"))


#Replace
print(sentence.replace("Python","programming"))


#Split
csv="Vyomesh,18,Haldwani,Python"
parts=csv.split(",")
print(parts)
print(parts[0])
print(parts[2])


#Join
words=["Data","Science","is","my","goal"]
print(" ".join(words))


#f-strings
name="Vyomesh"
age=18
city="Haldwani"
print(f"My name is {name}, I am {age} years old and I live in {city}.")


#f-string with experessions inside
marks=[88,79,92,95,84]
print(f"My average score is {sum(marks)/len(marks)}")

