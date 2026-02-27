print("Challenge 35:")
name = input("Type in your Name: ")
for a in range(0,3):
    print(name)

print("Challenge 36:")
name0 = input("Type in your Name: ")
number = int(input("Enter a Number: "))
for b in range(0,number):
    print(name0)

print("Challenge 37:")
name1 = input("Enter your Name: ")
for c in name1:
    print(c)

print("Challenge 38:")
num = int(input("Enter a Number: "))
name2 = input("Enter your Name: ")
for d in range(0,num):
    for e in name2:
        print(e)

print("Challenge 39:")
num0 = int(input("Enter a Number between 1 and 12: "))
for f in range(1,13):
    answer = f * num0
    print(f,"x",num0,"=",answer)

print("Challenge 40:")
num1 = int(input("Enter a Number below 50: "))
for g in range(50,num1 - 1,-1):
    print(g)

print("Challenge 41:")
name3 = input("Enter your Name: ")
num2 = int(input("Enter a Number: "))
if num2 < 10:
    for h in range(0,num2):
        print(name3)
else:
    for i in range(0,3):
        print("Too High")

print("Challenge 42:")
total = 0
for j in range(0,5):
    num3 = int(input("Enter a Number: "))
    answer0 = input("Do you want this number included? (y/n)    ")
    if answer0 == "y":
        total = total + num3
print(total)

print("Challenge 43:")
direction = input("Do you want to count up or down? (u/d)    ")
if direction == "u":
    num4 = int(input("What is the Top Number? "))
    for k in range(1,num4 + 1):
        print(k)
elif direction == "d":
    num5 = int(input("Enter a Number below 20: "))
    for l in range(20,num5 - 1,-1):
        print(l)
else:
    print("I don't understand.")

print("Challenge 44:")
num6 = int(input("How many friends do you want to invite to the Party? "))
if num6 < 10:
    for m in range(0,num6):
        name4 = input("Enter a Name: ")
        print(name4,"has been invited.")
else:
    print("Too many People.")