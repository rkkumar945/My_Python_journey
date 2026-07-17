for i in range(2,11,2):
    print(i)

count = 1
while count<=5:
    print(count)
    count += 1

for i in range(1,11):#break
    if i ==6:
        break
    print(i)    
       
for i in range(1,6): #continue current iteration ko skip karke next iteration oar chala jata hai
    if i ==3:
        continue
    print(i)


num = int(input("enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num * i)


total = 0

for i in range(1,11):
    total +=i
print("sum",total) 



for i in range(100,0,-1):
    print(i)

for i in range(1,51,2):
    print(i)    

for i in range(2,51,2):
    print(i)    


n = int(input("enter number (N) enter please: "))#sum of first n numbers

total = 0
for i in range(1,n+1):
    total +=i
print("i se",n,"tak ke numbers ka sum: ",total)


n = int(input("enter a number: "))#find factorial 
factorial =1

for i in range(1,n+1):
    factorial *=i
print(n,"is factorial of:",factorial)