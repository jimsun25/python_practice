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

hand = [rock, paper, scissors]
player = int(input("Type 0 for Rock, 1 for Paper, or 2 Scissors~ "))
com = random.randint(0,2)

if player > 2 or player < 0:
  print("INPUT INVALID!!!")
else:
  print(f"\nYou choose:\n{hand[player]}")
  print(f"\nComputer choose:\n{hand[com]}")

if player == com:
  print("Tie!0.0")
else:
  if player == 0:
    if com == 1:
      print("You lose!XDDD")
    else:
      print("You win...@@")
  elif player == 1:
    if com == 2:
      print("You lose!XDDD")
    else:
      print("You win...@@")
  elif player == 2 :
    if com == 0:
      print("You lose!XDDD")
    else:
      print("You win...@@")

