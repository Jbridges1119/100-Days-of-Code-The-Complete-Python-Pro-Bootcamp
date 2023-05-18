import random
banner = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/ 
'''


# Add a card to a hand
def draw_card(hand, cards):
  hand.append(random.choice(cards))
  return hand

# Count up hand and 'account' for the aces 
def hand_total(hand):
  total = 0
  ace_count = 0
  for card_value in hand:
    if card_value == 11:
      ace_count += 1
    total += card_value

  if total > 21 and ace_count > 0:
    while ace_count > 0:
      total -= 10
      ace_count -= 1
      if total <= 21:
        return total

  return total

# run the score statements and ask player if they want to draw a card
def score_statement(your_cards, your_total, puter_cards):
  if your_total >= 21:
    return 'n'
  
  print(f"Your cards: {your_cards}, current score: {your_total}")
  print(f"Computer's first card: {puter_cards}")
  return input("Type 'y' to get another card, type 'n' to pass: ")


def blackjack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
  
  while play_blackjack == 'y':
    print(banner)
    your_cards = [random.choice(cards), random.choice(cards)]
    your_total = hand_total(your_cards)
    puter_cards = [random.choice(cards)]
    puter_total = hand_total(puter_cards)
    
    if your_total == 21:
      continue_drawing = 'n'
    else:
      continue_drawing = score_statement(your_cards, your_total, puter_cards[0])
  
    while your_total < 21 and continue_drawing == 'y':
      draw_card(your_cards, cards)
      your_total = hand_total(your_cards)
      continue_drawing = score_statement(your_cards, your_total, puter_cards[0])
    
    while puter_total < 17:
      draw_card(puter_cards, cards)
      puter_total = hand_total(puter_cards)

    print(f"Your final hand: {your_cards}, final score: {your_total}")
    print(f"Computer's final hand: {puter_cards}, final score: {puter_total}")
    
    if your_total > 21 and puter_total > 21:
      print("Everyone loses")
    elif your_total > 21 and puter_total <= 21:
      print("You lose")
    elif your_total < 21 and puter_total > 21:
      print("You win")
    elif your_total < puter_total:
      print("You lose") 
    elif your_total > puter_total:
      print("You win") 
    elif your_total == puter_total:
      print("Draw") 
      
    play_blackjack = input("Do you want to play another game of Blackjack? Type 'y' or 'n':")

blackjack()