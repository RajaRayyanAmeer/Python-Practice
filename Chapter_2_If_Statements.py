print("Challenge 12:")
num001 = float(input("Enter 1st Number: "))
num002 = float(input("Enter 2nd Number: "))
if num001 > num002:
    print(num002, num001)
else:
    print(num001,num002)
print("\n")

print("Challenge 13:")
num = float(input("Enter a Value less than 20: "))
if num >= 20:
    print("Too High.")
else:
    print("Thank You.")
print("\n")

print("Challenge 14:")
num0 = float(input("Enter a Value between 10 and 20: "))
if num0 >= 10 and num0 <= 20:
    print("Thank You")
else:
    print("Incorrect Answer")
print("\n")

print("Challenge 15:")
color = input("Type in your Favourite Color: ")
if color == "Red" or color == "RED" or color == "red":
    print("I like Red too!")
else:
    print("I don't like that colour, I prefer Red.")
print("\n")

print("Challenge 16:")
raining = input("Is it Raining? ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy?")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an Umberalla.")
    else:
        print("Take an Umberalla.")
else:
    print("Enjoy your Day")
print("\n")

print("Challenge 17:")
age1 = int(input("What is your age?"))
if age >= 18:
    print("You can Vote")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")
print("\n")

print("Challenge 18:")
num00 = float(input("Enter a Number: "))
if num00 < 10:
    print("Too Low")
elif num00 >= 10 and num <= 20:
    print("Correct")
else:
    print("Too High")
print("\n")

print("Challenge 19:")
num000 = input("Enter 1, 2, or 3: ")
if num000 == "1":
    print("Thank You")
elif num000 == "2":
    print("Well Done")
elif num000 == "3":
    print("Correct")
else:
    print("Error Message")
print("\n")