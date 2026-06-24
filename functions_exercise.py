#A function with no return - just action
def print_separator():
    print("--------------------------------------")




#A function with parameters and a return value
def calculate_area(length, width):
    area = length * width
    return area

print_separator()


rectangle_1= calculate_area(5,10)
rectangle_2= calculate_area(7,3)

print("Area of rectangle 1 is:", rectangle_1)
print("Area of rectangle 2 is:", rectangle_2)


print_separator()


#A function with a default parameter
def apply_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price

print("Price after discount is:", apply_discount(100))
print("Price after discount is:", apply_discount(100, 20))

print_separator()

def check_voting_age(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
    
    
print(check_voting_age(20))
print(check_voting_age(16))
print(check_voting_age(18))


