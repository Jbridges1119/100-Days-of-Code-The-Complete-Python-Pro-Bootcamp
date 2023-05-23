from game_data import data
from art import logo, vs
import random
import os

def question(question_one, question_two):
    print(f"Compare A: {question_one['name']}, a {question_one['description']}, from {question_one['country']}.")
    print(f"{vs}")
    print(f"Against B: {question_two['name']}, a {question_two['description']}, from {question_two['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    while choice != 'a' and choice != 'b':
      choice = input("Invalid input. Please Type 'A' or 'B': ").lower()

    return choice

def random_data(data):
  return data[random.randint(0, len(data) - 1)]


def higher_lower():
  continue_game = True
  score = 0
  question_one = random_data(data)
  question_two = random_data(data)
  
  while continue_game:
    print(f"{logo}")
    if score > 0:
      print(f"You're right! Current score: {score}.")

    while question_one == question_two:
      question_two = random_data(data)

    choice = question(question_one, question_two)
    
    a_is_greater = question_one['follower_count'] > question_two['follower_count']

    if (choice == 'a' and a_is_greater) or (choice == 'b' and not a_is_greater):
      score += 1
      if a_is_greater:
        question_two = random_data(data)
      else:
        question_one = question_two
        question_two = random_data(data)
    else:
      continue_game = False

    os.system('clear')
    
  print(f"{logo}")
  print(f"Sorry, that's wrong. Final score: {score}")

higher_lower()