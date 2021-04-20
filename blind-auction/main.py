from replit import clear
from art import logo
print(logo)

other_user = True
winner = ""
highest_bid = 0
attendance = {}


while other_user:
  name = input("What is your name? ")
  price = input("How much would you like to bid? $")
  attendance[name] = price
  answer = input("Type \"yes\" if there is another user who wants to bid? Otherwise type \"no\".")
  if highest_bid < int(price):
    winner = name
    highest_bid = int(price)
  if answer == "no":
    other_user = False
  clear()
  
print(f"The winner is {winner}, bid price is ${attendance[winner]}.")
