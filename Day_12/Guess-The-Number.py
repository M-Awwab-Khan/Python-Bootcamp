import random
from art import logo
print(logo)
print("Welcome to the number guessing game.")
print("I am thinking a number between 1 and 100.")
chosen_number = random.randint(1, 100)
guessed_number = 0
attempts = 0
difficulty = ""

while difficulty != "easy" and difficulty != "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Type a valid difficulty.")

while attempts > 0 and guessed_number != chosen_number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))

    if guessed_number > chosen_number:
        print("Too High")
        print("Guess Again")
        attempts -= 1
    elif guessed_number < chosen_number:
        print("Too Low")
        print("Guess Again")
        attempts -= 1
    else:
        print(f"You got it. The correct answer was {chosen_number}")
