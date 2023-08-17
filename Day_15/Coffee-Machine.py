from data import resources, MENU

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 3. Print report.
# 4. Check resources sufficient?
# 5. Process coins.
# 6. Check transaction successful?
# 7. Make Coffee.

money = 0


def prompt():
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print(report())
        prompt()
    elif user_choice in MENU:
        if check_resources(user_choice):
            print(ask_for_money(user_choice))
            print(make_coffee(user_choice))
            prompt()
        else:
            prompt()
    elif user_choice == "off":
        print("GoodBye.")
        return
    else:
        print("Please Enter a Valid Input")
        prompt()


def check_resources(user_choice):
    for ingredient in MENU[user_choice]["ingredients"]:
        if not resources[ingredient] >= MENU[user_choice]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"


def ask_for_money(user_choice):
    print(
        f"{user_choice.title()} costs ${MENU[user_choice]['cost']}. Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    amount_paid = round(
        (((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies)/100), 2)
    if amount_paid < MENU[user_choice]["cost"]:
        print("Sorry, that is not enough money. Money refunded.")
        prompt()
    else:
        amount_to_refund = round(amount_paid - MENU[user_choice]["cost"], 2)
        return f"Here is ${amount_to_refund} in change"


def make_coffee(user_choice):
    global resources, money
    for ingredient in MENU[user_choice]["ingredients"]:
        resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]

    money += MENU[user_choice]["cost"]
    return f"Here is your {user_choice} ☕️. Enjoy!"


prompt()
