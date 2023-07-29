print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?: "))
bill = 0

if height >= 120:
    print("You can ride rollercoaster.")
    age = int(input("What's your age?: "))
    if age > 12:
        bill = 5
        print("Child's ticket cost $5")
    elif age <= 18:
        bill = 7
        print("Youth's ticket cost $7.")
    elif age > 18 and age < 45:
        bill = 12
        print("Adult's ticket cost $12.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Hurray! You can ride for free.")
    want_photo = input("Do you wanna photo taken? Y or N: ")
    if want_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you cannot ride rollercoaster. Please grow longer to be eligible to ride.")
