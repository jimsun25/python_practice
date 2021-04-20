from art import logo, vs
from game_data import data
import random
from replit import clear
def compare(h_dic, l_dic):
  return h_dic['follower_count'] > l_dic['follower_count']



print(logo)
score = 0
end = False
a = random.choice(data)

while not end:
  b = a
  while b == a:
    b = random.choice(data)
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
  guess =  input("Who has more followers? Type 'A' or 'B': ").lower()
  while guess != 'a' and guess != 'b':
    guess =  input("Invalid input, please try again? Type 'A' or 'B': ").lower()

  if guess == 'a':
    end = compare(a, b)
  elif guess == 'b':
    end = compare(b, a)

  clear()

  if not end:
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    if guess == 'b':
      a = b

print(f"You're wrong, final score: {score}")