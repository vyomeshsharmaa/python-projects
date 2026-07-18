#1
import sys
try:
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
except ValueError:
    print("Enter a valid number.")
    sys.exit()

#3 and 4    
try:
  operator=(input(f"Which operation to be done:"))
  if operator=="+":
      print(f"{a}+{b}={a+b}")
  elif operator=="-":
     print(f"{a}-{b}={a-b}")
  elif operator=="*":
     print(f"{a}*{b}={a*b}")
  elif operator=="/":
     print(f"{a}/{b}={a/b}")
  else:
        print("Put correct operation.")
    
except ValueError:
    print("Unknown operator.")
except ZeroDivisionError:
    print("You cannot divide any number by 0.")
finally:
    print("Calculator Session ended.")

