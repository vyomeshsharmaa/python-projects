#functions.py - writing resuable code


#A function with no parameters
def say_hello():
    print("Hello! Welcome to Python")

say_hello()
say_hello()
say_hello()


#A function with one parameters
def greet(name):
    print("Hello,",name)
greet("Vyomesh")
greet("Rahul")
greet("Priya")


#A function with 2 parameters
def add_numbers(a,b):
    result=a+b
    print("The sum is", result)

add_numbers(5,3)
add_numbers(10,20)


#A function that RETURNS a value instead of printing 
def multiply(a,b):
    result=a*b
    return result

answer=multiply(4,5)
print(answer)


#Using a returned value in further calculation 
total=multiply(2,3)+multiply(4,5)
print(total)


#A function with default parameter value
def power(base, exponent=2):
    return base**exponent 


print(power(5))   #Uses default exponent value of 2
print(power(5,3)) #Uses provided exponent value of 3

