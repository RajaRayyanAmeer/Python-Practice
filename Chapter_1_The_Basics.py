print("Challenge 1:")
firstname = input("Please Enter your Name: ")
print("Hi!",firstname)
print("\n")

print("Challenge 2:")
firstname1 = input("Enter your First Name: ")
surname = input("Enter your Surname: ")
print("Hi!",firstname,surname)
print("\n")

print("Challenge 3:")
print("What do you call a bear with no teeth?\nA Gummy Bear!")
print("\n")

print("Challenge 4:")
num1 = float(input("Enter your 1st Number: "))
num2 = float(input("Enter your 2nd Number: "))
answer = num1 + num2
print("The Answer is:",answer)
print("\n")

print("Challenge 5:")
num01 = float(input("Enter your 1st Number: "))
num02 = float(input("Enter your 2nd Number: "))
num03 = float(input("Enter your 3rd Number: "))
answer1 = (num01 + num02) * num03
print("The Answer is:",answer1)
print("\n")

print("Challenge 6:")
startNum = int(input("Enter the number of slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
slicesleft = startNum - endNum
print("You have ",slicesleft," slices remaining.")
print("\n")

print("Challenge 7:")
name = input("What is your Name? ")
age = int(input("How old are you? "))
newAge = age + 1
print(name,"next birthday you will be", newAge)
print("\n")

print("Challenge 8:")
bill = float(input("What is the total cost of the Bill? "))
people = int(input("How many people are there? "))
each = bill/people
print("Bill Division, Each Person: PKR", each)
print("\n")

print("Challenge 9:")
days = int(input("Enter the Number of Days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In ",days," days there are ",hours, " hours ",minutes," minutes ",seconds," seconds.")
print("\n")

print("Challenge 10:")
kilo = float(input("Enter the Number of Kilos: "))
pound = kilo * 2.204
print("That is",pound,"Pounds.")
print("\n")

print("Challenge 11:")
larger = float(input("Enter a Number over 100: "))
smaller = float(input("Enter a Number under 100: "))
answer = larger/smaller
print(smaller," goes into ",larger," ",answer," times")
print("\n")