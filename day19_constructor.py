#Constructor ek special method hota hai , jo object bante hi automatically execute ho jata hai

class car:

   def __init__(self):
      print("constructor Called")

my_car = car() #object bante hi constructor khud hi chalne lagta hai



#__init__ , python me constructor ka naam hamesha ye hi hota hai.



#instance variable
class Student:
   def __init__(self):           
      self.name = "rajat"
      self.age = "21"

student1 = Student()

print(student1.name)
print(student1.age)


#dynamic objects
class Student:
   def __init__ (self,name,age):
      self.name = name
      self.age = age

student1 = Student("rajat",23)
print(student1.name)
print(student1.age)


#Multiple Objects
class Student:

   def __init__(self,name,course):
      self.name = name
      self.course = course

student1 = Student("rajat",'DS')
student2 = Student("Amit",'BA')

print(student1.name)
print(student2.name)
print(student1.course)



# Method + Constructor
class Student:

   def __init__(self,name,age):
      self.name = name
      self.age = age

   def display(self):
      print("name:", self.name)
      print("age:", self.age)

student1 = Student("rajat",21)
student1.display()

#Student Informationden Project 01
class Student:

   def __init__(self,name,percentage):
      self.name = name
      self.percentage = percentage

student1 = Student("rajat",82)

print(student1.name)
print(student1.percentage)



#Employee Information Project 02
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Rohan", 50000)

print(emp1.name)
print(emp1.salary)




#Student display system project 03
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Rajat", 21)

student1.display()



#Final student object manager project
class Student:

    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

student1 = Student("Rajat", 21, 82)
student2 = Student("Amit", 22, 78)

student1.display()
print()  #ye beech me ek gap bana dega taki dono ka output saaf dikhe
student2.display()






