#        ** Capstone Project : BlackJack Game **
import random
import os
def clear_console():
    os.system('cls')
def deal_card():
    '''Returns an random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """Take the listof cards and return the calculated score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """ Compares the users card with computer cards"""
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "lost! opponent has a blackjack!"
    elif user_score == 0:
        return "WIn with a blackjack!"
    elif user_score >21:
        return " lost! you went over."
    elif computer_score> 21:
        return " opponent went over,you Win!!"
    elif user_score>computer_score:
        return " you Win!!"
    else :
        return " you Loose!"

def play_game():    
    user_cards = []
    computer_Cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_Cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_Cards)
        print(f" your cards: {user_cards}, your score is: {user_score} ")
        print(f" computer's first card is: {computer_Cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:    
            user_should_deal = input(" Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score!=0 and computer_score < 17:
        computer_Cards.append(deal_card())
        computer_score = calculate_score(computer_Cards)

    print(f" you final hand is: {user_cards} and your final score is: {user_score}")
    print(f" you final hand is: {computer_Cards} and your final score is: {computer_score}")
    print(compare(user_score , computer_score))

while input("Do you want to play a game of bkacjack? Type 'y' or 'n' : ") == 'y':
    clear_console()
    play_game()