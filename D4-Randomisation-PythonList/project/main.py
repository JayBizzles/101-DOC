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

#we are going to have the user compete against a computer

#it would be smart to put the decisions in list and choose them randomly for computer

#have to code logic for the game also ex: draws, rock wins, paper win etc

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

playerChoice = (options[player_choice])

print(playerChoice)

robotChoice = random.choice(options)

print(f"Computer chose: {robotChoice}")


if(playerChoice == robotChoice):
    print("Draw")
elif(playerChoice == rock and robotChoice == scissors):
    print("You win.")
elif(playerChoice == scissors and robotChoice == paper):
    print("You win.")
elif (playerChoice == paper and robotChoice == rock):
    print("You win.")
else:
    print("You lose.")




