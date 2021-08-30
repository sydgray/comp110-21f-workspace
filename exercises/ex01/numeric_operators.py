"""Exercise to learn inputting numbers"""

__author__ = "730400246"

side1: str = input("Left-hand side: ")
side2: str = input("Right-hand side: ")
side11 = side1
side11 = (int(side11))
side22 = side2
side22 = (int(side22))
formula1 = (int(side11) ** int(side22))
formula1 = str(formula1)
word1 = str(side11) + " ** " + str(side22) + " is "
formula2 = (int(side11) / int(side22))
formula2 = str(formula2)
word2 = str(side11) + " / " + str(side22) + " is "
formula3 = (int(side11) // int(side22))
formula3 = str(formula3)
word3 = str(side11) + " // " + str(side22) + " is "
formula4 = (int(side11) % int(side22))
formula4 = str(formula4)
word4 = str(side11) + " % " + str(side22) + " is "
print(word1 + formula1)
print(word2 + formula2)
print(word3 + formula3)
print(word4 + formula4)
