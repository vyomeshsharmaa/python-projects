#loops.py - repeating actions


#Basic for loop

for i in range(5):
    print("Count:",i)


#For loop with range start/stop
for i in range(2,8):
    print(i)


#For loop with step
for i in range(0,10,2):
    print(i)


#while loop
count=0
while count <5:
    print("While count:", count)
    count +=1


#loops with a condition inside - print only even numbers
for num in range (1,11):
    if num %2==0:
        print(num,"is even")


#loop that builds something
total=0
for num in range(1,6):
    total+=num
    print("Total sum is:",total)
    