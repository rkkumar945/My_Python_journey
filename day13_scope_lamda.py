#local scope,variable function ke andar banaye jate hai or sirf wahi usi function ke andar use hote hai
def show():
    name = "rajat"
    print(name)

show()  


#Global scope,variable function ke bahar banaye jate hai or wahi variable poore program me use ho sakte hai
name = "rajat"

def show():
    print(name)

show() 



#local vs global variables, ,local variable ko pehle priority leta hai 
name = "global rajat"

def show():
    name = "local rajat"
    print(name)

show()
print(name)


#global keyword, agar function ke andar global varible ko change karna ho
count = 0

def increase():
    global count
    count += 1

increase()
print(count)



#lambda function,it is a short function
def square(num): #normal function
    return num * num
print(square(5))


square = lambda num: num*num #lambda version function

print(square(5))




#multiple arguments lambda
add = lambda a,b: a+b
print(add(10,40))



#anonymous function
print((lambda x: x*2)(5))



#square calculator
square = lambda x: x ** 2
print(square(8))


#even or odd checker
check = lambda x: "Even" if x%2 == 0 else "odd"
print(check(10))

#student percentage
percentage = lambda total: (total/500)*100

print(percentage(420))

#Marks analysis tool
marks = [85,78,90,85]

print("total: ",sum(marks))
print("average: ",sum(marks)/ len(marks))
print("highest: ",max(marks))
print("lowest: ",min(marks))



#global and local variable
college_name = "MIT"

def show():
    student_name = "rajat"
    print("student_name: ",student_name)
    print("college_name: ",college_name)

show()
