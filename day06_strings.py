name = "Rajat Kumar"

print(name)



name = "Python"#string indexing

print(name[0])
print(name[1])
print(name[2])


name = "Python" #negative indexing

print(name[-1])
print(name[-2])


name = "Data Science" #string slicing

print(name[0:4])
print(name[5:12])

print(name[:])
print(name[:4])



name = "rajat"#upper

print(name.upper())



name = "PYTHON"#lower

print(name.lower())



name = "rajat kumar"#title

print(name.title())



name = "   Rajat   " #strip

print(name.strip())



text = "I love Java" #replace

print(text.replace("Java", "Python"))



text = "Data Science" #find

print(text.find("Science"))


text = "banana" #count

print(text.count("a"))



name = "Ireland" #length

print(len(name))


text = "Python,SQL,Power BI" #split

print(text.split(","))


name = input("Enter your name: ")#name formatter project

print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())


email = input("Enter your email: ")#Email checker

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")



sentence = input("Enter a sentence: ") #word counter

words = sentence.split()

print("Total Words:", len(words))   