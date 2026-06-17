#this is a comment- python ignores this line
#basics.py - exploring print statements

#print plain text
print("hello from basics.py")

#printing a number
print(42)

#printing multiple things at once
print("My name is", "Vyomesh Sharma")

#printing with a separator 
print("Python","Data Science","AI", sep="->")

#printing an empty line
print("")

#printing with end - notice no new line after first print
print("this is on", end=" ")
print("the same line")




print("Vyomesh Sharma","18","Haldwani")
print("Python","Data Science","AI",sep=" | ")
print("here's your two",end=" ")
print("joined lines using end")


#----VARIABLES----


#Creating Variables
name= "Vyomesh"
age= 18
city= "Haldwani"
is_student= True


#using Variables inside print
print(name)
print(age)
print(city)
print(is_student)


#Using vairables with text together
print("My name is", name)
print("I am", age, "years old")
print("I live in", city)


#updating a variable
age=19
print("Next year I will be", age)


#creating a variable from two others
full_intro= "My name is " + name + " and I live in " + city
print(full_intro)


favourite_language= "Python"  
print("my fav language is",favourite_language)

my_goal= "To become the greatest and the richest"
print("my goal is",my_goal)

years_to_master= 2 
print("I will master Python in",years_to_master,"yrs")

years_to_master=1
print("or I will try my best to master python in ",years_to_master,"yr")





#----DATA TYPES----

#Integer 
my_age=18
print(type(my_age))

#float
my_height=5.7
print(type(my_height))

#string
my_name="Vyomesh"
print(type(my_name))

#boolean
is_employed=False
print(type(is_employed))

#Checking Types of expressions
print(type(42))
print(type(3.14))
print(type("python"))
print(type(True))



#MY DATA TYPES EXERCISE


#for int
crushs_age=18
print(type(crushs_age))

#for float
crushs_height=5.3
print(type(crushs_height))

#for string
my_goal="To Become The Greatest"
print(type(my_goal))

#for boolean
is_rich=False
print(type(is_rich))

result= crushs_age + crushs_height
print(type(result))

