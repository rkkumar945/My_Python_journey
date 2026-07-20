# modules ek python file hoti hai jisme pehle se likhe hue functions or tools hote hai , 
#inka use karke hum apna kaam easy kar sakte hai
#ex: math calculations, random numbers, date & time, file handling

import math  #module ko use karne ke liye import ka use karte hai
print(math.sqrt(25))


import math  #mathematical operations ke liye math module ka use hota hai
print(math.sqrt(64))


import math # power calculate karta hai isme 2 ki power 5 ko calculate kiya
print(math.pow(2,5))


import math  #jo poora number hoga usko print karta hai, 4.3 ye 5 ke equally hai to print 5 hoga
print(math.ceil(4.3))


import math   #jo number point me uski niche wali value dega, 4.9 hai to 4 value print hogi 
print(math.floor(4.9))


import math # pi value 
print(math.pi)


import random  #random module,random data generate karne ke liye, har bar alag aata hai
print(random.randint(1,10))



import random
fruits = ['apple','fig','peer']
print(random.choice(fruits))


#Datetime module, date and time handle karne ke liye
from datetime import datetime
now = datetime.now()
print(now)


from datetime import date #current date print karne ke liye
today = date.today()
print(today)


import math  # user se number lekar sqrt nikalna
number = int(input("enter a number: "))
print("sqrt= ",math.sqrt(number))



import random  # dice simulator,direct print karne se pehle isko dice variable me daal diya,or phir dice ko print kiya
dice = random.randint(1,7)
print(dice)


import random # simple password generator project
digits = "0123456789"

password = " "
for i in range(6):
    password += random.choice(digits)

print("password:",password)    



#OTP generator project
import random 
digits = "0123456789"

OTP = " "
for i in range(4):
    OTP += random.choice(digits)

print("OTP:",OTP)   

