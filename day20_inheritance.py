#inheritance me ek class ki properties dusri class le sakti hai.

class Person:      #parent class

    def show(self):
        print("I am a person")

class Student(Person): #child class
    pass

student = Student()
student.show()



#Inheriting Attributes
class Person:          #parent class

    def __init__(self,name):
        self.name = name

class Student(Person):         #child class
    pass

student = Student("Rajat")
print(student.name)


#Method Inheritance
class Person:

    def welcome(self):
        print("welcome")

class Student(Person):
    pass

s1 = Student()
s1.welcome()



#child class se apna method
class Person:

    def welcome(self):
        print("welcome rajat")

class Student(Person):

    def study(self):
        print("studying python")

s1 = Student()

s1.welcome()
s1.study()



#Person & Student project 01
class Person:

    def show_name(self):
        print("name: rajat")

class Student(Person):
    pass

s1 = Student()

s1.show_name()



#Employee system project 02
class Employee:

    def company(self):
        print("Google")

class Developer(Employee):

    def role(self):
        print("Python Developer")

dev = Developer()

dev.company()
dev.role()



#Employeee Management System
class Employee:                 #ek class banai Employee naam ki

    def __init__(self, name, salary):    #__init__ constructor(method) use kiya, isme jab cbhi hum Employe ka koi naya object banayenge to yeh method apne aap chal padega bina call kiye or name or salary set kar dega
        self.name = name              #self current object ko refer karta hai amtlab jo object ban raha hai uske andar data store karna hai
        self.salary = salary

    def display_employee(self):    #yeh method function hai jo employee ke naam or salary screen per print karta hai
        print("Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):   #child class banai jo parent class ko inherit kar rahi hai, matlab Devolper class ne Employee class ki sari properties or method ko inherit kar liya

    def role(self):       #yeh Developer ka apna ek naya function hai jo sirf devolper ka role print karega
        print("Role: Python Developer")

dev1 = Developer("Rajat", 60000) #yeh ek object banaya jisme dev1 object hai, kyuki devolper ke pass class nahi hai isliye yeh parent class(Employee) ke constructor ko use karega

dev1.display_employee() #ye method Employee class se call hota hai or output deta hai
dev1.role()             #ye method Devloper class se call hota hai or output deta hai

