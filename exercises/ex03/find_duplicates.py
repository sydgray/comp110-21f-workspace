"""Finding duplicate letters in a word."""

__author__ = "730400246"


word: str = (input("Enter a word: "))
dup: str = "Found duplicate: True"
dup2: str = "Found duplicate: False"
i: int = 0
while i < len(word):
    j: int = i + 1
    while j < len(word):
        char = word[j]
        if char == word[i]:
            print(dup)
        else:
            if i == 1:
                print(dup2)
        j = j + 1
    i = i + 1
    