def greet(name):   #function arguments,
    print("welcome",name)

greet("rajat")


def add(a,b):  #multiple arguments
    print(a+b)

add(10,30)


def square(num):  #return statement , function ka jo result aata hai use vapas bhejta hai.
    return num * num
result = square(5)

print(result)


#RETURN VS PRINT
def add(a,b):  #return value ko program me aage dobara bhi use kiya ja sakta hai.
    return a + b
print(add(10,40))



def calculate(a,b):   #multiple return values, ek function me multiple values return kar sakta hai
    return a + b, a-b

sum_result,sub_result = calculate(10,5)

print('sum:',sum_result)
print('subtraction:',sub_result)


#function reusability
def cube(num):
    return num ** 3

print(cube(2))
print(cube(3))
print(cube(4))


#calculator using return
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

print(add(20,10))
print(subtract(20,10))



#student percentage generator
def percentage(m1,m2,m3,m4,m5):
    total = m1+m2+m3+m4+m5
    return (total/500)*100

result = percentage(80,75,85,90,75)
print("percentage",result)



#Area of rectangle
def area(length,width):
    return length * width

print("Area:", area(10,5))



#student result generator
def total_marks(m1,m2,m3):
    return m1+m2+m3

def percentage(total):
    return (total/300) * 100

m1 = int(input("enter a marks 1: "))
m2 = int(input("enter a marks 2: "))
m3 = int(input("enter a marks 3: "))

total = total_marks(m1,m2,m3)
per = percentage(total)

print("total marks: ",total)
print("percentage: ",per)



#multiple return values
def calculations(a,b):
    return a+b, a*b

sum_result, mul_result = calculations(3,5)

print("sum: ",sum_result)
print("multiplication: ",mul_result)

