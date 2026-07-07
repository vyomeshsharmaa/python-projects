#1
movies=["endgame","inception","interstellar","the dark knight","the matrix"]
movies.insert(2,"avatar")
print(movies)
movies.remove("avatar")
print(movies)


#2
numbers=[5,2,8,1,9,3,0]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.index(8)
idx=numbers.index(8)
print(f"Index of 8 is: {idx}")


#3
batch_a=["vyomesh","sachin","priyanshu","daksh"]
batch_b=["krishna","priya","tanvi"]
batch_a.extend(batch_b)
print(batch_a)
print(f"length of batch_a is: {len(batch_a)}")


#4
copy=[1,2,3]
wrong_copy=copy
wrong_copy.append(99)
print(copy) #99 is here too - they share the same list
print(wrong_copy) #99 is here too - they share the same list
real_copy=copy.copy() #Actual independent copy
real_copy.append(88)
print(copy) #88 is NOT here - truly separate
print(real_copy) #88 is here - truly separate