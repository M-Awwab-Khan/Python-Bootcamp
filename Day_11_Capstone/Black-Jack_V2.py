import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == 0:
        return "Opponent got a BlackJack. You lose"
    elif user_score == 0:
        return "You win with a BlackJack."
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    elif user_score > computer_score:
        return "You win"
    elif user_score < computer_score:
        return "You lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while not game_over:
        if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(computer_cards) > 21 or calculate_score(user_cards) > 21:
            game_over = True

        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(
            f"Your cards {user_cards}, current score = {calculate_score(user_cards)}")
        print(f"Computer's first card : {computer_cards[0]}")

        if not game_over:
            get_or_pass = input(
                "Do you want to get card? Type 'y' to get or 'n' to pass: ")
            if get_or_pass == 'y':
                user_cards.append(deal_cards())
                user_score = calculate_score(user_cards)
            else:
                while computer_score > 0 and computer_score < 17:
                    computer_cards.append(deal_cards())
                    computer_score = calculate_score(computer_cards)
                game_over = True

    print(f"Your final hand {user_cards}, final score = {user_score}")
    print(
        f"Computer's final hand {computer_cards}, final score = {computer_score}")
    print(compare(user_score, computer_score))


while input(
        "Do you want to play a game of BlackJack. Type 'y' to play or 'n' to exit: ") == 'y':
    os.system('clear')
    play_game()
