def greet():    #block of code which is reusable
    print("hello rajat")

greet() 


def greet(name):    #function with parameters, function ko data dene ke liye
    print("hello",name)

greet("rajat")    




def add(a,b):  #multiple parameters
    print(a+b)

add(10,20)    



def add(a,b):  #return statement
    return a+b
result = add(10,20)

print(result)



def square(num):  #return statement
    return num * num
print(square(5))



def test():  #local variable , function ke andar bane variable ka use function ke andar hi hota hai
    x = 10
    print(x)

test()  


name = "rajat" # global variable , poore program me use kar sakte hai

def show():
    print(name)

show()  



def square(num):  #return statement
    return num * num
number = int(input("enter a number: "))
print(square(number))



def area(radius):
    return 3.14 * radius*radius
r = float(input("enter radius: "))

print("area: ",area(r))



def check(num):   #even or odd
    if num%2 == 0:
        return "even"
    else:
        return "odd"
    
number = int(input("enter a number: "))

print(check(number))




#Student Result Management System project 
def total_marks(m1,m2,m3):
    return m1+m2+m3

def average_marks(total):
    return total / 3

m1 = int(input("enter marks 1: "))
m2 = int(input("enter marks 2: "))
m3 = int(input("enter marks 3: "))

total = total_marks(m1,m2,m3)

average = average_marks(total)

print("total: ", total)
print("average: ",average)







def cube(num):  #return statement
    return num * num* num
number = int(input("enter a number: "))
print(cube(number))


#ek function jo student ke marks ki % nikale
def percentage(m1,m2,m3,m4):
    total = m1+m2+m3+m4
    per = (total/400) * 100
    return per

result = percentage(80,75,90,85)

print("percentage: ",result)





#number positive ,negative,ya zero batane wala function
number = int(input("enter a number: "))

def check_number(num):
    if num>0:
        return "positive number"
    elif num<0:
        return "negative number"
    else:
        return "zero"
    
print(check_number(number))    





#user ka name lekar welcome msg print karne wala function
user_name = input("enter your name: ")

def welcome(name):
    print("welcome",name)

welcome(user_name) 



#function, jo user se student ka name or percentage lekar print kare
user_name = input("enter your name: ")
user_percentage = int(input("enter your percentage: "))

def welcome(name):
    print("welcome",name)

def percentage(per):
    print("your percentage is: ",per)

welcome(user_name)
percentage(user_percentage)        



