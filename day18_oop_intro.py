#OOP ek programming karne ka tarika hai , jisme hum real-world objects ko code me represent karte hai
# example= car,student,mobile etc. 
# Properties(Attributes)
# Actions(Methods) 
#ex. jaise student:- name,age,course iska attribute ho gya or study(),Attend_Class() iske Methods hai.

#Class- ek blueprint hai, class object banane ka blueprint hai

class Student:  #class ek keyword hai or student class ka naam hai (class ke naam ka pehla letter capital hota hai)
    pass        #agar hum abhi class me kuch bhi add nahi kiya hai to pass keyword likh dete hai taki error na aaye

s1 = Student()  #s1= ye ek object hai jo student class se bana hai , isko "Instance banana" kehte hai matlab class 
print(s1)       



#Attributes (object ki information store karte hai)
class Student:
    name = "Rajat"
    profession = "data scientist"

student_1 = Student()
print(student_1.profession) 
print(student_1.name)  


#Multiple objects
class Student:
    name = "rajat"

student1 = Student()
student2 = Student()

print(student1.name)
print(student2.name)



#Methods (is class ke andar functions hote hai)
class Student:
    def welcome(self):       #function
        print("welcome student")

student1 = Student()
student1.welcome()




#self (class ke method me pehla parameter hamesha self hota hai )
class Student:

    def show(self):    
        print("hello")

student = Student()
student.show()




# hume self ke sath kuch or parameter add karke 
class Student:

    def show(self,name):    
        print("hello",name)

student = Student()
student.show("rajat")


# Student Information project01
class Student:

      name = 'rajat kumar'
      age = 21

student1 = Student()
print(student1.name)
print(student1.age)


#college information project02
class College:
    college_name = "AKTU"

    def show(self):
        print(self.college_name)

college = College()
college.show()


#Employee Information 03
class Employee:
    company = "Google"

    def RK(self):
        print("company",self.company)

emp = Employee()

emp.RK()



#Simple Calculator Class project 04
class Calculator:
    def add(self,a,b):
        return a+b
calc = Calculator()
print(calc.add(10,25))



#Student class system 
class Student:

    name = "Rajat"
    percentage = 89

    def show_details(self):
        print("name:",self.name)
        print("percentage",self.percentage)

student1 = Student()
student1.show_details()



