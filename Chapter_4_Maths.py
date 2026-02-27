print("Challenge 27:")
num23 = float(input("Enter a Number with lots of Decimal Places: "))
print(num23)
print("\n")

print("Challenge 28:")
num13 = float(input("Enter a number with lots of decimal places: "))
answer = num13 * 2
print(answer)
print(round(answer,2))
print("\n")

print("Challenge 29:")
import math
num14 = float(input("Enter a Number over 500: "))
answer0 = math.sqrt(num14)
print(round(answer,2))
print("\n")

print("Challenge 30:")
import math
print(round(math.pi,5))
print("\n")

print("Challenge 31:")
import math
radius = float(input("Enter the Radius of the Circle: "))
area = math.pi * (radius ** 2)
print(area)
print("\n")

print("Challenge 32:")
import math
radius = float(input("Enter the Radius of the Circle: "))
depth = float(input("Enter Depth: "))
area = math.pi * (radius ** 2)
volume = area * depth
print(round(volume,3))
print("\n")

print("Challenge 33:")
num15 = float(input("Enter a Number: "))
num16 = float(input("Enter another Number: "))
ans = num15 // num16
ans0 = num15 % num16
print(num15," divided by ",num16," is ",ans," with ",ans0," remaining.")
print("\n")

print("Challenge 34:")
print("1. Square")
print("2. Triangle")
print()
menuselection = int(input("Enter a Number: "))
if menuselection == 1:
    side = float(input("Enter the Length of one Side: "))
    area = side * side
    print("The Area of your chosen shape is", area)
elif menuselection == 2:
    base = float(input("Enter the Length of the Base: "))
    height = float(input("Enter the Height of the Triangle: "))
    area = (base * height)/2
    print("The Area of your chosen Shape is", area)
else:
    print("Incorrect Option Selected")
print("\n")