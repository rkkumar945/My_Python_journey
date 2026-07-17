age = 20 #and operator dono codition true ho to eligible print hoga agar ek bhi false hai to eligible print nahi hoga.
citizen =True
if age >=18 and citizen:
    print("eligible")



    marks = 95
    sports = True#agar ek bhi true condition hai to code run hoga 

    if marks>=90 or sports:
        print("eligible for scholarship")


is_logged_in = False#true ko false or false ko true bana deti hai,ye operator value ko ulta(reverse) kar deta hai

if not is_logged_in:
    print("please login")

    age = int(input("enter your age: "))#nested 

    if age>= 18:
        license = input("do you have driving license? (yes/no): ")
        if license =="yes":
            print("you can drive.")
        else:
            print("get a driving license first.")
    else:
        print("you are under 18.")


password = input("enter password: ")#password checker machine project

if password == "python123":
    print("login successful")
else:
    print("wrong password")



salary = int(input("enter your salary: "))
if salary>=5000:
    print("high salary")
else:
    print("normal salary")    

num1 = int(input("enter a number:"))#gretest number find karna
num2 = int(input("enter a number:"))
num3 = int(input("enter a number:"))
if num1>= num2 and num1>= num3:
    print("greatest number i: ",num1)
elif num2>=num1 and num2>=num3:
    print("greatest number is: ",num2)
else:
    print("greatest number is: ",num3)


grade = int(input("enter your grade: "))#grade dena
if  grade>=90:
 print("A+")
elif grade>=80:
 print("A")
elif grade>=70:
 print("B")
else:
 print("pass")   


