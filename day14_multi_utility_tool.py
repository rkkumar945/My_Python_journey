#percentage calculator
def percentage (total_marks,obtained_marks):
    #return(obtained_marks/total_marks)*100

print(percentage(500,425))




#FINAL MULTI UTILITY TOOL
user_choice = int(input(
    """
1.Addition
2.percentage
3.Even/odd
4.Square

Enter Choice:
"""
))

def add(a,b):
    return a+b

def percentage (total,obtained):
    return (obtained/total)*100

def check(num):
    if num % 2 == 0:
         return "Even"
    return "odd"

def square(num):
    return num*num

if user_choice == 1:
    a = int(input("enter first marks: "))
    b = int(input("enter second marks: "))
    print("result: ",add(a,b))

elif user_choice == 2:
    total = int(input("enter total marks: "))
    obtained = int(input("enter obtained marks: "))
    print("percentage: ",percentage(total,obtained))


elif user_choice == 3:
    num = int(input("enter number: "))
    print(check(num))


elif user_choice == 4:
    num = int(input("enter number: "))
    print("square: ",square(num))


else:
    print("invalid choice")    
