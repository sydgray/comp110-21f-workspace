from random import randint
"""Which Nicktoon are you quiz"""
__author__ = "730400246"

CHARACTER_EMOJI: str = str("\U000FEB15")
CHARACTER_EMOJI2: str = str("\U0001f499")
CHARACTER_EMOJI3: str = str("\U0001F49C")
CHARACTER_EMOJI4: str = str("\U0001F496")


def main() -> None:
    player: str = str(greet())
    print("1: Resume")
    print("2: Quit")
    print("3: Character Quote")
    a: int = int(input("Continue? "))
    points: int = int(0)
    message: int = int(randint(1, 4))
    if a == 1:
        points: int = int(0)
        questions(1, points, player)
        print(f"{ player }, what is your favorite color? ")
        answer: str = str(input(""))
        if answer == "A":
            points = points + 1
            print(f"points: { points }")
        else:
            if answer == "B":
                points = points * -1
                print(f"points: { points }")
            else:
                if answer == "C":
                    points = points + 3
                    print(f"points: { points }")
                else:
                    if answer == "D":
                        points = points + 4
                        print(f"points: { points }")
        resume(points)
        questions(2, points, player)
        print(f"{ player }, what is your favorite place to be? ")
        answer: str = str(input(""))
        if answer == "A":
            points = points + 1
            print(f"points: { points }")
        else:
            if answer == "B":
                points = points * -1
                print(f"points: { points }")
            else:
                if answer == "C":
                    points = points + 3
                    print(f"points: { points }")
                else:
                    if answer == "D":
                        points = points + 4
                        print(f"points: { points }")
        resume(points)
        questions(3, points, player)
        print(f"{ player }, what is your favorite animal? ")
        answer: str = str(input(""))
        if answer == "A":
            points = points + 1
            print(f"points: { points }")
        else:
            if answer == "B":
                points = points * -1
                print(f"points: { points }")
            else:
                if answer == "C":
                    points = points + 3
                    print(f"points: { points }")
                else:
                    if answer == "D":
                        points = points + 4
                        print(f"points: { points }")
        resume(points)
        questions(4, points, player)
        print(f"{ player }, what is your personality like? ")
        answer: str = str(input(""))
        if answer == "A":
            points = points + 1
            print(f"points: { points }")
        else:
            if answer == "B":
                points = points + 2
                print(f"points: { points }")
            else:
                if answer == "C":
                    points = points * -1
                    print(f"points: { points }")
                else:
                    if answer == "D":
                        points = points + 4
                        print(f"points: { points }")
        character_assign(points)
    else:
        if a == 2:
            print(f"points: { points }")
            goodbye()
        else:
            if a == 3:
                if message == 1:
                    print("BA-AH-AH-AH-HA")
                else:
                    if message == 2:
                        print("Grandpa...")
                    else: 
                        if message == 3:
                            print("A baby's gotta do what a baby's gotta do!")
                        else: 
                            print("I wish...")


def questions(b: int, c: int, f: str) -> int:
    i: int = 1
    while i < 5:
        if b == 1:
            print("A. Yellow")
            print("B. Blue")
            print("C. Purple")
            print("D. Pink")
        else:
            if b == 2:
                print("A. Ocean")
                print("B. Cities")
                print("C. Backyard")
                print("D. Home")
            else:
                if b == 3:
                    print("A. Snail")
                    print("B. Pig")
                    print("C. Dog")
                    print("D. Fish")
                else:
                    if b == 4:
                        print("A. Hyper")
                        print("B. Wise")
                        print("C. Adventurous")
                        print("D. Imaginative")
        print(f"{ f }'s points: { c }")
        i = i + 5
    return b
        

def greet() -> str:
    player: str = input("What is your name? ")
    print(f"Welcome { player }, this is the which Nicktoon are you quiz! Please type all answers in caps lock :)")
    return player


def character_assign(c: int) -> None:
    if c < 11:
        print(f"You're Spongebob Squarepants! { CHARACTER_EMOJI }")
    else:
        if c < 0:
            print(f"You're Arnold! { CHARACTER_EMOJI2 }")
        else:
            if 12 < c < 15:
                print(f"You're Tommy Pickles! { CHARACTER_EMOJI3 }")
            else:
                print(f"You're Timmy Turner! { CHARACTER_EMOJI4 }")


def goodbye() -> None:
    message: int = int(randint(1, 4))

    if message == 1:
        print("Hope you had fun!")
    else:
        if message == 2:
            print("Bye!!!")
        else: 
            if message == 3:
                print("Thanks for playing!")
            else: 
                print("Play again!")


def resume(d: int) -> None:
    print("1: Resume")
    print("2: Quit")
    print("3: Character Quote")
    a: int = int(input("Continue? "))
    if a == 2:
        print(f"points: { d }")
        goodbye()
    else:
        message: int = int(randint(1, 4))
        if a == 3:
            if message == 1:
                print("BA-AH-AH-AH-HA")
            else:
                if message == 2:
                    print("Grandpa...")
                else: 
                    if message == 3:
                        print("A baby's gotta do what a baby's gotta do!")
                    else: 
                        print("I wish...")


if __name__ == "__main__":
    main()