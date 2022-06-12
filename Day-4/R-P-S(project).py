#Instructions
#Make a rock, paper, scissors game.

#Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

#Start the game by asking the player:

#"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

#From there you will need to figure out:

#How you will store the user's input.
#How you will generate a random choice for the computer.
#How you will compare the user's and the computer's choice to determine the winner (or a draw).
#And also how you will give feedback to the player.

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("0 for 'Rock', 1 for 'Paper', 2 for 'Scissors' Best of Luck\n"))
comp_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)
    if comp_choice == 3:
        print(scissors)
        print("computer choice:")
        print("You Win!! 😃😃")
    elif comp_choice == 2:
        print(paper)
        print("computer choice:")
        print("You Lose!! 😩😩")
    else:
        print(rock)
        print("computer choice:")
        print("Draw!! ")

elif user_choice == 1:
    print(paper)
    if comp_choice == 0:
        print(rock)
        print("computer choice:")
        print("You Win!! 😃😃")
    elif comp_choice == 3:
        print(scissors)
        print("computer choice:")
        print("You Lose!! 😩😩")
    else:
        print(paper)
        print("computer choice:")
        print("Draw!! ")

else:
    print(scissors)
    if comp_choice == 1:
        print(paper)
        print("computer choice:")
        print("You Win!! 😃😃")
    elif comp_choice == 0:
        print(rock)
        print("computer choice:")
        print("You Lose!! 😩😩")
    else:
        print(scissors)
        print("computer choice:")
        print("Draw!! ")
    





        
