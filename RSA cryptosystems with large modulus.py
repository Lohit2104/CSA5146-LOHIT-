from sympy import mod_inverse

# RSA encryption function
def rsa_encrypt(m, e, n):
    return pow(m, e, n)

# RSA decryption function
def rsa_decrypt(c, d, n):
    return pow(c, d, n)

# Function to convert letter to integer (A=0, ..., Z=25)
def letter_to_int(letter):
    return ord(letter.upper()) - ord('A')

# Function to convert integer to letter (0=A, ..., 25=Z)
def int_to_letter(i):
    return chr(i + ord('A'))

# Function to perform brute-force attack
def brute_force_attack(ciphertext, e, n):
    print("\nAttempting brute-force attack...")
    possible_plaintexts = []
    
    for c in ciphertext:
        for i in range(26):  # Try all possible values from 0 to 25
            if rsa_encrypt(i, e, n) == c:
                possible_plaintexts.append(int_to_letter(i))
                break
    
    return ''.join(possible_plaintexts)

# User input for RSA parameters and plaintext
e = int(input("Enter the public exponent (e): "))
n = int(input("Enter the modulus (n): "))
plaintext = input("Enter the plaintext message (alphabetic characters only): ")

# Encrypt the plaintext
ciphertext = []
for letter in plaintext:
    m = letter_to_int(letter)
    c = rsa_encrypt(m, e, n)
    ciphertext.append(c)

# Display encrypted message
print("\nEncrypted message (as integers):")
print(ciphertext)

# Perform brute-force attack
decrypted_message = brute_force_attack(ciphertext, e, n)
print(f"\nDecrypted message using brute-force attack: {decrypted_message}")
