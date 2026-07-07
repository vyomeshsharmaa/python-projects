#list_methods.py - manipulating lists


numbers=[5,2,8,1,9,3]
fruits=["apple","banana","mango"]


#append and insert
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"orange")
print(fruits)


#remove and pop
fruits.remove("banana")
print(fruits)
last=fruits.pop()
print(f"Removed:{last}")
print(fruits)


#index and count
fruits=["apple","orange","mango","orange"]
print(fruits.index("orange"))
print(fruits.count("orange"))


#sort and reverse
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)


#copy - the right way 
original=[1,2,3]
wrong_copy=original #NOT a real copy
real_copy=original.copy() #Actual independent copy
wrong_copy.append(99)
print(original) #99 is here too - they share the same list
print(real_copy) #99 is NOT here - truly separate


#extend
list_a=[1,2,3]
list_b=[4,5,6]
list_a.extend(list_b)
print(list_a)