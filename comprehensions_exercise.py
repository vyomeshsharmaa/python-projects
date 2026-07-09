#1

temperatures = [0, 15, 22, 37, 8, 41, 19, 30, 5, 28]
for1=[temp for temp in temperatures if temp>20]
print(f"Temperature above 20:{for1}")

for2=[temp*1.8+32 for temp in temperatures]
print(f"Temmperature in Fahrenheit:{for2}")

for3=[ "Hot" if temp >30 else
       "Warm" if temp >15 else
       "Cold" for temp in temperatures]
print(for3)


#2
students = ["vyomesh", "rahul", "priya", "arjun", "om", "lakshay"]
for4=[name.title() for name in students]
print(for4)

for5=[name for name in students if "a" in name]
print(for5)

for6=[len(name) for name in students if len(name)>4]
print(for6)


#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numb=[numb for numb in numbers if numb%2 ==0 and numb%3 ==0]
print(numb)

