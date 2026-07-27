#Module ek file hoti hai jisme functions ,variables,ya classes ya koi code hota hai , jis se programming or projects banane asan ho jate hai.
#examle= agar hamare pass (calculator.py) naam ki koi pytohn file hai to usko hum module keh sakte hai.
#USES = code reusability , easy maintenance, 

#CUSTOM MODULE, maan lo hamare pass ek file(calculator.py) hai jisme humne koi function ya code banaya hua hai jo moi task perform karta hai
#ab jo task calculator.py file perform karti hai usi same task ko hume is file(day17_modules.py) me perform karna hai to hum us file ko import kar lenge.

import calculator
print(calculator.add(10,5))

print(calculator.substract(10,4))


#IMPORT STATEMENT
import math     #(math) python ka built in function(module) hai jo is math module se jude sare works jaise sqrt,trigonometry,logarthim etc. kaam karta hai 
print(math.sqrt(25))



#from...import
from math import sqrt  #agar humko poore math module ki need nahi hai balki keval math ke sqrt wale function ki jarurat hai to hum keval math module ke sqrt function ko hi file me import karega poore module ko nahi
print(sqrt(36))


#Multiple functions import
#jab hume kisi modules ke ek se jyada function ki need hoti hai to hum comma(,) lagakar functions ke naam likh dete hai
from math import sqrt, pow
print(sqrt(49))
print(pow(2,3))



#BUILT IN MODULES(FUNCTION), jo python environment me pehle se hi available hai
#math module
import math
print(math.pi)


#Random module, har baar alag result dega
import random
print(random.randint(1,10))


#Datetime Module
from datetime import date
print(date.today())


#Module Alies , agar hume kisi module ka naam chota karna ho to , hum ye niche wala code ki tarah kar sakte hai
import math as m
print(m.sqrt(64))


#My calculator module project 01
import mycalculator        #mycalculator.py file ko import karke uske andar ke function ko use kiya

print(mycalculator.add(10,12))
print(mycalculator.multiply(10,2))



#Area module project 02
import area             #area.py file ko import kiya
print(area.circle_area(5))



#greeting module project 03
import greeting
print(greeting.welcome(" rajat"))



#Final project- utility package
import utility

print(utility.square(5))
print(utility.cube(5))
print(utility.even_odd(5))





