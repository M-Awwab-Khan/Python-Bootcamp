print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill? : $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
bill_per_person = (total_bill*(1+(tip_percentage/100)))/num_of_people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")