print("Challenge 52:")
import random
num13 = random.randint(1,100)
print(num13)

print("Challenge 53:")
import random
fruit = random.choice(['Apple','Orange','Grape','Banana','Strawberry'])
print(fruit)

print("Challenge 54:")
import random
coin = random.choice(['h','t'])
guess0 = input("Enter (h)eads or (t)ails: ")
if guess0 == coin:
    print("You Win")
else:
    print("Bad Luck")
if coin == "h":
    print("It was Heads")
else:
    print("It was Tails")

print("Challenge 55:")
import random
num14 = random.randint(1,5)
guess1 = int(input("Enter a Number: "))
if guess1 == num14:
    print("Well Done")
elif guess1 > num14:
    print("Too High")
    guess1 = int(input("Guess Again: "))
    if guess1 == num14:
        print("Correct")
    else:
        print("You Lose")
elif guess1 < num14:
    print("Too Low")
    guess1 = int(input("Guess Again: "))
    if guess1 == num14:
        print("Correct")
    else:
        print("You Lose")

print("Challenge 56:")
import random
num15 = random.randint(1,10)
correct = False
while correct == False:
    guess2 = int(input("Enter a Number: "))
    if guess2 == num15:
        correct = True

print("Challenge 57:")
import random
num16 = random.randint(1,10)
correct0 = False
while correct0 == False:
    guess3 = int(input("Enter a Number: "))
    if guess3 == num16:
        correct0 = True
    elif guess3 > num16:
        print("Too High")
    else:
        print("Too Low")

print("Challenge 58:")
import random
score = 0
for x in range(1,6):
    num23 = random.randint(1,50)
    num20 = random.randint(1, 50)
    correct3 = num23 + num20
    print(num23,"+",num20,"=")
    ans = int(input("Your Answer: "))
    if ans == correct3:
        score = score + 1
print("You Scores",score,"out of 5")

print("Challenge 59:")
import random
color = random.choice(['red','blue','green','white','pink'])
print("Select from Red, Blue, Green, White, or Pink:")
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a Color: ")
    theirchoice = theirchoice.lower()
    if color == theirchoice:
        print("Well Done")
        tryagain = False
    else:
        if color == "red":
            print("I bet you are seeing RED right now")
        elif color == "blue":
            print("Don't feel BLUE")
        elif color == "green":
            print("I bet you are GREEN with envy right now")
        elif color == "white":
            print("Are you WHITE as a sheet, as you didn't guess correctly")
        elif color == "pink":
            print("Shame you are not feeling in the PINK, as you got it wrong")
        else:
            print("Okay")