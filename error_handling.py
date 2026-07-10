#error_handling.py


#Basic try/except
try:
    number=int(input("Enter a number:"))
    print(f"You entered: {number}")

except ValueError:
    print("That's not a valid answer. Please enter digits only.")


#Handling division by zero
try:
    a=int(input("Enter numerator:"))
    b=int(input("Enter denominator:"))
    result=a/b
    print(f"Result: {result}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")


#else and finally
try:
    age=int(input("Enter your age:"))

except ValueError:
    print("Age must be a number")
else:
    print(f"Your age is {age}. No errors occured.")
finally:
    print("Thank you for using the program")


#KeyError - Dictionary
person={"name":"Vyomesh","age":18}
try:
    print(person["phone"])
except KeyError:
    print("That key doesn't exist in the dictionary")


#IndexError - list
mark=[88,92,79]
try:
    print(mark[10])
except IndexError:
    print("That index is out of range.")

