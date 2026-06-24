#lists.py - storing collections of data

#Creating a list
fruits=["apple","banana","mango","grapes"]


#Accessing items by index 
print(fruits[0])  #Output: apple
print(fruits[1])  #Output: banana
print(fruits[-1]) #Output: grapes

#Length of a list
print(len(fruits))  #Output: 4

#Changing an item
fruits[1]="orange"
print(fruits)


#Adding an item to the end 
fruits.append("kiwi")
print(fruits)


#Removing a specific item
fruits.remove("apple")
print(fruits)


#Removing the last item
last_item=fruits.pop()
print(last_item)
print(fruits)


#Looping through a list
for fruit in fruits:
    print("I like:",fruit)


#Checking if something is in a list
print("mango" in fruits)
print("apple" in fruits)


#A list of numbers - useful for calculations
scores=[88,92,79,95,84]
total=0
for score in scores:
    total+=score

average=total/len(scores)

print("Average score is:",average)