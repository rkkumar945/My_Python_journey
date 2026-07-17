fruits = ["apple","banana","mango",] #list
print(fruits)

fruits = ["apple","mango","banana"] # list indexing

print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1]) #negative indexing


print(fruits[-1]) #negative indexing

fruits = ['apple','mango'] #append method. list ke last me new element add karta hai

fruits.append('mango')
print(fruits)


fruits = ['apple','mango'] #insert method. specific index per element add karta hai

fruits.insert(1,'orange')
print(fruits)


fruits = ['apple','mango'] #remove mathod. value remove karta hai

fruits.remove('mango')
print(fruits)


fruits = ["apple","mango","banana"] #pop method. index ke according element remove karta hai.

fruits.pop(1)
print(fruits)


fruits.pop() #agar index na de to khud se last element hata deta hai


numbers = [50,20,10,40] #ascending order me sort karta hai

numbers.sort()
print(numbers)


numbers.sort(reverse=True) #descending order me sort karta hai

print(numbers)


numbers = [1,2,3,4,5] #reverse
numbers.reverse()
print(numbers)


fruits = ['apple','banana','orange'] #length
print(len(fruits))


marks = [85, 90, 78, 92, 88] # MINI PROJECT. 

print("Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average:", sum(marks) / len(marks))



shopping = [] # mini project shopping list

shopping.append("Milk")
shopping.append("Bread")
shopping.append("Rice")

print(shopping)



skills = ["Python", "SQL", "Power BI"] # mini project favourite skill

print("Current Skills:", skills)

skills.append("Machine Learning")

print("Updated Skills:", skills)



numbers = [5, 15, 25, 35, 45]
#first element index 0
print("first element :", numbers[0])

# last element (index -1)
print("last element:", numbers[-1])



fruits = []

# loop for 5 fruits name
for i in range(5):
    fruit = input(f"enter your favourite fruit name {i+1}: ")
    fruits.append(fruit)


print("\n your favourite fruit list:")
print(fruits)



numbers = [10, 25, 40, 5, 20]

max_val = max(numbers)
min_val = min(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"list: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print(f"Sum: {total_sum}")
print(f"Average: {average}")




cities = ["Delhi", "Mumbai", "Dublin", "Cork"]

cities.remove("Cork")

cities.append("Galway")

cities.sort()

print(cities)