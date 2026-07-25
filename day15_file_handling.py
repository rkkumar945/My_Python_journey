#file handling ki madad se hum data ko permanent store kar sakte hai

#file open karna
file = open("filename.txt", "w")


#file write mode(w)
file = open("notes.txt","w")#agar ye file me pehle se hai to uska purana data hat jata hai
file.write("hello ireland")
file.close()


#file close karna
file.close()



#Read mode(r)
file = open("notes.txt","r")#file ka data padhne ke liye
data = file.read()
print(data)
file.close()



#Read lines
file = open("notes.txt","r")
for line in file:
    print(line)
file.close()



#Append Mode(a), new information ko add karta hai, per purana data delete nahi karta hai
file = open("notes.txt","a")
file.write("\nwelcome rajat") #\n ka use welcome rajat ko next line print karne ke liye hai
file.close()


#ab jo ye welcome rajat add ho chuka hai isko dekne ke liye file ko dobara read karna hoga
file = open('notes.txt', 'r')
for line in file:
    print(line)
file.close()    




#is tarah se code karne per file automatically close ho jati hai, (with) statament file ko khud close kar deta hai, 
#phir humko file.close() likhne ki jarurat nahi hoti
with open('notes.txt','w') as file: #(as file) ka matlab hai ki humne khuli hui file ko file naam ke variable me store kar liya hai
    file.write('python file handling')




#simple note reader PROJECT 01
note = input("enter Note: ")
with open("note.txt",'w') as file:  #(as file) likhe hue code ko baar baar poora open fuction na likhna pade jaise ki upar humne welcome rajat add karne ke baad kiya tha, isliye hum as file likh kar us khuli hui file ko ek variable naam (file) de dete hai.
    file.write(note)
print("note saved successfully!")



#Daily journal PROJECT 02
journal = input("write today's journal: ")

with open("journal.txt",'a') as file:
    file.write(journal + "\n")

print("journal saved")   



#NOTES SAVER SYSTEM PROJECT 03
note = input("enter your note: ") #save notes through this code.

with open('notes.txt','a') as file:
    file.write(note + "\n")

print("note saved successfilly")  



#READ NOTES
with open('notes.txt','r') as file: #read notes through this code (is "r" ke jariye aap cod eko read kar sakte hai usme kuch add nahi akr sakte).
    print(file.read()) # iski help se is file me jo bhi text likha hua hai sare ko ek sath print kar dega.





#COMBINED VERSION (UPAR WALE PROJECT 03 KA)
choice = int(input("""
1. Save Note
2. Read Notes

Enter Choice:
"""))

if choice == 1:

    note = input("Enter Note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note Saved")

elif choice == 2:

    with open("notes.txt", "r") as file:
        print(file.read())

else:
    print("Invalid Choice")