student = ["rajat",21,"CSE"]#tuple ,jisko banane ke baad uski values ko change nahi kiya ja sakta
print(student)


student = ("rajat",21,'CSE')#tuple indexing
print(student[0])
print(student[1])


student = ('rajat',21,'CSE')#tuple length
print(len(student))


numbers = {10,23,45,12,34,10} #set, ye duplicate values ko khud remove karta hai
print(numbers)


numbers = {10,20,10,30} #values add karne ke liye set me 
numbers.add(40)
print(numbers)


numbers = {10,20,30}#value remove larne ke liye
numbers.remove(20)
print(numbers)


a ={1,2,3,4}#do sets ko jodna
b ={3,5,7,2}
print(a.union(b))


a ={1,2,3,4}# do sets ka intersect karna
b ={3,5,7,2}
print(a.intersection(b))



student= {           #Dictionary values
    'name': "rajat",
    "age": 21,
    'branch': "CSE"
}
print(student)

print(student["name"]) #only student name print karne ke liye
print(student["age"])  #only student age print karne ke liye


student= {           
    'name': "rajat",
    "age": 21,
    'branch': "CSE"
}
student['cgpa']= 7.0  #new value add karne ke liye
print(student)



student= {           #value update kARNE KE liye
    'name': "rajat",
    "age": 21,
    'branch': "CSE"
}
student["age"]=23 
print(student)



student= {           #value remove karne ke liye
    'name': "rajat",
    "age": 21,
    'branch': "CSE"
}
student.pop("age")
print(student)



student= {           #keys values nikalne ke liye
    'name': "rajat",
    "age": 21,
    'branch': "CSE"
}
print(student.keys())

print(student.values()) #values print karne ke liye
print(student.items()) #items


employee = {     #employee database
    "id":101,
    "name":'RIYA',
    'salary': 50000
}
print(employee)




technologies = {    #favourite Technologies
    'language': 'python',
    "database": "SQL",
    "tool": "POWER BI"
}
print(technologies)




student = ("rajat",21,'CSE')#last element print karo
print(student[-1])




student= {           #user se input leakr dictionary me store karna
    'name': str(input("enter a name: ")),
    "age": int(input("enter age: ")),
    'branch': str(input("enter branch: "))
}       
print(student)



#jab hum API se data nikalte hai to wo JSON Format me hota hai or JSON real me dictionary jaisa hi hota hai.
# Dictionary achhe se samaj aane per API, Web scrapping, Data Engineering,Machine Learning sikhna kafi easy ho jayga.
