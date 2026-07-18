fruits = ['apple','banana','mango']

for fruit in fruits:
    print(fruit)


name = 'rajat'
for letter in name:
    print(letter) 



for i in range(3):  #nested loop
    for j in range(2):
        print(i,j)



for i in range(5):
    print("*" * (i+1))




marks = [87,45,25,5,11,65,] # marks analyzer project

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print('total marks:',total)
print('Average marks:',average)
print('highest marks:', max(marks))
print('Lowest marks:',min(marks))



marks = [87,45,25,5,11,65,] # marks analyzer project

total = 0

for mark in marks:
    total = sum(marks)

average = total / len(marks)

print('total marks:',total)
print('Average marks:',average)
print('highest marks:', max(marks))
print('Lowest marks:',min(marks))




number = int(input("enter a number: ")) # table print 
for i in range(1,11):
    print(number,"x",i,"=",number*i)



word = input("enter a word")
for letter in word:
    print(letter)



total_sum = sum(range(1,101))# 1 se 100 tak numbers ka total
print("sum is: ",total_sum)    
