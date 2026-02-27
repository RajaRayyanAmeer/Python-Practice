print("Challenge 20:")
name1 = input("Enter your First Name: ")
length = len(name1)
print(length)
print("\n")

print("Challenge 21:")
firstName = input("Enter your First Name: ")
surName = input("Enter your SurName: ")
name0 = firstName + " " + surName
length = len(name0)
print(name0)
print(length)
print("\n")

print("Challenge 22:")
first_name = input("Enter your First Name in LowerCase: ")
sur_name = input("Enter your Sur Name in LowerCase: ")
first_name = first_name.title()
sur_name = sur_name.title()
name11 = first_name + " " + sur_name
print(name11)
print("\n")

print("Challenge 23:")
phrase = input("Enter the 1st Line of a Nursery Rhyme: ")
length0 = len(phrase)
print("This has", length0, "letters in it")
start = int(input("Enter a Starting Point: "))
end = int(input("Enter a End Point: "))
part = (phrase[start:end])
print(part)
print("\n")

print("Challenge 24:")
word = input("Enter a Word: ")
word = word.upper()
print(word)
print("\n")

print("Challenge 25:")
name12 = input("Enter your 1st Name: ")
if len(name) < 5:
    _sur_name = input("Enter your Sur Name: ")
    name12 = name12 + _sur_name
    print(name.upper())
else:
    print(name.lower())
print("\n")

print("Challenge 26:")
word1 = input("Please Enter a Word: ")
first = word1[0]
length2 = len(word1)
rest = word1[1:length2]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())
print("\n")