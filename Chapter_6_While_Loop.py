print("Challenge 45:")
total0 = 0
while total0 <= 50:
    num7 = int(input("Enter a Number: "))
    total0 = total0 + num7
    print("The total is",total0)

print("Challenge 46:")
num8 = 0
while num8 <= 5:
    num8 = int(input("Enter a Number: "))
print("The Last Number you entered was a",num8)

print("Challenge 47:")
num9 = int(input("Enter a Number: "))
total1 = num9
again = "y"
while again == "y":
    num10 = int(input("Enter another Number: "))
    total1 = total1 + num10
    again = input("Do you want to add another Number? (y/n)     ")
print("The Total is",total1)

print("Challenge 48:")
again0 = "y"
count = 0
while again0 == "y":
    name5 = input("Enter a Name of somebody, that you want to invite to your Party: ")
    print(name5,"has now been invited.")
    count = count + 1
    again0 = input("Do you want to invite somebody else? (y/n)     ")
print("You have",count,"people coming to your party.")

print("Challenge 49:")
compnum = 50
guess = int(input("Can you guess the Number, I am thinking of? "))
count0 = 1
while guess != compnum:
    if guess < compnum:
        print("Too Low")
    else:
        print("Too High")
    count0 = count0 + 1
    guess = int(input("Have another Guess: "))
print("Well Done! you took",count0,"attempts")

print("Challenge 50:")
num11 = int(input("Enter a Number between 10 and 20: "))
while num11 < 10 or num11 > 20:
    if num11 < 10:
        print("Too Low")
    else:
        print("Too High")
    num11 = int(input("Try Again"))
print("Thank You")

print("Challenge 51:")
num12 = 10
while num12 > 0:
    print("There are",num12,"green bottles hanging on the wall.")
    print("If 1 Green Bottle should accidentally fall.")
    num12 = num12 - 1
    answer1 = int(input("How many Green Bottles will be hanging on the wall? "))
    if answer1 == num12:
        print("There will be",num12,"Green Bottles hanging on the wall.")
    else:
        while answer1 != num12:
            answer1 = int(input("No, Try Again"))
print("There are no more green bottles hanging on the wall.")