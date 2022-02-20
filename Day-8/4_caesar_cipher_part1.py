
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


# Function to encrypt
def encrypt(plain_text, shift_amount):

    cipher_text = ""
    # Shift each letter of the 'text' forwards in the alphabet by the shift amount 
    # and print the encrypted text
    for letter in plain_text:
        position = 0
        if letter == " ":
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position >= len(alphabet):    
                new_position -= len(alphabet)
                cipher_text += alphabet[new_position]
            else:
                cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}.")

# Call the encrypt function and pass the user inputs.
encrypt(text, shift)

