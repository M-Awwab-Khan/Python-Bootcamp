from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
money_machine = MoneyMachine()
maker = CoffeeMaker()
off = False

while not off:
    choice = ""
    while choice not in menu.get_items().removesuffix('/').split('/') and choice != "off" and choice != "report":
        choice = input(
            "What would you like? (espresso/latte/cappuccino/):").lower()

    if choice == "report":
        money_machine.report()
        maker.report()
        continue
    elif choice == "off":
        off = True
    if not off:
        item = menu.find_drink(choice)
        if maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                maker.make_coffee(item)
