"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400246"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says... ")
fortune: int = int(randint(1, 4))

if fortune == 1:
    print("You will find love soon.")
else:
    if fortune == 2:
        print("The month will be boring.")
    else: 
        if fortune == 3:
            print("The day will be full of chaos.")
        else: 
            print("There will be misfortune in your year.")
print("Now, go spread positive vibes!")