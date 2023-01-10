# Project 4 - Rock, Paper, Scissors
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

choice_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
player = int(input("What will you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if player < 0 or player > 2:
  print("Range out of bounds. Restart game.")
else:
  print("Player chose:")
  print(f"{choice_images[player]}")
  
  computer = random.randint(0, 2)
  
  print("Computer chose:")
  print(f"{choice_images[computer]}")
  
  if player == 2 and computer == 0:
    print("You Lose :(")
  elif player > computer or (player == 0 and computer == 2):
    print("You Win!")
  elif player == computer:
    print("Draw.")
  else:
    print("You lose.")