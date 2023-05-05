import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game = [rock, paper, scissors]




user_choice = input("Enter your choice\n> ").lower()
# print(user_choice)
if user_choice == "paper":
    print(f"You choose: {user_choice}")
    computer_choice = random.choice(game)
    print(F"Computer choice: {computer_choice}")
    if computer_choice == paper:
      print("it is a tie")
    elif computer_choice == rock:
      print("you win")
    elif computer_choice == scissors:
      print("computer win")

elif user_choice == "scissors":
    print(f"You choose: {scissors}")
    computer_choice = random.choice(game)
    print(F"Computer choice: {computer_choice}")
    if computer_choice == scissors:
      print("it is a tie")
    elif computer_choice == rock:
      print("computer win")
    elif computer_choice == paper:
      print("you win")   

elif user_choice == "rock":
    print(f"You choose: {rock}")
    computer_choice = random.choice(game)
    print(F"Computer choice: {computer_choice}")
    if computer_choice == rock:
      print("it is a tie")
    elif computer_choice == paper:
      print("computer win")
    elif computer_choice == scissors:
      print("you win") 
else:
   print("You entered an invalid code")