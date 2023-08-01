import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choices = [rock, paper, scissors]
user_choice = choices[int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]

computer_choice = random.choice(choices)

if user_choice == computer_choice:
    print(user_choice+"\nComputer chose:\n"+computer_choice)
    print("Draw")
elif (user_choice == rock and computer_choice == paper) or (user_choice == scissors and computer_choice == rock) or (user_choice == paper and computer_choice == scissors):
    print(user_choice+"\nComputer chose:\n"+computer_choice)
    print("You lose")
else:
    print(user_choice+"\nComputer chose:\n"+computer_choice)
    print("You win!")
