
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Combine the encrypt and decrypt function into a single function called caesar().
def caesar(start_text, shift_amount, caesar_direction):
    end_text = ""
    if caesar_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        # for letters in alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # for numbers/spaces/symbols , we leave these 
        else:
            end_text += char
    print(f"The {caesar_direction}d text is {end_text}.")
    
from caesar_art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

    # If user enters a number greater than length of alphabet
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, caesar_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == 'no':
        should_continue = False
        print("Goodbye")

