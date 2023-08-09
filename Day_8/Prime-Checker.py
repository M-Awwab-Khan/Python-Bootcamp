import math
# Write your code below this line 👇
factors = []


def prime_checker(number):
    number_check = math.floor(math.sqrt(number))
    for i in range(2, number_check+1):
        if number % i == 0:
            factors.append(i)
    if len(factors) == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
