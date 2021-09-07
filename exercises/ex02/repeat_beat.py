"""Repeating a beat in a loop."""

__author__ = "730400246"


beat: str = input("What beat do you want to repeat? ")
i: int = int(input("How many times do you want to repeat it? "))
z: int = int(i)
while i > 0:
    print((beat + " ") * i)
    i = i - (i + i)
while z <= 0:
    print("No beat...") 
    z = z * -1 + (z + 1)