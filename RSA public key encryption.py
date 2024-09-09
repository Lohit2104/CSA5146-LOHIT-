import random
import sympy

# Function to generate RSA keys
def generate_rsa_keys(bits=512):
    # Generate two large prime numbers p and q
    p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
    q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose public exponent e such that gcd(e, phi_n) = 1
    e = random.choice([65537, 3, 5, 17])  # Common choices for e
    d = pow(e, -1, phi_n)  # Calculate private key d as the modular inverse of e mod phi_n
    
    return (e, n), (d, n), p, q  # Return public key, private key, and primes

# Function to simulate leaking the private key
def simulate_leakage(p, q):
    print("\nBob leaks his private key...")
    print("Attacker can now factor n!")
    print(f"Attacker finds p = {p} and q = {q}")
    print("It is not safe to reuse the modulus n.")

# User input for RSA key generation
bits = int(input("Enter the bit length for RSA key generation (e.g., 512, 1024): "))

# Generate RSA keys
public_key, private_key, p, q = generate_rsa_keys(bits)

# Display generated keys
print(f"\nGenerated Public Key: (e={public_key[0]}, n={public_key[1]})")
print(f"Generated Private Key: (d={private_key[0]}, n={private_key[1]})")

# Simulate private key leakage
simulate_leakage(p, q)

# Ask user if they want to generate a new public/private key pair with the same modulus
decision = input("\nBob decides to generate a new public and private key with the same modulus. Is this safe? (yes/no): ")

if decision.lower() == 'no':
    print("Correct! It's not safe. Bob should generate a new modulus.")
else:
    print("Incorrect! Reusing the modulus is not safe after a private key leak.")
