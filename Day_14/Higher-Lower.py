from game_data import data
from art import logo, vs
import random
from os import system

score = 0
end_of_game = False


def check(user_choice):
    global end_of_game, score
    if user_choice == "a":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            system("clear")
            print(logo)
            print(f"You are right! Current Score = {score}")
            return a
        else:
            end_of_game = True
            system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final Score = {score}")
    elif user_choice == "b":
        if a["follower_count"] < b["follower_count"]:
            score += 1
            system("clear")
            print(logo)
            print(f"You are right! Current Score = {score}")
            return b
        else:
            end_of_game = True
            system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final Score = {score}")
    else:
        print("Invalid input.")


print(logo)
a = random.choice(data)
while not end_of_game:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    b = random.choice(data)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    winner = check(user_choice)
    a = winner
