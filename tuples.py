#tuples.py - fixed collections of data

#Creating a tuple
coordinates=(28.6139,77.2090)
print(coordinates)
print(coordinates[0])  
print(coordinates[1])


#Days of the week - a perfect real-world tuple
days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days[0])
print(days[-1])
print(len(days))


#Looping through a tuple
for day in days:
    print(day)


#Checking membership 
print("Monday" in days)
print("Funday" in days)


#Trying to change a tuple - this WILL crash
#coordinates[0]=99