# this is Number guessing game :
from random import randint

print("\u2764\uFE0F""\u2764\uFE0F""\u2764\uFE0F""This Is Number Guessing Game (::)""\u2764\uFE0F""\u2764\uFE0F""\u2764\uFE0F")

GREEN = "\033[0;32m"
END = "\033[0m"

for x in range(6):
    guessing_number=int(input("Enter Your Guessing Number 1-10 : "))
    random_number=randint(1,10)

    if guessing_number==random_number:
        print( GREEN +"You Have Won " +'\u2713' + END)
        print()
    else:
        print("You Have Lost Level ")
        print("Correct Answer Is : ",random_number)
        print()

"""
Code By SHUVO KUMAR SAHAQ
Student Of Chapainawabganj Polytechnic Institute
"""