age = 20 #if

if age >= 18:
    print("You are eligible to vote.")



age = int(input("Enter your age: ")) #if-else

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")



marks = int(input("Enter your marks: ")) #if-elif-else

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")    




age = 20 #and operator
citizen = True

if age >= 18 and citizen:
    print("Eligible")   



marks = 95 #or operator
sports = True

if marks >= 90 or sports:
    print("Scholarship Eligible")



is_logged_in = False#not operator

if not is_logged_in:
    print("Please Login") 



age = int(input("Enter your age: "))#nested if

if age >= 18:
    license = input("Do you have a driving license? (yes/no): ")

    if license == "yes":
        print("You can drive.")
    else:
        print("Get a driving license first.")
else:
    print("You are under 18.")  




num = int(input("Enter a number: "))#even or odd

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")   




password = input("Enter password: ")#password checker project

if password == "Python123":
    print("Login Successful")
else:
    print("Wrong Password") 




salary = float(input("enter your salary: "))

if salary >= 50000:
    print("High Salary")
else:
    print("Normal Salary")



num1 = float(input("enter first number: "))#largest number
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))

largest = max(num1, num2, num3)
print("largest number is": largest)   




percentage = float(input("enter your percentage: "))

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")