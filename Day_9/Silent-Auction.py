from art import logo
from replit import clear
# HINT: You can call clear() to clear the output in the console.
end_of_auction = False
print(logo)

bidders = {}


def bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid


winner = ""
bid_of_winner = 0
while not end_of_auction:
    bid()
    any_other_bidders = input("Are there any other bidders? Type yes or no: ")
    if any_other_bidders == "yes":
        clear()
    elif any_other_bidders == "no":
        for bidder in bidders:
            if bid_of_winner < bidders[bidder]:
                bid_of_winner = bidders[bidder]
                winner = bidder
        clear()
        print(f"The winner is {winner} with the bid of ${bid_of_winner}.")
        end_of_auction = True
