print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
''')
print("Hello Player Welcome to Treasure island, your mission is to find the hidden treasure")
begin = input("Are you ready to begin your search? Yes or No\n").lower()
if begin == "yes":
    print("Perfect! head to the Entry to start your search")
elif begin == "no":
    print("please take the exit")
    exit()
else:
    print("invalid entry, try again")
    exit() 
first_stage = input("what direction will you take? Right or Left\n").lower()
if first_stage == "right":
    print("Congrats! Welcome to the next stage")
else:
    print("Sorry! Game over")
    exit()
second_stage = input("Where do you go next? Up or Down\n").lower()
if second_stage == "down":
    print("Congrats! Welcome to the next stage")
else:
    print("Sorry! Game over")
    exit()

third_stage = int(input("choose a number between 1 and 2\n"))
if third_stage == 2:
    print("Congrats! Welcome to the next stage")
else:
    print("Sorry! Game over")
    exit()

fourth_stage = input("choose between swim and walk\n").lower()
if fourth_stage == "walk":
    print("Congrats! Welcome to the next stage")
else:
    print("Sorry! Game over")
    exit()

fifth_stage = input("choose a colour between green, blue and red\n").lower()
if fifth_stage == "green":
    print("Congrats! You win")
elif fifth_stage == "blue":
    print("oops! You have one more chance")
    one_more_chance = input("choose the right colour to win")
    if one_more_chance == "green":
        print("Congrats! You win")
    else:
        print("Sorry! Game over")
        exit()
else:
    print("Sorry! Game over")
    exit() 





