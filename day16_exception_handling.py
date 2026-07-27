#wo error jo program ko run karte time aati hai unko exception kaha jata hai

num = int(input("enter number: ")) #agar number ki jagah hello likh de to error dega

#value error
num = int("abc")

#Zero division error
print(10/0)

#name error
print(name)


#TRY BLOCK (jo code error de sakta hai usko try block ke andar likhte hai)
try:
    num = int(input("enter number: "))
    print(num)

except:
    print("invalid input")  



#SPECIFIC EXCEPTION (hum alag alag errors ko alag alag handle akr sakte hai)   
try:
    num = int(input("enter number"))

except ValueError:    
    print("please enter numbers only") 



#MULTIPLE EXCEPTIONS 
try:
    a = int(input("enter A: "))
    b = int(input("enter B: "))

    print(a/b) 

except ValueError:
    print("invalid number")

except ZeroDivisionError:
    print("cannot Divide By Zero") 



#FINALLY BLOCK (hamesha execute hota chae error aaye tab bhi execute hota hai)
try:
    print(10/2)

except:
    print("error")

finally:
    print("program finished")



#ELSE BLOCK (agar error nahi aati to else block execute hota hai)
try:
    num = int(input("enter number: "))

except ValueError:
    print("invalid input") 

else:                #ye block tab chalta hai jab try block bina kisi error ke successfully run ho jata hai, to uske sath ye else block run hota hai.
    print("you entered", num)



#Safe Division project 01
try:
    age = int(input("enter age: "))
    print("age",age)

except ValueError:
    print("plaese enter valid age")



#Safe Division Project 02
try:
    a = int(input("enter first number:"))        
    b = int(input("enter second number:"))

except ZeroDivisionError:
    print("division by zero not allowed")

except ValueError:
    print("invalid input")



#safe percentage calculator project 03        
try:
    marks = int(input("Enter Marks: "))

    percentage = (marks / 500) * 100

    print("Percentage:", percentage)

except ValueError:
    print("Please Enter Numeric Marks")




#Name Checker project 04
try:
    name = input("Enter Name: ")

    if name == "":     #ye check karta hai ki user ne bina kuch likhe seedha enter toh nahi kar diya.
        raise ValueError  #agr user ne naam nahi daala or input khali hai ,to code khud se ValueError dega

    print("Welcome", name) #agar user ne sahi naam dala to ye code exceute ho jaiga.

except ValueError:         #ye jaise hi ValueError aaiga to ye usko acces(pakad) leta hai or niche wali line print kar deta hai.
    print("Name Cannot Be Empty")







#Final project- safe calculator 
try:

    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    operation = input("Enter (+,-,*,/): ")

    if operation == "+":
        print("Result:", a + b)

    elif operation == "-":
        print("Result:", a - b)

    elif operation == "*":
        print("Result:", a * b)

    elif operation == "/":
        print("Result:", a / b)

    else:
        print("Invalid Operator")

except ValueError:
    print("Please Enter Valid Numbers")

except ZeroDivisionError:
    print("Cannot Divide By Zero")

finally:
    print("Calculator Closed")    

    




#safe square calculator project

try:
    num = float(input("Enter a number to find its square: "))
    
    square = num ** 2     #Square calculate karke print karna
    print("Result: Square of", num, "is", square)

except ValueError:
    # Agar user number ki jagah koi text ya galat value daal de
    print("Error: Please enter a valid number only!")

finally:
    # Ye block hamesha chalega
    print("Calculator Closed")  



                                         