alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


# Encrypt function
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

    print(f"The encoded text is {cipher_text}.")

# Decrypt function
def decrypt(cipher_text, shift_amount):
    
    plain_text = ""
    for letter in cipher_text:
        position = 0
        if letter == " ":
            decrypted_text += " "
        else:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            if new_position < 0:
                new_position = len(alphabet) + new_position
            plain_text += alphabet[new_position]

    print(f"The decoded text is {plain_text}.")

# Check to encode or decode the text
if direction == "encode":    
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift)
