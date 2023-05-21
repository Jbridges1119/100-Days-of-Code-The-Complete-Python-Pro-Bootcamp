#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

EASY_GUESSES = 10
HARD_GUESSES = 5

def attempt(guesses, number):
  print(f"You have {guesses} attempts remaning to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too High.")
    return False
  elif guess < number:
    print("Too low.")
    return False
  else:
    print(f"Correct! The number was {number}")
    return True

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Invalid Input. Choose a difficulty. Type 'easy' or 'hard': ").lower() 

  if difficulty == 'easy':
    return EASY_GUESSES
  
  return HARD_GUESSES

def guess_game():
  print(''' 
            ________                            .__                   ________                       
           /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
          /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
          \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
           \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
                  \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
        ''')
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")


  guesses = set_difficulty()
  number = random.randint(1, 100)
  correct = False

  while not correct and guesses != 0:
    correct = attempt(guesses, number)
    guesses -= 1
    if guesses:
      print("Guess again.")
  
  if not correct:
    print("You ran out of attempts. Better luck next time.")


guess_game()