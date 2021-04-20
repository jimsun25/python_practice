import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

def calculate_score(card_list):
  score = sum(card_list)
  if score == 21 and len(card_list) == 2 :
    return 0
  if score > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
    score = sum(card_list)
  
  return score

def check_score():
  computer_score = calculate_score(computer_cards)
  user_score = calculate_score(user_cards) 
  if computer_score == 0 or user_score == 0:
    return True
  elif user_score > 21:
    return True

def compare(us, cs):
  if us > 21 and cs >21:
    return "You lose~"
  elif us == cs:
    return "draw"
  elif cs == 0:
    return "You lose~"
  elif us == 0:
    return "You win!"
  elif us > 21:
    return "You lose~"
  elif cs > 21:
    return "You win!"
  elif cs > us:
    return "You lose~"
  else:
    return "You win!"

play = True

while play:
  clear()
  print(logo)
  print("Game start!")
  print("_______________________________________________________________")

  user_cards = []
  computer_cards = []
  game_end = False
  computer_score = -1
  user_score = -1

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"Computer's first card: {computer_cards[0]}\n")

  game_end = check_score()

  while not game_end:
    draw = input("Type 'y' to draw another card, or 'n' to stop. ")
    if draw == 'y':
      user_cards.append(deal_card())
      print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}\n")
      game_end = check_score()
    elif draw == 'n':
      print("\n")
      game_end = True
    else:
      print("Invalid input!\n")

  user_score = calculate_score(user_cards)

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  print(compare(us = user_score, cs = computer_score))
  
  again = input("\nType 'y' to start another agame, or type anything else: ")

  if not again == 'y':
    print("\nSee you next time~") 
    play = False