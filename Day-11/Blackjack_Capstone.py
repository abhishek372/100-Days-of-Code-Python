## Blackjack Game

# Import random and os module
import random
import os

# Import logo from art 
from art import logo

# Deal card function
def deal_card():
    ''' Return a random card from the deck of cards'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# calulate score 
def calculate_score(cards):
    '''Take a list of cards and return the sum of all cards'''
    # check for blackjack (a hand of two cards: ace + 10) and return 0. 0 represent ace card in the game.
    if sum(cards)==21 and len(cards)==2:
        return 0

    # checks for 11 (ace) card. If the score is already over 21, remove 11 and replace with 1.
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    return sum(cards)

# Compare the user's score and computer's score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Adding cards to the user and computer
    for _ in range(2):
        # new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # score needs to be rechecked with every new card drawn and it continues till the game ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Print cards and score
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # Checks if the user score is over 21 or user or computer have a blackjack
        if user_score>21 or computer_score==0 or user_score==0:
            is_game_over = True

        # if the game has not ended, then ask the user to draw a card. If the user wants another card, draw a card and add
        # to the user_card list and if no, game has ended.
        else:
            # Ask user to get another card or not
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else: 
                is_game_over = True


    # Now, the user's cards is done. Computer keeps drawing the card until it's score is less than 17
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show the final cards and final score
    print(f"    Your final hand: {user_cards} and final_score: {user_score}.")
    print(f"    Computer final hand: {computer_cards} and final_score: {computer_score}.")
    
    print(compare(user_score, computer_score))


# Ask the user to play the game 
while input("Do you want to play the game? Type 'y' or 'n': ")=='y':
    os.system('cls')
    play_game()