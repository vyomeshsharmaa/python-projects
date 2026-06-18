#operators.py - exploring python operators


#----ARITHMETIC----
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#Practical use of modulus - even or odd
number=7
print(number%2)  #if result is 0, even. If 1, odd



#----COMPARISON----
x=10
y=5


print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=10)
print(x<=y)


#----LOGICAL----
age=18
has_id=True

print(age>=18 and has_id)
print(age>=18 or has_id)
print(not has_id)


#My OPERATORS EXERCISE

monthly_income=100000
monthly_expense=75000
monthly_saving=monthly_income-monthly_expense
print("monthly savings =",monthly_saving)

yearly_saving=12*monthly_saving
print("yearly savings =",yearly_saving)
print(yearly_saving>=100000)


score=73
print("If remainder is 1, odd. If remainder is 0, even. REMAINDER =",score%2)


knows_python=True
has_github=False

print(knows_python and has_github) #Here if he'll have both github and would know python, the outcome will be "TRUE". If not thn "FALSE"
print(knows_python or has_github)  #Here if one of them will be "True" the outcome will be "TRUE" aswell. If not thn "false"
print(not knows_python)  #Here it will flip the "TRUE" to "FALSE"
