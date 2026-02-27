print("Challenge 60: ")
import turtle
for a in range(0,4):
    turtle.forward(100)
    turtle.right(90)

print("Challenge 61: ")
import turtle
for b in range(0,3):
    turtle.forward(100)
    turtle.left(120)

print("Challenge 62: ")
import turtle
for c in range(0,360):
    turtle.forward(1)
    turtle.right(1)

print("Challenge 63: ")
import turtle
turtle.color("black","red")
turtle.begin_fill()
for d in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
for e in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for f in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

print("Challenge 64: ")
import turtle
for g in range(0,5):
    turtle.forward(100)
    turtle.right(144)

print("Challenge 65: ")
import turtle
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.hideturtle()

print("Challenge 66: ")
import turtle
import random
turtle.pensize(3)
for h in range(0,8):
    turtle.color(random.choice(["red","blue","yellow","pink","orange"]))
    turtle.forward(50)
    turtle.right(45)

print("Challenge 67: ")
import turtle
import random
for i in range(0,10):
    for j in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
turtle.hideturtle()

print("Challenge 68: ")
import turtle
import random
lines = random.randint(5,20)
for k in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()