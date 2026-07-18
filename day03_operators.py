a = 20 #airthmatic operators
b = 5

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division


print(10 % 3)#module operator
print(10 // 3)##floor division
print(2 ** 3)#power operator



x = 10#assignment operators

x += 5
print(x)


a = 10#camparison operator
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



is_student = True#boolean data type
is_employed = False

print(type(is_student))



num1 = float(input("Enter first number: ")) #mini project simple calculator
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)



obtained = float(input("Enter obtained marks: ")) #percentage calculator
total = float(input("Enter total marks: "))

percentage = (obtained / total) * 100

print("Percentage =", percentage)



age = int(input("Enter your age: "))#age after 5 years

print("Age after 5 years =", age + 5)



num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print(f"{num1} square is: {num1 ** 2}")
print(f"{num2} square is: {num2 ** 2}")



radius = float(input("enter radius of circle: "))
area = 3.14 * radius * radius

print("radius of circle is": area)




marks = float(input("enter obtained marks: "))
total_marks = float(input("enter total marks: "))

percentage = (marks / total_marks) * 100

print("your percentage is": percentage)



num = int(input("enter a number: "))

if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")


