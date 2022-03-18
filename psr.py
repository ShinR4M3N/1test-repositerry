your_name = input("your name ")
game = input("do you want to play a game (Y/N) ")
scoreboard_1 = 0
scoreboard_2 = 0
import random
item = 3
number = random.randint(0,2)
if game == "Y":


    while item > 0:
        your_pick = int(input("would you like to pick sci (1) rock (0) or paper (2) "))
        if your_pick == number:
            print(f"opponent's move:{number} your move:{your_pick} draw try again")
            item += 1



        elif your_pick == 0 and number == 1:
            print(f"opponent's move:{number} your move:{your_pick} you win")
            scoreboard_1 += 1
        elif your_pick == 0 and number == 2:
            print(f"opponent's move:{number} your move:{your_pick} you lose")
            scoreboard_2 += 1
        elif your_pick == 1 and number == 0:
            print(f"opponent's move:{number} your move:{your_pick} you lose")
            scoreboard_2 += 1
        elif your_pick == 1 and number == 2:
            print(f"opponent's move:{number} your move:{your_pick} you win")
            scoreboard_1 += 1
        elif your_pick ==2 and number == 0:
            print(f"opponent's move:{number} your move:{your_pick} you win")
            scoreboard_1 += 1
        elif your_pick ==2 and number == 1:
            print(f"opponent's move:{number} your move:{your_pick} you lose")
            scoreboard_2 += 1
        else:
            print("wrong number try again")
            item += 1
        item -= 1
    print(f"your scoreboard: {scoreboard_1} opponent's scoreboard: {scoreboard_2}")
    if scoreboard_1 > scoreboard_2:
        print(f"{your_name} you win")
    else:
        print(f"{your_name} you lose")
else:
    print("goodbye")









