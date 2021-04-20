import random
from art import logo

def compare(num):
  global TARGET
  if num == TARGET:
    return True
  elif num > TARGET:
    print("Too large~XD")
    return False
  else:
    print("Too small~www")
    return False

print(logo)
print('Welcome to "Guess The Number"!')
print("Yourtarget is a number between 1 and 100.")
TARGET = random.randint(1, 100)
#print(f"Pssst, the correct answer is {TARGET}")
diff = ''
atmp = 0
end = False

while diff != 'easy' and diff != 'hard':
  diff = input("Choose a difficulty. Type 'easy' or 'hard':")
  if diff == 'easy':
    atmp = 10
  elif diff == 'hard':
    atmp = 5
  else:
    print("Invalid input, please try again!") 
print("------------------------------------------------")
guess = int(input(f"You have {atmp} attemps, please start guessing: "))
end = compare(guess)
if end:
  print("Congradulations! You win~")
else:
  atmp -= 1
  while not end:
    if atmp == 0:
      end = True
      print("You've run out of attemps, game over~QAQ")
    else:
      guess = int(input(f"\nYou have {atmp} attemps left, please guess another number: "))
      end = compare(guess)
      if end:
        print("Congradulations! You win~")
      else:
        atmp -=1
