# Function to perform Caesar Cipher encryption
def caesar_cipher(text, shift):
    encrypted_text = ""

    # Loop through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, add it as it is
        else:
            encrypted_text += char

    return encrypted_text

# Get user input for the text and the shift value
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text using Caesar Cipher
encrypted_text = caesar_cipher(text, shift)

# Display the encrypted text
print("Encrypted text:", encrypted_text)
