def monoalphabetic_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_map = {alphabet[i]: key[i] for i in range(26)}

    encrypted_text = ""
    for char in text.lower():
        if char in cipher_map:
            encrypted_text += cipher_map[char]
        else:
            encrypted_text += char  

    return encrypted_text


text = input("Enter the text to encrypt: ")

key = input("Enter the 26-character substitution key: ").lower()


if len(key) != 26 or not key.isalpha():
    print("Invalid key. The key must be exactly 26 alphabetic characters.")
else:
    encrypted_text = monoalphabetic_cipher(text, key)
    print("Encrypted text:", encrypted_text)
