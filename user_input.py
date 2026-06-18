#user_input.py - making programs interactive 

#Basic input
name= input("What is your name?")
print("Hello,", name)

#Input with type conversion
age=int(input("How old are you?"))
next_year_age= age+1
print("Next year you will be,",next_year_age)

#float input
height=float(input("what is your height in feet?"))
print("your height is",height,"feet")

#using multiple inputs together
city=input("which city are you from?")
print(name,"is",age,"years old and lives in",city)


#MY INPUT EXERCISE


name=input("What is your name?")
age=int(input("What is your age?"))
goal=input("What is that one goal which you wanna accomplish?")
years=int(input("How many years will it take for you to accomplish your goal?"))
goal_year=2026+years
language=input("What is your favourite programming language?")

print("So, Hi,",name,".You are",age,"yrs old and your goal in your life is,",goal,". And you are determined to accomplish it by,",goal_year,". And your favourite programming language is,",language)
