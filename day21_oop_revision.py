class Student: #calss
    pass



class Student:  #object
    pass

student1 = Student()



class Student:   #attributes

    name = "Rajat"
    course = "Data Science"

student1 = Student()

print(student1.name)
print(student1.course)




class Student:   #methods

    def welcome(self):
        print("Welcome Student")

student1 = Student()

student1.welcome()




class Student:    #constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rajat", 21)

print(student1.name)
print(student1.age)




class Person:    #inheritance

    def welcome(self):
        print("Welcome")

class Student(Person):
    pass

student1 = Student()

student1.welcome()




class Student:      #student class project 01

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

student1 = Student("Rajat")

student1.display()




class Teacher: #teacher class project 02

    def __init__(self, subject):
        self.subject = subject

    def show(self):
        print("Subject:", self.subject)

teacher1 = Teacher("Python")

teacher1.show()




class Employee:       #employee class project 03

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

emp1 = Employee("Rohan", 50000)

emp1.display()




class Person:      #inheritance example project 04

    def show(self):
        print("I am Person")

class Student(Person):
    pass

s1 = Student()

s1.show()




class Person:     #Final project- school management system 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def __init__(self, name, age, percentage):
        super().__init__(name, age)
        self.percentage = percentage

    def display_student(self):
        self.display_person()
        print("Percentage:", self.percentage)


student1 = Student("Rajat", 21, 82)

student1.display_student()






#Advanced multiple students project
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, percentage):
        super().__init__(name, age)
        self.percentage = percentage

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)


student1 = Student("Rajat", 21, 82)
student2 = Student("Amit", 22, 78)

student1.display()

print()

student2.display()