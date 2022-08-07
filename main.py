import random

num = 0
print("This is a dice roller!")
inp = input("1 to roll a d6, 2 for d10, 3 for d20: ")
if inp == "1":
    num = random.randint(1,6)
elif inp == "2":
    num = random.randint(1,10)
elif inp == "3":
    num = random.randint(1,20)
else:
    print("ERROR: invalid input")

print("You rolled a:", num)
