def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_cipher(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    
    for i in range(len(text)):
       
        if text[i].isupper():
            x = (ord(text[i]) + ord(key[i].upper()) - 2 * ord('A')) % 26
            x += ord('A')
            encrypted_text.append(chr(x))
        elif text[i].islower():
            x = (ord(text[i]) + ord(key[i].lower()) - 2 * ord('a')) % 26
            x += ord('a')
            encrypted_text.append(chr(x))
        else:
           
            encrypted_text.append(text[i])
    
    return "".join(encrypted_text)

text = input("Enter the text to encrypt: ")
key = input("Enter the keyword: ")

encrypted_text = vigenere_cipher(text, key)

print("Encrypted text:", encrypted_text)
