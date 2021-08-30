"""Exercise to learn inputting numbers."""

__author__ = "730400246"

side_1: str = input("Left-hand side: ")
side_2: str = input("Right-hand side: ")
side_11 = side_1
side_11 = (int(side_11))
side_22 = side_2
side_22 = (int(side_22))
formula_1 = (int(side_11) ** int(side_22))
formula_1 = str(formula_1)
word_1 = str(side_11) + " ** " + str(side_22) + " is "
formula_2 = (int(side_11) / int(side_22))
formula_2 = str(formula_2)
word_2 = str(side_11) + " / " + str(side_22) + " is "
formula_3 = (int(side_11) // int(side_22))
formula_3 = str(formula_3)
word_3 = str(side_11) + " // " + str(side_22) + " is "
formula_4 = (int(side_11) % int(side_22))
formula_4 = str(formula_4)
word_4 = str(side_11) + " % " + str(side_22) + " is "
print(word_1 + formula_1)
print(word_2 + formula_2)
print(word_3 + formula_3)
print(word_4 + formula_4)
