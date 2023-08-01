# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

complete_name = (name1 + name2).lower()
true_total = complete_name.count('t') + complete_name.count('r') + complete_name.count('u') + complete_name.count('e')
love_total = complete_name.count('l') + complete_name.count('o') + complete_name.count('v') + complete_name.count('e')

love_score = int(str(true_total) + str(love_total))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
