def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Ensure shift is within the range of 0-25
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    
    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift, "encrypt")
decrypted_text = caesar_cipher(encrypted_text, shift, "decrypt")

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")
