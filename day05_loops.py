for i in range(5): #for loop
    print(i)


for i in range(1, 6): #range 
    print(i)    


for i in range(2, 11, 2): #step size
    print(i)  



count = 1#while 

while count <= 5:
    print(count)
    count += 1      



for i in range(1, 11): #break
    if i == 6:
        break
    print(i)    



for i in range(1, 6): #continue
    if i == 3:
        continue
    print(i)    



num = int(input("Enter a number: "))#multiplication table

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



total = 0#sum of first N number

for i in range(1, 11):
    total += i

print("Sum =", total)    




for i in range(1, 21): #even numbers 1 to 20
    if i % 2 == 0:
        print(i)




n = int(input("Enter a number (N): "))#sum of first N number
total_sum = sum(range(1, n + 1))
print("The sum of the first n numbers is": total_sum)  


import math#factorial of a number

n = int(input("Enter a number to find its factorial: "))
# Using the built-in math function
print(f"The factorial of {n} is: {math.factorial(n)}")

# Alternatively, using a loop:
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"The factorial of {n} is: {factorial}")






