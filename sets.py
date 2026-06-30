#Sets.py - unique unordered collections


#Creating a set with duplicates - watch them disappear
numbers={1,2,3,2,1,4,5,4}
print(numbers)


#Converting a list with duplicates into a set
visited_cities=["Delhi","Mumbai","Delhi","Bangalore","Mumbai","Delhi"]
unique_cities=set(visited_cities)
print(unique_cities)
print(len(unique_cities))


#Adding and Removing
fruits={"apple","banana","mango"}
fruits.add("kiwi")
print(fruits)
fruits.remove("banana")
print(fruits)



#Membership Check
print("apple" in fruits)


#Set operators
set_a={1,2,3,4}
set_b={3,4,5,6}

print(set_a.union(set_b))        #Union of two sets
print(set_a.intersection(set_b)) #Intersection of two sets
print(set_a.difference(set_b))   #Difference of two sets