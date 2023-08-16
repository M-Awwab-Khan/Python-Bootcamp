import random
from art import logo
print(logo)
print("Welcome to the number guessing game.")
print("I am thinking a number between 1 and 100.")
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 7


def set_difficulty(difficulty):
    if difficulty == "easy":
        return EASY_DIFFICULTY
    elif difficulty == "hard":
        return HARD_DIFFICULTY
    else:
        return set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))


def check_guess(guessed_number, chosen_number, attempts):
    if guessed_number > chosen_number:
        print("Too High")
        print("Guess Again")
        return attempts - 1
    elif guessed_number < chosen_number:
        print("Too Low")
        print("Guess Again")
        return attempts - 1
    else:
        print(f"You got it. The correct answer was {chosen_number}")
        return attempts


def game():
    total_attempts = set_difficulty(
        input("Choose a difficulty. Type 'easy' or 'hard': "))
    attempts_remaining = total_attempts
    chosen_number = random.randint(1, 100)
    guessed_number = 0
    print(chosen_number)
    while attempts_remaining > 0 and guessed_number != chosen_number:
        print(
            f"You have {attempts_remaining} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))

        attempts_remaining = check_guess(
            guessed_number, chosen_number, attempts_remaining)
        if attempts_remaining == 0:
            print("You've run out of guesses. You lose.")


game()
