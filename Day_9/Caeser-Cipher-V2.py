from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punctuation = [" ", ",", ".", "/", "!", "?", "&", "|", ":", ";"]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in punctuation:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > 25 or new_position < -26:
                new_position = new_position % 26
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")
    run_again = input(
        "Do you want to the CAESAR CIPHER once again? Type yes or no: ")
    if run_again == "yes":
        user_inputs()
    else:
        print("Goodbye")


# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


def user_inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).


user_inputs()
