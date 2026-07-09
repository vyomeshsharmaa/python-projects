#list_comprehensions.py - concise list creation


numbers=[1,2,3,4,5,6,7,8,9,10]

#Square of all numbers
squared=[num**2 for num in numbers]
print(squared)


#Only even numbers
evens=[num for num in numbers if num%2==0]
print(evens)

#Only odd nummbers
odds=[num for num in numbers if num%2!=0]
print(odds)


#Multiple every number by 3, but only if it's greater than 5
multiplication=[num*3 for num in numbers if num>5]
print(multiplication)


#string list comprehension
names=["vyomesh","rahul","priya","arjun","lakshay"]
capitalized=[name.title() for name in names]
print(capitalized)

long_names=[name for name in names if len(name)>5]
print(long_names)

lengths=[len(name) for name in names]
print(lengths)


#Practical - extract all passing marks from a list
marks=[88,35,72,45,29,91,55,38]
passing=[mark for mark in marks if mark>=40]
print(passing)

#Convert all marks to letter grades
grades=["Pass" if mark>=40 else
        "Fail" for mark in marks]
print(grades)